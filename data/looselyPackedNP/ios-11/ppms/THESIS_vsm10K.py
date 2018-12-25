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

from modelexp.data import XyeData

datfile10 = cwd+ '/data_rescaling/PMK18_10K_LangevinSAXSscaled.xye'
datfile300 = cwd+ '/data_rescaling/PMK18_300K_LangevinSAXSscaled.xye'

chapter = 'looselyPackedNP'
sample_name = 'IOS-11'

savefile = chapter + '_VSM_10K_' + sample_name

data = XyeData()
data.loadFromFile(datfile10)
B, M, sM = data.getData()

data = XyeData()
data.loadFromFile(datfile300)
B_300, M_300, sM_300 = data.getData()

min_B, max_B = -0.3, 0.3
min_M, max_M = -250, 250
T = 10

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
# ax.plot(B_300, M_300, linestyle='None', marker='.', zorder=0, alpha=0.2)
ax.plot(B, M, linestyle='None', marker='.', zorder=1,\
            label='IOS-11\n$\mathit{T} \,=\, ' + str(T) + ' \,K$')
# ax.text(0.51, 0.05,
#   'IOS-11\n'
#   '$\mathit{M_s} \, = \,  191.5(2) kA m^{-1}$\n'+
#   '$\mathit{\mu} \, = \,  11350(60) \mathit{\mu}_B$\n'+
#   '$\mathit{\mu_0 \chi} \, = \, 2.8(4) \cdot 10^{-4}$',
#   horizontalalignment='left',
#   verticalalignment='bottom',
#   transform=ax.transAxes,
#   fontsize=9)
ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")
ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
ax.legend(loc='upper left')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)