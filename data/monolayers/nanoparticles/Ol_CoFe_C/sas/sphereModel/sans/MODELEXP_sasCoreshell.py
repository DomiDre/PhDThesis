#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SphereCS, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
app.setExperiment(Sans)
dataRef = app.setData(XyeData)


dataRef.loadFromFile('./DD67_nuclear20_sa.dat', ['sa'])
dataRef.loadFromFile('./DD67_nuclear20_la_scaled.dat', ['la'])
dataRef.sliceDomain(0.004, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCS, InstrumentalResolution)
modelRef.setParam("i0", 0.167,  minVal = 0, maxVal = 0.5, vary = True)
modelRef.setParam("sldCore", 6.43514e-06,  minVal = 4.293e-06, maxVal = 7.289e-06, vary = True)
modelRef.setParam("d", 18.21,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("bg", 0.016040000000000002,  minVal = 0, maxVal = 0.02, vary = True)
modelRef.setParam("dTheta_sa", 0.0006941377777829783,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("dTheta_la", 0.0012900000000000001,  minVal = 0, maxVal = 0.01, vary = True)

modelRef.setConstantParam("r", 62.552194776360615)
modelRef.setConstantParam("sigR", 0.09738588873844115)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldShell", sld_neutrons_5A['Oleic Acid'])
modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()