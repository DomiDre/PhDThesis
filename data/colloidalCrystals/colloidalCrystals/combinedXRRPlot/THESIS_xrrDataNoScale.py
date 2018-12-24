#Initialized ScriptFactory v0.2
#Date: 2018-07-11 20:36:37.178142
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import warnings
from modelexp.data import XyeData
import matplotlib.patches as mpatches

# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

Chapter = 'colloidalCrystals'

xrrfile_25 = '../CC_Fe_0.25/XRR/DD151_2_1_cleaned_corrected.xye'
xrrfile_37 = '../CC_Fe_0.37/XRR/DD151_28_cleaned_corrected.xye'
xrrfile_50 = '../CC_Fe_0.50/XRR/DD151_30_cleaned_corrected.xye'

q_min, q_max = 0.013, 0.3
I_min, I_max = 1e-6, 1.9e1

refl_pngfile = f"{Chapter}_VerticalStructure_Combined_XRR_NoScale.png"

def get_data(file):
  data = XyeData()
  data.loadFromFile(file)
  q, I, sI = data.getData()
  q = np.array(q)
  I = np.array(I)
  sI = np.array(sI)
  valid_data = sI/I < 0.7
  q = q[valid_data]
  I = I[valid_data]
  sI = sI[valid_data]
  return q, I, sI

#load data
q_25, I_25, sI_25 = get_data(xrrfile_25)
q_37, I_37, sI_37 = get_data(xrrfile_37)
q_50, I_50, sI_50 = get_data(xrrfile_50)

left, bottom = 0.19, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

sf1 = 1

ax.errorbar(q_25, I_25*sf1, sI_25*sf1,
  label='CC-Fe-0.25',
  linestyle='None',
  zorder=0, capsize=0, marker='.', markersize=1)
ax.errorbar(q_37, I_37, sI_37,
  label='CC-Fe-0.37',
  linestyle='None',
  zorder=0, capsize=0, marker='.', markersize=1)
ax.errorbar(q_50, I_50/sf1, sI_50/sf1,
  label='CC-Fe-0.50',
  linestyle='None',
  zorder=0, capsize=0, marker='.', markersize=1)

ax.legend(loc='upper right')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, \AA^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)
