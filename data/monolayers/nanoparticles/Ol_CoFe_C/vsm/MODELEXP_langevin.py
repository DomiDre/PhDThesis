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

datafile = './DD67_BGLinSub_rescale.xy'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.plotData()
modelRef = app.setModel(Langevin)
modelRef.setParam("Ms", 34.94870070956077,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("mu", 4685.534720201063,  minVal = 0, maxVal = 10000, vary = True)
modelRef.setParam("chi", 21.18563874258423,  minVal = -100, maxVal = 100, vary = True)
# modelRef.setParam("sigMu", 0.3, minVal =0, maxVal= 1, vary=True)
modelRef.setConstantParam("sigMu", 0.0)
modelRef.setConstantParam('T', 300)

app.setFit(LevenbergMarquardt)

app.show()