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
modelRef.setParam("bg", 7.000000000000001e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 6.3,  minVal = 0.0, maxVal = 20, vary = False)
modelRef.setParam("roughnessSlope", 0.0391,  minVal = 0.0, maxVal = 0.1, vary = False)
modelRef.setParam("packingDensity1", 0.584,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity2", 0.614,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity3", 0.634,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity4", 0.5700000000000001,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity5", 0.562,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity6", 0.738,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity7", 0.882,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity8", 0.994,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity9", 1.196,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity10", 0.74,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("packingDensity11", 0.0,  minVal = 0.0, maxVal = 2.0, vary = False)
modelRef.setParam("layerDistance1", -1.0999999999999943,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -5.8617450452949456,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -5.170454788813636,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -6.078595401306828,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -2.8884389868287528,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -4.440366418963237,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance7", -8.260072290189477,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance8", -9.395660229021807,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance9", 7.400000000000006,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance10", -6.899999999999999,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance11", -50.0,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("dSpacer", 47.900000000000006,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("sldSpacer", 1.98e-06,  minVal = 0, maxVal = 3e-05, vary = False)
modelRef.setParam("dWavelength", 0.0221,  minVal = 0, maxVal = 0.1, vary = False)


modelRef.setConstantParam("r", 34.88)
modelRef.setConstantParam("d", 14.7)
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