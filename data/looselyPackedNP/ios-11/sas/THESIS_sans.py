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

sample_name = 'IOS-11'
Chapter = 'looselyPackedNP'
sans_fit_file = cwd + "/sans/Magnetite/fit_result.dat"
sans_sld_file = cwd + "/sans/Magnetite/fit_sld.dat"

q_min, q_max = 1e-2, 0.15
I_min, I_max = 1.5e-3, 3e0

sans_legend_label = "SANS @ D33"

sans_pngfile = Chapter+'_SAS_'+\
                sample_name+"_SANS.png"

#load data
data = MultiData(XyemData)
data.loadFromFile(sans_fit_file)
sans_sa_q, sans_sa_I, sans_sa_sI, sans_sa_Imodel = data.getDatasetBySuffix('sa').getData()
sans_la_q, sans_la_I, sans_la_sI, sans_la_Imodel = data.getDatasetBySuffix('la').getData()

#load sld
sldData = MultiData(XyData)
sldData.loadFromFile(sans_sld_file)
sans_r, sans_sld = sldData.getDatasetBySuffix('sa').getData()
sans_NP_r = sans_r[:7]
sans_NP_sld =  sans_sld[:7]
sans_OA_r = sans_r[11:]
sans_OA_sld =  sans_sld[11:]
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
  'IOS-11',
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

ax_sld.plot(sans_NP_r, sans_NP_sld, marker='None',
  color='#0EA8DF', zorder=2)
ax_sld.plot(sans_OA_r, sans_OA_sld, marker='None',
  color='#FAAB2D', alpha=0.8, zorder=1)
ax_sld.set_xlabel("$\mathit{r} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(r"$\rho_{nuc} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 2, 4, 6, 8])
ax_sld.set_yticks([0, 2, 4, 6, 8])
ax_sld.set_xlim([0, 9])
ax_sld.set_ylim([0, 9])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)


fig.savefig(thesisimgs + '/' + sans_pngfile)
fig.savefig(cwd + '/' + sans_pngfile)