#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import CubeCSMonolayerOnSpacer, Magnetic, DataResolution
from modelexp.data import MftData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8

import numpy as np
app = App()
expRef = app.setExperiment(PolarizedReflectometry)
expRef.setResiduumFormula('log chi2 noError')
dataRef = app.setData(MftData)

dataRef.loadFromFile('../../mftFiles/DD205_4_5K_-100mT_d.mft', ['p'])
dataRef.loadFromFile('../../mftFiles/DD205_4_5K_-100mT_u.mft', ['m'])
# dataRef.sliceDomain(0.012, 0.2)
dataRef.plotData()

modelRef = app.setModel(CubeCSMonolayerOnSpacer, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("i0", 1.0335,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setParam("magSldCore", 5.97201519259041e-07,  minVal = -2e-06, maxVal = 2e-06, vary = True)

modelRef.setConstantParam("polarizationEfficiency", 1.0)
modelRef.setConstantParam("bg", 1.3999999999999998e-07)
modelRef.setConstantParam("gamma", 0.0)


modelRef.setConstantParam("roughnessSubstrate", 20.041031505537347)
modelRef.setConstantParam("roughnessSpacer", 23.527612662946385)
modelRef.setConstantParam("roughnessShellCube", 14.57008761856568)
modelRef.setConstantParam("roughnessCubeShell", 22.31642583659761)
modelRef.setConstantParam("roughnessShellAir", 8.4)
modelRef.setConstantParam("packingDensity", 0.506358957399347)
modelRef.setConstantParam("thicknessShellTop", 39.6)
modelRef.setConstantParam("thicknessShellLower", 36.60100058114454)
modelRef.setConstantParam("thicknessSpacer", 24.25716072643032)

modelRef.setConstantParam("sldCore", 6.194e-06)
modelRef.setConstantParam("sldSubstrate", 2.079e-6)
modelRef.setConstantParam("sldSpacer", 4.186e-06)
modelRef.setConstantParam("sldShellLower", 0.078e-06)
modelRef.setConstantParam("sldShellTop", 0.078e-6)

modelRef.setConstantParam("coverage", 1.0)
modelRef.setConstantParam("a", 93.80000000000001)
modelRef.setConstantParam("sigA", 0)
modelRef.setConstantParam('orderHermite', 10)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()