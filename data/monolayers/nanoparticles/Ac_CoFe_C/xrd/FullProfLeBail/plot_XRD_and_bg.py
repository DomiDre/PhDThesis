#Initialized ScriptFactory v0.2
#Date: 2018-05-18 01:06:18.116619
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
from modelexp.data import PrfData

prffile = 'cofe2o4.prf'

sample_name = 'AH11'

savefile = 'XRD_'+sample_name

legend_label = "XRD"

data = PrfData()
data.loadFromFile(prffile)
tth, I, Imodel = data.getData()
bg = data.getBackground()

max_I = max(I)
I /= max_I
Imodel /= max_I
bg /= max_I
wavelength = 1.5406
q = 4*np.pi/wavelength *np.sin(tth/2 *np.pi/180)
min_q, max_q = min(q), max(q)
min_I, max_I = 0, 1.1

fig = plt.figure()
left, bottom = 0.21, 0.17
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.plot(q, I, label=legend_label, marker='.', linestyle='None', zorder=0)
ax.plot(q, Imodel, label='LeBail', marker='None', linestyle='-', zorder=1, alpha=0.5)
ax.plot(q, bg, label='Background', marker='None', linestyle='-', color='black', alpha=0.5)
ax.set_xlabel('$\mathit{q} \, / \, \AA^{-1}$')
ax.set_ylabel('$\mathit{I} \, / \, a.u.$')
ax.set_xlim([min_q, max_q])
ax.set_ylim([min_I, max_I])
ax.legend(loc='upper right', fontsize=8)
fig.savefig(savefile)