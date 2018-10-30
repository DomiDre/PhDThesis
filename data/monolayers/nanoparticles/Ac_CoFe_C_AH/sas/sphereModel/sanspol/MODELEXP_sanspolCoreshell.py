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

dataRef.loadFromFile('../AH11_plus_1.2T_LA_scaled.dat', ['p', 'la'])
dataRef.loadFromFile('../AH11_minus_1.2T_LA_scaled.dat', ['m', 'la'])
dataRef.loadFromFile('../AH11_plus_1.2T_SA.dat', ['p', 'sa'])
dataRef.loadFromFile('../AH11_minus_1.2T_SA.dat', ['m', 'sa'])

dataRef.sliceDomain(0, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCS, [Magnetic, InstrumentalResolution])
modelRef.setParam("magSldCore", 5.959999999999999e-07,  minVal = 0, maxVal = 2e-06, vary = True)
modelRef.setConstantParam("sin2alpha", 0.9974654)
modelRef.setParam("i0", 0.0926,  minVal = 0, maxVal = 0.2, vary = False)

modelRef.setConstantParam("d", 14.61)
modelRef.setConstantParam("bg", 0.004540000000000001)
modelRef.setConstantParam("sldCore", 6.9363966337827204e-06)
modelRef.setConstantParam("dTheta_sa", 0.0029687571385682825)
modelRef.setConstantParam("dTheta_la", 0.0035181744286348067)

modelRef.setConstantParam("bg", 0.004240000000000001)
modelRef.setConstantParam("sldCore", 6.863568e-06)

modelRef.setConstantParam("dDead", 0.0)

modelRef.setConstantParam("r", 55.6445128)
modelRef.setConstantParam("sigR", 0.12989754)
modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldShell", sld_neutrons_5A['Oleic Acid'])
modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()