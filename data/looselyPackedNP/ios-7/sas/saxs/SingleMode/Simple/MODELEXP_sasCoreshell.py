#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SphereCSSCoupled
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
experimentRef = app.setExperiment(Saxs)
experimentRef.setFitRange(0.06, 0.5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/KWi338.xye')
dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupled)

modelRef.setParam("particleSize", 34.84678452358795,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dShell", 79.92,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dSurfactant", 19.6,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("sigParticleSize", 0.09430000000000001,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0", 0.517,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg", 0.0,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore", 52.07e-6)
modelRef.setConstantParam("sldShell", 38.56e-6)
modelRef.setConstantParam("sldSurfactant", 8.52e-6)
modelRef.setConstantParam("sldSolvent", 7.55e-6)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()