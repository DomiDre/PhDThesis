#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:48:40.453330
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np

from modelexp.data import XyeData

datfile = './rescale/DD67_10K_LangevinSAXSscaled.xye'
datfileFC1T = './rescale/DD67_10K_FC1T_LangevinSAXSscaled.xye'

chapter = 'monolayer'
sample_name = 'Ol_CoFe_C'

savefile = chapter + '_VSM_10K_' + sample_name

data = XyeData()
data.loadFromFile(datfile)
B, M, sM = data.getData()

data = XyeData()
data.loadFromFile(datfileFC1T)
B_FC1T, M_FC1T, sM_FC1T = data.getData()

min_B, max_B = min(B), max(B)
min_M, max_M = -190, 190
T = 10

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(B, M, sM, linestyle='None', marker='.', zorder=2,\
            label='Ol-CoFe-C\n$\mathit{T} \,=\, ' + str(T) + ' \,K$', capsize=0)
ax.errorbar(B_FC1T, M_FC1T, sM_FC1T, linestyle='None', marker='.', zorder=1,\
            label='FC in 1 T', capsize=0, alpha=0.5)

ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")

ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
ax.legend(loc='lower right')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)
