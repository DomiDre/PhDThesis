#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:47:32.203901
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
import numpy as np
from modelexp import App
from modelexp.experiments.magnetometry import Vsm
from modelexp.models.magnetometry import TwoLangevin
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

datafile = '../../rawdata/dd147_stabledry_2_BGLinSub.xy'

app = App()
expRef = app.setExperiment(Vsm)
# expRef.setFitRange(-0.1,0.1)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)

dataRef.plotData()
modelRef = app.setModel(TwoLangevin)
modelRef.setParam("Ms1", 4.2,  minVal = 0, maxVal = 15, vary = True)
modelRef.setParam("mu1", 101000.0,  minVal = 50000.0, maxVal = 200000, vary = True)
modelRef.setParam("Ms2", 4.78,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("mu2", 15300.847,  minVal = 1, maxVal = 100000, vary = True)
modelRef.setParam("chi", 0.4399999999999995,  minVal = -10, maxVal = 10, vary = True)
modelRef.setConstantParam('T', 295) # 22 C
app.setFit(LevenbergMarquardt)

app.show()