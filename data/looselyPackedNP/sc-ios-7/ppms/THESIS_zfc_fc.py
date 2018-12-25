import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS

from modelexp.data import XyeData

zfc_datfile = cwd + '/rawdata/ES_S17_ZFCW_100OE.DAT'
fcw_datfile = cwd + '/rawdata/ES_S17_FCW_100OE.DAT'

chapter = 'looselyPackedNP'
sample_name = 'SC-IOS-7'
savefile = f'{chapter}_VSM_ZFC_FC_{sample_name}'

rescale_factor = 1828.206260347034
def load_file(datfile):
  ppms = PPMS()
  ppms.load(datfile)
  T, M = ppms.get_TM()
  sM = ppms.get('M. Std. Err. (emu)')
  valid_point = sM > 0
  T = T[valid_point]
  M = M[valid_point]*rescale_factor
  sM = sM[valid_point]*rescale_factor
  return T, M, sM

fig = plt.figure()
left, bottom = 0.15, 0.15
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

T_zfc, M_zfc, sM_zfc = load_file(zfc_datfile)
T_fcw, M_fcw, sM_fcw = load_file(fcw_datfile)
ax.plot(T_zfc, M_zfc, linestyle='None', marker='.', markersize=1, zorder=1, label='ZFCw')
ax.plot(T_fcw, M_fcw, linestyle='None', marker='.', markersize=1, zorder=1, label='FCw')

ax.set_xlabel("$\mathit{T} \, / \, K$")
ax.set_ylabel("$\mathit{M} \, / \, kAm^{-1}$")
ax.text(0.05, 0.95,
        '$\mathit{B} \, = \, 10 \, mT$',\
        horizontalalignment='left',
        verticalalignment='top',\
        transform=ax.transAxes)


ax.annotate('', xy=(47, 38), xytext=(47,25),
  horizontalalignment='center', fontsize=10,
  arrowprops=dict(facecolor='black', width=1, headwidth=5))
ax.text(90, 23,
        '$\mathit{T_B} \,= \, 47\, K$',\
        horizontalalignment='right',
        verticalalignment='top')
ax.text(0.92, 0.7,
        'SC-IOS-7',\
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)


ax.set_xlim(10, 230)
ax.set_ylim(-0.9, 70)
ax.legend(loc='upper right')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)
