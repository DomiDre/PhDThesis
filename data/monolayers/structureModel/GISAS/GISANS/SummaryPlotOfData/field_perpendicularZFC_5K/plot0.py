from GISANS.GISANSEval import GISANSEval
import numpy as np

sdd = 5000 # m
qzMin,qzMax = 0.0085, 0.0126
handler = GISANSEval(sdd, qzMin, qzMax)

#gf
handler.loadAndProject('../../0rawdata/020', np.arange(947, 959, 1))
handler.plotData('DD175.28 Guide Field', 'dd175_28_gf.png')
handler.plotYoneda('Guide Field')

#Remanence
handler.loadAndProject('../../0rawdata/020', np.arange(959, 971, 1))
handler.plotData('DD175.28 Remanence', 'dd175_28_rem.png')
handler.plotYoneda('Remanence')

handler.showYoneda('DD175.28 Perp. ZFC, 5K', 'dd175_28_yoneda_gfrem.png')