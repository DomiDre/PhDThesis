#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import SimultaneousSaxsSans
from modelexp.models.sas import SuperballCSSCoupledSigDOA, DataResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import scipy as sp
app = Cli()
app.setExperiment(SimultaneousSaxsSans)
dataRef = app.setData(XyerData)

dataRef.loadFromFile('../../experimental_data/DD67.xye', ['saxs'], 1)
dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_sa.dat', ['sans', 'sa'])
dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_la_scaled.dat', ['sans', 'la'])
dataRef.sliceDomain(0.004, 0.3)
dataRef.reducePointDensity(2)

ratio = 2.49
a_wustite = 4.2125
a_spinell = 8.4384

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
class ModifiedSuperballCSSCoupledSigDOA(SuperballCSSCoupledSigDOA):
  def calcSLD(self):
    x = self.params['x'].value
    pVal = self.params['pVal'].value
    particleSize = self.params['particleSize'].value
    dShell = self.params['dShell'].value
    rCore = particleSize - dShell
    vol_wustite = superballVolume(rCore, pVal)
    vol_spinell = superballVolume(particleSize, pVal) - vol_wustite
    nu = (a_spinell / a_wustite)**3 * vol_wustite / vol_spinell
    y = 2*x/nu + (nu*ratio - 6)/(nu*(1+ratio))
    if 'saxs' in self.suffix:
      self.params['sldCore'].value = 4 * (y * electron_density['Fe'] + (1-y)*electron_density['Co'] + electron_density['O']) / a_wustite**3
      self.params['sldShell'].value = 8 * (x*electron_density['Co'] + (3-x)*electron_density['Fe'] + 4*electron_density['O']) / a_spinell**3
      self.ptrModelContainer.params['sldCore_saxs'].value = self.params['sldCore'].value
      self.ptrModelContainer.params['sldShell_saxs'].value = self.params['sldShell'].value
    elif 'sans' in self.suffix:
      self.params['sldCore'].value = 4 * (y * b['Fe'] + (1-y)*b['Co'] + b['O']) / a_wustite**3
      self.params['sldShell'].value = 8 * (x*b['Co'] + (3-x)*b['Fe'] + 4*b['O']) / a_spinell**3
      self.ptrModelContainer.params['sldCore_sans'].value = self.params['sldCore'].value
      self.ptrModelContainer.params['sldShell_sans'].value = self.params['sldShell'].value
    print(x, y, self.params['sldCore'].value, self.params['sldShell'].value)

  def initParameters(self):
    super().initParameters()
    self.params.add('x', 0.5, min=0, max=1, vary=True)
    self.params['sldCore'].vary = False
    self.params['sldShell'].vary = False
    # self.calcSLD()

  def calcModel(self):
    self.calcSLD()
    super().calcModel()

modelRef = app.setModel(ModifiedSuperballCSSCoupledSigDOA, DataResolution)
modelRef.setResolution(['sans'])
modelRef.setParam("particleSize",     51.3053730,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("dShell",           34.3394593,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("dSurfactant",      15.7933194,  minVal = 0, maxVal = 50, vary = True)
modelRef.setParam("pVal",             4.09294505,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sigParticleSize",  0.06232648,  minVal = 0, maxVal = 0.5, vary = True)
modelRef.setParam("sigD",             0.17779981,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0_saxs",          0.02996434,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("x",                0.8243,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0Oleic",         0.69001465, minVal = 0, maxVal = 100, vary=True)
modelRef.setParam("i0_sans",         0.13027763,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("bg_sans",         0.01358112,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("rOleic", 21)
modelRef.setConstantParam("sldSurfactant_saxs", 8.52e-6)
modelRef.setConstantParam("sldSurfactant_sans", 0.078e-6)
modelRef.setConstantParam("sldSolvent_saxs", 7.55e-06)
modelRef.setConstantParam("sldSolvent_sans", 5.664e-6)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)

modelRef.setConstantParam('bg_saxs', 0)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')