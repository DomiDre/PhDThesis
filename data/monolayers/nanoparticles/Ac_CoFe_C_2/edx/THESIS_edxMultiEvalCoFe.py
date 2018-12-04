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
samplename = 'Ac-CoFe-C-2'
savefile = Chapter+'_EDX_' + samplename + ".png"
data_name = 'DD130_9_YF45'

min_E, max_E = 5.5, 8.5
min_I, max_I = 0.,1.3
lines_Fe, lines_Co, intensity_Ka1 = get_x_ray_CoFe()
num_measurements = 5

legend_label = "EDX"

current_sample = data_name+'_1'
datfile = f'{cwd}/data/{current_sample}.txt'
E, I, sI = get_EI(datfile, min_E)
num_pts = len(E)
energies = np.zeros((num_pts, num_measurements))
intensities = np.zeros((num_pts, num_measurements))
sig_intensities = np.zeros((num_pts, num_measurements))
ratios = []

for i in range(1, 1+num_measurements):
  current_sample = data_name+'_'+str(i)
  datfile = f'{cwd}/data/{current_sample}.txt'

  htmfile = datfile.replace('.txt', '.htm')
  E, I, sI = get_EI(datfile, min_E)

  energies[:, i-1] = E
  intensities[:, i-1] = I
  sig_intensities[:, i-1] = sI

  elements, weight_percent, atomic_percent = load_edx_htm(htmfile)
  sf_Co = get_CoFeRatio(elements, atomic_percent)
  ratios.append(1/sf_Co)

mE = np.mean(energies, axis=1)
mI = np.mean(intensities, axis=1)
msI = np.sqrt(np.mean(sig_intensities**2, axis=1))

mRatio = np.mean(ratios)
sRatio = np.std(ratios, ddof=1)
ratio_FeCo = np.round(mRatio, 2)
sig_ratio_FeCo = int(np.round(10*np.round(sRatio,3) / (10**floor(log10(np.round(sRatio,1))))))

Fe_line = get_el_line(lines_Fe, E, min_E)
Co_line = get_el_line(lines_Co, E, min_E)
model = Fe_line/intensity_Ka1 + Co_line/mRatio


# Plot
left, bottom = 0.16, 0.16
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.errorbar(mE, mI, msI, ls="None", zorder=0, label=legend_label)
ax.plot(E, model, color='black', marker="None", zorder=1, alpha=0.5)
ax.set_xlim(min_E, max_E)
ax.set_ylim(0, 1.1)
ax.text(0.96, 0.96, r'$\mathit{n}_{Fe}/\mathit{n}_{Co}$' + f' = {ratio_FeCo}({sig_ratio_FeCo})',
  horizontalAlignment='right',
  verticalAlignment='top',
  transform=ax.transAxes)
ax.set_xlabel('$\mathit{E} \, / \, keV$')
ax.set_ylabel('$\mathit{I} \, / \, a.u.$')

fig.savefig(thesisimgs + '/' + savefile)
fig.savefig(cwd + '/' + savefile)

print('Co:Fe = ' + str(np.mean(ratios)) + ' +/- ' + str(np.std(ratios,ddof=1)))