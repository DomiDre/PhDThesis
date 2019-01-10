import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from GALAXI.dd_gisaxs.dd_gisaxs import DDGISAXS
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib as mpl

chapter = 'monolayers'
savefile = chapter + '_GISAXS_SVcbar'

vmin = 1e-9
vmax = 15e-6
x0, y0 = 0.13, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
obj = DDGISAXS()
fig = plt.figure(figsize=(4, 0.5))
ax1 = fig.add_axes([0.05, 0.80, 0.9, 0.15])

cmap = obj.cmap
norm = mpl.colors.LogNorm(vmin = vmin, vmax=vmax)
cb1 = mpl.colorbar.ColorbarBase(
  ax1,
  cmap=cmap,
  norm=norm,
  orientation='horizontal')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
# plt.show()