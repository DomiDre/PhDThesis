#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sanspol
from modelexp.models.sas import SphereCSBimodalOA, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
from fortSAS import sphere_cs
import numpy as np

sans_sldCore = sld_neutrons_5A['Magnetite']
sans_sldShell = sld_neutrons_5A['Oleic Acid']
sans_sldSolvent = sld_neutrons_5A['Toluene-d8']

app = App()
app.setExperiment(Sanspol)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('sanspol_KWi338_8m_p.dat', ['p', 'sa'])
dataRef.loadFromFile('sanspol_KWi338_2m_p.dat', ['p', 'la'])
dataRef.loadFromFile('sanspol_KWi338_8m_m.dat', ['m', 'sa'])
dataRef.loadFromFile('sanspol_KWi338_2m_m.dat', ['m', 'la'])

dataRef.sliceDomain(1e-2, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSBimodalOA, [Magnetic, InstrumentalResolution])
modelRef.setParam("magSldCore", 3.259326126120011e-07,  minVal = 0, maxVal = 2e-06, vary = True)
modelRef.setParam("dDead1", 0.0,  minVal = 0, maxVal = 90, vary = False)
modelRef.setParam("dDead2", 0.0,  minVal = 0, maxVal = 90, vary = False)

modelRef.setConstantParam("sin2alpha", 0.9974654)

modelRef.setConstantParam("r1", 35.25471695947235)
modelRef.setConstantParam("r2", 9.52)
modelRef.setConstantParam("sigR1", 0.0698)
modelRef.setConstantParam("sigR2", 0.5895)
modelRef.setConstantParam("fraction", 0.40059999999999996)
modelRef.setConstantParam("d", 19.02)
modelRef.setConstantParam("i0", 0.73)
modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("sldShell", 2.5772256e-06)
modelRef.setConstantParam("i0Oleic", 0.6599999999999999)
modelRef.setConstantParam("dTheta_sa", 0.0030600000000000002)
modelRef.setConstantParam("dTheta_la", 0.0035800000000000003)
modelRef.setConstantParam("sigD", 0)

modelRef.setConstantParam("sldCore", sans_sldCore)
modelRef.setConstantParam("sldSolvent", sans_sldSolvent)
modelRef.setConstantParam('sldOleic', sans_sldShell)

modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()