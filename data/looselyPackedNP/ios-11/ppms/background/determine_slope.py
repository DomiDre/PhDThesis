#Initialized ScriptFactory v0.1
#Date: 2018-03-13 14:15:05.637807
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: PPMS
#Using experiment.py from PPMS folder to generate script.
import matplotlib.pyplot as plt
import numpy as np
from PPMS.ppms import PPMS

datfiles = ['./CO2_HYS.DAT', './MA1588_HYS300K.DAT', './MA15100_HYS300K.DAT', './MSCO28_HYS300K.DAT', './DTOLUENE_HYS300K.DAT']
datfiles = ['./DTOLUENE_HYS300K.DAT']
slopes = []
def get_slope(datfile):
  ppms = PPMS()
  ppms.load(datfile)
  ppms.do_diamagnetic_correction = False
  ppms.fit_diamagnetism(2, 3, show=False)
  slope = ppms.get_diamagnetic_slope()
  slopes.append(slope)

for datfile in datfiles:
  get_slope(datfile)

for i, datfile in enumerate(datfiles):
  print(f'{datfile.replace(".DAT", "")}\t{slopes[i].value}')

# B, M = ppms.get_BM()
# M *= 1000

# fig, ax = plt.subplots()
# ax.axhline(0, color='lightgray', marker='None', zorder=0)
# ax.axvline(0, color='lightgray', marker='None', zorder=0)
# def load_and_plot(datfile):
#   ppms = PPMS()
#   ppms.load(datfile)
#   B, M = ppms.get_BM()
#   M *= 1000
#   ax.plot(B, M, linestyle='None', marker='.', markersize=1, zorder=2, alpha=0.5, label=datfile.replace('.DAT',''))

#   # ax.text(0.08, 0.08, '$\mathit{T} \, = \, '+temperature+' \, K$',\
#   #         horizontalalignment='left',
#   #         verticalalignment='bottom',\
#   #         transform=ax.transAxes)
# load_and_plot('./CO2_HYS.DAT')
# load_and_plot('./MA1588_HYS300K.DAT')
# load_and_plot('./MA15100_HYS300K.DAT')
# load_and_plot('./MSCO28_HYS300K.DAT')
# load_and_plot()

# ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
# ax.set_ylabel("$\mathit{M} \, / \, \mu emu$")
# ax.set_xlim(-3.2, 3.2)
# ax.set_ylim(-2100, 2100)
# ax.legend(loc='upper left', fontsize=8)
# fig.tight_layout()
# plt.savefig('data.png')
