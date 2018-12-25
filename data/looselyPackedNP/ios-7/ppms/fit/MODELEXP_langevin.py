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

datafile = '../data_rescaling/KWi338_300K_LangevinSAXSscaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.plotData()

modelRef = app.setModel(Langevin)
modelRef.setParam("Ms", 183.13147505217555,  minVal = 0, maxVal = 400, vary = True)
modelRef.setParam("mu", 3616.9508388765958,  minVal = 0, maxVal = 5000, vary = True)
modelRef.setParam("chi", -0.6425614270361066,  minVal = -20, maxVal = 20, vary = True)
modelRef.setConstantParam("sigMu", 0)
modelRef.setConstantParam("T", 300)

app.setFit(LevenbergMarquardt)

app.show()