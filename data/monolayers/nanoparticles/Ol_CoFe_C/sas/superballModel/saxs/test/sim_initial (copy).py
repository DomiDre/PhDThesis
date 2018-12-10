#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import Cli
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SuperballCSSCoupledOA, DataResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A
import datetime

app = Cli()
app.setExperiment(Saxs)
dataRef = app.setData(XyerData)


dataRef.loadFromFile('../../../experimental_data/DD67.xye')
dataRef.sliceDomain(0.004, 0.26)

modelRef = app.setModel(SuperballCSSCoupledOA, DataResolution)
modelRef.setResolution(['sans'])

modelRef.setParam("particleSize", 54.9248019,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dShell", 18.9612785,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("dSurfactant", 15.5,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("pVal", 2.26,  minVal = 0, maxVal = 5, vary = True)
modelRef.setParam("sigParticleSize", 0.0747826,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.02033677,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("i0Oleic", 0.41, min=0, max=10, vary=True)
modelRef.setParam("sldShell", 46.447e-6, minVal=3e-5, maxVal=5e-5, vary=True)
#	1
#	20

modelRef.setConstantParam("rOleic", 21)
modelRef.setConstantParam("bg", 0.)
modelRef.setConstantParam('orderHermite', 5)
modelRef.setConstantParam('orderLegendre', 5)
modelRef.setConstantParam("sldCore", 51.22e-6)
modelRef.setConstantParam("sldShell", 45.704e-6)
modelRef.setConstantParam("sldSurfactant", 8.52e-6)
modelRef.setConstantParam("sldSolvent", 8.01e-6)

modelRef.updateModel()

# save model
modelData_sa = modelRef.getModelset(0)
q_sa = modelData_sa.getDomain()
I_sa = modelData_sa.getValues()
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

r_sa = modelData_sa.r
sld_sa = modelData_sa.sld

with open(f'superballData_simulation_sld.xy', 'w') as f:
  f.write(f'#Superball Data generated at {datetime.datetime.now()}\n')
  f.write(f'#[[Parameters]]\n')
  for param in modelRef.params:
    f.write(f'#{param}\t{modelRef.params[param].value}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] sa\n')
  f.write(f'#r\tsld\n')
  for j in range(len(r_sa)):
    f.write(f'{r_sa[j]}\t{sld_sa[j]}\n')