#Initialized ScriptFactory v0.2
#Date: 2018-06-06 10:32:46.030365
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
import sys, os
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from utils.fileformats import load_xyem
from PPMS.ppms import PPMS

datfile = 'DD205_4_HYST_100OE_10K.DAT'

sample_name = 'DD205.4'

savefile = 'VSM_'+sample_name

PPMS = PPMS()
PPMS.load(datfile)
B, M = PPMS.get_BM()
# chi = -0.020179117390692787
# M -= chi*B
M *= 1000
mass = 30
volume = mass / 2.336
area = volume / 
min_B, max_B = min(B), max(B)
min_M, max_M = -420, 420
T = 300

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(B, M, sM, linestyle='None', marker='.', zorder=1,\
            label=r'Dispersion\n$\mathit{T} \,=\, '+str(T)+' \,K$', capsize=0)
ax.plot(B, Mmodel, marker='None', zorder=2, label='Langevin', color='black')
ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")

ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
ax.legend(loc='upper left')
plt.savefig(savefile)
