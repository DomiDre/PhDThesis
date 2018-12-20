#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import SimultaneousXRNR
from modelexp.models.reflectometry import SphereCSSStacked6Spacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(SimultaneousXRNR)
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S14.xye', ['xrr'])
dataRef.loadFromFile('../ES_S14_300K_4mT_refl_corrected_combined.xy', ['nr'])
dataRef.sliceDomain(0, 0.2)
dataRef.plotData()

modelRef = app.setModel(SphereCSSStacked6Spacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("roughness", 2.0,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.04527766837491883,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("packingDensity1", 0.692045496261036,  minVal = 0.0, maxVal = 2, vary = True)
modelRef.setParam("packingDensity2", 0.7130813880603158,  minVal = 0.0, maxVal = 2, vary = True)
modelRef.setParam("packingDensity3", 0.7864432333038938,  minVal = 0.0, maxVal = 2, vary = True)
modelRef.setParam("packingDensity4", 0.9002974191813538,  minVal = 0.0, maxVal = 2, vary = True)
modelRef.setParam("packingDensity5", 1.0,  minVal = 0.0, maxVal = 2, vary = True)
modelRef.setParam("packingDensity6", 0.095,  minVal = 0.0, maxVal = 2, vary = True)
modelRef.setParam("layerDistance1", -25.38883083109284,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -31.46301925928406,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -26.554828654121604,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -20.89393517738242,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -18.051248894006644,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", 25.5,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("dSpacer", 48.011175954730284,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer_xrr", 1.9380000000000004e-05,  minVal = 0, maxVal = 3e-05, vary = True)
modelRef.setParam("sldSpacer_nr", 1.724313401634316e-06,  minVal = 0, maxVal = 3e-05, vary = True)


# modelRef.combineParameters('packingDensity1', 'packingDensity2')
# modelRef.combineParameters('packingDensity1', 'packingDensity3')
# modelRef.combineParameters('packingDensity1', 'packingDensity4')
# modelRef.combineParameters('packingDensity1', 'packingDensity5')
# modelRef.combineParameters('layerDistance1', 'layerDistance2')
# modelRef.combineParameters('layerDistance1', 'layerDistance3')
# modelRef.combineParameters('layerDistance1', 'layerDistance4')
# modelRef.combineParameters('layerDistance1', 'layerDistance5')

modelRef.setParam("dWavelength_xrr", 0.0,  minVal = 0, maxVal = 0.1, vary = False)
modelRef.setParam("dTheta_nr", 0.0,  minVal = 0, maxVal = 0.001, vary = False)


modelRef.setConstantParam('sldSubstrate_nr', 2.072e-6)#, min=1.5e-6, max=2.5e-6, vary=True)
modelRef.setConstantParam('sldSubstrate_xrr', sld_xray_D8['Silicon'].real)#, min=15e-6, max=25e-6, vary=True)


modelRef.setConstantParam("r", 54.1-16.16)
modelRef.setConstantParam("dShell", 16.16)
modelRef.setConstantParam("dSurfactant", 18.2)
modelRef.setConstantParam('sldCore_xrr', sld_xray_D8['Wustite'].real)
modelRef.setConstantParam('sldShell_xrr', sld_xray_D8['Magnetite'].real)
modelRef.setConstantParam('sldSurfactant_xrr', sld_xray_D8['Oleic Acid'].real)
modelRef.setConstantParam('sldBackground_xrr', 0e-6)


modelRef.setConstantParam('sldCore_nr', 8.34e-06)
modelRef.setConstantParam('sldShell_nr',7e-06)
modelRef.setConstantParam('sldSurfactant_nr', 0.078e-6)
modelRef.setConstantParam('sldBackground_nr', 0e-6)

# D8 properties
modelRef.setConstantParam("i0_xrr", 1)
modelRef.setConstantParam("bg_xrr", 1e-6)
modelRef.setConstantParam("dTheta_xrr", 0.0)
modelRef.setConstantParam('wavelength_xrr', 1.5418)

# SuperADAM
modelRef.setConstantParam("i0_nr", 1)
modelRef.setConstantParam("bg_nr", 2e-5)
modelRef.setConstantParam("dWavelength_nr", 0.005)
modelRef.setConstantParam('wavelength_nr', 5.14)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 900, 300))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()