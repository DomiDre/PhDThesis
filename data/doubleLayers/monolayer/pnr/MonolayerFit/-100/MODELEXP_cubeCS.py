#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import CubeCSStacked, Magnetic, DataResolution
from fortRefl import nanocubes, algorithms
import numpy as np
from modelexp.data import MftData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_neutrons_5A

app = App()
app.setExperiment(PolarizedReflectometry)
dataRef = app.setData(MftData)

dataRef.loadFromFile('../../mftFiles/DD205_4_5K_-100mT_u.mft', ['m'])
dataRef.loadFromFile('../../mftFiles/DD205_4_5K_-100mT_d.mft', ['p'])
dataRef.sliceDomain(0.007, 1)
dataRef.plotData()

modelRef = app.setModel(CubeCSStacked, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("magSldCore", 7.363840537180619e-07,  minVal = -2e-06, maxVal = 2e-06, vary = True)
modelRef.setParam("bg", 2.9999999974747418e-05,  minVal = 0.0, maxVal = 3e-05, vary = True)
modelRef.setParam("roughnessSubstrate", 0.0,  minVal = 0.0, maxVal = 50, vary = False)
modelRef.setParam("roughnessPlus1", 4.25,  minVal = 0.0, maxVal = 50, vary = False)
modelRef.setParam("packingDensity", 0.468,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("d", 9.54,  minVal = 0, maxVal = 45, vary = False)
modelRef.setParam("a", 93.84,  minVal = 0, maxVal = 120, vary = False)
modelRef.setParam("i0", 0.9245,  minVal = 0.7, maxVal = 1.2, vary = False)

# modelRef.setParam("qMisalignment", 3.164782555652493e-05,  minVal = -0.001, maxVal = 0.001, vary = True)

modelRef.setConstantParam('coverage', 1)
modelRef.setConstantParam('sldCore', sld_neutrons_5A['Cobalt Ferrite'].real)
modelRef.setConstantParam('sldShell', sld_neutrons_5A['Oleic Acid'].real)
modelRef.setConstantParam('sldMatrix', 0)
modelRef.setConstantParam('sldSubstrate', sld_neutrons_5A['Silicon'].real)

modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()