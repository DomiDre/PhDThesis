#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import SimultaneousSaxsSans
from modelexp.models.sas import SphereCSBimodalOA, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
from fortSAS import sphere_cs
import numpy as np

saxs_sldCore = sld_xray_GALAXI['Magnetite'].real
saxs_sldShell = sld_xray_GALAXI['Oleic Acid'].real
saxs_sldSolvent = sld_xray_GALAXI['Cyclohexane'].real

sans_sldCore = sld_neutrons_5A['Magnetite']
sans_sldShell = sld_neutrons_5A['Oleic Acid']
sans_sldSolvent = sld_neutrons_5A['Toluene-d8']

app = App()
app.setExperiment(SimultaneousSaxsSans)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('saxs_KWi338.xye', ['saxs'], 0.001)
dataRef.loadFromFile('023564_N.dat', ['sans', 'sa']) #sans_KWi338_N_8m.dat
dataRef.loadFromFile('023567_N.dat', ['sans', 'la']) # sans_KWi338_N_2m.dat

dataRef.sliceDomain(1e-2, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSBimodalOA, InstrumentalResolution)
modelRef.setParam("r1", 35.25471695947235,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("r2", 9.52,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigR1", 0.0698,  minVal = 0, maxVal = 0.2, vary = True)
modelRef.setParam("sigR2", 0.5895,  minVal = 0, maxVal = 1.5, vary = True)
modelRef.setParam("fraction", 0.40059999999999996,  minVal = 0.1, maxVal = 1, vary = True)
modelRef.setParam("i0_saxs", 0.685,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("bg_saxs", 0.00134,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setParam("d", 19.02,  minVal = 0, maxVal = 30, vary = False)
modelRef.setParam("i0_sans", 0.73,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("bg_sans", 0.0,  minVal = 0, maxVal = 0.02, vary = False)
modelRef.setParam("sldShell_sans", 2.5772256e-06,  minVal = 3.12e-08, maxVal = 5.664e-06, vary = False)

modelRef.setParam("i0Oleic", 0.6599999999999999,  minVal = 0, maxVal = 2, vary = True)

modelRef.setConstantParam("dTheta_sa", 0.0030600000000000002)
modelRef.setConstantParam("dTheta_la", 0.0035800000000000003)
modelRef.setConstantParam("sigD", 0)

modelRef.setConstantParam("sldCore_saxs", saxs_sldCore)
modelRef.setConstantParam("sldShell_saxs", saxs_sldShell)
modelRef.setConstantParam("sldSolvent_saxs", saxs_sldSolvent)
modelRef.setConstantParam('sldOleic_saxs', saxs_sldShell)

modelRef.setConstantParam("sldCore_sans", sans_sldCore)
#
modelRef.setConstantParam("sldSolvent_sans", sans_sldSolvent)
modelRef.setConstantParam('sldOleic_sans', sans_sldShell)

modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()