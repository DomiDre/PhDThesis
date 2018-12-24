#Initialized ScriptFactory v0.1
#Date: 2018-03-13 14:17:47.396619
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: PPMS
#Using experiment.py from PPMS folder to generate script.
import matplotlib.pyplot as plt
import numpy as np
from PPMS.ppms import PPMS

zfc_datfile = '../rawdata/DD205_4_ZFCW_100OE.DAT'
zfc_datfileCologne = './DD205_4_KOELNPPMS_ZFCW_100OE.DAT'
fc_datfile = '../rawdata/DD205_4_FCC_100OE.DAT'
fc_datfileCologne = './DD205_4_KOELNPPMS_FCC_100OE.DAT'

zfc_datfileCologne2 = './DD205_4_KOELNPPMS_ZFCW_100OE_TOUCHDOWN.DAT'
fc_datfileCologne2 = './DD205_4_KOELNPPMS_FCC_100OE_TOUCHDOWN.DAT'
fcw_datfileCologne2 = './DD205_4_KOELNPPMS_FCW_100OE_TOUCHDOWN.DAT'

pngfilename = 'compare_zfc_fc.png'

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

fig, ax = plt.subplots()
ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
# T_zfc, M_zfc, sM_zfc = load_file(zfc_datfile)
# T_fcc, M_fcc, sM_fcc = load_file(fc_datfile)
# ax.errorbar(T_zfc, M_zfc, sM_zfc, linestyle='None', marker='.', zorder=1, label='ZFC Julich')
# ax.errorbar(T_fcc, M_fcc, sM_fcc, linestyle='None', marker='.', zorder=1, label='FCC Julich')

T_zfc, M_zfc, sM_zfc = load_file(zfc_datfileCologne)
T_fcc, M_fcc, sM_fcc = load_file(fc_datfileCologne)
ax.errorbar(T_zfc, M_zfc, sM_zfc, linestyle='None', marker='.', markersize=1, zorder=1, label='ZFC Koln without Autocenter')
ax.errorbar(T_fcc, M_fcc, sM_fcc, linestyle='None', marker='.', markersize=1, zorder=1, label='FCC Koln without Autocenter')

T_zfc, M_zfc, sM_zfc = load_file(zfc_datfileCologne2)
T_fcc, M_fcc, sM_fcc = load_file(fc_datfileCologne2)
T_fcw, M_fcw, sM_fcw = load_file(fcw_datfileCologne2)
ax.errorbar(T_zfc, M_zfc, sM_zfc, linestyle='None', marker='.', markersize=1, zorder=1, label='ZFC Koln with Autocenter')
ax.errorbar(T_fcc, M_fcc, sM_fcc, linestyle='None', marker='.', markersize=1, zorder=1, label='FCC Koln with Autocenter')
ax.errorbar(T_fcw, M_fcw, sM_fcw, linestyle='None', marker='.', markersize=1, zorder=1, label='FCW Koln with Autocenter')

ax.set_xlabel("$\mathit{T} \, / \, K$")
ax.set_ylabel("$\mathit{M} \, / \, \mu emu$")
ax.text(0.08, 0.9,
        'DD205.4\n$\mathit{B} \, = \, 10 \, mT$',\
        horizontalalignment='left',
        verticalalignment='top',\
        transform=ax.transAxes)
ax.set_xlim(0, 350)
ax.set_ylim(-3, 19)
ax.legend(loc='upper right', fontsize=10)
fig.tight_layout()
plt.savefig(pngfilename)
plt.show()
