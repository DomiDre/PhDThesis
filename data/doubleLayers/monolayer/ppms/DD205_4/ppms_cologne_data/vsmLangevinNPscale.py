import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
datafile = './DD205_4_KOELNPPMS_HYST_100OE_300K.DAT'
samplename = 'AH11_ML'
r = 46.9420801
p = 2.65742743

Bmin, Bmax = -1, 1

ppms = PPMS()
ppms.load(datafile)
B, M = ppms.get_BM()
sM = ppms.get('M. Std. Err. (emu)')
valid_range = np.logical_and(B>Bmin, B<Bmax)
B = B[valid_range]
M = M[valid_range]
sM = sM[valid_range]

valid_point = sM > 0
B = B[valid_point]
M = M[valid_point]
sM = sM[valid_point]
M*=1000
sM*=1000

langevinScale = VSMLangevinNP.init()
langevinScale.set_xye(B, M, sM, datafile)
langevinScale.set_superball(r, p)
langevinScale.perform_fit()

langevinScale.save_fit_plot('fit_plot.png')
langevinScale.save(f'{samplename}_LangevinSAXSscaled.xye')