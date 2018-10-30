from GISANS.gisansd33 import GisansD33
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.ndimage.interpolation import rotate
from numpy import sqrt

sdd = 5000
qzmin,qzmax = 0.007, 0.016

global log
log = '#Evaluating DD175_28 GISANS at Saturation and Remanence\n'

#                               ######
#        ####    ##   #####     #     #   ##   #####   ##
#       #    #  #  #  #    #    #     #  #  #    #    #  #
#       #    # #    # #    #    #     # #    #   #   #    #
#       #    # ###### #    #    #     # ######   #   ######
#       #    # #    # #    #    #     # #    #   #   #    #
#######  ####  #    # #####     ######  #    #   #   #    #
def add_log(entry):
    global log
    log += entry

d33_data = GisansD33()
add_log('#Sample Detector-Distance: '+str(sdd)+'\n')
add_log('#Wavelength: '+str(d33_data.wavelength)+'\n')
add_log('#Pixelsize X: '+str(d33_data.pixelsize_x)+'\n')
add_log('#Pixelsize Y: '+str(d33_data.pixelsize_y)+'\n')
add_log('#Summing data in range qz = ' + str(qzmin)+' .. '  + str(qzmax) + '\n')

def load_files(path_prefix, filenum_list):
    add_log('#Loading files ' + path_prefix + " " + str(filenum_list) +'\n')
    d33_data = GisansD33()
    d33_data.sdd = sdd
    d33_data.load_file_range(path_prefix, filenum_list)
    qy, qz, data = d33_data.get_qyz_data()
    monitor = d33_data.get_monitor()
    qzrange = np.logical_and(qzmin<qz, qz<qzmax)
    data_projection = np.sum(data[:,qzrange], axis=1)
    return qy, qz, data_projection, monitor

qy_sat_plus, qz_sat_plus, data_projection_sat_plus, monitor_sat_plus =\
    load_files('./0rawdata/0206', np.arange(73, 85, 2))
qy_sat_minus, qz_sat_minus, data_projection_sat_minus, monitor_sat_minus =\
    load_files('./0rawdata/0206', np.arange(74, 85, 2))
qy_rem_plus, qz_rem_plus, data_projection_rem_plus, monitor_rem_plus =\
    load_files('./0rawdata/0206', np.arange(85, 97, 2))
qy_rem_minus, qz_rem_minus, data_projection_rem_minus, monitor_rem_minus =\
    load_files('./0rawdata/0206', np.arange(86, 97, 2))

I_sat = (data_projection_sat_plus/ monitor_sat_plus +\
            data_projection_sat_minus/ monitor_sat_minus)/2
sI_sat = np.sqrt(data_projection_sat_plus/ monitor_sat_plus**2 +\
                    data_projection_sat_minus/ monitor_sat_minus**2)/2

I_rem = (data_projection_rem_plus/ monitor_rem_plus +\
            data_projection_rem_minus/ monitor_rem_minus)/2
sI_rem = np.sqrt(data_projection_rem_plus/ monitor_rem_plus**2 +\
                    data_projection_rem_minus/ monitor_rem_minus**2)/2

Idiff = I_rem-I_sat
sIdiff = np.sqrt(sI_sat**2 + sI_rem**2)

 #####                       ######
#     #   ##   #    # ###### #     #   ##   #####   ##
#        #  #  #    # #      #     #  #  #    #    #  #
 #####  #    # #    # #####  #     # #    #   #   #    #
      # ###### #    # #      #     # ######   #   ######
#     # #    #  #  #  #      #     # #    #   #   #    #
 #####  #    #   ##   ###### ######  #    #   #   #    #

with open('DD175_28_SatRem_Diff.xye', 'w') as datafile:
    datafile.write(log)
    datafile.write('#qy/A-1\tIsat/a.u.\tsIsat/a.u.\t'+\
                          'tIrem/a.u.\tsIrem/a.u.\t'+\
                          'tIdiff/a.u.\tsIdiff/a.u.\n')
    for i, qval in enumerate(qy_sat_plus):
        datafile.write(str(qval) + "\t" +\
                       str(I_sat[i]) + "\t" +\
                       str(sI_sat[i]) + "\t" +\
                       str(I_rem[i]) + "\t" +\
                       str(sI_rem[i]) + "\t" +\
                       str(Idiff[i]) + "\t" +\
                       str(sIdiff[i])+ "\n")
    datafile.close()

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

ax_yoneda.errorbar(qy_sat_plus, I_sat, sI_sat, label='Saturation', elinewidth=1, capsize=1, linewidth=1)
ax_yoneda.errorbar(qy_sat_plus, I_rem, sI_rem, label='Remanence', elinewidth=1, capsize=1, linewidth=1)
ax_yoneda.legend(loc='upper right')
ax_yoneda.set_yscale('log')
ax_yoneda.set_ylabel("$ \mathit{I} \, / \, a.u.$")
ax_yoneda.set_xlim(0,0.068)
ax_yoneda.set_ylim(5e-3, 2e-1)

ax_diff.axhline(0, color='#AAAAAA')
ax_diff.errorbar(qy_sat_plus, Idiff, sIdiff, elinewidth=1, capsize=1, linewidth=1)
ax_diff.set_xlabel("$ \mathit{q_y} \, / \, \AA^{-1}$")
ax_diff.set_xlim(0.01,0.068)
ax_diff.set_ylim(-0.013, 0.013)
ax_diff.set_ylabel("$ \mathit{I_{rem}} - \mathit{I_{sat}} \, / \, a.u.$")
fig.tight_layout()
fig.savefig('DD175_28_GISANS_Saturation_Remanence_Difference.png')
plt.show()
