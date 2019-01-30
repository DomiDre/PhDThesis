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
experimentRef.setFitRange(0.01, 1)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/PMK18_SSDD_Mag20_I+.dat', ['p', 'la'])
dataRef.loadFromFile('../../experimentalData/PMK18_SSDD_Mag20_I-.dat', ['m', 'la'])
dataRef.loadFromFile('../../experimentalData/PMK18_LSDD_Mag20_I+.dat', ['p', 'sa'])
dataRef.loadFromFile('../../experimentalData/PMK18_LSDD_Mag20_I-.dat', ['m', 'sa'])

# dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSOA, [Magnetic, InstrumentalResolution])

modelRef.setParam("magSldCore", 1.002512804821604e-06,  minVal = 0, maxVal = 5e-06, vary = True)
modelRef.setParam("dDead", 7.293698016972579,  minVal = 0, maxVal = 30, vary = True)
# modelRef.setParam("magSldShell", 1.3150000000000001e-06,  minVal = 0, maxVal = 5e-06, vary = False)

modelRef.setConstantParam("d", 14.64)
modelRef.setConstantParam("i0", 0.05629890956403377)
modelRef.setConstantParam("i0Oleic", 0.2795362272625905)
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
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()