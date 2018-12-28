#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SuperballCSSCoupledOA, DataResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = Cli()
app.setExperiment(Sans)
dataRef = app.setData(XyerData)


dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_sa.dat', ['sa'])
dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_la_scaled.dat', ['la'])
dataRef.sliceDomain(0.004, 0.26)

modelRef = app.setModel(SuperballCSSCoupledOA, DataResolution)
modelRef.setResolution()

modelRef.setParam("dSurfactant", 19.6987290,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("i0", 0.11178,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("bg", 0.016935,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("dShell", 5.97351175, minVal=0, maxVal = 50, vary=True)

modelRef.setParam("i0Oleic", 1.612192, minVal = 0, maxVal = 5, vary=True)
modelRef.setConstantParam("rOleic", 21)

modelRef.setConstantParam("particleSize", 57.6590717)
modelRef.setConstantParam("pVal", 1.49983)
modelRef.setConstantParam("sigParticleSize", 0.08318968)

modelRef.setConstantParam("sldCore", 7.082e-6)
modelRef.setConstantParam("sldShell", 5.938e-6)
modelRef.setConstantParam("sldSurfactant", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.664e-6)
modelRef.setConstantParam('orderHermite', 5)
modelRef.setConstantParam('orderLegendre', 5)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')