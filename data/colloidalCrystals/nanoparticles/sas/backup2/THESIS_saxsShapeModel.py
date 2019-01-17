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

saxs_fit_file_superball = cwd + "/superballModel/saxs/fit_result.dat"
saxs_sld_file_superball = cwd + "/superballModel/saxs/fit_sld.dat"

pngfile = Chapter + '_SAS_' + sample_name + "_ShapeModelStudy.png"

#load data
def get_data(fit_result):
  data = MultiData(XyemData)
  data.loadFromFile(fit_result)
  q, I, sI, Imodel = data.getDataset(0).getData()
  params = data.params
  return params, q, I, sI, Imodel

def get_sld(sld_file):
  data = MultiData(XyData)
  data.loadFromFile(sld_file)
  z, sld = data.getDataset(0).getData()
  return z, sld

p_superball, q_superball, I_superball, sI_superball, Imodel_superball = get_data(saxs_fit_file_superball)
z, sld =  get_sld(saxs_sld_file_superball)

left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])

ax.errorbar(q_superball, I_superball, sI_superball,
  linestyle='None',
  label='SAXS @ GALAXI', zorder=0, capsize=0, marker='.', alpha=1)

ax.plot(q_superball, Imodel_superball, marker='None', linestyle='-',
  label='Superball Core-Shell', color='#FAAB2D', zorder=1, alpha=0.8)

ax_sld.plot(z, sld, marker='None', color='#FAAB2D', zorder=2)

ax.text(0.12, 0.18, 'Ol-CoFe-C',
  horizontalalignment='left',
  verticalalignment='bottom',
  transform=ax.transAxes,
  fontsize=inset_fontsize)

ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\,cm^{-1}$")
ax.set_xlim([1.5e-2, 0.25])
ax.set_ylim([1.1e-3, 4e2])


ax_sld.set_xlabel("$\mathit{r} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(r"$\rho_{el} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 2, 4, 6, 8])
ax_sld.set_yticks([0, 25, 50])
ax_sld.set_xlim([0, 9.9])
ax_sld.set_ylim([0, 59])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)
fig.savefig(thesisimgs + '/' + pngfile)
fig.savefig(cwd + '/' + pngfile)