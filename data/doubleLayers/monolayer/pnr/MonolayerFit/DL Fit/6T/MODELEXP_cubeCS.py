#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import CubeCSDoubleLayer, Magnetic, DataResolution
from fortRefl import nanocubes, algorithms
import numpy as np
from modelexp.data import MftData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_neutrons_5A
from fortRefl import nanocubes, algorithms

class Monolayer(CubeCSDoubleLayer):
  '''
  Model to describe the formfactor of a sphere
  '''
  def initParameters(self):
    self.params.add("i0", 1, min = 0, max = 2, vary = False)
    self.params.add("bg", 2.1e-06, min = 0.0, max = 0.0001, vary = False)
    self.params.add("a", 50, min = 0, max = 100, vary = True)
    self.params.add("d", 20, min = 0, max = 40, vary = True)
    self.params.add("packingDensity1", 0.517, min = 0.0, max = 1.0, vary = True)
    self.params.add("packingDensity2", 0.517, min = 0.0, max = 1.0, vary = True)
    self.params.add('roughnessSubstrate', 5, min= 0, max = 20, vary=True)
    self.params.add("roughnessPlus1", 0, min = 0.0, max = 20, vary = True)
    self.params.add("roughnessPlus2", 0, min = 0.0, max = 20, vary = True)
    self.params.add("spacerThickness", 0, min = 0, max = 40, vary = False)
    self.params.add('sldCore', 8e-6, min= 0, max = 40e-6, vary=False)
    self.params.add('sldShell', 10e-7, min= 0, max = 40e-6, vary=False)
    self.params.add('sldMatrix', 0e-6, min= 0, max = 40e-6, vary=False)
    self.params.add('sldSpacer', 0e-6, min= 0, max = 40e-6, vary=False)
    self.params.add('sldSubstrate', 2e-6, min= 0, max = 40e-6, vary=False)
    self.params.add('coverage', 1, min= 0, max = 1, vary=True)

  def initMagneticParameters(self):
    self.params.add('magSldCore', 1e-6)
    self.params.add('magSldShell', 0, vary=False)

    self.addConstantParam('magSldShell')

  def calcModel(self):
    a = self.params['a'].value
    d = self.params['d'].value
    pDens1 = self.params["packingDensity1"].value
    pDens2 = self.params["packingDensity2"].value
    sldSub = self.params['sldSubstrate'].value
    sldShell = self.params['sldShell'].value
    sldCore = self.params['sldCore'].value
    sldSpacer = self.params['sldSpacer'].value
    coverage = self.params['coverage'].value
    roughSub = self.params['roughnessSubstrate'].value
    roughLayer1 = roughSub + self.params["roughnessPlus1"].value
    roughLayer2 = roughLayer1 + self.params["roughnessPlus2"].value
    spacerThickness = self.params['spacerThickness'].value

    sld = np.array([
      sldSub,
      pDens1 * sldShell,
      pDens1 * sldCore,
      pDens1 * sldShell,
      sldSpacer,
      pDens2 * sldShell,
      pDens2 * sldCore,
      pDens2 * sldShell,
      0,
    ])

    thickness = [
      2*a,
      d,
      a,
      d,
      spacerThickness,
      d,
      a,
      d,
      2*a
    ]

    roughness = [
      roughSub,
      roughLayer1,
      roughLayer1,
      roughLayer1,
      roughLayer1,
      roughLayer2,
      roughLayer2,
      roughLayer2,
      roughLayer2
    ]

    IparticleLayer = algorithms.parrat(
      self.q,
      sld,
      roughness,
      thickness
    )

    Isubstrate = algorithms.parrat(
      self.q,
      [sldSub, 0],
      [roughSub, roughSub],
      [2*a, 2*a]
    )
    z = -thickness[0] + np.sum(thickness)

    self.z = np.linspace(-thickness[0], z, 300)
    self.I = self.params["i0"] * (
      self.params['coverage'] * IparticleLayer + (1-self.params['coverage']) * Isubstrate
    )  + self.params["bg"]
    self.sld = algorithms.roughsld_thick_layers(self.z, sld, roughness, thickness).real

  def calcMagneticModel(self):
    a = self.params['a'].value
    d = self.params['d'].value
    pDens1 = self.params["packingDensity1"].value
    pDens2 = self.params["packingDensity2"].value
    sldSub = self.params['sldSubstrate'].value
    sldShell = self.params['sldShell'].value
    sldCore = self.params['sldCore'].value
    sldSpacer = self.params['sldSpacer'].value
    magSldCore = self.params['magSldCore'].value
    coverage = self.params['coverage'].value
    roughSub = self.params['roughnessSubstrate'].value
    roughLayer1 = roughSub + self.params["roughnessPlus1"].value
    roughLayer2 = roughLayer1 + self.params["roughnessPlus2"].value
    spacerThickness = self.params['spacerThickness'].value

    sld = np.array([
      sldSub,
      pDens1 * sldShell,
      pDens1 * sldCore,
      pDens1 * sldShell,
      sldSpacer,
      pDens2 * sldShell,
      pDens2 * sldCore,
      pDens2 * sldShell,
      0,
    ])

    sldMag = np.array([
      0,
      0,
      pDens1 * magSldCore,
      0,
      0,
      0,
      pDens2 * magSldCore,
      0,
      0,
    ])

    thickness = [
      2*a,
      d,
      a,
      0*d,
      spacerThickness,
      0*d,
      a,
      d,
      2*a
    ]

    roughness = [
      roughSub,
      roughLayer1,
      roughLayer1,
      roughLayer1,
      roughLayer1,
      roughLayer2,
      roughLayer2,
      roughLayer2,
      roughLayer2
    ]

    IparticleLayer = algorithms.parrat(
      self.q,
      sld + self.params['polarization']*sldMag,
      roughness,
      thickness
    )

    Isubstrate = algorithms.parrat(
      self.q,
      [sldSub, 0],
      [roughSub, roughSub],
      [2*a, 2*a]
    )
    z = -thickness[0] + np.sum(thickness)

    self.z = np.linspace(-thickness[0], z, 300)
    self.I = self.params["i0"] * (
      self.params['coverage'] * IparticleLayer + (1-self.params['coverage']) * Isubstrate
    )  + self.params["bg"]
    self.sld = algorithms.roughsld_thick_layers(self.z, sld, roughness, thickness).real

    self.sldMag = algorithms.roughsld_thick_layers(self.z, sldMag, roughness, thickness).real

app = App()
app.setExperiment(PolarizedReflectometry)
dataRef = app.setData(MftData)

dataRef.loadFromFile('../../../mftFiles/DD205_4_5K_6000mT_d.mft', ['m'])
dataRef.loadFromFile('../../../mftFiles/DD205_4_5K_6000mT_u.mft', ['p'])
dataRef.sliceDomain(0.007, 1)
dataRef.plotData()
modelRef = app.setModel(Monolayer, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("i0", 0.9318707225999012,  minVal = 0, maxVal = 1.5, vary = True)
modelRef.setParam("roughnessSubstrate", 0.0,  minVal = 0.0, maxVal = 50, vary = False)
modelRef.setParam("roughnessPlus1", 8.3,  minVal = 0.0, maxVal = 50, vary = False)
modelRef.setParam("roughnessPlus2", 0.5,  minVal = 0.0, maxVal = 50, vary = False)
modelRef.setParam("packingDensity1", 0.649,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity2", 0.129,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("coverage", 0.396,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("spacerThickness", 30.900000000000002,  minVal = 0, maxVal = 50, vary = False)

modelRef.setParam("magSldCore", 1.3268951020032136e-06,  minVal = 0.0, maxVal = 2e-06, vary = True)

modelRef.setConstantParam("a", 93.84)
modelRef.setConstantParam("d", 9.525)
modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam('sldCore', sld_neutrons_5A['Cobalt Ferrite'].real)
modelRef.setConstantParam('sldShell', sld_neutrons_5A['Oleic Acid'].real)
modelRef.setConstantParam('sldSubstrate', sld_neutrons_5A['Silicon'].real)
modelRef.setConstantParam('sldSpacer', sld_neutrons_5A['Oleic Acid'].real)
modelRef.setConstantParam('sldMatrix', 0)

modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()