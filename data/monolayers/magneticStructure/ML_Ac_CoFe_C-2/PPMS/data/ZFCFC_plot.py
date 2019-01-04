import matplotlib.pyplot as plt
import numpy as np


def load_ppms_dat(filename):
    T = []
    B = []
    M = []
    sM = []
    with open(filename, 'r', errors='ignore') as f:
        for line in f:
            if not line.startswith(','):
                continue
            split_line = line.split(',')
            T.append(float(split_line[2])) # K
            B.append(float(split_line[3])/1e4) # T
            M.append(float(split_line[4])*1e6) # mu emu
            sM.append(float(split_line[5])*1e6) # mu emu
    return T, B, M, sM

def average(x,y, sy, n=10):
    x_avg = x[::n]
    y_avg = y[::n]
    sy_avg = sy[::n]
    return x_avg, y_avg, sy_avg

T_ZFCw, B_ZFCw, M_ZFCw, sM_ZFCw = load_ppms_dat("DD175_23_ZFC_100OE.DAT")
T_FCw, B_FCw, M_FCw, sM_FCw = load_ppms_dat("DD175_23_FW_100OE.DAT")
T_FCc, B_FCc, M_FCc, sM_FCc = load_ppms_dat("DD175_23_FC_100OE.DAT")
T_FC6Tw, B_FC6Tw, M_FC6Tw, sM_FC6Tw = load_ppms_dat("DD175_23_FC_6T_FW_10MT.DAT")


T_FCw, M_FCw, sM_FCw = average(T_FCw, M_FCw, sM_FCw, 25)
T_ZFCw, M_ZFCw, sM_ZFCw = average(T_ZFCw, M_ZFCw, sM_ZFCw, 25)
T_FC6Tw, M_FC6Tw, sM_FC6Tw = average(T_FC6Tw, M_FC6Tw, sM_FC6Tw, 25)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.errorbar(T_FCw, M_FCw, sM_FCw, label='FCw')
ax.errorbar(T_ZFCw, M_ZFCw, sM_ZFCw, label='ZFCw')
ax.errorbar(T_FC6Tw, M_FC6Tw, sM_FC6Tw, label='FC6Tw')
ax.legend(loc='upper right')
ax.set_xlabel('$\mathit{T} \, / \, K$')
ax.set_ylabel('$\mathit{M} \, / \, \mu emu$')
fig.tight_layout()
fig.savefig('DD175_23_zfc_fc.png')
plt.show()