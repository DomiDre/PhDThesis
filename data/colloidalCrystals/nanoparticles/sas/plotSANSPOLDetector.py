import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
plt.style.use('phdthesis')

import numpy as np
import pyFAI, h5py
from GISANS.gisansd33 import GisansD33


chapter = 'colloidalCrystals'

vmin, vmax = 2e-2,  3e0#1e-6, 1e-3
sdd = 2000 #  110000
beamcenter_y, beamcenter_z = 128.2559, 63.8996#65.4982, 126.261
pixelsize_y, pixelsize_z = 4, 8
wavelength = 0.721

def get_cmap():
  def make_colormap(seq):
    cdict = {'red': [], 'green': [], 'blue': []}
    for i, item in enumerate(seq):
      pos, r, g, b = item
      cdict['red'].append([pos, r, r])
      cdict['green'].append([pos, g, g])
      cdict['blue'].append([pos, b, b])
    return mcolors.LinearSegmentedColormap('CustomMap', cdict)
  c = mcolors.ColorConverter().to_rgb
  custom_colors = [
    (0, 0, 0, 0),
    (0.18, 0.05, 0.05, 0.2),
    (0.28, 0, 0, 1),
    (0.4, 0.7, 0.85, 0.9),
    (0.45, 0, 0.75, 0),
    (0.6, 1, 1, 0),
    (0.75, 1, 0, 0),
    (0.92 , 0.6, 0.6, 0.6),
    (1  , 0.95, 0.95, 0.95)
  ]
  cmap = make_colormap(custom_colors)
  cmap.set_bad(color='black')
  return cmap

def open_nexus_file(nexus_file):
  param_dict = {}
  print("Reading " + nexus_file)
  f = h5py.File(nexus_file, 'r')
  rawdata = f[f"entry0/data1/MultiDetector1_linear_data"][:,:,0]
  # rawdata = rawdata.T[:,::-1]
  param_dict["duration"] = f["entry0/duration"][0]
  param_dict["monitor"] = f['entry0/duration'][0] #f["entry0/monitor1/data"][0,0,0]
  param_dict["temperature"] = f["entry0/sample/temperature"][0]
  f.close()
  return rawdata, param_dict

def load_files(path_prefix, filenum_list):
  data = None
  monitor = None
  for range_num in filenum_list:
    datafile = f"{path_prefix}{range_num}.nxs"
    rawdata, param_dict = open_nexus_file(datafile)
    monitor = param_dict['monitor']
    if data is None:
      data = rawdata
      monitor = monitor
    else:
      data += rawdata
      monitor += monitor

  data = data / monitor
  Ny, Nz = data.shape
  y = (np.arange(Ny) - beamcenter_y)*pixelsize_y
  z = (np.arange(Nz) - beamcenter_z)*pixelsize_z
  qy = 2*np.pi/wavelength * y/sdd
  qz = 2*np.pi/wavelength * z/sdd
  return qy, qz, data

def plot(filepath, numbers, sample_name):
  savefile = chapter + f'_SANSPOL_{sample_name}'
  qy, qz, detector_data = load_files(filepath, numbers)

  x0, y0 = 0.12, 0.17
  width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
  fig = plt.figure()
  ax = fig.add_axes([x0, y0, width, height])
  pcm = ax.pcolormesh(
    qy, qz, detector_data.T,
    norm=mcolors.LogNorm(),
    cmap=get_cmap(), vmin=vmin, vmax=vmax
  )

  ax.text(1.5, -1.7, r"$\vec{\mathit{B}}$")
  ax.annotate("", xy=(2, -1.8), xytext=(1.3, -1.8),
    arrowprops=dict(arrowstyle="->"))
  deg = 90
  delta = 10
  ax.plot(
    [0,5*np.cos((deg-delta)*np.pi/180)],
    [0,5*np.sin((deg-delta)*np.pi/180)],
    color='black', marker='None')
  ax.plot(
    [0,5*np.cos((deg+delta)*np.pi/180)],
    [0,5*np.sin((deg+delta)*np.pi/180)],
    color='black', marker='None')
  ax.plot(
    [0,5*np.cos((180+deg-delta)*np.pi/180)],
    [0,5*np.sin((180+deg-delta)*np.pi/180)],
    color='black', marker='None')
  ax.plot(
    [0,5*np.cos((180+deg+delta)*np.pi/180)],
    [0,5*np.sin((180+deg+delta)*np.pi/180)],
    color='black', marker='None')
  ax.set_xlim(-2.1, 2.1)
  ax.set_ylim(-2.1, 2.1)
  ax.set_aspect('equal')
  ax.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
  ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')
  fig.savefig(cwd + '/' + savefile)
  fig.savefig(thesisimgs+'/'+savefile)

plot('./experimental_data/rawdata/094', [208, 211, 213], 'MagneticScattering_RFoff')
plot('./experimental_data/rawdata/094', [209, 212, 214], 'MagneticScattering_RFon')
