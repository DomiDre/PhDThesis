import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import lmfit
import datetime as dt

from GALAXI.dd_gisaxs.dd_gisaxs import DDGISAXS
import matplotlib.colors as mcolors
import matplotlib.patheffects as PathEffects
from mpl_toolkits.axes_grid1 import make_axes_locatable


default_sdd = 1733.5
default_beamcenter = (610.41, 338.41)

qz_min = 0.245
qz_max = 0.29
vmin = 1e-8
vmax = 1.5e-5
chapter = 'image'

filepath, sample_name = cwd+"/GISAXS/DD175_28.h5", 'ML-Ac-CoFe-C-2'
savefile = chapter + '_GISAXS_' + sample_name
obj = DDGISAXS()
obj.set_sdd(default_sdd)
obj.set_beamcenter(default_beamcenter[0], default_beamcenter[1])
obj.load_h5(filepath)
qy, qz = obj.get_qyqz()
qy *= 10 #transform to nm-1
qz *= 10 #transform to nm-1

data = obj.get_data()
qyslice, I_qyslice, sI_qyslice = obj.get_qy_slice(qz_min, qz_max)

x0, y0 = 0.01, 0.01
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()
ax = fig.add_axes([x0, y0, width, height])
pcm = ax.pcolormesh(qy, qz, data.T,\
                    norm=mcolors.LogNorm(),\
                    cmap=obj.cmap, vmin=vmin, vmax=vmax)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('')
ax.set_ylabel('')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)
# plt.setp(ax.get_xticklabels(), visible=False)
ax.set_xlim(-1.6,1.6)
ax.set_ylim(-1, 2)
ax.set_aspect('equal')
fig.savefig(cwd + '/' + savefile)
