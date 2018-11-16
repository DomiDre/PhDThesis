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

datafile = './rescale/YF45_300K_LangevinSAXSscaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.sliceDomain(-2, 2)
dataRef.plotData()
modelRef = app.setModel(LangevinMuWeighted)
modelRef.setParam("Ms", 316.0,  minVal = 0, maxVal = 400, vary = True)
modelRef.setParam("mu", 20900.0,  minVal = 0, maxVal = 50000, vary = True)
modelRef.setParam("chi", -2.1000000000000227,  minVal = -300, maxVal = 0, vary = True)
modelRef.setParam("sigMu", 0.45,  minVal = 0, maxVal = 1, vary = False)
modelRef.setConstantParam('T', 350)

app.setFit(LevenbergMarquardt)

app.show()