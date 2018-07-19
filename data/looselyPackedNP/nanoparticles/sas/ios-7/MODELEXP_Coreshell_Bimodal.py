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
modelRef.setParam("r1", 35.17974095275273,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("r2", 9.33953179608812,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigR1", 0.07549776216868476,  minVal = 0, maxVal = 0.2, vary = True)
modelRef.setParam("sigR2", 0.6050139188259823,  minVal = 0, maxVal = 1.5, vary = True)
modelRef.setParam("fraction", 0.5363056033284519,  minVal = 0.1, maxVal = 1, vary = True)
modelRef.setParam("i0_saxs", 0.609330304519774,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("i0_saxs", 0.609330304519774,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("bg_saxs", 0.00134,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setParam("d", 18.896805666596023,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("i0_sans", 0.2724857638871925,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("bg_sans", 0.0,  minVal = 0, maxVal = 0.02, vary = False)
modelRef.setParam("sldShell_sans", 1.16120612403591e-06,  minVal = 3.12e-08, maxVal = 5.664e-06, vary = True)

modelRef.setParam("i0Oleic", 1.0431048323153003,  minVal = 0, maxVal = 30, vary = True)

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