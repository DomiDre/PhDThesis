#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import CmplxCubeCSMonolayerOnSpacer, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8

import numpy as np
app = App()

expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2 noError')
dataRef = app.setData(XyeData)
dataRef.loadFromFile('../../transform_data/DD175_28.xye')
dataRef.sliceDomain(0.012, 1)
dataRef.plotData()

modelRef = app.setModel(CmplxCubeCSMonolayerOnSpacer, [InstrumentalResolution])


modelRef.setParam("roughnessSubstrate", 20.870933333769248,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessSpacer", 11.06836224951357,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube", 10.824292574547256,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell", 5.7976117338361775,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellAir", 17.056287404119363,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("packingDensity", 0.5576211549932599,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("thicknessShellTop", 16.6,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("thicknessShellLower", 0.7196271204652993,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessSpacer", 73.00984726050072,  minVal = 0, maxVal = 100, vary = True)

modelRef.setConstantParam("a", 85.784)
modelRef.setConstantParam("sigA", 0)
modelRef.setConstantParam("orderHermite", 10)

modelRef.setConstantParam("dWavelength", 0.02)
modelRef.setConstantParam("coverage", 1.0)


modelRef.setConstantParam("reSldShellLower", 8.52e-06)
modelRef.setConstantParam("imSldShellLower", 0.013e-06)
modelRef.setConstantParam('reSldCore', 39.963e-6)
modelRef.setConstantParam('imSldCore', 3.749e-6)
modelRef.setConstantParam("reSldSpacer", 22.724e-06)
modelRef.setConstantParam("imSldSpacer", 0.294e-06)
modelRef.setConstantParam("reSldShellTop", 8.52e-06)
modelRef.setConstantParam("imSldShellTop", 0.013e-06)
modelRef.setConstantParam("reSldSubstrate", 20.122e-6)
modelRef.setConstantParam("imSldSubstrate", 0.459e-6)

modelRef.setConstantParam("dTheta", 0.0)

modelRef.setConstantParam("i0", 1.0)
modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()