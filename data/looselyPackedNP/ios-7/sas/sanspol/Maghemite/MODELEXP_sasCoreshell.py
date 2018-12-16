#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sanspol
from modelexp.models.sas import SphereCSSCoupledBimodal, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
experimentRef = app.setExperiment(Sanspol)
experimentRef.setFitRange(0.03, 0.5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/KWi338_LA_Mag20_I+.dat', ['p', 'la'])
dataRef.loadFromFile('../../experimentalData/KWi338_LA_Mag20_I-.dat', ['m', 'la'])
dataRef.loadFromFile('../../experimentalData/KWi338_SA_Mag20_I+.dat', ['p', 'sa'])
dataRef.loadFromFile('../../experimentalData/KWi338_SA_Mag20_I-.dat', ['m', 'sa'])

dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupledBimodal, [Magnetic, InstrumentalResolution])

modelRef.setParam("magSldCore", 0.0,  minVal = 0, maxVal = 5e-06, vary = False)
modelRef.setParam("magSldShell", 4.397993089239108e-07,  minVal = 0, maxVal = 5e-06, vary = True)

modelRef.setConstantParam("particleSize1", 35.2)
modelRef.setConstantParam("particleSize2", 10.0)
modelRef.setConstantParam("sigParticleSize1", 0.0828)
modelRef.setConstantParam("sigParticleSize2", 0.36160000000000003)
modelRef.setConstantParam("dShell1", 37.92)
modelRef.setConstantParam("dShell2", 40.0)
modelRef.setConstantParam("fraction", 0.7392934578673449)
modelRef.setConstantParam("dSurfactant1", 14.55278082534625)
modelRef.setConstantParam("i0", 0.2897036549904314)
modelRef.setConstantParam("bg", 0.0015600000000000002)

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

modelRef.setConstantParam('magSldSurfactant', 0)
modelRef.setConstantParam('magSldSolvent', 0)

modelRef.combineParameters('dSurfactant1', 'dSurfactant2')
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()