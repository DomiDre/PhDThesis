#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import SphereCSStackedSpacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0, 0.1)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S17.xye')
dataRef.sliceDomain(0, 0.3)
dataRef.plotData()

modelRef = app.setModel(SphereCSStackedSpacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 1.9000000000000002e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 4.8,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.011600000000000001,  minVal = 0.0, maxVal = 0.1, vary = False)
modelRef.setParam("packingDensity", 0.319,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("layerDistance",  -12.199999999999996,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("dSpacer", 36.209092576635925,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 1.23e-06,  minVal = 0, maxVal = 3e-05, vary = False)
modelRef.setParam("nPeriods", 11.038,  minVal = 1, maxVal = 15, vary = False)
modelRef.setParam("dWavelength", 0.011300000000000001,  minVal = 0, maxVal = 0.1, vary = False)
modelRef.setParam("qShift", -0.003799999999999998,  minVal = -0.1, maxVal = 0.1, vary = False)

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
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 900, 300))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()