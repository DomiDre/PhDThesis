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

dataRef.loadFromFile('saxs_KWi338.xye', ['saxs'])
dataRef.loadFromFile('sans_KWi338_N_8m.dat', ['sans', 'sa'])
dataRef.loadFromFile('sans_KWi338_N_2m.dat', ['sans', 'la'])

dataRef.sliceDomain(0, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCS, InstrumentalResolution)
modelRef.setParam("r", 34.43759776022931,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("d", 20.88,  minVal = 0, maxVal = 30, vary = False)
modelRef.setParam("sigR", 0.10317415721568234,  minVal = 0, maxVal = 0.2, vary = True)
modelRef.setParam("i0_saxs", 0.3249578134919171,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg_saxs", 0.0011400000000000002,  minVal = 0, maxVal = 0.02, vary = False)
modelRef.setParam("i0_sans", 0.5353166855774111,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg_sans", 0.0,  minVal = 0, maxVal = 0.02, vary = False)
modelRef.setParam("sldShell_sans", 3.0835860348959935e-06,  minVal = 3.12e-08, maxVal = 5.664e-06, vary = True)

modelRef.setConstantParam("dTheta_sa", 0.002692)
modelRef.setConstantParam("dTheta_la", 0.002868)
modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore_saxs", saxs_sldCore)
modelRef.setConstantParam("sldShell_saxs", saxs_sldShell)
modelRef.setConstantParam("sldSolvent_saxs", saxs_sldSolvent)
modelRef.setConstantParam("sldCore_sans", sans_sldCore)
modelRef.setConstantParam("sldSolvent_sans", sans_sldSolvent)
modelRef.setConstantParam('wavelength', 5.0)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()