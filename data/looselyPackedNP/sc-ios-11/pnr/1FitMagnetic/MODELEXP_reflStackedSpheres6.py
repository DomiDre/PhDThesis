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
expRef.setFitRange(0, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../data/300Kfiles/footprint_correct/ES_S14_300K_500mT_refl_uu_fcorrected.xye', ['p'])
dataRef.loadFromFile('../data/300Kfiles/footprint_correct/ES_S14_300K_500mT_refl_du_fcorrected.xye', ['m'])
dataRef.sliceDomain(0, 0.15)
dataRef.plotData()

modelRef = app.setModel(SphereCSSStacked6Spacer, [Magnetic, InstrumentalResolution])

modelRef.setParam("magSldCore", 1.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.setParam("magSldShell", 1.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.setParam("gamma", 0.0,  minVal = 0, maxVal = 90, vary = False)
modelRef.setParam("magDensity1", 4.92e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity2", 4.65e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity3", 5.55e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity4", 8.01e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity5", 1.128e-06,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magDensity6", 9.51e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("polarizationEfficiency", 1.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.combineParameters('magSldCore', 'magSldShell')

modelRef.setConstantParam("bg", 2.7400000000000002e-05)
modelRef.setConstantParam("roughness", 5.606592778561598)
modelRef.setConstantParam("roughnessSlope", 0.05236432689354881)
modelRef.setConstantParam("dSpacer", 49.5998880211069)

modelRef.setConstantParam("packingDensity1", 0.9581500413420708)
modelRef.setConstantParam("packingDensity2", 1.028049007948123)
modelRef.setConstantParam("packingDensity3", 0.8898551100682931)
modelRef.setConstantParam("packingDensity4", 0.791481708455682)
modelRef.setConstantParam("packingDensity5", 0.7802481869652758)
modelRef.setConstantParam("packingDensity6", 0.1814358039752838)
modelRef.setConstantParam("layerDistance1", -17.733074425333115)
modelRef.setConstantParam("layerDistance2", -20.801833342650237)
modelRef.setConstantParam("layerDistance3", -18.427969256726474)
modelRef.setConstantParam("layerDistance4", -18.773680133279363)
modelRef.setConstantParam("layerDistance5", -6.880126130653785)
modelRef.setConstantParam("layerDistance6", 6.044419789481495)

modelRef.setConstantParam("sldSpacer", 1.264e-06)

modelRef.setConstantParam("r", 52.90)
modelRef.setConstantParam("dShell", 0)
modelRef.setConstantParam("dSurfactant", 14.7)
modelRef.setConstantParam('sldCore', 7.00e-6)
modelRef.setConstantParam('sldShell', 7.00e-6)
modelRef.setConstantParam('sldSurfactant', 0.078e-6)
modelRef.setConstantParam('sldSubstrate', 2.072e-6)
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