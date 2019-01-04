from PPMS.ppms import PPMS
import numpy as np

rf = 5.68279524355581

def rescale_B(input_file, output_file):
  ppms = PPMS()
  ppms.load(input_file)
  ppms.fit_diamagnetism(6,9, show=False)
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

rescale_B('./DD205_4_KOELNPPMS_HYST_100OE_5K.DAT', 'dd205_4_5K_rescaled.dat')
# rescale_B('./DD205_4_KOELNPPMS_HYST_100OE_10K.DAT', 'dd205_4_10K_rescaled.dat')
# rescale_B('./DD205_4_KOELNPPMS_HYST_100OE_20K.DAT', 'dd205_4_20K_rescaled.dat')
# rescale_B('./DD205_4_KOELNPPMS_HYST_100OE_50K.DAT', 'dd205_4_50K_rescaled.dat')
# rescale_B('./DD205_4_KOELNPPMS_HYST_100OE_100K.DAT', 'dd205_4_100K_rescaled.dat')
# rescale_B('./DD205_4_KOELNPPMS_HYST_100OE_150K.DAT', 'dd205_4_150K_rescaled.dat')
# rescale_B('./DD205_4_KOELNPPMS_HYST_100OE_200K.DAT', 'dd205_4_200K_rescaled.dat')
# rescale_B('./DD205_4_KOELNPPMS_HYST_100OE_250K.DAT', 'dd205_4_250K_rescaled.dat')
# rescale_B('./DD205_4_KOELNPPMS_HYST_100OE_300K.DAT', 'dd205_4_300K_rescaled.dat')
# rescale_T('./DD205_4_KOELNPPMS_FCW_100OE_TOUCHDOWN.DAT', 'dd205_4_fcw_rescaled.dat')
# rescale_T('./DD205_4_KOELNPPMS_ZFCW_100OE_TOUCHDOWN.DAT', 'dd205_4_zfcw_rescaled.dat')