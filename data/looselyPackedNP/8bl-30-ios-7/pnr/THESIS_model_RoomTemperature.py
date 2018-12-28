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

sample_name = '8BL-30-IOS-7'
Chapter = 'looselyPackedNP'
gf_rPlus_file = cwd  + '/data/rawdata/300K/ES_S16_300K_4mT_Virgin_tranformed_angs_uu_masked_qz_I_corrected.xy'
gf_rMinus_file = cwd + '/data/rawdata/300K/ES_S16_300K_4mT_Virgin_tranformed_angs_du_masked_qz_I_corrected.xy'
sat_rPlus_file = cwd  + '/data/rawdata/300K/ES_S16_300K_500mT_tranformed_angs_uu_masked_qz_I_corrected.xy'
sat_rMinus_file = cwd + '/data/rawdata/300K/ES_S16_300K_500mT_tranformed_angs_du_masked_qz_I_corrected.xy'
rem_rPlus_file = cwd +  '/data/rawdata/300K/ES_S16_300K_4mT_Remanence_tranformed_angs_uu_masked_qz_I_corrected.xy'
rem_rMinus_file = cwd + '/data/rawdata/300K/ES_S16_300K_4mT_Remanence_tranformed_angs_du_masked_qz_I_corrected.xy'

labeltext = '8BL-30-IOS-7\n300 K'
q_min, q_max = 0.05, 1.1
I_min, I_max = 5e-6, 5e2

refl_pngfile = f"{Chapter}_VerticalStructure_{sample_name}_PNR.png"


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
q_gf_p, I_gf_p, sI_gf_p = get_data(gf_rPlus_file)
q_gf_m, I_gf_m, sI_gf_m = get_data(gf_rMinus_file)

q_sat_p, I_sat_p, sI_sat_p = get_data(sat_rPlus_file)
q_sat_m, I_sat_m, sI_sat_m = get_data(sat_rMinus_file)

q_rem_p, I_rem_p, sI_rem_p = get_data(rem_rPlus_file)
q_rem_m, I_rem_m, sI_rem_m = get_data(rem_rMinus_file)


left, bottom = 0.19, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

sf_gf = 1e2
sf_sat = 1e1
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax.errorbar(q_gf_p, I_gf_p*sf_gf, sI_gf_p*sf_gf,
  linestyle='-', color='#793394',
  label='I_gf_p',
  zorder=0, capsize=0, marker='None')
ax.errorbar(q_gf_m, I_gf_m*sf_gf, sI_gf_m*sf_gf,
  linestyle='-', color='#7F0128',
  label='I_gf_m',
  zorder=0, capsize=0, marker='None')

ax.errorbar(q_sat_p, I_sat_p*sf_sat, sI_sat_p*sf_sat,
  linestyle='-', color='#0EA8DF',
  label='I_sat_p',
  zorder=0, capsize=0, marker='None')
ax.errorbar(q_sat_m, I_sat_m*sf_sat, sI_sat_m*sf_sat,
  linestyle='-', color='#EE292F',
  label='I_sat_m',
  zorder=0, capsize=0, marker='None')

ax.errorbar(q_rem_p, I_rem_p, sI_rem_p,
  linestyle='-', color='#FAAB2D',
  label='I_rem_p',
  zorder=0, capsize=0, marker='None')
ax.errorbar(q_rem_m, I_rem_m, sI_rem_m,
  linestyle='-', color='#76C152',
  label='I_rem_m',
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
   (handles[2], handles[3]),
   (handles[4], handles[5])],
  ['Initial', '500 mT', 'Remanence'],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  bbox_to_anchor = [0.53, 0.59])

ax.text(0.05, 0.05, labeltext,
  transform=ax.transAxes, fontsize=10)

fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)