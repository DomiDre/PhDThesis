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

datfile30_zfc = cwd+ '/data_rescaling/IOS-7_Dispersion_ZFC_30K_LangevinSAXSscaled.xye'
datfile30_fc = cwd+ '/data_rescaling/IOS-7_Dispersion_FC_30K_LangevinSAXSscaled.xye'

chapter = 'looselyPackedNP'
sample_name = 'IOS-7'

savefile = chapter + '_VSM_30K_' + sample_name

data = XyeData()
data.loadFromFile(datfile30_zfc, sort=False)
B_zfc, M_zfc, sM_zfc = data.getData()
B_zfc *= 1000
data = XyeData()
data.loadFromFile(datfile30_fc, sort=False)
B_fc, M_fc, sM_fc = data.getData()
B_fc *= 1000
min_B, max_B = -300, 300
min_M, max_M = -250, 250
T = 30

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.plot(B_zfc[1:], M_zfc[1:], marker='None', ls='-', zorder=1, label='ZFC')
ax.plot(B_fc[1:], M_fc[1:], marker='None', ls='-', zorder=1, label='FC @ 1 T')
# ,\
#             label=''
ax.text(0.7, 0.03,
  'IOS-7\n'
  '$\mathit{T} \, = \, 30\, K$',
  horizontalalignment='left',
  verticalalignment='bottom',
  transform=ax.transAxes)
ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, mT$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")
ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
ax.legend(loc='upper left')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)