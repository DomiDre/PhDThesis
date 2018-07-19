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

datafile = 'kwi338_BGLinSub_rescale.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.plotData()

modelRef = app.setModel(Langevin)
modelRef.setParam("Ms", 309.20000000000005,  minVal = 0, maxVal = 400, vary = True)
modelRef.setParam("mu", 3770.0,  minVal = 0, maxVal = 5000, vary = True)
modelRef.setParam("chi", 18.68,  minVal = -20, maxVal = 20, vary = True)
modelRef.setParam("sigMu", 0,  minVal = 0, maxVal = 0.8, vary = False)

app.setFit(LevenbergMarquardt)

app.show()