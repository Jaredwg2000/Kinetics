"""Takes concentration over time data and plots it."""

import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt("Part2.dat", unpack=True)

t, a, b, p, q, x, y, z = d

plt.plot(t, x, color="black", label="[X]")
plt.plot(t, y, color="red", label="[Y]")
plt.plot(t, z, color="blue", label="[Z]")

plt.legend()
plt.title("Oscillatory reaction: Concentrations over time")
plt.xlabel("t / s")
plt.ylabel("[Species] / M")
plt.yscale("log")
plt.xlim(0, 100)
plt.grid()
plt.show()
