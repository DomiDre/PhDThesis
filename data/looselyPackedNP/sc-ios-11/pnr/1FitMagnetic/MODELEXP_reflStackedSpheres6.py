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

modelRef.setParam("magSldCore", 5.998823268183986e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magSldShell", 6e-07,  minVal = 0, maxVal = 3e-06, vary = False)
modelRef.combineParameters('magSldCore', 'magSldShell')

modelRef.setConstantParam("bg", 2.7400000000000002e-05)
modelRef.setConstantParam("roughness", 6.0200000000000005)
modelRef.setConstantParam("roughnessSlope", 0.0509221190616767)
modelRef.setConstantParam("dSpacer", 49.82578424516434)
modelRef.setConstantParam("sldSpacer", 1.264e-06)

modelRef.setConstantParam("packingDensity1", 0.9625419041278631)
modelRef.setConstantParam("packingDensity2", 1.0331064120708469)
modelRef.setConstantParam("packingDensity3", 0.8938228715987308)
modelRef.setConstantParam("packingDensity4", 0.7937718969093424)
modelRef.setConstantParam("packingDensity5", 0.7829379596821477)
modelRef.setConstantParam("packingDensity6", 0.182)
modelRef.setConstantParam("layerDistance1", -22.173304860528965)
modelRef.setConstantParam("layerDistance2", -28.115790240531783)
modelRef.setConstantParam("layerDistance3", -25.78167493733926)
modelRef.setConstantParam("layerDistance4", -26.26680085810748)
modelRef.setConstantParam("layerDistance5", -14.526774110868466)
modelRef.setConstantParam("layerDistance6", -1.7999999999999972)


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