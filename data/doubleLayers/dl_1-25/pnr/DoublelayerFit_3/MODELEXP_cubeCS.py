#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import CubeCSDoubleLayer, Magnetic, DataResolution
from modelexp.data import MftData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_neutrons_5A

app = App()
app.setExperiment(PolarizedReflectometry)
dataRef = app.setData(MftData)

dataRef.loadFromFile('../mftFiles/DD205_3_5K_10mT_u.mft', ['m'])
dataRef.loadFromFile('../mftFiles/DD205_3_5K_10mT_d.mft', ['p'])
dataRef.sliceDomain(0.007, 0.25)
dataRef.plotData()

modelRef = app.setModel(CubeCSDoubleLayer, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("i0", 0.924,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setParam("roughnessSubstrate", 0.0,  minVal = 0, maxVal = 20, vary = True)
modelRef.setParam("roughnessPlus1", 10.244727174917108,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessPlus2", 0.0,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("packingDensity1", 0.3507562414144833,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity2", 0.5207052067716613,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("spacerThickness", 710.7853872427366,  minVal = 500, maxVal = 1000, vary = True)
modelRef.setParam("coverage", 1.0,  minVal = 0, maxVal = 1, vary = False)

modelRef.setParam("magSldCore", 0.0,  minVal = 0.0, maxVal = 2e-06, vary = False)

modelRef.setConstantParam("a", 93.84)
modelRef.setConstantParam("d", 9.525)
modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam('sldCore', sld_neutrons_5A['Cobalt Ferrite'].real)
modelRef.setConstantParam('sldShell', sld_neutrons_5A['Oleic Acid'].real)
modelRef.setConstantParam('sldSubstrate', sld_neutrons_5A['Silicon'].real)
modelRef.setConstantParam('sldSpacer', sld_neutrons_5A['PMMA'].real)
modelRef.setConstantParam('sldMatrix', 0)

modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()