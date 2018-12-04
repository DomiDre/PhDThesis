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

sans_sldCore = sld_neutrons_5A['Magnetite']
sans_sldShell = sld_neutrons_5A['Oleic Acid']
sans_sldSolvent = sld_neutrons_5A['Toluene-d8']

app = App()
app.setExperiment(Sanspol)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/AH11_plus_1.2T_LA_scaled.dat', ['p', 'la'])
dataRef.loadFromFile('../../experimental_data/AH11_minus_1.2T_LA_scaled.dat', ['m', 'la'])
dataRef.loadFromFile('../../experimental_data/AH11_plus_1.2T_SA.dat', ['p', 'sa'])
dataRef.loadFromFile('../../experimental_data/AH11_minus_1.2T_SA.dat', ['m', 'sa'])

dataRef.sliceDomain(0, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCS, [Magnetic, InstrumentalResolution])
modelRef.setParam("magSldCore", 9.219999999999999e-07,  minVal = 0, maxVal = 2e-06, vary = True)
modelRef.setConstantParam("sin2alpha", 0.9974654)


modelRef.setConstantParam("i0", 0.042)
modelRef.setConstantParam("d", 19.71)
modelRef.setConstantParam("bg", 0.00738)
modelRef.setConstantParam("sldCore", 7.286004e-06)
modelRef.setConstantParam("dTheta_sa", 0.0032)
modelRef.setConstantParam("dTheta_la", 0.00386)


modelRef.setConstantParam("sldShell", 7.8e-8)
modelRef.setConstantParam("r", 55.6445128)
modelRef.setConstantParam("sigR", 0.12989754)
modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()