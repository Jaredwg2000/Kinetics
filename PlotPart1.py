"""Takes equilibrium concentration data and plots it."""

import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt("Part1.dat", unpack=True)

Urea, ConcD, ConcI, ConcN = d

plt.plot(Urea, ConcD, color="black", label="[D]")
plt.plot(Urea, ConcI, color="red", label="[I]")
plt.plot(Urea, ConcN, color="blue", label="[N]")

plt.legend()
plt.title("Variation of equilibrium concentration of D, I, and N with \n" +
          "changing Urea concentration")
plt.xlabel("[Urea] / M")
plt.ylabel("[Species] / M")

plt.show()
