#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import CmplxCubeCSMonolayerOnSpacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8

import numpy as np
app = App()

expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2 noError')
dataRef = app.setData(XyeData)
dataRef.loadFromFile('../../transform_data/DD175_28.xye')
dataRef.sliceDomain(0.012, 0.3)
dataRef.plotData()

modelRef = app.setModel(CmplxCubeCSMonolayerOnSpacer, [InstrumentalResolution, ShiftQ])

modelRef.setParam("roughnessSubstrate", 2.0,  minVal = 0.0, maxVal = 50, vary = False)
modelRef.setParam("roughnessSpacer", 11.0,  minVal = 0.0, maxVal = 50, vary = True)
modelRef.setParam("roughnessCubeShell", 8.950689007954807,  minVal = 0.0, maxVal = 50, vary = True)
modelRef.setParam("packingDensity", 0.4875728402769438,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("thicknessShellLower", 3.749719574058963,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessSpacer", 31.50866002940029,  minVal = 0, maxVal = 150, vary = True)
modelRef.setParam("reSldSpacer", 2.2050000000000004e-05,  minVal = 0, maxVal = 3e-05, vary = False)
modelRef.setParam("reSldShellLower", 6.000000000000001e-08,  minVal = 0, maxVal = 2e-05, vary = False)
modelRef.setParam("reSldShellTop", 6.000000000000001e-08,  minVal = 0, maxVal = 3e-05, vary = False)
modelRef.setParam("thicknessShellTop", 28.68,  minVal = 0, maxVal = 40, vary = True)
modelRef.setParam("bg", 1.55e-06,  minVal = 0, maxVal = 5e-06, vary = False)

modelRef.setConstantParam("qShift", 0)
modelRef.setConstantParam("a", 85.784)
modelRef.setConstantParam("sigA", 0.1503)
modelRef.setConstantParam("orderHermite", 10)
modelRef.setConstantParam("roughnessShellAir", 0.0)

modelRef.setConstantParam("dWavelength", 0.0525)
modelRef.setConstantParam("coverage", 1.0)
modelRef.setConstantParam('reSldCore', 41.749e-6)
modelRef.setConstantParam('imSldCore', 3.013e-6)
modelRef.setConstantParam("reSldSubstrate", 20.061e-6)
modelRef.setConstantParam("imSldSubstrate", 0.351e-6)
modelRef.setConstantParam("imSldShellTop", 0.01e-6)
modelRef.setConstantParam("imSldShellLower", 0.01e-6)
modelRef.setConstantParam("imSldSpacer", 0.224e-6)

modelRef.setConstantParam("dTheta", 0.0)

modelRef.setConstantParam("i0", 1.0)
modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()