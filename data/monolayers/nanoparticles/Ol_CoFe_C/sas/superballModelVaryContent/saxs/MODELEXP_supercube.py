#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SuperballCSCoupled
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = Cli()
expRef = app.setExperiment(Saxs)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/DD67.xye')
dataRef.sliceDomain(0.005, 0.4)

modelRef = app.setModel(SuperballCSCoupled)
modelRef.setParam("particleSize", 54.9248019,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("d", 19.7888,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("pVal", 2.0155,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("sigParticleSize", 0.0747826,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.02033677,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("sldShell", 46.447e-6, minVal=3e-5, maxVal=5e-5, vary=True)

modelRef.setConstantParam("bg", 0.)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam("sldCore", 51.22e-6)
modelRef.setConstantParam("sldSolvent", 8.01e-6)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')