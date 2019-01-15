import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
import scipy as sp

#    Ms1:  2.98609399 +/- 0.00852753 (0.29%) (init = 2.986063)
#    mu1:  4142.20715 +/- 12.5110911 (0.30%) (init = 4142.248)
#    Ms2:  0.54964413 +/- 0.00712285 (1.30%) (init = 0.5496544)
#    mu2:  532.719512 +/- 15.4901888 (2.91%) (init = 532.7795)
#    chi:  0.00513778 +/- 6.4718e-04 (12.60%) (init = 0.005139687)
#    T:    300 (fixed)

Ms_is = 2.98609399
moment = 4142.20715
r1 = 35.4e-10
r2 = 6.8e-10
volSphere = lambda R:4/3 * np.pi * R**3
# vol_particle = (1-0.78)*volSphere(r1) + 0.78*volSphere(r2)
volume_particle = volSphere(r1)

chi = -0.1934
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

samplename = 'IOS-7_Dispersion'
rescale('../rawdata/KWI338_HYST_300K.DAT', f'{samplename}_300K')
rescale('../rawdata/KWI338_HYST_10K.DAT',  f'{samplename}_10K')
rescale('../rawdata/KWI338_HYST_ZFC_30K.DAT',  f'{samplename}_ZFC_30K')
rescale('../rawdata/KWI338_HYST_EB_FC1T_30K.DAT',  f'{samplename}_FC_30K')

rescale('../rawdata/KWI338_FCW_100OE.DAT',       f'{samplename}_FCw', True)
rescale('../rawdata/KWI338_ZFCW_100OE.DAT',f'{samplename}_ZFCw', True)
