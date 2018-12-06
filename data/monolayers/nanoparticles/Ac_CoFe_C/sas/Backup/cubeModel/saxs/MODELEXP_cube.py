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

app = App()
app.setExperiment(Saxs)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/AH11.xye')
dataRef.sliceDomain(0., 0.25)
dataRef.plotData()

modelRef = app.setModel(Cube)
modelRef.setParam("a", 90.06693973715922,  minVal = 0, maxVal = 120, vary = True)
modelRef.setParam("sigA", 0.10694704328488958,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.0446637868038028,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam("sldCore", 41.03e-6)
modelRef.setConstantParam("sldSolvent", 6.46e-6)
modelRef.setConstantParam('orderHermite', 15)
modelRef.setConstantParam('orderLegendre', 15)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()