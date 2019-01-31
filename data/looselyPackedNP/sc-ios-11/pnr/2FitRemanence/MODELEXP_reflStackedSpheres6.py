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

dataRef.loadFromFile('../data/300Kfiles/footprint_correct/ES_S14_300K_4mT_Remanence_refl_uu_fcorrected.xye', ['p'])
dataRef.loadFromFile('../data/300Kfiles/footprint_correct/ES_S14_300K_4mT_Remanence_refl_du_fcorrected.xye', ['m'])
dataRef.sliceDomain(0, 0.15)
dataRef.plotData()

modelRef = app.setModel(SphereCSSStacked6Spacer, [Magnetic, InstrumentalResolution])

modelRef.setParam("magSldCore", 7.726325704372262e-09,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magSldShell", 6e-09,  minVal = 0, maxVal = 3e-06, vary = False)
modelRef.combineParameters('magSldCore', 'magSldShell')


modelRef.setParam("bg", 2.7400000000000002e-05,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 6.62,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.0458,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("dSpacer", 57.1,  minVal = 0, maxVal = 100, vary = True)

modelRef.setParam("packingDensity1", 0.9580000000000001,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity2", 1.028,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity3", 0.888,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity4", 0.79,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity5", 0.78,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity6", 0.18,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("layerDistance1", -17.799999999999997,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance2", -20.9,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance3", -18.5,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance4", -18.799999999999997,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance5", -6.899999999999999,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance6", 6.0,  minVal = -50, maxVal = 50, vary = False)

# modelRef.combineParameters('packingDensity1', 'packingDensity2')
# modelRef.combineParameters('packingDensity1', 'packingDensity3')
# modelRef.combineParameters('packingDensity1', 'packingDensity4')
# modelRef.combineParameters('packingDensity1', 'packingDensity5')
# modelRef.combineParameters('layerDistance1', 'layerDistance2')
# modelRef.combineParameters('layerDistance1', 'layerDistance3')
# modelRef.combineParameters('layerDistance1', 'layerDistance4')
# modelRef.combineParameters('layerDistance1', 'layerDistance5')

modelRef.setConstantParam("sldSpacer", 1.264e-06)

modelRef.setConstantParam("r", 52.90)
modelRef.setConstantParam("dShell", 0)
modelRef.setConstantParam("dSurfactant", 14.7)
modelRef.setConstantParam('sldCore', 7.00e-6)
modelRef.setConstantParam('sldShell', 7.00e-6)
modelRef.setConstantParam('sldSurfactant', 0.078e-6)
modelRef.setConstantParam('sldSubstrate', 2.072e-6)
modelRef.setConstantParam('sldBackground', 0e-6)
modelRef.setConstantParam('magDensity1', 1)
modelRef.setConstantParam('magDensity2', 1)
modelRef.setConstantParam('magDensity3', 1)
modelRef.setConstantParam('magDensity4', 1)
modelRef.setConstantParam('magDensity5', 1)
modelRef.setConstantParam('magDensity6', 1)

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