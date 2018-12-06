#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SphereCSCoupled
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
expRef = app.setExperiment(Saxs)

dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/DD67.xye')
dataRef.sliceDomain(0.005, 0.4)
dataRef.plotData()

modelRef = app.setModel(SphereCSCoupled)
modelRef.setParam("particleSize", 63.23795606758981,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("d", 2.96,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigParticleSize", 0.08935713528314805,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("sigD", 0.24975,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.018139350602957512,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("sldCore", 51.22e-6)
modelRef.setConstantParam("sldShell", 41.28e-6)
modelRef.setConstantParam("sldSolvent", 8.01e-6)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()