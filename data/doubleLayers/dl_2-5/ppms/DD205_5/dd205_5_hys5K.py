#Initialized ScriptFactory v0.1
#Date: 2018-03-13 14:15:05.637807
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: PPMS
#Using experiment.py from PPMS folder to generate script.
import matplotlib.pyplot as plt
import numpy as np
from PPMS.ppms import PPMS

datfile = 'DD205_5_HYST_100OE_5K.DAT'
pngfilename = 'DD205_5_HYST_100OE_5K.png'

PPMS = PPMS()
PPMS.load(datfile)
B, M = PPMS.get_BM()
# chi = -0.020179117390692787
# M -= chi*B
M *= 1000

fig, ax = plt.subplots()
ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.plot(B, M, linestyle='None', marker='.', zorder=1, label='DD205.5')
ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel("$\mathit{M} \, / \, \mu emu$")
ax.text(0.08, 0.88, '$\mathit{T} \, = \, 5 \, K$',\
        horizontalalignment='left',
        verticalalignment='bottom',\
        transform=ax.transAxes)
# ax.set_xticks(np.arange(-9,10,3))
ax.set_xlim(-9.2, 9.2)
ax.set_ylim(-220, 220)
ax.legend(loc='upper left')
fig.tight_layout()
plt.savefig(pngfilename)
plt.show()
