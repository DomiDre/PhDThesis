import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
samplename = 'SC-IOS-11'
muB = sc.physical_constants['Bohr magneton'][0]

mu = 13767.9255
radius = 54.1e-10
vol_particle = 4/3 * np.pi * radius**3

Ms_is = 0.15822643


datafile = '../rawdata/ES_S14_HYST_30K_FC.DAT'
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
langevinScale.subtract_diamagnetic_slope(-0.04880897, 2.8241e-05)
langevinScale.rescale_by_moment_and_volume(Ms_is, mu, vol_particle)
langevinScale.save(f'{samplename}_30K_FC_LangevinSAXSscaled.xye')

datafile = '../rawdata/ES_S14_HYST_30K_ZFC.DAT'
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
langevinScale.subtract_diamagnetic_slope(-0.04880897, 2.8241e-05)
langevinScale.rescale_by_moment_and_volume(Ms_is, mu, vol_particle)
langevinScale.save(f'{samplename}_30K_ZFC_LangevinSAXSscaled.xye')