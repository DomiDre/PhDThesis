import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
import scipy as sp

#    Ms:            1.99000000 +/- 0.00180995 (0.09%) (init = 2.01)
#    mu:            23130.2290 +/- 80.3760505 (0.35%) (init = 19620.35)
#    chi:          -0.01000000 +/- 0.00145568 (14.56%) (init = -0.021)

moment = 23130

r = 4.65e-9
p = 2.9

def superballVolume(r, p):
  def B(x,y):
    return sp.special.gamma(x)*sp.special.gamma(y)/sp.special.gamma(x+y)
  return 2/p**2 * B(1/(2*p), (2*p+1)/(2*p)) * B(1/(2*p), (p+1)/p) * r**3

volume_particle = superballVolume(r, p)

def rescale(datafile, samplename, isTemp=False, Ms_is = None, chi=None, sigChi=None):
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
    if chi is not None:
      langevinScale.subtract_diamagnetic_slope(chi, sigChi)
    langevinScale.rescale_by_moment_and_volume(Ms_is, moment, volume_particle)
    print(f'{samplename}_LangevinSAXSscaled.xye')
    langevinScale.save(f'{samplename}_LangevinSAXSscaled.xye')

samplename = 'Ac_CoFe_C_Dispersion'
rescale('../data_dispersion/AH11_HYST_100OE_300K.DAT', f'{samplename}_300K', Ms_is = 1.99, chi=-0.01, sigChi=0.00145568)
rescale('../data_dispersion/AH11_HYST_100OE_10K.DAT',  f'{samplename}_10K', Ms_is = 4.6, chi=-0.01, sigChi=0.00145568)#3.88 0.15
rescale('../data_dispersion/AH11_FCC_100OE.DAT',       f'{samplename}_FCc', True, Ms_is = 6.28)
rescale('../data_dispersion/AH11_ZFCW_100OE_00001.dat',f'{samplename}_ZFCw', True, Ms_is = 6.28)
