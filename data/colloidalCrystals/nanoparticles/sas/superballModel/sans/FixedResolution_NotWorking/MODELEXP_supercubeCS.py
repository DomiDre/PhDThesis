#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SuperballCSSCoupledOA, InstrumentalResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = Cli()
expRef = app.setExperiment(Sans)
expRef.setResiduumFormula('log chi2 noError')
dataRef = app.setData(XyerData)


dataRef.loadFromFile('../../experimental_data/DD144_0A_nuc_SA.dat', ['sa'])
dataRef.loadFromFile('../../experimental_data/DD144_0A_nuc_LA.dat', ['la'])
dataRef.sliceDomain(0.02, 0.5)

modelRef = app.setModel(SuperballCSSCoupledOA, InstrumentalResolution)

modelRef.setParam("dShell", 27.0684415, minVal = 0, maxVal = 70, vary=True)
modelRef.setParam("dSurfactant", 14.9448111,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("i0", 0.03685254,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg", 0.00136043,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0Oleic", 0.20838644, minVal = 0, maxVal = 5, vary=True)

modelRef.setConstantParam("pVal", 2.17635593)
modelRef.setConstantParam("particleSize", 61.1466380)
modelRef.setConstantParam("rOleic", 21)
modelRef.setConstantParam("sigParticleSize", 0.07531189)
modelRef.setConstantParam("dTheta_sa", 0.0021)
modelRef.setConstantParam("dTheta_la", 0.0038)

modelRef.setConstantParam("sldCore", 8.34845e-6) # FeO 4.1809 A
modelRef.setConstantParam("sldShell", 6.9992e-6) # Fe3O4 8.3841 A
modelRef.setConstantParam("sldSurfactant", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.664e-6)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.save_intermediate_results_every = 1
fit.fit()
fit.exportResult('fit_result.dat')