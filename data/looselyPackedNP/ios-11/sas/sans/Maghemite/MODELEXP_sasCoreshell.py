#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SphereCSSCoupled, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
experimentRef = app.setExperiment(Sans)
# experimentRef.setFitRange(0.05, 0.5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/PMK18_LSDD_Nuclear20.dat', ['sa'])
dataRef.loadFromFile('../../experimentalData/PMK18_SSDD_Nuclear20.dat', ['la'])

# dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupled, InstrumentalResolution)

modelRef.setParam("particleSize", 54.160000000000004,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("dShell", 12.786260450385193,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dSurfactant", 18.435923146037997,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigParticleSize", 0.0543,  minVal = 0, maxVal = 0.1, vary = False)
modelRef.setParam("i0", 0.03273727581808111,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg", 0.0024732183368543358,  minVal = 0, maxVal = 0.02, vary = True)

modelRef.setConstantParam("sigD", 0.)
modelRef.setConstantParam("sldCore", 8.34e-6)
modelRef.setConstantParam("sldShell", 6.57e-6)
modelRef.setConstantParam("sldSurfactant", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.66e-6)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.setConstantParam("dTheta_sa", 0.0021)
modelRef.setConstantParam("dTheta_la", 0.0038)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()