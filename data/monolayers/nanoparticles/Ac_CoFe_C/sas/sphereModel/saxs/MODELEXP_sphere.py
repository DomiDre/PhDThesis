#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import Sphere
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

modelRef = app.setModel(Sphere)
modelRef.setParam("r", 55.64451414134869,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigR", 0.12989745010048562,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.04,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("sldCore", 4.172e-05,  minVal = 1e-05, maxVal = 5e-05, vary = False)
modelRef.setParam("bg", 0.0,  minVal = 0, maxVal = 0.02, vary = False)

modelRef.setConstantParam("sldSolvent", saxs_sldSolvent)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()