import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc
from numpy import sqrt, log, exp, cos, sin, tan, mean, std
pi, k, c, hbar, mu0 = np.pi, sc.k, sc.c, sc.hbar, sc.mu_0
muB = sc.physical_constants["Bohr magneton"][0]
mu_neutron = sc.physical_constants["neutron mag. mom."][0]
mass_neutron = sc.physical_constants["neutron mass"][0]
sldm_to_MkAm=343.5918606833081


def load_sld(datafile):
    rawdata = np.loadtxt(datafile)
    x = rawdata[:,0]
    y = rawdata[:,1]
    sy = rawdata[:,2]
    return x, y, sy
    

def load_sldmag(datafile):
    rawdata = np.loadtxt(datafile)
    x = rawdata[:,0]
    y = rawdata[:,1]
    ymag = rawdata[:,2]
    symag = rawdata[:,3]
    return x, y, ymag, symag
    
def get_idx(array, value):
    idx_sorted = np.argsort(array)
    sorted_array = np.array(array[idx_sorted])
    idx = np.searchsorted(sorted_array, value, side="left")
    if idx >= len(array):
        idx_nearest = idx_sorted[len(array)-1]
        return idx_nearest
    elif idx == 0:
        idx_nearest = idx_sorted[0]
        return idx_nearest
    else:
        if abs(value - sorted_array[idx-1]) < abs(value - sorted_array[idx]):
            idx_nearest = idx_sorted[idx-1]
            return idx_nearest
        else:
            idx_nearest = idx_sorted[idx]
        return idx_nearest

sld_datapath = "./SMI_ESS14_result_sld.dat"
z, sld, slderr = load_sld(sld_datapath)

sldmag_datapath = "./SMMI_ESS14_result_sld_410.dat"
hz, hsld, sldmag, sldmagerr = load_sldmag(sldmag_datapath)

left_idx = get_idx(z, 1)
z_left = z[left_idx]
right_idx = get_idx(z, 52)
z_right = z[right_idx-1]

z_int = z[left_idx:right_idx]
sld_int = sld[left_idx:right_idx]
sldmag_int = sldmag[left_idx:right_idx]

mean_sld = np.trapz(sld_int, x=z_int) / (z_right - z_left)
mean_sldmag = np.trapz(sldmag_int, x=z_int) / (z_right - z_left)
iron_oxide_sld = 6.975 #1E-6
packing_density = mean_sld / iron_oxide_sld

particle_sldmag = mean_sldmag/packing_density
#Plot
fig, ax = plt.subplots()
ax.errorbar(z, sld, slderr, marker='None', color='#92c5de')
ax.errorbar(z, sldmag, sldmagerr, marker='None', color='#f4a582')

ax.axhline(mean_sld, color='#0571b0')
ax.axhline(mean_sldmag, color='#ca0020')
ax.text(0.99, 0.97, r'$\overline{SLD}_n \, = \, ' + "{:.2f}".format(mean_sld) + " \, \cdot \, 10^{-6} \,\AA^{2-}$ \n"+\
                r'$\rho \, = \, ' + "{:.2f}".format(packing_density*100) + " \, \%$ \n"+\
                r'$\overline{SLD}_m \, = \, ' + "{:.2f}".format(mean_sldmag) + " \, \cdot \, 10^{-6} \,\AA^{2-}$ \n"+\
                r'$SLD_m^{particle} \, = \, ' + "{:.2f}".format(particle_sldmag) + " \, \cdot \, 10^{-6} \,\AA^{2-}$",
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)
ax.fill_between(z_int, 0, sld_int, color='#92c5de', alpha=0.5)
ax.fill_between(z_int, 0, sldmag_int, color='#f4a582', alpha=0.5)
ax.set_xlabel("$ \mathit{z} \, / \, nm$")
ax.set_ylabel("$ \mathit{SLD} \, / \, 10^{-6} \AA^{-2}$")
ax.set_xlim(min(z), max(z))
ax.set_ylim(0, 4.9)
fig.tight_layout()
plt.savefig("MagSLDIntegration_ESS14_300K.png")
plt.show()
#A = 27.77 # mm2
#print(A*sig_A*1e-7, "mm3") 
