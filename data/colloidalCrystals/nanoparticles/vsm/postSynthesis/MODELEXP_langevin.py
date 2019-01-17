#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:47:32.203901
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.magnetometry import Vsm
from modelexp.models.magnetometry import TwoLangevin
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

datafile = './rescale/Ol-Fe-C_powder_295K_rescaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.sliceDomain(-2,2)
dataRef.plotData()
modelRef = app.setModel(TwoLangevin)
modelRef.setParam("Ms1", 154.5,  minVal = 120, maxVal = 180, vary = False)
modelRef.setParam("mu1", 25590.0,  minVal = 15000, maxVal = 30000, vary = False)
modelRef.setParam("Ms2", 177.10000000000002,  minVal = 100, maxVal = 200, vary = False)
modelRef.setParam("mu2", 3602.0,  minVal = 2000, maxVal = 5000, vary = False)
modelRef.setParam("chi", 42.400000000000006,  minVal = -100, maxVal = 100, vary = False)
modelRef.setConstantParam('T', 295)
app.setFit(LevenbergMarquardt)

app.show()