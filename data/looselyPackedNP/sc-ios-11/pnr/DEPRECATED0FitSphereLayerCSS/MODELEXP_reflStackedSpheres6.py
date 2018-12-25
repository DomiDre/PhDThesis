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

modelRef.setParam("bg", 2.7400000000000002e-05,  minVal = 0.0, maxVal = 0.0001, vary = True)
modelRef.setParam("roughness", 12.44,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.0419,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("dSpacer", 0.0,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("sldSpacer", 4.186e-06,  minVal = -inf, maxVal = inf, vary = False)

modelRef.setParam("packingDensity1", 0.988,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 1.054,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.894,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.798,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.762,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.146,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("layerDistance1", -1.3713386773606118,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -27.2,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -25.099999999999998,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -25.03592493218232,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -12.5,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", 1.0,  minVal = -50, maxVal = 50, vary = True)
# modelRef.setParam("bg", 0.00020999999999999998,  minVal = 0.0, maxVal = 0.001, vary = False)
# modelRef.setParam("roughness", 1.04,  minVal = 0.0, maxVal = 20, vary = False)
# modelRef.setParam("roughnessSlope", 0.0,  minVal = 0.0, maxVal = 0.1, vary = False)
# modelRef.setParam("dSpacer", 13.700000000000001,  minVal = 0, maxVal = 100, vary = True)

# modelRef.setParam("packingDensity1", 0.9659414219800899,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("packingDensity2", 1.0486015784643499,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("packingDensity3", 0.8983715379312163,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("packingDensity4", 0.8062136751500585,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("packingDensity5", 0.776,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("packingDensity6", 0.15800584438626586,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("layerDistance1", -1.3762866656055621,  minVal = -50, maxVal = 50, vary = True)
# modelRef.setParam("layerDistance2", -27.4,  minVal = -50, maxVal = 50, vary = True)
# modelRef.setParam("layerDistance3", -25.4,  minVal = -50, maxVal = 50, vary = True)
# modelRef.setParam("layerDistance4", -25.069313914711564,  minVal = -50, maxVal = 50, vary = True)
# modelRef.setParam("layerDistance5", -11.917932748843526,  minVal = -50, maxVal = 50, vary = True)
# modelRef.setParam("layerDistance6", -0.5999999999999943,  minVal = -50, maxVal = 50, vary = True)

# modelRef.setParam("packingDensity1", 1.1280000000000001,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("packingDensity2", 1.04,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("packingDensity3", 0.902,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("packingDensity4", 1.03,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("packingDensity5", 1.086,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("packingDensity6", 0.15,  minVal = 0.0, maxVal = 2.0, vary = True)
# modelRef.setParam("layerDistance1", 0.0,  minVal = -50, maxVal = 0, vary = False)
# modelRef.setParam("layerDistance2", -9.432853413443468,  minVal = -50, maxVal = 0, vary = True)
# modelRef.setParam("layerDistance3", -24.25,  minVal = -50, maxVal = 0, vary = True)
# modelRef.setParam("layerDistance4", -21.549999999999997,  minVal = -50, maxVal = 0, vary = True)
# modelRef.setParam("layerDistance5", -34.05,  minVal = -50, maxVal = 0, vary = True)
# modelRef.setParam("layerDistance6", -0.04999999999999716,  minVal = -50, maxVal = 0, vary = True)

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
modelRef.setConstantParam("sldSpacer", 4.186e-06)

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