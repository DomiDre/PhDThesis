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

sample_name = 'Ac_CoFe_C'
Chapter = 'monolayers'

saxs_fit_file_sphere = cwd + "/sphereModel/saxs/fit_result.dat"
saxs_sld_file_sphere = cwd + "/sphereModel/saxs/fit_sld.dat"

saxs_fit_file_cube = cwd + "/cubeModel/saxs/fit_result.dat"
saxs_sld_file_cube = cwd + "/cubeModel/saxs/fit_sld.dat"

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

p_sphere, q_sphere, I_sphere, sI_sphere, Imodel_sphere = get_data(saxs_fit_file_sphere)
p_superball, q_superball, I_superball, sI_superball, Imodel_superball = get_data(saxs_fit_file_superball)
p_cube, q_cube, I_cube, sI_cube, Imodel_cube = get_data(saxs_fit_file_cube)

bg = 0#params['bg']['value']
left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_inset = fig.add_axes([left+0.03, bottom+0.03, 0.4, 0.4])

ax.errorbar(q_sphere, I_sphere, sI_sphere,
  linestyle='None',
  label='Ac-CoFe-C', zorder=0, capsize=0, marker='.', alpha=1)

ax.plot(q_sphere, Imodel_sphere, marker='None', linestyle='-',
  label='Sphere', zorder=1, alpha=0.8)

ax.plot(q_superball, Imodel_superball, marker='None', linestyle='-',
  label='Superball', zorder=1, alpha=0.8)

ax.plot(q_cube, Imodel_cube, marker='None', linestyle='-',
  label='Cube', zorder=1, alpha=0.8)


ax_inset.errorbar(q_sphere, I_sphere, sI_sphere, marker='.', linestyle='None', zorder=0, alpha=1)
ax_inset.plot(q_sphere, Imodel_sphere, marker='None', linestyle='-', zorder=1, alpha=0.8)
ax_inset.plot(q_superball, Imodel_superball, marker='None', linestyle='-', zorder=1, alpha=0.8)
ax_inset.plot(q_cube, Imodel_cube, marker='None', linestyle='-', zorder=1, alpha=0.8)

# ax.text(0.12, 0.35, '',
#   horizontalalignment='left',
#   verticalalignment='bottom',
#   transform=ax.transAxes,
#   fontsize=inset_fontsize)

ax.legend(loc='upper right', fontsize=inset_fontsize)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\,cm^{-1}$")
ax.set_xlim([1.5e-2, 0.25])
ax.set_ylim([1.1e-3, 4e1])

ax_inset.set_xscale('log')
ax_inset.set_yscale('log')
ax_inset.set_xlim([0.05, 0.2])
ax_inset.set_ylim([1e-2, 5e-1])
ax_inset.set_xlim([0.07, 0.14])
ax_inset.set_ylim([2e-2, 3e-1])
ax_inset.get_xaxis().set_visible(False)
ax_inset.get_yaxis().set_visible(False)
fig.savefig(thesisimgs + '/' + pngfile)
fig.savefig(cwd + '/' + pngfile)