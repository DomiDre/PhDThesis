from GISANS.gisansd33 import GisansD33
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.ndimage.interpolation import rotate
from numpy import sqrt

sdd = 5000 # m
qzmin,qzmax = 0.007, 0.023

# Saturation:
d33_data_sat_plus = GisansD33()
d33_data_sat_plus.sdd = sdd
d33_data_sat_plus.load_file_range('./0rawdata/0206', np.arange(73, 85, 2))
qy_sat_plus, qz_sat_plus, data_sat_plus = d33_data_sat_plus.get_qyz_data()
monitor_sat_plus = d33_data_sat_plus.get_monitor()
qzrange_sat_plus = np.logical_and(qzmin<qz_sat_plus, qz_sat_plus<qzmax)
data_projection_sat_plus = np.sum(data_sat_plus[:,qzrange_sat_plus], axis=1)

d33_data_sat_minus = GisansD33()
d33_data_sat_minus.sdd = sdd
d33_data_sat_minus.load_file_range('./0rawdata/0206', np.arange(74, 85, 2))
qy_sat_minus, qz_sat_minus, data_sat_minus = d33_data_sat_minus.get_qyz_data()
monitor_sat_minus = d33_data_sat_minus.get_monitor()
qzrange_sat_minus = np.logical_and(qzmin<qz_sat_minus, qz_sat_minus<qzmax)
data_projection_sat_minus = np.sum(data_sat_minus[:,qzrange_sat_minus], axis=1)

plot2d = 1
vmin =1e-4
vmax=1e-1
plot_projection = 0


if plot2d:
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
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plot_data = data_sat_plus / monitor_sat_plus
    pcm = ax.pcolormesh(\
            qy_sat_minus, qz_sat_minus, plot_data.T,\
            norm=mcolors.LogNorm(), cmap=custom_cmap,
            vmin=vmin, vmax=vmax)

    # ax.axhline(qzmin,color='white')
    # ax.axhline(qzmax,color='white')
    ax.set_xlabel("$ \mathit{q_y} \, / \, \AA^{-1}$")
    ax.set_ylabel("$ \mathit{q_z} \, / \, \AA^{-1}$")
    ax.set_aspect('equal')

    divider3 = make_axes_locatable(ax)
    cax = divider3.append_axes("right", size="5%", pad=0.05)
    cbar = plt.colorbar(pcm, cax=cax, label='Counts / Monitor')

    fig.tight_layout()
    ax.set_xlim([min(qy_sat_minus), max(qy_sat_minus)])
    ax.set_ylim([min(qz_sat_minus), max(qz_sat_minus)])
    fig.savefig('GISASDD175_28.png')
    plt.show()