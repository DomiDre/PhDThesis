#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:47:32.203901
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from PPMS.ppms import PPMS
import numpy as np
from modelexp import App
from modelexp.experiments.magnetometry import Vsm
from modelexp.models.magnetometry import LangevinMuWeighted
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

datafile = '../../rawdata/ES_S14_HYST_30K_FC.DAT'

app = App()
app.setExperiment(Vsm)

Bmin, Bmax = -9, 9

ppms = PPMS()
ppms.load(datafile)
# ppms.remove_virgin_data()
B, M = ppms.get_BM()
sM = ppms.get('M. Std. Err. (emu)')
# valid_range = np.logical_and(B>Bmin, B<Bmax)
# B = B[valid_range]
# M = M[valid_range]
# sM = sM[valid_range]

dataRef = app.setData(XyeData)
dataset = XyeData()
dataset.setData(B, M, sM)
dataRef.addDataset(dataset)

dataRef.plotData()
modelRef = app.setModel(LangevinMuWeighted)
modelRef.setParam("Ms", 0.164,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("mu", 13740.542,  minVal = 1, maxVal = 30000, vary = False)
modelRef.setParam("chi", -0.04799999999999999,  minVal = -0.5, maxVal = 0.5, vary = False)
modelRef.setParam("sigMu", 0.0,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setConstantParam('orderHermite', 50)
modelRef.setConstantParam('T', 300)

app.setFit(LevenbergMarquardt)

app.show()