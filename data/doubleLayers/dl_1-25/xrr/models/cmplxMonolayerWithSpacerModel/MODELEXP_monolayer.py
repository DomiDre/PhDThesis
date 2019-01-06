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
dataRef.loadFromFile('../../transform_data/DD205_3.xye')
dataRef.sliceDomain(0.012, 1)
dataRef.plotData()

modelRef = app.setModel(CmplxCubeCSDoublelayerOnSpacer, [InstrumentalResolution])

modelRef.setParam("roughnessSubstrate", 5.5,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("roughnessSpacer", 10.15400526960729,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube1", 96.5,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell1", 18.47613439972799,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellPMMA", 19.233649347577025,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube2", 16.75513665733059,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell2", 8.075520236503625,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellAir", 0.0,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("roughnessPMMA", 7.530640357339507,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("packingDensity1", 0.4494789073064813,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("packingDensity2", 0.5359134833027371,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("thicknessShell1Top", 28.681811860151218,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell1Lower", 34.98274258523259,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell2Top", 31.542829650322744,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell2Lower", 18.927188511648396,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessSpacer", 74.66928485559458,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessPMMA", 585.3849369279862,  minVal = 0, maxVal = 1000, vary = True)
modelRef.setParam("bg", 7.4e-07,  minVal = 0, maxVal = 5e-06, vary = False)
modelRef.setParam("i0", 1.0332,  minVal = 0, maxVal = 1.2, vary = False)
modelRef.setParam("dWavelength", 0.029900000000000003,  minVal = 0, maxVal = 0.1, vary = False)

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


modelRef.setConstantParam("a", 93.8)
modelRef.setConstantParam("sigA", 0.)
modelRef.setConstantParam("orderHermite", 10)
modelRef.setConstantParam("coverage", 1.0)
modelRef.setConstantParam("dTheta", 0.0)

modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()