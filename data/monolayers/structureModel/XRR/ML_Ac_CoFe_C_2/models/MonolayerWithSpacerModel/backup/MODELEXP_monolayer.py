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
dataRef.loadFromFile('../../transform_data/DD175_28.xye')
dataRef.sliceDomain(0.012, 0.5)
dataRef.plotData()

modelRef = app.setModel(CubeCSMonolayerOnSpacer, [InstrumentalResolution, ShiftQ])

modelRef.setParam("qShift", -0.00418,  minVal = -0.01, maxVal = 0.01, vary = False)
modelRef.setParam("roughnessSubstrate", 2.4142420030905027,  minVal = 0.0, maxVal = 50, vary = True)
modelRef.setParam("roughnessSpacer", 23.0,  minVal = 0.0, maxVal = 50, vary = False)
modelRef.setParam("roughnessCubeShell", 14.700000000000001,  minVal = 0.0, maxVal = 50, vary = False)
modelRef.setParam("packingDensity", 0.437,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("thicknessShellLower", 52.7,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("thicknessSpacer", 72.75,  minVal = 0, maxVal = 150, vary = False)
modelRef.setParam("sldSpacer", 7.71e-06,  minVal = 0, maxVal = 3e-05, vary = False)
modelRef.setParam("sldShellLower", 0.0,  minVal = 0, maxVal = 2e-05, vary = False)

modelRef.setConstantParam("a", 85.784)
modelRef.setConstantParam("sigA", 0.1503)
modelRef.setConstantParam("orderHermite", 10)
modelRef.setConstantParam("sldShellTop", 0.0)
modelRef.setConstantParam("thicknessShellTop", 0.0)
modelRef.setConstantParam("roughnessShellAir", 0.0)

modelRef.setConstantParam("dWavelength", 0.0525)
modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("coverage", 1.0)
modelRef.setConstantParam('sldCore', 41.749e-6)
modelRef.setConstantParam("sldSubstrate", 20.061e-6)
modelRef.setConstantParam("dTheta", 0.0)

modelRef.setConstantParam("i0", 1.0)
modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()