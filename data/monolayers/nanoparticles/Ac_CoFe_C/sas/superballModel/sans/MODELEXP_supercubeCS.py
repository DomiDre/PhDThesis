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
import datetime
app = Cli()
app.setExperiment(Sans)
dataRef = app.setData(XyeData)


dataRef.loadFromFile('../../experimental_data/AH11_nuclear_SA.dat', ['sa'])
dataRef.loadFromFile('../../experimental_data/AH11_nuclear_LA_scaled.dat', ['la'])
dataRef.sliceDomain(0., 0.25)

modelRef = app.setModel(SuperballCSOA, DataResolution)

modelRef.setParam("d", 14.6708551,  minVal = 0, maxVal = 40, vary = True)
modelRef.setParam("i0", 0.03811865,  minVal = 0.01, maxVal = 0.1, vary = True)
modelRef.setParam("rOleic", 17.7116193,  minVal = 0, maxVal = 40, vary = True)
modelRef.setParam("i0Oleic", 1.91234649,  minVal = 0, maxVal = 10, vary = True)

modelRef.setParam("bg", 0.00272943,  minVal = 0, maxVal = 0.02, vary = True)

modelRef.setConstantParam("r", 46.9420932)
modelRef.setConstantParam("pVal", 2.65741745)
modelRef.setConstantParam("sigR", 0.11870449)

modelRef.setConstantParam("sldCore", 6.198e-6)
modelRef.setConstantParam("sldShell", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.664e-6)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)


fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')