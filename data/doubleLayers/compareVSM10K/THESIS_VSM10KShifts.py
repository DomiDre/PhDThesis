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
sample_name = 'allSamplesShifted'
savefile = f'{chapter}_PPMS_10K_{sample_name}'


def load_file(datafile, sf=1, chi=0):
  data = XyeData()
  data.loadFromFile(datafile, sort=False)
  B1, M1, sM1 = data.getData()
  B1 = B1[800:]
  M1 = M1[800:]
  sM1 = sM1[800:]
  return B1, (M1-chi*B1)*sf, sM1*sf

B_1, M_1, sM_1 = load_file('../dl_0-125/ppms/rescale/DL_0-125_10K_rescaled.xye')
B_2, M_2, sM_2 = load_file('../dl_0-25/ppms/rescale/DL_0-25_10K_rescaled.xye')
B_3, M_3, sM_3 = load_file('../dl_1-25/ppms/rescale/DL_1-25_10K_rescaled.xye')
B_4, M_4, sM_4 = load_file('../dl_2-5/ppms/rescale/DL_2-5_10K_rescaled.xye')
B_5, M_5, sM_5 = load_file('../dl_5/ppms/rescale/DL_5_10K_rescaled.xye')

shift = 100

fig = plt.figure()
left, bottom = 0.09, 0.16 #0.09, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
# ax.axhline(0, color='lightgray', marker='None', zorder=0)
# ax.axvline(0, color='lightgray', marker='None', zorder=0)

ax.errorbar(B_1, M_1, sM_1, linestyle='None', marker='.', capsize=0, markersize=1, zorder=1, color=color_variant('#0EA8DF', 0), label='DL-0.125%')

ax.errorbar(B_2, M_2+shift, sM_2, linestyle='None', marker='.', capsize=0, markersize=1, zorder=1, color=color_variant('#0EA8DF', -50), label='DL-0.25%')

ax.errorbar(B_3, M_3+2*shift, sM_3, linestyle='None', marker='.', capsize=0, markersize=1, zorder=1, color=color_variant('#0EA8DF', -100), label='DL-1.25%')

ax.errorbar(B_4, M_4+3*shift, sM_4, linestyle='None', marker='.', capsize=0, markersize=1, zorder=1, color=color_variant('#0EA8DF', -150), label='DL-2.5%')

ax.errorbar(B_5, M_5+4*shift, sM_5, linestyle='None', marker='.', capsize=0, markersize=1, zorder=1, color=color_variant('#0EA8DF', -200), label='DL-5%')


handles, labels = ax.get_legend_handles_labels()

def add_legend(handle, title, height):
  legend = ax.legend([handle],[title],
    handler_map={tuple: HandlerTuple(ndivide=None)},
    fontsize=10,
    handletextpad=0,
    loc='upper left',
    bbox_to_anchor = [0.65, height],
    bbox_transform=fig.transFigure)
  return legend

legend1 = add_legend(handles[4], 'DL-5%', 0.58)
legend2 = add_legend(handles[3], 'DL-2.5%', 0.51)
legend3 = add_legend(handles[2], 'DL-1.25%', 0.44)
legend4 = add_legend(handles[1], 'DL-0.25%', 0.37)
legend5 = add_legend(handles[0], 'DL-0.125%', 0.3)

plt.gca().add_artist(legend1)
plt.gca().add_artist(legend2)
plt.gca().add_artist(legend3)
plt.gca().add_artist(legend4)


ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel("$\mathit{M} \, / \, a.u.$")
ax.set_xlim(-8.9, 8.9)
ax.set_ylim(-430, 820)
ax.set_yticklabels([])
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)

# plt.show()