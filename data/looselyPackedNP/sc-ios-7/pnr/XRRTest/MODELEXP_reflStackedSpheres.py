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
modelRef.setParam("bg", 2.46e-05,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 7.140000000000001,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.0397,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("packingDensity1", 0.902,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 0.768,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.634,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.5680000000000001,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.56,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.58,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity7", 0.54,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity8", 0.602,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity9", 0.728,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity10", 0.00032255745329301533,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity11", 0.0,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("layerDistance1", 0.10000000000000142,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -6.399999999999999,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -8.199999999999996,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -9.799999999999997,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -11.0,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -15.0,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance7", -21.4,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance8", -24.9,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance9", -13.299999999999997,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance10", -50.0,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance11", -50.0,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("dSpacer", 46.2,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 0.0,  minVal = 0, maxVal = 3e-05, vary = True)


modelRef.setConstantParam("r", 35.4)
modelRef.setConstantParam("d", 16.9)

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