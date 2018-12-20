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
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0.032, 0.15)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S17.xye')
dataRef.sliceDomain(0, 0.15)
dataRef.plotData()
modelRef = app.setModel(SphereCSStacked11Spacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 0.0,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 6.98,  minVal = 0.0, maxVal = 20, vary = False)
modelRef.setParam("roughnessSlope", 0.0357,  minVal = 0.0, maxVal = 0.1, vary = False)
modelRef.setParam("packingDensity1", 0.554,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 0.524,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 0.6431716758998636,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 0.6960000000000001,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.686,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.758,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity7", 0.882,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity8", 1.0421854889754747,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity9", 1.166,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity10", 1.068,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity11", 0.646,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("layerDistance1", -13.5,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -7.599999999999994,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -10.099999999999994,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -13.100000000000001,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -11.399999999999999,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -10.299999999999997,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance7", -11.805687247201163,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance8", -11.5,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance9", 1.1000000000000014,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance10", -15.399999999999999,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance11", -8.699999999999996,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("dSpacer", 52.6,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("sldSpacer", 2.1600000000000005e-06,  minVal = 0, maxVal = 3e-05, vary = False)
modelRef.setParam("dWavelength", 0.0218,  minVal = 0, maxVal = 0.1, vary = False)
modelRef.setParam("qShift", 0.0,  minVal = -0.1, maxVal = 0.1, vary = False)


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