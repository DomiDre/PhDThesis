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

modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("sldCore", 41.03e-6)
modelRef.setConstantParam("sldSolvent", 6.46e-6)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')