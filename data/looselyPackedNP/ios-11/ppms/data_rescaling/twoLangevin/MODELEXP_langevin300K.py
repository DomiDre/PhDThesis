#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:47:32.203901
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from PPMS.ppms import PPMS
import numpy as np
from modelexp import App
from modelexp.experiments.magnetometry import Vsm
from modelexp.models.magnetometry import TwoLangevin
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

datafile = '../../rawdata/PMK18_HYST_300K.DAT'

app = App()
expRef = app.setExperiment(Vsm)
# expRef.setFitRange(-1,1)
Bmin, Bmax = -9, 9

ppms = PPMS()
ppms.load(datafile)
ppms.remove_virgin_data()
B, M = ppms.get_BM()
sM = ppms.get('M. Std. Err. (emu)')
valid_range = np.logical_and(B>Bmin, B<Bmax)
B = B[valid_range]
M = M[valid_range] + 0.1728*B
sM = sM[valid_range]

dataRef = app.setData(XyeData)
dataset = XyeData()
dataset.setData(B, M, sM)
dataRef.addDataset(dataset)

dataRef.plotData()
modelRef = app.setModel(TwoLangevin)
modelRef.setParam("Ms1", 9.204378564447417,  minVal = 0, maxVal = 20, vary = True)
modelRef.setParam("mu1", 13931.508123571306,  minVal = 1, maxVal = 30000, vary = True)
modelRef.setParam("Ms2", 1.7930647514696196,  minVal = 0, maxVal = 20, vary = True)
modelRef.setParam("mu2", 484.79918278808555,  minVal = 1, maxVal = 30000, vary = True)
modelRef.setParam("chi", 0.07001613484477898,  minVal = -1, maxVal = 1, vary = True)
modelRef.setConstantParam('T', 300)

modelRef.updateModel()
app.setFit(LevenbergMarquardt)

app.show()