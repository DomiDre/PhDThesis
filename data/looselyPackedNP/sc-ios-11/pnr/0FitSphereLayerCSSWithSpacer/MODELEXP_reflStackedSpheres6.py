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

dataRef.loadFromFile('../data/300Kfiles/footprint_correct/ES_S14_300K_4mT_refl_uu_fcorrected.xye', ['p'])
dataRef.loadFromFile('../data/300Kfiles/footprint_correct/ES_S14_300K_4mT_refl_du_fcorrected.xye', ['m'])
dataRef.sliceDomain(0, 0.15)
dataRef.plotData()

modelRef = app.setModel(SphereCSSStacked6Spacer, [Magnetic, InstrumentalResolution])

modelRef.setParam("bg", 2.7400000000000002e-05,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 6.0200000000000005,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.0509221190616767,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("dSpacer", 49.82578424516434,  minVal = 0, maxVal = 100, vary = True)

modelRef.setParam("packingDensity1", 0.9625419041278631,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 1.0331064120708469,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.8938228715987308,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.7937718969093424,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.7829379596821477,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.182,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("layerDistance1", -22.173304860528965,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -28.115790240531783,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -25.78167493733926,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -26.26680085810748,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -14.526774110868466,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -1.7999999999999972,  minVal = -50, maxVal = 50, vary = True)

# modelRef.combineParameters('packingDensity1', 'packingDensity2')
# modelRef.combineParameters('packingDensity1', 'packingDensity3')
# modelRef.combineParameters('packingDensity1', 'packingDensity4')
# modelRef.combineParameters('packingDensity1', 'packingDensity5')
# modelRef.combineParameters('layerDistance1', 'layerDistance2')
# modelRef.combineParameters('layerDistance1', 'layerDistance3')
# modelRef.combineParameters('layerDistance1', 'layerDistance4')
# modelRef.combineParameters('layerDistance1', 'layerDistance5')

modelRef.setConstantParam("magSldCore", 0)
modelRef.setConstantParam("magSldShell", 0)
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