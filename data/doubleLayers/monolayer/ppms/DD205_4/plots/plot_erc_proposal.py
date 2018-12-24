#Initialized ScriptFactory v0.2
#Date: 2018-06-06 10:32:46.030365
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
import sys, os
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from thesis_utils.fileformats import load_xyem
from PPMS.ppms import PPMS

sample_name = 'DD205.4'
savefile = 'erc_PPMSM_'+sample_name+'.png'

def load_file(datfile):
  ppms = PPMS()
  ppms.load(datfile)
  ppms.reduce_averages(5)
  T, sT, M, sM = ppms.get_TMavg()
  mass = 29.86 # mg
  volume = mass / 2.336  # mm3
  area = volume / 0.525 # mm2, surface area of wafer
  particle_volume = area * 8.6e-6 * (8.6/(8.6+1.5))**2 # mm3, area times particle height
  M /= particle_volume
  sM /= particle_volume
  return T, M, sM

T_zfc, M_zfc, sM_zfc = load_file('../rawdata/DD205_4_ZFCW_100OE.DAT')
T_fcc, M_fcc, sM_fcc = load_file('../rawdata/DD205_4_FCC_100OE.DAT')

min_T, max_T = min(T_zfc), max(T_zfc)
min_M, max_M = -20, 90
B = 10

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)

ax.errorbar(
  T_zfc, M_zfc, sM_zfc, linestyle='None', marker='.', zorder=1,
  label='Zero-Field Cooled'
)
ax.errorbar(
  T_fcc, M_fcc, sM_fcc, linestyle='None', marker='.', zorder=1,
  label='Field Cooled, $\mathit{B}$ = ' + str(B) + ' mT'
)
ax.set_xlabel(r"$\mathit{T} \, / \, K$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")

ax.set_xlim(min_T, max_T)
ax.set_ylim(min_M, max_M)
ax.legend(loc='upper left')
plt.savefig(savefile)
plt.show()
