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
from modelexp.data import XyData

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

Chapter = 'monolayers'
sample_name = 'SuperballFF'

q_min, q_max = 5e-3, 0.2
I_min, I_max = 2e-5, 1.5e0

pngfile = Chapter + '_SAS_' + sample_name + '.png'


bg = 0#params['bg']['value']
left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
# ax_inset = fig.add_axes([0.6, 0.7, 1-0.6-0.01, 1-0.7-0.01])
ax_inset = fig.add_axes([left+0.03, bottom+0.03, 0.4, 0.4])

for p in ['1.0', '1.5', '2.0', '4.0']:
  #load data
  data = XyData()
  data.loadFromFile(f'./superballData_sigR_0.05_p_{p}.xy')
  q, I = data.getData()

  ax.plot(q, I, marker='None', linestyle='-', zorder=1, alpha=1, label=f"p = {p}")
  ax_inset.plot(q, I, marker='None', linestyle='-', zorder=1, alpha=1, label=f"p = {p}")
# ax.text(0.12, 0.2, 'Ac-CoFe-C',
#   horizontalalignment='left',
#   verticalalignment='bottom',
#   transform=ax.transAxes,
#   fontsize=inset_fontsize)

ax.legend(loc='upper right', fontsize=inset_fontsize)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{P}_{Superball}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax_inset.set_xscale('log')
ax_inset.set_yscale('log')
ax_inset.set_xlim([0.04, 0.12])
ax_inset.set_ylim([0.0001, 0.01])
ax_inset.get_xaxis().set_visible(False)
ax_inset.get_yaxis().set_visible(False)

fig.savefig(thesisimgs + '/' + pngfile)
fig.savefig(cwd + '/' + pngfile)