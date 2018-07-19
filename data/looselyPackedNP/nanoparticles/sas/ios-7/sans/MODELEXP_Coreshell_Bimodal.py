#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SphereCSBimodal, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
from fortSAS import sphere_cs
import numpy as np

sans_sldCore = sld_neutrons_5A['Magnetite']
sans_sldShell = sld_neutrons_5A['Oleic Acid']
sans_sldSolvent = sld_neutrons_5A['Toluene-d8']

app = App()
app.setExperiment(Sans)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../023564_N.dat', ['sa']) #sans_KWi338_N_8m.dat
dataRef.loadFromFile('../023567_N.dat', ['la']) # sans_KWi338_N_2m.dat

dataRef.sliceDomain(1e-2, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSBimodal, InstrumentalResolution)
modelRef.setParam("r1", 34.96,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("r2", 11.6,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("d", 18.96,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("sigR1", 0.0942,  minVal = 0, maxVal = 0.2, vary = False)
modelRef.setParam("sigR2", 0.2896,  minVal = 0, maxVal = 0.8, vary = False)
modelRef.setParam("fraction", 0.3079,  minVal = 0.1, maxVal = 1, vary = False)
modelRef.setParam("i0", 1.1,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("bg", 0.0,  minVal = 0, maxVal = 0.02, vary = False)
modelRef.setParam("sldShell", 3.3751693454419203e-06,  minVal = 3.12e-08, maxVal = 5.664e-06, vary = True)
modelRef.setParam("dTheta_sa", 0.004096000000000001,  minVal = 0.001, maxVal = 0.01, vary = True)
modelRef.setParam("dTheta_la", 0.006869799874829066,  minVal = 0.001, maxVal = 0.01, vary = True)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore", sans_sldCore)
modelRef.setConstantParam("sldSolvent", sans_sldSolvent)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()