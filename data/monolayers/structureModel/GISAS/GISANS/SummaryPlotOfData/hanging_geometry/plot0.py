from GISANS.GISANSEval import GISANSEval
import numpy as np

sdd = 5000 # m
qzMin,qzMax = 0.0095, 0.013
qyMin = 0.01
qyMax = 0.075
handler = GISANSEval(sdd, qzMin, qzMax, qyMin, qyMax, _transpose=True)

#gf I+
handler.loadAndProject('../../0rawdata/0204', np.arange(14, 38, 2))
handler.plotData('DD175.28 Guide Field I+', 'dd175_28_gf_i+.png')
handler.plotYoneda('Guide Field I+')

#gf I-
handler.loadAndProject('../../0rawdata/0204', np.arange(15, 38, 2))
handler.plotData('DD175.28 Guide Field I-', 'dd175_28_gf_i-.png')
handler.plotYoneda('Guide Field I-')

# #sat I+
# handler.loadAndProject('../../0rawdata/0204', np.arange(38, 40, 2))
# handler.plotData('DD175.28 Saturated I+', 'dd175_28_sat_i+.png')
# handler.plotYoneda('Saturated I+')

# #sat I-
# handler.loadAndProject('../../0rawdata/0204', np.arange(39, 40, 2))
# handler.plotData('DD175.28 Saturated I-', 'dd175_28_sat_i-.png')
# handler.plotYoneda('Saturated I-')

#rem I+
handler.loadAndProject('../../0rawdata/020', np.arange(455, 503, 2))
handler.plotData('DD175.28 Remanence I+', 'dd175_28_rem_i+.png')
handler.plotYoneda('Remanence I+')

#rem I-
handler.loadAndProject('../../0rawdata/020', np.arange(456, 503, 2))
handler.plotData('DD175.28 Remanence I-', 'dd175_28_rem_i-.png')
handler.plotYoneda('Remanence I-')

#negField I+
handler.loadAndProject('../../0rawdata/020', np.arange(503, 527, 2))
handler.plotData('DD175.28 neg. Field I+', 'dd175_28_negField_i+.png')
handler.plotYoneda('neg. Field I+')

#negField I-
handler.loadAndProject('../../0rawdata/020', np.arange(504, 527, 2))
handler.plotData('DD175.28 neg. Field I-', 'dd175_28_negField_i-.png')
handler.plotYoneda('neg. Field I-')


handler.showYoneda('DD175.28 Field || Beam, ZFC, 5K', 'dd175_28_yoneda_gfremNegField.png')