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
savefile = 'erc_PPMSM_'+sample_name+'Hys10K.png'

def load_file(datfile):
  ppms = PPMS()
  ppms.load(datfile)
  ppms.clean_peaks(M_threshold=0.01, show=False)
  ppms.reduce_averages(10)
  B, sB, M, sM = ppms.get_BMavg()
  # sM = np.zeros(len(M))
  # chi_300K = -0.03751104
  M -= -0.026*B
  mass = 29.86 # mg
  volume = mass / 2.336  # mm3
  area = volume / 0.525 # mm2, surface area of wafer
  a = 8.6 # tem
  d = 1.5 # estimated
  particle_volume = area * a*1e-6 * (a/(a+d))**2 # mm3, area times particle height
  M /= particle_volume
  sM /= particle_volume
  return B, M, sM

B, M, sM = load_file('../rawdata/DD205_4_HYST_100OE_10K.DAT')

min_B, max_B = -9, 9
min_M, max_M = -550, 550
T = 10

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)

ax.errorbar(
  B, M, sM, linestyle='None', marker='.', zorder=1,
  label='$\mathit{T}$ = ' + str(T) + ' K'
)
ax.set_xlabel(r"$\mu_0 \mathit{H} \, / \, T$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")

ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
ax.legend(loc='upper left')
plt.savefig(savefile)
plt.show()
