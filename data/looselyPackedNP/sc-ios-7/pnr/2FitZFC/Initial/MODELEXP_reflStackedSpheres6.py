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
modelRef.setParam("bg", 1.7000000000000002e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 9.60706155435272,  minVal = 0.0, maxVal = 40, vary = True)
modelRef.setParam("roughnessSlope", 0.0004242190508670918,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("packingDensity1", 0.8094435466098029,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 0.6889707737681452,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.6178498513937996,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.612296893901263,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.6496893761538566,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.6281554882604345,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity7", 0.6076174324895113,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity8", 0.5677610415585745,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity9", 0.5151829912424655,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity10", 0.4043711162261666,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity11", 0.0,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("layerDistance1", -7.099999999999994,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance2", -19.299999999999997,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance3", -28.299999999999997,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance4", -29.7,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance5", -26.9,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance6", -23.5,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance7", -22.099999999999998,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance8", -20.9,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance9", -20.799999999999997,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance10", -22.599999999999998,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance11", -48.0,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("dSpacer", 37.50041227348886,  minVal = 0, maxVal = 100, vary = False)
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