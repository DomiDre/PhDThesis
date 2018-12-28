#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SuperballCSSCoupledOA, DataResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

import scipy as sp

b = {
  'Co': 2.49e-5,
  'Fe': 9.45e-5,
  'O': 5.803e-5,
}

ratio = 2.49
def superballVolume(r, p):
  def B(x,y):
    return sp.special.gamma(x)*sp.special.gamma(y)/sp.special.gamma(x+y)
  return 2/p**2 * B(1/(2*p), (2*p+1)/(2*p)) * B(1/(2*p), (p+1)/p) * r**3
a_spinell = 8.4384
a_wustite = 4.2125

class ModifiedSuperballCSSCoupledOA(SuperballCSSCoupledOA):
  def calcSLD(self):
    x = self.params['x'].value
    pVal = self.params['pVal'].value
    particleSize = self.params['particleSize'].value
    dShell = self.params['dShell'].value
    rCore = particleSize - dShell
    vol_wustite = superballVolume(rCore, pVal)
    vol_spinell = superballVolume(particleSize, pVal) - vol_wustite
    nu = (a_spinell / a_wustite)**3 * vol_wustite / vol_spinell
    y = (2 + ratio)*x/(nu*(1+ratio)) + (nu*ratio - 6)/(nu*(1+ratio))
    self.params['sldCore'].value = 4 * (y * b['Fe'] + (1-y)*b['Co'] + b['O']) / a_wustite**3
    self.params['sldShell'].value = 8 * (x*b['Co'] + (3-x)*b['Fe'] + 4*b['O']) / a_spinell**3
    print(x, y, self.params['sldCore'].value, self.params['sldShell'].value)
  
  def initParameters(self):
    super().initParameters()
    self.params.add('x', 0.5, min=0, max=1, vary=True)
    self.params['sldCore'].vary = False
    self.params['sldShell'].vary = False
    self.calcSLD()

  def calcModel(self):
    self.calcSLD()
    super().calcModel()

app = Cli()
app.setExperiment(Sans)
dataRef = app.setData(XyerData)


dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_sa.dat', ['sa'])
dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_la_scaled.dat', ['la'])
dataRef.sliceDomain(0.004, 0.26)

modelRef = app.setModel(ModifiedSuperballCSSCoupledOA, DataResolution)
modelRef.setResolution()


modelRef.setParam("dSurfactant", 14.4889664,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("i0", 0.17639958,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("bg", 0.01817,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0Oleic", 0.83781846, minVal = 0, maxVal = 20, vary=True)
modelRef.setParam("x", 0.84480928, minVal = 0, maxVal = 1, vary=True)

modelRef.setConstantParam("dShell", 18.9612785)
modelRef.setConstantParam("rOleic", 21)
modelRef.setConstantParam("particleSize", 54.3975573)
modelRef.setConstantParam("pVal", 2.26861847)
modelRef.setConstantParam("sigParticleSize", 0.07116433)

# modelRef.setConstantParam("sldCore", 7.082e-6)
modelRef.setConstantParam("sldSurfactant", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.664e-6)
modelRef.setConstantParam('orderHermite', 5)
modelRef.setConstantParam('orderLegendre', 5)

fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.fit()
fit.exportResult('fit_result.dat')