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

dataRef.loadFromFile('../mftFiles/DD205_5_5K_10mT_u.mft', ['p'])
dataRef.loadFromFile('../mftFiles/DD205_5_5K_10mT_d.mft', ['m'])
dataRef.sliceDomain(0.007, 0.25)
dataRef.plotData()

modelRef = app.setModel(CubeCSDoubleLayer, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("i0", 0.9105,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setParam("roughness", 0.0,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("packingDensity1", 0.63,  minVal = 0.0, maxVal = 1.0, vary = True)
# modelRef.setParam("packingDensity2", 0.8862431136043241,  minVal = 0.0, maxVal = 1.0, vary = True)

modelRef.setParam("spacerThickness", 1539.0,  minVal = 1000, maxVal = 2000, vary = True)
modelRef.setParam("coverage", 1.0,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("magSldCore", 0.0,  minVal = 0.0, maxVal = 2e-06, vary = False)

modelRef.setParam("a", 93.84,  minVal = 0, maxVal = 120, vary = False)
modelRef.setParam("d", 9.525,  minVal = 0, maxVal = 25, vary = False)
modelRef.combineParameters('packingDensity1', 'packingDensity2')
modelRef.combineParameters('roughness', 'roughnessSubstrate')
modelRef.setConstantParam("bottomThickness", 0)

modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam('sldCore', 6.86e-6)#sld_neutrons_5A['Cobalt Ferrite'].real)
modelRef.setConstantParam('sldShell', sld_neutrons_5A['Oleic Acid'].real)
modelRef.setConstantParam('sldMatrix', 0)
modelRef.setConstantParam('sldSubstrate', sld_neutrons_5A['Silicon'].real)
modelRef.setConstantParam('sldBottom',  sld_neutrons_5A['Silicon Dioxide'].real)
modelRef.setConstantParam('sldSpacer', sld_neutrons_5A['PMMA'].real)
# modelRef.setConstantParam("roughnessSubstrate", 9.1647)

modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()