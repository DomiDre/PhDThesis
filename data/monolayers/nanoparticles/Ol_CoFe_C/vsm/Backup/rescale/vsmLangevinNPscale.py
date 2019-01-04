import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
datafile = '../rawdata/DD172_6_HYST_300K.DAT'
samplename = 'DD67'
r = 56.2265926
p = 1.53773769
sigR = 0.09266898
Bmin, Bmax = -2, 2

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

langevinScale = VSMLangevinNP.init(verbose=True)
langevinScale.set_xye(B, M, sM, datafile)
langevinScale.set_superball(r, p)
langevinScale.set_size_distribution(3*sigR, vary=False)
langevinScale.set_chi(-0.035)
langevinScale.set_T(300)
langevinScale.perform_fit()

langevinScale.save_fit_plot('fit_plot.png')
langevinScale.save(f'{samplename}_LangevinSAXSscaled.xye')