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


import numpy as np
app = App()
expRef = app.setExperiment(PolarizedReflectometry)
expRef.setResiduumFormula('log chi2 noError')
dataRef = app.setData(MftData)

dataRef.loadFromFile('../../mftFiles/DD205_4_5K_10mT_d.mft', ['m'])
dataRef.loadFromFile('../../mftFiles/DD205_4_5K_10mT_u.mft', ['p'])
# dataRef.sliceDomain(0.012, 0.2)
dataRef.plotData()

modelRef = app.setModel(CubeCSMonolayerOnSpacer, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("i0", 0.93,  minVal = 0, maxVal = 1.5, vary = False)


modelRef.setConstantParam("magSldCore", 0.0)
modelRef.setConstantParam("polarizationEfficiency", 1.0)
modelRef.setConstantParam("gamma", 0.0)


modelRef.setParam("roughnessSubstrate", 20.041185753774926,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessSpacer", 23.52694515689599,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube", 14.570243367487063,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell", 22.316437966056185,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellAir", 8.4,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("packingDensity", 0.5000645870803766,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("thicknessShellTop", 39.6,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("thicknessShellLower", 36.6,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessSpacer", 24.2564768302209,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("bg", 1.3999999999999998e-07,  minVal = 0, maxVal = 2e-06, vary = False)

# modelRef.setParam("roughnessSubstrate", 11.100000000000001,  minVal = 0, maxVal = 100, vary = True)
# modelRef.setParam("roughnessSpacer", 21.6,  minVal = 0, maxVal = 100, vary = True)
# modelRef.setParam("roughnessShellCube", 24.5,  minVal = 0, maxVal = 100, vary = True)
# modelRef.setParam("roughnessCubeShell", 23.766717706187528,  minVal = 0, maxVal = 100, vary = True)
# modelRef.setParam("roughnessShellAir", 0.0,  minVal = 0, maxVal = 100, vary = False)
# modelRef.setParam("packingDensity", 0.5330795667386928,  minVal = 0, maxVal = 1, vary = True)
# modelRef.setParam("thicknessShellTop", 11.605678311877316,  minVal = 0, maxVal = 100, vary = True)
# modelRef.setParam("thicknessShellLower", 42.44130818745893,  minVal = 0, maxVal = 100, vary = True)
# modelRef.setParam("thicknessSpacer", 22.96271832659487,  minVal = 0, maxVal = 100, vary = True)

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