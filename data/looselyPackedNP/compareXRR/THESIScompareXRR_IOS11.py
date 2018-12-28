import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
chapter = 'looselyPackedNP'
savefile = chapter+'_BilayersXRR_compareIOS11'

def load_xye(xyefile):
  rawdata = np.genfromtxt(xyefile)
  x = rawdata[:,0]
  y = rawdata[:,1]
  sy = rawdata[:,2]
  return x*10, y, sy


q_3, I_3, sI_3 = load_xye('../8bl-15-ios-11/xrr/ES-S12.xye')
q_4, I_4, sI_4 = load_xye('../8bl-40-ios-11/xrr/ES-S13.xye')

left, bottom = 0.19, 0.17
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.plot(q_3, I_3*10, alpha=0.8, marker='None', label='8BL-15-IOS-11')
ax.plot(q_4, I_4,     alpha=0.8, marker='None', label='8BL-40-IOS-11')
# ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('$\mathit{q_z} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{R}$')
ax.set_xlim(0.20, 1.7)
ax.set_ylim(5e-7, 2.5e1)
ax.legend(loc='upper right', fontsize=10)

fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')
plt.show()