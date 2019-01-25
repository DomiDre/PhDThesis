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
from modelexp.data import MultiData, XyemData, XyData, XyeData

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'Ol-Fe-C'
Chapter = 'colloidalCrystals'

# expData_sa = cwd + "/experimental_data/DD144_0A_nuc_SA.dat"
# expData_la = cwd + "/experimental_data/DD144_0A_nuc_LA.dat"
# modelData = cwd + "/superballModel/sans/simulated_model.xy"
# sldFile  = cwd + "/superballModel/sans/simulated_model_sld.xy"
modelData = cwd + "/superballModel/sans/fit_result.dat"
sldFile  = cwd + "/superballModel/sans/fit_sld.dat"

q_min, q_max = 0.5e-2, 0.17
I_min, I_max = 2.5e-3, 7e0

sans_legend_label = "SANS @ D33"

sans_pngfile = Chapter+'_SAS_'+\
                sample_name+"_SANS.png"

#load data
data = MultiData(XyemData)
data.loadFromFile(modelData)
sans_sa_q, sans_sa_I, sans_sa_sI, sans_sa_Imodel = data.getDatasetBySuffix('sa').getData()
sans_la_q, sans_la_I, sans_la_sI, sans_la_Imodel = data.getDatasetBySuffix('la').getData()

# sans_sa_q_model, sans_sa_Imodel = data.getDatasetBySuffix('sa').getData()
# sans_la_q_model, sans_la_Imodel = data.getDatasetBySuffix('la').getData()

# data = XyeData()
# data.loadFromFile(expData_sa)
# sans_sa_q, sans_sa_I, sans_sa_sI = data.getData()
# data = XyeData()
# data.loadFromFile(expData_la)
# sans_la_q, sans_la_I, sans_la_sI = data.getData()

#load sld
sldData = XyData()
sldData.loadFromFile(sldFile)
sans_r, sans_sld = sldData.getData()
# sans_r /= 10
# sans_sld *= 1e6
sans_q_min, sans_q_max = None, None

left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])

ax.errorbar(sans_sa_q, sans_sa_I, sans_sa_sI,\
  linestyle='None', color='#0EA8DF',\
  label=sans_legend_label, zorder=0, capsize=0, marker='.')
ax.plot(sans_sa_q, sans_sa_Imodel, marker='None', linestyle='-',\
  color=color_variant('#0EA8DF', -150), zorder=1)

ax.errorbar(sans_la_q, sans_la_I, sans_la_sI,\
  linestyle='None', color=color_variant('#0EA8DF', -50),\
  zorder=0, capsize=0, marker='.')
ax.plot(sans_la_q, sans_la_Imodel, marker='None', linestyle='-',\
  color=color_variant('#0EA8DF', -150), zorder=1)

ax.text(0.11, 0.12,
  'Ol-Fe-C\n3 months after synthesis',
  color='black',
  fontsize=inset_fontsize,
  horizontalalignment='left',
  verticalalignment='bottom',
  transform=ax.transAxes)

ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\,cm^{-1}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax_sld.plot(sans_r, sans_sld, marker='None',
  color='#0EA8DF')
ax_sld.set_xlabel("$\mathit{r} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(r"$\rho_{nuc} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 2, 4, 6, 8])
ax_sld.set_yticks([0, 2, 4, 6, 8])
ax_sld.set_xlim([0, 9])
ax_sld.set_ylim([0, 9])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)


fig.savefig(thesisimgs + '/' + sans_pngfile)
fig.savefig(cwd + '/' + sans_pngfile)