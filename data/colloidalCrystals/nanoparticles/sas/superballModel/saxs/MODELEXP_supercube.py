#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SuperballCSCoupledSigD
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

app = Cli()
expRef = app.setExperiment(Saxs)
expRef.setFitRange(0.03, 0.4)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/DD144.xye')

modelRef = app.setModel(SuperballCSCoupledSigD)
modelRef.setParam("particleSize",     65.1851544,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("d",                21.1855186,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("pVal",             2.47376320,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sigParticleSize",  0.07143705,  minVal = 0, maxVal = 0.5, vary = True)
modelRef.setParam("sigD",             0.40385040,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0",               0.02369477,  minVal = 0, maxVal = 0.1, vary = True)

# modelRef.setConstantParam('x', 1)
modelRef.setConstantParam("bg", 0.)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('orderHermite', 5)

modelRef.setConstantParam("sldCore", 52.1122e-6) # FeO 4.1809 A
modelRef.setConstantParam("sldShell", 41.8489e-6) # Magnetite 8.3841 A
modelRef.setConstantParam("sldSolvent", 8.01e-6) # Toluene

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')