import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS

from modelexp.data import XyeData

zfc_datfile = './rescale/DL_0-125_zfcw_rescaled.xye'
fcw_datfile = './rescale/DL_0-125_fcw_rescaled.xye'

chapter = 'doublelayers'
sample_name = 'DL_0-125'
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
ax.set_ylabel("$\mathit{M} \, / \, kAm^{-1}$")
ax.text(0.05, 0.95,
        'DL-0.125%\n'+
        '$\mathit{B} \, = \, 10 \, mT$',\
        horizontalalignment='left',
        verticalalignment='top',\
        transform=ax.transAxes)

ax.annotate('', xy=(315, 45), xytext=(315,12),
  horizontalalignment='center', fontsize=10,
  arrowprops=dict(facecolor='black', width=1, headwidth=5))
ax.text(345, 10,
        '$\mathit{T_B} \,= \, 315\, K$',\
        horizontalalignment='right',
        verticalalignment='top')

ax.set_xlim(0, 350)
ax.set_ylim(-0.9, 99)
ax.legend(loc='upper right')
plt.savefig(cwd + '/' + savefile)
# plt.savefig(thesisimgs + '/' + savefile)

# plt.show()