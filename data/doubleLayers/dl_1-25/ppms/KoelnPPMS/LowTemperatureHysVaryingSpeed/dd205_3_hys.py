#Initialized ScriptFactory v0.1
#Date: 2018-03-13 14:15:05.637807
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: PPMS
#Using experiment.py from PPMS folder to generate script.
import matplotlib.pyplot as plt
import numpy as np
from PPMS.ppms import PPMS

pngfilename = 'dd205_3_cooldown_speed_variation.png'
fig, ax = plt.subplots()
ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)

def load_and_plot(filename, label):
  ppms = PPMS()
  ppms.load(filename)
  # ppms.clean_peaks(M_threshold=0.01, show=False)
  # ppms.fit_diamagnetism(5, 9, show=False, fit_both_sides=False)
  # chi = ppms.get_diamagnetic_slope()
  B, M = ppms.get_BM()
  M *= 1000

  ax.plot(
    B, M,
    linestyle='None', marker='.', markersize=3, zorder=2,
    alpha=1, label=label
  )

for cooldown_speed in ['0-5', '1']:
  datfileCologne = './DD205_ZFC_'+cooldown_speed+'KMIN_HYS9T.DAT'
  load_and_plot(datfileCologne, cooldown_speed.replace('-','.')+' K/min')

load_and_plot('DD205_ZFC_1KMIN_HYS9T_REPRODUCE.DAT', '1 K/min Reproduce')

for cooldown_speed in ['1-5', '2']:
  datfileCologne = './DD205_ZFC_'+cooldown_speed+'KMIN_HYS9T.DAT'
  load_and_plot(datfileCologne, cooldown_speed.replace('-','.')+' K/min')

load_and_plot('DD205_ZFC_2KMIN_HYS9T_REPRODUCE.DAT', '2 K/min Reproduce')

ax.text(0.08, 0.08, '$\mathit{T} \, = \, 10 \, K$',\
        horizontalalignment='left',
        verticalalignment='bottom',\
        transform=ax.transAxes)

ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel("$\mathit{M} \, / \, \mu emu$")
ax.set_xlim(-9.2, 9.2)
ax.set_ylim(-600, 600)
ax.legend(loc='upper left')
fig.tight_layout()
plt.savefig(pngfilename)
plt.show()
