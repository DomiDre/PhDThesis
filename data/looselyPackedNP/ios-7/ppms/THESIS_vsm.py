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

datfile = cwd + '/calcLangevinModel/fit_result.dat'

chapter = 'looselyPackedNP'
sample_name = 'IOS-7'

savefile = chapter + '_VSM_' + sample_name

data = XyemData()
data.loadFromFile(datfile)
B, M, sM, Mmodel = data.getData()

min_B, max_B = -9.01, 9.01
min_M, max_M = -250, 250
T = 300

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_inset = fig.add_axes([0.7,bottom+0.1, 0.25, 0.3])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(B, M, sM, linestyle='None', marker='.', zorder=1,\
            label='IOS-7\n$\mathit{T} \,=\, ' + str(T) + ' \,K$', capsize=0)
ax.plot(B, Mmodel, marker='None', zorder=2, color='black')

ax_inset.axhline(0, color='lightgray', marker='None', zorder=0)
ax_inset.axvline(0, color='lightgray', marker='None', zorder=0)
ax_inset.errorbar(B, M, sM, linestyle='None', marker='.', zorder=1,\
            label='IOS-11\n$\mathit{T} \,=\, ' + str(T) + ' \,K$', capsize=0)
ax_inset.plot(B, Mmodel, marker='None', zorder=2, color='black')
ax_inset.set_xlim(-0.1, 0.1)
ax_inset.set_ylim(-90, 90)
ax_inset.tick_params(axis='both', which='major', labelsize=8)
ax_inset.tick_params(axis='both', which='minor', labelsize=8)
# ax.text(0.51, 0.05,
#   'IOS-7\n'
#   '$\mathit{M_s} \, = \,  212.5(1) kA m^{-1}$\n'+
#   '$\mathit{\mu} \, = \,  3609(8) \mathit{\mu}_B$\n'+
#   '$\mathit{\mu_0 \chi} \, = \, -0.0132(1)$',
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
