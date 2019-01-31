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

datafile = '../data_rescaling/SC-IOS-11_300K_LangevinSAXSscaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.plotData()

modelRef = app.setModel(TwoLangevin)
modelRef.setParam("Ms1", 0.15822642761862843*1301.371861446249,  minVal = 150, maxVal = 260, vary = False)
modelRef.setParam("mu1", 13767.92552707809,  minVal = 13e3, maxVal = 18000, vary = False)
modelRef.setParam("Ms2", 0,  minVal = 0, maxVal = 50, vary = False)
modelRef.setParam("mu2", 858.1,  minVal = 700, maxVal = 1000, vary = False)
modelRef.setParam("chi", 0.0,  minVal = -20, maxVal = 20, vary = False)
modelRef.setConstantParam("T", 300)

app.setFit(LevenbergMarquardt)

app.show()