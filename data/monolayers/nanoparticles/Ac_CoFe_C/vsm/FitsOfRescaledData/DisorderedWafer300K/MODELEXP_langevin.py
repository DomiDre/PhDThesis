#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:47:32.203901
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.magnetometry import Vsm
from modelexp.models.magnetometry import LangevinMuWeighted
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

datafile = '../../rescale/Ac_CoFe_C_DisorderedWafer_300K_LangevinSAXSscaled.xye'

app = App()
expRef = app.setExperiment(Vsm)
expRef.setFitRange(-2,2)
dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.plotData()
modelRef = app.setModel(LangevinMuWeighted)
modelRef.setParam("Ms", 300.0,  minVal = 0, maxVal = 400, vary = False)
modelRef.setParam("mu", 22100.0,  minVal = 0, maxVal = 50000, vary = False)
modelRef.setParam("chi", -1.1999999999999886,  minVal = -300, maxVal = 0, vary = False)
modelRef.setParam("sigMu", 0.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.setConstantParam('T', 300)
modelRef.setConstantParam('orderHermite', 50)

app.setFit(LevenbergMarquardt)

app.show()