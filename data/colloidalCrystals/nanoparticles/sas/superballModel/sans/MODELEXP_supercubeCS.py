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


modelRef.setParam("dSurfactant", 16.2882927,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("i0", 0.11311443,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("bg", 0.02783424,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0Oleic", 4.985199, minVal = 0, maxVal = 5, vary=True)
modelRef.setParam("sldShell", 5.1879e-06, minVal = 5e-6, maxVal = 7e-6, vary=True)

modelRef.setConstantParam("dShell", 18.9612785)
modelRef.setConstantParam("rOleic", 21)
modelRef.setConstantParam("particleSize", 54.3975573)
modelRef.setConstantParam("pVal", 2.26861847)
modelRef.setConstantParam("sigParticleSize", 0.07116433)

modelRef.setConstantParam("sldCore", 8.34845e-6) # FeO 4.1809 A
modelRef.setConstantParam("sldShell", 6.9992e-6) # Fe3O4 8.3841 A
modelRef.setConstantParam("sldSurfactant", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.664e-6)
modelRef.setConstantParam('orderHermite', 5)
modelRef.setConstantParam('orderLegendre', 5)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')