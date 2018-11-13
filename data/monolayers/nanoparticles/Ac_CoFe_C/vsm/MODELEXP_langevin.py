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

datafile = './AH11_LangevinSAXSscaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.plotData()
modelRef = app.setModel(Langevin)
modelRef.setParam("Ms", 287.4,  minVal = 0, maxVal = 300, vary = True)
modelRef.setParam("mu", 22500.0,  minVal = 0, maxVal = 50000, vary = True)
modelRef.setParam("chi", 3.0,  minVal = -100, maxVal = 100, vary = True)
# modelRef.setParam("sigMu", 0.3, minVal =0, maxVal= 1, vary=True)
modelRef.setConstantParam("sigMu", 0.0)
modelRef.setConstantParam('T', 300)

app.setFit(LevenbergMarquardt)

app.show()