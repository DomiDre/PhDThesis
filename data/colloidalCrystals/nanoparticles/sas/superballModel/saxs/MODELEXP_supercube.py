#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SuperballCSCoupledSigD
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

app = Cli()
expRef = app.setExperiment(Saxs)
expRef.setFitRange(0.02, 0.3)
dataRef = app.setData(XyerData)

dataRef.loadFromFile('../../experimental_data/DD144.xye')
dataRef.reducePointDensity(4)

modelRef = app.setModel(SuperballCSCoupledSigD)
modelRef.setParam("particleSize",     59.6324049,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("d",                44.6297852,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("pVal",             3.05439927,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sigParticleSize",  0.06563234,  minVal = 0, maxVal = 0.5, vary = True)
modelRef.setParam("sigD",             0.0,  minVal = 0, maxVal = 3, vary = False)
modelRef.setParam("i0",               0.02981003,  minVal = 0, maxVal = 0.1, vary = True)

# modelRef.setConstantParam('x', 1)
modelRef.setConstantParam("bg", 0.)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('orderHermite', 10)

modelRef.setConstantParam("sldCore", 52.1122e-6) # FeO 4.1809 A
modelRef.setConstantParam("sldShell", 41.8489e-6) # Magnetite 8.3841 A
modelRef.setConstantParam("sldSolvent", 8.01e-6) # Toluene

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.save_intermediate_results_every = 1
fit.fit()
fit.exportResult('fit_result.dat')