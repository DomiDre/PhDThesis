#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sanspol
from modelexp.models.sas import SuperballCSOA, DataResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_neutrons_5A

app = Cli()
app.setExperiment(Sanspol)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/YF45_plus_1.2T_LA_scaled.dat', ['p', 'la'])
dataRef.loadFromFile('../../experimentalData/YF45_minus_1.2T_LA_scaled.dat', ['m', 'la'])
dataRef.loadFromFile('../../experimentalData/YF45_plus_1.2T_SA.dat', ['p', 'sa'])
dataRef.loadFromFile('../../experimentalData/YF45_minus_1.2T_SA.dat', ['m', 'sa'])

dataRef.sliceDomain(0, 0.25)

modelRef = app.setModel(SuperballCSOA, [Magnetic, DataResolution])
modelRef.setParam("magSldCore", 7.9162e-07,  minVal = 0, maxVal = 2e-06, vary = True)
modelRef.setConstantParam("sin2alpha", 0.9899)

modelRef.setConstantParam("d", 14.1228789)
modelRef.setConstantParam("i0", 0.04103704)
modelRef.setConstantParam("rOleic", 23.3623414)
modelRef.setConstantParam("i0Oleic", 0.42893074)
modelRef.setConstantParam("bg", 0.00612996)

modelRef.setConstantParam("magSldShell", 0)

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