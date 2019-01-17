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

datfile = 'fit_result.dat'

chapter = 'colloidalCrystals'
sample_name = 'Ol_Fe_C-oxidized'

savefile = chapter + '_VSM_' + sample_name

data = XyemData()
data.loadFromFile(datfile)
B, M, sM, Mmodel = data.getData()

fitData = MultiData(XyemData)
fitData.loadFromFile(datfile)
fit_params = fitData.params

min_B, max_B = min(B), max(B)
min_M, max_M = -990, 990
T = 295

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(B, M, sM, linestyle='None', marker='.', zorder=1, capsize=0)
ax.plot(B, Mmodel, marker='None', zorder=2, color='black')


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