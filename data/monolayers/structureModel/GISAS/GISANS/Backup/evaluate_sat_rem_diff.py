from GISANS.gisansd33 import GisansD33
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.ndimage.interpolation import rotate
from numpy import sqrt

sdd = 5000 # m
qzmin,qzmax = 0.007, 0.023

def load_files(path_prefix, filenum_list):
    d33_data = GisansD33()
    d33_data.sdd = sdd
    d33_data.load_file_range(path_prefix, filenum_list)
    qy, qz, data = d33_data.get_qyz_data()
    monitor = d33_data.get_monitor()
    qzrange = np.logical_and(qzmin<qz, qz<qzmax)
    data_projection = np.sum(data[:,qzrange], axis=1)
    return qy, qz, data_projection, monitor
#                               ######
#        ####    ##   #####     #     #   ##   #####   ##
#       #    #  #  #  #    #    #     #  #  #    #    #  #
#       #    # #    # #    #    #     # #    #   #   #    #
#       #    # ###### #    #    #     # ######   #   ######
#       #    # #    # #    #    #     # #    #   #   #    #
#######  ####  #    # #####     ######  #    #   #   #    #
qy_sat_plus, qz_sat_plus, data_projection_sat_plus, monitor_sat_plus =\
    load_files('./0rawdata/0206', np.arange(73, 85, 2))
qy_sat_minus, qz_sat_minus, data_projection_sat_minus, monitor_sat_minus =\
    load_files('./0rawdata/0206', np.arange(74, 85, 2))
qy_rem_plus, qz_rem_plus, data_projection_rem_plus, monitor_rem_plus =\
    load_files('./0rawdata/0206', np.arange(85, 97, 2))
qy_rem_minus, qz_rem_minus, data_projection_rem_minus, monitor_rem_minus =\
    load_files('./0rawdata/0206', np.arange(86, 97, 2))

Isum_sat = (data_projection_sat_plus/ monitor_sat_plus +\
            data_projection_sat_minus/ monitor_sat_minus)/2
sIsum_sat = np.sqrt(data_projection_sat_plus/ monitor_sat_plus**2 +\
                    data_projection_sat_minus/ monitor_sat_minus**2)/2

Isum_rem = (data_projection_rem_plus/ monitor_rem_plus +\
            data_projection_rem_minus/ monitor_rem_minus)/2
sIsum_rem = np.sqrt(data_projection_rem_plus/ monitor_rem_plus**2 +\
                    data_projection_rem_minus/ monitor_rem_minus**2)/2

 #####                       ######
#     #   ##   #    # ###### #     #   ##   #####   ##
#        #  #  #    # #      #     #  #  #    #    #  #
 #####  #    # #    # #####  #     # #    #   #   #    #
      # ###### #    # #      #     # ######   #   ######
#     # #    #  #  #  #      #     # #    #   #   #    #
 #####  #    #   ##   ###### ######  #    #   #   #    #


######                         ######
#     # #       ####  #####    #     #   ##   #####   ##
#     # #      #    #   #      #     #  #  #    #    #  #
######  #      #    #   #      #     # #    #   #   #    #
#       #      #    #   #      #     # ######   #   ######
#       #      #    #   #      #     # #    #   #   #    #
#       ######  ####    #      ######  #    #   #   #    #

fig = plt.figure(figsize=(4,4))
ax_yoneda = fig.add_subplot(211)
ax_diff = fig.add_subplot(212, sharex=ax_yoneda)


ax_yoneda.errorbar(qy_sat_plus, Isum_sat, sIsum_sat, label='Saturation')
ax_yoneda.errorbar(qy_sat_plus, Isum_rem, sIsum_rem, label='Remanence')
ax_yoneda.legend(loc='upper right')
ax_yoneda.set_yscale('log')
ax_yoneda.set_ylabel("$ \mathit{I} \, / \, a.u.$")
ax_yoneda.set_xlim(0,0.068)
ax_yoneda.set_ylim(1e-2, 2e-1)

ax_diff.axhline(0, color='#AAAAAA')
ax_diff.errorbar(qy_sat_plus, Isum_rem-Isum_sat, np.sqrt(sIsum_sat**2 + sIsum_rem**2))
ax_diff.set_xlabel("$ \mathit{q_y} \, / \, \AA^{-1}$")
ax_diff.set_xlim(0,0.068)
ax_diff.set_ylim(-1e-2, 1e-2)
ax_diff.set_ylabel("$ \mathit{I_{rem}} - \mathit{I_{sat}} \, / \, a.u.$")
fig.tight_layout()
fig.savefig('DifferenceDD175_28_Projection.png')
plt.show()
