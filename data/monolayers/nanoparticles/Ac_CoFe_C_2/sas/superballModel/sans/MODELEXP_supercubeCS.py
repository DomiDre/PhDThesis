#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SuperballCSOA, DataResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = Cli()
app.setExperiment(Sans)
dataRef = app.setData(XyerData)


dataRef.loadFromFile('../../experimentalData/YF45_nuclear_SA.dat', ['sa'])
dataRef.loadFromFile('../../experimentalData/YF45_nuclear_LA_scaled.dat', ['la'])
dataRef.sliceDomain(0., 0.25)

modelRef = app.setModel(SuperballCSOA, DataResolution)
modelRef.setResolution()

#    r:              42.89598 (fixed)
#    d:              16.8218933 +/- 0.40860616 (2.43%) (init = 11.23638)
#    pVal:           2.164725 (fixed)
#    sldCore:        6.132e-06 (fixed)
#    sldShell:       7.8e-08 (fixed)
#    sldSolvent:     5.664e-06 (fixed)
#    sigR:           0.1503024 (fixed)
#    i0:             0.02121094 +/- 0.00134805 (6.36%) (init = 0.02929779)
#    bg:             0.00448148 +/- 3.0998e-04 (6.92%) (init = 0.00394841)
#    orderHermite:   10 (fixed)
#    orderLegendre:  10 (fixed)
#    i0Oleic:        0.40822231 +/- 0.08602899 (21.07%) (init = 0.4289)
#    rOleic:         20.3698272 +/- 0.76020661 (3.73%) (init = 23.36)
modelRef.setParam("i0", 0.02121,  minVal = 0, maxVal = 0.6, vary = True)
modelRef.setParam("d", 16.8218933,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("bg", 0.00448148, minVal = 0, maxVal = 0.01, vary = True)

modelRef.setParam("rOleic", 20.3698,  minVal = 0, maxVal = 40, vary = True)
modelRef.setParam("i0Oleic", 0.40822,  minVal = 0, maxVal = 10, vary = True)

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