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

dataRef.loadFromFile('../ES-S17.xye')
dataRef.sliceDomain(0, 0.3)
dataRef.plotData()

modelRef = app.setModel(SphereCSStackedParabolicSpacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 1.9000000000000002e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 6.469748181704578,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.037030188619610695,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("packingDensity", 0.34818342238445305,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensitySlope", 0.00025296878060701924,  minVal = -0.005, maxVal = 0.005, vary = True)
modelRef.setParam("layerDistance", 38.400000000000006,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistanceSlope", 0.07083678572856034,  minVal = -1, maxVal = 1, vary = True)
modelRef.setParam("dSpacer", 27.6,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 2.0458904702351537e-05,  minVal = 0, maxVal = 3e-05, vary = True)
modelRef.setParam("dWavelength", 0.020800000000000003,  minVal = 0, maxVal = 0.1, vary = False)
modelRef.setParam("qShift", -0.004032620509250784,  minVal = -0.01, maxVal = 0.01, vary = True)
modelRef.setParam("nPeriods", 9.892999999999999,  minVal = 0, maxVal = 13, vary = False)
modelRef.setParam("layerDistanceParab", 0.,  minVal = -0.01, maxVal = 0.01, vary = True)

modelRef.setConstantParam("roughnessParab", 0.)
modelRef.setConstantParam("packingDensityParab", 0.)
modelRef.setConstantParam("r", 35.4)
modelRef.setConstantParam("d", 16.9)
modelRef.setConstantParam("sigR", 0.0752)
modelRef.setConstantParam('sldCore', sld_xray_D8['Magnetite'].real)
modelRef.setConstantParam('sldShell', sld_xray_D8['Oleic Acid'].real)
modelRef.setConstantParam('sldSubstrate', sld_xray_D8['Silicon'].real)
modelRef.setConstantParam('sldBackground', 0e-6)

# D8 properties
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0)
modelRef.setConstantParam('wavelength', 1.5418)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 1200, 500))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()