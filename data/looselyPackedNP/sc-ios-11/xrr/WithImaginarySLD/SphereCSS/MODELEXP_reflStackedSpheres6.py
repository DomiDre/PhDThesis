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
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0.0275, 0.15)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../transform_data/ES-S14.xye')
dataRef.plotData()

modelRef = app.setModel(CmplxSphereCSSStacked6Spacer, [InstrumentalResolution])
modelRef.setParam("bg", 1.6000000000000001e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 1.22,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.04600000000000001,  minVal = 0., maxVal = 0.1, vary = True)
modelRef.setParam("dSpacer", 0.0,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("dWavelength", 0.0001,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setParam("i0", 1.466,  minVal = 0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity1", 0.9520000000000001,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 0.9520000000000001,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity3", 0.9520000000000001,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity4", 0.9520000000000001,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity5", 0.9520000000000001,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity6", 0.0,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("layerDistance1", -25.099999999999998,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -33.3,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -28.0,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -22.9,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -19.5,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -50.0,  minVal = -50, maxVal = 50, vary = False)

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
modelRef.setConstantParam("reSldSpacer", 2.166e-05)
modelRef.setConstantParam('reSldSubstrate', sld_xray_D8['Silicon'].real)
modelRef.setConstantParam('reSldBackground', 0e-6)
modelRef.setConstantParam('imSldCore', sld_xray_D8['Wustite'].imag)
modelRef.setConstantParam('imSldShell', sld_xray_D8['Magnetite'].imag)
modelRef.setConstantParam('imSldSurfactant', sld_xray_D8['Oleic Acid'].imag)
modelRef.setConstantParam('imSldSubstrate', sld_xray_D8['Silicon'].imag)
modelRef.setConstantParam("imSldSpacer", -0.296e-6)
modelRef.setConstantParam('imSldBackground', 0e-6)
# D8 properties
modelRef.setConstantParam("dTheta", 0.0)
modelRef.setConstantParam('wavelength', 1.5418)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 700, 300))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()