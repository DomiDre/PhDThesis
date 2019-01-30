#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SphereCSOA
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
experimentRef = app.setExperiment(Saxs)
experimentRef.setFitRange(0.06, 0.5)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimentalData/KWi338.xye')
dataRef.sliceDomain(0.01, 0.5)
dataRef.plotData()

modelRef = app.setModel(SphereCSOA)

modelRef.setParam("r", 34.88004817571305,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigR", 0.09611441352810439,  minVal = 0, maxVal = 0.2, vary = True)
modelRef.setParam("i0", 0.4114724385020394,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("i0Oleic", 0.0,  minVal = 0, maxVal = 40, vary = False)
modelRef.setParam("rOleic", 21.0,  minVal = 0, maxVal = 200, vary = False)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("d", 14.0)
modelRef.setConstantParam("bg", 0)
modelRef.setConstantParam("sldCore", 41.85e-6)
modelRef.setConstantParam("sldShell", 8.52e-6)
modelRef.setConstantParam("sldSolvent", 7.55e-6)
modelRef.setConstantParam("sldOleic", 8.52e-6)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()