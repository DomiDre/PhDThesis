import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
import scipy as sp

#    Ms:            4.45771958 +/- 0.05668773 (1.27%) (init = 4.45)
#    mu:            6284.34389 +/- 122.907403 (1.96%) (init = 6270.791)
#    chi:           2.84452075 +/- 0.04298546 (1.51%) (init = 2.8427)

moment = 6284

r = 5.1e-9
p = 4.1

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

samplename = 'Ol_CoFe_C_Dispersion'
rescale('../data_dispersion/DD67_HYST_300K_INIT.DAT', f'{samplename}_300K', Ms_is = 4.46, chi=0.0, sigChi=1e-5)
rescale('../data_dispersion/DD67_HYST_10K.DAT',f'{samplename}_10K', Ms_is = 14, chi=0.0, sigChi=1e-5)#3.88 0.15
