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
app.setExperiment(PolarizedReflectometry)
dataRef = app.setData(MftData)

dataRef.loadFromFile('../../mftFiles/DD205_4_5K_6000mT_d.mft', ['m'])
dataRef.loadFromFile('../../mftFiles/DD205_4_5K_6000mT_u.mft', ['p'])
# dataRef.sliceDomain(0.012, 0.2)
dataRef.plotData()

modelRef = app.setModel(CubeCSMonolayerOnSpacer, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("i0", 0.921,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setParam("magSldCore", 1.0688021249773728e-06,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.setConstantParam("polarizationEfficiency", 1.0)
modelRef.setConstantParam("gamma", 0.0)


modelRef.setParam("roughnessSubstrate", 20.041031505537347,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessSpacer", 23.527612662946385,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube", 14.57008761856568,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell", 22.31642583659761,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellAir", 8.4,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("packingDensity", 0.506358957399347,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("thicknessShellTop", 39.6,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("thicknessShellLower", 36.60100058114454,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessSpacer", 24.25716072643032,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("bg", 1.3999999999999998e-07,  minVal = 0, maxVal = 2e-06, vary = False)

# modelRef.setConstantParam("roughnessSubstrate", 20.041031505537347)
# modelRef.setConstantParam("roughnessSpacer", 23.527612662946385)
# modelRef.setConstantParam("roughnessShellCube", 14.57008761856568)
# modelRef.setConstantParam("roughnessCubeShell", 22.31642583659761)
# modelRef.setConstantParam("roughnessShellAir", 8.4)
# modelRef.setConstantParam("packingDensity", 0.506358957399347)
# modelRef.setConstantParam("thicknessShellTop", 39.6)
# modelRef.setConstantParam("thicknessShellLower", 36.60100058114454)
# modelRef.setConstantParam("thicknessSpacer", 24.25716072643032)
# modelRef.setConstantParam("bg", 1.3999999999999998e-07)


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