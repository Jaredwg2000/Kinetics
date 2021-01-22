"""Program to simulate reactions.

Outputs a data file containing either concentrations at equilibrium,
or concentrations over time as a reaction proceeds.
"""
from math import e


class Reaction:
    """Class containing information about each reaction.

    Variables:
        reactants - list of strings refering to the species
        products - list of string refering to the species
        rates - list of ints giving the forward and back rate constants

    Methods:
        getChanges - works out the concentration changes caused by this
                    reaction in the reactants and products. Takes the
                    species list as input.
    """

    def __init__(self, reactants, products, rates):
        """Initialize a reaction class.

        Takes the inputs from calling the class and puts them into
        local variables.
        """
        self.reactants = reactants
        self.products = products
        self.rates = rates

    def getChanges(self, species):
        """Calculate the change in concentration over a timestep.

        Takes the species list and changes the "changes" index so as to
        perform a timestep without changing the concentrations. The
        concentrations are then updated later.
        """
        change1 = 1.0
        change2 = -1.0

        # For each reactant, multiply their concentrations
        for i in self.reactants:
            for s in species:
                if(s["Name"] == i):
                    change1 *= s["Conc"]

        # Then multiply by the rate of the forward reaction
        change1 *= self.rates[0]

        # Repeat for products and the backwards rate
        for i in self.products:
            for s in species:
                if(s["Name"] == i):
                    change2 *= s["Conc"]

        change2 *= self.rates[1]

        # Output the sum. This is the rate of change for all species in the
        # reaction. Sum because we start with +1 and -1.
        return (change1 + change2)


class Cell:
    """Class containing the reaction objects.

    Variables:
        reactions - a list of all of the reaction objects
        x; y - a pair of ints giving the position of the cell (not needed
                when only using 1 cell, but left in for generality)

        Methods:
            timeStep - advances the time of the simulation
    """

    def __init__(self, reactions, x, y):
        """Initialize a reaction class.

        Takes the inputs from calling the class and puts them into
        local variables.
        """
        self.reactions = reactions

        # I put this in with foresight to the extension task.
        # I had a go at it, but ran into some issues with my way of
        # tracking species concentrations. I was trying to make a
        # ndarray of lists, but that doesn't really work.
        # Maybe the way to do it would be a list of ndarrays, one for each
        # species in the system.
        self.x = x
        self.y = y

    def timeStep(self, species, step):
        """Perform a timestep of the reaction."""
        # Loop over every reaction, find the changes for each.
        for rxn in self.reactions:
            change = rxn.getChanges(species)

            # For a reaction, the change for any species is the change
            # for that reaction. Positive for reactants, negatvie for
            # products.
            for i in rxn.reactants:
                for s in species:
                    if(s["Name"] == i):
                        s["Change"] -= change
            for i in rxn.products:
                for s in species:
                    if(s["Name"] == i):
                        s["Change"] += change

        # After all changes are calculated, change the concentrations.
        for s in species:
            s["Conc"] += s["Change"] * step
            if(s["Conc"] < 0):
                s["Conc"] = 0


def Converge(rxnVessel, species):
    """Find equilibrium concentrations."""
    dT = 10e-6
    timeElapsed = 0
    converged = False

    while not converged:
        converged = True
        ReactionVessel.timeStep(species, dT)
        timeElapsed += dT

        # Work out if the concentrations have converged to eqbm.
        for s in species:
            if(s["Change"] > 10e-6):
                converged = False
            # Reset the changes.
            s["Change"] = 0

    # Output the changed concentrations.
    return species


def TimeEvolve(rxnVessel, species):
    """Find concentrations over time."""
    dT = 1e-6
    timeElapsed = 0
    i = 0

    # Instead of waiting for convergence, set a time limit.
    while(timeElapsed < 100):
        ReactionVessel.timeStep(species, dT)
        timeElapsed += dT
        # Reset the changes. Can do this immediately as we don't need them.
        for s in species:
            s["Change"] = 0

        # Output something at regular intervals. Using i here instead of
        # timeElapsed due to some floating point errors. Seemed the easiest
        # way to get around the problem.
        if(i % 1e6 == 0):
            with open("Part2.dat", "a") as f:
                f.write(str(timeElapsed) + "\t")
                for s in species:
                    f.write(str(s["Conc"]) + "\t")
                f.write("\n")
        i += 1


species = []
Reactions = []

# Ask the user what they want to do
print("Part 1 or 2?")
answer = int(input())

if(answer == 1):
    # I got bored of typing this in every time I ran a test, so hard-coded
    # the inputs for the first task.
    species = [{"Name": "D", "Conc": 0.5, "Change": 0.0},
               {"Name": "I", "Conc": 0.0, "Change": 0.0},
               {"Name": "N", "Conc": 0.5, "Change": 0.0}]
    react1 = ["D"]
    prod1 = ["I"]
    react2 = ["I"]
    prod2 = ["N"]

    # Write the header line to the data file.
    with open("Part1.dat", "w") as f:
        f.write("# [Urea] \t [D] \t [I] \t [N] \n")

    # Scale which determines how many data points I get between integer values
    # of [Urea].
    scale = 20

    # Loop over the different rates, run the reaction to eqbm and record the
    # results.
    for i in range(0, 8*scale):
        rate1 = [26000.0*pow(e, -1.68*i/scale), 6e-2*pow(e, 0.95*i/scale)]
        rate2 = [730.0*pow(e, -1.72*i/scale), 7.5e-4*pow(e, 1.2*i/scale)]
        Reactions = (Reaction(react1, prod1, rate1),
                     Reaction(react2, prod2, rate2))
        ReactionVessel = Cell(Reactions, 0, 0)
        species = Converge(ReactionVessel, species)

        # Write the data. This is different from part 2, as we only care
        # about eqbm concentations here. Part 2 writes to the data file
        # in the function it calls at regular time intervals.
        with open("Part1.dat", "a") as f:
            f.write(str(i/scale) + "\t" + str(species[0]["Conc"]) + "\t" +
                    str(species[1]["Conc"]) + "\t" +
                    str(species[2]["Conc"]) + "\n")
elif(answer == 2):
    # This lets the user input a general reaction system. I am quite happy
    # with this...

    # Number of species
    print("How many distinct species in total?")
    noSpecies = int(input())

    # Species names and concentrations
    for i in range(noSpecies):
        print("Species " + str(i+1) + " name:")
        speciesName = input()
        print("Species " + str(i+1) + " initital concentration:")
        speciesConc = input()
        species.append({"Name": speciesName, "Conc": float(speciesConc),
                        "Change": 0.0})

    # Reactions
    print("How many pairs of reactions (forward + back)?")
    noRxn = int(input())

    # Loop over each reaction
    for i in range(noRxn):
        reactants = []
        products = []
        rates = []

        # Number of reactants and products
        print("How many moles of reactants in reaction " + str(i+1) + "?")
        noMolesReact = int(input())

        print("How many moles of products in reaction " + str(i+1) + "?")
        noMolesProd = int(input())

        print("If a species is present in multiple moles, input " +
              "it that many times below.")
        # Names of the products and reactants
        for j in range(noMolesReact):
            print("Name of reactant mole " + str(j+1) + ":")
            reactants.append(input())
        for j in range(noMolesProd):
            print("Name of product mole " + str(j+1) + ":")
            products.append(input())

        # Rates of forward and back reactions
        print("Rate of forward reaction:")
        rates.append(float(input()))
        print("Rate of back reaction (0 if none):")
        rates.append(float(input()))

        Reactions.append(Reaction(reactants, products, rates))

    ReactionVessel = Cell(Reactions, 0, 0)

    # Header line for the data file.
    with open("Part2.dat", "w") as f:
        f.write("# t \t")
    with open("Part2.dat", "a") as f:
        for s in species:
            f.write("[" + s["Name"] + "] \t")
        f.write("\n")

    TimeEvolve(ReactionVessel, species)