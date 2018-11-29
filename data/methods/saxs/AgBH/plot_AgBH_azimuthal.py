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
sample_name = 'AgBH_azimuthal'
savefile = chapter + f'_SAXS_{sample_name}'

vmin, vmax = 0.1, 100
agBH_file = f'{cwd}/Zaktuna_SSDD_AgBH_25684.1.tif'
sdd = 690.14
beamcenter_x, beamcenter_y = 616.43, 364.08

tifdata = fabio.open(agBH_file)
data = tifdata.data
detector_data = data[::-1,:].T
mask = (detector_data < 0)*1 # automatically treshold mask
mask = mask.copy(order='C')

ai = pyFAI.AzimuthalIntegrator(
  dist=sdd/1000,
  poni1=beamcenter_x*172e-6,
  poni2=beamcenter_y*172e-6,
  detector=pyFAI.detectors.Pilatus1M(),
  wavelength=1.3414e-10
)
data_caked, q, chi = ai.integrate2d(
  detector_data,
  npt_rad=300, npt_azim=360,
  mask=mask,
  unit="q_A^-1"
)

data_projection = np.sum(data_caked, axis=0)

x0, y0 = 0.13, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()
ax = fig.add_axes([x0, y0, width-0.3, height])
ax2 = fig.add_axes([x0+width-0.3, y0, 0.3, height], sharey=ax)
pcm = ax.pcolormesh(
  chi, q*10, data_caked.T,
  norm=mcolors.LogNorm(),
  cmap=get_cmap(), vmin=vmin, vmax=vmax
)
ax2.plot(data_projection, q*10, marker='None')
ax2.set_xscale('log')
# ax.set_xticks([])
# ax.set_yticks([0, 1])
ax.set_ylim([0.2,7])
ax2.set_xlim([10, 9e4])
ax2.set_xticks([])
ax.set_xlabel('$\chi \, / \, ^\circ$')
ax.set_ylabel('$\mathit{q} \, / \, nm^{-1}$')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
