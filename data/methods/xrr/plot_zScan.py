import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
plt.style.use('phdthesis3cols')

import numpy as np
import jcnsBrukerD8

sample_name = 'zScan'
savefile = f'appendix_methods_XRR_{sample_name}'

vmin, vmax = 0.1, 100
txtfile = f'{cwd}/ZScanExample_DD205_3.txt'

app = jcnsBrukerD8.App()
app.load_zdat(txtfile)

z = app.z + 1.1
I = app.I / np.mean(app.I[np.logical_and(z>0, z<0.1)])

x0, y0 = 0.24, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()
ax = fig.add_axes([x0, y0, width, height])
ax.plot(z, I, marker="None")
ax.annotate("",
  xy=(0.27, 0.0), xytext=(0.27, 0.5),
  arrowprops=dict(facecolor='black', arrowstyle='->'),
  horizontalalignment='left',
  verticalalignment='bottom',)
# ax.set_xscale('log')
# ax.set_yscale('log')
ax.set_xlim([0,0.9])
ax.set_ylim([0, 1.1])
ax.set_xlabel('$\mathit{z} \, / \, mm$')
ax.set_ylabel('$\mathit{T}$')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
