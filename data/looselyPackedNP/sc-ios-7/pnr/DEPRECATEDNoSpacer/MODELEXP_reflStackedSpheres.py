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
expRef.setFitRange(0, 0.15)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES_S17_300K_4mT_refl_corrected_combined.xy')
dataRef.sliceDomain(0, 0.15)
dataRef.plotData()
modelRef = app.setModel(SphereCSStacked11Spacer, [InstrumentalResolution])
modelRef.setParam("bg", 2.46e-05,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 19.289195650938236,  minVal = 0.0, maxVal = 50, vary = True)
modelRef.setParam("roughnessSlope", 0.005931644346408582,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("packingDensity1", 0.8785835693745353,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity2", 1.1016733533008936,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity3", 1.183028882051915,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity4", 1.1619627040118767,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity5", 0.9303407211709026,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity6", 0.6029189697435591,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity7", 0.9031663060051042,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity8", 0.8925301822098751,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("packingDensity9", 1.3516686618036546,  minVal = 0.0, maxVal = 2.0, vary = True)
modelRef.setParam("layerDistance1", 0.0,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance2", -11.536782363641592,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -10.306814596768831,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -8.926579794626491,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -13.44086246287872,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -34.110260672080926,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance7", -25.21857172874482,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance8", -0.498304795012551,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance9", 26.328940597140317,  minVal = -50, maxVal = 50, vary = True)

modelRef.setConstantParam("packingDensity10", 0.0)
modelRef.setConstantParam("packingDensity11", 0.0)
modelRef.setConstantParam("layerDistance10", 0.0)
modelRef.setConstantParam("layerDistance11", 0.0)
# modelRef.combineParameters('layerDistance2', 'layerDistance3')
# modelRef.combineParameters('layerDistance2', 'layerDistance4')
# modelRef.combineParameters('layerDistance2', 'layerDistance5')
# modelRef.combineParameters('layerDistance2', 'layerDistance6')
# modelRef.combineParameters('layerDistance2', 'layerDistance7')
# modelRef.combineParameters('layerDistance2', 'layerDistance8')
# modelRef.combineParameters('layerDistance2', 'layerDistance9')
# modelRef.combineParameters('layerDistance2', 'layerDistance10')
modelRef.setConstantParam("dSpacer", 0.0)
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