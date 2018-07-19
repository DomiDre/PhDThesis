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

dataRef.loadFromFile('saxs_PMK18.xye', ['saxs'], 0.001)
dataRef.loadFromFile('sans_PKM18_N_8m.dat', ['sans', 'sa'])
dataRef.loadFromFile('sans_PKM18_N_2m.dat', ['sans', 'la'])

dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCS, InstrumentalResolution)
modelRef.setParam("r", 52.7569433553093,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigR", 0.0604,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0_saxs", 0.5327255482957137,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg_saxs", 0.008784830048293083,  minVal = 0, maxVal = 0.02, vary = True)

modelRef.setParam("d", 19.02,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("i0_sans", 0.2686665865782178,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg_sans", 0.0,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setParam("dTheta_sa", 0.0030600000000000002,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("dTheta_la", 0.0035800000000000003,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("sldShell_sans", 2.6391864000000003e-06,  minVal = 3.12e-08, maxVal = 5.664e-06, vary = True)

Fraction = (2.583e-6 - sans_sldShell)/(sans_sldSolvent - sans_sldShell)
modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore_saxs", saxs_sldCore)
modelRef.setConstantParam("sldShell_saxs", saxs_sldShell) #saxs_sldShell + mixtureFraction*(saxs_sldSolvent - saxs_sldShell))
modelRef.setConstantParam("sldSolvent_saxs", saxs_sldSolvent)
modelRef.setConstantParam("sldCore_sans", sans_sldCore)
modelRef.setConstantParam("sldSolvent_sans", sans_sldSolvent)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()