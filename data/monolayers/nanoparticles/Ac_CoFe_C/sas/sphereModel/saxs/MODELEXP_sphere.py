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

dataRef.loadFromFile('../../experimental_data/AH11.xye')
dataRef.sliceDomain(0., 0.25)
dataRef.plotData()

modelRef = app.setModel(Sphere)
modelRef.setParam("r", 55.64451281012996,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigR", 0.12989754094878023,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.04000007285696197,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("bg", 0.0,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam("sldCore", saxs_sldCore)
modelRef.setConstantParam("sldSolvent", saxs_sldSolvent)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()