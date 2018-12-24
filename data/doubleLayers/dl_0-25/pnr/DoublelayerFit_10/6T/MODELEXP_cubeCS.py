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

dataRef.loadFromFile('../../mftFiles/DD205_10_5K_6000mT_u.mft', ['p'])
dataRef.loadFromFile('../../mftFiles/DD205_10_5K_6000mT_d.mft', ['m'])
dataRef.sliceDomain(0.007, 0.25)
dataRef.plotData()

modelRef = app.setModel(CubeCSDoubleLayer, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("i0", 0.9105,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setParam("roughness", 10.420165653851118,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("packingDensity1", 0.33202566730047567,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity2", 0.9999999996703263,  minVal = 0.0, maxVal = 1.0, vary = True)

modelRef.setParam("spacerThickness", 143.00296892087925,  minVal = 0, maxVal = 500, vary = True)
modelRef.setParam("coverage", 0.3770498670411325,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("magSldCore", 1.999477126347237e-06,  minVal = 0.0, maxVal = 2e-06, vary = True)

modelRef.setParam("a", 80.28144366421203,  minVal = 0, maxVal = 120, vary = True)
modelRef.setParam("d", 11.475000000000001,  minVal = 0, maxVal = 25, vary = False)
modelRef.combineParameters('roughness', 'roughnessSubstrate')
modelRef.setConstantParam("bottomThickness", 0)
modelRef.setParam("bg", 4.200436723836452e-07,  minVal = 0, maxVal = 1e-06, vary = True)


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