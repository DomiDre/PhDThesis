#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import SphereCSSStacked6Spacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S14.xye')
dataRef.sliceDomain(0, 0.3)
dataRef.plotData()

modelRef = app.setModel(SphereCSSStacked6Spacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 1.6000000000000001e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 3.2800000000000002,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.0207,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("packingDensity1", 0.6980000000000001,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity2", 0.6980000000000001,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity3", 0.6980000000000001,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity4", 0.6980000000000001,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity5", 0.6980000000000001,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity6", 0.6980000000000001,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("layerDistance1", -24.799999999999997,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -24.599999999999998,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance3", -24.599999999999998,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance4", -24.599999999999998,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance5", -24.599999999999998,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance6", -13.399999999999999,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("dSpacer", 47.15717711086203,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 2.9190000000000003e-05,  minVal = 0, maxVal = 3e-05, vary = True)
modelRef.setParam("dWavelength", 0.0097,  minVal = 0, maxVal = 0.1, vary = False)


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
modelRef.setConstantParam("sigR", 0.0545)
modelRef.setConstantParam('sldCore', sld_xray_D8['Wustite'].real)
modelRef.setConstantParam('sldShell', sld_xray_D8['Magnetite'].real)
modelRef.setConstantParam('sldSurfactant', sld_xray_D8['Oleic Acid'].real)
modelRef.setConstantParam('sldSubstrate', sld_xray_D8['Silicon'].real)
modelRef.setConstantParam('sldBackground', 0e-6)

# D8 properties
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0)
modelRef.setConstantParam('wavelength', 1.5418)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 900, 300))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()