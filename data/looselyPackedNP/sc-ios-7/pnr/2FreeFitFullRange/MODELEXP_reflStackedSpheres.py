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
modelRef.setParam("bg", 2.46e-05,  minVal = 0.0, maxVal = 0.0001, vary = True)
modelRef.setParam("roughness", 14.540000000000001,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.0,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("packingDensity1", 0.992,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 0.774,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.598,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.49,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.454,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.5,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity7", 0.540542504836051,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity8", 0.552,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity9", 0.512,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity10", 0.354,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity11", 0.0,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("layerDistance1", -8.799999999999997,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -0.09999999999999432,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -6.299999999999997,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -14.5,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -22.599999999999998,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -25.9,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance7", -24.599999999999998,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance8", -24.4,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance9", -26.799999999999997,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance10", -32.0,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance11", -50.0,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("dSpacer", 60.800000000000004,  minVal = 0, maxVal = 100, vary = True)
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