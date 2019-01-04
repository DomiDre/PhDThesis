import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import scipy.constants as sc
import scipy as sp

muB = sc.physical_constants['Bohr magneton'][0]

r = 4.28959813e-6 # mm
a = 2*r
layer_packing = (a/(a+0e-6))**2

m_wafer = 28.98 #mg
chi_Si = -0.00111 # memu/T / mg
rho_Si = 2.33 # mg / mm3

chi, sigChi = m_wafer*chi_Si, 1e-5#-0.0435, 2.8208e-05 #chi_Si*m_wafer, 0.00001*m_wafer

area_wafer = m_wafer/rho_Si/0.525 # mm2

volume = 2*r*area_wafer*layer_packing

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
  langevinScale.rescale_with_factor(1/volume)
  print(f'{samplename}_LangevinSAXSscaled.xye')
  langevinScale.save(f'{samplename}_LangevinSAXSscaled.xye')


rescale('../data/DD175_23_HYST_300K.DAT', 'ML-Ac-CoFe-C-2star_300K')
rescale('../data/DD175_23_HYST_5K_100OE.DAT', 'ML-Ac-CoFe-C-2star_5K')