from GISANS.GISANSEval import GISANSEval
import numpy as np

sdd = 5000 # m
qzMin,qzMax = 0.0095, 0.013
qyMin = 0.01
qyMax = 0.075
handler = GISANSEval(sdd, qzMin, qzMax, qyMin, qyMax, _transpose=True)

handler.loadData('../../0rawdata/0204', np.arange(14, 38, 1), 'Guide Field')
handler.loadData('../../0rawdata/020', np.arange(455, 503, 1), 'Remanence')
handler.loadData('../../0rawdata/020', np.arange(503, 527, 1), 'Negative Field')
handler.plotYonedaDifference('Guide Field', 'Remanence', 'dd175_28_diff_gfrem.png')
handler.plotYonedaDifference('Guide Field', 'Negative Field', 'dd175_28_diff_gfneg.png')
handler.plotYonedaDifference('Remanence', 'Negative Field', 'dd175_28_diff_remneg.png')
