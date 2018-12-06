#Initialized ScriptFactory v0.2
#Date: 2018-05-19 20:37:21.116784
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

# remove some annoying warnings
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

import numpy as np
from thesis_utils.fileformats import load_xy, load_edx_htm
from PlottingTemplates.edx import *
from EDX.edx import *
from math import floor, log10

Chapter = 'monolayers'
samplename = 'AcAcTGA'
savefile = Chapter+'_EDX_TGA_' + samplename + ".png"

min_E, max_E = 5.5, 8.5
min_I, max_I = 0.,1.3
lines_Fe, lines_Co, intensity_Ka1 = get_x_ray_CoFe()
num_measurements = 5

legend_label = "EDX"

coAcAc = f'{cwd}/tga_acac/coacac.txt'
feAcAc = f'{cwd}/tga_acac/feacac.txt'
m_fe = 5.018
m_co = 5.815
def load_file(filename, m_init):
  with open (filename, "r", errors='ignore') as data:
    x = []
    y = []
    for _ in range(35):
      next(data)
    for line in data:
      if line.startswith('#'):
        continue
      if line.startswith('2)'):
        continue
      if line.startswith('3)'):
        continue
      strip_line = line.split()
      if len(strip_line) < 5:
        continue
      try:
        float(strip_line[0])
      except ValueError:
        continue
      x.append(float(strip_line[4])) # Sample Temperature
      w_sample = float(strip_line[1])#sample_weight
      w_baseline = float(strip_line[2])
      y.append((w_sample - w_baseline)/m_init)
  return np.asarray(x), np.asarray(y)

T_fe, w_fe = load_file(feAcAc, m_fe)
T_co, w_co = load_file(coAcAc, m_co)

# Plot
left, bottom = 0.19, 0.16
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.plot(T_fe, w_fe+1, marker="None", zorder=1, label='$Fe(acac)_3$')
ax.plot(T_co, w_co+1.11, marker="None", zorder=1, label='$Co(acac)_2$')
ax.plot([290, 290], [0.1, .5], color='black', marker='None')
ax.set_xlim(120, 450)
ax.set_ylim(0.1, 1.09)
ax.text(292, 0.52, 'Reflux Temp.',
  horizontalAlignment='left',
  verticalAlignment='top')
ax.set_xlabel('$\mathit{T} \, / \, K$')
ax.set_ylabel('$\mathit{m} / \mathit{m_0}}$')
ax.legend(loc='upper right')
fig.savefig(thesisimgs + '/' + savefile)
fig.savefig(cwd + '/' + savefile)
