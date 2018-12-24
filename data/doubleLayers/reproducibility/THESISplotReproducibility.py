import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
chapter = 'doubleLayers'
savefile = chapter+'_XRR_reproducibility'

def load_xye(xyefile):
  rawdata = np.genfromtxt(xyefile)
  x = rawdata[:,0]
  y = rawdata[:,1]
  sy = rawdata[:,2]
  return x, y, sy


q_1, I_1, sI_1 = load_xye('../dl_1-25/xrr/DD205_3.xye')
q_2, I_2, sI_2 = load_xye('../dl_1-25-2/xrr/DD205_12.xye')

left, bottom = 0.19, 0.17
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

# ax.errorbar(q_1, I_1, sI_1, marker='None', label='DL-1.25%')
# ax.errorbar(q_2, I_2*0.1, sI_2*0.1, marker='None', label='DL-1.25%-2')
ax.plot(q_1, I_1,   alpha=0.8, marker='None', label='DL-1.25%')
ax.plot(q_2, I_2*2, alpha=0.8, marker='None', label='$10 \cdot$ DL-1.25%-2')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('$\mathit{q_z} \, / \, \AA^{-1}$')
ax.set_ylabel('$\mathit{R}$')
ax.set_xlim(0.007, 0.41)
ax.set_ylim(1e-6, 2.9e0)
ax.legend(loc='lower left')

fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')