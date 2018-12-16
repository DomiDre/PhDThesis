#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SphereCSSCoupledBimodal, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
experimentRef = app.setExperiment(Sans)
# experimentRef.setFitRange(0.05, 0.5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../experimentalData/KWi338_SA_Nuc20.dat', ['sa'])
dataRef.loadFromFile('../experimentalData/KWi338_LA_Nuc20.dat', ['la'])

dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupledBimodal, InstrumentalResolution)
modelRef.setParam("particleSize1", 35.2,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("particleSize2", 10.0,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("sigParticleSize1", 0.0828,  minVal = 0, maxVal = 0.2, vary = False)
modelRef.setParam("sigParticleSize2", 0.36160000000000003,  minVal = 0, maxVal = 0.8, vary = False)
modelRef.setParam("dShell1", 37.92,  minVal = 0, maxVal = 40, vary = False)
modelRef.setParam("dShell2", 40.0,  minVal = 0, maxVal = 40, vary = False)
modelRef.setParam("fraction", 0.7392934578673449,  minVal = 0.1, maxVal = 1, vary = True)
modelRef.setParam("dSurfactant1", 14.55278082534625,  minVal = 0, maxVal = 50, vary = True)
modelRef.setParam("i0", 0.2897036549904314,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("bg", 0.0015600000000000002,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam("sigD1", 0.)
modelRef.setConstantParam("sigD2", 0.)
modelRef.setConstantParam("sldCore", 8.34e-6)
modelRef.setConstantParam("sldShell", 6.57e-6)
modelRef.setConstantParam("sldSurfactant", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.66e-6)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.setConstantParam("dTheta_sa", 0.0021)
modelRef.setConstantParam("dTheta_la", 0.0038)

modelRef.combineParameters('dSurfactant1', 'dSurfactant2')
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()