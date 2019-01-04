import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams.update({'font.size': 18})


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

m_SiliconTheory = -31.078
M_10K -= (m_SiliconTheory+10)*B_10K
M_10K /= 6*4*10.1e-6*1000*10.1/13

x0, y0 = 0.21, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure(figsize=(4.5,4.5))
ax = fig.add_axes([x0, y0, width, height])

ax.axhline(0, color='#DDDDDD')
ax.axvline(0, color='#DDDDDD')
ax.plot(B_10K, M_10K, label='VSM, $\mathit{T} \, = \, 10 \,K$')
ax.legend(loc='lower right', fontsize=17)
ax.set_xlabel('$\mathit{\mu_0 H} \, / \, T$')
ax.set_ylabel('$\mathit{M} \, / \, kAm^{-1}$')
ax.set_xlim(-5.9, 5.9)
ax.set_ylim(-450, 450)
fig.savefig('DD175_23_hyst.png')
plt.show()