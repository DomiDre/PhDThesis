#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import SphereCSStacked6Spacer, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0, 0.15)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S14.xye')
dataRef.sliceDomain(0, 0.3)
dataRef.plotData()

modelRef = app.setModel(SphereCSStacked6Spacer, InstrumentalResolution)
modelRef.setParam("bg", 1.9000000000000002e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 6.18,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.01,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("packingDensity1", 0.309,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity2", 0.401,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity3", 0.5070061844298268,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity4", 0.5650927005223263,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity5", 0.5860148630740047,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity6", 0.23900000000000002,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("layerDistance1", -16.09620040163322,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -17.789574484066165,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -15.787342254536917,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -17.981671200148305,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -13.099020156014696,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -12.0,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("dSpacer", 50.70379991318038,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 7.380000000000001e-06,  minVal = 0, maxVal = 3e-05, vary = True)
modelRef.setParam("dWavelength", 0.021929479915969087,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("r", 54.1)
modelRef.setConstantParam("d", 18.2)
modelRef.setConstantParam("sigR", 0.0545)
modelRef.setConstantParam('sldCore', sld_xray_D8['Magnetite'].real)
modelRef.setConstantParam('sldShell', sld_xray_D8['Oleic Acid'].real)
modelRef.setConstantParam('sldSubstrate', sld_xray_D8['Silicon'].real)
modelRef.setConstantParam('sldBackground', 0e-6)

# D8 properties
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0)
modelRef.setConstantParam('wavelength', 1.5418)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 700, 150))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()