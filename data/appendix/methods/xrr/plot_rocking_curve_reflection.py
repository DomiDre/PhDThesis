import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
plt.style.use('phdthesis3cols')

import numpy as np
import jcnsBrukerD8

sample_name = 'rockingCurve_reflection'
savefile = f'appendix_methods_XRR_{sample_name}'

vmin, vmax = 0.1, 100

txtfile = f'{cwd}/RockingCurve2th0-6degExample_DD205_3.txt'

app = jcnsBrukerD8.App()
app.load_dat(txtfile)
ai = app.ai
I = app.I / max(app.I)
# I = app.I / np.mean(app.I[np.logical_and(z>0, z<0.1)])

x0, y0 = 0.24, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()
ax = fig.add_axes([x0, y0, width, height])
ax.plot(ai, I, marker="None")
ax.annotate("",
  xy=(0.322, 0.), xytext=(0.322, 1),
  arrowprops=dict(facecolor='black', arrowstyle='->'),
  horizontalalignment='left',
  verticalalignment='bottom',)
# ax.set_xscale('log')
# ax.set_yscale('log')
# ax.set_xticks([-0.3, 0, 0.3])
ax.set_xlim([0.25,0.39])
ax.set_ylim([0., 1.05])
ax.set_xlabel(r'$2\alpha_i - \alpha_o \, / \, ^\circ$')
ax.set_ylabel('$\mathit{I}\, / \, a.u.$')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
