import numpy as np
import matplotlib as mpl
from cube_magnet import magnetic_cube
import numpy as np
import scipy.constants as sc

from numpy import cos, sin, pi, sqrt
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle
from matplotlib.pyplot import cm
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.animation as manimation


pi = np.pi
muB = sc.physical_constants["Bohr magneton"][0] *1e18# A nm2
mu0 = sc.mu_0 * 1e3 * 1e9  # mT * nm / A
d_pp = 20 # nm
r = d_pp/2 - 1
V = 4/3 *pi * r**3
a = V**(1/3)

mu = 12.7*muB
Ms = mu/V # A / nm

plot_dipole = False

magnetic_cube.ms = Ms
magnetic_cube.a = a

fov_x = a*3
fov_y = a*3
npts = 200
clim = [0,80]
xspace = np.linspace(-fov_x, fov_x, npts)
yspace = np.linspace(-fov_y, fov_y, npts)

zval = 0.
box_center = np.array([0,0,0])
box_corner = box_center - np.array([a/2,a/2,a/2])
n_cubes = 5
B, Bx, By, Bz = 0,0,0,0
for i in range(-n_cubes, n_cubes):
    if plot_dipole:
        x, y, hB, hBx, hBy, hBz = magnetic_cube.get_b_xy_dipole(\
                     xspace, yspace, zval,\
                     box_center+ np.array([0,i*d_pp,0]),\
                     
                     (1,0,0), (0,0,-1),(0,1,0))
    else:
        x, y, hB, hBx, hBy, hBz = magnetic_cube.get_b_xy(\
                         xspace, yspace, zval,\
                         box_corner + np.array([0,i*d_pp,0]),\
                         (1,0,0), (0,0,-1),(0,1,0))
    Bx = B*Bx + hB*hBx
    By = B*By + hB*hBy
    Bz = B*Bz + hB*hBz
    B = np.sqrt(Bx**2 + By**2 + Bz**2)
    Bx /= B
    By /= B
    Bz /= B


fig, ax = plt.subplots()
ax.set_aspect('equal')
ax.set_xlim([-1.75*d_pp, 1.75*d_pp])
ax.set_ylim([-1.75*d_pp, 1.75*d_pp])

im = ax.streamplot(xspace, yspace, (Bx*B).T, (By*B).T,\
                   color='black',\
                   linewidth=1,\
                    arrowstyle='->',\
                    arrowsize=5, density=4)#,\


for i in range(-n_cubes, n_cubes):
    if plot_dipole:
        particle = Circle((box_center[0], i*d_pp+box_center[1]),\
                      r,\
                      color='black', fill=False, hatch='//')
    else:
        particle = Rectangle((box_corner[0], i*d_pp+box_corner[1]),\
                      a, a,\
                      color='black', fill=False, hatch='//')
    ax.add_patch(particle)

ax.set_xlabel("$\mathit{x} \, / \, nm$")
ax.set_ylabel("$\mathit{y} \, / \, nm$")
fig.tight_layout()
if plot_dipole:
    fig.savefig('DipoleChain.png')
else:
    fig.savefig('CubeChain.png')
plt.show()
