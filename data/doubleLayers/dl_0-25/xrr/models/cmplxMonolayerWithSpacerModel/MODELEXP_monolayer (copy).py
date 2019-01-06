#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import CmplxCubeCSDoublelayerOnSpacer, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8

import numpy as np
app = App()

expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0.025, 0.2)

dataRef = app.setData(XyeData)
dataRef.loadFromFile('../../transform_data/DD205_10.xye')
dataRef.sliceDomain(0.012, 1)
dataRef.plotData()

modelRef = app.setModel(CmplxCubeCSDoublelayerOnSpacer, [InstrumentalResolution])

modelRef.setParam("roughnessSubstrate", 0.0,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessSpacer", 10.100000000000001,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube1", 19.1,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell1", 15.200000000000001,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellPMMA", 0.0,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube2", 29.1,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell2", 4.5,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellAir", 7.5,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessPMMA", 5.527638111449695,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("packingDensity1", 0.538,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("packingDensity2", 0.463,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("thicknessShell1Top", 60.6,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell1Lower", 33.0,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell2Top", 31.400000000000002,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell2Lower", 11.3,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessSpacer", 82.60000000000001,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessPMMA", 542.0,  minVal = 0, maxVal = 1000, vary = True)
modelRef.setParam("bg", 1.555e-06,  minVal = 0, maxVal = 5e-06, vary = False)
modelRef.setParam("i0", 0.8543999999999999,  minVal = 0, maxVal = 1.2, vary = False)

modelRef.setConstantParam("reSldShellLower", 8.52e-06)
modelRef.setConstantParam("imSldShellLower", 0.013e-06)
modelRef.setConstantParam('reSldCore', 39.445e-6)
modelRef.setConstantParam('imSldCore', 3.663e-6)
modelRef.setConstantParam("reSldSpacer", 22.724e-06)
modelRef.setConstantParam("imSldSpacer", 0.294e-06)
modelRef.setConstantParam("reSldShellTop", 8.52e-06)
modelRef.setConstantParam("imSldShellTop", 0.013e-06)
modelRef.setConstantParam("reSldSubstrate", 20.122e-6)
modelRef.setConstantParam("imSldSubstrate", 0.459e-6)
modelRef.setConstantParam("reSldPMMA", 10.841e-6)
modelRef.setConstantParam("imSldPMMA", 0.023127e-6)

modelRef.setConstantParam("dWavelength", 0.03)

modelRef.setConstantParam("a", 93.8)
modelRef.setConstantParam("sigA", 0.)
modelRef.setConstantParam("orderHermite", 10)
modelRef.setConstantParam("coverage", 1.0)
modelRef.setConstantParam("dTheta", 0.0)

modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()