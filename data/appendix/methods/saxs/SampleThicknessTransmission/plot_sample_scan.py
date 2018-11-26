import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
plt.style.use('phdthesis')

import numpy as np
from GALAXI.dd_saxs.lib.class_transmission_evaluator import TransmissionEvaluator

chapter = 'appendix_methods'
sample_name = 'SampleScan'
savefile = chapter + f'_SAXS_{sample_name}'

scan_file = f'{cwd}/Zaktuna_Adjustment_25663.dat'
evaluator = TransmissionEvaluator(scan_file)

shift_pz = evaluator.pz+10
evaluator.I -= 104
I_max = np.mean(evaluator.I[np.logical_and(shift_pz>0, shift_pz<1)])
x0, y0 = 0.17, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()
ax = fig.add_axes([x0, y0, width, height])
ax.plot(shift_pz, evaluator.I/I_max, marker='None')
ax.annotate("$\mathit{T}_{d.\,b.}$",
  xy=(1.4, 1), xytext=(2.3, 1),
  arrowprops=dict(facecolor='black', arrowstyle='->'),
  horizontalalignment='left',
  verticalalignment='center')

ax.annotate("$\mathit{T}_{b.\,b.}$",
  xy=(3, 0.01), xytext=(3, 0.2),
  arrowprops=dict(facecolor='black', arrowstyle='->'),
  horizontalalignment='center',
  verticalalignment='bottom')

ax.annotate("$\mathit{T}_{s}$",
  xy=(6.2, 0.78), xytext=(6.2, 0.5),
  arrowprops=dict(facecolor='black', arrowstyle='->'),
  horizontalalignment='center',
  verticalalignment='bottom')
ax.text(6.125, 0.93, '$\mathit{d}_{s}$',horizontalalignment='center')
ax.annotate("",
  xy=(5.15, 0.89), xytext=(7.1, 0.89),
  arrowprops=dict(
    facecolor='black', arrowstyle='<->'
  ),
  horizontalalignment='left',
  verticalalignment='bottom'
)

ax.set_xlim([0,7.9])
ax.set_ylim([-0.01, 1.1])
ax.set_xlabel('$\mathit{z} \, / \, cm$')
ax.set_ylabel('$\mathit{T}$')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
