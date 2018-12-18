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

datafile = './rescale/DD67_300K_LangevinSAXSscaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.sliceDomain(-2,2)
dataRef.plotData()
modelRef = app.setModel(LangevinMuWeighted)
modelRef.setParam("Ms", 34.2,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("mu", 3790.0,  minVal = 0, maxVal = 10000, vary = True)
modelRef.setParam("chi", 20.400000000000006,  minVal = -100, maxVal = 100, vary = True)
modelRef.setParam("sigMu", 0.278,  minVal = 0, maxVal = 1, vary = False)
modelRef.setConstantParam('T', 300)

app.setFit(LevenbergMarquardt)

app.show()