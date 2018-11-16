#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import OneLayer, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8

app = App()

app.setExperiment(Reflectometry)

dataRef = app.setData(XyeData)
dataRef.loadFromFile('./transform_data/SiWafer.xye')
dataRef.sliceDomain(0.01, 0.4)
dataRef.plotData()

modelRef = app.setModel(OneLayer, InstrumentalResolution)

modelRef.setParam("bg", 1.3e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughnessSubstrate", 0.0,  minVal = 0.0, maxVal = 20, vary = False)
modelRef.setParam("roughnessLayer", 0.0,  minVal = 0.0, maxVal = 20, vary = False)
modelRef.setParam("sldLayer", 2.2700000000000003e-05,  minVal = 0, maxVal = 5e-05, vary = False)
modelRef.setParam("sldSubstrate", 2.0050000000000003e-05,  minVal = 0, maxVal = 5e-05, vary = False)
modelRef.setParam("thickness", 1.0,  minVal = 1.0, maxVal = 20, vary = False)
modelRef.setParam("dTheta", 0.0,  minVal = 0, maxVal = 0.001, vary = True)
modelRef.setParam("dWavelength", 0.045000000000000005,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()