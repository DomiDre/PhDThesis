from GISANS.GISANSEval import GISANSEval
import numpy as np

sdd = 5000 # m
qzMin,qzMax = 0.0095, 0.0126
qyMin = 0.01
qyMax = 0.075
handler = GISANSEval(sdd, qzMin, qzMax, qyMin, qyMax)
handler.Imin = 1.5e-3
handler.Imax = 2e-2
handler.loadData('../../0rawdata/020', np.arange(781, 805, 1), 'Saturated')
handler.loadData('../../0rawdata/020', np.arange(805, 829, 1), 'Remanence')
handler.loadData('../../0rawdata/020', np.arange(829, 853, 1), 'Negative Field')
handler.plotYonedaDifference('Saturated', 'Remanence', 'dd175_28_diff_satrem.png')
handler.plotYonedaDifference('Saturated', 'Negative Field', 'dd175_28_diff_satneg.png')
handler.plotYonedaDifference('Remanence', 'Negative Field', 'dd175_28_diff_remneg.png')

