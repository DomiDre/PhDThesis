import VSMLangevinNP
from modelexp.data import XyeData
import numpy as np
import scipy.constants as sc
import scipy as sp

Ms_is = 8.8
moment = 61600
chi, sigChi = 0, 1e-5 # 3.92

r = 6.0775e-9
p = 1.8324

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
rescale('../rawdata/dd147_stabledry_2_BGLinSub.xy', f'{samplename}_296K_rescaled')