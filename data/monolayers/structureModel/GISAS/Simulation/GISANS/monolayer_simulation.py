import sys, os, h5py, matplotlib
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import matplotlib.colors as mcolors

import bornagain as ba
from uzkBornAgain import D33, BAPlot, BASimulation, utils
from uzkBornAgain.models import BA_Cubes_SquareParacrystal

model = BA_Cubes_SquareParacrystal(
  cube_a = 8.58,
  lattice_a = 13.275,
  domain_length = 0,
  position_uncertainty = 0.92,
  damping_length = 750.,
  thickness_SiO2 = 7.3,
  thickness_OA_lower = 5.3,
  SLD_substrate = (2.0e-06, 0e-07),
  SLD_SiO2 = (7.78e-06, 0e-07),
  SLD_OA_lower = (0.0e-06, 0e-07),
  SLD_particle = (4.307e-05, 0e-07),
  integrate_xi = True)

detector = Pilatus1M(1733.5, 610.41, 338.41, 0.15)
detector.set_detector_range_in_mm(-40.709, 59.2137, 0, 55.51285)
detector.beam_y = 40.709
detector.beam_z = 0
detector.beam_intensity = 2.5e7
sim = BASimulation(detector, model)
plot = BAPlot()

y, z, I = sim.run()

# store simulation
sim.save('monolayer.h5')

#plot simulation
vmin = 1e-2
vmax = 1.5e5
qy, qz = detector.coordinates_to_q(y, z)

qz_min = 0.20#45
qz_max = 0.245#9
qz_range = np.logical_and(qz>qz_min, qz<qz_max)
yoneda_line = np.sum(I[:, qz_range], axis=1)

I_yoneda = yoneda_line
sI_yoneda = np.sqrt(yoneda_line)


def plot_q_square_lines(q10, ax):
  ymin = 0.1
  ymax = 0.2

  # rest position of peaks
  qsquare = lambda h,k: q10 * np.sqrt(h**2 + k**2)
  q11 = qsquare(1,1)
  q20 = qsquare(2,0)
  q21 = qsquare(2,1)
  q22 = qsquare(2,2)
  q30 = qsquare(3,0)
  q31 = qsquare(3,1)
  q32 = qsquare(3,2)
  q33 = qsquare(3,3)

  ax.axvline(q10, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q11, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q20, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q21, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q22, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q30, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q31, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q32, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q33, color='black', ymin=ymin, ymax=ymax, marker='None')

  ax.axvline(-q10, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q11, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q20, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q21, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q22, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q30, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q31, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q32, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q33, color='black', ymin=ymin, ymax=ymax, marker='None')


x0, y0 = 0.13, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01

fig = plt.figure()
ax = fig.add_axes([x0, 0.42, width, 0.57])
ax2 = fig.add_axes([x0, y0, width, 0.25])
pcm = ax.pcolormesh(qy, qz, I.T,\
                    norm=mcolors.LogNorm(),\
                    cmap=utils.get_cmap(), vmin=vmin, vmax=vmax)
ax.axhline(qz_min, color='white', marker='None', alpha=0.5)
ax.axhline(qz_max, color='white', marker='None', alpha=0.5)
txt = ax.text(0.95, 0.95,\
        'Simulation',\
        color='white',\
        horizontalalignment='right',
        verticalalignment='top',\
        transform=ax.transAxes)
ax2.errorbar(
  qy, I_yoneda, sI_yoneda,
  linestyle='None', capsize=0, elinewidth=1, color='#ca0020'
)
ax2.set_yscale('log')
plot_q_square_lines(0.4726, ax2)
ax.set_xticks([])

ax.set_yticks([0, 1])
ax2.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')

ax2.get_yaxis().set_visible(False)
plt.setp(ax.get_xticklabels(), visible=False)
ax.set_xlim(-1.1,1.6)
ax2.set_xlim(-1.1,1.6)
ax.set_ylim(0, 1.5)
ax2.set_ylim([1e1, 3e5])
ax.set_aspect('equal')

fig.savefig('simulation.png')