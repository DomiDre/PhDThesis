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


chapter = 'monolayer'
sample_name = 'ML_Ac_CoFe_C'
savefile = f'{chapter}_PPMS_VSM_10KCompareDispersion_{sample_name}'

datfile = './rescale/ML_Ac_CoFe_C_10K_rescaled.xye'
dispfile = './DispersionDry/Ac_CoFe_C_Dispersion_10K_LangevinSAXSscaled.xye'
waferfile = './DispersionDry/Ac_CoFe_C_DisorderedWafer_10K_LangevinSAXSscaled.xye'

Ms = 410

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)

data = XyeData()
data.loadFromFile(datfile)
B, M, sM = data.getData()
ax.errorbar(B, M*1.13/Ms, sM*1.13/Ms, linestyle='None', marker='.', markersize=1, capsize=0, zorder=1, label='ML-Ac-CoFe-C')
data = XyeData()
data.loadFromFile(waferfile)
B, M, sM = data.getData()
ax.errorbar(B, M/Ms, sM/Ms, linestyle='None', marker='.', markersize=1, capsize=0, zorder=1, label='Disordered ML')
data = XyeData()
data.loadFromFile(dispfile)
B, M, sM = data.getData()
ax.errorbar(B, M/Ms, sM/Ms, linestyle='None', marker='.', markersize=1, capsize=0, zorder=1, label='Dispersion')

ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel(r"$\mathit{M} \, / \, M_s$")

ax.text(0.95,0.02,'$\mathit{T}$ = 10 K',
  transform=ax.transAxes,
  horizontalalignment='right',
  verticalalignment='bottom')

ax.set_xlim(-8.9, 8.9)
ax.set_ylim(-1.3, 1.3)
ax.legend(loc='upper left', bbox_to_anchor=[-0.05, 1.03], handletextpad=0, fontsize=11)
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)