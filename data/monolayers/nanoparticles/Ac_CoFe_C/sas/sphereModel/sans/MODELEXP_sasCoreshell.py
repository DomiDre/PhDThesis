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

sans_sldCore = sld_neutrons_5A['Cobalt(II) oxide']
sans_sldShell = sld_neutrons_5A['Cobalt Ferrite']

app = App()
app.setExperiment(Sans)
dataRef = app.setData(XyeData)


dataRef.loadFromFile('../../experimental_data/AH11_nuclear_SA.dat', ['sa'])
dataRef.loadFromFile('../../experimental_data/AH11_nuclear_LA_scaled.dat', ['la'])
dataRef.sliceDomain(0., 0.25)
dataRef.plotData()
#    bg:          0 (fixed)

modelRef = app.setModel(SphereCS, InstrumentalResolution)
modelRef.setParam("i0", 0.13540000000000002,  minVal = 0, maxVal = 0.2, vary = True)
modelRef.setParam("d", 14.61,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("bg", 0.004540000000000001,  minVal = 0, maxVal = 0.02, vary = True)
modelRef.setParam("sldCore", 6.713768e-06,  minVal = 4.293e-06, maxVal = 7.289e-06, vary = True)
modelRef.setParam("dTheta_sa", 0.0029696167102563464,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("dTheta_la", 0.0035181888925484572,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("sldShell", 1.040158e-06,  minVal = 7.8e-08, maxVal = 7e-06, vary = True)


modelRef.setConstantParam("r", 55.6445128)
modelRef.setConstantParam("sigR", 0.12989754)
modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()