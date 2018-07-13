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

datafile = 'finalPMK18.xy'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.plotData()

modelRef = app.setModel(Langevin)
modelRef.setParam("Ms", 204.94725380743165,  minVal = 0, maxVal = 300, vary = True)
modelRef.setParam("mu", 12418.235571179048,  minVal = 0, maxVal = 50000, vary = True)
modelRef.setParam("chi", 13.493005717350258,  minVal = -100, maxVal = 100, vary = True)
modelRef.setParam("sigMu", 0.3283108705014714,  minVal = 0, maxVal = 0.8, vary = True)

app.setFit(LevenbergMarquardt)

app.show()