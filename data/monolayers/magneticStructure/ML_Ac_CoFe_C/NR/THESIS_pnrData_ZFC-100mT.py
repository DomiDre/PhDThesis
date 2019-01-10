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
from modelexp.data import XyeData, XyemData, MultiData
import matplotlib.patches as mpatches
from PlottingTemplates.saxssanssanspol import color_variant, colors

from matplotlib.legend_handler import HandlerTuple

# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

Chapter = 'monolayers'
sample_name = 'Ac-CoFe-C'
labeltext = 'ML-Ac-CoFe-C '

fit_fileZFC_rem = cwd + "/-100mT/fit_result.dat"
sld_fileZFC_rem = cwd + "/-100mT/fit_sld.dat"


q_min, q_max = 0.05, 0.99
I_min, I_max = 5e-6, 1.9e0

refl_pngfile = f"{Chapter}_MagneticStructure_{sample_name}_PNR_ZFC5K_neg100mT.png"

def get_fit_data(file):
  data = MultiData(XyemData)
  data.loadFromFile(file)
  q_p, I_p, sI_p, Imodel_p = data.getDatasetBySuffix('m').getData()
  q_p = np.array(q_p)
  I_p = np.array(I_p)
  sI_p = np.array(sI_p)
  Imodel_p = np.array(Imodel_p)
  q_m, I_m, sI_m, Imodel_m = data.getDatasetBySuffix('p').getData()
  q_m = np.array(q_m)
  I_m = np.array(I_m)
  sI_m = np.array(sI_m)
  Imodel_m = np.array(Imodel_m)
  return q_p*10, I_p, sI_p, Imodel_p, q_m*10, I_m, sI_m, Imodel_m

def get_sld_data(file):
  sldData = MultiData(XyeData)
  sldData.loadFromFile(file)
  z, sld, sldMag = sldData.getDataset(0).getData()
  return z, sld, sldMag

q_rem_p_fit, I_rem_p_fit, sI_rem_p_fit, Imodel_rem_p_fit, q_rem_m_fit, I_rem_m_fit, sI_rem_m_fit, Imodel_rem_m_fit = get_fit_data(fit_fileZFC_rem)

z_rem, sld_rem, sldMag_rem = get_sld_data(sld_fileZFC_rem)

left, bottom = 0.19, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

sf_rem = 1
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])

ax.errorbar(q_rem_p_fit, I_rem_p_fit*sf_rem, sI_rem_p_fit*sf_rem,
  linestyle='None',
  label='-100mT, $R^{+}$',
  zorder=0, capsize=0, marker='.')
ax.errorbar(q_rem_m_fit, I_rem_m_fit*sf_rem, sI_rem_m_fit*sf_rem,
  linestyle='None',
  label='-100mT, $R^{-}$',
  zorder=0, capsize=0, marker='.')

handles, labels = ax.get_legend_handles_labels()

ax.plot(q_rem_p_fit, Imodel_rem_p_fit*sf_rem, zorder=1, color=color_variant(colors['sanspol_p_sa_data'], -100), marker='None')
ax.plot(q_rem_m_fit, Imodel_rem_m_fit*sf_rem, zorder=1, color=color_variant(colors['sanspol_m_sa_data'], -100), marker='None')

ax.text(0.05, 0.28, labeltext,
  transform=ax.transAxes, fontsize=10)
ax.text(0.05, 0.21, '$R^{+},\, R^{-}$',
  transform=ax.transAxes, fontsize=10)

ax.legend(
  [(handles[0], handles[1])],
  ['-100mT'],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  bbox_to_anchor = [0.4, 0.20])



ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, nm^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax_sld.plot(z_rem, sldMag_rem, marker='None', color=color_variant(colors['sanspol_p_sa_data'], -100))

ax_sld.set_xlabel("$\mathit{z} \,/\,nm$", fontsize=8)
ax_sld.set_ylabel(r"$\rho_\mathrm{mag.} \, / \, 10^{-6} \AA^{-2}$", fontsize=8)
ax_sld.set_xticks([0, 10, 20])
ax_sld.set_yticks([0, 0.5, 1])
ax_sld.set_xlim([-4, 25])
ax_sld.set_ylim([0, 0.6])
ax_sld.tick_params(axis='both', which='major', labelsize=8)

fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)
