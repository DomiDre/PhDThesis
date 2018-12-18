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
# expRef.setFitRange(0, 0.15)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S14.xye')
dataRef.sliceDomain(0, 0.3)
dataRef.plotData()

modelRef = app.setModel(SphereCSStacked6Spacer, InstrumentalResolution)
modelRef.setParam("bg", 1.9000000000000002e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 6.066800341473227,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.017678953201082592,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("packingDensity1", 0.14955767074437687,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity2", 0.322,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity3", 0.462,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity4", 0.5750000000000001,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity5", 0.545124976077325,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity6", 0.116,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("layerDistance1", -49.6,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -33.9,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -20.599999999999998,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -20.099999999999998,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -11.199999999999996,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -33.3,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("dSpacer", 80.7,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 4.597738006638438e-06,  minVal = 0, maxVal = 3e-05, vary = True)
modelRef.setParam("dWavelength", 0.024300000000000002,  minVal = 0, maxVal = 0.1, vary = True)

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