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

dataRef.loadFromFile('../AH11_plus_1.2T_LA_scaled.dat', ['p', 'la'])
dataRef.loadFromFile('../AH11_minus_1.2T_LA_scaled.dat', ['m', 'la'])
dataRef.loadFromFile('../AH11_plus_1.2T_SA.dat', ['p', 'sa'])
dataRef.loadFromFile('../AH11_minus_1.2T_SA.dat', ['m', 'sa'])

dataRef.sliceDomain(0, 0.5)

modelRef = app.setModel(SuperballCS, [Magnetic, InstrumentalResolution])
modelRef.setParam("magSldCore", 5.239999999999999e-07,  minVal = 0, maxVal = 2e-06, vary = True)
modelRef.setConstantParam("sin2alpha", 0.9974654)

modelRef.setConstantParam("i0", 0.19538960)
modelRef.setConstantParam("sldCore", 6.6312e-06)
modelRef.setConstantParam("d", 11.5721385)
modelRef.setConstantParam("sldShell", 1.3935e-06)
modelRef.setConstantParam("dTheta_sa", 0.00315176)
modelRef.setConstantParam("dTheta_la", 0.00381881)
modelRef.setConstantParam("bg", 0.00409023)

modelRef.setConstantParam("r", 46.9420801)
modelRef.setConstantParam("pVal", 2.65742743)
modelRef.setConstantParam("sigR", 0.11870446)

modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.setConstantParam("r", 46.9420801)
modelRef.setConstantParam("pVal", 2.65742743)
modelRef.setConstantParam("sigR", 0.11870446)

modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam("magSldShell", 0)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')