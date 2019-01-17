import VSMLangevinNP
from modelexp.data import XyeData
import numpy as np
import scipy.constants as sc
import scipy as sp

#    Ms1:  4.20693475 +/- 0.07846342 (1.87%) (init = 4.2)
#    mu1:  101042.002 +/- 2398.39989 (2.37%) (init = 101000)
#    Ms2:  4.78488402 +/- 0.07394440 (1.55%) (init = 4.78)
#    mu2:  15332.0886 +/- 287.239180 (1.87%) (init = 15300.85)
#    chi:  0.45157070 +/- 0.01511891 (3.35%) (init = 0.4515731)
#    T:    295 (fixed)

#    Ms1:  4.20000000 +/- 0.07846356 (1.87%) (init = 5.13)
#    mu1:  101000.000 +/- 2398.56227 (2.37%) (init = 81800)
#    Ms2:  4.78000000 +/- 0.07394376 (1.55%) (init = 4.36)
#    mu2:  15300.8470 +/- 287.236325 (1.88%) (init = 10400.9)
#    chi:  0.44000000 +/- 0.01511878 (3.44%) (init = 0)
#    T:    295 (fixed)
Ms_is = 4.2
moment = 101000
chi, sigChi = 0, 0 # 3.92

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


samplename = 'Ol-Fe-C_powderOxidized'
rescale('../rawdata/dd147_stabledry_2_BGLinSub.xy', f'{samplename}_295K_rescaled')