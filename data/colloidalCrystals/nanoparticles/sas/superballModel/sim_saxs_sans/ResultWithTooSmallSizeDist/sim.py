#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import SimultaneousSaxsSans
from modelexp.models.sas import SuperballCSSCoupledOA, DataResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import datetime
import scipy as sp

app = Cli()
app.setExperiment(SimultaneousSaxsSans)
dataRef = app.setData(XyerData)


dataRef.loadFromFile('../../../experimental_data/DD67.xye', ['saxs'], 10)
dataRef.loadFromFile('../../../experimental_data/DD67_nuclear20_sa.dat', ['sans', 'sa'])
dataRef.loadFromFile('../../../experimental_data/DD67_nuclear20_la_scaled.dat', ['sans', 'la'])
# dataRef.sliceDomain(0.004, 0.26)

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
    if 'saxs' in self.suffix:
      self.params['sldCore'].value = 4 * (y * electron_density['Fe'] + (1-y)*electron_density['Co'] + electron_density['O']) / a_wustite**3
      self.params['sldShell'].value = 8 * (x*electron_density['Co'] + (3-x)*electron_density['Fe'] + 4*electron_density['O']) / a_spinell**3
    elif 'sans' in self.suffix:
      self.params['sldCore'].value = 4 * (y * b['Fe'] + (1-y)*b['Co'] + b['O']) / a_wustite**3
      self.params['sldShell'].value = 8 * (x*b['Co'] + (3-x)*b['Fe'] + 4*b['O']) / a_spinell**3
    else:
      print('SOMETHING WRONG')
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


modelRef = app.setModel(ModifiedSuperballCSSCoupledOA, DataResolution)
modelRef.setResolution(['sans'])

modelRef.setParam("particleSize", 52.6233879,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("dShell", 24.4418791,  minVal = 0, maxVal = 50, vary = True)
modelRef.setParam("dSurfactant", 13.0346824,  minVal = 0, maxVal = 50, vary = True)
modelRef.setParam("pVal", 5.249,  minVal = 1, maxVal = 100, vary = True)
modelRef.setParam("sigParticleSize", 0.03809988,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0_saxs", 0.02571824,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("i0Oleic", 0.90053992, minVal = 0, maxVal = 100, vary=True)
modelRef.setParam("x", 1, minVal = 0, maxVal = 1, vary=False)
modelRef.setParam("i0_sans", 0.18020533,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("bg_sans", 0.01184569,  minVal = 0, maxVal = 0.1, vary = True)


modelRef.setConstantParam("rOleic", 21)
modelRef.setConstantParam("sldSurfactant_saxs", 8.52e-6)
modelRef.setConstantParam("sldSurfactant_sans", 0.078e-6)
modelRef.setConstantParam("sldSolvent_saxs", 8.01e-06)
modelRef.setConstantParam("sldSolvent_sans", 5.664e-6)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('bg_saxs', 0)

modelRef.updateModel()

# save model
modelData_saxs = modelRef.getModelset(0)
modelData_sa = modelRef.getModelset(1)
modelData_la = modelRef.getModelset(2)
q_saxs = modelData_saxs.getDomain()
I_saxs = modelData_saxs.getValues()
r_saxs = modelData_saxs.r
sld_saxs = modelData_saxs.sld
q_sa = modelData_sa.getDomain()
I_sa = modelData_sa.getValues()
r_sa = modelData_sa.r
sld_sa = modelData_sa.sld
q_la = modelData_la.getDomain()
I_la = modelData_la.getValues()
r_la = modelData_la.r
sld_la = modelData_la.sld

modelRef.params['sldCore_sans'].value = modelData_la.params['sldCore'].value
modelRef.params['sldShell_sans'].value = modelData_la.params['sldShell'].value
modelRef.params['sldCore_saxs'].value = modelData_saxs.params['sldCore'].value
modelRef.params['sldShell_saxs'].value = modelData_saxs.params['sldShell'].value

with open(f'superballData_simulation.xy', 'w') as f:
  f.write(f'#Superball Data generated at {datetime.datetime.now()}\n')
  f.write(f'#[[Parameters]]\n')
  for param in modelRef.params:
    f.write(f'#{param}\t{modelRef.params[param].value}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] saxs\n')
  f.write(f'#q\tI\n')
  for j in range(len(q_saxs)):
    f.write(f'{q_saxs[j]}\t{I_saxs[j]}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] sans_sa\n')
  f.write(f'#q\tI\n')
  for j in range(len(q_sa)):
    f.write(f'{q_sa[j]}\t{I_sa[j]}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] sans_la\n')
  f.write(f'#q\tI\n')
  for j in range(len(q_la)):
    f.write(f'{q_la[j]}\t{I_la[j]}\n')

with open(f'superballData_simulation_sld.xy', 'w') as f:
  f.write(f'#Superball Data generated at {datetime.datetime.now()}\n')
  f.write(f'#[[Parameters]]\n')
  for param in modelRef.params:
    f.write(f'#{param}\t{modelRef.params[param].value}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] saxs\n')
  f.write(f'#r\tsld\n')
  for j in range(len(r_saxs)):
    f.write(f'{r_saxs[j]}\t{sld_saxs[j]}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] sans_sa\n')
  f.write(f'#r\tsld\n')
  for j in range(len(r_sa)):
    f.write(f'{r_sa[j]}\t{sld_sa[j]}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] sans_la\n')
  f.write(f'#r\tsld\n')
  for j in range(len(r_la)):
    f.write(f'{r_la[j]}\t{sld_la[j]}\n')