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

datafile = '../data_rescaling/IOS-11_Dispersion_300K_LangevinSAXSscaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.plotData()
# dataRef.sliceDomain(-2,2)

modelRef = app.setModel(TwoLangevin)
modelRef.setParam("Ms1", 194.4,  minVal = 0, maxVal = 400, vary = True)
modelRef.setParam("mu1", 13920.0,  minVal = 0, maxVal = 30000, vary = True)
modelRef.setParam("Ms2", 37.6,  minVal = 0, maxVal = 400, vary = True)
modelRef.setParam("mu2", 480.0,  minVal = 0, maxVal = 30000, vary = True)
modelRef.setParam("chi", 1.4800000000000004,  minVal = -20, maxVal = 20, vary = True)
modelRef.setConstantParam("T", 300)

app.setFit(LevenbergMarquardt)

app.show()