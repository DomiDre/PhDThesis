#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import SphereCSSStacked6Spacer, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(PolarizedReflectometry)
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0.007, 0.12)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../../data/30Kfiles/footprint_correct/ES_S14_30K_730mT_ZFC_reduced_in_x_ai_uu_qz_I_fcorrected.xye', ['p'])
dataRef.loadFromFile('../../../data/30Kfiles/footprint_correct/ES_S14_30K_730mT_ZFC_reduced_in_x_ai_dd_qz_I_fcorrected.xye', ['m'])
dataRef.plotData()

modelRef = app.setModel(SphereCSSStacked6Spacer, [Magnetic, InstrumentalResolution])

modelRef.setParam("magSldCore", 1.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.setParam("magSldShell", 1.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.setParam("gamma", 0.0,  minVal = -inf, maxVal = inf, vary = False)
modelRef.setParam("magDensity1", 6.391579556777325e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity2", 6.63e-07,  minVal = 0, maxVal = 3e-06, vary = False)
modelRef.setParam("magDensity3", 6.63e-07,  minVal = 0, maxVal = 3e-06, vary = False)
modelRef.setParam("magDensity4", 6.63e-07,  minVal = 0, maxVal = 3e-06, vary = False)
modelRef.setParam("magDensity5", 6.63e-07,  minVal = 0, maxVal = 3e-06, vary = False)
modelRef.setParam("magDensity6", 6.63e-07,  minVal = 0, maxVal = 3e-06, vary = False)
modelRef.setParam("polarizationEfficiency", 1.0,  minVal = 0.95, maxVal = 1, vary = False)
modelRef.combineParameters('magSldCore', 'magSldShell')

modelRef.setConstantParam("bg", 1.76e-05)
modelRef.setConstantParam("roughness", 16.56)
modelRef.setConstantParam("roughnessSlope", 0.0237)
modelRef.setConstantParam("dSpacer", 30.4)
modelRef.setConstantParam("gamma", 0.0)
modelRef.setConstantParam("packingDensity1", 1.224)
modelRef.setConstantParam("packingDensity2", 1.122)
modelRef.setConstantParam("packingDensity3", 0.93)
modelRef.setConstantParam("packingDensity4", 0.792)
modelRef.setConstantParam("packingDensity5", 0.716)
modelRef.setConstantParam("packingDensity6", 0.132)
modelRef.setConstantParam("layerDistance1", -47.5)
modelRef.setConstantParam("layerDistance2", -26.0)
modelRef.setConstantParam("layerDistance3", -28.2)
modelRef.setConstantParam("layerDistance4", -31.94184086089053)
modelRef.setConstantParam("layerDistance5", -26.299999999999997)
modelRef.setConstantParam("layerDistance6", -21.599999999999998)

modelRef.combineParameters('magDensity1', 'magDensity2')
modelRef.combineParameters('magDensity1', 'magDensity3')
modelRef.combineParameters('magDensity1', 'magDensity4')
modelRef.combineParameters('magDensity1', 'magDensity5')
modelRef.combineParameters('magDensity1', 'magDensity6')

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