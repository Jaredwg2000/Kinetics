# Kinetics
Calculates time evolutions of chemical equilibria

The user can follow the instructions given in the console to input the data required.
The program will output to datafiles to store the concentration data, either at equilibrium or over time.

The inputs for the first task are hard-coded, but for the second task any system can be used as input.

To see the plots, either use PlotPart1.py, to see the graph produced for task 1 (protein folding), or
PlotPart2.py, to see the graph for the second task. The captions used assume that the system being used
is the system from the course guide, but these could be in priciple changed quite easily - this could be made into
a runtime thing, with the user specifying the legend.

Running the second task takes a while, particularly if it is run in 2D. I have tested it for a 1x5 system which took
~3 hours to run each time. The method I am using to plot would not really work for a properly 2D system (e.g. 3x3)
because it plotted as concentration vs time. This could be fixed with a 2D plot of x and y (which would have to be
added to the output) which is animated, with each frame being a new moment in time, and colour corresponding to
concentration.
