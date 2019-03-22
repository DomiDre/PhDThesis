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
from modelexp.data import MultiData, XyData, XyemData

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'Ac_CoFe_C'
Chapter = 'monolayers'


fit_file = cwd + "/superballModel/sans/fit_result.dat"
sld_file = cwd + "/superballModel/sans/fit_sld.dat"

pngfile = Chapter + '_SAS_' + sample_name + "_SANS.png"

modelRef = MultiData(XyemData)
modelRef.loadFromFile(fit_file)
q_sa, I_sa, sI_sa, Imodel_sa = modelRef.getDataset(0).getData()
q_la, I_la, sI_la, Imodel_la = modelRef.getDataset(1).getData()

sldData = MultiData(XyData)
sldData.loadFromFile(sld_file)
r, sld = sldData.getDatasetBySuffix('sa').getData()
r_part = r[:6]
sld_part = sld[:6]
r_oa = r[12:16]
sld_oa = sld[12:16]

left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])

ax.errorbar(q_sa, I_sa, sI_sa,
  linestyle='None',
  color=colors['sans_sa_data'],
  label='SANS', zorder=0, capsize=0, marker='.', alpha=1)

ax.errorbar(q_la, I_la, sI_la,
  linestyle='None',
  color=colors['sans_la_data'],
  zorder=0, capsize=0, marker='.', alpha=1)

ax.plot(q_sa, Imodel_sa, marker='None', linestyle='-',
  color='black',
  zorder=2, alpha=0.8)

ax.plot(q_la, Imodel_la, marker='None', linestyle='-',
  color='black',
  zorder=2, alpha=0.8)
ax.text(0.05, 0.18, 'Ac-CoFe-C',
  horizontalalignment='left',
  verticalalignment='bottom',
  transform=ax.transAxes)
ax_sld.plot(r_part, sld_part, marker='None', color='#FAAB2D', zorder=2, label="NP")
ax_sld.plot(r_oa, sld_oa, marker='None', color='#0EA8DF', zorder=1, alpha=0.5, label="OA")

ax_sld.set_xlabel("$\mathit{r} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(r"$\rho_{nuc} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 2, 4, 6, 8])
ax_sld.set_yticks([0, 2, 4, 6, 8])
ax_sld.set_xlim([0, 9.9])
ax_sld.set_ylim([0, 9.9])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)
ax_sld.legend(fontsize=8, loc='upper', ncol=2)

ax.legend(loc='lower left')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\,cm^{-1}$")
ax.set_xlim([1e-2, 0.2])
ax.set_ylim([3e-3, 3e0])

fig.savefig(cwd + '/' + pngfile)