import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
datafile = '../rawdata/PMK18_HYST_300K.DAT'
samplename = 'PMK18'
muB = sc.physical_constants['Bohr magneton'][0]

mu = 11689.6793
radius = 54.1e-10
vol_particle = 4/3 * np.pi * radius**3

Ms_is = 9.96728549

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