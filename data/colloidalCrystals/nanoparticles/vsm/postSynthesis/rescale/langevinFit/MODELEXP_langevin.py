#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:47:32.203901
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
import numpy as np
from modelexp import App
from modelexp.experiments.magnetometry import Vsm
from modelexp.models.magnetometry import LangevinMuWeighted
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

datafile = '../../rawdata/dd144_dry_BGLinSub.xy'

app = App()
expRef = app.setExperiment(Vsm)
# expRef.setFitRange(-2,2)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)

dataRef.plotData()
modelRef = app.setModel(LangevinMuWeighted)
modelRef.setParam("Ms", 22.05,  minVal = 0, maxVal = 50, vary = False)
modelRef.setParam("mu", 17730.409,  minVal = 1, maxVal = 30000, vary = False)
modelRef.setParam("chi", 3.92,  minVal = -10, maxVal = 10, vary = False)
modelRef.setParam("sigMu", 0.0,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setConstantParam('orderHermite', 50)
modelRef.setConstantParam('T', 296) # 22 C

app.setFit(LevenbergMarquardt)

app.show()