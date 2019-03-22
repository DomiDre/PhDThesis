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
from modelexp.data import XyeData, XyemData, MultiData
import matplotlib.patches as mpatches
from PlottingTemplates.saxssanssanspol import color_variant, colors

import scipy.constants as sc

from matplotlib.patches import Rectangle
from matplotlib.legend_handler import HandlerTuple
from dipole_sum import dipole_sum

# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

Chapter = 'monolayers'
pngfile = f"{Chapter}_MagneticStructure_afm_field.png"

#calc field

pi = np.pi
muB = sc.physical_constants["Bohr magneton"][0] *1e18# A nm2
mu0 = sc.mu_0 * 1e3 * 1e9  # mT * nm / A

a = 8.52
d_pp = 13.2
dipole_sum.a = d_pp
dipole_sum.mu = 23e3

plot_dipole = False

fov_x = d_pp*2
fov_y = d_pp*2
npts = 500
clim = [0,80]
xspace = np.arange(-fov_x, fov_x, d_pp/200)
yspace = np.arange(-fov_y, fov_y, d_pp/200)
z = 0

n_cubes = 2
B, Bx, By, Bz = dipole_sum.get_b_xy_dipole_afm(xspace, yspace, z, n_cubes, n_cubes)

left, bottom = 0.1, 0.1

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])


for i in range(-n_cubes, n_cubes+1):
  for j in range(-n_cubes, n_cubes+1):
    particle = Rectangle(((i)*d_pp-0.5*a, (j)*d_pp-0.5*a),
                        a, a,
                        color='black', fill=False, alpha=0.5)
    ax.add_patch(particle)
    if j % 2 == 0:
      ax.arrow(
        i*d_pp-0.125*a, j*d_pp, a*0.25, 0, color='#EE292F',
        head_length=2, head_width=2, zorder=2)
    else:
      ax.arrow(
        i*d_pp+0.125*a, j*d_pp, -a*0.25, 0, color='#EE292F',
        head_length=2, head_width=2, zorder=2)
seed_pairs = [
  (0,0),
  (0,1),
  (0,-1),
  (0+0.15, 0+0.15),
  (1+0.15, 0+0.15),
  (-1+0.15,0+0.15),
  (0+0.15, 1+0.15),
  (1+0.15, 1+0.15),
  (-1+0.15,1+0.15),
  (0+0.15, -1+0.15),
  (1+0.15, -1+0.15),
  (-1+0.15,-1+0.15),
  ( 0-0.15, 0+0.15),
  ( 1-0.15, 0+0.15),
  (-1-0.15,0+0.15),
  ( 0-0.15, 1+0.15),
  ( 1-0.15, 1+0.15),
  (-1-0.15,1+0.15),
  ( 0-0.15, -1+0.15),
  ( 1-0.15, -1+0.15),
  (-1-0.15,-1+0.15),
  ( 0-0.15, -2+0.15),
  ( 1-0.15, -2+0.15),
  (-1-0.15, -2+0.15),
  ( 0+0.15, -2+0.15),
  ( 1+0.15, -2+0.15),
  (-1+0.15, -2+0.15),
  (0+0.45, 0+0.25),
  (0+0.45, 0-0.25),
  (1+0.45, 0+0.25),
  (1+0.45, 0-0.25),
  (-1+0.45,0+0.25),
  (-1+0.45,0-0.25),
  (-2+0.45,0+0.25),
  (-2+0.45,0-0.25),
  (0+0.45, 1+0.25),
  (0+0.45, 1-0.25),
  (1+0.45, 1+0.25),
  (1+0.45, 1-0.25),
  
  (-1+0.45,1+0.25),
  (-1+0.45,1-0.25),
  (-2+0.45,1+0.25),
  (-2+0.45,1-0.25),
  (0+0.45, -1+0.25),
  (0+0.45, -1-0.25),
  (1+0.45, -1+0.25),
  (1+0.45, -1-0.25),
  (-1+0.45,-1+0.25),
  (-1+0.45,-1-0.25),
  (-2+0.45,-1+0.25),
  (-2+0.45,-1-0.25),
  (0+0.45, -2+0.25),
  (1+0.45, -2+0.25),
  (-1+0.45,-2+0.25),
  (-2+0.45,-2+0.25),
  (0+0.45, 2-0.25),
  (1+0.45, 2-0.25),
  (-1+0.45,2-0.25),
  (-2+0.45,2-0.25),
  ( 0+0.5, 0+0.45),
  ( 0+0.5, 0-0.45),
  ( 1+0.5, 0+0.45),
  ( 1+0.5, 0-0.45),
  (-1+0.5, 0+0.45),
  (-1+0.5, 0-0.45),
  (-2+0.5, 0+0.45),
  (-2+0.5, 0-0.45),
  ( 0+0.5, 1+0.45),
  ( 0+0.5, 1-0.45),
  ( 1+0.5, 1+0.45),
  ( 1+0.5, 1-0.45),
  (-1+0.5, 1+0.45),
  (-1+0.5, 1-0.45),
  (-2+0.5, 1+0.45),
  (-2+0.5, 1-0.45),
  ( 0+0.5, -1+0.45),
  ( 0+0.5, -1-0.45),
  ( 1+0.5, -1+0.45),
  ( 1+0.5, -1-0.45),
  (-1+0.5, -1+0.45),
  (-1+0.5, -1-0.45),
  (-2+0.5, -1+0.45),
  (-2+0.5, -1-0.45),
  ( 0+0.5, -2+0.45),
  ( 1+0.5, -2+0.45),
  (-1+0.5, -2+0.45),
  (-2+0.5, -2+0.45),
  ( 0+0.5, 2-0.45),
  ( 1+0.5, 2-0.45),
  (-1+0.5, 2-0.45),
  (-2+0.5, 2-0.45),
]
seedx, seedy = zip((*seed_pairs))
seedx = np.array(seedx)
seedy = np.array(seedy)
seed_points = np.array([seedx, seedy])*d_pp
im = ax.streamplot(xspace, yspace, (Bx*B).T, (By*B).T,
  start_points=seed_points.T,
  color=color_variant('#0EA8DF', -50),
  linewidth=1,
  density=100,
  arrowsize=1,
  arrowstyle='->',
  zorder=1)

ax.axis('off')

ax.set_xlabel("$\mathit{x} \, / \, nm$")
ax.set_ylabel("$\mathit{y} \, / \, nm$")
ax.set_aspect('equal')
ax.set_xlim([-1.75*d_pp, 1.75*d_pp])
ax.set_ylim([-1.75*d_pp, 1.75*d_pp])
# ax.set_xlim([q_min, q_max])
# ax.set_ylim([I_min, I_max])

# fig.savefig(thesisimgs + '/' + pngfile)
fig.savefig(cwd + '/' + pngfile)
