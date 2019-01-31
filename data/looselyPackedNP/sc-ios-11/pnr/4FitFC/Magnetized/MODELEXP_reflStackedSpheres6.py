#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import SphereCSSStacked6Spacer, InstrumentalResolution, Magnetic, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(PolarizedReflectometry)
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0.007, 0.12)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../data/30Kfiles/footprint_correct/ES_S14_30K_730mT_FC_reduced_in_x_ai_uu_qz_I_fcorrected.xye', ['p'])
dataRef.loadFromFile('../../data/30Kfiles/footprint_correct/ES_S14_30K_730mT_FC_reduced_in_x_ai_dd_qz_I_fcorrected.xye', ['m'])
dataRef.plotData()

modelRef = app.setModel(SphereCSSStacked6Spacer, [Magnetic, InstrumentalResolution, ShiftQ])

modelRef.setParam("magSldCore", 1.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.setParam("magSldShell", 1.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.setParam("magDensity1", 5.73e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity2", 5.04e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity3", 6.48e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity4", 9.18e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity5", 1.236e-06,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity6", 1.449e-06,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("polarizationEfficiency", 1.0,  minVal = 0.95, maxVal = 1, vary = False)
modelRef.combineParameters('magSldCore', 'magSldShell')

modelRef.setConstantParam("bg", 1.5e-05)
modelRef.setConstantParam("qShift", 5.1e-4)
modelRef.setConstantParam("roughness", 18.22)
modelRef.setConstantParam("roughnessSlope", 0.0185)
modelRef.setConstantParam("dSpacer", 37.3)
modelRef.setConstantParam("gamma", 0.0)

modelRef.setConstantParam("packingDensity1", 1.306)
modelRef.setConstantParam("packingDensity2", 1.136)
modelRef.setConstantParam("packingDensity3", 0.936)
modelRef.setConstantParam("packingDensity4", 0.792)
modelRef.setConstantParam("packingDensity5", 0.716)
modelRef.setConstantParam("packingDensity6", 0.14)
modelRef.setConstantParam("layerDistance1", -50.0)
modelRef.setConstantParam("layerDistance2", -15.8)
modelRef.setConstantParam("layerDistance3", -19.9)
modelRef.setConstantParam("layerDistance4", -24.1)
modelRef.setConstantParam("layerDistance5", -18.9)
modelRef.setConstantParam("layerDistance6", -15.9)

modelRef.setConstantParam("sldSpacer", 1.264e-06)

modelRef.setConstantParam("r", 52.90)
modelRef.setConstantParam("dShell", 0)
modelRef.setConstantParam("dSurfactant", 14.7)
modelRef.setConstantParam('sldCore', 7.00e-06)
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