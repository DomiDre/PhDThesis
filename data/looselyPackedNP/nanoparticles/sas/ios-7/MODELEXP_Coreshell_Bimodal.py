#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import SimultaneousSaxsSans
from modelexp.models.sas import SphereCS, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
from fortSAS import sphere_cs
import numpy as np

class SphereCS_Bimodal(SphereCS):
  def initParameters(self):
    self.params.add('r1', 100)
    self.params.add('r2', 70)
    self.params.add('d', 20)
    self.params.add('sldCore', 40e-6)
    self.params.add('sldShell', 30e-6)
    self.params.add('sldSolvent', 10e-6)
    self.params.add('sigR1', 0.05)
    self.params.add('sigR2', 0.05)
    self.params.add('sigD', 0)
    self.params.add('i0', 1)
    self.params.add('fraction', 0.3)
    self.params.add('bg', 1e-6)

  def initMagneticParameters(self):
    self.params.add('dDead', 5, min=0)
    self.params.add('magSldCore', 1e-6)
    self.params.add('magSldShell', 0, vary=False)
    self.params.add('magSldSolvent', 0, vary=False)

    self.addConstantParam('magSldShell')
    self.addConstantParam('magSldSolvent')



  def calcModel(self):
    self.I = self.params['i0'] * (
      (1-self.params['fraction']) * sphere_cs.formfactor(
        self.q,
        self.params['r1'],
        self.params['d'],
        self.params['sldCore'],
        self.params['sldShell'],
        self.params['sldSolvent'],
        self.params['sigR1'],
        self.params['sigD']
    ) + self.params['fraction'] * sphere_cs.formfactor(
        self.q,
        self.params['r2'],
        self.params['d'],
        self.params['sldCore'],
        self.params['sldShell'],
        self.params['sldSolvent'],
        self.params['sigR2'],
        self.params['sigD']
    )) + self.params['bg']

    r1, sld1 = sphere_cs.sld(
      self.params['r1'],
      self.params['d'],
      self.params['sldCore'],
      self.params['sldShell'],
      self.params['sldSolvent']
    )

    r2, sld2 = sphere_cs.sld(
      self.params['r2'],
      self.params['d'],
      self.params['sldCore'],
      self.params['sldShell'],
      self.params['sldSolvent']
    )
    self.r = np.concatenate([r1, r1[::-1], r2])
    self.sld = np.concatenate([sld1, sld1[::-1], sld2])

  def calcMagneticModel(self):
    self.I = self.params['i0'] * (
      (1-self.params['fraction']) * sphere_cs.magnetic_formfactor(
        self.q,
        self.params['r1'],
        self.params['d'],
        self.params['sldCore'],
        self.params['sldShell'],
        self.params['sldSolvent'],
        self.params['sigR1'],
        self.params['sigD'],
        self.params['dDead'],
        self.params['magSldCore'],
        self.params['magSldShell'],
        self.params['magSldSolvent'],
        self.params['xi'],
        self.params['sin2alpha'],
        self.params['polarization'],
    ) + self.params['fraction'] * sphere_cs.magnetic_formfactor(
        self.q,
        self.params['r2'],
        self.params['d'],
        self.params['sldCore'],
        self.params['sldShell'],
        self.params['sldSolvent'],
        self.params['sigR2'],
        self.params['sigD'],
        self.params['dDead'],
        self.params['magSldCore'],
        self.params['magSldShell'],
        self.params['magSldSolvent'],
        self.params['xi'],
        self.params['sin2alpha'],
        self.params['polarization'],
    )) + self.params['bg']


    r1, sld1 = sphere_cs.sld(
      self.params['r1'],
      self.params['d'],
      self.params['sldCore'],
      self.params['sldShell'],
      self.params['sldSolvent']
    )

    r2, sld2 = sphere_cs.sld(
      self.params['r2'],
      self.params['d'],
      self.params['sldCore'],
      self.params['sldShell'],
      self.params['sldSolvent']
    )
    self.r = np.concatenate([r1, r1[::-1], r2])
    self.sld = np.concatenate([sld1, sld1[::-1], sld2])

    rMag1, sldMag1 = sphere_cs.sld(
      self.params['r1']-self.params['dDead'],
      self.params['d'],
      self.params['magSldCore'],
      self.params['magSldShell'],
      self.params['magSldSolvent']
    )

    rMag2, sldMag2 = sphere_cs.sld(
      self.params['r2']-self.params['dDead'],
      self.params['d'],
      self.params['magSldCore'],
      self.params['magSldShell'],
      self.params['magSldSolvent']
    )
    self.rMag = np.concatenate([rMag1, rMag1[::-1], rMag2])
    self.sldMag = np.concatenate([sldMag1, sldMag1[::-1], sldMag2])




saxs_sldCore = sld_xray_GALAXI['Magnetite'].real
saxs_sldShell = sld_xray_GALAXI['Oleic Acid'].real
saxs_sldSolvent = sld_xray_GALAXI['Cyclohexane'].real

sans_sldCore = sld_neutrons_5A['Magnetite']
sans_sldShell = sld_neutrons_5A['Oleic Acid']
sans_sldSolvent = sld_neutrons_5A['Toluene-d8']

app = App()
app.setExperiment(SimultaneousSaxsSans)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('saxs_KWi338.xye', ['saxs'])
dataRef.loadFromFile('023564_N.dat', ['sans', 'sa']) #sans_KWi338_N_8m.dat
dataRef.loadFromFile('023567_N.dat', ['sans', 'la']) # sans_KWi338_N_2m.dat

dataRef.sliceDomain(1e-2, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCS_Bimodal, InstrumentalResolution)
modelRef.setParam("r1", 34.98349822830021,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("r2", 11.629073659996152,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("d", 16.189415744184586,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("sigR1", 0.0942,  minVal = 0, maxVal = 0.2, vary = False)
modelRef.setParam("sigR2", 0.2896,  minVal = 0, maxVal = 0.8, vary = False)
modelRef.setParam("fraction", 0.35901699314781876,  minVal = 0.1, maxVal = 1, vary = True)
modelRef.setParam("i0_saxs", 0.47973801912317826,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg_saxs", 0.0011400000000000002,  minVal = 0, maxVal = 0.02, vary = False)
modelRef.setParam("i0_sans", 1.11,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("bg_sans", 0.0,  minVal = 0, maxVal = 0.02, vary = False)
modelRef.setParam("sldShell_sans", 2.7743736e-06,  minVal = 3.12e-08, maxVal = 5.664e-06, vary = True)
modelRef.setParam("dTheta_sa", 0.003228,  minVal = 0.001, maxVal = 0.005, vary = False)
modelRef.setParam("dTheta_la", 0.006418,  minVal = 0.001, maxVal = 0.007, vary = True)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore_saxs", saxs_sldCore)
modelRef.setConstantParam("sldShell_saxs", saxs_sldShell)
modelRef.setConstantParam("sldSolvent_saxs", saxs_sldSolvent)
modelRef.setConstantParam("sldCore_sans", sans_sldCore)
modelRef.setConstantParam("sldSolvent_sans", sans_sldSolvent)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()