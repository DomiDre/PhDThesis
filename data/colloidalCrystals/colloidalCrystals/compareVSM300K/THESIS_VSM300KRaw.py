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
sample_name = 'allSamples'
savefile = f'{chapter}_PPMS_300KrawData_{sample_name}'


def load_file(datafile):
  ppms = PPMS()
  ppms.load(datafile)
  ppms.remove_virgin_data()
  B, M = ppms.get_BM()
  sM = ppms.get('M. Std. Err. (emu)')
  return B, M, sM

B_1, M_1, sM_1 = load_file('../CC_Fe_0.25/PPMS/rawdata/DD151_2_HYST_INIT_300K.DAT')
B_2, M_2, sM_2 = load_file('../CC_Fe_0.37/PPMS/rawdata/DD151_28_HYST_300KREPEAT.DAT')
B_3, M_3, sM_3 = load_file('../CC_Fe_0.50/PPMS/rawdata/DD151_30_HYST_INIT_300K.DAT')

shift = 0

fig = plt.figure()
left, bottom = 0.16, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)

ax.errorbar(B_1, M_1, sM_1, linestyle='-', marker='None',
  capsize=0, markersize=1, zorder=1,
  color=color_variant('#0EA8DF', 0), label='CC-Fe-0.25')

ax.errorbar(B_2, M_2+shift, sM_2, linestyle='-', marker='None',
  capsize=0, markersize=1, zorder=1,
  color=color_variant('#76C152', -50), label='CC-Fe-0.37')

ax.errorbar(B_3, M_3+2*shift, sM_3, linestyle='-', marker='None',
  capsize=0, markersize=1, zorder=1,
  color=color_variant('#0EA8DF', -200), label='CC-Fe-0.50')

B_fit = np.linspace(0, 10, 100)
B_straight = np.linspace(5, 9, 100)
def linear(B, chi, Ms):
  return Ms + chi*B
ax.plot(B_fit, linear(B_fit, -16.18e-3, 1.8480), marker='None', ls='--',
  color=color_variant('#EE292F', 0), zorder=2)
ax.plot(B_fit, linear(B_fit, -5.46e-3, 1.5599), marker='None', ls='--',
  color=color_variant('#FAAB2D', -50), zorder=2)
ax.plot(B_fit, linear(B_fit, 6.68e-3, 4.4333), marker='None', ls='--',
  color=color_variant('#EE292F', -200), zorder=2)

ax.plot(B_straight, linear(B_straight, -16.18e-3, 1.8480), marker='None', ls='-',
  color=color_variant('#EE292F', 0), zorder=2)
ax.plot(B_straight, linear(B_straight, -5.46e-3, 1.5599), marker='None', ls='-',
  color=color_variant('#FAAB2D', -50), zorder=2)
ax.plot(B_straight, linear(B_straight, 6.68e-3, 4.4333), marker='None', ls='-',
  color=color_variant('#EE292F', -200), zorder=2)


handles, labels = ax.get_legend_handles_labels()

def add_legend(handle, title, height):
  legend = ax.legend([handle],[title],
    handler_map={tuple: HandlerTuple(ndivide=None)},
    fontsize=10,
    handletextpad=0,
    loc='upper left',
    bbox_to_anchor = [0.14, height],
    bbox_transform=fig.transFigure)
  return legend

legend1 = add_legend(handles[0], 'CC-Fe-0.25', 0.84)
legend2 = add_legend(handles[1], 'CC-Fe-0.37', 0.91)
legend3 = add_legend(handles[2], 'CC-Fe-0.50', 0.98)

ax.add_artist(legend1)
ax.add_artist(legend2)


ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel("$\mathit{M} \, / \, memu$")
ax.set_xlim(-8.9, 8.9)
ax.set_ylim(-4.9, 4.9)
# ax.set_yticklabels([])
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)

# plt.show()