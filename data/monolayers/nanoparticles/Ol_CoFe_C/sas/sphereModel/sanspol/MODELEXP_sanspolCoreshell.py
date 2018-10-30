#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sanspol
from modelexp.models.sas import SphereCS, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_neutrons_5A

app = App()
app.setExperiment(Sanspol)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/dd67_rfm_la_scaled.dat', ['p', 'la'])
dataRef.loadFromFile('../../experimental_data/dd67_rfp_la_scaled.dat', ['m', 'la'])
dataRef.loadFromFile('../../experimental_data/dd67_rfm_sa.dat', ['p', 'sa'])
dataRef.loadFromFile('../../experimental_data/dd67_rfp_sa.dat', ['m', 'sa'])
dataRef.onlyPositiveValues()
dataRef.sliceDomain(0, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCS, [Magnetic, InstrumentalResolution])
modelRef.setParam("magSldCore", 2.8799999999999993e-07,  minVal = 0, maxVal = 2e-06, vary = True)
modelRef.setConstantParam("sin2alpha", 0.9974654)
modelRef.setParam("i0", 0.167,  minVal = 0, maxVal = 0.2, vary = False)

modelRef.setConstantParam("sldCore", 6.43514e-06)
modelRef.setConstantParam("d", 18.21)
modelRef.setConstantParam("bg", 0.016040000000000002)
modelRef.setConstantParam("dTheta_sa", 0.0006941377777829783)
modelRef.setConstantParam("dTheta_la", 0.0012900000000000001)

modelRef.setConstantParam("r", 62.552194776360615)
modelRef.setConstantParam("sigR", 0.09738588873844115)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldShell", sld_neutrons_5A['Oleic Acid'])
modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.setConstantParam("dDead", 0.0)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()