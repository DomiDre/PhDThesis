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
modelRef.setParam("particleSize", 54.6377495,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("d", 13.1833002,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("pVal", 2.61015508,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("sigParticleSize", 0.06440415,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.02056698,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("bg", 0.)
modelRef.setConstantParam('orderHermite', 20)
modelRef.setConstantParam('orderLegendre', 20)
modelRef.setConstantParam("sldCore", 51.22e-6)
modelRef.setConstantParam("sldShell", 41.28e-6)
modelRef.setConstantParam("sldSolvent", 8.01e-6)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')