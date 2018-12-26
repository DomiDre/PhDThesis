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
expRef.setResiduumFormula('log chi2 noError')
# expRef.setFitRange(0, 0.15)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S17.xye')
# dataRef.sliceDomain(0, 0.15)
dataRef.plotData()
modelRef = app.setModel(SphereCSStacked11Spacer, [InstrumentalResolution])
modelRef.setParam("bg", 0.0,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 3.4294873389685474,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.0371,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("packingDensity1", 0.4891839060959611,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 0.480870149711789,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.5769966007374667,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.554,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.486,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.652,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity7", 0.868,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity8", 1.024,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity9", 1.094,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity10", 0.752,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity11", 0.0,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("layerDistance1", -13.648076919260014,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -8.527459219542465,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -10.720798104425121,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -14.117284444385213,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -9.960009437363418,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -8.899999999999999,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance7", -14.0,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance8", -13.600000000000001,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance9", -3.0999999999999943,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance10", -20.0,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance11", -50.0,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("dSpacer", 52.6,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("sldSpacer", 2.1600000000000005e-06,  minVal = 0, maxVal = 3e-05, vary = False)
modelRef.setParam("dWavelength", 0.0221,  minVal = 0, maxVal = 0.1, vary = False)


modelRef.setConstantParam("r", 35.4)
modelRef.setConstantParam("d", 16.9)
modelRef.setConstantParam('sldCore', sld_xray_D8['Magnetite'].real)
modelRef.setConstantParam('sldShell', sld_xray_D8['Oleic Acid'].real)
modelRef.setConstantParam('sldSubstrate', sld_xray_D8['Silicon'].real)
modelRef.setConstantParam('sldBackground', 0e-6)

# D8 properties
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0)
modelRef.setConstantParam('wavelength', 1.5418)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 1200, 500))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()