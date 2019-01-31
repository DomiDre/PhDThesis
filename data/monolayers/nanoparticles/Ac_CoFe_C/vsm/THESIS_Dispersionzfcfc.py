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

def load_file(datafile):
  ppms = PPMS()
  ppms.load(datafile)
  T, M = ppms.get_TM()
  sM = ppms.get('M. Std. Err. (emu)')
  valid_point = sM > 0
  T = T[valid_point]
  M = M[valid_point]
  sM = sM[valid_point]
  return T, M, sM

T_fcc, M_fcc, sM_fcc = load_file('./data_dispersion/AH11_FCC_100OE.DAT')
T_zfcw, M_zfcw, sM_zfcw = load_file('./data_dispersion/AH11_ZFCW_100OE_00001.dat')


chapter = 'monolayer'
sample_name = 'Ac_CoFe_C'
savefile = f'{chapter}_PPMS_Dispersion_ZFC_FC_{sample_name}'

fig = plt.figure()
left, bottom = 0.21, 0.15
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.errorbar(T_fcc, M_fcc, sM_fcc,    linestyle='-', marker='None', capsize=0, markersize=1, zorder=1, label='FCc')
ax.errorbar(T_zfcw, M_zfcw, sM_zfcw, linestyle='-', marker='None', capsize=0, markersize=1, zorder=1, label='ZFCw')

ax.text(0.02, 0.97,
  '$\mathit{B} \, = \, 10 \, mT$',
  horizontalalignment='left',
  verticalalignment='top',
  transform=ax.transAxes)

ax.set_xlabel("$\mathit{T} \, / \, K$")
ax.set_ylabel("$\mathit{M} \, / \, memu$", labelpad=-1)

ax.set_xlim(0, 320)
ax.set_ylim(-0.3, 1.2)
ax.legend(loc='upper right')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)
