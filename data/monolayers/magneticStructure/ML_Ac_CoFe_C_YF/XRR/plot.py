import numpy as np
import matplotlib.pyplot as plt
import sys
import matplotlib
matplotlib.rcParams.update({'font.size': 18})

def load_xye(xyefile):
    rawdata = np.genfromtxt(xyefile)
    x = rawdata[:,0]
    y = rawdata[:,1]
    sy = rawdata[:,2]
    return x, y, sy


q, I, sI = load_xye('DD175_28.xye')

x0, y0 = 0.21, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure(figsize=(4.5, 4.5))
ax = fig.add_axes([x0, y0, width, height])

ax.errorbar(q, I, sI, label='XRR @ D8', color='#fdae61')
ax.set_yscale('log')
ax.set_xlabel('$\mathit{q} \, / \, \AA^{-1}$')
ax.set_ylabel('$\mathit{R}$')
ax.set_xlim(0.007, 0.31)
ax.set_ylim(1e-6, 1.4e0)
ax.legend()
fig.savefig('XRR_DD175_28.png')
plt.show()