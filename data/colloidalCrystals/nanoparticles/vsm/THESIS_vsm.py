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

from modelexp.data import XyemData, MultiData

datfile_initial = './postSynthesis/fit_result.dat'
datfile_postOxidation = './postOxidationStep/fit_result.dat'

chapter = 'colloidalCrystals'
sample_name = 'Ol_Fe_C_compare'

savefile = chapter + '_VSM_' + sample_name

data = XyemData()
data.loadFromFile(datfile_initial)
B_init, M_init, sM_init, Mmodel_init = data.getData()

data = XyemData()
data.loadFromFile(datfile_postOxidation)
B_pOxi, M_pOxi, sM_pOxi, Mmodel_pOxi = data.getData()


min_B, max_B = -1.99, 1.99
min_M, max_M = -550, 550
T = 296

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(B_init, M_init, sM_init, linestyle='None', marker='.',
  markersize=1, zorder=1, capsize=0)
ax.errorbar(B_pOxi, M_pOxi, sM_pOxi, linestyle='None', marker='.',
  markersize=1, zorder=1, capsize=0)

ax.plot(B_init, Mmodel_init, marker='None', zorder=2, color='black', alpha=0.5)
ax.plot(B_pOxi, Mmodel_pOxi, marker='None', zorder=2, color='black', alpha=0.5)


ax.text(0.95,0.02,'Ol-Fe-C\n$\mathit{T}$ = 296 K',
  transform=ax.transAxes,
  horizontalalignment='right',
  verticalalignment='bottom')

ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")

ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)