import VSMLangevinNP
from PPMS.ppms import PPMS
import numpy as np
import fortMag

# fortMag.flib.math.n_integration_cuts = 1
datafile = '../rawdata/DD226_2_HYST_350K_REPEAT.DAT'
samplename = 'AH11'
r = 46.9420801
p = 2.65742743
sigR = 0.119
Bmin, Bmax = -2, 2

ppms = PPMS()
ppms.load(datafile)
ppms.remove_virgin_data()
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
M *= 1000
sM *= 1000

langevinScale = VSMLangevinNP.init(fit_size_distribution=True, verbose=True)
langevinScale.set_xye(B, M, sM, datafile)
langevinScale.set_superball(r, p)
langevinScale.set_size_distribution(3*sigR, 0, 3, False)
langevinScale.set_Ms(43, True)
langevinScale.set_mu(11000, True)
langevinScale.set_chi(-34, True)
langevinScale.set_T(350)
print(langevinScale.p)
langevinScale.perform_fit()
langevinScale.save_fit_plot('fit_plot.png')
langevinScale.save(f'{samplename}_LangevinSAXSscaled.xye')