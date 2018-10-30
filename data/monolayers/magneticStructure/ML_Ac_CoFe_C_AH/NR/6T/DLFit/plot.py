#Initialized ScriptFactory v0.2
#Date: 2018-07-11 20:36:37.178142
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
import sys, os
import matplotlib.pyplot as plt
# thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
# plt.style.use('phdthesis')

import numpy as np
import warnings
from modelexp.data import MultiData, XyemData, XyeData
import matplotlib
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')
inset_fontsize = 13
matplotlib.rcParams.update({'font.size': 18})

sample_name = 'DD205_4'
Chapter = 'Monolayer'
fit_file = cwd + "/fit_result.dat"
sld_file = cwd + "/fit_sld.dat"


q_min, q_max = 7e-3, 0.09
I_min, I_max = 1e-5, 1.5

nr_legend_label = "NR @ D17"

nr_pngfile = Chapter+'_PNR_'+\
                sample_name+"_NR.png"
cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

#load data
data = MultiData(XyemData)
data.loadFromFile(fit_file)
nr_p_q, nr_p_I, nr_p_sI, nr_p_Imodel = data.getDatasetBySuffix('p').getData()
nr_m_q, nr_m_I, nr_m_sI, nr_m_Imodel = data.getDatasetBySuffix('m').getData()

#load sld
sldData = MultiData(XyeData)
sldData.loadFromFile(sld_file)
nr_p_z, nr_p_sld, nr_p_sldMag = sldData.getDatasetBySuffix('p').getData()
nr_m_z, nr_m_sld, nr_m_sldMag = sldData.getDatasetBySuffix('m').getData()

nr_q_min, nr_q_max = min(nr_p_q), max(nr_p_q)


left, bottom = 0.18, 0.17
x0in = 0.5
y0in = 0.6
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure(figsize=(4.5, 4.5))
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])
ax.errorbar(nr_p_q, nr_p_I, nr_p_sI,\
  linestyle='None', color=cycle[1],\
  label='I(+) @ D17', zorder=0, capsize=0, marker='.')
ax.errorbar(nr_m_q, nr_m_I, nr_m_sI,\
  linestyle='None', color=cycle[0],\
  label='I(-) @ D17', zorder=0, capsize=0, marker='.')
ax.plot(nr_p_q, nr_p_Imodel, marker='None', linestyle='-',\
  zorder=1, color='#004279')
ax.plot(nr_m_q, nr_m_Imodel, marker='None', linestyle='-',\
  zorder=1, color='#6F0000')

ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax_sld.set_xlabel("$\mathit{z} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel("$\mathit{SLD} \,/\, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xlim([-7, 32])
ax_sld.set_ylim([0, 4.9])

ax_sld.plot(nr_p_z, nr_p_sld, marker='None',
  color='black', label='Nuclear')
ax_sld.plot(nr_p_z, nr_p_sldMag, marker='None',
  color=cycle[0], label='Magnetic')

ax_sld.legend(fontsize=inset_fontsize, loc='upper left')
# ax_sld.set_xticks([0, 2, 4, 6, 8])
ax_sld.set_yticks([0, 1, 2, 3, 4])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)


# fig.savefig(thesisimgs + '/' + nr_pngfile)
fig.savefig(nr_pngfile)