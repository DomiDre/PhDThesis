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
dataRef.sliceDomain(0, 0.15)
dataRef.plotData()

modelRef = app.setModel(SphereCSSStacked6Spacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 1.6000000000000001e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 5.525314257438043,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.0031000000000000003,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("dSpacer", 60.17995631052854,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 6.810481395294044e-06,  minVal = 0, maxVal = 3e-05, vary = True)
modelRef.setParam("dWavelength", 0.0219,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setParam("packingDensity1", 0.6421115617376807,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 0.846,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.8541973191208986,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.8160000000000001,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.7621072802354298,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.20800000000000002,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("layerDistance1", -27.06997351917375,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -34.47209837266813,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -31.571849806206544,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -33.39212400668635,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -29.89975565378582,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -22.599999999999998,  minVal = -50, maxVal = 50, vary = True)

modelRef.setParam("dSpacer", 60.17995631052854,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 6.810481395294044e-06,  minVal = 0, maxVal = 3e-05, vary = True)
modelRef.setParam("dWavelength", 0.0219,  minVal = 0, maxVal = 0.1, vary = True)


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