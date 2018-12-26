import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
chapter = 'doubleLayers'
savefile = chapter+'_XRR_compareThickness'

def load_xye(xyefile):
  rawdata = np.genfromtxt(xyefile)
  x = rawdata[:,0]
  y = rawdata[:,1]
  sy = rawdata[:,2]
  return x, y, sy


q_1, I_1, sI_1 = load_xye('../dl_0-125/xrr/DD213_7.xye')
q_2, I_2, sI_2 = load_xye('../dl_0-25/xrr/DD205_10.xye')
q_3, I_3, sI_3 = load_xye('../dl_1-25/xrr/DD205_3.xye')
q_4, I_4, sI_4 = load_xye('../dl_2-5/xrr/DD205_5.xye')
q_5, I_5, sI_5 = load_xye('../dl_5/xrr/DD205_6.xye')

left, bottom = 0.19, 0.17
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

# ax.errorbar(q_1, I_1, sI_1, marker='None', label='DL-1.25%')
# ax.errorbar(q_2, I_2*0.1, sI_2*0.1, marker='None', label='DL-1.25%-2')
ax.plot(q_1, I_1*1e4, alpha=0.8, marker='None', label='DL-0.125%')
ax.plot(q_2, I_2*1e3, alpha=0.8, marker='None', label='DL-0.25%')
ax.plot(q_3, I_3*1e2, alpha=0.8, marker='None', label='DL-1.25%')
ax.plot(q_4, I_4*1e1, alpha=0.8, marker='None', label='DL-2.5%')
ax.plot(q_5, I_5,     alpha=0.8, marker='None', label='DL-5%')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('$\mathit{q_z} \, / \, \AA^{-1}$')
ax.set_ylabel('$\mathit{R}$')
ax.set_xlim(0.007, 0.31)
ax.set_ylim(5e-7, 2.5e4)
ax.legend(loc='lower left', fontsize=10)

fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')