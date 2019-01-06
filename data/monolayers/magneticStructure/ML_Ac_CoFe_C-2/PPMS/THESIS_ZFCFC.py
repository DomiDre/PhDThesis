import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS

from modelexp.data import XyeData

zfc_datfile = './rescale/ML_Ac_CoFe_C_2star_zfcw_rescaled_LangevinSAXSscaled.xye'
fcw_datfile = './rescale/ML_Ac_CoFe_C_2star_fcw_rescaled_LangevinSAXSscaled.xye'

chapter = 'monolayer'
sample_name = 'ML_Ac_CoFe_C_2star'
savefile = f'{chapter}_PPMS_ZFC_FC_{sample_name}'

def load_file(datfile):
  data = XyeData()
  data.loadFromFile(datfile)
  T, M, sM = data.getData()
  # ppms = PPMS()
  # ppms.load(datfile)
  # ppms.clean_peaks(0.0005, show=False)
  # T, M = ppms.get_TM()
  # sM = np.zeros(len(M))
  # M *= 1000
  # sM *= 1000
  return T, M, sM

fig = plt.figure()
left, bottom = 0.15, 0.15
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
# ax.axhline(0, color='lightgray', marker='None', zorder=0)
# ax.axvline(0, color='lightgray', marker='None', zorder=0)

T_zfc, M_zfc, sM_zfc = load_file(zfc_datfile)
T_fcw, M_fcw, sM_fcw = load_file(fcw_datfile)
ax.errorbar(T_zfc, M_zfc, sM_zfc, linestyle='None', marker='.', markersize=1, zorder=1, label='ZFCw')
ax.errorbar(T_fcw, M_fcw, sM_fcw, linestyle='None', marker='.', markersize=1, zorder=1, label='FCw')

ax.set_xlabel("$\mathit{T} \, / \, K$")
ax.set_ylabel("$\mathit{M} \, / \, kAm^{-1}$", labelpad=-5)
ax.text(0.05, 0.95,
        'ML-Ac-CoFe-C-2*\n'+
        '$\mathit{B} \, = \, 10 \, mT$',\
        horizontalalignment='left',
        verticalalignment='top',\
        transform=ax.transAxes)

ax.annotate('', xy=(303, 70), xytext=(303,35),
  horizontalalignment='center', fontsize=10,
  arrowprops=dict(facecolor='black', width=1, headwidth=5))
ax.text(345, 30,
        '$\mathit{T_B} \,= \, 303\, K$',\
        horizontalalignment='right',
        verticalalignment='top')
ax.set_yticks([0, 30, 60, 90, 120])
ax.set_xlim(0, 350)
ax.set_ylim(-9, 145)
ax.legend(loc='upper right')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)
