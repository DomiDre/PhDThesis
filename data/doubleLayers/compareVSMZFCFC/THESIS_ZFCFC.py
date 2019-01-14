import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS

from modelexp.data import XyeData
from matplotlib.legend_handler import HandlerTuple

from PlottingTemplates.saxssanssanspol import color_variant

chapter = 'doublelayers'
sample_name = 'allSamples'
savefile = f'{chapter}_PPMS_ZFC_FC_{sample_name}'


def load_file(datfile_zfcw, datfile_fcw):
  data = XyeData()
  data.loadFromFile(datfile_zfcw)
  T1, M1, sM1 = data.getData()
  
  data = XyeData()
  data.loadFromFile(datfile_fcw)
  T2, M2, sM2 = data.getData()
  
  maxM = max(M2)
  M1 /= maxM
  M2 /= maxM
  sM1 /= maxM
  sM2 /= maxM
  return T1, M1, sM1, T2, M2, sM2

T_zfc_1, M_zfc_1, sM_zfc_1, T_fcw_1, M_fcw_1, sM_fcw_1 =\
  load_file('../dl_0-125/ppms/rescale/DL_0-125_zfcw_rescaled.xye',
            '../dl_0-125/ppms/rescale/DL_0-125_fcw_rescaled.xye')
T_zfc_2, M_zfc_2, sM_zfc_2, T_fcw_2, M_fcw_2, sM_fcw_2 =\
  load_file('../dl_0-25/ppms/rescale/DL_0-25_zfcw_rescaled.xye',
            '../dl_0-25/ppms/rescale/DL_0-25_fcw_rescaled.xye')
T_zfc_3, M_zfc_3, sM_zfc_3, T_fcw_3, M_fcw_3, sM_fcw_3 =\
  load_file('../dl_1-25/ppms/rescale/DL_1-25_zfcw_rescaled.xye',
            '../dl_1-25/ppms/rescale/DL_1-25_fcw_rescaled.xye')
T_zfc_4, M_zfc_4, sM_zfc_4, T_fcw_4, M_fcw_4, sM_fcw_4 =\
  load_file('../dl_2-5/ppms/rescale/DL_2-5_zfcw_rescaled.xye',
            '../dl_2-5/ppms/rescale/DL_2-5_fcw_rescaled.xye')
T_zfc_5, M_zfc_5, sM_zfc_5, T_fcw_5, M_fcw_5, sM_fcw_5 =\
  load_file('../dl_5/ppms/rescale/DL_5_zfcw_rescaled.xye',
            '../dl_5/ppms/rescale/DL_5_fcw_rescaled.xye')

shift = 0# 0.2
shift_fc_base = 0#1

fig = plt.figure()
left, bottom = 0.13, 0.15
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
# ax.axhline(0, color='lightgray', marker='None', zorder=0)
# ax.axvline(0, color='lightgray', marker='None', zorder=0)

ax.errorbar(T_zfc_1, M_zfc_1, sM_zfc_1, linestyle='None', marker='.', markersize=1, zorder=1, color=color_variant('#0EA8DF', 0), label='DL-0.125% ZFCw')
ax.errorbar(T_fcw_1, M_fcw_1+shift_fc_base, sM_fcw_1, linestyle='None', marker='.', markersize=1, zorder=1, color=color_variant('#EE292F', 0), label='DL-0.125% FCw')

ax.errorbar(T_zfc_2, M_zfc_2+shift, sM_zfc_2, linestyle='None', marker='.', markersize=1, zorder=1, color=color_variant('#0EA8DF', -50), label='DL-0.25% ZFCw')
ax.errorbar(T_fcw_2, M_fcw_2+shift_fc_base+shift, sM_fcw_2, linestyle='None', marker='.', markersize=1, zorder=1, color=color_variant('#EE292F', -50), label='DL-0.25% FCw')

ax.errorbar(T_zfc_3, M_zfc_3+2*shift, sM_zfc_3, linestyle='None', marker='.', markersize=1, zorder=1, color=color_variant('#0EA8DF', -100), label='DL-1.25% ZFCw')
ax.errorbar(T_fcw_3, M_fcw_3+shift_fc_base+2*shift, sM_fcw_3, linestyle='None', marker='.', markersize=1, zorder=1, color=color_variant('#EE292F', -100), label='DL-1.25% FCw')

ax.errorbar(T_zfc_4, M_zfc_4+3*shift, sM_zfc_4, linestyle='None', marker='.', markersize=1, zorder=1, color=color_variant('#0EA8DF', -150), label='DL-2.5% ZFCw')
ax.errorbar(T_fcw_4, M_fcw_4+shift_fc_base+3*shift, sM_fcw_4, linestyle='None', marker='.', markersize=1, zorder=1, color=color_variant('#EE292F', -150), label='DL-2.5% FCw')

ax.errorbar(T_zfc_5, M_zfc_5+4*shift, sM_zfc_5, linestyle='None', marker='.', markersize=1, zorder=1, color=color_variant('#0EA8DF', -200), label='DL-5% ZFCw')
ax.errorbar(T_fcw_5, M_fcw_5+shift_fc_base+4*shift, sM_fcw_5, linestyle='None', marker='.', markersize=1, zorder=1, color=color_variant('#EE292F', -200), label='DL-5% FCw')


handles, labels = ax.get_legend_handles_labels()
ax.legend(
  [
   (handles[8], handles[9]),
   (handles[6], handles[7]),
   (handles[4], handles[5]),
   (handles[2], handles[3]),
   (handles[0], handles[1])
   ],
  [
   'DL-5%',
   'DL-2.5%',
   'DL-1.25%',
   'DL-0.25%',
   'DL-0.125%'
  ],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=8,
  loc='upper left',
  bbox_to_anchor = [0.15, 0.75],
  bbox_transform=fig.transFigure)
ax.set_xlabel("$\mathit{T} \, / \, K$")
ax.set_ylabel("$\mathit{M} \, / \, a.u.$")
ax.set_xlim(10, 350)
ax.set_ylim(-0.1, 2.9)
ax.set_yticklabels([])
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)

# plt.show()