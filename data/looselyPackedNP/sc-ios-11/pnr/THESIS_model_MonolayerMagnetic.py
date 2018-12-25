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
from matplotlib.legend_handler import HandlerTuple
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'SC-IOS-11'
Chapter = 'looselyPackedNP'
fit_file = cwd + "/1FitMagnetic/fit_result.dat"
sld_file = cwd + "/1FitMagnetic/fit_sld.dat"

rem_fit_file = cwd + "/2FitRemanence/fit_result.dat"
rem_sld_file = cwd + "/2FitRemanence/fit_sld.dat"

labeltext = 'SC-IOS-11'
q_min, q_max = 0.05, 1.1
I_min, I_max = 1e-6, 1.2e1

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


def get_xye_data(file):
  data = XyeData()
  data.loadFromFile(file)
  q, I, sI = data.getData()
  q = np.array(q)
  I = np.array(I)
  sI = np.array(sI)
  valid_data = I > 0
  q = q[valid_data]
  I = I[valid_data]
  sI = sI[valid_data]
  valid_data = sI/I < 1
  q = q[valid_data]
  I = I[valid_data]
  sI = sI[valid_data]
  return q*10, I, sI

#load data
data = MultiData(XyemData)
data.loadFromFile(fit_file)
q_p, I_p, sI_p, Imodel_p, q_m, I_m, sI_m, Imodel_m = get_clean_data(data)

data = MultiData(XyemData)
data.loadFromFile(rem_fit_file)
q_rem_p, I_rem_p, sI_rem_p, Imodel_rem_p, q_rem_m, I_rem_m, sI_rem_m, Imodel_rem_m = get_clean_data(data)
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
ax.errorbar(q_p, I_p*10, sI_p*10,\
  linestyle='None', color=colors['sanspol_p_sa_data'],
  label='$R^{+}$ 500 mT', zorder=0, capsize=0, marker='.')
ax.errorbar(q_m, I_m*10, sI_m*10,\
  linestyle='None', color=colors['sanspol_m_sa_data'],
  label='$R^{-}$ 500 mT', zorder=0, capsize=0, marker='.')
ax.plot(q_p, Imodel_p*10, zorder=1, color=color_variant(colors['sanspol_p_sa_data'], -100), marker='None')
ax.plot(q_m, Imodel_m*10, zorder=1, color=color_variant(colors['sanspol_m_sa_data'], -100), marker='None')

ax.errorbar(q_rem_p, I_rem_p, sI_rem_p,\
  linestyle='None', color='#FAAB2D',
  label='$R^{+}$ Remanence', zorder=0, capsize=0, marker='.')
ax.errorbar(q_rem_m, I_rem_m, sI_rem_m,\
  linestyle='None', color="#76C152",
  label='$R^{-}$ Remanence', zorder=0, capsize=0, marker='.')
ax.plot(q_rem_p, Imodel_rem_p, zorder=1, color=color_variant("#FAAB2D", -100), marker='None')
ax.plot(q_rem_m, Imodel_rem_m, zorder=1, color=color_variant("#76C152", -100), marker='None')


handles, labels = ax.get_legend_handles_labels()

ax.text(0.05, 0.3, labeltext,
  transform=ax.transAxes, fontsize=10)
ax.text(0.05, 0.22, '$R^{+}, R^{-}$',
  transform=ax.transAxes, fontsize=10)
ax.legend(
  [(handles[0], handles[1]),
   (handles[2], handles[3])],
  ['500 mT', 'Remanence'],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  bbox_to_anchor = [0.5, 0.25])

ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, nm^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

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
