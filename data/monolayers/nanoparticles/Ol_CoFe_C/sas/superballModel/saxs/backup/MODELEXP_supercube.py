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
expRef = app.setExperiment(Saxs)
expRef.setFitRange(0.04, 0.4)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/DD67.xye')
dataRef.sliceDomain(0.005, 0.4)

modelRef = app.setModel(Superball)
modelRef.setParam("r", 57.2530803,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("pVal", 1.41948566,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("sigR", 0.09106502,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.02603174,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("bg", 0.0011400000000000002,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam("sldCore", saxs_sldCore)
modelRef.setConstantParam("sldSolvent", saxs_sldSolvent)
# modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')