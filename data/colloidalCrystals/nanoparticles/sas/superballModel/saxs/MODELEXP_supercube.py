#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SuperballCSCoupledSigD
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import scipy as sp

app = Cli()
expRef = app.setExperiment(Saxs)
dataRef = app.setData(XyerData)

dataRef.loadFromFile('../../experimental_data/DD144.xye')
dataRef.sliceDomain(0.005, 0.3)
dataRef.reducePointDensity(4)

a_wustite = 4.1809092
a_spinell = 8.3841209

def superballVolume(r, p):
  def B(x,y):
    return sp.special.gamma(x)*sp.special.gamma(y)/sp.special.gamma(x+y)
  return 2/p**2 * B(1/(2*p), (2*p+1)/(2*p)) * B(1/(2*p), (p+1)/p) * r**3

b = {
  'Fe': 9.45e-5,
  'O': 5.803e-5,
}

r_e = 2.8179403e-5 #A
electron_density = {
  'Fe':   25.7468*r_e,
  'O': 8.04077*r_e,
}

sldCore = 4 * (electron_density['Fe'] + electron_density['O']) / a_wustite**3
sldShell = 8 * ( 3*electron_density['Fe'] + 4*electron_density['O'] ) / a_spinell**3

modelRef = app.setModel(SuperballCSCoupledSigD)
modelRef.setParam("particleSize",     65.1851544,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("d",                21.1855186,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("pVal",             2.47376320,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sigParticleSize",  0.07143705,  minVal = 0, maxVal = 0.5, vary = True)
modelRef.setParam("sigD",             0.40385040,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0",               0.02369477,  minVal = 0, maxVal = 0.1, vary = True)

# modelRef.setConstantParam('x', 1)
modelRef.setConstantParam("bg", 0.)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam("sldSolvent", 7.55e-6)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')