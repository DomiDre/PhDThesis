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

dataRef.loadFromFile('../../experimental_data/AH11_plus_1.2T_LA_scaled.dat', ['p', 'la'])
dataRef.loadFromFile('../../experimental_data/AH11_minus_1.2T_LA_scaled.dat', ['m', 'la'])
dataRef.loadFromFile('../../experimental_data/AH11_plus_1.2T_SA.dat', ['p', 'sa'])
dataRef.loadFromFile('../../experimental_data/AH11_minus_1.2T_SA.dat', ['m', 'sa'])

dataRef.sliceDomain(0, 0.5)
dataRef.plotData()

modelRef = app.setModel(CubeCS, [Magnetic, InstrumentalResolution])
modelRef.setParam("magSldCore", 4.2919676279767794e-07,  minVal = 0, maxVal = 2e-06, vary = True)

modelRef.setConstantParam("sin2alpha", 0.9974654)

modelRef.setConstantParam("i0", 0.19540000000000002)
modelRef.setConstantParam("d", 10.302942403473624)
modelRef.setConstantParam("bg", 0.00412688899449506)
modelRef.setConstantParam("sldCore", 6.746724e-06)
modelRef.setConstantParam("dTheta_sa", 0.0033164139117529026)
modelRef.setConstantParam("dTheta_la", 0.00411)
modelRef.setConstantParam("sldShell", 8.265240000000001e-07)


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