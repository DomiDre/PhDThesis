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
from modelexp.data import MultiData, XyData, XyemData

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'Ol_CoFe_C'
Chapter = 'monolayers'


file_superball = cwd + "/superballModel/saxs/fit_result.dat"
file_sld =       cwd + "/superballModel/saxs/fit_sld.dat"

pngfile = Chapter + '_SAS_' + sample_name + "_Saxs.png"

def chi2(q, I, sI, Imodel):
  return np.sum(((np.log(I) - np.log(Imodel))/sI*I)**2) / len(q)

modelRef = MultiData(XyemData)
modelRef.loadFromFile(file_superball)
q, I, sI, I_model = modelRef.getDataset(0).getData()

modelRef = MultiData(XyData)
modelRef.loadFromFile(file_sld)
r_saxs, sld_saxs = modelRef.getDataset(0).getData()
r_saxs, sld_saxs = np.array(r_saxs), np.array(sld_saxs)
r_saxs_part = r_saxs[:8]
sld_saxs_part = sld_saxs[:8]

left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

chi2_saxs = chi2(q, I, sI, I_model)
print(f"saxs: {chi2_saxs}")

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])

ax.errorbar(q, I, sI,
  linestyle='None',
  color=colors['saxs_data'],
  label='SAXS', zorder=0, capsize=0, marker='.', alpha=1)

ax.plot(q, I_model, marker='None', linestyle='-',
  color='black',
  label='Superball', zorder=2, alpha=0.8)

ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\,cm^{-1}$")
ax.set_xlim([1e-2, 0.3])
ax.set_ylim([4e-4, 2e3])

ax_sld.plot(r_saxs_part/10, sld_saxs_part/1e-6, marker='None', color='#FAAB2D', zorder=4, label=r"NP")
# ax_sld.plot(r_saxs_oa/10, sld_saxs_oa/1e-6, marker='None', color='#0EA8DF', zorder=2, label="OA")

ax_sld.set_xlabel("$\mathit{r} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(r"$\rho_\mathrm{el} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
# ax_sld.set_xticks([0, 2, 4, 6, 8])
# ax_sld.set_yticks([0, 2, 4, 6, 8])
ax_sld.set_xlim([0, 9.9])
ax_sld.set_ylim([-0.1, 59])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)
ax_sld.legend(fontsize=8, loc='upper right')

fig.savefig(thesisimgs + '/' + pngfile)
fig.savefig(cwd + '/' + pngfile)