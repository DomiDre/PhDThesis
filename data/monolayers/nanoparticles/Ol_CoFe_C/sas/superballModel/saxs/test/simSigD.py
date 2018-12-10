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

import datetime

app = Cli()
expRef = app.setExperiment(Saxs)
dataRef = app.setData(XyerData)

dataRef.loadFromFile('../../../experimental_data/DD67.xye')
dataRef.sliceDomain(0.005, 0.3)
dataRef.reducePointDensity(2)

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
    y = (2 + ratio)*x/(nu*(1+ratio)) + (nu*ratio - 6)/(nu*(1+ratio))
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


modelRef = app.setModel(ModifiedSuperballCSCoupled)

modelRef.setParam("i0",               0.02457670,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("particleSize",     53.1285814,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("d",                22.7277094,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("pVal",             2.5,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("sigParticleSize",  0.08,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("sigD",  0.2,  minVal = 0, maxVal = 0.5, vary = True)

modelRef.setConstantParam('x', 1)
modelRef.setConstantParam("bg", 0.)
modelRef.setConstantParam('orderHermite', 5)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam("sldSolvent", 8.01e-6)


modelRef.updateModel()

# save model
modelData_sa = modelRef.getModelset(0)
q_sa = modelData_sa.getDomain()
I_sa = modelData_sa.getValues()
with open(f'superballData_simulation.xy', 'w') as f:
  f.write(f'#Superball Data generated at {datetime.datetime.now()}\n')
  f.write(f'#[[Parameters]]\n')
  for param in modelRef.params:
    f.write(f'#{param}\t{modelRef.params[param].value}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] sa\n')
  f.write(f'#q\tI\n')
  for j in range(len(q_sa)):
    f.write(f'{q_sa[j]}\t{I_sa[j]}\n')

r_sa = modelData_sa.r
sld_sa = modelData_sa.sld

with open(f'superballData_simulation_sld.xy', 'w') as f:
  f.write(f'#Superball Data generated at {datetime.datetime.now()}\n')
  f.write(f'#[[Parameters]]\n')
  for param in modelRef.params:
    f.write(f'#{param}\t{modelRef.params[param].value}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] sa\n')
  f.write(f'#r\tsld\n')
  for j in range(len(r_sa)):
    f.write(f'{r_sa[j]}\t{sld_sa[j]}\n')