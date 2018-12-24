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
from modelexp.data import XyeData
import matplotlib.patches as mpatches

from matplotlib.legend_handler import HandlerTuple

# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

Chapter = 'looselyPackedNP'
sample_name = '8BL-30-IOS-7'
labeltext = '8BL-30-IOS-7 ZFC'

gf_rPlus_file = cwd +   '/data/ES_S16_30K_ZFC_7Oe_Virgin_tranformed_angs_uu_masked_qz_I_corrected.xy'
gf_rMinus_file = cwd +  '/data/ES_S16_30K_ZFC_7Oe_Virgin_tranformed_angs_du_masked_qz_I_corrected.xy'
sat_rPlus_file = cwd +  '/data/ES_S16_30K_ZFC_7300Oe_tranformed_angs_uu_masked_qz_I_corrected.xy'
sat_rMinus_file = cwd + '/data/ES_S16_30K_ZFC_7300Oe_tranformed_angs_du_masked_qz_I_corrected.xy'
rem_rPlus_file = cwd +  '/data/ES_S16_30K_ZFC_7Oe_Remanence_tranformed_angs_uu_masked_qz_I_corrected.xy'
rem_rMinus_file = cwd + '/data/ES_S16_30K_ZFC_7Oe_Remanence_tranformed_angs_du_masked_qz_I_corrected.xy'

q_min, q_max = 0.05, 1.2
I_min, I_max = 1e-6, 1.9e2


refl_pngfile = f"{Chapter}_VerticalStructure_{sample_name}_PNR_ZFC30K.png"


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
  valid_data = sI/I < 0.7
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
p_gf_p = ax.errorbar(q_gf_p, I_gf_p*sf_gf, sI_gf_p*sf_gf,
  label='ZFC, GF, $R^{+}$',
  zorder=0, capsize=0, ls='-', marker='.', markersize=1, color='#793394')
p_gf_m = ax.errorbar(q_gf_m, I_gf_m*sf_gf, sI_gf_m*sf_gf,
  label='ZFC, GF, $R^{-}$',
  zorder=0, capsize=0, ls='-', marker='.', markersize=1, color='#7F0128')

p_sat_p = ax.errorbar(q_sat_p, I_sat_p*sf_sat, sI_sat_p*sf_sat,
  label='730 mT, $R^{+}$',
  zorder=0, capsize=0, ls='-', marker='.', markersize=1)
p_sat_m = ax.errorbar(q_sat_m, I_sat_m*sf_sat, sI_sat_m*sf_sat,
  label='730 mT, $R^{-}$',
  zorder=0, capsize=0, ls='-', marker='.', markersize=1)

p_rem_p = ax.errorbar(q_rem_p, I_rem_p, sI_rem_p,
  label='Remanence, $R^{+}$',
  zorder=0, capsize=0, ls='-', marker='.', markersize=1)
p_rem_m = ax.errorbar(q_rem_m, I_rem_m, sI_rem_m,
  label='Remanence, $R^{-}$',
  zorder=0, capsize=0, ls='-', marker='.', markersize=1)

handles, labels = ax.get_legend_handles_labels()

ax.legend(
  [(handles[0], handles[1]),
   (handles[2], handles[3]),
   (handles[4], handles[5])],
  ['Initial', '730 mT', 'Remanence'],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  bbox_to_anchor = [0.53, 0.56])

ax.text(0.58, 0.9, '$R^{+}, \, R^{-}$',
  transform=ax.transAxes, fontsize=10)
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, nm^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax.text(0.025, 0.025, labeltext,
  transform=ax.transAxes, fontsize=10)
fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)
