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

from modelexp.data import XyemData

datfile = 'fit_result.dat'

chapter = 'looselyPackedNP'
sample_name = 'IOS-7'

savefile = chapter + '_VSM_' + sample_name

data = XyemData()
data.loadFromFile(datfile)
B, M, sM, Mmodel = data.getData()

min_B, max_B = min(B), max(B)
min_M, max_M = -210, 210
T = 298

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(B, M, sM, linestyle='None', marker='.', zorder=1,\
            label='VSM\n$\mathit{T} \,=\, ' + str(T) + ' \,K$', capsize=0)
ax.plot(B, Mmodel, marker='None', zorder=2, color='black')
ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")

ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
ax.legend(loc='upper left')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)
