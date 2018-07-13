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

dataRef.loadFromFile('PKM18_M_p_2m.dat', ['p', 'la'])
dataRef.loadFromFile('PKM18_M_m_2m.dat', ['m', 'la'])
dataRef.loadFromFile('PKM18_M_p_8m.dat', ['p', 'sa'])
dataRef.loadFromFile('PKM18_M_m_8m.dat', ['m', 'sa'])

dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCS, [Magnetic, InstrumentalResolution])
modelRef.setParam("dDead", 3.175095146065315,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("magSldCore", 5.135000772410115e-07,  minVal = 0, maxVal = 5e-06, vary = True)

modelRef.setConstantParam("sin2alpha", 0.9974654)
modelRef.setConstantParam("r", 52.72)
modelRef.setConstantParam("sigR", 0.060000000000000005)
modelRef.setConstantParam("d", 18.690)
modelRef.setConstantParam("i0", 0.27251)
modelRef.setConstantParam("bg", 0)
modelRef.setConstantParam("dTheta_sa", 0.0030085)
modelRef.setConstantParam("dTheta_la", 0.00356313)
modelRef.setConstantParam("sldShell", 2.583e-06)
modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore", sans_sldCore)
modelRef.setConstantParam("sldSolvent", sans_sldSolvent)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()