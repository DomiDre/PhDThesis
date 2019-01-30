#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sanspol
from modelexp.models.sas import SphereCSOA, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
experimentRef = app.setExperiment(Sanspol)
experimentRef.setFitRange(0.03, 0.5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/KWi338_LA_Mag20_I+.dat', ['p', 'la'])
dataRef.loadFromFile('../../experimentalData/KWi338_LA_Mag20_I-.dat', ['m', 'la'])
dataRef.loadFromFile('../../experimentalData/KWi338_SA_Mag20_I+.dat', ['p', 'sa'])
dataRef.loadFromFile('../../experimentalData/KWi338_SA_Mag20_I-.dat', ['m', 'sa'])

dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSOA, [Magnetic, InstrumentalResolution])

modelRef.setParam("magSldCore", 4.406137399700236e-07,  minVal = 0, maxVal = 5e-06, vary = True)
modelRef.setParam("dDead", 0.0,  minVal = 0, maxVal = 30, vary = True)

modelRef.setConstantParam("d", 14.7)
modelRef.setConstantParam("i0", 0.09)
modelRef.setConstantParam("i0Oleic", 0.41929337440618)
modelRef.setConstantParam("rOleic", 21.0)

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