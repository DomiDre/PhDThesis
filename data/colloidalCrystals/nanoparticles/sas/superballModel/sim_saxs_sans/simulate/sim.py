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
import datetime
import scipy as sp

app = Cli()
app.setExperiment(SimultaneousSaxsSans)
dataRef = app.setData(XyerData)


dataRef.loadFromFile('../../../experimental_data/DD67.xye', ['saxs'])
dataRef.loadFromFile('../../../experimental_data/DD67_nuclear20_sa.dat', ['sans', 'sa'])
dataRef.loadFromFile('../../../experimental_data/DD67_nuclear20_la_scaled.dat', ['sans', 'la'])
dataRef.sliceDomain(0.004, 0.3)

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
  'O': 5.803e-5
}

r_e = 2.8179403e-5 # A
electron_density = {
  'Co': 26.3717*r_e,
  'Fe':   25.7468*r_e,
  'O': 8.04077*r_e
}
class ModifiedSuperballCSSCoupledOA(SuperballCSSCoupledSigDOA):
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

  def calcModel(self):
    self.calcSLD()
    super().calcModel()
    # particleSize:        52.9730432 (init = 53.62415)
    # dShell:              24.2804195 (init = 21.98288)
    # dSurfactant:         14.9579410 (init = 15.15999)
    # pVal:                3.65347231 (init = 3.342915)
    # sldCore_saxs:        5.148667e-05 (fixed)
    # sldShell_saxs:       4.128062e-05 (fixed)
    # sldSurfactant_saxs:  8.52e-06 (fixed)
    # sldSolvent_saxs:     8.01e-06 (fixed)
    # sigParticleSize:     0.04814643 (init = 0.05454183)
    # sigD:                0.32003848 (init = 0.3458353)
    # i0_saxs:             0.02538755 (init = 0.02410723)
    # bg_saxs:             0 (fixed)
    # orderHermite:        5 (fixed)
    # orderLegendre:       10 (fixed)
    # i0Oleic:             0.84965279 (init = 0.9518238)
    # rOleic:              21 (fixed)
    # x:                   1 (fixed)
    # sldCore_sans:        6.033778e-06 (fixed)
    # sldShell_sans:       5.938325e-06 (fixed)
    # sldSurfactant_sans:  7.8e-08 (fixed)
    # sldSolvent_sans:     5.664e-06 (fixed)
    # i0_sans:             0.13392160 (init = 0.1225224)
    # bg_sans:             0.01326956 (init = 0.01344027)

modelRef = app.setModel(ModifiedSuperballCSSCoupledOA, DataResolution)
modelRef.setResolution(['sans'])
modelRef.setParam("particleSize",    52.7699958,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("dShell",          18.9209031,  minVal = 0, maxVal = 50, vary = True)
modelRef.setParam("dSurfactant",     12.9039191,  minVal = 0, maxVal = 50, vary = True)
modelRef.setParam("pVal",            3.62864056,  minVal = 1, maxVal = 100, vary = True)
modelRef.setParam("sigParticleSize", 0.05866237,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("sigD",            0.42047532,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0_saxs",         0.02342544,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("i0Oleic",         0.62844234,  minVal = 0, maxVal = 100, vary=True)
modelRef.setParam("x",               0.27099955,           minVal = 0, maxVal = 1, vary=False)
modelRef.setParam("i0_sans",         0.22815262,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("bg_sans",         0.00940958,  minVal = 0, maxVal = 0.1, vary = True)

# modelRef.setParam("particleSize",    52.3400024,  minVal = 0, maxVal = 100, vary = True)
# modelRef.setParam("dShell",          24.6274740,  minVal = 0, maxVal = 50, vary = True)
# modelRef.setParam("dSurfactant",     15.1599864,  minVal = 0, maxVal = 50, vary = True)
# modelRef.setParam("pVal",            5.38836634,  minVal = 1, maxVal = 100, vary = True)
# modelRef.setParam("sigParticleSize", 0.06,  minVal = 0, maxVal = 0.25, vary = True)
# modelRef.setParam("i0_saxs",         0.02591386,  minVal = 0, maxVal = 10, vary = True)
# modelRef.setParam("i0Oleic",         0.95182376, minVal = 0, maxVal = 100, vary=True)
# modelRef.setParam("i0_sans",         0.12252244,  minVal = 0, maxVal = 10, vary = True)
# modelRef.setParam("bg_sans",         0.01344027,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("rOleic", 21)
modelRef.setConstantParam("sldSurfactant_saxs", 8.52e-6)
modelRef.setConstantParam("sldSurfactant_sans", 0.078e-6)
modelRef.setConstantParam("sldSolvent_saxs", 8.01e-06)
modelRef.setConstantParam("sldSolvent_sans", 5.664e-6)
modelRef.setConstantParam('orderHermite', 5)
modelRef.setConstantParam('orderLegendre', 10)

# modelRef.setParam("particleSize", 54.3590982,  minVal = 0, maxVal = 100, vary = True)
# modelRef.setParam("dShell", 24.5796378,  minVal = 0, maxVal = 50, vary = True)
# modelRef.setParam("dSurfactant", 15.3433410,  minVal = 0, maxVal = 50, vary = True)
# modelRef.setParam("pVal", 2.52303639,  minVal = 1, maxVal = 100, vary = True)
# modelRef.setParam("sigParticleSize", 0.06185158,  minVal = 0, maxVal = 0.25, vary = True)
# modelRef.setParam("i0_saxs", 0.02468291,  minVal = 0, maxVal = 10, vary = True)
# modelRef.setParam("i0Oleic", 0.74137496, minVal = 0, maxVal = 100, vary=True)
# modelRef.setParam("x", 1, minVal = 0, maxVal = 1, vary=False)
# modelRef.setParam("i0_sans", 0.13141034,  minVal = 0, maxVal = 10, vary = True)
# modelRef.setParam("bg_sans", 0.01355457,  minVal = 0, maxVal = 0.1, vary = True)

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