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
from modelexp.data import MultiData, XyData, XyerData, XyemData

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'Ol_CoFe_C'
Chapter = 'monolayers'


file_superball = cwd + "/superballModel/sim_saxs_sans/fit_result.dat"
file_sld =       cwd + "/superballModel/sim_saxs_sans/fit_sld.dat"

# sans_initial_file_superball = cwd + "/superballModel/sim_saxs_sans/simulate/superballData_simulation.xy"
# sans_initial_file_sld = cwd + "/superballModel/sim_saxs_sans/simulate/superballData_simulation_sld.xy"

pngfile = Chapter + '_SAS_' + sample_name + "_SimultaneousSaxsSans.png"

def chi2(q, I, sI, Imodel):
  return np.sum(((np.log(I) - np.log(Imodel))/sI*I)**2) / len(q)


modelRef = MultiData(XyemData)
modelRef.loadFromFile(file_superball)
q_saxs, I_saxs, sI_saxs, I_model_saxs = modelRef.getDatasetBySuffix('saxs').getData()
q_sa, I_sa, sI_sa, I_model_sa = modelRef.getDatasetBySuffix('sans_sa').getData()
q_la, I_la, sI_la, I_model_la = modelRef.getDatasetBySuffix('sans_la').getData()

modelRef = MultiData(XyData)
modelRef.loadFromFile(file_sld)
r_saxs, sld_saxs = modelRef.getDatasetBySuffix('saxs').getData()
r_saxs_part = np.array(r_saxs[:8])
sld_saxs_part = np.array(sld_saxs[:8])
r_saxs_oa = np.array(r_saxs[16:20])
sld_saxs_oa = np.array(sld_saxs[16:20])

r_sa, sld_sa = modelRef.getDatasetBySuffix('sans_sa').getData()
r_sa, sld_sa = np.array(r_sa), np.array(sld_sa)
r_sa_part = r_sa[:8]
sld_sa_part = sld_sa[:8]
r_sa_oa = r_sa[16:20]
sld_sa_oa = sld_sa[16:20]

left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

chi2_saxs = chi2(q_saxs, I_saxs, sI_saxs, I_model_saxs)
chi2_sa = chi2(q_sa, I_sa, sI_sa, I_model_sa)
chi2_la = chi2(q_la, I_la, sI_la, I_model_la)
print(f"saxs: {chi2_saxs}\tsans sa: {chi2_sa}\tsans la: {chi2_la}")
sf = 5e-2
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])

ax.errorbar(q_saxs, I_saxs, sI_saxs,
  linestyle='None',
  color=colors['saxs_data'],
  label='SAXS', zorder=0, capsize=0, marker='.', alpha=1)

ax.errorbar(q_sa, np.array(I_sa)*sf, np.array(sI_sa)*sf,
  linestyle='None',
  color=colors['sans_sa_data'],
  label='$0.05 \cdot$SANS @ D33', zorder=0, capsize=0, marker='.', alpha=1)

ax.errorbar(q_la, np.array(I_la)*sf, np.array(sI_la)*sf,
  linestyle='None',
  color=colors['sans_la_data'],
  zorder=0, capsize=0, marker='.', alpha=1)


ax.plot(q_saxs, I_model_saxs, marker='None', linestyle='-',
  color='black',
  label='Superball', zorder=2, alpha=0.8)

ax.plot(q_sa, np.array(I_model_sa)*sf, marker='None', linestyle='-',
  color='black',
  zorder=2, alpha=0.8)

ax.plot(q_la, np.array(I_model_la)*sf, marker='None', linestyle='-',
  color='black',
  zorder=2, alpha=0.8)


ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.text(0.04, 0.26, 'Ol-CoFe-C',
  horizontalalignment='left',
  verticalalignment='bottom',
  transform=ax.transAxes,
  fontsize=inset_fontsize)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\,cm^{-1}$")
ax.set_xlim([1e-2, 0.3])
ax.set_ylim([4e-4, 2e3])

ax_sld.plot(r_saxs_part, sld_saxs_part, marker='None', color='#FAAB2D', zorder=4, label=r"$\rho_\mathrm{el}$")
ax_sld.plot(r_sa_part, sld_sa_part, marker='None', color=color_variant('#FAAB2D', -100), zorder=3, label=r"$\rho_\mathrm{nuc}$")
# ax_sld.plot(r_saxs_oa/10, sld_saxs_oa/1e-6, marker='None', color='#0EA8DF', zorder=2, label="OA")
# ax_sld.plot(r_sa_oa/10, 5*sld_sa_oa/1e-6, marker='None', color=color_variant('#0EA8DF', -100), zorder=2)

ax_sld.set_xlabel("$\mathit{r} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(r"$\rho \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
# ax_sld.set_xticks([0, 2, 4, 6, 8])
# ax_sld.set_yticks([0, 2, 4, 6, 8])
ax_sld.set_xlim([0, 9.9])
ax_sld.set_ylim([-0.1, 59])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)
ax_sld.legend(fontsize=8, loc='upper right')

fig.savefig(thesisimgs + '/' + pngfile)
fig.savefig(cwd + '/' + pngfile)