#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import Cube
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import numpy as np
saxs_sldCore = sld_xray_GALAXI['Cobalt Ferrite'].real
saxs_sldSolvent = sld_xray_GALAXI['n-Hexane'].real

# class SaxsNoError(Saxs):
#   def residuum_function(self, I_data, I_error, I_model):
#     return (np.log(I_data) - np.log(I_model))# * I_data / I_error

app = App()
expRef = app.setExperiment(Saxs)
expRef.setFitRange(0.05, 0.4)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/DD67.xye')
dataRef.sliceDomain(0.005, 0.4)
dataRef.plotData()

modelRef = app.setModel(Cube)
modelRef.setParam("a", 98.69470072995549,  minVal = 0, maxVal = 120, vary = True)
modelRef.setParam("sigA", 0.060365869851552845,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.027056690907628564,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("bg", 0.0,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam("sldCore", saxs_sldCore)
modelRef.setConstantParam("sldSolvent", saxs_sldSolvent)
modelRef.setConstantParam("orderHermite", 10)
modelRef.setConstantParam("orderLegendre", 10)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()