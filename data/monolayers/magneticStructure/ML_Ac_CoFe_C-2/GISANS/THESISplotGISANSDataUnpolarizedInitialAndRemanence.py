import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis2cols')

from GISANS.gisansd33 import GisansD33
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as patches
import matplotlib.patheffects as PathEffects
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.ndimage.interpolation import rotate
from numpy import sqrt
import matplotlib

sdd = 5000 # m
qzmin, qzmax = 0.009, 0.013
vmin=2
vmax=5e2

chapter = 'monolayers'
savefile = chapter + '_GISANS_ML-Ac-CoFe-C-2_ZFC5K_Unpolarized_GF_Remanence'
def load_files(path_prefix, filenum_list):
  d33_data = GisansD33(transpose=False)
  d33_data.sdd = sdd
  d33_data.load_file_range(path_prefix, filenum_list)
  qy, qz, data = d33_data.get_qyz_data()
  monitor = d33_data.get_monitor()

  mask = np.ones(data.shape)
  mask_y = np.logical_and(qy < 0.008, qy > -0.005)
  mask[mask_y, :] = mask[mask_y, :] + 1
  mask_z = np.logical_and(qz < 0.007, qz > -0.005)
  mask[:, mask_z] = mask[:, mask_z] + 1
  data[mask > 2] = 0
  
  qzrange = np.logical_and(qzmin<qz, qz<qzmax)
  data_projection = np.sum(data[:,qzrange], axis=1)
  sig_data_projection = np.sqrt(data_projection)
  data = data / monitor* 14000
  data_projection = data_projection / monitor* 14000
  sig_data_projection = sig_data_projection / monitor* 14000
  
  return qy, qz, data, data_projection, sig_data_projection

qy_ini, qz_ini, data_ini, I_ini, sI_ini = load_files('./0rawdata/020', np.arange(947, 959, 1))
qy_rem, qz_rem, data_rem, I_rem, sI_rem = load_files('./0rawdata/020', np.arange(959, 970, 1))

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
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)
#Nice Coloring:
c = mcolors.ColorConverter().to_rgb
sabrina_colors = [(0, 0, 0, 0),\
         (0.18, 0.05, 0.05, 0.2),\
         (0.28, 0, 0, 1),\
         (0.4, 0.7, 0.85, 0.9),\
         (0.45, 0, 0.75, 0),\
         (0.6, 1, 1, 0),\
         (0.75, 1, 0, 0),\

         (0.92 , 0.6, 0.6, 0.6),\
         (1  , 0.95, 0.95, 0.95)]
custom_cmap = make_colormap(sabrina_colors)
custom_cmap.set_bad(color='black')



x0, y0 = 0.10, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()

ax = fig.add_axes([x0, 0.45, width/2, 0.57])
axR = fig.add_axes([x0+width/2, 0.45, width/2, 0.57])
ax2 = fig.add_axes([x0, y0, width, 0.22])

pcm = ax.pcolormesh(
  qy_ini*10, qz_ini*10, data_ini.T,\
  norm=mcolors.LogNorm(),\
  cmap=custom_cmap, vmin=vmin, vmax=vmax)
pcm2 = axR.pcolormesh(
  qy_rem*10, qz_rem*10, data_rem.T,\
  norm=mcolors.LogNorm(),\
  cmap=custom_cmap, vmin=vmin, vmax=vmax)
ax.axhline(qzmin*10, color='white', marker='None', alpha=0.5)
ax.axhline(qzmax*10, color='white', marker='None', alpha=0.5)
axR.axhline(qzmin*10, color='white', marker='None', alpha=0.5)
axR.axhline(qzmax*10, color='white', marker='None', alpha=0.5)
# ax.set_xticks([])
ax2.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')

txt = ax.text(0.99, 0.95,\
        "ML-Ac-CoFe-C-2\nInitial",\
        color='black',\
        horizontalalignment='right',
        verticalalignment='top',\
        transform=ax.transAxes, fontsize= 8)
txt = axR.text(0.99, 0.95,\
        "ML-Ac-CoFe-C-2\nRemanence",\
        color='black',\
        horizontalalignment='right',
        verticalalignment='top',\
        transform=axR.transAxes, fontsize= 8)
# txt = ax.text(0.01, 0.01,\
#         "$T\, =\, 250 \,K$\n$\mu_0 H \,=\, 4\, T$",\
#         color='white',\
#         horizontalalignment='left',
#         verticalalignment='bottom',\
#         transform=ax.transAxes, fontsize=18)
# txt.set_path_effects([PathEffects.withStroke(linewidth=5, foreground='black')])

ax2.errorbar(qy_ini*10, I_ini, sI_ini, label='$\mathit{I}_{initial}$', elinewidth=1, capsize=1, linewidth=1, color='#76C152')
ax2.errorbar(qy_rem*10, I_rem, sI_rem, label='$\mathit{I}_{rem.}$', elinewidth=1, capsize=1, linewidth=1, color='#7F0128')
ax2.set_yscale('log')

# plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(axR.get_yticklabels(), visible=False)
ax.set_xlim(-0.66,0.66)
axR.set_xlim(-0.66,0.66)
ax2.set_xlim(-0.66,0.66)
ax.set_ylim(-0.11, 0.49)
axR.set_ylim(-0.11, 0.49)
ax.set_aspect('equal')
axR.set_aspect('equal')
ax2.set_ylim(150, 8e2)
ax2.legend(loc='lower center', fontsize=10)
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
