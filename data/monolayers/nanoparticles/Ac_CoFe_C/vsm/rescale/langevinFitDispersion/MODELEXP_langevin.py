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

datafile = '../../data_dispersion/AH11_HYST_100OE_300K.DAT'

app = App()
expRef = app.setExperiment(Vsm)
expRef.setFitRange(-2,2)

ppms = PPMS()
ppms.load(datafile)
ppms.remove_virgin_data()
B, M = ppms.get_BM()
sM = ppms.get('M. Std. Err. (emu)')
valid_range = np.logical_and(B>-2.3, B<2.3)
B = B[valid_range]
M = M[valid_range]
sM = sM[valid_range]

dataRef = app.setData(XyeData)
dataset = XyeData()
dataset.setData(B, M, sM)
dataRef.addDataset(dataset)

dataRef.plotData()
modelRef = app.setModel(LangevinMuWeighted)
modelRef.setParam("Ms", 1.9934283666829482,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("mu", 23157.342191585358,  minVal = 1, maxVal = 30000, vary = True)
modelRef.setParam("chi", -0.009467968128018742,  minVal = -0.1, maxVal = 0.1, vary = True)
modelRef.setParam("sigMu", 0.0,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setConstantParam('orderHermite', 50)
modelRef.setConstantParam('T', 300)

app.setFit(LevenbergMarquardt)

app.show()