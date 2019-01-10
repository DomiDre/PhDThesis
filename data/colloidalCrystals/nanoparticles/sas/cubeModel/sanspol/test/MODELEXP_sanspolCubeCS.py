#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sanspol
from modelexp.models.sas import CubeCS, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_neutrons_5A

sans_sldCore = sld_neutrons_5A['Magnetite']
sans_sldShell = sld_neutrons_5A['Oleic Acid']
sans_sldSolvent = sld_neutrons_5A['Toluene-d8']

app = App()
app.setExperiment(Sanspol)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../../experimental_data/AH11_plus_1.2T_LA_scaled.dat', ['p', 'la'])
dataRef.loadFromFile('../../../experimental_data/AH11_minus_1.2T_LA_scaled.dat', ['m', 'la'])
dataRef.loadFromFile('../../../experimental_data/AH11_plus_1.2T_SA.dat', ['p', 'sa'])
dataRef.loadFromFile('../../../experimental_data/AH11_minus_1.2T_SA.dat', ['m', 'sa'])

dataRef.sliceDomain(0, 0.5)
dataRef.plotData()

modelRef = app.setModel(CubeCS, [Magnetic, InstrumentalResolution])
modelRef.setParam("magSldCore", 7.999999999999999e-07,  minVal = 0, maxVal = 2e-06, vary = False)

modelRef.setConstantParam("sin2alpha", 0.9974654)

modelRef.setParam("i0", 0.04287558762332592,  minVal = 0, maxVal = 0.5, vary = False)
modelRef.setParam("d", 14.309999999999999,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("bg", 0.00532,  minVal = 0, maxVal = 0.02, vary = True)
modelRef.setParam("sldCore", 7.256044e-06,  minVal = 4.293e-06, maxVal = 7.289e-06, vary = True)
modelRef.setParam("dTheta_sa", 0.0035384038935242813,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("dTheta_la", 0.0050100000000000006,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("sldShell", 7.8e-08,  minVal = 7.8e-08, maxVal = 5.664e-06, vary = True)

modelRef.setConstantParam("a", 90.06071056809513)
modelRef.setConstantParam("sigA", 0.1069991862611728)
modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('magSldShell', 0.)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()