#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import CubeCSMonolayer, InstrumentalResolution, ShiftQ
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

modelRef = app.setModel(CubeCSMonolayer, [InstrumentalResolution, ShiftQ])

modelRef.setParam("bg", 5e-06,  minVal = 0.0, maxVal = 0.0001, vary = True)
modelRef.setParam("qShift", -0.0013799999999999993,  minVal = -0.01, maxVal = 0.01, vary = False)
modelRef.setParam("roughnessSubstrate", 5.45,  minVal = 0.0, maxVal = 50, vary = True)
modelRef.setParam("roughnessCubeShell", 3.85,  minVal = 0.0, maxVal = 50, vary = True)
modelRef.setParam("roughnessShellAir", 1.1326327875593734e-06,  minVal = 0.0, maxVal = 50, vary = True)
modelRef.setParam("packingDensity", 0.48653097725634037,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("sldShellLower", 1.1799925925934012e-05,  minVal = 0, maxVal = 2e-05, vary = True)
modelRef.setParam("thicknessShellLower", 66.1476789115926,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("coverage", 1.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.setParam("sldShellTop", 1.252e-05,  minVal = 0, maxVal = 2e-05, vary = True)
modelRef.setParam("thicknessShellTop", 25.588533250435074,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("a", 69.0,  minVal = 0, maxVal = 200, vary = True)
modelRef.setParam("dWavelength", 0.062200000000000005,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam('sldCore', 41.749e-6)
modelRef.setConstantParam("sldSubstrate", 1.9686962563206795e-05)
modelRef.setConstantParam("dTheta", 0.0)

modelRef.setParam("i0", 1.0,  minVal = 0, maxVal = 2, vary = False)
modelRef.setConstantParam('wavelength', 1.5418)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()