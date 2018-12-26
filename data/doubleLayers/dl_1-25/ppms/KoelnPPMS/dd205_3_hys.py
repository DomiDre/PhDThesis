#Initialized ScriptFactory v0.1
#Date: 2018-03-13 14:15:05.637807
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: PPMS
#Using experiment.py from PPMS folder to generate script.
import matplotlib.pyplot as plt
import numpy as np
from PPMS.ppms import PPMS


chi = []
for temperature in ['10', '20', '50', '100', '150', '200', '250', '300']:
  datfileCologne = './DD205_3_HYST_100OE_'+temperature+'K.DAT'
  pngfilename = 'dd205_3_'+temperature+'K.png'

  fig, ax = plt.subplots()
  ax.axhline(0, color='lightgray', marker='None', zorder=0)
  ax.axvline(0, color='lightgray', marker='None', zorder=0)

  ppms = PPMS()
  ppms.load(datfileCologne)
  ppms.fit_diamagnetism(8, 9, show=False)
  ppms.do_diamagnetic_correction(False)
  chi.append(ppms.get_diamagnetic_slope())
  B, M = ppms.get_BM()
  M *= 1000
  ax.plot(B, M, linestyle='None', marker='.', markersize=1, zorder=2, alpha=0.5, label='Koln')

  ax.text(0.08, 0.08, '$\mathit{T} \, = \, '+temperature+' \, K$',\
          horizontalalignment='left',
          verticalalignment='bottom',\
          transform=ax.transAxes)

  ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
  ax.set_ylabel("$\mathit{M} \, / \, \mu emu$")
  ax.set_xlim(-9.2, 9.2)
  ax.set_ylim(-220, 220)
  ax.legend(loc='upper right')
  fig.tight_layout()
  plt.savefig(pngfilename)
# plt.show()

print(chi)