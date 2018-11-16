import VSMLangevinNP
from PPMS.ppms import PPMS
from modelexp.data import XyeData
import numpy as np

samplename = 'YF45'
rescale_factor = 1.381881364777391

def rescale_file_T(datafile, outfile):
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

def rescale_file_M(datafile, outfile):
  # ppms = PPMS()
  # ppms.load(datafile)
  # B, M = ppms.get_BM()
  # sM = ppms.get('M. Std. Err. (emu)')

  dataRef = XyeData()
  dataRef.loadFromFile(datafile)
  B, M, sM = dataRef.getData()
  valid_point = sM > 0
  B = B[valid_point]
  M = M[valid_point]
  sM = sM[valid_point]
  # M*=1000
  # sM*=1000

  langevinScale = VSMLangevinNP.init()
  langevinScale.set_xye(B, M, sM, datafile)
  langevinScale.rescale_with_factor(rescale_factor)
  langevinScale.save(outfile)

# rescale_file_T('../rawdata/DD226_2_ZFCW_100OE.DAT', f'{samplename}_ZFC_LangevinSAXSscaled.xye')
# rescale_file_T('../rawdata/DD226_2_FCW_100OE.DAT', f'{samplename}_FCw_LangevinSAXSscaled.xye')
# rescale_file_M('../rawdata/DD226_2_HYST_350K_REPEAT.DAT', f'{samplename}_350K_LangevinSAXSscaled.xye')
rescale_file_M('../rawdata/YF045_final_rescaled.xy', f'{samplename}_300K_LangevinSAXSscaled.xye')
