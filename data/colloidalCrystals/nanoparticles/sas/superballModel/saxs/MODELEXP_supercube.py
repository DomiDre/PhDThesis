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
# Iteration: 406  Chi2:74128.17848003955
# [[Variables]]
#     particleSize:     58.9943565 (init = 65.18515)
#     d:                6.76320262 (init = 21.18552)
#     pVal:             4.40910687 (init = 2.473763)
#     sldCore:          5.21122e-05 (fixed)
#     sldShell:         4.18489e-05 (fixed)
#     sldSolvent:       8.01e-06 (fixed)
#     sigParticleSize:  0.05646412 (init = 0.07143705)
#     sigD:             0.99669205 (init = 0.4038504)
#     i0:               0.01818002 (init = 0.02369477)
#     bg:               0 (fixed)
#     orderHermite:     5 (fixed)
#     orderLegendre:    10 (fixed)


modelRef = app.setModel(SuperballCSCoupledSigD)
modelRef.setParam("particleSize",     58.9943565,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("d",                6.76320262,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("pVal",             4.40910687,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sigParticleSize",  0.05646412,  minVal = 0, maxVal = 0.5, vary = True)
modelRef.setParam("sigD",             0.99669205,  minVal = 0, maxVal = 3, vary = True)
modelRef.setParam("i0",               0.01818002,  minVal = 0, maxVal = 0.1, vary = True)

# modelRef.setConstantParam('x', 1)
modelRef.setConstantParam("bg", 0.)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('orderHermite', 10)

modelRef.setConstantParam("sldCore", 52.1122e-6) # FeO 4.1809 A
modelRef.setConstantParam("sldShell", 41.8489e-6) # Magnetite 8.3841 A
modelRef.setConstantParam("sldSolvent", 8.01e-6) # Toluene

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')