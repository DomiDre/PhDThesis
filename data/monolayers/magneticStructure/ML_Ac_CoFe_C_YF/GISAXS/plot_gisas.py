import numpy as np
import matplotlib.pyplot as plt
from GALAXI.dd_gisaxs.dd_gisaxs import DDGISAXS
import matplotlib.colors as mcolors
import matplotlib.patheffects as PathEffects
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib
matplotlib.rcParams.update({'font.size': 18})

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


x0, y0 = 0.13, 0.15
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
# fig = plt.figure(figsize=(5,4))
# x0, y0 = 0.17, 0.17
# width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure(figsize=(4.5,4.5))

ax = fig.add_axes([x0, 0.42, width, 0.57])
ax2 = fig.add_axes([x0, y0, width, 0.25])

pcm = ax.pcolormesh(qy, qz, data.T,\
                    norm=mcolors.LogNorm(),\
                    cmap=obj.cmap, vmin = 1e-8, vmax=15e-6)
ax.axhline(q_min, color='white', marker='None', alpha=0.5)
ax.axhline(q_max, color='white', marker='None', alpha=0.5)
# divider3 = make_axes_locatable(ax)
# cax = divider3.append_axes('right', size="2.5%", pad=0.1)
# cbar = fig.colorbar(pcm, cax=cax, orientation='vertical')
ax.set_xticks([])
ax2.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')

txt = ax.text(0.95, 0.95,\
        "GISAXS @ GALAXI",\
        color='white',\
        horizontalalignment='right',
        verticalalignment='top',\
        transform=ax.transAxes, fontsize=18)
txt.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='black')])

plot_q_square_lines(0.484, ax2)
data_left = qyslice<-0.06
data_right = qyslice>0.06
ax2.errorbar(qyslice[data_left], I_qyslice[data_left], sI_qyslice[data_left], label='Yoneda', color='#ca0020')
ax2.errorbar(qyslice[data_right], I_qyslice[data_right], sI_qyslice[data_right], color='#ca0020')
ax2.set_yscale('log')
# ax.plot(q_gisans_sat_plus, I_gisans_sat_plus, label='Saturation I+')
# ax.plot(q_gisans_sat_minus, I_gisans_sat_minus, label='Saturation I-')
# ax.plot(q_gisans_rem_plus, I_gisans_rem_plus, label='Remanence I+')
# ax.plot(q_gisans_rem_minus, I_gisans_rem_minus, label='Remanence I-')
# ax.plot(q_gisaxs, I_gisaxs*sf, label='GISAXS')
ax2.get_yaxis().set_visible(False)
plt.setp(ax.get_xticklabels(), visible=False)
# plt.setp(ax2.get_yticklabels(), visible=False)
# ax.legend(loc='best')
ax.set_xlim(-1.2,1.5)
ax2.set_xlim(-1.2,1.5)
ax.set_ylim(0.1, 2.8)
ax2.set_ylim([2e-8, 2e-4])
ax2.legend()
fig.savefig('Gisaxs175_28.png')
# plt.show()
