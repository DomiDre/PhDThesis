from GISANS.gisansd33 import GisansD33
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.patches as patches
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.ndimage.interpolation import rotate
from numpy import sqrt
import matplotlib

sdd = 5000 # m
qzmin,qzmax = 0.007 * 10, 0.016* 10

# Saturation:
d33_data_sat_plus = GisansD33()
d33_data_sat_plus.sdd = sdd
d33_data_sat_plus.load_file_range('./0rawdata/0206', np.arange(73, 85, 2))
qy_sat_plus, qz_sat_plus, data_sat_plus = d33_data_sat_plus.get_qyz_data()
monitor_sat_plus = d33_data_sat_plus.get_monitor()

d33_data_sat_minus = GisansD33()
d33_data_sat_minus.sdd = sdd
d33_data_sat_minus.load_file_range('./0rawdata/0206', np.arange(74, 85, 2))
qy_sat_minus, qz_sat_minus, data_sat_minus = d33_data_sat_minus.get_qyz_data()
monitor_sat_minus = d33_data_sat_minus.get_monitor()

qy = qy_sat_minus
qz = qz_sat_minus
plot_data = (data_sat_plus/ monitor_sat_plus +\
            data_sat_minus/ monitor_sat_minus)/2
# vmin =1e-4
# vmax=1e-1
# plot_projection = 0

projected_data = np.genfromtxt('./DD175_28_SatRem_Diff.xye')
qy_sat_plus = projected_data[:, 0]
I_sat = projected_data[:, 1]
sI_sat = projected_data[:, 2]
I_rem = projected_data[:, 3]
sI_rem = projected_data[:, 4]
Idiff = projected_data[:, 5]
sIdiff = projected_data[:, 6]

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
# fig = plt.figure()
# ax = fig.add_subplot(111)

# qy = qy_sat_plus
# qz = qz_sat_plus


# pcm = ax.pcolormesh(\
#         qy, qz, plot_data.T,\
#         norm=mcolors.LogNorm(), cmap=custom_cmap,
#         vmin=vmin, vmax=vmax)
# ax.add_patch(
#     patches.Rectangle(
#         (qy[0], qzmin),   # (x,y)
#         qy[-1]-qy[0],          # width
#         qzmax-qzmin,          # height
#     facecolor='white', alpha=0.6))

# ax.set_aspect('equal')

# fig.tight_layout()
# ax.set_xlim([min(qy_sat_minus), max(qy_sat_minus)])
# ax.set_ylim([min(qz_sat_minus), max(qz_sat_minus)])
# fig.savefig('DD175_28_GISANS_saturation.png')
# plt.show()



matplotlib.rcParams.update({'font.size': 18})

qy *= 10
qz *= 10
qy_sat_plus *= 10

x0, y0 = 0.13, 0.15
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure(figsize=(4.5, 4.5))

ax = fig.add_axes([x0, 0.42, width, 0.57])
ax2 = fig.add_axes([x0, y0, width, 0.25])

pcm = ax.pcolormesh(qy, qz, plot_data.T,\
                    norm=mcolors.LogNorm(),\
                    cmap=custom_cmap, vmin=5e-4, vmax=3e-2)
ax.axhline(qzmin, color='white', marker='None', alpha=0.5)
ax.axhline(qzmax, color='white', marker='None', alpha=0.5)
ax.set_xticks([])
ax2.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')

ax.text(0.01, 0.95,\
        "GISANS @ D33",\
        color='white',\
        horizontalalignment='left',
        verticalalignment='top',\
        transform=ax.transAxes, fontsize=16)


ax2.errorbar(qy_sat_plus, I_sat, sI_sat, label='Saturation', elinewidth=1, capsize=1, linewidth=1)
ax2.errorbar(qy_sat_plus, I_rem, sI_rem, label='Remanence', elinewidth=1, capsize=1, linewidth=1)
ax2.set_yscale('log')

plt.setp(ax.get_xticklabels(), visible=False)
ax.set_xlim(-0.66,0.66)
ax2.set_xlim(-0.66,0.66)
ax.set_ylim(-0.5, 0.5)
ax2.set_ylim(5e-3, 3e-1)
ax2.legend(loc='upper left', fontsize=12)
fig.savefig('Gisans175_28.png')
# plt.show()
