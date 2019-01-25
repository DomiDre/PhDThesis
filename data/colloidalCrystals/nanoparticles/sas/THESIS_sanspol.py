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

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'Ol-Fe-C'
Chapter = 'colloidalCrystals'
fit_file = cwd + "/superballModel/sanspol/fit_result.dat"
sld_file = cwd + "/superballModel/sanspol/fit_sld.dat"

# expData_p_sa = cwd + "/experimental_data/50A/DD144_50A_20deg_SA_rfm.dat"
# expData_p_la = cwd + "/experimental_data/50A/DD144_50A_20deg_LA_rfm.dat"
# expData_m_sa = cwd + "/experimental_data/50A/DD144_50A_20deg_SA_rfp.dat"
# expData_m_la = cwd + "/experimental_data/50A/DD144_50A_20deg_LA_rfp.dat"

expData_sa = cwd + "/experimental_data/DD144_0A_nuc_SA.dat"
expData_la = cwd + "/experimental_data/DD144_0A_nuc_LA.dat"

q_min, q_max = 0.5e-2, 0.17
I_min, I_max = 2.5e-3, 35e0#1.5e-3, 12e0

sanspol_p_legend_label = "I(+) SANSPOL @ D33"
sanspol_m_legend_label = "I(-) SANSPOL @ D33"

sanspol_pngfile = Chapter+'_SAS_'+\
                sample_name+"_SANSPOL.png"


def get_clean_data(data, suffix):
  q, I, sI, Imodel = data.getDatasetBySuffix(suffix).getData()
  q = np.array(q)
  I = np.array(I)
  sI = np.array(sI)
  Imodel = np.array(Imodel)
  valid_data = sI/I < 0.5
  q = q[valid_data]
  I = I[valid_data]
  sI = sI[valid_data]
  Imodel = Imodel[valid_data]
  return q, I, sI, Imodel

data = XyeData()
data.loadFromFile(expData_sa)
sans_sa_q, sans_sa_I, sans_sa_sI = data.getData()
data = XyeData()
data.loadFromFile(expData_la)
sans_la_q, sans_la_I, sans_la_sI = data.getData()

#load data
data = MultiData(XyemData)
data.loadFromFile(fit_file)
sanspol_p_la_q, sanspol_p_la_I, sanspol_p_la_sI, sanspol_p_la_Imodel = get_clean_data(data, 'p_la')
sanspol_m_la_q, sanspol_m_la_I, sanspol_m_la_sI, sanspol_m_la_Imodel = get_clean_data(data, 'm_la')
sanspol_p_sa_q, sanspol_p_sa_I, sanspol_p_sa_sI, sanspol_p_sa_Imodel = get_clean_data(data, 'p_sa')
sanspol_m_sa_q, sanspol_m_sa_I, sanspol_m_sa_sI, sanspol_m_sa_Imodel = get_clean_data(data, 'm_sa')

#load sld
sldData = MultiData(XyemData)
sldData.loadFromFile(sld_file)
sanspol_p_la_r, sanspol_p_la_sld, sanspol_p_la_rMag, sanspol_p_la_sldMag = sldData.getDatasetBySuffix('p_la').getData()
sanspol_m_la_r, sanspol_m_la_sld, sanspol_m_la_rMag, sanspol_m_la_sldMag = sldData.getDatasetBySuffix('m_la').getData()
sanspol_p_sa_r, sanspol_p_sa_sld, sanspol_p_sa_rMag, sanspol_p_sa_sldMag = sldData.getDatasetBySuffix('p_sa').getData()
sanspol_m_sa_r, sanspol_m_sa_sld, sanspol_m_sa_rMag, sanspol_m_sa_sldMag = sldData.getDatasetBySuffix('m_sa').getData()


# data = XyeData()
# data.loadFromFile(expData_p_sa)
# sanspol_p_sa_q, sanspol_p_sa_I, sanspol_p_sa_sI = data.getData()
# data = XyeData()
# data.loadFromFile(expData_p_la)
# sanspol_p_la_q, sanspol_p_la_I, sanspol_p_la_sI = data.getData()
# data = XyeData()
# data.loadFromFile(expData_m_la)
# sanspol_m_la_q, sanspol_m_la_I, sanspol_m_la_sI = data.getData()
# data = XyeData()
# data.loadFromFile(expData_m_sa)
# sanspol_m_sa_q, sanspol_m_sa_I, sanspol_m_sa_sI = data.getData()

# r_part = sanspol_p_la_r[:6]
# sld_part = sanspol_p_la_sld[:6]
# rMag_part = sanspol_p_la_r[:6]
# sldMag_part = sanspol_p_la_sldMag[:6]
# r_oa = sanspol_p_la_r[12:16]
# sld_oa = sanspol_p_la_sld[12:16]


left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])


# ax.errorbar(sans_sa_q, sans_sa_I, sans_sa_sI,\
#   linestyle='None', color='#0EA8DF',\
#   zorder=0, capsize=0, marker='.')

# ax.errorbar(sans_la_q, sans_la_I, sans_la_sI,\
#   linestyle='None', color=color_variant('#0EA8DF', -50),\
#   zorder=0, capsize=0, marker='.')

ax.errorbar(sanspol_p_sa_q, sanspol_p_sa_I, sanspol_p_sa_sI,\
  linestyle='None', color='#76C152',\
  label=sanspol_p_legend_label, zorder=0, capsize=0, marker='.')
ax.plot(sanspol_p_sa_q, sanspol_p_sa_Imodel, marker='None', linestyle='-',\
  color=color_variant('#76C152', -150), zorder=1)

ax.errorbar(sanspol_p_la_q, sanspol_p_la_I, sanspol_p_la_sI,\
  linestyle='None', color=color_variant('#76C152', -50),\
  zorder=0, capsize=0, marker='.')
ax.plot(sanspol_p_la_q, sanspol_p_la_Imodel, marker='None', linestyle='-',\
  color=color_variant('#76C152', -150), zorder=1)

ax.errorbar(sanspol_m_sa_q, sanspol_m_sa_I, sanspol_m_sa_sI,\
  linestyle='None', color='#EE292F',\
  label=sanspol_m_legend_label, zorder=0, capsize=0, marker='.')
ax.plot(sanspol_m_sa_q, sanspol_m_sa_Imodel, marker='None', linestyle='-',\
  color=color_variant('#EE292F', -150), zorder=1)

ax.errorbar(sanspol_m_la_q, sanspol_m_la_I, sanspol_m_la_sI,\
  linestyle='None', color=color_variant('#EE292F', -50),\
  zorder=0, capsize=0, marker='.')
ax.plot(sanspol_m_la_q, sanspol_m_la_Imodel, marker='None', linestyle='-',\
  color=color_variant('#EE292F', -150), zorder=1)


ax.text(0.11, 0.2,
  'Ol-Fe-C\n3 months old',
  color='black',
  horizontalalignment='left',
  verticalalignment='bottom',
  transform=ax.transAxes,
  fontsize=inset_fontsize)

ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\,cm^{-1}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])
# ax_sld.plot(r_part, sld_part, marker='None',
#   color='#EE292F', zorder=2, alpha=0.2)
ax_sld.plot(sanspol_p_la_rMag, sanspol_p_la_sldMag, marker='None',
  color='#FAAB2D', zorder=3)

ax_sld.set_xlabel("$\mathit{r} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(r"$\rho_{mag} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 2, 4, 6, 8])
ax_sld.set_yticks([0, 0.5, 1, 1.5])
ax_sld.set_xlim([0, 9.9])
ax_sld.set_ylim([0, 1.9])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)

fig.savefig(thesisimgs + '/' + sanspol_pngfile)
fig.savefig(cwd + '/' + sanspol_pngfile)