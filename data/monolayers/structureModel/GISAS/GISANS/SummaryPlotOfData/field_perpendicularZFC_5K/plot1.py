from GISANS.GISANSEval import GISANSEval
import numpy as np

sdd = 5000 # m
qzMin,qzMax = 0.0085, 0.0126
qyMin,qyMax = 0.01, 0.07
handler = GISANSEval(sdd, qzMin, qzMax, qyMin, qyMax)

handler.loadData('../../0rawdata/020', np.arange(947, 959, 1), 'Guide Field')
handler.loadData('../../0rawdata/020', np.arange(959, 971, 1), 'Remanence')

handler.plotYonedaDifference('Guide Field', 'Remanence', 'dd175_28_diff_gfrem.png')

# handler.plotData('DD175.28 Guide Field', 'dd175_28_gf.png')
# handler.plotYoneda('Guide Field')

# #Remanence
# handler.plotData('DD175.28 Remanence', 'dd175_28_rem.png')
# handler.plotYoneda('Remanence')

# handler.showYoneda('DD175.28 Perp. ZFC, 5K', 'dd175_28_yoneda_gfrem.png')