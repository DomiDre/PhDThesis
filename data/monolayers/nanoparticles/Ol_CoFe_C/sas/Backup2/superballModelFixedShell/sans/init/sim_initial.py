#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SuperballCSSCoupled, DataResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import datetime

app = Cli()
app.setExperiment(Sans)
dataRef = app.setData(XyerData)


dataRef.loadFromFile('../../../experimental_data/DD67_nuclear20_sa.dat', ['sa'])
dataRef.loadFromFile('../../../experimental_data/DD67_nuclear20_la_scaled.dat', ['la'])
dataRef.sliceDomain(0.004, 0.26)

modelRef = app.setModel(SuperballCSSCoupled, DataResolution)
modelRef.setResolution()
modelRef.setParam("dSurfactant", 19,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("i0", 0.15,  minVal = 0, maxVal = 0.5, vary = True)
modelRef.setParam("bg", 0.01,  minVal = 0, maxVal = 0.1, vary = False)

modelRef.setConstantParam("particleSize", 57.6590717)
modelRef.setConstantParam("dShell", 5.97351175)
modelRef.setConstantParam("pVal", 1.49983)
modelRef.setConstantParam("sigParticleSize", 0.08318968)

modelRef.setConstantParam("sldCore", 7.082e-6)
modelRef.setConstantParam("sldShell", 5.938e-6)
modelRef.setConstantParam("sldSurfactant", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.664e-6)
modelRef.setConstantParam('orderHermite', 2)
modelRef.setConstantParam('orderLegendre', 2)

modelRef.updateModel()

# save model
modelData_sa = modelRef.getModelset(0)
modelData_la = modelRef.getModelset(1)
q_sa = modelData_sa.getDomain()
I_sa = modelData_sa.getValues()
q_la = modelData_la.getDomain()
I_la = modelData_la.getValues()
with open(f'superballData_simulation.xy', 'w') as f:
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