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

modelRef.setParam("roughnessSubstrate", 9.019539841717133,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessSpacer", 18.860520473538433,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellCube", 14.680061580734243,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessCubeShell", 8.554030651881362,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("roughnessShellAir", 3.643112301377699,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("packingDensity", 0.4147377127468205,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("thicknessShellTop", 34.10489014271471,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShellLower", 38.55410273622441,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessSpacer", 8.454304689459924,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("bg", 8.788356251075819e-07,  minVal = 0, maxVal = 5e-06, vary = True)

# modelRef.setParam("i0", 1.0, minVal=0, maxVal=1.2, vary=True)
modelRef.setConstantParam("dWavelength", 0.05)
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