from GISANS.GISANSEval import GISANSEval
import numpy as np

sdd = 5000 # m
qzMin,qzMax = 0.0095, 0.013
qyMin = 0.01
qyMax = 0.075
handler = GISANSEval(sdd, qzMin, qzMax, qyMin, qyMax, _transpose=True)

#gf
handler.loadAndProject('../../0rawdata/0204', np.arange(14, 38, 1))
handler.plotData('DD175.28 Guide Field', 'dd175_28_gf.png')
handler.plotYoneda('Guide Field')

#rem
handler.loadAndProject('../../0rawdata/020', np.arange(455, 503, 1))
handler.plotData('DD175.28 Remanence', 'dd175_28_rem.png')
handler.plotYoneda('Remanence')

#negField
handler.loadAndProject('../../0rawdata/020', np.arange(503, 527, 1))
handler.plotData('DD175.28 neg. Field', 'dd175_28_negField.png')
handler.plotYoneda('neg. Field')