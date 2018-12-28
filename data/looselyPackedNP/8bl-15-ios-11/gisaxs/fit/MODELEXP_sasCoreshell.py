#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SphereCSSCoupledHSStructure
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import numpy as np

app = App()
experimentRef = app.setExperiment(Saxs)
experimentRef.setFitRange(0.03,5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../8BL-15-IOS-11_Yoneda.xye')
dataRef.sliceDomain(0.006, 5)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupledHSStructure)
modelRef.setParam("hardSphereRadius", 57.0813308018941,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("eta", 0.42276297918822847,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0", 2025.5230075553925,  minVal = 100.0, maxVal = 5000.0, vary = True)
modelRef.setParam("bg", 618.0,  minVal = 0, maxVal = 1000, vary = False)

modelRef.setConstantParam("particleSize", 54.01861053150746)
modelRef.setConstantParam("dShell", 4.5600000000000005)
modelRef.setConstantParam("dSurfactant", 18.16)
modelRef.setConstantParam("sigParticleSize", 0.05446755447954498)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore", 52.07e-6)
modelRef.setConstantParam("sldShell", 41.85e-6)
modelRef.setConstantParam("sldSurfactant", 8.52e-6)
modelRef.setConstantParam("sldSolvent", 7.55e-6)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()