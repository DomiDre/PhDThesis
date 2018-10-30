#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import Cube
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

saxs_sldCore = sld_xray_GALAXI['Cobalt Ferrite'].real
saxs_sldSolvent = sld_xray_GALAXI['n-Hexane'].real

app = App()
app.setExperiment(Saxs)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/finalDD67.xy')
dataRef.sliceDomain(0.005, 0.4)
dataRef.plotData()

modelRef = app.setModel(Cube)
modelRef.setParam("a", 100.95075087881172,  minVal = 0, maxVal = 120, vary = True)
modelRef.setParam("sigA", 0.06253789531504311,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.028444056456638167,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("bg", 0.0011400000000000002,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam("sldCore", saxs_sldCore)
modelRef.setConstantParam("sldSolvent", saxs_sldSolvent)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()