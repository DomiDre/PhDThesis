import matplotlib.pyplot as plt
import numpy as np


mu = np.array([1,0,0])


w = 5
Y, X = np.mgrid[-w:w:100j, -w:w:100j]
R = np.sqrt(X**2 + Y**2)
U = (3*X**2 - R**2)/R**5
V = 3*Y*X/R**5
speed = np.sqrt(U*U + V*V)


fig, ax = plt.subplots()

#  Varying line width along a streamline
lw = 5*speed / speed.max()
ax.streamplot(X, Y, U, V, density=[0.5, 1])
plt.show()