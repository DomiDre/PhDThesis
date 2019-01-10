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

# class ModifiedResiduum(Reflectometry):
#   def residuumFormula(self, q, I, sI, Imodel):
#     return (np.log(I) - np.log(Imodel))

expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2 noError')
# expRef.setFitRange(0.025, 1)

dataRef = app.setData(XyeData)
dataRef.loadFromFile('../../transform_data/DD205_4.xye')
dataRef.sliceDomain(0.012, 1)
dataRef.plotData()

modelRef = app.setModel(CmplxCubeCSMonolayerOnSpacer, [InstrumentalResolution])

modelRef.setParam("roughnessSubstrate", 25.815531343710852,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessSpacer", 19.24937346513197,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube", 15.20411566246973,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell", 9.212401025815037,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellAir", 3.229342069551655,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("packingDensity", 0.5587375235643111,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("thicknessShellTop", 35.101505845376515,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShellLower", 32.772266917681826,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessSpacer", 38.96962564752343,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("bg", 8.254587874933867e-07,  minVal = 0, maxVal = 5e-06, vary = True)

# modelRef.setParam("i0", 1.0, minVal=0, maxVal=1.2, vary=True)
modelRef.setConstantParam("dWavelength", 0.02)
# modelRef.combineParameters('roughnessShellCube', 'roughnessCubeShell')
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


modelRef.setConstantParam("a", 93.8)
modelRef.setConstantParam("sigA", 0.)
modelRef.setConstantParam("orderHermite", 10)
modelRef.setConstantParam("coverage", 1.0)
modelRef.setConstantParam("dTheta", 0.0)

modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()