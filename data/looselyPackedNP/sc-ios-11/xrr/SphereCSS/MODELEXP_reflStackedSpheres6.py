#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import CmplxSphereCSSStacked6Spacer, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
# expRef.setResiduumFormula('log chi2 noError')
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0.035, 0.4)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S14.xye')
# dataRef.sliceDomain(0, 0.15)
dataRef.plotData()

modelRef = app.setModel(CmplxSphereCSSStacked6Spacer, [InstrumentalResolution])
modelRef.setParam("bg", 1.4000000000000001e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 3.46,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.025400000000000002,  minVal = 0.0, maxVal = 0.1, vary = True)

modelRef.setParam("packingDensity1", 0.642,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 0.8244583969291223,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.852,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.852,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.774536171960156,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.184,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("layerDistance1", -19.4,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -30.9,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -27.0,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -24.4,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -17.9,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -6.099999999999994,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("i0", 1.16,  minVal = 0, maxVal = 2, vary = False)
modelRef.setParam("dSpacer", 56.400000000000006,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("dWavelength", 0.020800000000000003,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("reSldSpacer", 7.650000000000001e-06,  minVal = 0, maxVal = 3e-05, vary = True)
# modelRef.combineParameters('packingDensity1', 'packingDensity2')
# modelRef.combineParameters('packingDensity1', 'packingDensity3')
# modelRef.combineParameters('packingDensity1', 'packingDensity4')
# modelRef.combineParameters('packingDensity1', 'packingDensity5')
# modelRef.combineParameters('layerDistance1', 'layerDistance2')
# modelRef.combineParameters('layerDistance1', 'layerDistance3')
# modelRef.combineParameters('layerDistance1', 'layerDistance4')
# modelRef.combineParameters('layerDistance1', 'layerDistance5')

modelRef.setConstantParam("r", 52.90)
modelRef.setConstantParam("dShell", 0)
modelRef.setConstantParam("dSurfactant", 14.7)
modelRef.setConstantParam('reSldCore', sld_xray_D8['Magnetite'].real)
modelRef.setConstantParam('reSldShell', sld_xray_D8['Magnetite'].real)
modelRef.setConstantParam('reSldSurfactant', sld_xray_D8['Oleic Acid'].real)
modelRef.setConstantParam('reSldSubstrate', sld_xray_D8['Silicon'].real)
modelRef.setConstantParam('reSldBackground', 0e-6)

modelRef.setConstantParam('imSldCore', 0)
modelRef.setConstantParam('imSldShell', 0)
modelRef.setConstantParam('imSldSpacer', 0)
modelRef.setConstantParam('imSldSurfactant', 0)
modelRef.setConstantParam('imSldSubstrate', 0)
modelRef.setConstantParam('imSldBackground', 0)

# D8 properties
# modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0)
modelRef.setConstantParam('wavelength', 1.5418)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 900, 300))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()