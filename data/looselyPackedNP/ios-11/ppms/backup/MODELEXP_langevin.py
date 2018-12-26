#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:47:32.203901
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.magnetometry import Vsm
from modelexp.models.magnetometry import Langevin
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

datafile = 'PMK18_20muL_4cmTeflonPara_BGLinSub_rescale.xye'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.plotData()

modelRef = app.setModel(Langevin)
modelRef.setParam("Ms", 152.96840655759837,  minVal = 0, maxVal = 300, vary = True)
modelRef.setParam("mu", 12752.78393537624,  minVal = 0, maxVal = 50000, vary = True)
modelRef.setParam("chi", 11.81830000698389,  minVal = -100, maxVal = 100, vary = True)
modelRef.setParam("sigMu", 0,  minVal = 0, maxVal = 0.8, vary = False)

app.setFit(LevenbergMarquardt)

app.show()