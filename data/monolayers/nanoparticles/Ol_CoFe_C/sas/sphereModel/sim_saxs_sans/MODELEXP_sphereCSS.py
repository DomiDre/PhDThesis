#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SphereCSSCoupled, DataResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import numpy as np
from fortSAS import sphere
app = App()
app.setExperiment(Saxs)
dataRef = app.setData(XyerData)

dataRef.loadFromFile('../../experimental_data/DD67.xye')#, ['saxs'], 0.1)
# dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_sa.dat', ['sans', 'sa'])
# dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_la_scaled.dat', ['sans', 'la'])
dataRef.sliceDomain(0.004, 0.3)
dataRef.plotData()

ratio = 2.49
a_wustite = 4.2125
a_spinell = 8.4384

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
class ModifiedSphereCSSCoupledOA(SphereCSSCoupled):
  def calcSLD(self):
    x = self.params['x'].value
    particleSize = self.params['particleSize'].value
    dShell = self.params['dShell'].value
    rCore = particleSize - dShell
    vol_wustite = 4/3*np.pi*rCore**3
    vol_spinell = 4/3*np.pi*particleSize**3 - vol_wustite
    nu = (a_spinell / a_wustite)**3 * vol_wustite / vol_spinell
    y = (2 + ratio)*x/(nu*(1+ratio)) + (nu*ratio - 6)/(nu*(1+ratio))
    # if 'saxs' in self.suffix:
    self.params['sldCore'].value = 4 * (y * electron_density['Fe'] + (1-y)*electron_density['Co'] + electron_density['O']) / a_wustite**3
    self.params['sldShell'].value = 8 * (x*electron_density['Co'] + (3-x)*electron_density['Fe'] + 4*electron_density['O']) / a_spinell**3
    #   self.ptrModelContainer.params['sldCore_saxs'].value = self.params['sldCore'].value
    #   self.ptrModelContainer.params['sldShell_saxs'].value = self.params['sldShell'].value
    # elif 'sans' in self.suffix:
    #   self.params['sldCore'].value = 4 * (y * b['Fe'] + (1-y)*b['Co'] + b['O']) / a_wustite**3
    #   self.params['sldShell'].value = 8 * (x*b['Co'] + (3-x)*b['Fe'] + 4*b['O']) / a_spinell**3
    #   self.ptrModelContainer.params['sldCore_sans'].value = self.params['sldCore'].value
    #   self.ptrModelContainer.params['sldShell_sans'].value = self.params['sldShell'].value

  def initParameters(self):
    super().initParameters()
    self.params.add('x', 0.5, min=0, max=1, vary=True)
    self.params['sldCore'].vary = False
    self.params['sldShell'].vary = False
    self.params.add('i0Oleic', 1)
    self.params.add('rOleic', 20)
    # self.calcSLD()

  def calcModel(self):
    self.calcSLD()
    super().calcModel()
    self.I = self.I + self.params['i0Oleic'] * sphere.formfactor(
      self.q,
      self.params['rOleic'],
      self.params['sldSurfactant'],
      self.params['sldSolvent'],
      0
    )


modelRef = app.setModel(ModifiedSphereCSSCoupledOA, DataResolution)
modelRef.setResolution(['sans'])

modelRef.setParam("particleSize", 62.692238695787374,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("dShell", 4.471564916608581,  minVal = 0, maxVal = 50, vary = True)
modelRef.setParam("dSurfactant", 23.158650546905605,  minVal = 0, maxVal = 50, vary = True)
modelRef.setParam("sigParticleSize", 0.09471418224130146,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam('sigD', 0.0, minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.018764708159967336,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0Oleic", 0.2455796235523111,  minVal = 0, maxVal = 1, vary = True)
# modelRef.setParam("i0_sans", 0.09139518085784448,  minVal = 0, maxVal = 1, vary = True)
# modelRef.setParam("bg_sans", 0.015903903940622206,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("rOleic", 21)
modelRef.setConstantParam("sldSurfactant", 8.52e-6)
modelRef.setConstantParam("sldSolvent", 8.01e-06)
modelRef.setConstantParam("sldCore", 0)
modelRef.setConstantParam("sldShell",0)
# modelRef.setConstantParam("sldSurfactant_saxs", 8.52e-6)
# modelRef.setConstantParam("sldSolvent_saxs", 8.01e-06)
# modelRef.setConstantParam("sldCore_saxs", 0)
# modelRef.setConstantParam("sldShell_saxs",0)
# modelRef.setConstantParam("sldSurfactant_sans", 0.078e-6)
# modelRef.setConstantParam("sldSolvent_sans", 5.664e-6)
# modelRef.setConstantParam("sldCore_sans", 0)
# modelRef.setConstantParam("sldShell_sans",0)

modelRef.setConstantParam('x', 1)
modelRef.setConstantParam('bg', 0)
# modelRef.setConstantParam('bg_saxs', 0)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)
app.show()