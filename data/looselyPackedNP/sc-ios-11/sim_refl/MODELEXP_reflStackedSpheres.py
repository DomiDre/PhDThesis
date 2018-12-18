#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import SimultaneousXRNR
from modelexp.models.reflectometry import SphereCSStacked6Spacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8, sld_neutrons_5A
import numpy as np

app = App()
expRef = app.setExperiment(SimultaneousXRNR)
expRef.setResiduumFormula('log chi2')
# expRef.setFitRange(0, 0.15)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('./ES-S14.xye', ['xrr'])
dataRef.loadFromFile('./ES_S14_300K_4mT_refl_corrected_combined.xy', ['nr'])
dataRef.sliceDomain(0, 0.3)
dataRef.plotData()

modelRef = app.setModel(SphereCSStacked6Spacer, [InstrumentalResolution])
modelRef.setParam("roughness", 4.877694811706008,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.0,  minVal = 0.0, maxVal = 0.1, vary = False)
modelRef.setParam("packingDensity1", 0.6067308583505893,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity2", 0.5065346518380619,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity3", 0.3370066462904706,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity4", 0.21559886264119904,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity5", 0.145,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity6", 0.00571271604641882,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("layerDistance1", -19.799999999999997,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -30.323663505662413,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -29.510488056263167,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -30.448685122983925,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -24.843533585663835,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -50.0,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("dSpacer", 49.6,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer_xrr", 1.7938258331208492e-05,  minVal = 0, maxVal = 3e-05, vary = True)
modelRef.setParam("sldSpacer_nr", 1.6500000000000003e-06,  minVal = 0, maxVal = 3e-05, vary = False)

modelRef.setParam("dWavelength_xrr", 0.01,  minVal = 0, maxVal = 0.1, vary = False)
modelRef.setParam("dTheta_nr", 0.00039999999999999996,  minVal = 0, maxVal = 0.001, vary = False)


modelRef.setConstantParam('sldSubstrate_nr', 2.072e-6)#, min=1.5e-6, max=2.5e-6, vary=True)
modelRef.setConstantParam('sldSubstrate_xrr', sld_xray_D8['Silicon'].real)#, min=15e-6, max=25e-6, vary=True)


modelRef.setConstantParam("r", 54.1)
modelRef.setConstantParam("d", 18.2)
modelRef.setConstantParam("sigR", 0.0545)
modelRef.setConstantParam('sldCore_xrr', sld_xray_D8['Magnetite'].real)
modelRef.setConstantParam('sldShell_xrr', sld_xray_D8['Oleic Acid'].real)
modelRef.setConstantParam('sldBackground_xrr', 0e-6)

modelRef.setConstantParam('sldCore_nr', 7.00e-6)
modelRef.setConstantParam('sldShell_nr', 0.078e-6)
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