#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import SimultaneousSaxsSansSanspol
from modelexp.models.sas import SphereCSSCoupled, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
expRef = app.setExperiment(SimultaneousSaxsSansSanspol)

dataRef = app.setData(XyeData)


dataRef.loadFromFile('../experimentalData/PMK18.xye', ['saxs'])
dataRef.loadFromFile('../experimentalData/PMK18_LSDD_Nuclear20.dat', ['sans', 'sa'])
dataRef.loadFromFile('../experimentalData/PMK18_SSDD_Nuclear20.dat', ['sans', 'la'])

dataRef.loadFromFile('../experimentalData/PMK18_SSDD_Mag20_I+.dat', ['sans', 'p', 'la'])
dataRef.loadFromFile('../experimentalData/PMK18_SSDD_Mag20_I-.dat', ['sans', 'm', 'la'])
dataRef.loadFromFile('../experimentalData/PMK18_LSDD_Mag20_I+.dat', ['sans', 'p', 'sa'])
dataRef.loadFromFile('../experimentalData/PMK18_LSDD_Mag20_I-.dat', ['sans', 'm', 'sa'])

dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupled, [Magnetic, InstrumentalResolution])
modelRef.setParam("magSldCore", 1.085e-06,  minVal = 0, maxVal = 5e-06, vary = True)
modelRef.setParam("magSldShell", 5e-09,  minVal = 0, maxVal = 5e-06, vary = True)

modelRef.setParam("particleSize", 53.52532255801053,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dShell", 3.06788487244511,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dSurfactant", 21.28,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigParticleSize", 0.0579,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0_sans", 0.028,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg_sans", 0.0,  minVal = 0, maxVal = 0.02, vary = False)
modelRef.setParam("i0_saxs", 0.3193553851380457,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg_saxs", 0.0010600000000000002,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam("sigD", 0.)
modelRef.setConstantParam("sldCore_sans", 8.34e-6)
modelRef.setConstantParam("sldShell_sans", 7.00e-6)
modelRef.setConstantParam("sldSurfactant_sans", 0.078e-6)
modelRef.setConstantParam("sldSolvent_sans", 5.66e-6)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.setConstantParam("dTheta_sa", 0.0021)
modelRef.setConstantParam("dTheta_la", 0.0038)

modelRef.setConstantParam("sldCore_saxs", 52.07e-6)
modelRef.setConstantParam("sldShell_saxs", 41.85e-6)
modelRef.setConstantParam("sldSurfactant_saxs", 8.52e-6)
modelRef.setConstantParam("sldSolvent_saxs", 7.55e-6)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()