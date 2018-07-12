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

saxs_sldCore = sld_xray_GALAXI['Magnetite'].real
saxs_sldShell = sld_xray_GALAXI['Oleic Acid'].real
saxs_sldSolvent = sld_xray_GALAXI['Cyclohexane'].real

sans_sldCore = sld_neutrons_5A['Magnetite']
sans_sldShell = sld_neutrons_5A['Oleic Acid']
sans_sldSolvent = sld_neutrons_5A['Toluene-d8']

app = App()
app.setExperiment(SimultaneousSaxsSans)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('saxs_PMK18.xye', ['saxs'])
dataRef.loadFromFile('sans_PKM18_N_8m.dat', ['sans', 'sa'])
dataRef.loadFromFile('sans_PKM18_N_2m.dat', ['sans', 'la'])

dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCS, InstrumentalResolution)
modelRef.setParam("r", 52.68847698374829,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("d", 21.043479620605215,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("sigR", 0.05977094596977442,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0_saxs", 0.5347139116115067,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg_saxs", 0.008865404779555709,  minVal = 0, maxVal = 0.02, vary = True)
modelRef.setParam("i0_sans", 0.22381979688833298,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg_sans", 0.00436,  minVal = 0, maxVal = 0.02, vary = True)
modelRef.setParam("dTheta_sa", 0.0032301805812655743,  minVal = 0, maxVal = 0.004, vary = True)
modelRef.setParam("dTheta_la", 0.00344,  minVal = 0, maxVal = 0.004, vary = True)
modelRef.setParam("sldShell_sans", 2.8209698958468325e-06,  minVal = 3.12e-08, maxVal = 5.664e-06, vary = True)

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