#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SuperballCS, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = Cli()
app.setExperiment(Sans)
dataRef = app.setData(XyeData)


dataRef.loadFromFile('../DD67_nuclear20_sa.dat', ['sa'])
dataRef.loadFromFile('../DD67_nuclear20_la_scaled.dat', ['la'])
dataRef.sliceDomain(0.004, 0.5)

modelRef = app.setModel(SuperballCS, InstrumentalResolution)
modelRef.setParam("i0", 0.18342268,  minVal = 0, maxVal = 0.6, vary = True)
modelRef.setParam("d", 16.0355329,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("sldCore", 6.4968e-06,  minVal = 4.293e-06, maxVal = 7.289e-06, vary = True)
modelRef.setParam("dTheta_sa", 0.0010312,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("dTheta_la", 0.00150274,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("bg", 0.00999, minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("r", 56.2265926)
modelRef.setConstantParam("pVal", 1.53773769)
modelRef.setConstantParam("sigR", 0.09266898)

modelRef.setConstantParam("sldShell", sld_neutrons_5A['Oleic Acid'])
modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')