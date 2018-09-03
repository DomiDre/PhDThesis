#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SphereCS, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

sans_sldCore = sld_neutrons_5A['Magnetite']
sans_sldShell = sld_neutrons_5A['Oleic Acid']
sans_sldSolvent = sld_neutrons_5A['Toluene-d8']

app = App()
app.setExperiment(Sans)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../sans_PKM18_N_8m.dat', ['sa'])
dataRef.loadFromFile('../sans_PKM18_N_2m.dat', ['la'])

dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCS, InstrumentalResolution)
modelRef.setParam("r", 52.64,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("d", 18.689999999999998,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("sigR", 0.0597,  minVal = 0, maxVal = 0.1, vary = False)
modelRef.setParam("i0", 0.272,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg", 0.0,  minVal = 0, maxVal = 0.02, vary = False)
modelRef.setParam("dTheta_sa", 0.003,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("dTheta_la", 0.0035600000000000002,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("sldShell", 2.5828584e-06,  minVal = 3.12e-08, maxVal = 5.664e-06, vary = True)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore", sans_sldCore)
modelRef.setConstantParam("sldSolvent", sans_sldSolvent)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()