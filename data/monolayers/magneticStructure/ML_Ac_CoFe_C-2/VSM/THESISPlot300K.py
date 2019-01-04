import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS
from modelexp.data import XyeData

chapter = 'monolayer'
sample_name = 'ML_Ac_CoFe_C_2star'
sample_label = 'ML-Ac-CoFe-C-2'
savefile = f'{chapter}_PPMS_VSM_300K_{sample_name}'

datfile = './rescale/ML-Ac-CoFe-C-2star_300K_LangevinSAXSscaled.xye'
label = '300 K'
fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)

data = XyeData()
data.loadFromFile(datfile)
B, M, sM = data.getData()
ax.plot(B, M, linestyle='None', marker='.', markersize=1, zorder=2, alpha=0.5,
  label=label)

ax.text(0.99, 0.05, sample_label,
  verticalalignment='bottom',
  horizontalalignment='right',
  transform=ax.transAxes)

ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel("$\mathit{M} \, / \, kAm^{-1}$")
ax.set_xlim(-9.2, 9.2)
ax.set_ylim(-590, 590)
ax.legend(loc='upper left')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)

