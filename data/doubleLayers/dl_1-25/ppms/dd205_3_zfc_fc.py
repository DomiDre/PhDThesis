#Initialized ScriptFactory v0.1
#Date: 2018-03-13 14:17:47.396619
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: PPMS
#Using experiment.py from PPMS folder to generate script.
import matplotlib.pyplot as plt
import numpy as np
from PPMS.ppms import PPMS

pngfilename = 'DD205_3_zfc_fc.png'

def load_file(datfile):
  ppms = PPMS()
  ppms.load(datfile)
  # ppms.clean_peaks(M_threshold=0.01, TM_mode=True, show=False)
  # ppms.reduce_averages(20)
  # T, sT, M, sM = ppms.get_TMavg()
  T, M = ppms.get_TM()
  sM = np.zeros(len(M))
  M *= 1000
  sM *= 1000

  return T, M, sM
  
T_zfc, M_zfc, sM_zfc = load_file('DD205_3_ZFC_100OE.DAT')
T_fcc, M_fcc, sM_fcc = load_file('DD205_3_FC_100OE.DAT')
fig, ax = plt.subplots()
ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(T_zfc, M_zfc, sM_zfc, linestyle='None', marker='.', zorder=1, label='ZFC')
ax.errorbar(T_fcc, M_fcc, sM_fcc, linestyle='None', marker='.', zorder=1, label='FCC')
ax.set_xlabel("$\mathit{T} \, / \, K$")
ax.set_ylabel("$\mathit{M} \, / \, \mu emu$")
ax.text(0.08, 0.85,
        'DD205.3\n$\mathit{B} \, = \, 10 \, mT$',\
        horizontalalignment='left',
        verticalalignment='top',\
        transform=ax.transAxes)
ax.set_xlim(0, 350)
ax.set_ylim(0, 34)
ax.legend(loc='upper left')
fig.tight_layout()
plt.savefig(pngfilename)
plt.show()
