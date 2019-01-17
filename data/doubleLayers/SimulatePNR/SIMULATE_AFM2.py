#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import CubeCSDoubleLayerOnSpacer, Magnetic, InstrumentalResolution
from modelexp.data import MftData
from modelexp.fit import LevenbergMarquardt
import numpy as np
import datetime

from thesis_utils.materials import sld_neutrons_5A

app = App()
expRef = app.setExperiment(PolarizedReflectometry)

modelRef = app.setModel(CubeCSDoubleLayerOnSpacer, [Magnetic, InstrumentalResolution])
q_range = np.linspace(1e-3, 0.25, 2000)
modelRef.addModel(q_range, 'p')
modelRef.addModel(q_range, 'm')

modelRef.setConstantParam("roughnessSubstrate", 20.041031505537347)
modelRef.setConstantParam("roughnessSpacer", 23.527612662946385)
modelRef.setConstantParam("roughnessShellCube1", 14.57008761856568)
modelRef.setConstantParam("roughnessCubeShell1", 22.31642583659761)
modelRef.setConstantParam("roughnessShellAir", 8.4)
modelRef.setConstantParam("packingDensity1", 0.506358957399347)
modelRef.setConstantParam("packingDensity2", 0.506358957399347)
modelRef.setConstantParam("thicknessShell1Lower", 36.60100058114454)
modelRef.setConstantParam("thicknessShell1Top", 39.6)
modelRef.setConstantParam("thicknessShell2Lower", 36.60100058114454)
modelRef.setConstantParam("thicknessShell2Top", 39.6)
modelRef.setConstantParam("thicknessSpacer", 24.25716072643032)
modelRef.setConstantParam("bg", 1.3999999999999998e-07)
modelRef.setConstantParam("roughnessShellCube2", 14.57008761856568)
modelRef.setConstantParam("roughnessCubeShell2", 22.31642583659761)
modelRef.setConstantParam('roughnessShellAir', 0)
modelRef.setConstantParam('thicknessShell2Top', 0)

modelRef.setParam("thicknessPMMA", 721.0,  minVal = 0, maxVal = 1000, vary = True)
modelRef.setParam("roughnessShellPMMA", 0.0,  minVal = 0, maxVal = 60, vary = True)
modelRef.setParam("roughnessPMMAShell", 0.0,  minVal = 0, maxVal = 60, vary = True)
modelRef.setParam("magSldCore1", -0.92e-6,  minVal = -2e-6, maxVal = 2e-6, vary = False)
modelRef.setParam("magSldCore2", 0.92e-6,  minVal = -2e-6, maxVal = 2e-6, vary = False)
modelRef.setConstantParam("dTheta", 0.3e-3)
modelRef.setConstantParam("dWavelength", 0.025)
modelRef.setConstantParam("wavelength", 5)

modelRef.setConstantParam("gamma", 0)
modelRef.setConstantParam("polarizationEfficiency", 0.98)

modelRef.setConstantParam("a", 93.84)
modelRef.setConstantParam("i0", 1.0)

modelRef.setConstantParam("sldCore", 6.194e-06)
modelRef.setConstantParam("sldSubstrate", 2.079e-6)
modelRef.setConstantParam("sldSpacer", 4.186e-06)
modelRef.setConstantParam("sldShellLower", 0.078e-06)
modelRef.setConstantParam("sldShellTop", 0.078e-6)
modelRef.setConstantParam("sldPMMA", 1.059e-6)

modelRef.updateModel()

# save model
modelData_p = modelRef.getModelset(0)
modelData_m = modelRef.getModelset(1)
q_p = modelData_p.getDomain()
I_p = modelData_p.getValues()
q_m = modelData_m.getDomain()
I_m = modelData_m.getValues()
z = modelData_p.z
rho = modelData_p.sld
rhoMag = modelData_p.sldMag
with open(f'simulation_AFM2.xy', 'w') as f:
  f.write(f'#PNR generated at {datetime.datetime.now()}\n')
  f.write(f'#[[Parameters]]\n')
  for param in modelRef.params:
    f.write(f'#{param}\t{modelRef.params[param].value}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] p\n')
  f.write(f'#q\tI\n')
  for j in range(len(q_p)):
    f.write(f'{q_p[j]}\t{I_p[j]}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]] m\n')
  f.write(f'#q\tI\n')
  for j in range(len(q_m)):
    f.write(f'{q_m[j]}\t{I_m[j]}\n')

with open(f'sld_AFM2.xy', 'w') as f:
  f.write(f'#PNR generated at {datetime.datetime.now()}\n')
  f.write(f'#[[Parameters]]\n')
  for param in modelRef.params:
    f.write(f'#{param}\t{modelRef.params[param].value}\n')
  f.write(f'#\n')
  f.write(f'#[[Data]]\n')
  f.write(f'#z\trho_nuc\trho_mag\n')
  for j in range(len(z)):
    f.write(f'{z[j]}\t{rho[j]}\t{rhoMag[j]}\n')
# app.show()