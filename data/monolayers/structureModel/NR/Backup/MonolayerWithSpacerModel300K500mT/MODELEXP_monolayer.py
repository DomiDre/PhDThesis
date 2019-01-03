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

dataRef.loadFromFile('../../mftFiles/DD205_4_300K_500mT_d.mft', ['m'])
dataRef.loadFromFile('../../mftFiles/DD205_4_300K_500mT_u.mft', ['p'])
# dataRef.sliceDomain(0.012, 0.2)
dataRef.plotData()

modelRef = app.setModel(CubeCSMonolayerOnSpacer, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("i0", 0.921,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setParam("sldShellLower", 5.6e-07,  minVal = 0, maxVal = 2e-05, vary = False)
modelRef.setParam("sldSpacer", 2.4300000000000005e-06,  minVal = 0, maxVal = 3e-05, vary = False)
modelRef.setParam("sldCore", 6.1669999999999996e-06,  minVal = 0, maxVal = 7e-06, vary = False)
modelRef.setParam("sldSubstrate", 2.067e-06,  minVal = 0, maxVal = 3e-06, vary = False)
modelRef.setParam("magSldCore", 5.76e-07,  minVal = 0, maxVal = 3e-06, vary = True)

modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("roughnessSubstrate", 4.4)
modelRef.setConstantParam("roughnessSpacer", 1.7000000000000002)
modelRef.setConstantParam("roughnessCubeShell", 9.950000000000001)
modelRef.setConstantParam("roughnessShellAir", 8.5)
modelRef.setConstantParam("packingDensity", 0.484)
modelRef.setConstantParam("thicknessShellLower", 22.900000000000002)
modelRef.setConstantParam("thicknessSpacer", 38.400000000000006)
modelRef.setConstantParam("coverage", 1.0)
modelRef.setConstantParam("sldShellTop", 0.0)
modelRef.setConstantParam("thicknessShellTop", 0.0)
modelRef.setConstantParam("a", 93.80000000000001)
# modelRef.setParam("dWavelength", 0.061700000000000005,  minVal = 0, maxVal = 0.1, vary = False)

# modelRef.setConstantParam("dTheta", 0.0)

# modelRef.setParam("i0", 1.0,  minVal = 0, maxVal = 2, vary = False)
# modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()