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
from modelexp.data import XyeData, XyemData, MultiData
import matplotlib.patches as mpatches
from PlottingTemplates.saxssanssanspol import color_variant, colors

from matplotlib.legend_handler import HandlerTuple

# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

Chapter = 'looselyPackedNP'
sample_name = 'SC-IOS-7'
labeltext = 'SC-IOS-7 ZFC'

sat_rPlus_file = cwd  + '/data/footprint_corrected/ES_S17_30K_FC_73000Oe_reduced_in_x_ai_uu_masked_qz_I_fcorrected.xye'

gf_rPlus_file = cwd +   '/data/footprint_corrected/ES_S17_30K_ZFC_7Oe_reduced_in_x_ai_uu_masked_qz_I_fcorrected.xye'
gf_rMinus_file = cwd +  '/data/footprint_corrected/ES_S17_30K_ZFC_7Oe_reduced_in_x_ai_du_masked_qz_I_fcorrected.xye'
sat_rPlus_file = cwd  + '/data/footprint_corrected/ES_S17_30K_ZFC_7300Oe_reduced_in_x_ai_uu_masked_qz_I_fcorrected.xye'
sat_rMinus_file = cwd + '/data/footprint_corrected/ES_S17_30K_ZFC_7300Oe_reduced_in_x_ai_du_masked_qz_I_fcorrected.xye'
rem_rPlus_file = cwd +  '/data/footprint_corrected/ES_S17_30K_ZFC_7Oe_Remanence_reduced_in_x_ai_uu_masked_qz_I_fcorrected.xye'
rem_rMinus_file = cwd + '/data/footprint_corrected/ES_S17_30K_ZFC_7Oe_Remanence_reduced_in_x_ai_du_masked_qz_I_fcorrected.xye'

q_min, q_max = 0.05, 1.2
I_min, I_max = 7e-5, 1.9e2

fit_fileZFC_ini = cwd + "/2FitZFC/Initial/fit_result.dat"
sld_fileZFC_ini = cwd + "/2FitZFC/Initial/fit_sld.dat"

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
  valid_data = sI/I < 1
  q = q[valid_data]
  I = I[valid_data]
  sI = sI[valid_data]
  return q*10, I, sI



def get_fit_data(file):
  data = MultiData(XyemData)
  data.loadFromFile(file)
  q_p, I_p, sI_p, Imodel_p = data.getDatasetBySuffix('p').getData()
  q_p = np.array(q_p)
  I_p = np.array(I_p)
  sI_p = np.array(sI_p)
  Imodel_p = np.array(Imodel_p)
  q_m, I_m, sI_m, Imodel_m = data.getDatasetBySuffix('m').getData()
  q_m = np.array(q_m)
  I_m = np.array(I_m)
  sI_m = np.array(sI_m)
  Imodel_m = np.array(Imodel_m)
  return q_p*10, I_p, sI_p, Imodel_p, q_m*10, I_m, sI_m, Imodel_m
q_ini_p_fit, I_ini_p_fit, sI_ini_p_fit, Imodel_ini_p_fit, q_ini_m_fit, I_ini_m_fit, sI_ini_m_fit, Imodel_ini_m_fit = get_fit_data(fit_fileZFC_ini)

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
  linestyle='-',
  label='ZFC, GF, $R^{+}$',
  zorder=0, capsize=0, marker='.', markersize=1, color='#793394')
p_gf_m = ax.errorbar(q_gf_m, I_gf_m*sf_gf, sI_gf_m*sf_gf,
  linestyle='-',
  label='ZFC, GF, $R^{-}$',
  zorder=0, capsize=0, marker='.', markersize=1, color='#7F0128')

p_sat_p = ax.errorbar(q_sat_p, I_sat_p*sf_sat, sI_sat_p*sf_sat,
  linestyle='-',
  label='730 mT, $R^{+}$',
  zorder=0, capsize=0, marker='.', markersize=1)
p_sat_m = ax.errorbar(q_sat_m, I_sat_m*sf_sat, sI_sat_m*sf_sat,
  linestyle='-',
  label='730 mT, $R^{-}$',
  zorder=0, capsize=0, marker='.', markersize=1)

p_rem_p = ax.errorbar(q_rem_p, I_rem_p, sI_rem_p,
  linestyle='-',
  label='Remanence, $R^{+}$',
  zorder=0, capsize=0, marker='.', markersize=1)
p_rem_m = ax.errorbar(q_rem_m, I_rem_m, sI_rem_m,
  linestyle='-',
  label='Remanence, $R^{-}$',
  zorder=0, capsize=0, marker='.', markersize=1)

ax.plot(q_ini_p_fit, Imodel_ini_p_fit*sf_gf, zorder=1, color=color_variant('#793394', -50), marker='None', alpha=0.5)
ax.plot(q_ini_m_fit, Imodel_ini_m_fit*sf_gf, zorder=1, color=color_variant('#7F0128', -50), marker='None', alpha=0.5)


handles, labels = ax.get_legend_handles_labels()

ax.legend(
  [(handles[0], handles[1]),
   (handles[2], handles[3]),
   (handles[4], handles[5])],
  ['Initial', '730 mT', 'Remanence'],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  bbox_to_anchor = [0.53, 0.49])

ax.text(0.58, 0.9, labeltext,
  transform=ax.transAxes, fontsize=10)
ax.text(0.58, 0.83, '$R^{+}, R^{-}$',
  transform=ax.transAxes, fontsize=10)
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, nm^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)
