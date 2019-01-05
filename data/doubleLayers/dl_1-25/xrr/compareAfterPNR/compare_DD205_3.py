import numpy as np
import matplotlib.pyplot as plt
import sys

def load_xye(xyefile):
    rawdata = np.genfromtxt(xyefile)
    x = rawdata[:,0]
    y = rawdata[:,1]
    sy = rawdata[:,2]
    return x, y, sy


q_dd205_3, I_dd205_3, sI_dd205_3 = load_xye('DD205_3.xye')
q_dd205_3second, I_dd205_3second, sI_dd205_3second = load_xye('DD205_3_halfPieceAfterPNR.xye')

fig, ax = plt.subplots()
ax.errorbar(q_dd205_3, I_dd205_3, sI_dd205_3, label='DD205.3 1st')
ax.errorbar(q_dd205_3second, I_dd205_3second, sI_dd205_3second, label='DD205.3 2nd')

ax.set_yscale('log')
ax.set_xlabel('$\mathit{q} \, / \, \AA^{-1}$')
ax.set_ylabel('$\mathit{R}$')
ax.set_xlim(0.007, 0.21)
ax.set_ylim(1e-6, 1.2e0)
ax.legend().draw_frame(True)
fig.savefig('Compare_DD205_3.png')
plt.show()