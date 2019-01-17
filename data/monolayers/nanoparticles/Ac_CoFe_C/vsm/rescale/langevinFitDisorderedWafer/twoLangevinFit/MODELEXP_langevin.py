#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:47:32.203901
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
import numpy as np
from modelexp import App
from modelexp.experiments.magnetometry import Vsm
from modelexp.models.magnetometry import TwoLangevin
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt
from PPMS.ppms import PPMS

datafile = '../../../data_disorderedWafer/DD226_2_HYST_300K.DAT'

app = App()
expRef = app.setExperiment(Vsm)
expRef.setFitRange(-9, 9)

ppms = PPMS()
ppms.load(datafile)
ppms.remove_virgin_data()
B, M = ppms.get_BM()
sM = ppms.get('M. Std. Err. (emu)')
# valid_range = np.logical_and(B>-2.3, B<2.3)
# B = B[valid_range]
# M = M[valid_range]
# sM = sM[valid_range]

dataRef = app.setData(XyeData)
dataset = XyeData()
dataset.setData(B, M, sM)
dataRef.addDataset(dataset)

dataRef.plotData()
modelRef = app.setModel(TwoLangevin)
modelRef.setParam("Ms1", 0.021253964914367277,  minVal = 0, maxVal = 0.04, vary = True)
modelRef.setParam("Ms2", 0.02284631097520846,  minVal = 0, maxVal = 0.04, vary = True)
modelRef.setParam("mu1", 33780.437,  minVal = 1, maxVal = 60000, vary = True)
modelRef.setParam("mu2", 1928.9564004039364,  minVal = 1, maxVal = 4000, vary = True)
modelRef.setParam("chi", -0.036351635132555155,  minVal = -0.1, maxVal = 0.1, vary = True)
modelRef.setConstantParam('T', 300) # 22 C

modelRef.updateModel()
app.setFit(LevenbergMarquardt)

app.show()