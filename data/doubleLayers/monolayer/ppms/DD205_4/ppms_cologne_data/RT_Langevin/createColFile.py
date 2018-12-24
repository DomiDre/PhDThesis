from PPMS.ppms import PPMS

datafile = '../DD205_4_KOELNPPMS_HYST_100OE_300K.DAT'
ppms = PPMS()
ppms.load(datafile)
B, M = ppms.get_BM()
sM = ppms.get('M. Std. Err. (emu)')
M*=1000
sM*=1000
with open('dd205_4_300K_columnfile.dat', 'w') as f:
  f.write(f'#Loaded datafile {datafile}\n')
  f.write(f'#B/T\tM/memu\tsM/memu\n')

  for i in range(len(B)):
    f.write(f'{B[i]}\t{M[i]}\t{sM[i]}\n')