#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SphereCSCoupledHSStructure
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import numpy as np

app = App()
experimentRef = app.setExperiment(Saxs)
experimentRef.setFitRange(0.03,5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../8BL-15-IOS-7_Yoneda.xye')
dataRef.sliceDomain(0.006, 5)
dataRef.plotData()

modelRef = app.setModel(SphereCSCoupledHSStructure)
modelRef.setParam("hardSphereRadius", 56.54690522456867,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("eta", 0.4388237100483382,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0", 2550.0,  minVal = 100.0, maxVal = 5000.0, vary = True)
modelRef.setParam("bg", 410.65389218096965,  minVal = 0, maxVal = 1000, vary = True)

modelRef.setConstantParam("particleSize", 35.4033361)
modelRef.setConstantParam("dShell", 15.6)
modelRef.setConstantParam("sigParticleSize", 0.0752)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore", 4.185e-05)
modelRef.setConstantParam("sldShell", 8.52e-6)
modelRef.setConstantParam("sldSolvent", 7.55e-6)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()