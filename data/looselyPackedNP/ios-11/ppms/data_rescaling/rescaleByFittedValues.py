import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
import scipy as sp

#    Ms:            9.30370224 +/- 0.02447303 (0.26%) (init = 9.3)
#    mu:            13699.7706 +/- 108.681553 (0.79%) (init = 13680.54)
#    chi:           0.56093618 +/- 0.01828230 (3.26%) (init = 0.56)

moment = 13931.5081
radius = 54.1e-10
volume_particle = 4/3 * np.pi * radius**3
Ms_is = 9.20437856
chi = -0.173 # d8 toluene

def rescale(datafile, samplename, isTemp=False):
  ppms = PPMS()
  ppms.load(datafile)
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
    # ppms.remove_virgin_data(6.9)
    B, M = ppms.get_BM()
    sM = ppms.get('M. Std. Err. (emu)')
    valid_point = sM > 0
    B = B[valid_point]
    M = M[valid_point]
    sM = sM[valid_point]

    langevinScale = VSMLangevinNP.init()
    langevinScale.set_xye(B, M, sM, datafile)
    if chi is not None:
      langevinScale.subtract_diamagnetic_slope(chi, 0)
    langevinScale.rescale_by_moment_and_volume(Ms_is, moment, volume_particle)
    print(f'{samplename}_LangevinSAXSscaled.xye')
    langevinScale.save(f'{samplename}_LangevinSAXSscaled.xye')

samplename = 'IOS-11_Dispersion'
rescale('../rawdata/PMK18_HYST_300K.DAT', f'{samplename}_300K')
rescale('../rawdata/PMK18_HYST_10K.DAT',  f'{samplename}_10K')
rescale('../rawdata/PMK18_HYST_ZFC_30K.DAT',  f'{samplename}_ZFC_30K')
rescale('../rawdata/PMK18_HYST_EB_FC1T_30K.DAT',  f'{samplename}_FC_30K')

rescale('../rawdata/PMK18_FCW_100OE.DAT',       f'{samplename}_FCw', True)
rescale('../rawdata/PMK18_ZFCW_100OE.DAT',f'{samplename}_ZFCw', True)
