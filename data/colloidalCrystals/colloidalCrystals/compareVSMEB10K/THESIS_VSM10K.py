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

chapter = 'colloidalCrystals'
sample_name = 'CC-Fe-0-37_EB'
savefile = f'{chapter}_PPMS_10K_{sample_name}'


def load_file(datafile, sf=1, chi=0):
  data = XyeData()
  data.loadFromFile(datafile, sort=False)
  B1, M1, sM1 = data.getData()
  return B1, (M1-chi*B1)*sf, sM1*sf

B_1, M_1, sM_1 = load_file('../CC_Fe_0.37/PPMS/rescale/CC_Fe_0-37_10K_rescaled.xye')
B_2, M_2, sM_2 = load_file('../CC_Fe_0.37/PPMS/rescale/CC_Fe_0-37_10K_FC4T_rescaled.xye')

shift = 0

fig = plt.figure()
left, bottom = 0.16, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_inset = fig.add_axes([0.7,bottom+0.1, 0.25, 0.3])

ax.errorbar(B_1, M_1, sM_1, linestyle='-', marker='None',
  capsize=0, markersize=1, zorder=1,
  color=color_variant('#0EA8DF', 0), label='CC-Fe-0.37 ZFC')

ax.errorbar(B_2, M_2+shift, sM_2, linestyle='-', marker='None',
  capsize=0, markersize=1, zorder=1,
  color=color_variant('#EE292F', -100), label='CC-Fe-0.37 FC')

ax_inset.axhline(0, color='lightgray', marker='None', zorder=0)
ax_inset.axvline(0, color='lightgray', marker='None', zorder=0)

ax_inset.errorbar(B_1, M_1, sM_1, linestyle='-', marker='None',
  capsize=0, markersize=1, zorder=1,
  color=color_variant('#0EA8DF', 0), label='CC-Fe-0.37 ZFC')

ax_inset.errorbar(B_2, M_2+shift, sM_2, linestyle='-', marker='None',
  capsize=0, markersize=1, zorder=1,
  color=color_variant('#EE292F', -100), label='CC-Fe-0.37 FC')

ax_inset.set_xlim(-0.10, 0.10)
ax_inset.set_ylim(-0.9, 0.9)
ax_inset.tick_params(axis='both', which='major', labelsize=8)
ax_inset.tick_params(axis='both', which='minor', labelsize=8)

handles, labels = ax.get_legend_handles_labels()

def add_legend(handle, title, height):
  legend = ax.legend([handle],[title],
    handler_map={tuple: HandlerTuple(ndivide=None)},
    fontsize=10,
    # handletextpad=0,
    loc='upper left',
    bbox_to_anchor = [0.14, height],
    bbox_transform=fig.transFigure)
  return legend

ax.text(0.03, 0.93, 'CC-Fe-0.37',
  verticalalignment='top',
  horizontalalignment='left',
  fontsize=10,
  transform = ax.transAxes)
legend1 = add_legend(handles[0], 'ZFC', 0.84)
legend2 = add_legend(handles[1], 'FC @ 4T', 0.91)

ax.add_artist(legend1)
ax.add_artist(legend2)


ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel("$(\mathit{M} - \chi^{300 K} \mu_0 H) \, / \, \mathit{M}_{s}^{300 K}$")
ax.set_xlim(-8.9, 8.9)
ax.set_ylim(-1.2, 1.2)
ax.set_yticks([-1, 0, 1])
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)
