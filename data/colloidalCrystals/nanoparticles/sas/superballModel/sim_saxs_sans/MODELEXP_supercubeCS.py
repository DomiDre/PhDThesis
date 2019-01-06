from modelexp import Cli
from modelexp.experiments.sas import SimultaneousSaxsSans
from modelexp.models.sas import SuperballCSSCoupledSigDOA, DataResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

app = Cli()
expRef = app.setExperiment(SimultaneousSaxsSans)
expRef.setFitRange(0.02, 0.3)
expRef.setResiduumFormula("log chi2 noError")

dataRef = app.setData(XyerData)

dataRef.loadFromFile('../../experimental_data/DD144.xye', ['saxs'], 1)
dataRef.loadFromFile('../../experimental_data/DD144_0A_nuc_SA.dat', ['sans', 'sa'])
dataRef.loadFromFile('../../experimental_data/DD144_0A_nuc_LA.dat', ['sans', 'la'])
# dataRef.reducePointDensity(4)
dataRef.sliceDomain(0.02,0.3)

modelRef = app.setModel(SuperballCSSCoupledSigDOA, DataResolution)
modelRef.setResolution(['sans'])
modelRef.setParam("particleSize",     60.5046326,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("dShell",           29.0657183,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("dSurfactant",      15.9187433,  minVal = 0, maxVal = 50, vary = True)
modelRef.setParam("pVal",             3.13550130,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sigParticleSize",  0.06835789,  minVal = 0, maxVal = 0.5, vary = True)
modelRef.setParam("sigD",             0.50,  minVal = 0, maxVal = 3, vary = True)
modelRef.setParam("i0_saxs",          0.02574363,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0Oleic",          0.54232130, minVal = 0, maxVal = 100, vary=True)
modelRef.setParam("i0_sans",          0.03205054,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("bg_sans",          0.00137358,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("rOleic", 21)

modelRef.setConstantParam("sldCore_saxs", 52.1122e-6) # FeO 4.1809 A
modelRef.setConstantParam("sldCore_sans", 8.34845e-6) # FeO 4.1809 A

modelRef.setConstantParam("sldShell_saxs", 41.8489e-6) # Magnetite 8.3841 A
modelRef.setConstantParam("sldShell_sans", 6.9992e-6)

modelRef.setConstantParam("sldSurfactant_saxs", 8.52e-6)
modelRef.setConstantParam("sldSurfactant_sans", 0.078e-6)

modelRef.setConstantParam("sldSolvent_saxs", 8.01e-6) # Toluene
modelRef.setConstantParam("sldSolvent_sans", 5.664e-6) # Toluene-d8

modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)

modelRef.setConstantParam('bg_saxs', 0)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.save_intermediate_results_every = 1
fit.fit()
fit.exportResult('fit_result.dat')