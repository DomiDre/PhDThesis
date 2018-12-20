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

data_path_30K_FC_p = "./ES_S16_30K_FC_7300Oe_tranformed_angs_uu_masked_qz_I_corrected.xy"
data_path_30K_FC_m = "./ES_S16_30K_FC_7300Oe_tranformed_angs_du_masked_qz_I_corrected.xy"
data_path_30K_ZFC_p = "./ES_S16_30K_ZFC_7300Oe_tranformed_angs_uu_masked_qz_I_corrected.xy"
data_path_30K_ZFC_m = "./ES_S16_30K_ZFC_7300Oe_tranformed_angs_du_masked_qz_I_corrected.xy"

exp_points_color_30K_FC_p = '#0571b0'
exp_points_color_30K_FC_m = "#ca0020"
exp_points_color_30K_ZFC_p = '#92c5de'
exp_points_color_30K_ZFC_m = "#f4a582"

data_path_30K_FC_p_rem = "./ES_S16_30K_FC_7Oe_Remanence_tranformed_angs_uu_masked_qz_I_corrected.xy"
data_path_30K_FC_m_rem = "./ES_S16_30K_FC_7Oe_Remanence_tranformed_angs_du_masked_qz_I_corrected.xy"
data_path_30K_ZFC_p_rem = "./ES_S16_30K_ZFC_7Oe_Remanence_tranformed_angs_uu_masked_qz_I_corrected.xy"
data_path_30K_ZFC_m_rem = "./ES_S16_30K_ZFC_7Oe_Remanence_tranformed_angs_du_masked_qz_I_corrected.xy"

exp_points_color_30K_FC_p_rem = '#7b3294'
exp_points_color_30K_FC_m_rem = "#008837"
exp_points_color_30K_ZFC_p_rem = '#c2a5cf'
exp_points_color_30K_ZFC_m_rem = "#a6dba0"
       
qmin = 0
qmax = np.inf

def load_data(datapath):
    exp_data = np.genfromtxt(datapath)
    qz = exp_data[:, 0] # in A-1
    I_exp = exp_data[:, 1]
    sI_exp = exp_data[:, 2]
    
    valid = sI_exp/I_exp < 0.5
    qz = qz[valid]
    I_exp = I_exp[valid]
    sI_exp = sI_exp[valid]

    valid = I_exp > 1e-8
    qz = qz[valid]
    I_exp = I_exp[valid]
    sI_exp = sI_exp[valid]
    
    return qz, I_exp, sI_exp
    
def plotplots():
        # R Plot
        fig = plt.figure(figsize=(8/2.54, 8/2.54))
        x0, y0 = 0.21, 0.16
        axR = fig.add_axes([x0,y0, 1-x0-0.01, 1-y0-0.01])
        qz_30K_FC_p, I_30K_FC_p, sI_30K_FC_p = load_data(data_path_30K_FC_p)
        qz_30K_FC_m, I_30K_FC_m, sI_30K_FC_m = load_data(data_path_30K_FC_m)
        qz_30K_ZFC_p, I_30K_ZFC_p, sI_30K_ZFC_p = load_data(data_path_30K_ZFC_p)
        qz_30K_ZFC_m, I_30K_ZFC_m, sI_30K_ZFC_m = load_data(data_path_30K_ZFC_m)
        
        qz_30K_FC_p_rem, I_30K_FC_p_rem, sI_30K_FC_p_rem = load_data(data_path_30K_FC_p_rem)
        qz_30K_FC_m_rem, I_30K_FC_m_rem, sI_30K_FC_m_rem = load_data(data_path_30K_FC_m_rem)
        qz_30K_ZFC_p_rem, I_30K_ZFC_p_rem, sI_30K_ZFC_p_rem = load_data(data_path_30K_ZFC_p_rem)
        qz_30K_ZFC_m_rem, I_30K_ZFC_m_rem, sI_30K_ZFC_m_rem = load_data(data_path_30K_ZFC_m_rem)
        
        sf30_FC = 400
        sf30_ZFC = 1
        sf30_FC_rem = 1e-3
        sf30_ZFC_rem = 1e-6
        x0 = 0.045
        fontsize=10
        axR.errorbar(qz_30K_FC_p, I_30K_FC_p*sf30_FC, sI_30K_FC_p*sf30_FC,\
                    marker='o', linestyle='-',\
                    color=exp_points_color_30K_FC_p,\
                    markersize=2, capsize=2,\
                    elinewidth=1)
#                    label="I+, FC @ 30 K, 730 mT",\
        axR.errorbar(qz_30K_FC_m, I_30K_FC_m*sf30_FC, sI_30K_FC_m*sf30_FC,\
                    marker='o', linestyle='-',\
                    color=exp_points_color_30K_FC_m,\
                    markersize=2, capsize=2, elinewidth=1)
#                    label="I-, FC @ 30 K, 730 mT",\
        axR.text(x0, 1, "FC @ 7.3 kOe", fontsize=fontsize)
        axR.errorbar(qz_30K_ZFC_p, I_30K_ZFC_p*sf30_ZFC, sI_30K_ZFC_p*sf30_ZFC,\
                    marker='o', linestyle='-',\
                    color=exp_points_color_30K_ZFC_p,\
                    markersize=2, capsize=2,\
                    elinewidth=1)
#                    label="I+, ZFC @ 30 K, 730 mT",\
        axR.errorbar(qz_30K_ZFC_m, I_30K_ZFC_m*sf30_ZFC, sI_30K_ZFC_m*sf30_ZFC,\
                    marker='o', linestyle='-',\
                    color=exp_points_color_30K_ZFC_m,\
                    markersize=2, capsize=2, elinewidth=1)
#                    label="I-, ZFC @ 30 K, 730 mT",\
        axR.text(x0, 2e-3, "ZFC @ 7.3 kOe", fontsize=fontsize)
        
        #remanence
        axR.errorbar(qz_30K_FC_p_rem, I_30K_FC_p_rem*sf30_FC_rem, sI_30K_FC_p_rem*sf30_FC_rem,\
                    marker='o', linestyle='-',\
                    color=exp_points_color_30K_FC_p_rem,\
                    markersize=2, capsize=2,\
                    elinewidth=1)
#                    label="I+, FC @ 30 K, Remanence",\
        axR.errorbar(qz_30K_FC_m_rem, I_30K_FC_m_rem*sf30_FC_rem, sI_30K_FC_m_rem*sf30_FC_rem,\
                    marker='o', linestyle='-',\
                    color=exp_points_color_30K_FC_m_rem,\
                    markersize=2, capsize=2, elinewidth=1)
#                    label="I-, FC @ 30 K, Remanence",\
        axR.text(x0, 2e-6, "FC @ Remanence", fontsize=fontsize)
                    
        axR.errorbar(qz_30K_ZFC_p_rem, I_30K_ZFC_p_rem*sf30_ZFC_rem, sI_30K_ZFC_p_rem*sf30_ZFC_rem,\
                    marker='o', linestyle='-',\
                    color=exp_points_color_30K_ZFC_p_rem,\
                    markersize=2, capsize=2,\
                    elinewidth=1)
#                    label="I+, ZFC @ 30 K, Remanence",\
        axR.errorbar(qz_30K_ZFC_m_rem, I_30K_ZFC_m_rem*sf30_ZFC_rem, sI_30K_ZFC_m_rem*sf30_ZFC_rem,\
                    marker='o', linestyle='-',\
                    color=exp_points_color_30K_ZFC_m_rem,\
                    markersize=2, capsize=2, elinewidth=1)
#                    label="I-, ZFC @ 30 K, Remanence",\
        axR.text(x0, 2e-9, "ZFC @ Remanence", fontsize=fontsize)
#        axR.legend(loc='upper right')
        axR.set_xlabel("$\mathit{q_z} \, / \, \AA^{-1}$")
        axR.set_ylabel("$\mathit{I} \, / \, a.u.$")
        axR.set_xlim([min(qz_30K_FC_p), 0.105])
        axR.set_ylim([3.5e-12, 500])
        axR.set_yscale('log')
        axR.set_yticks([1e-9, 1e-7, 1e-5, 1e-1, 1e-3, 1e-1, 1e1])
        
        plt.savefig("./ESS16_magnetic_compare.png")
        plt.show()
        
        
if __name__ == "__main__":
        plotplots()
