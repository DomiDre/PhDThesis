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
modelRef.setParam("magSldCore", 4.2999999999999996e-07,  minVal = 0, maxVal = 2e-06, vary = True)

modelRef.setConstantParam("sin2alpha", 0.9974654)

modelRef.setConstantParam("i0", 0.1942)
modelRef.setConstantParam("d", 10.304008063405336)
modelRef.setConstantParam("bg", 0.0041223432758615034)
modelRef.setConstantParam("sldCore", 6.7497200000000005e-06)
modelRef.setConstantParam("dTheta_sa", 0.003317510030626826)
modelRef.setConstantParam("dTheta_la", 0.00411)
modelRef.setConstantParam("sldShell", 8.097660000000001e-07)

modelRef.setConstantParam("a", 90.06693973299343)
modelRef.setConstantParam("sigA", 0.1069470439352857)

modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()