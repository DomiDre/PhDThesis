#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import Sphere
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
app.setExperiment(Saxs)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/AH22.xye')
dataRef.plotData()

modelRef = app.setModel(Sphere)
modelRef.setParam("r", 68.56,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigR", 0.134,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.015300000000000001,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("sldCore", 41.97e-6)
modelRef.setConstantParam("sldSolvent", 8.01e-6)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()