#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import CubeCSMonolayerOnSpacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8

import numpy as np
app = App()

# class ModifiedResiduum(Reflectometry):
#   def residuumFormula(self, q, I, sI, Imodel):
#     return (np.log(I) - np.log(Imodel))

app.setExperiment(Reflectometry)

dataRef = app.setData(XyeData)
dataRef.loadFromFile('../../transform_data/DD205_4.xye')
dataRef.sliceDomain(0.012, 0.2)
dataRef.plotData()

modelRef = app.setModel(CubeCSMonolayerOnSpacer, [InstrumentalResolution, ShiftQ])

modelRef.setParam("qShift", -0.00258,  minVal = -0.01, maxVal = 0.01, vary = False)
modelRef.setParam("roughnessSubstrate", 3.42,  minVal = 0.0, maxVal = 30, vary = False)
modelRef.setParam("roughnessSpacer", 3.0,  minVal = 0.0, maxVal = 30, vary = False)
modelRef.setParam("roughnessCubeShell", 14.85,  minVal = 0.0, maxVal = 30, vary = False)
modelRef.setParam("packingDensity", 0.486,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("thicknessShellLower", 25.400000000000002,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("thicknessSpacer", 34.300000000000004,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("sldSpacer", 1.2330000000000002e-05,  minVal = 0, maxVal = 3e-05, vary = False)
modelRef.setParam("sldShellLower", 6.5000000000000004e-06,  minVal = 0, maxVal = 2e-05, vary = False)

modelRef.setConstantParam("roughnessShellAir", 0)
modelRef.setConstantParam("thicknessShellTop", 0.0)
modelRef.setConstantParam("sldShellTop", 8.52e-06)
modelRef.setConstantParam("dWavelength", 0.0525)
modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("a", 93.8)
modelRef.setConstantParam("sigA", 0.)
modelRef.setConstantParam("orderHermite", 10)
modelRef.setConstantParam("coverage", 1.0)
modelRef.setConstantParam('sldCore', 41.749e-6)
modelRef.setConstantParam("sldSubstrate", 20.061e-6)
modelRef.setConstantParam("dTheta", 0.0)

modelRef.setConstantParam("i0", 1.0)
modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()