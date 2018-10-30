#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sans
from modelexp.models.sas import CubeCS, InstrumentalResolution
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

modelRef = app.setModel(CubeCS, InstrumentalResolution)
modelRef.setParam("i0", 0.1942,  minVal = 0, maxVal = 0.2, vary = True)
modelRef.setParam("d", 10.304008063405336,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("bg", 0.0041223432758615034,  minVal = 0, maxVal = 0.02, vary = True)
modelRef.setParam("sldCore", 6.7497200000000005e-06,  minVal = 4.293e-06, maxVal = 7.289e-06, vary = True)
modelRef.setParam("dTheta_sa", 0.003317510030626826,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("dTheta_la", 0.00411,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("sldShell", 8.097660000000001e-07,  minVal = 7.8e-08, maxVal = 5.664e-06, vary = True)

modelRef.setConstantParam("a", 90.06693973299343)
modelRef.setConstantParam("sigA", 0.1069470439352857)

modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()