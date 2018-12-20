#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import SphereCSSStacked6Spacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES_S14_300K_4mT_refl_corrected_combined.xy')
dataRef.sliceDomain(0, 0.15)
dataRef.plotData()

modelRef = app.setModel(SphereCSSStacked6Spacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 2.6279697434099622e-05,  minVal = 0.0, maxVal = 0.0001, vary = True)
modelRef.setParam("roughness", 10.389818738326472,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.0437,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("dSpacer", 37.123726506927866,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 2.034628305975884e-06,  minVal = 0, maxVal = 5e-06, vary = True)

modelRef.setParam("packingDensity1", 0.9659414219800899,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 1.0486015784643499,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.8983715379312163,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.8062136751500585,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.776,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.15800584438626586,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("layerDistance1", -1.3762866656055621,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -27.4,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -25.4,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -25.069313914711564,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -11.917932748843526,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -0.5999999999999943,  minVal = -50, maxVal = 50, vary = True)

# modelRef.combineParameters('packingDensity1', 'packingDensity2')
# modelRef.combineParameters('packingDensity1', 'packingDensity3')
# modelRef.combineParameters('packingDensity1', 'packingDensity4')
# modelRef.combineParameters('packingDensity1', 'packingDensity5')
# modelRef.combineParameters('layerDistance1', 'layerDistance2')
# modelRef.combineParameters('layerDistance1', 'layerDistance3')
# modelRef.combineParameters('layerDistance1', 'layerDistance4')
# modelRef.combineParameters('layerDistance1', 'layerDistance5')

modelRef.setConstantParam("r", 54-16)
modelRef.setConstantParam("dShell", 16)
modelRef.setConstantParam("dSurfactant", 18.2)
modelRef.setConstantParam('sldCore', 8.34e-06)
modelRef.setConstantParam('sldShell', 7.00e-6)
modelRef.setConstantParam('sldSurfactant', 0.078e-6)
modelRef.setConstantParam('sldSubstrate', 2.072e-6)
modelRef.setConstantParam('sldBackground', 0e-6)
modelRef.setConstantParam('sldBackground', 0e-6)

# SADAM properties
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0003)
modelRef.setConstantParam("dWavelength", 0.0021)
modelRef.setConstantParam('wavelength', 5.14)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 900, 300))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()