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
    return np.asarray(T), np.asarray(B), np.asarray(M), np.asarray(sM)

def average(x,y, sy, n=10):
    x_avg = x[::n]
    y_avg = y[::n]
    sy_avg = sy[::n]
    return x_avg, y_avg, sy_avg

T_10K, B_10K, M_10K, sM_10K = load_ppms_dat("DD175_23_HYST_10K_100OE.DAT")
T_300K, B_300K, M_300K, sM_300K = load_ppms_dat("DD175_23_HYST_300K.DAT")

m_SiliconTheory = -31.078
M_10K -= (m_SiliconTheory+10)*B_10K
mRT = -42
M_300K -= mRT*B_300K

fig = plt.figure()
ax = fig.add_subplot(111)
ax.axhline(0, color='#DDDDDD')
ax.axvline(0, color='#DDDDDD')
# ax.plot(B_2K, M_2K, label='2 K')
# ax.plot(B_5K, M_5K, label='5 K')
ax.plot(B_10K, M_10K, label='10 K')
# ax.plot(B_20K, M_20K, label='20 K')
ax.plot(B_300K, M_300K, label='300 K')
ax.legend(loc='lower right')
ax.set_xlabel('$\mathit{\mu_0 H} \, / \, T$')
ax.set_ylabel('$\mathit{M} \, / \, \mu emu$')
fig.tight_layout()
ax.set_xlim(-6, 6)
ax.set_ylim(-200, 200)
plt.show()