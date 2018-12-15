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

dataRef.loadFromFile('../../experimentalData/PMK18.xye')
dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupled)
modelRef.setParam("particleSize", 54.01861053150746,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dShell", 4.5600000000000005,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dSurfactant", 18.16,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("sigParticleSize", 0.05446755447954498,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0", 0.328,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg", 0.0010600000000000002,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore", 52.07e-6)
modelRef.setConstantParam("sldShell", 41.85e-6)
modelRef.setConstantParam("sldSurfactant", 8.52e-6)
modelRef.setConstantParam("sldSolvent", 7.55e-6)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()