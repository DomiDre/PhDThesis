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
modelRef.setParam("magSldCore", 4.677429344095434e-07,  minVal = 0, maxVal = 2e-06, vary = True)
modelRef.setParam("dDead1", 0.0,  minVal = 0, maxVal = 90, vary = False)
modelRef.setParam("dDead2", 1.1425758139615994e-06,  minVal = 0, maxVal = 90, vary = False)

modelRef.setConstantParam("sin2alpha", 0.9974654)

modelRef.setConstantParam("r1", 35.17974095275273)
modelRef.setConstantParam("r2", 9.33953179608812)
modelRef.setConstantParam("sigR1", 0.07549776216868476)
modelRef.setConstantParam("sigR2", 0.6050139188259823)
modelRef.setConstantParam("fraction", 0.5363056033284519)
modelRef.setConstantParam("d", 18.896805666596023)
modelRef.setConstantParam("i0", 0.2724857638871925)
modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("sldShell", 1.16120612403591e-06)
modelRef.setConstantParam("i0Oleic", 1.0431048323153003)
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