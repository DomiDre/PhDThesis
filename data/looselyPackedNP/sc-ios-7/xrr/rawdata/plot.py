import numpy as np
import matplotlib.pyplot as plt
import sys

def load_xye(xyefile):
    rawdata = np.genfromtxt(xyefile)
    x = rawdata[:,0]
    y = rawdata[:,1]
    sy = rawdata[:,2]
    return x, y, sy


q, I, sI = load_xye('ES-S17.xye')

fig, ax = plt.subplots()
ax.errorbar(q, I, sI)
ax.set_yscale('log')
ax.set_xlabel('$\mathit{q} \, / \, \AA^{-1}$')
ax.set_ylabel('$\mathit{R}$')
ax.set_xlim(min(q), None)
# ax.set_ylim(1e-6, 1.2e0)
fig.savefig('XRR_ES-S17.png')
plt.show()