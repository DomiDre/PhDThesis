#Initialized ScriptFactory v0.2
#Date: 2018-07-11 20:36:37.178142
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import warnings
from modelexp.data import MultiData, XyemData, XyeData
from matplotlib.legend_handler import HandlerTuple

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = '8BL-40-IOS-11'
Chapter = 'looselyPackedNP'
rPlus_file_300K = cwd  + '/data/footprintCorrect/ES_S13_300K_4mT_refl_uu_fcorrected.xye'
rMinus_file_300K = cwd + '/data/footprintCorrect/ES_S13_300K_4mT_refl_du_fcorrected.xye'
rPlus_file_30K = cwd  + '/data/footprintCorrect/ES_S13_30K_2mT_ZFC_refl_uu_fcorrected.xye'
rMinus_file_30K = cwd + '/data/footprintCorrect/ES_S13_30K_2mT_ZFC_refl_dd_fcorrected.xye'

labeltext = '8BL-40-IOS-11'
q_min, q_max = 0.05, 1.1
I_min, I_max = 1e-6, 15

refl_pngfile = f"{Chapter}_VerticalStructure_{sample_name}_PNRCompare30K300K.png"


def get_data(file):
  data = XyeData()
  data.loadFromFile(file)
  q, I, sI = data.getData()
  q = np.array(q)
  I = np.array(I)
  sI = np.array(sI)
  valid_data = I > 0
  q = q[valid_data]
  I = I[valid_data]
  sI = sI[valid_data]
  valid_data = sI/I < 1
  q = q[valid_data]
  I = I[valid_data]
  sI = sI[valid_data]
  return q*10, I, sI

#load data
q_30K_p, I_30K_p, sI_30K_p = get_data(rPlus_file_30K)
q_30K_m, I_30K_m, sI_30K_m = get_data(rMinus_file_30K)

q_300K_p, I_300K_p, sI_300K_p = get_data(rPlus_file_300K)
q_300K_m, I_300K_m, sI_300K_m = get_data(rMinus_file_300K)

left, bottom = 0.19, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

sf_300K = 10
sf_30K = 1
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax.errorbar(q_300K_p, I_300K_p*sf_300K, sI_300K_p*sf_300K,
  linestyle='-', color='#0EA8DF',
  label='I_300K_p',
  zorder=0, capsize=0, marker='None')
ax.errorbar(q_300K_m, I_300K_m*sf_300K, sI_300K_m*sf_300K,
  linestyle='-', color='#EE292F',
  label='I_300K_m',
  zorder=0, capsize=0, marker='None')

ax.errorbar(q_30K_p, I_30K_p*sf_30K, sI_30K_p*sf_30K,
  linestyle='-', color='#793394',
  label='I_30K_p',
  zorder=0, capsize=0, marker='None')
ax.errorbar(q_30K_m, I_30K_m*sf_30K, sI_30K_m*sf_30K,
  linestyle='-', color='#7F0128',
  label='I_30K_m',
  zorder=0, capsize=0, marker='None')

ax.legend(loc='lower left', fontsize=10)
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, nm^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

handles, labels = ax.get_legend_handles_labels()
ax.legend(
  [(handles[0], handles[1]),
   (handles[2], handles[3])],
  ['300 K', '30 K'],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  bbox_to_anchor = [0.99, 0.99],
  bbox_transform=plt.gcf().transFigure)

ax.text(0.05, 0.05, labeltext,
  transform=ax.transAxes, fontsize=10)

fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)
plt.show()