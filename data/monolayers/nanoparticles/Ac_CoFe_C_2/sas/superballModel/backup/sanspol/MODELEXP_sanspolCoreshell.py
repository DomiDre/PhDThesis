#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sanspol
from modelexp.models.sas import SuperballCSOA, DataResolution, Magnetic
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_neutrons_5A

app = Cli()
app.setExperiment(Sanspol)
dataRef = app.setData(XyerData)

dataRef.loadFromFile('../../experimentalData/YF45_plus_1.2T_LA_scaled.dat', ['p', 'la'])
dataRef.loadFromFile('../../experimentalData/YF45_minus_1.2T_LA_scaled.dat', ['m', 'la'])
dataRef.loadFromFile('../../experimentalData/YF45_plus_1.2T_SA.dat', ['p', 'sa'])
dataRef.loadFromFile('../../experimentalData/YF45_minus_1.2T_SA.dat', ['m', 'sa'])

dataRef.sliceDomain(0, 0.25)

modelRef = app.setModel(SuperballCSOA, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("magSldCore", 1.7259e-6,  minVal = 0, maxVal = 2e-06, vary = True)
modelRef.setConstantParam("sin2alpha", 0.9899)

modelRef.setConstantParam("d", 17.0110293)
modelRef.setConstantParam("i0", 0.02060729)
modelRef.setConstantParam("bg", 0.00445686)
modelRef.setConstantParam("i0Oleic", 0.42822500)
modelRef.setConstantParam("rOleic", 20.1857237)

modelRef.setConstantParam("magSldShell", 0)

modelRef.setConstantParam("r", 42.8959813)
modelRef.setConstantParam("pVal", 2.16472545)
modelRef.setConstantParam("sigR", 0.15030238)

modelRef.setConstantParam("sldCore", 6.132e-06)
modelRef.setConstantParam("sldShell", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.664e-6)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')