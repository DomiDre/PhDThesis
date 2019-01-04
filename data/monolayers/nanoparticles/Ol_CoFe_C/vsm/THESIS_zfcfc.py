import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS

from modelexp.data import XyeData
from scipy import interpolate
import scipy.signal as spsig
from PlottingTemplates.saxssanssanspol import color_variant

zfc_datfile = './rescale/Ol_CoFe_C_DisorderedWafer_ZFCw_LangevinSAXSscaled.xye'
fcw_datfile = './rescale/Ol_CoFe_C_DisorderedWafer_FCw_LangevinSAXSscaled.xye'

chapter = 'monolayer'
sample_name = 'Ol_CoFe_C'
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
ax.plot(T_zfc, M_zfc, linestyle='None', marker='.', markersize=1, zorder=1, label='ZFCw')
ax.plot(T_fcw, M_fcw, linestyle='None', marker='.', markersize=1, zorder=1, label='FCc')

M_zfc_medfilt = spsig.medfilt(M_zfc, 49)
ax.plot(T_zfc[30:-30], M_zfc_medfilt[30:-30], linestyle='-', marker='None',
  color=color_variant('#0EA8DF', -150),
  markersize=1, zorder=1)


M_fcw_medfilt = spsig.medfilt(M_fcw, 49)
ax.plot(T_fcw[30:-30], M_fcw_medfilt[30:-30], linestyle='-', marker='None',
  color=color_variant('#EE292F', -150),
  markersize=1, zorder=1)

ax.set_xlabel("$\mathit{T} \, / \, K$")
ax.set_ylabel("$\mathit{M} \, / \, kAm^{-1}$")

ax.annotate('', xy=(210, 3.5), xytext=(210,-1),
  horizontalalignment='center', fontsize=10,
  arrowprops=dict(facecolor='black', width=1, headwidth=5))
ax.text(270, -2,
        '$\mathit{T_B} \,= \, 210\, K$',\
        horizontalalignment='right',
        verticalalignment='top')
ax.text(0.02, 0.97,
        'Ol-CoFe-C\n'+\
        '$\mathit{B} \, = \, 10 \, mT$',
        horizontalalignment='left',
        verticalalignment='top',
        transform=ax.transAxes)

ax.set_xlim(0, 350)
ax.set_ylim(-4, 16)
ax.legend(loc='upper right')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)
