#Initialized ScriptFactory v0.1
#Date: 2018-03-13 14:15:05.637807
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: PPMS
#Using experiment.py from PPMS folder to generate script.
import matplotlib.pyplot as plt
import numpy as np
from PPMS.ppms import PPMS


for suffix in ['', '_2', '_3']:
  datfileCologne = './DD205_4_KOELNPPMS_HYST_100OE_50K'+suffix+'.DAT'
  pngfilename = 'dd205_4_50K'+suffix+'.png'

  fig, ax = plt.subplots()
  ax.axhline(0, color='lightgray', marker='None', zorder=0)
  ax.axvline(0, color='lightgray', marker='None', zorder=0)

  ppms = PPMS()
  ppms.load(datfileCologne)
  B, M = ppms.get_BM()
  M *= 1000
  ax.plot(B, M, linestyle='None', marker='.', markersize=1, zorder=2, alpha=0.5, label='Koln')

  ax.text(0.08, 0.08, '$\mathit{T} \, = \, 50 \, K$',\
          horizontalalignment='left',
          verticalalignment='bottom',\
          transform=ax.transAxes)

  ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
  ax.set_ylabel("$\mathit{M} \, / \, \mu emu$")
  ax.set_xlim(-9.2, 9.2)
  ax.set_ylim(-520, 520)
  ax.legend(loc='upper right')
  fig.tight_layout()
  plt.savefig(pngfilename)
# plt.show()
