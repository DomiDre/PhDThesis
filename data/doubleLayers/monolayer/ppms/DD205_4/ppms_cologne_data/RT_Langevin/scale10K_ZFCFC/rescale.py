from PPMS.ppms import PPMS
import numpy as np

rf = 5.68279524355581

def rescale_B(input_file, output_file):
  ppms = PPMS()
  ppms.load(input_file)
  B, M = ppms.get_BM()
  sM = ppms.get('M. Std. Err. (emu)')
  M *= 1000
  sM *= 1000
  validValues = sM > 0

  B = B[validValues]
  M = M[validValues]
  sM = sM[validValues]

  M = M * rf
  sM = sM * rf

  with open(output_file, 'w') as f:
    f.write(f'#Loaded datafile {input_file}\n')
    f.write(f'#Rescaled data with factor {rf}\n')

    f.write(f'#B/T\tM/kAm-1\tsM/kAm-1\n')

    for i in range(len(B)):
      f.write(f'{B[i]}\t{M[i]}\t{sM[i]}\n')

def rescale_T(input_file, output_file):
  ppms = PPMS()
  ppms.load(input_file)
  T, M = ppms.get_TM()
  sM = ppms.get('M. Std. Err. (emu)')
  M *= 1000
  sM *= 1000
  validValues = sM > 0

  T = T[validValues]
  M = M[validValues]
  sM = sM[validValues]

  M = M * rf
  sM = sM * rf

  with open(output_file, 'w') as f:
    f.write(f'#Loaded datafile {input_file}\n')
    f.write(f'#Rescaled data with factor {rf}\n')

    f.write(f'#T/K\tM/kAm-1\tsM/kAm-1\n')

    for i in range(len(T)):
      f.write(f'{T[i]}\t{M[i]}\t{sM[i]}\n')

rescale_B('../../DD205_4_KOELNPPMS_HYST_100OE_10K.DAT', 'dd205_4_10K_rescaled.dat')
rescale_T('../../DD205_4_KOELNPPMS_FCW_100OE_TOUCHDOWN.DAT', 'dd205_4_fcw_rescaled.dat')
rescale_T('../../DD205_4_KOELNPPMS_ZFCW_100OE_TOUCHDOWN.DAT', 'dd205_4_zfcw_rescaled.dat')