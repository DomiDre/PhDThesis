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

datafile = './rescale/AH11_350K_LangevinSAXSscaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.sliceDomain(-2, 2)
dataRef.plotData()
modelRef = app.setModel(LangevinMuWeighted)
modelRef.setParam("Ms", 151.5,  minVal = 0, maxVal = 300, vary = True)
modelRef.setParam("mu", 11550.0,  minVal = 0, maxVal = 50000, vary = True)
modelRef.setParam("chi", -135.6,  minVal = -300, maxVal = 0, vary = True)
modelRef.setParam("sigMu", 0.357,  minVal = 0, maxVal = 1, vary = False)
modelRef.setConstantParam('T', 350)

app.setFit(LevenbergMarquardt)

app.show()