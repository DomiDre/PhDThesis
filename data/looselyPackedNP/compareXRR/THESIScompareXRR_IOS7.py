import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
chapter = 'looselyPackedNP'
savefile = chapter+'_BilayersXRR_compareIOS7'

def load_xye(xyefile):
  rawdata = np.genfromtxt(xyefile)
  x = rawdata[:,0]
  y = rawdata[:,1]
  sy = rawdata[:,2]
  return x*10, y, sy


q_1, I_1, sI_1 = load_xye('../8bl-15-ios-7/xrr/ES-S15.xye')
q_2, I_2, sI_2 = load_xye('../8bl-30-ios-7/xrr/ES-S16.xye')

left, bottom = 0.19, 0.17
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.plot(q_1, I_1*1e1, alpha=0.8, marker='None', label='8BL-15-IOS-7')
ax.plot(q_2, I_2*1, alpha=0.8, marker='None', label='8BL-30-IOS-7')
# ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('$\mathit{q_z} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{R}$')
ax.set_xlim(0.20, 1.7)
ax.set_ylim(5e-7, 2.5e1)
ax.legend(loc='upper right', fontsize=10)

fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')