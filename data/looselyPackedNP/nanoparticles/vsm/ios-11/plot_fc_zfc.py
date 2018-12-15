import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS

from modelexp.data import XyeData

zfc_datfile = cwd + '/rawdata/ZFC100Oe.dc.dat'
fcw_datfile = cwd + '/rawdata/FC100Oe.dc.dat'

chapter = 'looselyPackedNP'
sample_name = 'IOS-11'
savefile = f'{chapter}_VSM_ZFC_FC_{sample_name}'

def load_file(datfile):
  ppms = PPMS()
  ppms.load(datfile)
  T, M = ppms.get_TM()
  M = M/(13.800/6)
  return T, M

fig = plt.figure()
left, bottom = 0.15, 0.15
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

T_zfc, M_zfc = load_file(zfc_datfile)
T_fcw, M_fcw = load_file(fcw_datfile)
ax.plot(T_zfc, M_zfc, linestyle='None', marker='.', markersize=1, zorder=1, label='ZFCw')
ax.plot(T_fcw, M_fcw, linestyle='None', marker='.', markersize=1, zorder=1, label='FCw')

ax.set_xlabel("$\mathit{T} \, / \, K$")
ax.set_ylabel("$\mathit{M} \, / \, kAm^{-1}$")
ax.text(0.05, 0.95,
        '$\mathit{B} \, = \, 10 \, mT$',\
        horizontalalignment='left',
        verticalalignment='top',\
        transform=ax.transAxes)

ax.annotate('', xy=(100, 21), xytext=(100,16),
  horizontalalignment='center', fontsize=10,
  arrowprops=dict(facecolor='black', width=1, headwidth=5))
ax.text(120, 13,
        '$\mathit{T_B} \,= \, 100\, K$',\
        horizontalalignment='right',
        verticalalignment='top')
ax.text(0.92, 0.7,
        'IOS-11',\
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)

ax.set_xlim(10, 180)
ax.set_ylim(-0.9, 39)
ax.legend(loc='upper right')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)
