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
from modelexp.data import MultiData, XyemData, XyData

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'Ol_CoFe_C'
Chapter = 'monolayers'
saxs_fit_file = cwd + "/cubeModel/saxs/fit_result.dat"
saxs_sld_file = cwd + "/cubeModel/saxs/fit_sld.dat"

sans_fit_file = cwd + "/cubeModel/sans/fit_result.dat"
sans_sld_file = cwd + "/cubeModel/sans/fit_sld.dat"

q_min, q_max = 1e-2, 0.25
I_min, I_max = 8e-4, 2e2

saxs_legend_label = "SAXS @ GALAXI"
sans_legend_label = "SANS @ D33"

pngfile = Chapter + '_SAS_' + sample_name + "_SASCubeModelFit.png"

#load data
saxs_data = MultiData(XyemData)
saxs_data.loadFromFile(saxs_fit_file)
saxs_q, saxs_I, saxs_sI, saxs_Imodel = saxs_data.getDataset(0).getData()

sans_data = MultiData(XyemData)
sans_data.loadFromFile(sans_fit_file)
sans_sa_q, sans_sa_I, sans_sa_sI, sans_sa_Imodel = sans_data.getDatasetBySuffix('sa').getData()
sans_la_q, sans_la_I, sans_la_sI, sans_la_Imodel = sans_data.getDatasetBySuffix('la').getData()
sans_sa_I, sans_sa_sI, sans_sa_Imodel = np.array(sans_sa_I), np.array(sans_sa_sI), np.array(sans_sa_Imodel)
sans_la_I, sans_la_sI, sans_la_Imodel = np.array(sans_la_I), np.array(sans_la_sI), np.array(sans_la_Imodel)
params = sans_data.params
bg = 0#params['bg']['value']
left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.errorbar(saxs_q, saxs_I, saxs_sI,\
  linestyle='None', color=colors['saxs_data'],\
  label=saxs_legend_label, zorder=0, capsize=0, marker='.', alpha=0.5)
ax.plot(saxs_q, saxs_Imodel, marker='None', linestyle='-',\
  color=colors['saxs_sans_model'], zorder=1, alpha=0.5)

ax.errorbar(sans_sa_q, sans_sa_I-bg, sans_sa_sI,\
  linestyle='None', color=colors['sans_sa_data'],\
  label=sans_legend_label, zorder=0, capsize=0, marker='.', alpha=0.5)
ax.plot(sans_sa_q, sans_sa_Imodel-bg, marker='None', linestyle='-',\
  color=colors['saxs_sans_model'], zorder=1, alpha=0.5)

ax.errorbar(sans_la_q, sans_la_I-bg, sans_la_sI,\
  linestyle='None', color=colors['sans_la_data'],\
  zorder=0, capsize=0, marker='.', alpha=0.5)
ax.plot(sans_la_q, sans_la_Imodel-bg, marker='None', linestyle='-',\
  color=colors['saxs_sans_model'], zorder=1, alpha=0.5)


ax.text(0.12, 0.2, 'Ol-CoFe-C',
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

fig.savefig(thesisimgs + '/' + pngfile)
fig.savefig(cwd + '/' + pngfile)