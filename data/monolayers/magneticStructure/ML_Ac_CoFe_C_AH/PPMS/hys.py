import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS
from modelexp.data import XyeData

chapter = 'monolayer'
sample_name = 'ML_Ac_CoFe_C'
savefile = f'{chapter}_PPMS_VSM_multiTemps_{sample_name}'

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)

def plot(datfile, label):
  data = XyeData()
  data.loadFromFile(datfile)
  B, M, sM = data.getData()
  ax.plot(B, M, linestyle='None', marker='.', markersize=1, zorder=2, alpha=0.5,
    label=label)

for temp in [10, 100, 150, 200]:
  plot(f'dd205_4_{temp}K_rescaled.dat', f'{temp} K')

ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel("$\mathit{M} \, / \, kAm^{-1}$")
ax.set_xlim(-9.2, 9.2)
ax.set_ylim(-450, 450)
ax.legend(loc='upper left')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)

