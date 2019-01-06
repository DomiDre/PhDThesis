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
dataRef.loadFromFile('../../transform_data/DD213_7.xye')
dataRef.sliceDomain(0.012, 1)
dataRef.plotData()

modelRef = app.setModel(CmplxCubeCSDoublelayerOnSpacer, [InstrumentalResolution])

modelRef.setParam("roughnessSubstrate", 21.6,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessSpacer", 17.6,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube1", 26.200000000000003,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell1", 10.5,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellPMMA", 0.0,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube2", 30.6,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell2", 19.700000000000003,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellAir", 35.7,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessPMMA", 16.400000000000002,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("packingDensity1", 0.672,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("packingDensity2", 0.0,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("thicknessShell1Top", 11.600000000000001,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell1Lower", 34.1,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell2Top", 3.829214723083396e-10,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell2Lower", 27.26833199196254,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessSpacer", 71.8,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessPMMA", 235.90695727421368,  minVal = 0, maxVal = 1000, vary = True)
modelRef.setParam("bg", 1.255e-06,  minVal = 0, maxVal = 5e-06, vary = False)
modelRef.setParam("i0", 0.9431999999999999,  minVal = 0, maxVal = 1.2, vary = False)

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

modelRef.setConstantParam("dWavelength", 0.02)

modelRef.setConstantParam("a", 93.8)
modelRef.setConstantParam("sigA", 0.)
modelRef.setConstantParam("orderHermite", 10)
modelRef.setConstantParam("coverage", 1.0)
modelRef.setConstantParam("dTheta", 0.0)

modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()