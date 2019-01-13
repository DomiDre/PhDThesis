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

sample_name = 'DD144'
Chapter = ''
fit_file = cwd + "/intermediateResult.dat"
sld_file = cwd + "/fit_sld.dat"

q_min, q_max = 9e-3, 0.3

I_min, I_max = 7e-4, 2e3

saxs_legend_label = "SAXS @ GALAXI"

saxs_pngfile = Chapter+'_SAS_'+\
                sample_name+"_SASFit.png"

#load data
data = MultiData(XyemData)
data.loadFromFile(fit_file)
saxs_q, saxs_I, saxs_sI, saxs_Imodel = data.getDataset(0).getData()

# #load sld
# sldData = MultiData(XyData)
# sldData.loadFromFile(sld_file)
# # saxs_r, saxs_sld = sldData.getDataset(0).getData()
# saxs_r, saxs_sld = sldData.getDataset(0).getData()

left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
# ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])

ax.errorbar(saxs_q, saxs_I, saxs_sI,\
  linestyle='None', color=colors['saxs_data'],\
  label=saxs_legend_label, zorder=0, capsize=0, marker='.')
ax.plot(saxs_q, saxs_Imodel, marker='None', linestyle='-',\
  color=colors['saxs_sans_model'], zorder=1)


ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\,cm^{-1}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

# ax_sld.plot(saxs_r, saxs_sld, marker='None',
#   color=colors['sans_sa_data'])
# ax_sld.set_xlabel("$\mathit{r} \,/\,nm$", fontsize=inset_fontsize)
# ax_sld.set_ylabel("$SLD \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
# ax_sld.set_xticks([0, 2, 4, 6, 8])
# ax_sld.set_yticks([0, 5, 10])
# ax_sld.set_xlim([0, 9])
# ax_sld.set_ylim([0, 59])
# ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)


# fig.savefig(thesisimgs + '/' + saxs_pngfile)
fig.savefig(cwd + '/' + saxs_pngfile)