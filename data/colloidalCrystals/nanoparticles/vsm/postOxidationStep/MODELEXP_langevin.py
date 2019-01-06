#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:47:32.203901
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.magnetometry import Vsm
from modelexp.models.magnetometry import LangevinMuWeighted
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

datafile = './rescale/Ol-Fe-C_powderOxidized_296K_rescaled.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.sliceDomain(-2,2)
dataRef.plotData()
modelRef = app.setModel(LangevinMuWeighted)
modelRef.setParam("Ms", 412.40000000000003,  minVal = 100, maxVal = 500, vary = False)
modelRef.setParam("mu", 61600.0,  minVal = 50000, maxVal = 70000, vary = False)
modelRef.setParam("chi", 20.60000000000001,  minVal = -100, maxVal = 100, vary = False)
modelRef.setParam("sigMu", 0.0,  minVal = 0, maxVal = 1, vary = False)
modelRef.setConstantParam('T', 296)

app.setFit(LevenbergMarquardt)

app.show()