import VSMLangevinNP
from modelexp.data import XyeData
import numpy as np
import scipy.constants as sc
import scipy as sp

#    Ms1:  11.3264645 +/- 0.10902757 (0.96%) (init = 11.32661)
#    mu1:  25600.9638 +/- 264.306611 (1.03%) (init = 25600.65)
#    Ms2:  12.9819615 +/- 0.08829429 (0.68%) (init = 12.98191)
#    mu2:  3604.77401 +/- 64.8894282 (1.80%) (init = 3604.686)
#    chi:  3.12331096 +/- 0.04801167 (1.54%) (init = 3.123265)
#    T:    295 (fixed)

Ms_is = 11.3264645
moment = 25600.9638
chi, sigChi = 0, 1e-5 # 3.92

r = 6.13e-9
p = 2.18

def superballVolume(r, p):
  def B(x,y):
    return sp.special.gamma(x)*sp.special.gamma(y)/sp.special.gamma(x+y)
  return 2/p**2 * B(1/(2*p), (2*p+1)/(2*p)) * B(1/(2*p), (p+1)/p) * r**3

volume_particle = superballVolume(r, p)


def rescale(datafile, samplename):
  data = XyeData()
  data.loadFromFile(datafile)
  B, M, sM = data.getData()

  valid_point = sM > 0
  B = B[valid_point]
  M = M[valid_point]
  sM = sM[valid_point]

  langevinScale = VSMLangevinNP.init()
  langevinScale.set_xye(B, M, sM, datafile)
  langevinScale.subtract_diamagnetic_slope(chi, sigChi)
  langevinScale.rescale_by_moment_and_volume(Ms_is, moment, volume_particle)
  print(f'{samplename}.xye')
  langevinScale.save(f'{samplename}.xye')


samplename = 'Ol-Fe-C_powder'
rescale('../rawdata/dd144_dry_BGLinSub.xy', f'{samplename}_295K_rescaled')