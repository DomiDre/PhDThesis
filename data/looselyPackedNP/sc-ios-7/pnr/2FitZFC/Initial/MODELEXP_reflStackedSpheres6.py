#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import SphereCSStacked11Spacer, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0.005, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../data/footprint_corrected/ES_S17_30K_ZFC_7Oe_reduced_in_x_ai_uu_masked_qz_I_fcorrected.xye')
dataRef.sliceDomain(0.007, 1)
dataRef.plotData()
modelRef = app.setModel(SphereCSStacked11Spacer, [InstrumentalResolution])
modelRef.setParam("bg", 1.991524406692036e-06,  minVal = 0.0, maxVal = 0.0001, vary = True)
modelRef.setParam("roughness", 9.18540654563359,  minVal = 0.0, maxVal = 40, vary = True)
modelRef.setParam("roughnessSlope", 0.0,  minVal = 0.0, maxVal = 0.1, vary = False)
modelRef.setParam("packingDensity1", 0.8562202890906117,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 0.731242118376412,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.6558944537567484,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.6482607748543772,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.6893359849513783,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.6680603297349672,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity7", 0.646049087470722,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity8", 0.6046270892992822,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity9", 0.550193080659303,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity10", 0.42919089649595166,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity11", 0.0,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("layerDistance1", -8.910442957879866,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -23.841057882542927,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -32.7,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -34.2,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -31.358534610073136,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -27.86384522338104,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance7", -26.46564846004602,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance8", -25.207166473090997,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance9", -25.024149758015145,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance10", -26.866355646135105,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance11", -50.0,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("dSpacer", 36.389590732585496,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 0.0,  minVal = 0, maxVal = 3e-05, vary = False)


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