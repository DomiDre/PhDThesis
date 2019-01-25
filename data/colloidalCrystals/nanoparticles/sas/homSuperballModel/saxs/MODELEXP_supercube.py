#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import Superball
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt
import datetime
import numpy as np
app = Cli()
expRef = app.setExperiment(Saxs)
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0.02, 0.3)
dataRef = app.setData(XyerData)

dataRef.loadFromFile('../../experimental_data/DD144.xye')
# dataRef.reducePointDensity(4)
modelRef = app.setModel(Superball)
modelRef.setParam("r",     61.1466380,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("pVal",             2.17635593,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sigR",  0.07531189,  minVal = 0, maxVal = 0.5, vary = True)
modelRef.setParam("i0",               0.02970345,  minVal = 0, maxVal = 0.1, vary = True)

# modelRef.setConstantParam('x', 1)
modelRef.setConstantParam("bg", 0.)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('orderHermite', 10)

modelRef.setConstantParam("sldCore", 41.8489e-6) # Magnetite 8.3841 A
modelRef.setConstantParam("sldSolvent", 8.01e-6) # Toluene

modelRef.updateModel()

# modelData = modelRef.getModelset(0)
# q = modelData.getDomain()
# I = modelData.getValues()
# with open(f'simulated_model.xy', 'w') as f:
#   f.write(f'#Superball Data generated at {datetime.datetime.now()}\n')
#   f.write(f'#[[Parameters]]\n')
#   for param in modelRef.params:
#     f.write(f'#{param}\t{modelRef.params[param].value}\n')
#   f.write(f'#\n')
#   f.write(f'#[[Data]]\n')
#   f.write(f'#q\tI\n')
#   for j in range(len(q)):
#     f.write(f'{q[j]}\t{I[j]}\n')

# r = modelData.r
# sld = modelData.sld

# with open(f'simulated_model_sld.xy', 'w') as f:
#   f.write(f'#Superball Data generated at {datetime.datetime.now()}\n')
#   f.write(f'#[[Parameters]]\n')
#   for param in modelRef.params:
#     f.write(f'#{param}\t{modelRef.params[param].value}\n')
#   f.write(f'#\n')
#   f.write(f'#[[Data]] sa\n')
#   f.write(f'#r\tsld\n')
#   for j in range(len(r)):
#     f.write(f'{r[j]}\t{sld[j]}\n')
fit = app.setFit(LevenbergMarquardt)
fit.printIteration = 1
fit.save_intermediate_results_every = 1
fit.fit()
fit.exportResult('fit_result.dat')