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
from modelexp.data import MultiData, XyemData

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'IOS-7'
Chapter = 'looselyPackedNP'
fit_file = cwd + "/fit_result.dat"
sld_file = cwd + "/fit_sld_plotted.dat"


I_min, I_max = 1.5e-3, 3e1

sanspol_p_legend_label = "I(+) SANSPOL @ D33"
sanspol_m_legend_label = "I(-) SANSPOL @ D33"

sanspol_pngfile = Chapter+'_SAS_'+\
                sample_name+"_SANSPOLFit.png"

#load data
data = MultiData(XyemData)
data.loadFromFile(fit_file)
sanspol_p_la_q, sanspol_p_la_I, sanspol_p_la_sI, sanspol_p_la_Imodel = data.getDatasetBySuffix('p_la').getData()
sanspol_m_la_q, sanspol_m_la_I, sanspol_m_la_sI, sanspol_m_la_Imodel = data.getDatasetBySuffix('m_la').getData()
sanspol_p_sa_q, sanspol_p_sa_I, sanspol_p_sa_sI, sanspol_p_sa_Imodel = data.getDatasetBySuffix('p_sa').getData()
sanspol_m_sa_q, sanspol_m_sa_I, sanspol_m_sa_sI, sanspol_m_sa_Imodel = data.getDatasetBySuffix('m_sa').getData()

#load sld
sldData = MultiData(XyemData)
sldData.loadFromFile(sld_file)
sanspol_p_sa_r1, sanspol_p_sa_sld1, sanspol_p_sa_rMag1, sanspol_p_sa_sldMag1 = sldData.getDatasetBySuffix('p_sa_model1').getData()
sanspol_p_sa_r2, sanspol_p_sa_sld2, sanspol_p_sa_rMag2, sanspol_p_sa_sldMag2 = sldData.getDatasetBySuffix('p_sa_model2').getData()

q_min = 1e-2
q_max = max(max(sanspol_p_la_q),
            max(sanspol_p_sa_q),
            max(sanspol_m_la_q),
            max(sanspol_m_sa_q))

left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])
ax.errorbar(sanspol_p_sa_q, sanspol_p_sa_I, sanspol_p_sa_sI,\
  linestyle='None', color=colors['sanspol_p_sa_data'],\
  label=sanspol_p_legend_label, zorder=0, capsize=0, marker='.')
ax.plot(sanspol_p_sa_q, sanspol_p_sa_Imodel, marker='None', linestyle='-',\
  color=colors['sanspol_p_model'], zorder=1)

ax.errorbar(sanspol_p_la_q, sanspol_p_la_I, sanspol_p_la_sI,\
  linestyle='None', color=colors['sanspol_p_la_data'],\
  zorder=0, capsize=0, marker='.')
ax.plot(sanspol_p_la_q, sanspol_p_la_Imodel, marker='None', linestyle='-',\
  color=colors['sanspol_p_model'], zorder=1)

ax.errorbar(sanspol_m_sa_q, sanspol_m_sa_I, sanspol_m_sa_sI,\
  linestyle='None', color=colors['sanspol_m_sa_data'],\
  label=sanspol_m_legend_label, zorder=0, capsize=0, marker='.')
ax.plot(sanspol_m_sa_q, sanspol_m_sa_Imodel, marker='None', linestyle='-',\
  color=colors['sanspol_m_model'], zorder=1)

ax.errorbar(sanspol_m_la_q, sanspol_m_la_I, sanspol_m_la_sI,\
  linestyle='None', color=colors['sanspol_m_la_data'],\
  zorder=0, capsize=0, marker='.')
ax.plot(sanspol_m_la_q, sanspol_m_la_Imodel, marker='None', linestyle='-',\
  color=colors['sanspol_m_model'], zorder=1)

ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\,cm^{-1}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax_sld.plot(sanspol_p_sa_r1, sanspol_p_sa_sld1, marker='None',
  color=colors['sanspol_sld'])
ax_sld.plot(sanspol_p_sa_rMag1, sanspol_p_sa_sldMag1, marker='None',
  color=colors['sanspol_sldMag'])
ax_sld.plot(sanspol_p_sa_r2, sanspol_p_sa_sld2, marker='None',
  color=colors['sanspol_sld'], alpha=0.5)
ax_sld.plot(sanspol_p_sa_rMag2, sanspol_p_sa_sldMag2, marker='None',
  color=colors['sanspol_sldMag'], alpha=0.5)
ax_sld.set_xlabel("$\mathit{r} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel("$SLD \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 2, 4, 6, 8])
ax_sld.set_yticks([0, 2, 4, 6, 8])
ax_sld.set_xlim([0, 9])
ax_sld.set_ylim([0, 9])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)


fig.savefig(thesisimgs + '/' + sanspol_pngfile)
fig.savefig(cwd + '/' + sanspol_pngfile)