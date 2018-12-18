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
from modelexp.data import MultiData, XyData, XyeData

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'Ol_CoFe_C'
Chapter = 'monolayers'


sans_initial_file_superball = cwd + "/superballModel/sans/init/superballData_simulation.xy"
sans_initial_file_oleicAcid = cwd + "/superballModel/sans/oa_sim/oleicAcid_simulation.xy"

pngfile = Chapter + '_SAS_' + sample_name + "_InitialSANS.png"


dataRef_sa = XyeData()
dataRef_sa.loadFromFile(cwd + '/experimental_data/DD67_nuclear20_sa.dat')
q_sa, I_sa, sI_sa = dataRef_sa.getData()
dataRef_la = XyeData()
dataRef_la.loadFromFile(cwd + '/experimental_data/DD67_nuclear20_la_scaled.dat')
q_la, I_la, sI_la = dataRef_la.getData()

modelRef = MultiData(XyData)
modelRef.loadFromFile(sans_initial_file_superball)
q_model_sa, I_model_sa = modelRef.getDataset(0).getData()
q_model_la, I_model_la = modelRef.getDataset(1).getData()

modelRef = MultiData(XyData)
modelRef.loadFromFile(sans_initial_file_oleicAcid)
q_model_oa_sa, I_model_oa_sa = modelRef.getDataset(0).getData()
q_model_oa_la, I_model_oa_la = modelRef.getDataset(1).getData()

r_part = [0, 4.69420932, 4.69420932, 4.69420932+1.5, 4.69420932+1.5, 10.0]
sld_part = [6.198, 6.198, 0.078, 0.078, 5.664, 5.664]
r_oa = [0, 1.5, 1.5, 10.0]
sld_oa = [0.078, 0.078, 5.664, 5.664]

sf = 1.4
I_model_sa = sf*np.array(I_model_sa)
I_model_la = sf*np.array(I_model_la)

sf_oa = 1
I_model_oa_sa = sf_oa*np.array(I_model_oa_sa)
I_model_oa_la = sf_oa*np.array(I_model_oa_la)


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
  label='Ac-CoFe-C', zorder=0, capsize=0, marker='.', alpha=1)

ax.errorbar(q_la, I_la, sI_la,
  linestyle='None',
  color=colors['sans_la_data'],
  zorder=0, capsize=0, marker='.', alpha=1)

# ax.plot(q_model_sa, I_model_sa, marker='None', linestyle='-',
#   color='green',
#   label='Superball', zorder=2, alpha=0.8)

# ax.plot(q_model_la, I_model_la, marker='None', linestyle='-',
#   color='green',
#   zorder=2, alpha=0.8)


# ax.plot(q_model_oa_sa, I_model_oa_sa, marker='None', linestyle='-',
#   color='#0EA8DF',
#   label='Oleic Acid Micelles', zorder=1, alpha=0.8)

# ax.plot(q_model_oa_la, I_model_oa_la, marker='None', linestyle='-',
#   color='#0EA8DF',
#   zorder=1, alpha=0.8)

# ax.plot(q_model_oa_sa, I_model_sa+I_model_oa_sa, marker='None', linestyle='-',
#   color='black',
#   label='Oleic Acid Micelles', zorder=1, alpha=0.8)

# ax.plot(q_model_oa_la, I_model_la+I_model_oa_la, marker='None', linestyle='-',
#   color='black',
#   zorder=1, alpha=0.8)

ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\,cm^{-1}$")
ax.set_xlim([1e-2, 0.2])
ax.set_ylim([3e-3, 3e1])

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

# fig.savefig(thesisimgs + '/' + pngfile)
fig.savefig(cwd + '/' + pngfile)