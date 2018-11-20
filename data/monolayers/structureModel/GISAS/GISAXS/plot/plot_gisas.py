import numpy as np
import matplotlib.pyplot as plt
from GALAXI.dd_gisaxs.dd_gisaxs import DDGISAXS
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable

obj = DDGISAXS()
obj.set_sdd(1733.5)
obj.set_beamcenter(610.41, 338.41)
obj.load_h5('DD175_28.h5')
qy, qz = obj.get_qyqz()
qy *= 10
qz *= 10

data = obj.get_data()
q_min = 0.23
q_max = 0.3
qyslice, I_qyslice, sI_qyslice = obj.get_qy_slice(q_min, q_max)


def plot_q_square_lines(q10, ax):
    ymin = 0.1
    ymax = 0.2

    # rest position of peaks
    qsquare = lambda h,k: q10 * np.sqrt(h**2 + k**2)
    q11 = qsquare(1,1)
    q20 = qsquare(2,0)
    q21 = qsquare(2,1)
    q22 = qsquare(2,2)
    q30 = qsquare(3,0)
    q31 = qsquare(3,1)
    q32 = qsquare(3,2)
    q33 = qsquare(3,3)

    ax.axvline(q10, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(q11, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(q20, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(q21, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(q22, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(q30, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(q31, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(q32, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(q33, color='black', ymin=ymin, ymax=ymax, marker='None')


    ax.axvline(-q10, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(-q11, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(-q20, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(-q21, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(-q22, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(-q30, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(-q31, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(-q32, color='black', ymin=ymin, ymax=ymax, marker='None')
    ax.axvline(-q33, color='black', ymin=ymin, ymax=ymax, marker='None')


fig = plt.figure()
ax = fig.add_axes([0.15, 0.4, 1-0.25,0.55])
ax2 = fig.add_axes([0.15, 0.15, 1-0.25-0.055,0.25])

pcm = ax.pcolormesh(qy, qz, data.T,\
                    norm=mcolors.LogNorm(),\
                    cmap=obj.cmap, vmin = 1e-8, vmax=1e-5)
ax.axhline(q_min, color='white', marker='None', alpha=0.5)
ax.axhline(q_max, color='white', marker='None', alpha=0.5)
divider3 = make_axes_locatable(ax)
cax = divider3.append_axes('right', size="5%", pad=0.1)
cbar = fig.colorbar(pcm, cax=cax, orientation='vertical')
ax.set_xticks([])
ax2.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')

ax.text(0.95, 0.95,\
        "GISAXS @ GALAXI",\
        color='white',\
        horizontalalignment='right',
        verticalalignment='top',\
        transform=ax.transAxes)


plot_q_square_lines(0.484, ax2)
ax2.errorbar(qyslice, I_qyslice, sI_qyslice, label='Yoneda')
ax2.set_yscale('log')
# ax.plot(q_gisans_sat_plus, I_gisans_sat_plus, label='Saturation I+')
# ax.plot(q_gisans_sat_minus, I_gisans_sat_minus, label='Saturation I-')
# ax.plot(q_gisans_rem_plus, I_gisans_rem_plus, label='Remanence I+')
# ax.plot(q_gisans_rem_minus, I_gisans_rem_minus, label='Remanence I-')
# ax.plot(q_gisaxs, I_gisaxs*sf, label='GISAXS')

plt.setp(ax.get_xticklabels(), visible=False)
plt.setp(ax2.get_yticklabels(), visible=False)
# ax.legend(loc='best')
ax.set_xlim(-1.2,1.5)
ax2.set_xlim(-1.2,1.5)
ax.set_ylim(0, 2.7)
ax2.legend()
fig.savefig('Gisaxs175_28.png')
plt.show()
