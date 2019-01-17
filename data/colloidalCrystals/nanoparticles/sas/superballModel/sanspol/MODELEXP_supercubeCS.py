#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sanspol
from modelexp.models.sas import SuperballCSSCoupled, InstrumentalResolution, Magnetic
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import scipy as sp
app = Cli()
expRef = app.setExperiment(Sanspol)
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0.02, 0.5)
dataRef = app.setData(XyerData)


dataRef.loadFromFile('../../experimental_data/50A/DD144_50A_20deg_LA_rfm.dat', ['p', 'la'])
dataRef.loadFromFile('../../experimental_data/50A/DD144_50A_20deg_LA_rfp.dat', ['m', 'la'])
dataRef.loadFromFile('../../experimental_data/50A/DD144_50A_20deg_SA_rfm.dat', ['p', 'sa'])
dataRef.loadFromFile('../../experimental_data/50A/DD144_50A_20deg_SA_rfp.dat', ['m', 'sa'])
# dataRef.sliceDomain(0.02, 0.5)

modelRef = app.setModel(SuperballCSSCoupled, [Magnetic, InstrumentalResolution])
modelRef.setParam("magSldCore", 0.92116e-7,  minVal = 0, maxVal = 5e-06, vary = True)
modelRef.setParam("magSldShell", 1.1413e-06,  minVal = 0, maxVal = 5e-06, vary = True) #3.2842e-07 +/- 2.6516e-08 (8.07%)
modelRef.setConstantParam("sin2alpha", 0.9974654)

modelRef.setConstantParam("dShell", 35.6757557)
modelRef.setConstantParam("dSurfactant", 14.1)
modelRef.setConstantParam("i0", 0.05571249)
modelRef.setConstantParam("bg", 0.)
modelRef.setConstantParam("dTheta_sa", 0.00150471)
modelRef.setConstantParam("dTheta_la", 0.00270328)

modelRef.setConstantParam("pVal", 2.17635593)
modelRef.setConstantParam("particleSize", 61.1466380)
modelRef.setConstantParam("sigParticleSize", 0.07531189)

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
