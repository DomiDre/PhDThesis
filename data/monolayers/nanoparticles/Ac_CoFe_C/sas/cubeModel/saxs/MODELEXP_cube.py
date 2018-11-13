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

saxs_sldCore = sld_xray_GALAXI['Cobalt Ferrite'].real
saxs_sldSolvent = sld_xray_GALAXI['n-Hexane'].real

app = App()
app.setExperiment(Saxs)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/AH11.xye')
dataRef.sliceDomain(0., 0.25)
dataRef.plotData()

modelRef = app.setModel(Cube)
modelRef.setParam("a", 90.06071056809513,  minVal = 0, maxVal = 120, vary = True)
modelRef.setParam("sigA", 0.1069991862611728,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.04287558762332592,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("bg", 0.0,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam("sldCore", saxs_sldCore)
modelRef.setConstantParam("sldSolvent", saxs_sldSolvent)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()