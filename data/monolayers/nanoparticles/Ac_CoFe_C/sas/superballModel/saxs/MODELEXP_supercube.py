#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import Superball
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

saxs_sldCore = sld_xray_GALAXI['Cobalt Ferrite'].real
saxs_sldSolvent = sld_xray_GALAXI['n-Hexane'].real

app = Cli()
app.setExperiment(Saxs)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../AH11.xye')
dataRef.sliceDomain(0., 0.25)

modelRef = app.setModel(Superball)
modelRef.setParam("r", 46.9420801,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("pVal", 2.65742743,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("sigR", 0.11870446,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.04124193,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("bg", 0.0,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam('orderHermite', 20)
modelRef.setConstantParam('orderLegendre', 20)
modelRef.setConstantParam("sldCore", saxs_sldCore)
modelRef.setConstantParam("sldSolvent", saxs_sldSolvent)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')