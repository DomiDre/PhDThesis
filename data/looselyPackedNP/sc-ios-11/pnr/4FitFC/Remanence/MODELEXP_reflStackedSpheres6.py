#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import SphereCSSStacked6Spacer, InstrumentalResolution, MagneticSF
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(PolarizedReflectometry)
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0.006, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../data/30Kfiles/footprint_correct/ES_S14_30K_2mT_ZFC_Remanence_reduced_in_x_ai_uu_qz_I_fcorrected.xye', ['p'])
dataRef.loadFromFile('../../data/30Kfiles/footprint_correct/ES_S14_30K_2mT_ZFC_Remanence_reduced_in_x_ai_dd_qz_I_fcorrected.xye', ['m'])
dataRef.plotData()

modelRef = app.setModel(SphereCSSStacked6Spacer, [MagneticSF, InstrumentalResolution])

modelRef.setParam("magSldCore", 1.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.setParam("magSldShell", 1.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.setParam("gamma", 0.0,  minVal = 0, maxVal = 90, vary = False)
modelRef.setParam("magDensity1", 1.05e-07,  minVal = -3e-6, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity2", 9e-08,  minVal = -3e-6, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity3", 1.5e-07,  minVal = -3e-6, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity4", 1.8e-07,  minVal = -3e-6, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity5", 2.0099999999999999e-07,  minVal = -3e-6, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity6", 2.0099999999999999e-07,  minVal = -3e-6, maxVal = 3e-06, vary = True)
modelRef.setParam("polarizationEfficiency", 1.0,  minVal = 0.95, maxVal = 1, vary = False)
modelRef.combineParameters('magSldCore', 'magSldShell')

modelRef.setConstantParam("bg", 1.76e-05)
modelRef.setConstantParam("roughness", 11.98)
modelRef.setConstantParam("roughnessSlope", 0.041)
modelRef.setConstantParam("dSpacer", 37.1)

modelRef.setConstantParam("packingDensity1", 1.112)
modelRef.setConstantParam("packingDensity2", 1.116)
modelRef.setConstantParam("packingDensity3", 0.9560000000000001)
modelRef.setConstantParam("packingDensity4", 0.854)
modelRef.setConstantParam("packingDensity5", 0.8260000000000001)
modelRef.setConstantParam("packingDensity6", 0.2)
modelRef.setConstantParam("layerDistance1", -41.3)
modelRef.setConstantParam("layerDistance2", -29.299999999999997)
modelRef.setConstantParam("layerDistance3", -29.5)
modelRef.setConstantParam("layerDistance4", -32.0)
modelRef.setConstantParam("layerDistance5", -23.0)
modelRef.setConstantParam("layerDistance6", -19.2)
# modelRef.combineParameters('packingDensity1', 'packingDensity2')
# modelRef.combineParameters('packingDensity1', 'packingDensity3')
# modelRef.combineParameters('packingDensity1', 'packingDensity4')
# modelRef.combineParameters('packingDensity1', 'packingDensity5')
# modelRef.combineParameters('layerDistance1', 'layerDistance2')
# modelRef.combineParameters('layerDistance1', 'layerDistance3')
# modelRef.combineParameters('layerDistance1', 'layerDistance4')
# modelRef.combineParameters('layerDistance1', 'layerDistance5')

modelRef.setConstantParam("sldSpacer", 1.264e-06)

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