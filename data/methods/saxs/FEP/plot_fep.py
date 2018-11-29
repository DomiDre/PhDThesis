import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
plt.style.use('phdthesis')

import numpy as np
import pyFAI, fabio

from GALAXI.dd_saxs.dd_saxs import DDSAXS, DDSAXSMask

chapter = 'appendix_methods'
sample_name = 'FEP'
savefile = chapter + f'_SAXS_{sample_name}'

vmin, vmax = 0.1, 100
FEP_file = f'{cwd}/Zaktuna_LSDD_FEP_25665.1.tif'

sdd = 3388.50
beamcenter_x, beamcenter_y = 605.67, 288.089


tifdata = fabio.open(FEP_file)
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

I_proj = np.sum(data_caked, axis=0)
sI_proj = np.sqrt(I_proj)
x0, y0 = 0.17, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()
ax = fig.add_axes([x0, y0, width, height])
ax.errorbar(q*10, I_proj, sI_proj)
ax.annotate("$\mathit{I}_{FEP}^{peak}$",
  xy=(0.2, 1.2e4), xytext=(0.4, 2.5e4),
  arrowprops=dict(facecolor='black', arrowstyle='->'),
  horizontalalignment='left',
  verticalalignment='bottom',)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlim([0.09,1.9])
ax.set_ylim([1, 0.9e5])
ax.set_xlabel('$\mathit{q} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{I} \, / \, a.u.$')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
