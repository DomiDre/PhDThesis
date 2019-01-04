import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
import scipy as sp

Ms_is = 0.0484
moment = 23130
chi, sigChi = -0.0334, 1e-5

r = 4.65e-9
p = 2.9

def superballVolume(r, p):
  def B(x,y):
    return sp.special.gamma(x)*sp.special.gamma(y)/sp.special.gamma(x+y)
  return 2/p**2 * B(1/(2*p), (2*p+1)/(2*p)) * B(1/(2*p), (p+1)/p) * r**3

volume_particle = superballVolume(r, p)


def rescale(datafile, samplename, isTemp=False):
  ppms = PPMS()
  ppms.load(datafile)
  # ppms.remove_virgin_data(6.9)
  if isTemp:
    T, M = ppms.get_TM()
    sM = ppms.get('M. Std. Err. (emu)')
    valid_point = sM > 0
    T = T[valid_point]
    M = M[valid_point]
    sM = sM[valid_point]

    langevinScale = VSMLangevinNP.init()
    langevinScale.set_xye(T, M, sM, datafile)
    langevinScale.rescale_by_moment_and_volume(Ms_is, moment, volume_particle)
    print(f'{samplename}_LangevinSAXSscaled.xye')
    langevinScale.save(f'{samplename}_LangevinSAXSscaled.xye')

  else:
    B, M = ppms.get_BM()
    sM = ppms.get('M. Std. Err. (emu)')
    valid_point = sM > 0
    B = B[valid_point]
    M = M[valid_point]
    sM = sM[valid_point]

    langevinScale = VSMLangevinNP.init()
    langevinScale.set_xye(B, M, sM, datafile)
    langevinScale.subtract_diamagnetic_slope(chi, sigChi)
    langevinScale.rescale_by_moment_and_volume(Ms_is, moment, volume_particle)
    print(f'{samplename}_LangevinSAXSscaled.xye')
    langevinScale.save(f'{samplename}_LangevinSAXSscaled.xye')


samplename = 'ML_Ac_CoFe_C'
rescale('../data/DD205_4_KOELNPPMS_HYST_100OE_5K.DAT', f'{samplename}_5K_rescaled.dat')
rescale('../data/DD205_4_KOELNPPMS_HYST_100OE_10K.DAT', f'{samplename}_10K_rescaled.dat')
rescale('../data/DD205_4_KOELNPPMS_HYST_100OE_20K.DAT', f'{samplename}_20K_rescaled.dat')
rescale('../data/DD205_4_KOELNPPMS_HYST_100OE_50K.DAT', f'{samplename}_50K_rescaled.dat')
rescale('../data/DD205_4_KOELNPPMS_HYST_100OE_100K.DAT', f'{samplename}_100K_rescaled.dat')
rescale('../data/DD205_4_KOELNPPMS_HYST_100OE_150K.DAT', f'{samplename}_150K_rescaled.dat')
rescale('../data/DD205_4_KOELNPPMS_HYST_100OE_200K.DAT', f'{samplename}_200K_rescaled.dat')
rescale('../data/DD205_4_KOELNPPMS_HYST_100OE_250K.DAT', f'{samplename}_250K_rescaled.dat')
rescale('../data/DD205_4_KOELNPPMS_HYST_100OE_300K.DAT', f'{samplename}_300K_rescaled.dat')
rescale('../data/DD205_4_KOELNPPMS_FCW_100OE_TOUCHDOWN.DAT', f'{samplename}_fcw_rescaled.dat', True)
rescale('../data/DD205_4_KOELNPPMS_ZFCW_100OE_TOUCHDOWN.DAT', f'{samplename}_zfcw_rescaled.dat', True)