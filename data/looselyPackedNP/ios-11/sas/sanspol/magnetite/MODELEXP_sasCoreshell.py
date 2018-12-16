#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sanspol
from modelexp.models.sas import SphereCSSCoupled, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
experimentRef = app.setExperiment(Sanspol)
experimentRef.setFitRange(0.01, 1)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/PMK18_SSDD_Mag20_I+.dat', ['p', 'la'])
dataRef.loadFromFile('../../experimentalData/PMK18_SSDD_Mag20_I-.dat', ['m', 'la'])
dataRef.loadFromFile('../../experimentalData/PMK18_LSDD_Mag20_I+.dat', ['p', 'sa'])
dataRef.loadFromFile('../../experimentalData/PMK18_LSDD_Mag20_I-.dat', ['m', 'sa'])

# dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupled, [Magnetic, InstrumentalResolution])

modelRef.setParam("magSldCore", 3.6175654175816726e-07,  minVal = 0, maxVal = 5e-06, vary = False)
modelRef.setParam("magSldShell", 1.3150000000000001e-06,  minVal = 0, maxVal = 5e-06, vary = False)

modelRef.setConstantParam("particleSize", 54.0)
modelRef.setConstantParam("dShell", 16.16)
modelRef.setConstantParam("dSurfactant", 18.16)
modelRef.setConstantParam("sigParticleSize", 0.054400000000000004)
modelRef.setConstantParam("i0", 0.035)
modelRef.setConstantParam("bg", 0.00206)

modelRef.setConstantParam("sigD", 0.)
modelRef.setConstantParam("sldCore", 8.34e-6)
modelRef.setConstantParam("sldShell", 7.00e-6)
modelRef.setConstantParam("sldSurfactant", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.66e-6)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.setConstantParam("dTheta_sa", 0.0021)
modelRef.setConstantParam("dTheta_la", 0.0038)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()