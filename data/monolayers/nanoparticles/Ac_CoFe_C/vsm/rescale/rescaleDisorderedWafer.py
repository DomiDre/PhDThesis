import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
import scipy as sp
#    Ms:            0.043 (fixed)
#    mu:            23130.23 (fixed)
#    chi:          -0.0356 (fixed)

moment = 23130
Ms_is = 0.043
chi, sigChi = -0.0369, 1e-5

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

samplename = 'Ac_CoFe_C_DisorderedWafer'
rescale('../data_disorderedWafer/DD226_2_HYST_300K_REPEAT.DAT', f'{samplename}_300K')
rescale('../data_disorderedWafer/DD226_2_HYST_10K_REPEAT_3.DAT',  f'{samplename}_10K')
rescale('../data_disorderedWafer/DD226_2_FCW_100OE.DAT',       f'{samplename}_FCw', True)
rescale('../data_disorderedWafer/DD226_2_ZFCW_100OE.DAT',f'{samplename}_ZFCw', True)