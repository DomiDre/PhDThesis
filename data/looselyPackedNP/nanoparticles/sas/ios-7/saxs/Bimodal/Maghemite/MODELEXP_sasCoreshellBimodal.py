#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SphereCSSCoupledBimodal
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
from fortSAS import sphere_css_coupled
import numpy as np

app = App()
expRef = app.setExperiment(Saxs)
# expRef.setFitRange(0.05, 1)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/KWi338.xye')

dataRef.sliceDomain(1e-2, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupledBimodal)
modelRef.setParam("particleSize1", 35.237194651185746,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("particleSize2", 10.0,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigParticleSize1", 0.08280504877345288,  minVal = 0, maxVal = 0.2, vary = True)
modelRef.setParam("sigParticleSize2", 0.36160000000000003,  minVal = 0, maxVal = 0.8, vary = True)
modelRef.setParam("dShell1", 37.92,  minVal = 0, maxVal = 40, vary = False)
modelRef.setParam("dShell2", 40.0,  minVal = 0, maxVal = 40, vary = False)
modelRef.setParam("fraction", 0.6553,  minVal = 0.1, maxVal = 1, vary = True)
modelRef.setParam("dSurfactant1", 13.950000000000001,  minVal = 0, maxVal = 50, vary = False)
modelRef.setParam("i0", 1.34,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("bg", 0.0,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam("sigD1", 0)
modelRef.setConstantParam("sigD2", 0)
modelRef.setConstantParam("sldCore", 52.07e-6)
modelRef.setConstantParam("sldShell", 38.56e-6)
modelRef.setConstantParam("sldSurfactant", 8.52e-6)
modelRef.setConstantParam("sldSolvent", 7.55e-6)
modelRef.combineParameters('dSurfactant1', 'dSurfactant2')
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()