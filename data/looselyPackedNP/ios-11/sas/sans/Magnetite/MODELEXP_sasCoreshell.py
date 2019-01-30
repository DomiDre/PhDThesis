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
experimentRef.setResiduumFormula('chi2 log noError')
# experimentRef.setFitRange(0.05, 0.5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/PMK18_LSDD_Nuclear20.dat', ['sa'])
dataRef.loadFromFile('../../experimentalData/PMK18_SSDD_Nuclear20.dat', ['la'])

dataRef.plotData()

modelRef = app.setModel(SphereCSOA, InstrumentalResolution)

modelRef.setParam("d", 14.64,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("i0", 0.05629890956403377,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0Oleic", 0.2795362272625905,  minVal = 0, maxVal = 3, vary = True)
# modelRef.setConstantParam("rOleic", 21.0)

modelRef.setConstantParam("r", 52.89761472142036)
modelRef.setConstantParam("sigR", 0.05594273920569346)
modelRef.setConstantParam("sigD", 0.)
modelRef.setConstantParam("sldCore", 7.00e-6)
modelRef.setConstantParam("sldShell", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.66e-6)
modelRef.setConstantParam("sldOleic", 0.078e-6)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)
modelRef.setConstantParam("dTheta_sa", 0.0017)
modelRef.setConstantParam("dTheta_la", 0.0028)
modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("rOleic", 21.0)
# modelRef.setConstantParam("dTheta_sa", 0.0021)
# modelRef.setConstantParam("dTheta_la", 0.0038)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()