import VSMLangevinNP
from modelexp.data import XyeData
import numpy as np
import fortMag

# fortMag.flib.math.n_integration_cuts = 1
datafile = '../rawdata/YF045_final_rescaled.xy'
samplename = 'YF45'
r = 42.8959582
p = 2.16474488
sigR = 0.1503
Bmin, Bmax = -2, 2

dataRef = XyeData()
dataRef.loadFromFile(datafile)
B, M, sM = dataRef.getData()

valid_range = np.logical_and(B>Bmin, B<Bmax)
B = B[valid_range]
M = M[valid_range]
sM = sM[valid_range]

valid_point = sM > 0
B = B[valid_point]
M = M[valid_point]
sM = sM[valid_point]
# M *= 1000
# sM *= 1000

langevinScale = VSMLangevinNP.init(fit_size_distribution=True, verbose=True)
langevinScale.set_xye(B, M, sM, datafile)
langevinScale.set_superball(r, p)
langevinScale.set_size_distribution(3*sigR, 0, 3, False)
langevinScale.set_Ms(43, True)
langevinScale.set_mu(11000, True)
langevinScale.set_chi(-34, True)
langevinScale.set_T(300)
print(langevinScale.p)
langevinScale.perform_fit()
langevinScale.save_fit_plot('fit_plot.png')
langevinScale.save(f'{samplename}_LangevinSAXSscaled.xye')