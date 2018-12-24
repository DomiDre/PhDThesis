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

dataRef.loadFromFile('../mftFiles/DD213_7_5K_-100mT_u.mft', ['m'])
dataRef.loadFromFile('../mftFiles/DD213_7_5K_-100mT_d.mft', ['p'])
dataRef.sliceDomain(0.007, 0.25)
dataRef.plotData()

modelRef = app.setModel(CubeCSDoubleLayer, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("i0", 0.9675,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setParam("roughness", 2.8840142648057676,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("packingDensity1", 0.9990474148273498,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity2", 0.290000000252444,  minVal = 0.0, maxVal = 1.0, vary = True)

modelRef.setParam("spacerThickness", 13.591109634954412,  minVal = 0, maxVal = 200, vary = True)
modelRef.setParam("coverage", 0.22447691937639175,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("magSldCore", 8.520000928020591e-07,  minVal = 0.0, maxVal = 1.2e-06, vary = True)

modelRef.setParam("a", 89.11772847176248,  minVal = 0, maxVal = 120, vary = True)
modelRef.setParam("d", 10.28993320605696,  minVal = 0, maxVal = 25, vary = True)
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