from PPMS.ppms import PPMS
import numpy as np
datafile = '../DD205_4_KOELNPPMS_HYST_100OE_300K.DAT'
ppms = PPMS()
ppms.load(datafile)
B, M = ppms.get_BM()
sM = ppms.get('M. Std. Err. (emu)')
M *= 1000
sM *= 1000
validValues = sM > 0

B = B[validValues]
M = M[validValues]
sM = sM[validValues]

Ms_fit = 36.4433331

# mu = 16242 muB
# v = 727325 A3 (r=46.9420801, p = 2.65742743)
Ms_calc = 207.10

M = M * Ms_calc/Ms_fit
sM = sM * Ms_calc/Ms_fit

with open('dd205_4_300K_rescaled.dat', 'w') as f:
  f.write(f'#Loaded datafile {datafile}\n')
  f.write(f'#Used as Ms_fit {Ms_fit}\n')
  f.write(f'#Used as Ms_calc {Ms_calc}\n')
  f.write(f'#Rescaled data with factor {Ms_calc/Ms_fit}\n')

  f.write(f'#B/T\tM/kAm-1\tsM/kAm-1\n')

  for i in range(len(B)):
    f.write(f'{B[i]}\t{M[i]}\t{sM[i]}\n')