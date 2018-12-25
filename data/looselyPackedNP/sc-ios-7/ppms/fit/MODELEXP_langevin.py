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

datafile = '../data_rescaling/SC-IOS-7_300K_LangevinSAXSscaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.plotData()

modelRef = app.setModel(Langevin)
modelRef.setParam("Ms", 219.82207769806251,  minVal = 0, maxVal = 400, vary = True)
modelRef.setParam("mu", 4373.602337595599,  minVal = 0, maxVal = 30000, vary = True)
modelRef.setParam("chi", 0.0,  minVal = -20, maxVal = 20, vary = True)
modelRef.setConstantParam("sigMu", 0)
modelRef.setConstantParam("T", 300)

app.setFit(LevenbergMarquardt)

app.show()