import sys, os
import matplotlib.pyplot as plt

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

chapter = 'monolayers'

def plot_gisas(filepath, sample_name):
  obj = DDGISAXS()
  obj.set_sdd(default_sdd)
  obj.set_beamcenter(default_beamcenter[0], default_beamcenter[1])
  obj.load_h5(filepath)

  data = obj.get_data()
  Ny, Nz = data.shape
  y = (np.arange(Ny) - default_beamcenter[0])*0.172
  z = (np.arange(Nz) - default_beamcenter[1])*0.172
  x0, y0 = 0.13, 0.17
  width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
  fig = plt.figure()

  ax = fig.add_axes([x0, y0, width, height])

  pcm = ax.pcolormesh(y, z, data.T,\
                      norm=mcolors.LogNorm(),\
                      cmap=obj.cmap, vmin = 1e-8, vmax=15e-6)
  ax.axhline(qz_min, color='white', marker='None', alpha=0.5)
  ax.axhline(qz_max, color='white', marker='None', alpha=0.5)
  ax.set_xlabel('$\mathit{y} \, / \, mm$')
  ax.set_ylabel('$\mathit{z} \, / \, mm$')
  ax.set_aspect('equal')


plot_gisas("./GISAXS/DD175_28.h5", 'ML-Ac-CoFe-C-2')
plt.show()