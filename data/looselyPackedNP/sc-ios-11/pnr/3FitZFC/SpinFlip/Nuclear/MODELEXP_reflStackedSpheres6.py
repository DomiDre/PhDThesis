#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometrySF
from modelexp.models.reflectometry import SphereCSSStacked6Spacer, InstrumentalResolution, MagneticSF
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(PolarizedReflectometrySF)
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../../data/30Kfiles/footprint_correct/ES_S14_30K_2mT_ZFC_reduced_in_x_ai_uu_qz_I_fcorrected.xye', ['p'])
dataRef.loadFromFile('../../../data/30Kfiles/footprint_correct/ES_S14_30K_2mT_ZFC_reduced_in_x_ai_dd_qz_I_fcorrected.xye', ['m'])
dataRef.loadFromFile('../../../data/30Kfiles/footprint_correct/ES_S14_30K_2mT_ZFC_reduced_in_x_ai_du_qz_I_fcorrected.xye', ['sf'])
dataRef.plotData()

modelRef = app.setModel(SphereCSSStacked6Spacer, [MagneticSF, InstrumentalResolution])

modelRef.setParam("polarizationEfficiency", 0.98325,  minVal = 0.95, maxVal = 1, vary = False)
modelRef.setParam("bg", 1.76e-05,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 11.98,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.041,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("dSpacer", 37.1,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("gamma", 0.0,  minVal = 0, maxVal = 90, vary = False)

modelRef.setParam("packingDensity1", 1.112,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 1.116,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.9560000000000001,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.854,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.8260000000000001,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.2,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("layerDistance1", -41.3,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -29.299999999999997,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -29.5,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -32.0,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -23.0,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -19.2,  minVal = -50, maxVal = 50, vary = True)

modelRef.setConstantParam("magDensity1", 6.73817567637411e-07)
modelRef.setConstantParam("magDensity2", 5.420457054847503e-07)
modelRef.setConstantParam("magDensity3", 6.867877697721098e-07)
modelRef.setConstantParam("magDensity4", 8.773843209268112e-07)
modelRef.setConstantParam("magDensity5", 1.10497667398459e-06)
modelRef.setConstantParam("magDensity6", 1.091804631640173e-06)
# modelRef.combineParameters('packingDensity1', 'packingDensity2')
# modelRef.combineParameters('packingDensity1', 'packingDensity3')
# modelRef.combineParameters('packingDensity1', 'packingDensity4')
# modelRef.combineParameters('packingDensity1', 'packingDensity5')
# modelRef.combineParameters('layerDistance1', 'layerDistance2')
# modelRef.combineParameters('layerDistance1', 'layerDistance3')
# modelRef.combineParameters('layerDistance1', 'layerDistance4')
# modelRef.combineParameters('layerDistance1', 'layerDistance5')

modelRef.setConstantParam("magSldCore", 1)
modelRef.setConstantParam("magSldShell", 1)
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