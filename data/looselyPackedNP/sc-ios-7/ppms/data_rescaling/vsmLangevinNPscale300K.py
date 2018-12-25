import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
datafile = '../rawdata/ES_S17_HYST_300K.DAT'
samplename = 'SC-IOS-7'
muB = sc.physical_constants['Bohr magneton'][0]

#[[Variables]]
#    Ms:            0.12024767 +/- 1.4213e-04 (0.12%) (init = 0.12)
#    mu:            4350.85500 +/- 15.8644098 (0.36%) (init = 4320.856)
#    chi:          -0.05763115 +/- 3.9590e-05 (0.07%) (init = -0.058)
#    sigMu:         0 (fixed)
mu = 4350.855
radius = 35.2547170e-10
vol_particle = 4/3 * np.pi * radius**3

Ms_is = 0.12024767
chi = -0.05763
sig_chi = 3.9590e-5

ppms = PPMS()
ppms.load(datafile)
B, M = ppms.get_BM()
sM = ppms.get('M. Std. Err. (emu)')
valid_point = sM > 0
B = B[valid_point]
M = M[valid_point]
sM = sM[valid_point]

langevinScale = VSMLangevinNP.init()
langevinScale.set_xye(B, M, sM, datafile)
langevinScale.subtract_diamagnetic_slope(chi, sig_chi)
langevinScale.rescale_by_moment_and_volume(Ms_is, mu, vol_particle)
langevinScale.save(f'{samplename}_300K_LangevinSAXSscaled.xye')