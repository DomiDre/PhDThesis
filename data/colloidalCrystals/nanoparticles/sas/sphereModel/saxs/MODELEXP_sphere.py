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

saxs_sldCore = sld_xray_GALAXI['Maghemite'].real
saxs_sldSolvent = sld_xray_GALAXI['n-Hexane'].real

app = App()
expRef = app.setExperiment(Saxs)
expRef.setFitRange(0.03, 2)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../DD144.xye')
# dataRef.sliceDomain(0., 0.25)
dataRef.plotData()

modelRef = app.setModel(Sphere)
modelRef.setParam("r", 70.49144306027468,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigR", 0.08947199315063842,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.030393334064297534,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("bg", 0.0005291831141359082,  minVal = 0, maxVal = 0.02, vary = True)

modelRef.setConstantParam("sldCore", saxs_sldCore)
modelRef.setConstantParam("sldSolvent", saxs_sldSolvent)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()