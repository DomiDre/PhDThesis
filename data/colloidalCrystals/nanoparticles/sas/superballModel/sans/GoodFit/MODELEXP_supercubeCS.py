#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SuperballCSSCoupled, InstrumentalResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import datetime
app = Cli()
expRef = app.setExperiment(Sans)
expRef.setResiduumFormula('log chi2 noError')
dataRef = app.setData(XyerData)


dataRef.loadFromFile('../../experimental_data/DD144_0A_nuc_SA.dat', ['sa'])
dataRef.loadFromFile('../../experimental_data/DD144_0A_nuc_LA.dat', ['la'])
# dataRef.sliceDomain(0.02, 0.5)
modelRef = app.setModel(SuperballCSSCoupled, InstrumentalResolution)
modelRef.setParam("dShell", 35.6757557, minVal = 0, maxVal = 70, vary=True)
modelRef.setParam("dSurfactant", 14.1,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("i0", 0.05571249,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("bg", 0.,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("dTheta_sa", 0.00150471, minVal = 0, maxVal = 0.01, vary=True)
modelRef.setParam("dTheta_la", 0.00270328, minVal = 0, maxVal = 0.01, vary=True)

modelRef.setConstantParam("pVal", 2.17635593)
modelRef.setConstantParam("particleSize", 61.1466380)
modelRef.setConstantParam("sigParticleSize", 0.07531189)

modelRef.setConstantParam("sldCore", 8.34845e-6) # FeO 4.1809 A
modelRef.setConstantParam("sldShell", 6.9992e-6) # Fe3O4 8.3841 A
modelRef.setConstantParam("sldSurfactant", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.664e-6)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)


modelRef.updateModel()

modelData_sa = modelRef.getModelset(0)
q_sa = modelData_sa.getDomain()
I_sa = modelData_sa.getValues()
modelData_la = modelRef.getModelset(1)
q_la = modelData_la.getDomain()
I_la = modelData_la.getValues()
with open(f'simulated_model.xy', 'w') as f:
  f.write(f'#Superball Data generated at {datetime.datetime.now()}\n')
  f.write(f'#[[Parameters]]\n')
  for param in modelRef.params:
    f.write(f'#{param}\t{modelRef.params[param].value}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] sa\n')
  f.write(f'#q\tI\n')
  for j in range(len(q_sa)):
    f.write(f'{q_sa[j]}\t{I_sa[j]}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] la\n')
  f.write(f'#q\tI\n')
  for j in range(len(q_la)):
    f.write(f'{q_la[j]}\t{I_la[j]}\n')

r = modelData_sa.r
sld = modelData_sa.sld

with open(f'simulated_model_sld.xy', 'w') as f:
  f.write(f'#Superball Data generated at {datetime.datetime.now()}\n')
  f.write(f'#[[Parameters]]\n')
  for param in modelRef.params:
    f.write(f'#{param}\t{modelRef.params[param].value}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]]\n')
  f.write(f'#r\tsld\n')
  for j in range(len(r)):
    f.write(f'{r[j]}\t{sld[j]}\n')

# fit = app.setFit(LevenbergMarquardt)
# fit.printIteration = 1
# fit.save_intermediate_results_every = 1
# fit.fit()
# fit.exportResult('fit_result.dat')