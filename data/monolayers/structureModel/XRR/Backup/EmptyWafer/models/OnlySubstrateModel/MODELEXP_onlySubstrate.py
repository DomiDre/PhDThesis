#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import Substrate, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8

app = App()

app.setExperiment(Reflectometry)

dataRef = app.setData(XyeData)
dataRef.loadFromFile('../../transform_data/SiWafer.xye')
dataRef.sliceDomain(0.01, 0.25)
dataRef.plotData()

modelRef = app.setModel(Substrate, [InstrumentalResolution, ShiftQ])

modelRef.setParam("bg", 3.9e-06,  minVal = 0.0, maxVal = 0.0001, vary = True)
modelRef.setParam("qShift", -0.0007600000000000003,  minVal = -0.01, maxVal = 0.01, vary = True)
modelRef.setParam("dWavelength", 0.0524,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("roughness", 9.82,  minVal = 0.0, maxVal = 20, vary = True)

modelRef.setConstantParam("sldSubstrate", 2.061e-05)
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam('wavelength', 1.5418)
modelRef.setConstantParam("dTheta", 0.0)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()