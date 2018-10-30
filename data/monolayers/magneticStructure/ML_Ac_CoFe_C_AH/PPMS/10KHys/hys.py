import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from PPMS.ppms import PPMS
from modelexp.data import XyeData

temperature = '10'
chapter = 'monolayer'
sample_name = 'ML_Ac_CoFe_C'
savefile = f'{chapter}_PPMS_VSM_{temperature}K_{sample_name}'

# datfileCologne = f'./DD205_4_KOELNPPMS_HYST_100OE_{temperature}K.DAT'
datfileCologne = 'dd205_4_10K_rescaled.dat'

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)

data = XyeData()
data.loadFromFile(datfileCologne)
B, M, sM = data.getData()

# ppms = PPMS()
# ppms.load(datfileCologne)
# ppms.fit_diamagnetism(6,9, show=False)
# B, M = ppms.get_BM()
# M *= 1000
ax.plot(B, M, linestyle='None', marker='.', markersize=1, zorder=2, alpha=0.5)

ax.text(0.05, 0.95, '$\mathit{T} \, = \, '+str(temperature)+' \, K$',\
        horizontalalignment='left',
        verticalalignment='top',\
        transform=ax.transAxes)

ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel("$\mathit{M} \, / \, kAm^{-1}$")
ax.set_xlim(-9.2, 9.2)
ax.set_ylim(-320, 320)
ax.legend(loc='upper right')
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)

