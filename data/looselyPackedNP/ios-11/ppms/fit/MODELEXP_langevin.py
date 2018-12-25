#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:47:32.203901
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.magnetometry import Vsm
from modelexp.models.magnetometry import Langevin
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

datafile = '../data_rescaling/PMK18_300K_LangevinSAXSscaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.plotData()

modelRef = app.setModel(Langevin)
modelRef.setParam("Ms", 164.14343549707334,  minVal = 0, maxVal = 400, vary = True)
modelRef.setParam("mu", 11354.26250066554,  minVal = 0, maxVal = 30000, vary = True)
modelRef.setParam("chi", 2.6799999999999997,  minVal = -20, maxVal = 20, vary = True)
modelRef.setConstantParam("sigMu", 0)
modelRef.setConstantParam("T", 300)

app.setFit(LevenbergMarquardt)

app.show()