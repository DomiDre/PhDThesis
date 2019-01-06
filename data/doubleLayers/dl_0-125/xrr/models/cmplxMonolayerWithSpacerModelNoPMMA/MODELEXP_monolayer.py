#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import CmplxCubeCSDoublelayerOnSpacerNoPmma, InstrumentalResolution
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

modelRef = app.setModel(CmplxCubeCSDoublelayerOnSpacerNoPmma, [InstrumentalResolution])

modelRef.setParam("roughnessSubstrate", 20.1,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessSpacer", 20.1,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube1", 26.700000000000003,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell1", 9.593560355087355,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellShell", 2.6,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("roughnessShellCube2", 61.5,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell2", 16.8,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellAir", 23.3,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("packingDensity1", 0.6213642370291839,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("packingDensity2", 0.07,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("thicknessShell1Top", 56.6,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell1Lower", 33.300000000000004,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell2Top", 99.99999934317877,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell2Lower", 2.0,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessSpacer", 78.5,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("bg", 1.42e-06,  minVal = 0, maxVal = 5e-06, vary = False)
modelRef.setParam("i0", 1.0475999999999999,  minVal = 0, maxVal = 1.2, vary = False)

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

modelRef.setConstantParam("dWavelength", 0.02)

modelRef.setConstantParam("a", 93.8)
modelRef.setConstantParam("orderHermite", 10)
modelRef.setConstantParam("coverage", 1.0)
modelRef.setConstantParam("dTheta", 0.0)

modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()