import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
plt.style.use('phdthesis')

import numpy as np
import pyFAI, fabio
def get_cmap():
  def make_colormap(seq):
      cdict = {'red': [], 'green': [], 'blue': []}
      for i, item in enumerate(seq):
          pos, r, g, b = item
          cdict['red'].append([pos, r, r])
          cdict['green'].append([pos, g, g])
          cdict['blue'].append([pos, b, b])
      return mcolors.LinearSegmentedColormap('CustomMap', cdict)
  c = mcolors.ColorConverter().to_rgb
  custom_colors = [(0, 0, 0, 0),\
                    (0.18, 0.05, 0.05, 0.2),\
                    (0.28, 0, 0, 1),\
                    (0.4, 0.7, 0.85, 0.9),\
                    (0.45, 0, 0.75, 0),\
                    (0.6, 1, 1, 0),\
                    (0.75, 1, 0, 0),\
                    (0.92 , 0.6, 0.6, 0.6),\
                    (1  , 0.95, 0.95, 0.95)]
  cmap = make_colormap(custom_colors)
  cmap.set_bad(color='black')
  return cmap


chapter = 'appendix_methods'
sample_name = 'AgBH'
savefile = chapter + f'_SAXS_{sample_name}'

vmin, vmax = 0.1, 100
agBH_file = f'{cwd}/Zaktuna_SSDD_AgBH_25684.1.tif'
sdd = 690.14
beamcenter_x, beamcenter_y = 616.43, 364.08

tifdata = fabio.open(agBH_file)
data = tifdata.data
detector_data = data[::-1,:].T
mask = (detector_data < 0)*1 # automatically treshold mask
Ny, Nz = detector_data.shape

y = np.arange(Ny)
z = np.arange(Nz)

x0, y0 = 0.13, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()
ax = fig.add_axes([x0, y0, width, height])
pcm = ax.pcolormesh(
  y, z, detector_data.T,
  norm=mcolors.LogNorm(),
  cmap=get_cmap(), vmin=vmin, vmax=vmax
)
ax.set_aspect('equal')
ax.set_xlabel('$\mathit{y} \, / \, pixels$')
ax.set_ylabel('$\mathit{z} \, / \, pixels$')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
