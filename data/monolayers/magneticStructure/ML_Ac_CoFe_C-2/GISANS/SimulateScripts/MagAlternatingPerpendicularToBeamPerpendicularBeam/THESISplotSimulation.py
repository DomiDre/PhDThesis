import sys, os, h5py, matplotlib
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import matplotlib.colors as mcolors
from uzkBornAgain import Pilatus1M, utils
from matplotlib.legend_handler import HandlerTuple
import matplotlib.patches as patches

chapter = 'monolayers'
sample_name = 'ParacrystalSimulationMagAlternatingPerpendicularToBeamPolarizationPerpendicular'
savefile = chapter + '_GISANS_' + sample_name

ba_uu_file = 'simulation_uu.int'
ba_dd_file = 'simulation_dd.int'
ba_du_file = 'simulation_du.int'
ba_ud_file = 'simulation_ud.int'

axis0 = ''
axis1 = ''

with open(ba_uu_file, 'r') as f:
  for line in f:
    if 'axis-0' in line:
      axis0 = f.readlines(1)[0]
      continue
    elif 'axis-1' in line:
      axis1 = f.readlines(1)[0]
      break

split_axis0 = axis0.split(',')[1:]
Ny = int(split_axis0[0])
y0 = float(split_axis0[1])
y1 = float(split_axis0[2].split(')')[0])
y = np.linspace(y0, y1, Ny)

split_axis1 = axis1.split(',')[1:]
Nz = int(split_axis1[0])
z0 = float(split_axis1[1])
z1 = float(split_axis1[2].split(')')[0])
z = np.linspace(z0, z1, Nz)

def read_ba_int(intfile):
  data_array = np.zeros((Ny, Nz), dtype = np.float)
  with open(intfile, 'r') as f:
    readArray = False
    i=0
    for line in f:
      if '# data' in line:
        readArray = True
        continue
      if readArray:
        splitted_line = [float(x) for x in line.strip().split()]
        if len(splitted_line) > 0:
          data_array[i, :] = np.array(splitted_line)
        i += 1
  return data_array

I_uu = read_ba_int(ba_uu_file)
I_dd = read_ba_int(ba_dd_file)
I_ud = read_ba_int(ba_ud_file)
I_du = read_ba_int(ba_du_file)

I_u = (I_uu + I_ud)/2
I_d = (I_dd + I_du)/2

detector_distance = 5000
wavelength = 0.6
tthf = np.arctan((y - 319.225) / detector_distance)
aiaf = np.arctan((z - 326.15) / detector_distance)
k0 = 2*np.pi / wavelength
qy = k0 * np.sin(tthf)
qz = k0 * np.sin(aiaf)

#plot simulation
qz_min = 0.09
qz_max = 0.15

vmin = 0.01
vmax = 10e4 #1.5e-5

qz_range = np.logical_and(qz>qz_min, qz<qz_max)
I_u_yoneda = np.sum(I_u[:, qz_range], axis=1)
sI_u_yoneda = np.sqrt(I_u_yoneda)
I_d_yoneda = np.sum(I_d[:, qz_range], axis=1)
sI_d_yoneda = np.sqrt(I_d_yoneda)

x0, y0 = 0.17, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()
ax = fig.add_axes([x0, 0.42, width, 0.57])
ax2 = fig.add_axes([x0, y0, width, 0.25])

ax_config = fig.add_axes([0.81, 0.81, 0.25, 0.25])
ax_config.axis('off')

cube_size = 10
pp_distance = 13
Nx = 2
Ny = 2
M_direction = (0,1)
ax_config.annotate("", xy=(0, 25), xytext=(-30, 25),
  arrowprops=dict(arrowstyle="->"))
for ix in range(Nx):
  for iy in range(Ny):
    #1
    ax_config.add_patch(
        patches.Rectangle(
            (ix*2*pp_distance, iy*2*pp_distance),   # (x,y)
            cube_size,          # width
            cube_size,          # height
            fill=True,
            color='white'
        )
    )
    ax_config.arrow(ix*2*pp_distance + cube_size/2,
              iy*2*pp_distance + cube_size/4,
              M_direction[0]*cube_size/2,
              M_direction[1]*cube_size/2,
              head_width=1, head_length=1, fc='k', ec='k')
    #2
    ax_config.add_patch(
        patches.Rectangle(
            (pp_distance+ix*2*pp_distance, iy*2*pp_distance),   # (x,y)
            cube_size,          # width
            cube_size,          # height
            fill=True,
            color='white'
        )
    )
    ax_config.arrow(pp_distance+ix*2*pp_distance + cube_size/2,
              iy*2*pp_distance + 3*cube_size/4,
              M_direction[0]*cube_size/2,
              -M_direction[1]*cube_size/2,
              head_width=1, head_length=1, fc='k', ec='k')

    #3
    ax_config.add_patch(
        patches.Rectangle(
            (ix*2*pp_distance, pp_distance+iy*2*pp_distance),   # (x,y)
            cube_size,          # width
            cube_size,          # height
            fill=True,
            color='white'
        )
    )
    ax_config.arrow(ix*2*pp_distance + cube_size/2,
              pp_distance+iy*2*pp_distance + cube_size/4,
              M_direction[0]*cube_size/2,
              M_direction[1]*cube_size/2,
              head_width=1, head_length=1, fc='k', ec='k')

    #4
    ax_config.add_patch(
        patches.Rectangle(
            (pp_distance+ix*2*pp_distance, pp_distance+iy*2*pp_distance),   # (x,y)
            cube_size,          # width
            cube_size,          # height
            fill=True,
            color='white'
        )
    )
    ax_config.arrow(pp_distance+ix*2*pp_distance + cube_size/2,
              pp_distance+iy*2*pp_distance + 3*cube_size/4,
              M_direction[0]*cube_size/2,
              -M_direction[1]*cube_size/2,
              head_width=1, head_length=1, fc='k', ec='k')

ax_config.set_xlim(-5, 80)
ax_config.set_ylim(-5, 80)
ax_config.set_xticklabels([])
ax_config.set_yticklabels([])
ax_config.set_xticks([])
ax_config.set_yticks([])

pcm = ax.pcolormesh(qy, qz, I_uu.T,\
                    norm=mcolors.LogNorm(),\
                    cmap=utils.get_cmap(), vmin=vmin, vmax=vmax)
ax.axhline(qz_min, color='white', marker='None', alpha=0.5)
ax.axhline(qz_max, color='white', marker='None', alpha=0.5)
# txt = ax.text(0.95, 0.95,\
#         'Simulation',\
#         color='white',\
#         horizontalalignment='right',
#         verticalalignment='top',\
#         transform=ax.transAxes)
ax2.plot(qy, I_u_yoneda, linewidth=1, label='I(+)', marker='^', markersize=1)
ax2.plot(qy, I_d_yoneda, linewidth=1, label='I(-)', marker='v', markersize=1)
ax2.set_yscale('log')
ax.set_xticks([])

# ax.set_yticks([0, 0.5])
ax2.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')

plt.setp(ax.get_xticklabels(), visible=False)
# ax.set_xlim(-1.1,1.6)
# ax2.set_xlim(-1.1,1.6)
# ax.set_ylim(0, 1.5)
ax.set_xlim(-0.66,0.66)
ax2.set_xlim(-0.66,0.66)
ax.set_ylim(-0.11, 0.66)
ax2.set_ylim([200, 2e4])
ax.set_aspect('equal')
handles, labels = ax2.get_legend_handles_labels()
ax2.legend(
  [handles[0], handles[1]],
  ['$I^{+}$', '$I^{-}$'],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  bbox_to_anchor = [0.02, 0.12])

fig.savefig(cwd + '/' + savefile)
# fig.savefig(thesisimgs+'/'+savefile)