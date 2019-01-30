#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SphereCSOA, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
experimentRef = app.setExperiment(Sans)
# experimentRef.setFitRange(0.03, 0.5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/KWi338_SA_Nuc20.dat', ['sa'])
dataRef.loadFromFile('../../experimentalData/KWi338_LA_Nuc20.dat', ['la'])

dataRef.plotData()

modelRef = app.setModel(SphereCSOA, InstrumentalResolution)

modelRef.setParam("d", 14.700000000000001,  minVal = 0, maxVal = 25, vary = False)
modelRef.setParam("i0", 0.09,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0Oleic", 0.41929337440618,  minVal = 0, maxVal = 40, vary = True)
modelRef.setParam("rOleic", 21.0,  minVal = 0, maxVal = 200, vary = False)

modelRef.setConstantParam("r", 34.88004817571305)
modelRef.setConstantParam("sigR", 0.09611441352810439)
modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("bg", 0)
modelRef.setConstantParam("sldCore", 7.00e-6)
modelRef.setConstantParam("sldShell", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.66e-6)
modelRef.setConstantParam("sldOleic", 0.078e-6)

modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.setConstantParam("dTheta_sa", 0.0017)
modelRef.setConstantParam("dTheta_la", 0.0028)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()