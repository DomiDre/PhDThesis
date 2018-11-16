#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import Substrate, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8

app = App()

app.setExperiment(Reflectometry)

dataRef = app.setData(XyeData)
dataRef.loadFromFile('../../transform_data/SiWafer.xye')
dataRef.sliceDomain(0.01, 0.25)
dataRef.plotData()

modelRef = app.setModel(Substrate, InstrumentalResolution)

modelRef.setParam("bg", 3e-06,  minVal = 0.0, maxVal = 0.0001, vary = True)
modelRef.setParam("roughness", 9.32,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("sldSubstrate", 1.9686962563206795e-05,  minVal = 0, maxVal = 5e-05, vary = True)
modelRef.setParam("dTheta", 0.0,  minVal = 0, maxVal = 0.001, vary = False)
modelRef.setParam("dWavelength", 0.0543,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()