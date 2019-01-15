import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS

from modelexp.data import XyeData

# zfc_datfile = cwd + '/rawdata/PMK18_ZFCW_100OESLOW.DAT'
# fcw_datfile = cwd + '/rawdata/PMK18_FCW_100OESLOW.DAT'
zfc_datfile = cwd + '/data_rescaling/IOS-11_Dispersion_ZFCw_LangevinSAXSscaled.xye'
fcw_datfile = cwd + '/data_rescaling/IOS-11_Dispersion_FCw_LangevinSAXSscaled.xye'

chapter = 'looselyPackedNP'
sample_name = 'IOS-11'
savefile = f'{chapter}_VSM_ZFC_FC_{sample_name}'

def load_file(datfile):
  data = XyeData()
  data.loadFromFile(datfile, sort=False)
  T, M, sM = data.getData()

#   ppms = PPMS()
#   ppms.load(datfile)
#   T, M = ppms.get_TM()
#   sM = ppms.get('M. Std. Err. (emu)')
  valid_point = sM > 0
  T = T[valid_point]
  M = M[valid_point]
  sM = sM[valid_point]
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


ax.annotate('', xy=(95, 55), xytext=(95,30),
  horizontalalignment='center', fontsize=10,
  arrowprops=dict(facecolor='black', width=1, headwidth=5))
ax.text(140, 27,
        '$\mathit{T_B} \,= \, 95.5(5)\, K$',\
        horizontalalignment='right',
        verticalalignment='top')
ax.text(0.92, 0.7,
        'IOS-11',\
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)


ax.set_xlim(10, 230)
ax.set_ylim(-0.9, 99)
ax.legend(loc='upper right')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)
plt.show()