import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS
from modelexp.data import XyeData
import fortMag

chapter = 'doublelayers'
sample_name = 'DL_0-25'
savefile = f'{chapter}_PPMS_VSM_300K_{sample_name}'

datfile = './rescale/DL_0-25_300K_rescaled.xye'


fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)

data = XyeData()
data.loadFromFile(datfile)
B, M, sM = data.getData()
ax.errorbar(B, M, sM, linestyle='None', marker='.', markersize=1, zorder=1)

Ms = 298.496840
mu = 23400
dispersion_M = fortMag.langevin.magnetization(B, Ms, mu, 300, 0)
ax.plot(B, dispersion_M, linestyle='-', marker='None', color='black', zorder=2, alpha=0.5)

ax.text(0.02,0.98,'DL-0.25%\n$\mathit{T}$ = 300 K',
  transform=ax.transAxes,
  horizontalalignment='left',
  verticalalignment='top')

ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel("$\mathit{M} \, / \, kAm^{-1}$")
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-450, 450)
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)

