#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import Sphere
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

saxs_sldCore = sld_xray_GALAXI['Cobalt Ferrite'].real
saxs_sldSolvent = sld_xray_GALAXI['n-Hexane'].real

app = App()
app.setExperiment(Saxs)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('./finalDD67.xy')
dataRef.sliceDomain(0.005, 0.4)
dataRef.plotData()

modelRef = app.setModel(Sphere)
modelRef.setParam("r", 62.552194776360615,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigR", 0.09738588873844115,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.026048534855793583,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("bg", 0.0011400000000000002,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam("sldCore", saxs_sldCore)
modelRef.setConstantParam("sldSolvent", saxs_sldSolvent)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()