#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SphereCSSCoupledBimodalHSStructure
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import numpy as np

app = App()
experimentRef = app.setExperiment(Saxs)
experimentRef.setFitRange(0.06,5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../SC-IOS-7_Yoneda.xye')
dataRef.sliceDomain(0.006, 5)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupledBimodalHSStructure)
modelRef.setParam("hardSphereRadius", 38.72,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("eta", 0.342,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0", 22405.3,  minVal = 100.0, maxVal = 50000.0, vary = True)
modelRef.setParam("bg", 147.5,  minVal = 0, maxVal = 500, vary = False)

modelRef.setConstantParam("particleSize1", 35.403336065098124)
modelRef.setConstantParam("particleSize2", 6.877)
modelRef.setConstantParam("sigParticleSize1", 0.0752)
modelRef.setConstantParam("sigParticleSize2", 0.5976)
modelRef.setConstantParam("dShell1", 36.2)
modelRef.setConstantParam("dShell2", 40.0)
modelRef.setConstantParam("fraction", 0.7795)
modelRef.setConstantParam("dSurfactant1", 15.600000000000001)
# modelRef.setConstantParam("i0", 1.6300000000000001)
# modelRef.setConstantParam("bg", 0.0)

modelRef.setConstantParam("sigD1", 0)
modelRef.setConstantParam("sigD2", 0)
modelRef.setConstantParam("sldCore", 52.07e-6)
modelRef.setConstantParam("sldShell", 41.85e-6)
modelRef.setConstantParam("sldSurfactant", 8.52e-6)
modelRef.setConstantParam("sldSolvent", 7.55e-6)
modelRef.combineParameters('dSurfactant1', 'dSurfactant2')

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()