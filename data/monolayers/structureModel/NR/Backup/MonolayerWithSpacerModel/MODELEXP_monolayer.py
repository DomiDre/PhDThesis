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

dataRef.loadFromFile('../../mftFiles/DD205_4_5K_10mT_d.mft', ['m'])
dataRef.loadFromFile('../../mftFiles/DD205_4_5K_10mT_u.mft', ['p'])
# dataRef.sliceDomain(0.012, 0.2)
dataRef.plotData()

modelRef = app.setModel(CubeCSMonolayerOnSpacer, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("i0", 0.921,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setParam("sldCore", 6.081069351458225e-06,  minVal = 0, maxVal = 2e-05, vary = True)
modelRef.setParam("sldShellLower", 6.021142831832316e-07,  minVal = 0, maxVal = 2e-05, vary = True)
modelRef.setParam("magSldCore", 0.0,  minVal = 0, maxVal = 3e-06, vary = False)


modelRef.setConstantParam("sldSpacer", 2.26e-06)
modelRef.setConstantParam("sldSubstrate", 2.072e-6)

modelRef.setConstantParam("roughnessSubstrate", 2.3128366807801144)
modelRef.setConstantParam("roughnessSpacer", 2.5)
modelRef.setConstantParam("roughnessCubeShell", 12.200000000000001)
modelRef.setConstantParam("packingDensity", 0.491)
modelRef.setConstantParam("thicknessShellLower", 23.5)
modelRef.setConstantParam("thicknessSpacer", 36.1)

modelRef.setConstantParam("sldShellTop", 0.0)
modelRef.setConstantParam("thicknessShellTop", 0.0)
modelRef.setConstantParam("roughnessShellAir", 0.0)

modelRef.setConstantParam("roughnessShellAir", 0.0)
modelRef.setConstantParam("thicknessShellTop", 0.0)

modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("coverage", 1.0)
modelRef.setConstantParam("a", 93.80000000000001)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()