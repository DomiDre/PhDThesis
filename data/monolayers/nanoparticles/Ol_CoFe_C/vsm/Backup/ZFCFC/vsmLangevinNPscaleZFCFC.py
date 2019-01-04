import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np

samplename = 'DD67'
rescale_factor = 0.05727350591745316

def rescale_file(datafile, outfile):
  ppms = PPMS()
  ppms.load(datafile)
  T, M = ppms.get_TM()
  sM = ppms.get('M. Std. Err. (emu)')
  valid_point = sM > 0
  T = T[valid_point]
  M = M[valid_point]
  sM = sM[valid_point]
  M*=1000
  sM*=1000

  langevinScale = VSMLangevinNP.init(T_dependent=True)
  langevinScale.set_xye(T, M, sM, datafile)
  langevinScale.rescale_with_factor(rescale_factor)
  langevinScale.save(outfile)

rescale_file('./DD172_6_ZFCw_100OE.DAT', f'{samplename}_ZFC_LangevinSAXSscaled.xye')
rescale_file('./DD172_6_FCW_100OE.DAT', f'{samplename}_FCw_LangevinSAXSscaled.xye')