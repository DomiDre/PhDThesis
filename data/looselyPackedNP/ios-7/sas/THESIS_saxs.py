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

sample_name = 'IOS-7'
Chapter = 'looselyPackedNP'
saxs_fit_file = cwd + "/saxs/SingleMode/fit_result.dat"
saxs_sld_file = cwd + "/saxs/SingleMode/fit_sld.dat"

I_min, I_max = 1.5e-4*2, 3e3*2

saxs_legend_label = "SAXS @ GALAXI"

saxs_pngfile = Chapter+'_SAS_'+\
                sample_name+"_SAXS.png"

#load data
data = MultiData(XyemData)
data.loadFromFile(saxs_fit_file)
saxs_q, saxs_I, saxs_sI, saxs_Imodel = data.getDataset(0).getData()

#load sld
sldData = MultiData(XyData)
sldData.loadFromFile(saxs_sld_file)
saxs_r, saxs_sld = sldData.getDataset(0).getData()
r1 = saxs_r[:8]
sld1 = saxs_sld[:8]

r2 = saxs_r[16:]
sld2 = saxs_sld[16:]

q_min = 1e-2
q_max = 0.5

left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])
ax.errorbar(saxs_q, saxs_I, saxs_sI,\
  linestyle='None', color='#0EA8DF',\
  label=saxs_legend_label, zorder=0, capsize=0, marker='.')
ax.plot(saxs_q, saxs_Imodel, marker='None', linestyle='-',\
  color=color_variant('#0EA8DF', -150), zorder=1)

ax.text(0.11, 0.12,
  'IOS-7',
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

ax_sld.plot(r1, sld1, marker='None', color=colors['saxs_data'], zorder=1)
ax_sld.plot(r2, sld2, marker='None', color=colors['sans_sa_data'], zorder=0)
ax_sld.set_xlabel("$\mathit{r} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(r"$\rho_{el} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 2, 4, 6])
ax_sld.set_yticks([0, 10, 20, 30, 40, 50])
ax_sld.set_xlim([0, 7])
ax_sld.set_ylim([0, 49])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)

fig.savefig(thesisimgs + '/' + saxs_pngfile)
fig.savefig(cwd + '/' + saxs_pngfile)