#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sanspol
from modelexp.models.sas import SuperballCS, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_neutrons_5A

app = Cli()
app.setExperiment(Sanspol)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../YF45_plus_1.2T_LA.dat', ['p', 'la'])
dataRef.loadFromFile('../YF45_minus_1.2T_LA.dat', ['m', 'la'])
dataRef.loadFromFile('../YF45_plus_1.2T_SA.dat', ['p', 'sa'])
dataRef.loadFromFile('../YF45_minus_1.2T_SA.dat', ['m', 'sa'])

dataRef.sliceDomain(0, 0.25)

modelRef = app.setModel(SuperballCS, [Magnetic, InstrumentalResolution])
modelRef.setParam("magSldCore", 7.9162e-07,  minVal = 0, maxVal = 2e-06, vary = True)
modelRef.setConstantParam("sin2alpha", 0.9974654)

modelRef.setConstantParam("i0", 0.10093954)
modelRef.setConstantParam("d", 11.2363778)
modelRef.setConstantParam("sldCore", 6.9385e-06)
modelRef.setConstantParam("dTheta_sa", 0.00195257)
modelRef.setConstantParam("dTheta_la", 0.00337370)
modelRef.setConstantParam("bg", 0.00394841)

modelRef.setConstantParam("r", 42.8959582)
modelRef.setConstantParam("pVal", 2.16474488)
modelRef.setConstantParam("sigR", 0.15030187)

modelRef.setConstantParam("sldShell", sld_neutrons_5A['Oleic Acid'])
modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam("magSldShell", 0)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.updateModel()
fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')