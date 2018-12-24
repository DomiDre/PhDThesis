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

datafile = './dd205_4_300K_columnfile.dat'

app = App()
app.setExperiment(Vsm)

dataRef = app.setData(XyeData)
dataRef.loadFromFile(datafile)
dataRef.sliceDomain(-1, 1)
dataRef.plotData()

modelRef = app.setModel(Langevin)
modelRef.setParam("Ms", 36.44333307188932,  minVal = 0, maxVal = 70, vary = True)
modelRef.setParam("mu", 16242.446837944657,  minVal = 0, maxVal = 50000, vary = True)
modelRef.setParam("chi", -21.32300149434822,  minVal = -100, maxVal = 100, vary = True)
# modelRef.setParam("sigMu", 0.3, minVal =0, maxVal= 1, vary=True)
modelRef.setConstantParam("sigMu", 0.0)
modelRef.setConstantParam('T', 300)

app.setFit(LevenbergMarquardt)

app.show()