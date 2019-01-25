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
from modelexp.data import MultiData, XyemData, XyData, XyeData

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'Ol-Fe-C'
Chapter = 'colloidalCrystals'
saxs_fit_file = cwd + "/homSuperballModel/saxs/fit_result.dat"
saxs_sld_file = cwd + "/homSuperballModel/saxs/fit_sld.dat"
# saxs_sld_file = cwd + "/superballModel/saxs/simulated_model_sld.xy"
# model_file = cwd + "/superballModel/saxs/simulated_model.xy"
# expdata_file = cwd + "/experimental_data/DD144.xye"

q_min, q_max = 1e-2, 0.35
I_min, I_max = 3.5e-4, 3e3

saxs_legend_label = "SAXS @ GALAXI"

saxs_pngfile = Chapter+'_SAS_'+\
                sample_name+"_SAXS.png"

#load data
data = MultiData(XyemData)
data.loadFromFile(saxs_fit_file)
qdata, Idata, sIdata, Imodel = data.getDataset(0).getData()

#load sld
sldData = XyData()
sldData.loadFromFile(saxs_sld_file)
saxs_r, saxs_sld = sldData.getData()
# saxs_r /= 10
# saxs_sld *= 1e6
# data = XyeData()
# data.loadFromFile(expdata_file)
# qdata, Idata, sIdata = data.getData()

# data = XyData()
# data.loadFromFile(model_file)
# qmodel, Imodel = data.getData()


left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

def linear(x, a, n):
  return a*x**n

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])
ax.errorbar(qdata, Idata, sIdata,\
  linestyle='None', color='#0EA8DF',\
  label=saxs_legend_label, zorder=0, capsize=0, marker='.')

ax.plot(qdata, Imodel, marker='None', linestyle='-',\
  color=color_variant('#0EA8DF', -150), zorder=1)

q_linear = np.linspace(1e-2, 0.03, 100)
ax.plot(q_linear, linear(q_linear, 0.152, -1.474), marker='None',
  linestyle='--', color='#EE292F', zorder=1)
ax.text(0.012, 2e2, '$q^{-1.47(1)}$', color='#EE292F')

ax.text(0.11, 0.12,
  'Ol-Fe-C\n8 months after synthesis',
  color='black',
  fontsize=inset_fontsize,
  horizontalalignment='left',
  verticalalignment='bottom',
  transform=ax.transAxes)

ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\,cm^{-1}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax_sld.plot(saxs_r, saxs_sld, marker='None',
  color=colors['saxs_data'])
ax_sld.set_xlabel("$\mathit{r} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(r"$\rho_{el} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 2, 4, 6, 8])
ax_sld.set_yticks([0, 10, 20, 30, 40, 50])
ax_sld.set_xlim([0, 9])
ax_sld.set_ylim([0, 59])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)


fig.savefig(thesisimgs + '/' + saxs_pngfile)
fig.savefig(cwd + '/' + saxs_pngfile)