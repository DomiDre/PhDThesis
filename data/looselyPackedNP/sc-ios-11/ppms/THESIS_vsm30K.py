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

datfile30K_fc = cwd+ '/data_rescaling/SC-IOS-11_30K_FC_LangevinSAXSscaled.xye'
datfile30K_zfc = cwd+ '/data_rescaling/SC-IOS-11_30K_ZFC_LangevinSAXSscaled.xye'

chapter = 'looselyPackedNP'
sample_name = 'SC-IOS-11'

savefile = chapter + '_VSM30K_' + sample_name

def load_file(datfile):
  data = XyeData()
  data.loadFromFile(datfile, sort=False)
  B, M, sM = data.getData()
  B *= 1000
  valid_point = sM > 0
  B = B[valid_point]
  M = M[valid_point]
  sM = sM[valid_point]
  return B, M, sM


B_30Kfc, M_30Kfc, sM_30Kfc = load_file(datfile30K_fc)
B_30Kzfc, M_30Kzfc, sM_30Kzfc = load_file(datfile30K_zfc)

min_B, max_B = -300, 300
min_M, max_M = -250, 250
T = 30

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
# ax_inset = fig.add_axes([0.67, 0.25, 0.3, 0.3])
ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(B_30Kzfc, M_30Kzfc, sM_30Kzfc, linestyle='-', marker='None', zorder=1,\
  label='ZFC',
  capsize=0)
ax.errorbar(B_30Kfc, M_30Kfc, sM_30Kfc, linestyle='-', marker='None', zorder=1,\
  label='FC',
  capsize=0)
# ax_inset.errorbar(B_30Kfc, M_30Kfc, sM_30Kfc, linestyle='-', marker='None', zorder=1,\
#   capsize=0)
# ax_inset.errorbar(B_30Kzfc, M_30Kzfc, sM_30Kzfc, linestyle='-', marker='None', zorder=1,\
#   capsize=0)

# ax_inset.axhline(0, color='lightgray', marker='None', zorder=0)
# ax_inset.axvline(0, color='lightgray', marker='None', zorder=0)
# ax_inset.set_xlim(-40, 40)
# ax_inset.set_ylim(-50, 50)

# ax_inset.tick_params(axis='both', which='major', labelsize=8)
# ax_inset.tick_params(axis='both', which='minor', labelsize=8)

ax.text(0.6, 0.03,
  'SC-IOS-11\n'+\
  '$\mathit{T} \,=\, ' + str(T) + ' \,K$',
  horizontalalignment='left',
  verticalalignment='bottom',
  transform=ax.transAxes)
ax.legend(loc='upper left')
ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, mT$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")
ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)