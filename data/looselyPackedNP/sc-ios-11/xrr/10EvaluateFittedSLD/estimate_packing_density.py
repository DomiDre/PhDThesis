import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc
from numpy import sqrt, log, exp, cos, sin, tan, mean, std
pi, k, c, hbar, mu0 = np.pi, sc.k, sc.c, sc.hbar, sc.mu_0
muB = sc.physical_constants["Bohr magneton"][0]
mu_neutron = sc.physical_constants["neutron mag. mom."][0]
mass_neutron = sc.physical_constants["neutron mass"][0]
sldm_to_MkAm=343.5918606833081

import numpy as np
import warnings
from modelexp.data import MultiData, XyemData, XyData

def load_data(datafile):
    rawdata = np.loadtxt(datafile)
    x = rawdata[:,0]
    y = rawdata[:,1]
    return x, y

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


sld_datapath = "../SphereCSS/fit_sld.dat"

sldData = MultiData(XyData)
sldData.loadFromFile(sld_datapath)
z, sld = sldData.getDataset(0).getData()
z = np.array(z)
sld = np.array(sld)

left_idx = get_idx(z, 10)
z_left = z[left_idx]
right_idx = get_idx(z, 45)
z_right = z[right_idx-1]

z_int = z[left_idx:right_idx]
sld_int = sld[left_idx:right_idx]

mean_sld = np.trapz(sld_int, x=z_int) / (z_right - z_left)
iron_oxide_sld = 45 #1E-6
packing_density = mean_sld / iron_oxide_sld
#Plot
fig, ax = plt.subplots()
ax.plot(z, sld, marker='None', color='#92c5de')

ax.axhline(mean_sld, color='gray')
ax.text(0.99, 0.97, '$SLD_{mean} \, = \, ' + "{:.2f}".format(mean_sld) + " \, \cdot \, 10^{-6} \,\AA^{2-}$ \n"+\
                r'$\rho \, = \, ' + "{:.2f}".format(packing_density*100) + " \, \%$",
        horizontalalignment='right',
        verticalalignment='top',
        transform=ax.transAxes)
ax.fill_between(z_int, 0, sld_int, color='#92c5de', alpha=0.5)
ax.set_xlabel("$ \mathit{z} \, / \, nm$")
ax.set_ylabel("$ \mathit{SLD} \, / \, 10^{-6} \AA^{-2}$")
ax.set_xlim(min(z), max(z))
ax.set_ylim(0, 30)
fig.tight_layout()
plt.savefig("SLDintegration_PackingDensity.png")
plt.show()
#A = 27.77 # mm2
#print(A*sig_A*1e-7, "mm3")
