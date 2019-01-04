import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
import scipy as sp

#    Ms:            0.05178662 +/- 1.1871e-04 (0.23%) (init = 0.05178667)
#    mu:            9582.44471 +/- 137.726975 (1.44%) (init = 9582.356)
#    chi:          -0.04180186 +/- 3.2909e-05 (0.08%) (init = -0.04180187)
moment = 9582
Ms_is = 0.05178662

r = 4.28959813e-9
p = 2.2

def superballVolume(r, p):
  def B(x,y):
    return sp.special.gamma(x)*sp.special.gamma(y)/sp.special.gamma(x+y)
  return 2/p**2 * B(1/(2*p), (2*p+1)/(2*p)) * B(1/(2*p), (p+1)/p) * r**3

volume_particle = superballVolume(r, p)

m_wafer = 28.98 #mg
chi_Si = -0.00111 # memu/T / mg
chi, sigChi = m_wafer*chi_Si, 1e-5#-0.0435, 2.8208e-05 #chi_Si*m_wafer, 0.00001*m_wafer

def rescale(datafile, samplename):
  ppms = PPMS()
  ppms.load(datafile)
  # ppms.remove_virgin_data(6.9)
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


rescale('../data/DD175_23_HYST_300K.DAT', 'ML-Ac-CoFe-C-2star_300K')
rescale('../data/DD175_23_HYST_5K_100OE.DAT', 'ML-Ac-CoFe-C-2star_5K')