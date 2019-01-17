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

datafile = './rescale/Ol-Fe-C_powderOxidized_295K_rescaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.sliceDomain(-2,2)
dataRef.plotData()
modelRef = app.setModel(TwoLangevin)
modelRef.setParam("Ms1", 610.3,  minVal = 100, maxVal = 800, vary = True)
modelRef.setParam("mu1", 101030.0,  minVal = 50000, maxVal = 120000, vary = True)
modelRef.setParam("Ms2", 694.3,  minVal = 100, maxVal = 800, vary = True)
modelRef.setParam("mu2", 15320.0,  minVal = 0, maxVal = 20000, vary = True)
modelRef.setParam("chi", 65.4,  minVal = -100, maxVal = 100, vary = True)
modelRef.setConstantParam('T', 295)

app.setFit(LevenbergMarquardt)

app.show()