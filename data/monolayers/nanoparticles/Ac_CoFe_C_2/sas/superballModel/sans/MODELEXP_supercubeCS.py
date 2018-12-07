#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SuperballCSOA, DataResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = Cli()
app.setExperiment(Sans)
dataRef = app.setData(XyeData)


dataRef.loadFromFile('../../experimentalData/YF45_nuclear_SA.dat', ['sa'])
dataRef.loadFromFile('../../experimentalData/YF45_nuclear_LA_scaled.dat', ['la'])
dataRef.sliceDomain(0., 0.25)

modelRef = app.setModel(SuperballCSOA, DataResolution)

modelRef.setParam("i0", 0.02929779,  minVal = 0, maxVal = 0.6, vary = True)
modelRef.setParam("d", 11.2363778,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("bg", 0.00394841, minVal = 0, maxVal = 0.01, vary = True)

modelRef.setParam("rOleic", 23.36,  minVal = 0, maxVal = 40, vary = True)
modelRef.setParam("i0Oleic", 0.4289,  minVal = 0, maxVal = 10, vary = True)

modelRef.setConstantParam("r", 42.8959813)
modelRef.setConstantParam("pVal", 2.16472545)
modelRef.setConstantParam("sigR", 0.15030238)

modelRef.setConstantParam("sldCore", 6.132e-06)
modelRef.setConstantParam("sldShell", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.664e-6)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)

modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')