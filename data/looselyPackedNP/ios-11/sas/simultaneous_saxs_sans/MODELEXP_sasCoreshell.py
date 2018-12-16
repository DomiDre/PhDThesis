#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import SimultaneousSaxsSans
from modelexp.models.sas import SphereCSSCoupled, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
app.setExperiment(SimultaneousSaxsSans)
dataRef = app.setData(XyeData)


dataRef.loadFromFile('../experimentalData/PMK18.xye', ['saxs'])
dataRef.loadFromFile('../experimentalData/PMK18_LSDD_Nuclear20.dat', ['sans', 'sa'])
dataRef.loadFromFile('../experimentalData/PMK18_SSDD_Nuclear20.dat', ['sans', 'la'])

dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupled, InstrumentalResolution)


modelRef.setParam("particleSize", 53.52,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dShell", 2.311685120892304,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dSurfactant", 21.6,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigParticleSize", 0.058,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0_saxs", 0.319,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg_saxs", 0.0,  minVal = 0, maxVal = 0.02, vary = True)
modelRef.setParam("i0_sans", 0.025198296884048177,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg_sans", 0.0029400000000000003,  minVal = 0, maxVal = 0.02, vary = True)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore_saxs", 52.07e-6)
modelRef.setConstantParam("sldShell_saxs", 38.56e-6)
modelRef.setConstantParam("sldSurfactant_saxs", 8.52e-6)
modelRef.setConstantParam("sldSolvent_saxs", 7.55e-6)

modelRef.setConstantParam("sldCore_sans", 8.34e-6)
modelRef.setConstantParam("sldShell_sans", 6.57e-6)
modelRef.setConstantParam("sldSurfactant_sans", 0.078e-6)
modelRef.setConstantParam("sldSolvent_sans", 5.66e-6)

modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.setConstantParam("dTheta_sa", 0.0021)
modelRef.setConstantParam("dTheta_la", 0.0038)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()