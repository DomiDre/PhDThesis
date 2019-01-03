from GISANS.GISANSEval import GISANSEval
import numpy as np

sdd = 5000 # m
qzMin,qzMax = 0.0095, 0.0126
qyMin = 0.01
qyMax = 0.075
handler = GISANSEval(sdd, qzMin, qzMax, qyMin, qyMax)
handler.Imin = 1.5e-3
handler.Imax = 2e-2
# #sat I+
handler.loadAndProject('../../0rawdata/020', np.arange(673, 685, 2))
handler.plotData('DD175.28 Saturated I+', 'dd175_28_sat_i+.png')
handler.plotYoneda('Saturated I+')

# #sat I-
handler.loadAndProject('../../0rawdata/020', np.arange(674, 685, 2))
handler.plotData('DD175.28 Saturated I-', 'dd175_28_sat_i-.png')
handler.plotYoneda('Saturated I-')

#rem I+
handler.loadAndProject('../../0rawdata/020', np.arange(685, 697, 2))
handler.plotData('DD175.28 Remanence I+', 'dd175_28_rem_i+.png')
handler.plotYoneda('Remanence I+')

#rem I-
handler.loadAndProject('../../0rawdata/020', np.arange(686, 697, 2))
handler.plotData('DD175.28 Remanence I-', 'dd175_28_rem_i-.png')
handler.plotYoneda('Remanence I-')

#negField I+
handler.loadAndProject('../../0rawdata/020', np.arange(697, 709, 2))
handler.plotData('DD175.28 neg. Field I+', 'dd175_28_negField_i+.png')
handler.plotYoneda('neg. Field I+')

#negField I-
handler.loadAndProject('../../0rawdata/020', np.arange(698, 709, 2))
handler.plotData('DD175.28 neg. Field I-', 'dd175_28_negField_i-.png')
handler.plotYoneda('neg. Field I-')


handler.showYoneda('DD175.28 Field || Beam, ZFC, 250K', 'dd175_28_yoneda_satremNegField.png')