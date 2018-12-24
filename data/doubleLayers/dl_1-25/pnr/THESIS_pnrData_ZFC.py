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
from modelexp.data import MftData
import matplotlib.patches as mpatches

from matplotlib.legend_handler import HandlerTuple

# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'DL-1-25'
labeltext = 'DL-1.25%'
Chapter = 'doubleLayers'

gf_rPlus_file = cwd +   '/mftFiles/DD205_3_5K_10mT_u.mft'
gf_rMinus_file = cwd +  '/mftFiles/DD205_3_5K_10mT_d.mft'
sat_rPlus_file = cwd +  '/mftFiles/DD205_3_5K_6000mT_u.mft'
sat_rMinus_file = cwd + '/mftFiles/DD205_3_5K_6000mT_d.mft'
neg_rPlus_file = cwd +  '/mftFiles/DD205_3_5K_-100mT_d.mft'
neg_rMinus_file = cwd + '/mftFiles/DD205_3_5K_-100mT_u.mft'


q_min, q_max = 0.009, 0.19
I_min, I_max = 1e-7, 2.9e2

refl_pngfile = f"{Chapter}_VerticalStructure_{sample_name}_PNR_ZFC5K.png"

def get_data(file):
  data = MftData()
  data.loadFromFile(file)
  q, I, sI = data.getData()
  q = np.array(q)
  I = np.array(I)
  sI = np.array(sI)
  valid_data = sI/I < 0.9
  q = q[valid_data]
  I = I[valid_data]
  sI = sI[valid_data]
  return q, I, sI

#load data
q_gf_p, I_gf_p, sI_gf_p = get_data(gf_rPlus_file)
q_gf_m, I_gf_m, sI_gf_m = get_data(gf_rMinus_file)
q_sat_p, I_sat_p, sI_sat_p = get_data(sat_rPlus_file)
q_sat_m, I_sat_m, sI_sat_m = get_data(sat_rMinus_file)
q_neg_p, I_neg_p, sI_neg_p = get_data(neg_rPlus_file)
q_neg_m, I_neg_m, sI_neg_m = get_data(neg_rMinus_file)

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
  linestyle='None',
  label='ZFC, GF, $R^{+}$',
  zorder=0, capsize=0, marker='.', markersize=1, color='#793394')
p_gf_m = ax.errorbar(q_gf_m, I_gf_m*sf_gf, sI_gf_m*sf_gf,
  linestyle='None',
  label='ZFC, GF, $R^{-}$',
  zorder=0, capsize=0, marker='.', markersize=1, color='#7F0128')

p_sat_p = ax.errorbar(q_sat_p, I_sat_p*sf_sat, sI_sat_p*sf_sat,
  linestyle='None',
  label='6 T, $R^{+}$',
  zorder=0, capsize=0, marker='.', markersize=1)
p_sat_m = ax.errorbar(q_sat_m, I_sat_m*sf_sat, sI_sat_m*sf_sat,
  linestyle='None',
  label='6 T, $R^{-}$',
  zorder=0, capsize=0, marker='.', markersize=1)

p_neg_p = ax.errorbar(q_neg_p, I_neg_p, sI_neg_p,
  linestyle='None',
  label='-100 mT, $R^{+}$',
  zorder=0, capsize=0, marker='.', markersize=1)
p_neg_m = ax.errorbar(q_neg_m, I_neg_m, sI_neg_m,
  linestyle='None',
  label='-100 mT, $R^{-}$',
  zorder=0, capsize=0, marker='.', markersize=1)

handles, labels = ax.get_legend_handles_labels()

ax.legend(
  [(handles[0], handles[1]),
   (handles[2], handles[3]),
   (handles[4], handles[5])],
  ['Initial', '6 T', '-100 mT'],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  bbox_to_anchor = [0.525, 0.47],
  bbox_transform=fig.transFigure)

ax.text(0.01, 0.35, '$R^{+}, \, R^{-}$',
  transform=ax.transAxes, fontsize=10)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, \AA^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax.text(0.975, 0.975, labeltext,
  transform=ax.transAxes,
  verticalalignment='top',
  horizontalalignment='right',
  fontsize=10)
fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)
