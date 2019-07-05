import sys, os, h5py, matplotlib
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import matplotlib.colors as mcolors
def get_cmap():
  def make_colormap(seq):
    """Return a LinearSegmentedColormap
    seq: a sequence of floats and RGB-tuples. The floats should be increasing
    and in the interval (0,1).
    """
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
      pos, r, g, b = item
      cdict['red'].append([pos, r, r])
      cdict['green'].append([pos, g, g])
      cdict['blue'].append([pos, b, b])
    return matplotlib.colors.LinearSegmentedColormap('CustomMap', cdict)
  #Nice Coloring:
  c = matplotlib.colors.ColorConverter().to_rgb
  custom_colors = [(0, 0, 0, 0),\
        (0.18, 0.05, 0.05, 0.2),\
        (0.28, 0, 0, 1),\
        (0.4, 0.7, 0.85, 0.9),\
        (0.45, 0, 0.75, 0),\
        (0.6, 1, 1, 0),\
        (0.75, 1, 0, 0),\
        (0.92 , 0.6, 0.6, 0.6),\
        (1  , 0.95, 0.95, 0.95)]
  custom_cmap = make_colormap(custom_colors)
  custom_cmap.set_bad(color='black')
  return custom_cmap


chapter = 'monolayers'
sample_name = 'ParacrystalSimulation'
savefile = chapter + '_GISAXS_' + sample_name

ba_file = 'simulation.int'

axis0 = ''
axis1 = ''

with open(ba_file, 'r') as f:
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

data_array = np.zeros((Ny, Nz), dtype = np.float)
with open(ba_file, 'r') as f:
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

I = data_array

detector_distance = 1733.5
wavelength = 0.13414
tthf = np.arctan((y-105.000) / detector_distance)
aiaf = np.arctan((z-58.206) / detector_distance)
k0 = 2*np.pi/wavelength
qy = k0*np.sin(tthf) #*np.cos(af) is approx 1, would require rebinning
qz = k0*np.sin(aiaf)

#plot simulation
qz_min = 0.24
qz_max = 0.3

vmin = 0.5
vmax = 1e3 #1.5e-5
ymin, ymax = 2e0, 2e4
sf = 1#2.5e-7

qz_range = np.logical_and(qz>qz_min, qz<qz_max)
yoneda_line = np.sum(I[:, qz_range], axis=1)

I_yoneda = yoneda_line
sI_yoneda = np.sqrt(yoneda_line)

I *= sf
I_yoneda *= sf
sI_yoneda *= sf

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
                    cmap=get_cmap(), vmin=vmin, vmax=vmax)
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
  linestyle='None', marker='.', capsize=0, elinewidth=1, color='#ca0020'
)
ax2.set_yscale('log')
plot_q_square_lines(0.4726, ax2)
ax.set_xticks([])

ax.set_yticks([0, 1])
ax2.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')

ax2.get_yaxis().set_visible(False)
plt.setp(ax.get_xticklabels(), visible=False)
# ax.set_xlim(-1.1,1.6)
# ax2.set_xlim(-1.1,1.6)
# ax.set_ylim(0, 1.5)
ax.set_xlim(-2.7,1.6)
ax2.set_xlim(-2.7,1.6)
ax.set_ylim(0, 2.4)
ax2.set_ylim([ymin, ymax])
ax.set_aspect('equal')

fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)