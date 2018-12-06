#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import CubeCSCoupled
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import numpy as np

app = App()
expRef = app.setExperiment(Saxs)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/DD67.xye')
dataRef.sliceDomain(0.005, 0.4)
dataRef.plotData()

modelRef = app.setModel(CubeCSCoupled)
modelRef.setParam("particleSize", 82.56,  minVal = 0, maxVal = 120, vary = True)
modelRef.setParam("sigParticleSize", 0.03675,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.0251,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("d", 22.0,  minVal = 0, maxVal = 50, vary = True)

modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("sldCore", 51.22e-6)
modelRef.setConstantParam("sldShell", 41.28e-6)
modelRef.setConstantParam("sldSolvent", 8.01e-6)
modelRef.setConstantParam("orderHermite", 20)
modelRef.setConstantParam("orderLegendre", 20)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()