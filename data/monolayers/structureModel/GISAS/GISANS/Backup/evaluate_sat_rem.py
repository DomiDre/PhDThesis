from GISANS.gisansd33 import GisansD33
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.ndimage.interpolation import rotate
from numpy import sqrt

sdd = 5000 # m
qzmin,qzmax = 0.007, 0.023

# # Guide Field I+
# d33_data_gf_plus = GisansD33()
# d33_data_gf_plus.sdd = sdd
# d33_data_gf_plus.load_file_range('./0rawdata/0206', np.arange(48, 56, 2))
# qy_gf_plus, qz_gf_plus, data_gf_plus = d33_data_gf_plus.get_qyz_data()
# monitor_gf_plus = d33_data_gf_plus.get_monitor()
# qzrange_gf_plus = np.logical_and(qzmin<qz_gf_plus, qz_gf_plus<qzmax)
# data_projection_gf_plus = np.sum(data_gf_plus[:,qzrange_gf_plus], axis=1)


# d33_data_gf_minus = GisansD33()
# d33_data_gf_minus.sdd = sdd
# d33_data_gf_minus.load_file_range('./0rawdata/0206', np.arange(49, 56, 2))
# qy_gf_minus, qz_gf_minus, data_gf_minus = d33_data_gf_minus.get_qyz_data()
# monitor_gf_minus = d33_data_gf_minus.get_monitor()
# qzrange_gf_minus = np.logical_and(qzmin<qz_gf_minus, qz_gf_minus<qzmax)
# data_projection_gf_minus = np.sum(data_gf_minus[:,qzrange_gf_minus], axis=1)


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

#Remanence
d33_data_rem_plus = GisansD33()
d33_data_rem_plus.sdd = sdd
d33_data_rem_plus.load_file_range('./0rawdata/0206', np.arange(85, 97, 2))
qy_rem_plus, qz_rem_plus, data_rem_plus = d33_data_rem_plus.get_qyz_data()
monitor_rem_plus = d33_data_rem_plus.get_monitor()
qzrange_rem_plus = np.logical_and(qzmin<qz_rem_plus, qz_rem_plus<qzmax)
data_projection_rem_plus = np.sum(data_rem_plus[:,qzrange_rem_plus], axis=1)

d33_data_rem_minus = GisansD33()
d33_data_rem_minus.sdd = sdd
d33_data_rem_minus.load_file_range('./0rawdata/0206', np.arange(86, 97, 2))
qy_rem_minus, qz_rem_minus, data_rem_minus = d33_data_rem_minus.get_qyz_data()
monitor_rem_minus = d33_data_rem_minus.get_monitor()
qzrange_rem_minus = np.logical_and(qzmin<qz_rem_minus, qz_rem_minus<qzmax)
data_projection_rem_minus = np.sum(data_rem_minus[:,qzrange_rem_minus], axis=1)

plot2d = 1
vmin =1
vmax=100
plot_projection = 1

if plot_projection:
    fig = plt.figure(figsize=(10,4))
    # ax = fig.add_subplot(131)
    # ax2 = fig.add_subplot(132, sharex=ax, sharey=ax)
    ax3 = fig.add_subplot(111)#, sharex=ax, sharey=ax)
    
    # ax3.errorbar(qy_gf_plus, data_projection_gf_plus / monitor_gf_plus,\
    #              sqrt(data_projection_gf_plus) / monitor_gf_plus, label='Initial I+')
    ax3.errorbar(qy_sat_plus, data_projection_sat_plus / monitor_sat_plus,\
                 sqrt(data_projection_sat_plus) / monitor_sat_plus, label='Saturation I+')
    ax3.errorbar(qy_rem_plus, data_projection_rem_plus / monitor_rem_plus,\
                 sqrt(data_projection_rem_plus) / monitor_rem_plus, label='Remanence I+')
    
    # ax3.errorbar(qy_gf_minus, data_projection_gf_minus / monitor_gf_minus,\
    #              sqrt(data_projection_gf_minus) / monitor_gf_minus, label='Initial I-')
    ax3.errorbar(qy_sat_minus, data_projection_sat_minus / monitor_sat_minus,\
                 sqrt(data_projection_sat_minus) / monitor_sat_minus, label='Saturation I-')
    ax3.errorbar(qy_rem_minus, data_projection_rem_minus / monitor_rem_minus,\
                 sqrt(data_projection_rem_minus) / monitor_rem_minus, label='Remanence I-')
    ax3.legend(loc='upper right')
    ax3.set_yscale('log')
    ax3.set_xlabel("$ \mathit{q_y} \, / \, \AA^{-1}$")
    ax3.set_ylabel("$ \mathit{I} \, / \, a.u.$")
    ax3.set_xlim(0,0.068)
    ax3.set_ylim(1e-2, 2e-1)
    fig.tight_layout()
    fig.savefig('Projection.png')
    plt.show()

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
    fig = plt.figure(figsize=(10,4))
    ax = fig.add_subplot(121)
    ax2 = fig.add_subplot(122, sharex=ax, sharey=ax)
    pcm = ax.pcolormesh(\
            qy_sat_minus, qz_sat_minus, data_sat_minus.T,\
            norm=mcolors.LogNorm(), cmap=custom_cmap,vmin=vmin, vmax=vmax)

    pcm2 = ax2.pcolormesh(\
            qy_rem_minus, qz_rem_minus, data_rem_minus.T,\
            norm=mcolors.LogNorm(), cmap=custom_cmap, vmin=vmin, vmax=vmax)

    ax.axhline(qzmin,color='white')
    ax.axhline(qzmax,color='white')
    ax.set_xlabel("$ \mathit{q_y} \, / \, \AA^{-1}$")
    ax.set_ylabel("$ \mathit{q_z} \, / \, \AA^{-1}$")
    #ax.set_aspect('equal')

    ax2.axhline(qzmin,color='white')
    ax2.axhline(qzmax,color='white')
    ax2.set_xlabel("$ \mathit{q_y} \, / \, \AA^{-1}$")
    ax2.axes.get_yaxis().set_visible(False)
    #ax2.set_aspect('equal')



    fig.tight_layout()
    ax.set_xlim([min(qy_sat_minus), max(qy_sat_minus)])
    ax.set_ylim([min(qz_sat_minus), max(qz_sat_minus)])
    ax2.set_xlim([min(qy_rem_minus), max(qy_rem_minus)])
    ax2.set_ylim([min(qz_rem_minus), max(qz_rem_minus)])
    fig.savefig('2dImagesSatRem.png')
    plt.show()