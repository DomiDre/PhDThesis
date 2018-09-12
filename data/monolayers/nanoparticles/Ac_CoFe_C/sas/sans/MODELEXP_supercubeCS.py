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


dataRef.loadFromFile('../YF45_nuclear_SA.dat', ['sa'])
dataRef.loadFromFile('../YF45_nuclear_LA.dat', ['la'])
dataRef.sliceDomain(0., 0.25)

modelRef = app.setModel(SuperballCS, InstrumentalResolution)

modelRef.setParam("i0", 0.10093954,  minVal = 0, maxVal = 0.6, vary = True)
modelRef.setParam("d", 11.2363778,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("sldCore", 6.9385e-06,  minVal = 4.293e-06, maxVal = 7.289e-06, vary = True)
modelRef.setParam("dTheta_sa", 0.00195257,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("dTheta_la", 0.00337370,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("bg", 0.00394841, minVal = 0, maxVal = 0.01, vary = True)

modelRef.setConstantParam("r", 42.8959582)
modelRef.setConstantParam("pVal", 2.16474488)
modelRef.setConstantParam("sigR", 0.15030187)

modelRef.setConstantParam("sldShell", sld_neutrons_5A['Oleic Acid'])
modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')