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
from PlottingTemplates.saxssanssanspol import color_variant

from matplotlib.legend_handler import HandlerTuple

# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

Chapter = 'looselyPackedNP'
sample_name = 'SC-IOS-11'
labeltext = 'SC-IOS-11 FC'

sat_rPlus_file = cwd  + '/data/30Kfiles/ES_S14_30K_730mT_FC_reduced_in_x_ai_uu_qz_I_fcorrected.xye'
sat_rMinus_file = cwd + '/data/30Kfiles/ES_S14_30K_730mT_FC_reduced_in_x_ai_dd_qz_I_fcorrected.xye'
sat_sf_file = cwd     + '/data/30Kfiles/ES_S14_30K_730mT_FC_reduced_in_x_ai_du_qz_I_fcorrected.xye'
rem_rPlus_file = cwd +  '/data/30Kfiles/ES_S14_30K_2mT_FC_Remanence_reduced_in_x_ai_uu_qz_I_fcorrected.xye'
rem_rMinus_file = cwd + '/data/30Kfiles/ES_S14_30K_2mT_FC_Remanence_reduced_in_x_ai_dd_qz_I_fcorrected.xye'
rem_sf_file = cwd    +  '/data/30Kfiles/ES_S14_30K_2mT_FC_Remanence_reduced_in_x_ai_du_qz_I_fcorrected.xye'


q_min, q_max = 0.05, 1.2
I_min, I_max = 1e-6, 1.9e1

refl_pngfile = f"{Chapter}_VerticalStructure_{sample_name}_PNR_FC30K.png"

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
q_sat_p, I_sat_p, sI_sat_p = get_data(sat_rPlus_file)
q_sat_m, I_sat_m, sI_sat_m = get_data(sat_rMinus_file)
q_sat_sf, I_sat_sf, sI_sat_sf = get_data(sat_sf_file)

q_rem_p, I_rem_p, sI_rem_p = get_data(rem_rPlus_file)
q_rem_m, I_rem_m, sI_rem_m = get_data(rem_rMinus_file)
q_rem_sf, I_rem_sf, sI_rem_sf = get_data(rem_sf_file)

# qmin_rem = 0.16
# sf_rem = 0.4
# valid_rem_p = q_rem_p > qmin_rem
# q_rem_p = q_rem_p[valid_rem_p]
# I_rem_p = I_rem_p[valid_rem_p]*sf_rem
# sI_rem_p = sI_rem_p[valid_rem_p]*sf_rem

# valid_rem_m = q_rem_m > qmin_rem
# q_rem_m = q_rem_m[valid_rem_m]
# I_rem_m = I_rem_m[valid_rem_m]*sf_rem
# sI_rem_m = sI_rem_m[valid_rem_m]*sf_rem

# valid_rem_sf = q_rem_sf > qmin_rem
# q_rem_sf = q_rem_sf[valid_rem_sf]
# I_rem_sf = I_rem_sf[valid_rem_sf]*sf_rem
# sI_rem_sf = sI_rem_sf[valid_rem_sf]*sf_rem



left, bottom = 0.19, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

sf_gf = 1e2
sf_sat = 1e1
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax.errorbar(q_sat_p, I_sat_p*sf_sat, sI_sat_p*sf_sat,
  linestyle='-',
  label='1.08 T, $R^{++}$',
  zorder=0, capsize=0, marker='.', markersize=1)
ax.errorbar(q_sat_m, I_sat_m*sf_sat, sI_sat_m*sf_sat,
  linestyle='-',
  label='1.08 T, $R^{--}$',
  zorder=0, capsize=0, marker='.', markersize=1)

ax.errorbar(q_rem_p, I_rem_p, sI_rem_p,
  linestyle='-',
  label='Remanence, $R^{++}$',
  zorder=0, capsize=0, marker='.', markersize=1)
ax.errorbar(q_rem_m, I_rem_m, sI_rem_m,
  linestyle='-',
  label='Remanence, $R^{--}$',
  zorder=0, capsize=0, marker='.', markersize=1)

ax.errorbar(q_sat_sf, I_sat_sf, sI_sat_sf,
  linestyle='-',
  label='1.08 T, $R^{-+}$',
  color=color_variant('#0EA8DF',-100),
  zorder=0, capsize=0, marker='.', markersize=1)
ax.errorbar(q_rem_sf, I_rem_sf, sI_rem_sf,
  linestyle='-',
  label='Remanence, $R^{-+}$',
  color=color_variant('#FAAB2D',-100),
  zorder=0, capsize=0, marker='.', markersize=1)

handles, labels = ax.get_legend_handles_labels()

ax.legend(
  [(handles[0], handles[1], handles[4]),
   (handles[2], handles[3], handles[5])],
  ['730 mT', 'Remanence'],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  bbox_to_anchor = [0.5, 0.62])


ax.text(0.55, 0.93, labeltext,
  transform=ax.transAxes, fontsize=10)
ax.text(0.55, 0.86, '$R^{++}, R^{--}, R^{-+}$',
  transform=ax.transAxes, fontsize=10)
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, nm^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)
