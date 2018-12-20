#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import SphereCSStacked6Spacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0, 0.15)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S14.xye')
dataRef.sliceDomain(0, 0.3)
dataRef.plotData()

modelRef = app.setModel(SphereCSStacked6Spacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 0.0,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 6.502767577306686,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.0339,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("packingDensity1", 0.509,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity2", 0.554,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity3", 0.529,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity4", 0.498,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity5", 0.534,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity6", 0.28600000000000003,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("layerDistance1", -10.599999999999994,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance2", -26.2,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance3", -26.9,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance4", -29.5,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance5", -26.7,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance6", -18.2,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("dSpacer", 51.5,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("sldSpacer", 1.1880000000000001e-05,  minVal = 0, maxVal = 3e-05, vary = False)
modelRef.setParam("dWavelength", 0.0112,  minVal = 0, maxVal = 0.1, vary = False)

modelRef.setConstantParam("r", 54.1)
modelRef.setConstantParam("d", 18.2)
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