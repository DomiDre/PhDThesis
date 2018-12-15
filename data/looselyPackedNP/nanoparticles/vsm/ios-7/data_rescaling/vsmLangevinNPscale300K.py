import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
datafile = '../rawdata/KWI338_HYST_300K.DAT'
samplename = 'KWi338'
muB = sc.physical_constants['Bohr magneton'][0]

mu = 3649.95665
r1 = 35.4e-10
r2 = 6.8e-10
volSphere = lambda R:4/3 * np.pi * R**3
# vol_particle = (1-0.78)*volSphere(r1) + 0.78*volSphere(r2)
vol_particle = volSphere(r1)
Ms_is = 3.30000000

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
langevinScale.subtract_diamagnetic_slope(-0.305*20/40, 0.00149)
langevinScale.rescale_by_moment_and_volume(Ms_is, mu, vol_particle)
langevinScale.save(f'{samplename}_300K_LangevinSAXSscaled.xye')