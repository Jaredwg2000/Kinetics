"""Takes concentration over time data and plots it."""

import numpy as np
import matplotlib.pyplot as plt

d = np.loadtxt("Part2-2D.dat", unpack=True)

t, a, b, p, q, x, y, z = d

t1 = t[::5]
x1 = x[::5]
y1 = y[::5]
z1 = z[::5]

t2 = t[1::5]
x2 = x[1::5]
y2 = y[1::5]
z2 = z[1::5]

t3 = t[2::5]
x3 = x[2::5]
y3 = y[2::5]
z3 = z[2::5]

t4 = t[3::5]
x4 = x[3::5]
y4 = y[3::5]
z4 = z[3::5]

t5 = t[4::5]
x5 = x[4::5]
y5 = y[4::5]
z5 = z[4::5]

# plt.plot(t1, x1, color="midnightblue", label="[X1]")
# plt.plot(t2, x2, color="navy", label="[X2]")
# plt.plot(t3, x3, color="darkblue", label="[X3]")
# plt.plot(t4, x4, color="mediumblue", label="[X4]")
# plt.plot(t5, x5, color="blue", label="[X5]")

# plt.plot(t1, y1, color="darkred", label="[Y1]")
# plt.plot(t2, y2, color="firebrick", label="[Y2]")
# plt.plot(t3, y3, color="red", label="[Y3]")
# plt.plot(t4, y4, color="indianred", label="[Y4]")
# plt.plot(t5, y5, color="lightcoral", label="[Y5]")

plt.plot(t1, z1, color="black", label="[Z1]")
plt.plot(t2, z2, color="dimgray", label="[Z2]")
plt.plot(t3, z3, color="gray", label="[Z3]")
plt.plot(t4, z4, color="darkgray", label="[Z4]")
plt.plot(t5, z5, color="lightgray", label="[Z5]")

plt.legend()
plt.title("Oscillatory reaction: Concentrations over time")
plt.xlabel("t / s")
plt.ylabel("[Species] / M")
plt.yscale("log")
plt.xlim(0, 100)
# plt.ylim(1e-14, 1e-2)
plt.grid()
plt.show()
