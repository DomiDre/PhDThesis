#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:48:40.453330
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np

from modelexp.data import XyeData, XyemData, MultiData

datfile_disp = './rescale/Ac_CoFe_C_Dispersion_10K_LangevinSAXSscaled.xye'
datfile_dry = './rescale/Ac_CoFe_C_DisorderedWafer_10K_LangevinSAXSscaled.xye'

chapter = 'monolayer'
sample_name = 'Ac_CoFe_C'

savefile = chapter + '_VSM_10K_' + sample_name + '_2'

data = XyeData()
data.loadFromFile(datfile_disp)
B_disp, M_disp, sM_disp = data.getData()

data = XyeData()
data.loadFromFile(datfile_dry)
B_dry, M_dry, sM_dry = data.getData()

min_B, max_B = -8.9, 8.9
min_M, max_M = -450, 450
T = 10

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(B_disp, M_disp, sM_disp, linestyle='None', marker='.', markersize=1, zorder=1,\
            label='Dispersion', capsize=0)
ax.errorbar(B_dry, M_dry, sM_dry, linestyle='None', marker='.', markersize=1, zorder=2,\
            label='Dry', capsize=0, alpha=0.2)

ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")

ax.text(0.95,0.02,'Ac-CoFe-C\n$\mathit{T}$ = 10 K',
  transform=ax.transAxes,
  horizontalalignment='right',
  verticalalignment='bottom')

ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
ax.legend(loc='upper left', bbox_to_anchor=[-0.05, 1.03])
plt.savefig(cwd + '/' + savefile)