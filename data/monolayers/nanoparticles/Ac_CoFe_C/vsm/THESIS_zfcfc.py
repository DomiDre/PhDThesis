import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS

from modelexp.data import XyeData

samplename = 'Ac_CoFe_C'
zfc_datfile = './rescale/Ac_CoFe_C_DisorderedWafer_ZFCw_LangevinSAXSscaled.xye'
fcw_datfile = './rescale/Ac_CoFe_C_DisorderedWafer_FCw_LangevinSAXSscaled.xye'

chapter = 'monolayer'
sample_name = 'Ac_CoFe_C'
savefile = f'{chapter}_PPMS_ZFC_FC_{sample_name}'

def load_file(datfile):
  data = XyeData()
  data.loadFromFile(datfile)
  T, M, sM = data.getData()
  return T, M, sM

fig = plt.figure()
left, bottom = 0.15, 0.15
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

T_zfc, M_zfc, sM_zfc = load_file(zfc_datfile)
T_fcw, M_fcw, sM_fcw = load_file(fcw_datfile)
ax.errorbar(T_zfc, M_zfc, sM_zfc, linestyle='None', marker='.', markersize=1, zorder=1, label='ZFCw')
ax.errorbar(T_fcw, M_fcw, sM_fcw, linestyle='None', marker='.', markersize=1, zorder=1, label='FCc')

ax.set_xlabel("$\mathit{T} \, / \, K$")
ax.set_ylabel("$\mathit{M} \, / \, kAm^{-1}$")

ax.annotate('', xy=(315, 44), xytext=(315,8),
  horizontalalignment='center', fontsize=10,
  arrowprops=dict(facecolor='black', width=1, headwidth=5))
ax.text(349, 5,
        '$\mathit{T_B} \,= \, 315\, K$',\
        horizontalalignment='right',
        verticalalignment='top')
ax.text(0.02, 0.97,
        'Ac-CoFe-C\n'+\
        '$\mathit{B} \, = \, 10 \, mT$',
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes)

ax.set_xlim(0, 350)
ax.set_ylim(-7, 99)
ax.legend(loc='upper right')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)
