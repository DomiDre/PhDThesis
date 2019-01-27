import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
# plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS

from modelexp.data import XyeData
from matplotlib.legend_handler import HandlerTuple

from PlottingTemplates.saxssanssanspol import color_variant

chapter = 'colloidalCrystals'
sample_name = 'allSamples'
savefile = f'{chapter}_PPMS_ZFC_FC_{sample_name}'


def load_file(datfile_zfcw, datfile_fcw):
  data = XyeData()
  data.loadFromFile(datfile_zfcw)
  T1, M1, sM1 = data.getData()
  data = XyeData()
  data.loadFromFile(datfile_fcw)
  T2, M2, sM2 = data.getData()
  return T1, M1, sM1, T2, M2, sM2

T_zfc_1, M_zfc_1, sM_zfc_1, T_fcw_1, M_fcw_1, sM_fcw_1 =\
  load_file('../CC_Fe_0.25/PPMS/rescale/CC_Fe_0-25_zfcw_rescaled.xye',
            '../CC_Fe_0.25/PPMS/rescale/CC_Fe_0-25_fcw_rescaled.xye')
T_zfc_2, M_zfc_2, sM_zfc_2, T_fcw_2, M_fcw_2, sM_fcw_2 =\
  load_file('../CC_Fe_0.37/PPMS/rescale/CC_Fe_0-37_zfcw_rescaled.xye',
            '../CC_Fe_0.37/PPMS/rescale/CC_Fe_0-37_fcw_rescaled.xye')
T_zfc_3, M_zfc_3, sM_zfc_3, T_fcw_3, M_fcw_3, sM_fcw_3 =\
  load_file('../CC_Fe_0.50/PPMS/rescale/CC_Fe_0-50_zfcw_rescaled.xye',
            '../CC_Fe_0.50/PPMS/rescale/CC_Fe_0-50_fcw_rescaled.xye')

shift = 0
shift_fc_base = 0

fig = plt.figure()
left, bottom = 0.18, 0.15
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.errorbar(T_zfc_1, M_zfc_1, sM_zfc_1, linestyle='-', capsize=0, marker='None', markersize=1, zorder=1, color=color_variant('#0EA8DF', 0), label='CC-Fe-0.25 ZFCW')
ax.errorbar(T_fcw_1, M_fcw_1+shift_fc_base, sM_fcw_1, linestyle='-', capsize=0, marker='None', markersize=1, zorder=1, color=color_variant('#EE292F', 0), label='CC-Fe-0.25 FCw')

ax.errorbar(T_zfc_2, M_zfc_2+shift, sM_zfc_2, linestyle='-', capsize=0, marker='None', markersize=1, zorder=1, color=color_variant('#76C152', -50), label='CC-Fe-0.37 ZFCw')
ax.errorbar(T_fcw_2, M_fcw_2+shift_fc_base+shift, sM_fcw_2, linestyle='-', capsize=0, marker='None', markersize=1, zorder=1, color=color_variant('#FAAB2D', -50), label='CC-Fe-0.37 FCw')

ax.errorbar(T_zfc_3, M_zfc_3+2*shift, sM_zfc_3, linestyle='-', capsize=0, marker='None', markersize=1, zorder=1, color=color_variant('#0EA8DF', -150), label='CC-Fe-0.50 ZFCw')
ax.errorbar(T_fcw_3, M_fcw_3+shift_fc_base+2*shift, sM_fcw_3, linestyle='-', capsize=0, marker='None', markersize=1, zorder=1, color=color_variant('#EE292F', -150), label='CC-Fe-0.50 FCw')


handles, labels = ax.get_legend_handles_labels()
ax.legend(
  [
   (handles[4], handles[5]),
   (handles[2], handles[3]),
   (handles[0], handles[1]),
   ],
  [
   'CC-Fe-0.50',
   'CC-Fe-0.37',
   'CC-Fe-0.25',
  ],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  loc='upper left',
  bbox_to_anchor = [0.6, 0.5],
  bbox_transform=fig.transFigure)

# ax.annotate('', xy=(315, 40), xytext=(315,15),
#   horizontalalignment='center', fontsize=10,
#   arrowprops=dict(facecolor='black', width=1, headwidth=5))
# ax.text(345, 10,
#         '$\mathit{T_B} \,= \, 315\, K$',\
#         horizontalalignment='right',
#         verticalalignment='top')

ax.set_xlabel("$\mathit{T} \, / \, K$")
ax.set_ylabel("$\mathit{M} \, / \, \mathit{M}_{s}^{300 K}$")
ax.set_xlim(10, 350)
ax.set_ylim(0, 0.49)
# ax.set_yticklabels([])
plt.savefig(cwd + '/' + savefile)
# plt.savefig(thesisimgs + '/' + savefile)

plt.show()