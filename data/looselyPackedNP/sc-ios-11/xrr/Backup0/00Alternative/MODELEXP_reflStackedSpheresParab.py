#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import SphereCSStackedParabolicSpacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S14.xye')
dataRef.sliceDomain(0, 0.15)
dataRef.plotData()

modelRef = app.setModel(SphereCSStackedParabolicSpacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 1.9000000000000002e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 6.84,  minVal = 0.0, maxVal = 20, vary = False)
modelRef.setParam("roughnessSlope", 0.0629,  minVal = 0.0, maxVal = 0.1, vary = False)
modelRef.setParam("roughnessParab", 0.0,  minVal = 0.0, maxVal = 0.001, vary = False)
modelRef.setParam("packingDensity", 0.585,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensitySlope", -0.0015199999999999997,  minVal = -0.005, maxVal = 0.005, vary = False)
modelRef.setParam("packingDensityParab", 4.9900000000000005e-06,  minVal = -5e-05, maxVal = 5e-05, vary = False)
modelRef.setParam("layerDistance", 10.100000000000001,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistanceSlope", -0.16400000000000003,  minVal = -1, maxVal = 1, vary = True)
modelRef.setParam("layerDistanceParab", -0.0001,  minVal = -0.001, maxVal = 0.001, vary = True)
modelRef.setParam("dSpacer", 75.8,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 2.3220000000000005e-05,  minVal = 0, maxVal = 3e-05, vary = False)
modelRef.setParam("dWavelength", 0.0105,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("qShift", -0.004399999999999999,  minVal = -0.01, maxVal = 0.01, vary = True)

modelRef.setConstantParam("r", 54.1)
modelRef.setConstantParam("d", 18.2)
modelRef.setConstantParam("sigR", 0.0545)
modelRef.setConstantParam('sldCore', sld_xray_D8['Magnetite'].real)
modelRef.setConstantParam('sldShell', sld_xray_D8['Oleic Acid'].real)
modelRef.setConstantParam('sldSubstrate', sld_xray_D8['Silicon'].real)
modelRef.setConstantParam('sldBackground', 0e-6)
modelRef.setConstantParam('nPeriods', 5)

# D8 properties
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0)
modelRef.setConstantParam('wavelength', 1.5418)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 700, 150))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()