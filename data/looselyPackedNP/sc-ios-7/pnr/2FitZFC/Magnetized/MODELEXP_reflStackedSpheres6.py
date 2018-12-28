#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import SphereCSStacked11Spacer, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(PolarizedReflectometry)
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0.005, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../data/footprint_corrected/ES_S17_30K_ZFC_7300Oe_reduced_in_x_ai_uu_masked_qz_I_fcorrected.xye', ['p'])
dataRef.loadFromFile('../../data/footprint_corrected/ES_S17_30K_ZFC_7300Oe_reduced_in_x_ai_du_masked_qz_I_fcorrected.xye', ['m'])
dataRef.sliceDomain(0.007, 1)
dataRef.plotData()
modelRef = app.setModel(SphereCSStacked11Spacer, [Magnetic, InstrumentalResolution])



modelRef.setConstantParam("bg", 1.991524406692036e-6)
modelRef.setConstantParam("roughness", 9.18540654563359)
modelRef.setConstantParam("roughnessSlope", 0.0)
modelRef.setConstantParam("packingDensity1", 0.8562202890906117)
modelRef.setConstantParam("packingDensity2", 0.731242118376412)
modelRef.setConstantParam("packingDensity3", 0.6558944537567484)
modelRef.setConstantParam("packingDensity4", 0.6482607748543772)
modelRef.setConstantParam("packingDensity5", 0.6893359849513783)
modelRef.setConstantParam("packingDensity6", 0.6680603297349672)
modelRef.setConstantParam("packingDensity7", 0.646049087470722)
modelRef.setConstantParam("packingDensity8", 0.6046270892992822)
modelRef.setConstantParam("packingDensity9", 0.550193080659303)
modelRef.setConstantParam("packingDensity10", 0.42919089649595166)
modelRef.setConstantParam("packingDensity11", 0.0)
modelRef.setConstantParam("layerDistance1", -8.910442957879866)
modelRef.setConstantParam("layerDistance2", -23.841057882542927)
modelRef.setConstantParam("layerDistance3", -32.7)
modelRef.setConstantParam("layerDistance4", -34.2)
modelRef.setConstantParam("layerDistance5", -31.358534610073136)
modelRef.setConstantParam("layerDistance6", -27.86384522338104)
modelRef.setConstantParam("layerDistance7", -26.46564846004602)
modelRef.setConstantParam("layerDistance8", -25.207166473090997)
modelRef.setConstantParam("layerDistance9", -25.024149758015145)
modelRef.setConstantParam("layerDistance10", -26.866355646135105)
modelRef.setConstantParam("layerDistance11", -50.0)
modelRef.setConstantParam("dSpacer", 36.389590732585496)
modelRef.setConstantParam("sldSpacer", 0.0)

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