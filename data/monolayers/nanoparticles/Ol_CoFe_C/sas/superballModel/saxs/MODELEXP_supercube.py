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

dataRef.loadFromFile('../../experimental_data/DD67.xye')
dataRef.sliceDomain(0.005, 0.3)
dataRef.reducePointDensity(4)

a_wustite = 4.2125
a_spinell = 8.4384
ratio = 2.49
def superballVolume(r, p):
  def B(x,y):
    return sp.special.gamma(x)*sp.special.gamma(y)/sp.special.gamma(x+y)
  return 2/p**2 * B(1/(2*p), (2*p+1)/(2*p)) * B(1/(2*p), (p+1)/p) * r**3


b = {
  'Co': 2.49e-5,
  'Fe': 9.45e-5,
  'O': 5.803e-5,
}

r_e = 2.8179403e-5 #A
electron_density = {
  'Co': 26.3717*r_e,
  'Fe':   25.7468*r_e,
  'O': 8.04077*r_e,
}

class ModifiedSuperballCSCoupled(SuperballCSCoupledSigD):
  def calcSLD(self):
    x = self.params['x'].value
    pVal = self.params['pVal'].value
    particleSize = self.params['particleSize'].value
    dShell = self.params['d'].value
    rCore = particleSize - dShell
    vol_wustite = superballVolume(rCore, pVal)
    vol_spinell = superballVolume(particleSize, pVal) - vol_wustite
    nu = (a_spinell / a_wustite)**3 * vol_wustite / vol_spinell
    y = 2*x/nu + (nu*ratio - 6) / (nu*(1+ratio))
    self.params['sldCore'].value = 4 * (y * electron_density['Fe'] + (1-y)*electron_density['Co'] + electron_density['O']) / a_wustite**3
    self.params['sldShell'].value = 8 * (x*electron_density['Co'] + (3-x)*electron_density['Fe'] + 4*electron_density['O']) / a_spinell**3
    self.ptrModelContainer.params['sldCore'].value = self.params['sldCore'].value
    self.ptrModelContainer.params['sldShell'].value = self.params['sldShell'].value
    print(x, y)
  def initParameters(self):
    super().initParameters()
    self.params.add('x', 0.5, min=0, max=1, vary=True)
    self.params['sldCore'].vary = False
    self.params['sldShell'].vary = False

  def calcModel(self):
    self.calcSLD()
    super().calcModel()
    # particleSize:     54.1762098 (init = 51.81424)
    # d:                21.2107393 (init = 6.252337)
    # pVal:             2.41359662 (init = 3.337198)
    # sldCore:          5.111393e-05 (fixed)
    # sldShell:         4.127803e-05 (fixed)
    # sldSolvent:       7.55e-06 (fixed)
    # sigParticleSize:  0.07546698 (init = 0.06081491)
    # sigD:             0.39874919 (init = 0.2325013)
    # i0:               0.02381543 (init = 0.02755086)
    # bg:               0 (fixed)
    # orderHermite:     5 (fixed)
    # orderLegendre:    10 (fixed)
    # x:                0.98894968 (init = 0.4283)
modelRef = app.setModel(ModifiedSuperballCSCoupled)
modelRef.setParam("particleSize",     54.1851544,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("d",                21.1855186,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("pVal",             2.47376320,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sigParticleSize",  0.07143705,  minVal = 0, maxVal = 0.5, vary = True)
modelRef.setParam("sigD",             0.40385040,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0",               0.02369477,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("x",                0.98606207,  minVal = 0, maxVal = 1, vary = True)

# modelRef.setConstantParam('x', 1)
modelRef.setConstantParam("bg", 0.)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam("sldSolvent", 7.55e-6)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')