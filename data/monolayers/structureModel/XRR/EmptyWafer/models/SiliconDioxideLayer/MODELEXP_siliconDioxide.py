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
dataRef.loadFromFile('../../transform_data/SiWafer.xye')
dataRef.sliceDomain(0.01, 0.25)
dataRef.plotData()

modelRef = app.setModel(OneLayer, InstrumentalResolution)

modelRef.setParam("roughnessSubstrate", 5.84,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessLayer", 3.86,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("sldLayer", 3.4500000000000004e-06,  minVal = 0, maxVal = 5e-05, vary = True)
modelRef.setParam("sldSubstrate", 1.9687613477889477e-05,  minVal = 0, maxVal = 5e-05, vary = True)
modelRef.setParam("thickness", 19.962,  minVal = 1.0, maxVal = 100, vary = True)
modelRef.setParam("dWavelength", 0.0543,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam('wavelength', 1.5418)
modelRef.setConstantParam("dTheta", 0.0)
modelRef.setConstantParam("coverage", 1)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()