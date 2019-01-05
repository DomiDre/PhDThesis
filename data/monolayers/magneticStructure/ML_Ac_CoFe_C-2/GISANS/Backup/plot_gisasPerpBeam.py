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
qzmin, qzmax = 0.007, 0.014

def load_files(path_prefix, filenum_list):
  d33_data = GisansD33()
  d33_data.sdd = sdd
  d33_data.load_file_range(path_prefix, filenum_list)
  qy, qz, data = d33_data.get_qyz_data()
  monitor = d33_data.get_monitor()
  qzrange = np.logical_and(qzmin<qz, qz<qzmax)
  data_projection = np.sum(data[:,qzrange], axis=1)
  sig_data_projection = np.sqrt(data_projection)
  data = data / monitor
  data_projection = data_projection / monitor
  sig_data_projection = sig_data_projection / monitor
  return qy, qz, data, data_projection, sig_data_projection

qy_sat_p, qz_sat_p, data_sat_p, I_sat_p, sI_sat_p = load_files('./0rawdata/020', np.arange(781, 804, 2))
qy_sat_m, qz_sat_m, data_sat_m, I_sat_m, sI_sat_m = load_files('./0rawdata/020', np.arange(782, 804, 2))

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

matplotlib.rcParams.update({'font.size': 18})

x0, y0 = 0.13, 0.15
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure(figsize=(4.5, 4.5))

ax = fig.add_axes([x0, 0.42, width, 0.57])
ax2 = fig.add_axes([x0, y0, width, 0.25])

pcm = ax.pcolormesh(
  qy_sat_p*10, qz_sat_p*10, data_sat_p.T,\
  norm=mcolors.LogNorm(),\
  cmap=custom_cmap, vmin=5e-4, vmax=3e-2)
ax.axhline(qzmin*10, color='white', marker='None', alpha=0.5)
ax.axhline(qzmax*10, color='white', marker='None', alpha=0.5)
ax.set_xticks([])
ax2.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')

txt = ax.text(0.01, 0.95,\
        "polGISANS\n@ D33",\
        color='white',\
        horizontalalignment='left',
        verticalalignment='top',\
        transform=ax.transAxes, fontsize=18)
txt = ax.text(0.01, 0.01,\
        "$\mathit{T}\, =\, 250 \,K$\n$\mu_0 \mathit{H} \,=\, 4\, T$\n$"+r"\mathit{\vec{H}} \mathrm{\perp} \mathit{\vec{k}}"+"$",\
        color='white',\
        horizontalalignment='left',
        verticalalignment='bottom',\
        transform=ax.transAxes, fontsize=18)
# txt.set_path_effects([PathEffects.withStroke(linewidth=5, foreground='black')])

ax2.errorbar(qy_sat_m*10, I_sat_m, sI_sat_m, label='I(+)', elinewidth=1, capsize=1, linewidth=1)
ax2.errorbar(qy_sat_p*10, I_sat_p, sI_sat_p, label='I(-)', elinewidth=1, capsize=1, linewidth=1)
ax2.set_yscale('log')

plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
ax2.set_yticks([])
ax2.get_yaxis().set_visible(False)
ax.set_xlim(-0.66,0.66)
ax2.set_xlim(-0.66,0.66)
ax.set_ylim(-0.5, 0.5)
ax2.set_ylim(5e-3, 5e-2)
ax2.legend(loc='lower center', fontsize=10)
fig.savefig('Gisans175_28_perpBeam.png')
# plt.show()
