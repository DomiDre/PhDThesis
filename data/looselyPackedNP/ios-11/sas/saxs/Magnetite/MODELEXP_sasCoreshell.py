#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SphereCS
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
experimentRef = app.setExperiment(Saxs)
experimentRef.setFitRange(0.06, 0.5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/PMK18.xye')
dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCS)
modelRef.setParam("r", 52.897607525841025,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigR", 0.05594273920569346,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0", 0.5330791847257481,  minVal = 0, maxVal = 1, vary = True)

modelRef.setConstantParam("d", 14.72095)
modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore", 41.85e-6)
modelRef.setConstantParam("sldShell", 8.52e-6)
modelRef.setConstantParam("sldSolvent", 7.55e-6)
modelRef.setConstantParam("bg", 0.0)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()