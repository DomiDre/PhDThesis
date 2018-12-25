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
expRef.setFitRange(0, 0.15)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../data/footprint_correct300K/ES_S17_300K_500mT_refl_uu_fcorrected.xye', 'p')
dataRef.loadFromFile('../data/footprint_correct300K/ES_S17_300K_500mT_refl_du_fcorrected.xye', 'm')

dataRef.sliceDomain(0, 0.15)
dataRef.plotData()
modelRef = app.setModel(SphereCSStacked11Spacer, [Magnetic, InstrumentalResolution])


modelRef.setParam("magSldCore", 3e-09,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setParam("magSldShell", 0.0,  minVal = 0, maxVal = 3e-06, vary = False)
modelRef.combineParameters('magSldCore', 'magSldShell')
modelRef.setConstantParam("bg", 2.46e-05)
modelRef.setConstantParam("roughness", 14.540000000000001)
modelRef.setConstantParam("roughnessSlope", 0.0)
modelRef.setConstantParam("packingDensity1", 0.992)
modelRef.setConstantParam("packingDensity2", 0.774)
modelRef.setConstantParam("packingDensity3", 0.598)
modelRef.setConstantParam("packingDensity4", 0.49)
modelRef.setConstantParam("packingDensity5", 0.454)
modelRef.setConstantParam("packingDensity6", 0.5)
modelRef.setConstantParam("packingDensity7", 0.540542504836051)
modelRef.setConstantParam("packingDensity8", 0.552)
modelRef.setConstantParam("packingDensity9", 0.512)
modelRef.setConstantParam("packingDensity10", 0.354)
modelRef.setConstantParam("packingDensity11", 0.0)
modelRef.setConstantParam("layerDistance1", -8.799999999999997)
modelRef.setConstantParam("layerDistance2", -0.09999999999999432)
modelRef.setConstantParam("layerDistance3", -6.299999999999997)
modelRef.setConstantParam("layerDistance4", -14.5)
modelRef.setConstantParam("layerDistance5", -22.599999999999998)
modelRef.setConstantParam("layerDistance6", -25.9)
modelRef.setConstantParam("layerDistance7", -24.599999999999998)
modelRef.setConstantParam("layerDistance8", -24.4)
modelRef.setConstantParam("layerDistance9", -26.799999999999997)
modelRef.setConstantParam("layerDistance10", -32.0)
modelRef.setConstantParam("layerDistance11", -50.0)
modelRef.setConstantParam("dSpacer", 60.800000000000004)
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