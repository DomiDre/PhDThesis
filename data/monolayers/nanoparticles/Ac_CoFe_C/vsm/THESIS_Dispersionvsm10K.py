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
from PPMS.ppms import PPMS

datfile_300K = './data_dispersion/AH11_HYST_100OE_300K.DAT'
datfile_10K = './data_dispersion/AH11_HYST_100OE_10K.DAT'

chapter = 'monolayer'
sample_name = 'Ac_CoFe_C'

savefile = chapter + '_VSM_DispersionHyst_' + sample_name

def load_data(datafile):
  ppms = PPMS()
  ppms.load(datafile)
  ppms.remove_virgin_data(6.9)
  B, M = ppms.get_BM()
  sM = ppms.get('M. Std. Err. (emu)')
  valid_point = sM > 0
  B = B[valid_point]
  M = M[valid_point]
  sM = sM[valid_point]
  return B, M, sM

B_300K, M_300K, sM_300K = load_data(datfile_300K)
B_10K, M_10K, sM_10K = load_data(datfile_10K)

min_B, max_B = -8.9, 8.9
min_M, max_M = -7, 7
T = 10

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(B_10K, M_10K, sM_10K, linestyle='-', marker='None', markersize=1, zorder=2,\
            label='10 K ', capsize=0)
ax.errorbar(B_300K, M_300K, sM_300K, linestyle='-', marker='None', markersize=1, zorder=1,\
            label='300 K', capsize=0)

ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel(r"$\mathit{M} \, / \, memu$")

ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
ax.legend(loc='upper left', bbox_to_anchor=[-0.05, 1.03])
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)
# plt.show()