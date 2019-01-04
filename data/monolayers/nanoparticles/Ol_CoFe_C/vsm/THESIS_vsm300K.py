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


paramfile_disp = './FitsOfRescaledData/Dispersion300K/fit_result.dat'
paramfile_wafer = './FitsOfRescaledData/DisorderedWafer300K/fit_result.dat'

chapter = 'monolayer'
sample_name = 'Ol_CoFe_C'

savefile = chapter + '_VSM_300K_' + sample_name

fitData = MultiData(XyemData)
fitData.loadFromFile(paramfile_disp)
B_disp, M_disp, sM_disp, Mmodel_disp = fitData.getDataset(0).getData()

fitData = MultiData(XyemData)
fitData.loadFromFile(paramfile_wafer)
B_wafer, M_wafer, sM_wafer, Mmodel_wafer = fitData.getDataset(0).getData()

min_B, max_B = -2.2, 2.2
min_M, max_M = -155, 155
T = 300

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(B_disp, M_disp, sM_disp, linestyle='None', marker='.', markersize=1,
  zorder=1, label='Dispersion', capsize=0)
ax.errorbar(B_wafer, M_wafer, sM_wafer, linestyle='None', marker='.', markersize=1,
  zorder=2, label='Dry', capsize=0, alpha=0.2)
ax.plot(B_disp, Mmodel_disp, marker='None', zorder=2, color='black')

ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")

ax.text(0.95,0.02,'Ol-CoFe-C\n$\mathit{T}$ = 300 K',
  transform=ax.transAxes,
  horizontalalignment='right',
  verticalalignment='bottom')

ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
ax.legend(loc='upper left', bbox_to_anchor=[-0.05, 1.03])
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)