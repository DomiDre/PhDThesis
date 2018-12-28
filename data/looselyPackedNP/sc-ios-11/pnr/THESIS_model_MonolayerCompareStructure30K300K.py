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

sample_name = 'SC-IOS-11'
Chapter = 'looselyPackedNP'
fit_file300K = cwd + "/0FitSphereLayerCSSWithSpacer/fit_result.dat"
sld_file300K = cwd + "/0FitSphereLayerCSSWithSpacer/fit_sld.dat"

fit_file30K = cwd + "/3FitZFC/Initial/Nuclear/fit_result.dat"
sld_file30K = cwd + "/3FitZFC/Initial/Nuclear/fit_sld.dat"

labeltext = 'SC-IOS-11'
q_min, q_max = 0.05, 1.1
I_min, I_max = 1e-6, 1.9e0

refl_pngfile = f"{Chapter}_VerticalStructure_{sample_name}_PNR_Compare30K300K.png"

def get_clean_data(data):
  q, I, sI, Imodel = data.getDataset(0).getData()
  q = np.array(q)
  I = np.array(I)
  sI = np.array(sI)
  Imodel = np.array(Imodel)
  valid_data = sI/I < 0.5
  q = q[valid_data]
  I = I[valid_data]
  sI = sI[valid_data]
  Imodel = Imodel[valid_data]
  return q*10, I, sI, Imodel

#load data
data = MultiData(XyemData)
data.loadFromFile(fit_file300K)
q300K, I300K, sI300K, Imodel300K = get_clean_data(data)
# print(data.chi2)
#load sld
sldData = MultiData(XyeData)
sldData.loadFromFile(sld_file300K)
r300K, sld300K, sldMag300K = sldData.getDataset(0).getData()


#load data
data = MultiData(XyemData)
data.loadFromFile(fit_file30K)
q30K, I30K, sI30K, Imodel30K = get_clean_data(data)
# print(data.chi2)
#load sld
sldData = MultiData(XyeData)
sldData.loadFromFile(sld_file30K)
r30K, sld30K, sldMag30K = sldData.getDataset(0).getData()

left, bottom = 0.19, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])
ax.errorbar(q30K, I30K, sI30K,\
  linestyle='None', color=colors['sanspol_p_sa_data'],
  label='30 K', zorder=1, capsize=0, marker='.')
ax.plot(q30K, Imodel30K, zorder=2, color='black', marker='None')

ax.errorbar(q300K, I300K, sI300K,\
  linestyle='None', color='gray',
  label='300 K', zorder=0, capsize=0, marker='.')
ax.plot(q300K, Imodel300K, zorder=1, color=color_variant('#202020', 50), marker='None')
ax.legend(loc='lower left', fontsize=10)
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, nm^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax.text(0.05, 0.25, labeltext,
  transform=ax.transAxes, fontsize=10)
ax_sld.plot(r30K, sld30K, marker='None',
  color=color_variant(colors['sanspol_p_sa_data'],-50), zorder=1)
ax_sld.plot(r300K, sld300K, marker='None',
  color=color_variant('#202020', 50), alpha=0.5, zorder=0)
ax_sld.set_xlabel("$\mathit{z} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(r"$\mathit{\rho}_{nuc} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 25, 50, 75])
ax_sld.set_yticks([0, 2, 4])
ax_sld.set_xlim([-10, 90])
ax_sld.set_ylim([0, 4.9])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)

fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)