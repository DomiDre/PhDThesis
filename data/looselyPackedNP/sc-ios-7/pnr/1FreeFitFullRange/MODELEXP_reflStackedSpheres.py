#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import SphereCSStacked11Spacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0, 0.15)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES_S17_300K_4mT_refl_corrected_combined.xy')
dataRef.sliceDomain(0, 0.15)
dataRef.plotData()
modelRef = app.setModel(SphereCSStacked11Spacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 2.650093537763057e-05,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 9.56,  minVal = 0.0, maxVal = 20, vary = False)
modelRef.setParam("roughnessSlope", 0.026600000000000002,  minVal = 0.0, maxVal = 0.1, vary = False)
modelRef.setParam("packingDensity1", 0.8686337385343138,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity2", 0.7193376441396282,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity3", 0.5700000000000001,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity4", 0.442,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity5", 0.3,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity6", 0.4469170637549428,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity7", 0.5330438269157318,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity8", 0.5388015756636322,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity9", 0.5320628225313359,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity10", 0.538,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity11", 0.0,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("layerDistance1",  -0.8,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2",  -0.5835982510996516,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3",  -4.230599300899399,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4",  -11.5,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5",  -29.9,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6",  -30.520838382146238,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance7",  -17.299999999999997,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance8",  -16.1,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance9",  -19.599999999999998,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance10", -18.2,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance11", -48.0,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("dSpacer", 34.06652732893591,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("sldSpacer", 0.0,  minVal = 0, maxVal = 3e-05, vary = False)


modelRef.setConstantParam("r", 34.88)
modelRef.setConstantParam("d", 14.7)

modelRef.setConstantParam('sldCore', 7.00e-6)
modelRef.setConstantParam('sldShell', 0.078e-6)
modelRef.setConstantParam('sldSubstrate', 2.072e-6)
modelRef.setConstantParam('sldBackground', 0e-6)

# SADAM properties
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0003)
modelRef.setConstantParam("dWavelength", 0.0021)
modelRef.setConstantParam('wavelength', 5.14)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 1200, 500))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()