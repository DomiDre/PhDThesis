from GISANS.GISANSEval import GISANSEval
import numpy as np

sdd = 5000 # m
qzMin,qzMax = 0.0095, 0.0126
qyMin = 0.01
qyMax = 0.075
handler = GISANSEval(sdd, qzMin, qzMax, qyMin, qyMax)
handler.Imin = 1.5e-3
handler.Imax = 2e-2
# #sat
handler.loadAndProject('../../0rawdata/020', np.arange(673, 685, 1))
handler.plotData('DD175.28 Saturated', 'dd175_28_sat.png')
handler.plotYoneda('Saturated')


#rem
handler.loadAndProject('../../0rawdata/020', np.arange(685, 697, 1))
handler.plotData('DD175.28 Remanence', 'dd175_28_rem.png')
handler.plotYoneda('Remanence')

#negField
handler.loadAndProject('../../0rawdata/020', np.arange(697, 709, 1))
handler.plotData('DD175.28 neg. Field', 'dd175_28_negField.png')
handler.plotYoneda('neg. Field')