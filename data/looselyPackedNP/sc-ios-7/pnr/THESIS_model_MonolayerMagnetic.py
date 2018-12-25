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

from PlottingTemplates.saxssanssanspol import colors, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')
inset_fontsize=10
sample_name = 'SC-IOS-7'
Chapter = 'looselyPackedNP'
fit_file = cwd + "/3MagneticFit/fit_result.dat"
sld_file = cwd + "/3MagneticFit/fit_sld.dat"

labeltext = 'SC-IOS-7'
q_min, q_max = 0.05, 0.635
I_min, I_max = 5e-5, 1.9e0

refl_pngfile = f"{Chapter}_VerticalStructure_{sample_name}_PNR300K_500mT.png"

def get_clean_data(data):
  q_p, I_p, sI_p, Imodel_p = data.getDatasetBySuffix('p').getData()
  q_m, I_m, sI_m, Imodel_m = data.getDatasetBySuffix('m').getData()
  q_p = np.array(q_p)
  I_p = np.array(I_p)
  sI_p = np.array(sI_p)
  Imodel_p = np.array(Imodel_p)
  q_m = np.array(q_m)
  I_m = np.array(I_m)
  sI_m = np.array(sI_m)
  Imodel_m = np.array(Imodel_m)

  valid_data = sI_p/I_p < 0.5
  q_p = q_p[valid_data]
  I_p = I_p[valid_data]
  sI_p = sI_p[valid_data]
  Imodel_p = Imodel_p[valid_data]
  valid_data = sI_m/I_m < 0.5
  q_m = q_m[valid_data]
  I_m = I_m[valid_data]
  sI_m = sI_m[valid_data]
  Imodel_m = Imodel_m[valid_data]
  return q_p*10, I_p, sI_p, Imodel_p, q_m*10, I_m, sI_m, Imodel_m

#load data
data = MultiData(XyemData)
data.loadFromFile(fit_file)
q_p, I_p, sI_p, Imodel_p, q_m, I_m, sI_m, Imodel_m = get_clean_data(data)
# print(data.chi2)
#load sld
sldData = MultiData(XyeData)
sldData.loadFromFile(sld_file)
r, sld, sldMag = sldData.getDataset(0).getData()

left, bottom = 0.19, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])
ax.errorbar(q_p, I_p, sI_p,\
  linestyle='None', color=colors['sanspol_p_sa_data'],
  label='$R^{+}$', zorder=0, capsize=0, marker='.')
ax.errorbar(q_m, I_m, sI_m,\
  linestyle='None', color=colors['sanspol_m_sa_data'],
  label='$R^{-}$', zorder=0, capsize=0, marker='.')
ax.plot(q_p, Imodel_p, zorder=1, color=color_variant(colors['sanspol_p_sa_data'], -100), marker='None')
ax.plot(q_m, Imodel_m, zorder=1, color=color_variant(colors['sanspol_m_sa_data'], -100), marker='None')
ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, nm^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax.text(0.05, 0.25, labeltext,
  transform=ax.transAxes, fontsize=inset_fontsize)
ax_sld.plot(r, sld, marker='None', alpha=0.3,
  color=colors['sanspol_sld'])
ax_sld.plot(r, sldMag, marker='None',
  color='#EE292F')
ax_sld.set_xlabel("$\mathit{z} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(r"$\mathit{\rho}_{mag} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 25, 50, 75])
ax_sld.set_yticks([0, 1])
ax_sld.set_xlim([-10, 90])
ax_sld.set_ylim([0, 1.2])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)

fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)
