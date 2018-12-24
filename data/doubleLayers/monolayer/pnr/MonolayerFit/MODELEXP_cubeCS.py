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

dataRef.loadFromFile('../mftFiles/DD205_4_5K_10mT_d.mft', ['m'])
dataRef.loadFromFile('../mftFiles/DD205_4_5K_10mT_u.mft', ['p'])
dataRef.sliceDomain(0.007, 1)
dataRef.plotData()

modelRef = app.setModel(CubeCSStacked, [Magnetic, DataResolution])
modelRef.setResolution()
modelRef.setParam("magSldCore", 0.0,  minVal = 0.0, maxVal = 2e-06, vary = False)
modelRef.setParam("bg", 9.96e-07,  minVal = 0.0, maxVal = 3e-06, vary = False)
modelRef.setParam("roughnessSubstrate", 0.0,  minVal = 0.0, maxVal = 50, vary = False)
modelRef.setParam("roughnessPlus1", 4.31554644256337,  minVal = 0.0, maxVal = 50, vary = True)
modelRef.setParam("packingDensity", 0.4684044463774274,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("d", 9.54,  minVal = 0, maxVal = 45, vary = False)
modelRef.setParam("a", 93.84,  minVal = 0, maxVal = 120, vary = False)
modelRef.setParam("i0", 0.9249775925086379,  minVal = 0.7, maxVal = 1.2, vary = True)

modelRef.setConstantParam('coverage', 1)
modelRef.setConstantParam('sldCore', sld_neutrons_5A['Cobalt Ferrite'].real)
modelRef.setConstantParam('sldShell', sld_neutrons_5A['Oleic Acid'].real)
modelRef.setConstantParam('sldMatrix', 0)
modelRef.setConstantParam('sldSubstrate', sld_neutrons_5A['Silicon'].real)

modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()