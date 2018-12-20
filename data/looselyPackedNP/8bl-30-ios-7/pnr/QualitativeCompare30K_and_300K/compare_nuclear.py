import ReflectivityMethods
import domimethods
import numpy as np
import matplotlib.pyplot as plt
import lmfit
import sys
import os
import datetime

pi = np.pi
inf = np.inf
path_to_file = os.path.realpath(__file__)

data_path_300K = "./ES_S16_300K_4mT_Virgin_tranformed_angs_masked_qz_I_corrected_combined.xy"
data_path_30K = "./ES_S16_30K_ZFC_7Oe_Virgin_tranformed_angs_masked_qz_I_corrected_combined.xy"

exp_points_color_30K = '#dfc27d'
exp_points_color_300K = 'gray'#80cdc1'
       
qmin = 0
qmax = np.inf

def load_data(datapath):
    exp_data = np.genfromtxt(datapath)
    qz = exp_data[:, 0] # in A-1
    I_exp = exp_data[:, 1]
    sI_exp = exp_data[:, 2] 
    return qz, I_exp, sI_exp
    
def plotplots():
        # R Plot
        fig = plt.figure(figsize=(10/2.54, 7/2.54))
        x0, y0= 0.17, 0.18
        axR = fig.add_axes([x0,y0,1-x0-0.01, 1-y0-0.01])
        qz_30K, I_30K, sI_30K = load_data(data_path_30K)

        qz_300K, I_300K, sI_300K = load_data(data_path_300K)
        
        sf30 = 1
        sf300 = 1

        axR.errorbar(qz_300K, I_300K*sf300, sI_300K*sf300,\
                    marker='o', color=exp_points_color_300K,\
                    label="NR @ 300 K", markersize=2, capsize=2,\
                    elinewidth=1, ls="-")
        axR.errorbar(qz_30K, I_30K*sf30, sI_30K*sf30, marker='o',\
                        color=exp_points_color_30K, label="NR @ 30 K",\
                        markersize=2, capsize=2, elinewidth=1, ls="-")
        axR.set_xlabel("$\mathit{q_z} \, / \, \AA^{-1}$")
        axR.set_ylabel("$\mathit{I} \, / \, a.u.$")
        axR.set_xlim([min(qz_30K), 0.105])
        axR.set_ylim([5e-6, 50])
        axR.legend(loc='lower left', fontsize=11)
#        axR.legend(bbox_to_anchor=(0., 0.45, 1., .102))#loc='best')
        axR.set_yscale('log')
        
        
        plt.savefig("./ESS15_nuclear_compare_T.png")
        plt.show()
        
        
if __name__ == "__main__":
        plotplots()
