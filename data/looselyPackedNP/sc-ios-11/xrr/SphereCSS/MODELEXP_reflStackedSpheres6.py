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
modelRef.setParam("bg", 3.4000000000000005e-06,  minVal = 0.0, maxVal = 0.0001, vary = True)
modelRef.setParam("roughness", 3.5,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.012700000000000001,  minVal = 0.0, maxVal = 0.1, vary = True)

modelRef.setParam("packingDensity1", 0.684,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 0.882,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.864,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.796,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.722,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.154,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("layerDistance1", -22.099999999999998,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -33.099999999999994,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -30.33206387099186,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -33.878287222529785,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -30.5,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -18.2,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("i0", 1.16,  minVal = 0, maxVal = 2, vary = False)
modelRef.setParam("dSpacer", 53.5,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("dWavelength", 0.0196,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("reSldSpacer", 7.620000000000001e-06,  minVal = 0, maxVal = 3e-05, vary = True)
# modelRef.combineParameters('packingDensity1', 'packingDensity2')
# modelRef.combineParameters('packingDensity1', 'packingDensity3')
# modelRef.combineParameters('packingDensity1', 'packingDensity4')
# modelRef.combineParameters('packingDensity1', 'packingDensity5')
# modelRef.combineParameters('layerDistance1', 'layerDistance2')
# modelRef.combineParameters('layerDistance1', 'layerDistance3')
# modelRef.combineParameters('layerDistance1', 'layerDistance4')
# modelRef.combineParameters('layerDistance1', 'layerDistance5')

modelRef.setConstantParam("r", 54-16)
modelRef.setConstantParam("dShell", 16)
modelRef.setConstantParam("dSurfactant", 18.2)
modelRef.setConstantParam('reSldCore', sld_xray_D8['Wustite'].real)
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