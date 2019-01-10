import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import lmfit
import fabio
import datetime as dt

from GALAXI.dd_gisaxs.dd_gisaxs import DDGISAXS
import matplotlib.colors as mcolors
import matplotlib.patheffects as PathEffects
from mpl_toolkits.axes_grid1 import make_axes_locatable

wavelength = 1.033202
pixelsize = 0.172 #mm
sdd = 2907.08 #mm
beam_center_y = 324.5
beam_center_z = 62.09

qz_width = 0.02
qz_min = 0.36 - qz_width/2
qz_max = 0.36 + qz_width/2
vmin = 5e0 #1e-8
vmax = 1e4 #1.5e-5
chapter = 'looselyPackedNP'
sample_name = 'SC-IOS-7'
tiffile = cwd + "/rawdata/ES-S17_pos02_.tif"
savefile = chapter + '_GISAXS_' + sample_name


obj = DDGISAXS()
data_file = fabio.open(tiffile)
header = data_file.header
data = data_file.data
y = np.arange(data.shape[0])
z = np.arange(data.shape[1])

k0 = 2*np.pi/wavelength
tth = np.arctan((y-beam_center_y)*pixelsize/sdd/2)
aiplusaf = np.arctan((z-beam_center_z)*pixelsize/sdd/2)
qy = 2*k0*np.sin(tth)
qz = 2*k0*np.sin(aiplusaf)

qy *= 10 #transform to nm-1
qz *= 10 #transform to nm-1

yoneda_data = []
qz_range = np.logical_and(qz> qz_min, qz<qz_max)
yoneda_data = np.sum(data[:, qz_range], axis=1)
print(np.sum(qz_range))
background_line = np.sum(data[:, -1*np.sum(qz_range):], axis=1)
bg_est = np.mean(background_line)
sbg_est = np.std(background_line, ddof=1)

headerstring = f"Extracted data from {tiffile}\n"+\
               f"Projected data from qz = {qz_min} .. {qz_max}\n"+\
               f"Background estimate: {bg_est} +/- {sbg_est}\n"+\
               f"q_y / A-1 \t I / Counts"
valid_data = yoneda_data > 0
qy_save = qy[valid_data]
yoneda_save = yoneda_data[valid_data]
np.savetxt(f"{sample_name}_Yoneda.xye",\
    np.c_[qy_save/10, yoneda_save, np.sqrt(yoneda_save)],\
    header=headerstring)

x0, y0 = 0.13, 0.17
width, height = 1 - x0 - 0.15, 1 - y0 - 0.01
fig = plt.figure()
ax = fig.add_axes([x0, y0, width, height])
cax = fig.add_axes([0.86, y0+0.025, 0.025, height-0.046])

pcm = ax.pcolormesh(qy, qz, data.T,\
                    norm=mcolors.LogNorm(),\
                    cmap=obj.cmap, vmin=vmin, vmax=vmax)
cbar = fig.colorbar(pcm, cax=cax, orientation='vertical')
ax.axhline(qz_min, color='white', marker='None', alpha=0.5)
ax.axhline(qz_max, color='white', marker='None', alpha=0.5)

ax.set_yticks([0, 1, 2])
ax.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')

txt = ax.text(0.95, 0.95,\
        sample_name,\
        color='white',\
        horizontalalignment='right',
        verticalalignment='top',\
        transform=ax.transAxes)

ax.set_xlim(-1.1,2.2)
ax.set_ylim(-0.2, 2.8)
ax.set_aspect('equal')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
