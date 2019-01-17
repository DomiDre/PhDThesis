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

datafile = '../../rawdata/dd144_dry_BGLinSub.xy'

app = App()
expRef = app.setExperiment(Vsm)
# expRef.setFitRange(-0.1,0.1)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)

dataRef.plotData()
modelRef = app.setModel(TwoLangevin)
modelRef.setParam("Ms1", 11.32646452540523,  minVal = 0, maxVal = 50, vary = True)
modelRef.setParam("mu1", 25600.963823584912,  minVal = 1, maxVal = 30000, vary = True)
modelRef.setParam("Ms2", 12.981961523057253,  minVal = 0, maxVal = 50, vary = True)
modelRef.setParam("mu2", 3604.774008399192,  minVal = 1, maxVal = 30000, vary = True)
modelRef.setParam("chi", 3.1233109629283877,  minVal = -10, maxVal = 10, vary = True)
modelRef.setConstantParam('T', 295) # 22 C
app.setFit(LevenbergMarquardt)

app.show()