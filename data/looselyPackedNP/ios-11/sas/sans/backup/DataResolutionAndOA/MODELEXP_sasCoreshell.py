#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SphereCSSCoupledOA, DataResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
experimentRef = app.setExperiment(Sans)
# experimentRef.setFitRange(0.05, 0.5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/sans_PKM18_N_8m.dat', ['sa'])
dataRef.loadFromFile('../../experimentalData/sans_PKM18_N_2m.dat', ['la'])

# dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupledOA, DataResolution)

modelRef.setParam("particleSize", 54.160000000000004,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("dShell", 25.813887854079432,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dSurfactant", 19.430089054917197,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigParticleSize", 0.0543,  minVal = 0, maxVal = 0.1, vary = False)
modelRef.setParam("i0", 0.043943778694026936,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg", 0.0030345440321790885,  minVal = 0, maxVal = 0.02, vary = True)
modelRef.setParam("rOleic", 21.0,  minVal = 0, maxVal = 50, vary = False)
modelRef.setParam("i0Oleic", 0.8610517576155581,  minVal = 0, maxVal = 2, vary = True)
# modelRef.setParam("dTheta_sa", 0.0029467535570545343,  minVal = 0, maxVal = 0.01, vary = True)
# modelRef.setParam("dTheta_la", 0.0032314645344779054,  minVal = 0, maxVal = 0.01, vary = True)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore", 8.34e-6)
modelRef.setConstantParam("sldShell", 6.57e-6)
modelRef.setConstantParam("sldSurfactant", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.66e-6)
# modelRef.setConstantParam('wavelength', 5.9984)
# modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()