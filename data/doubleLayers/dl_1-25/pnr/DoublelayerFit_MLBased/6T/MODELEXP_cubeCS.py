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

from thesis_utils.materials import sld_neutrons_5A

app = App()
expRef = app.setExperiment(PolarizedReflectometry)
expRef.setResiduumFormula('log chi2 noError')
dataRef = app.setData(MftData)

dataRef.loadFromFile('../../mftFiles/DD205_3_5K_6000mT_u.mft', ['p'])
dataRef.loadFromFile('../../mftFiles/DD205_3_5K_6000mT_d.mft', ['m'])
dataRef.sliceDomain(0.007, 0.25)
dataRef.plotData()

modelRef = app.setModel(CubeCSDoubleLayerOnSpacer, [Magnetic, InstrumentalResolution])
modelRef.setParam("i0", 0.942,  minVal = 0, maxVal = 1.2, vary = False)

modelRef.setParam("thicknessPMMA", 653.0,  minVal = 0, maxVal = 1000, vary = False)
modelRef.setParam("roughnessShellPMMA", 4.32,  minVal = 0, maxVal = 60, vary = False)
modelRef.setParam("roughnessPMMAShell", 3.9,  minVal = 0, maxVal = 60, vary = False)
modelRef.setParam("dTheta", 0.0003,  minVal = 0, maxVal = 0.001, vary = False)
modelRef.setParam("dWavelength", 0.0499,  minVal = 0, maxVal = 0.1, vary = False)
modelRef.setParam("magSldCore1", 1.143053589888058e-06,  minVal = -2e-06, maxVal = 2e-06, vary = True)
modelRef.setParam("magSldCore2", 9.22967501653923e-07,  minVal = -2e-06, maxVal = 2e-06, vary = True)

modelRef.setParam("roughnessShellCube1", 15.100000000000001,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("roughnessCubeShell1", 26.6,  minVal = 0, maxVal = 100, vary = False)

modelRef.setConstantParam("packingDensity1", 0.506358957399347)
modelRef.setConstantParam("packingDensity2", 0.506358957399347)
modelRef.setConstantParam("roughnessSubstrate", 20.041031505537347)
modelRef.setConstantParam("roughnessSpacer", 23.527612662946385)
# modelRef.setConstantParam("roughnessShellCube1", 14.57008761856568)
# modelRef.setConstantParam("roughnessCubeShell1", 22.31642583659761)
modelRef.setConstantParam("roughnessShellAir", 8.4)
modelRef.setConstantParam("thicknessShell1Lower", 36.60100058114454)
modelRef.setConstantParam("thicknessShell1Top", 39.6)
modelRef.setConstantParam("thicknessShell2Lower", 36.60100058114454)
modelRef.setConstantParam("thicknessShell2Top", 39.6)
modelRef.setConstantParam("thicknessSpacer", 24.25716072643032)
modelRef.setConstantParam("bg", 1.3999999999999998e-07)
modelRef.setConstantParam('roughnessShellAir', 0)
modelRef.setConstantParam('thicknessShell2Top', 0)

modelRef.combineParameters('roughnessShellCube1', 'roughnessShellCube2')
modelRef.combineParameters('roughnessCubeShell1', 'roughnessCubeShell2')
modelRef.setConstantParam("gamma", 0)
modelRef.setConstantParam("polarizationEfficiency", 0.98)
modelRef.setConstantParam("wavelength", 5)

modelRef.setConstantParam("a", 93.84)

modelRef.setConstantParam("sldCore", 6.194e-06)
modelRef.setConstantParam("sldSubstrate", 2.079e-6)
modelRef.setConstantParam("sldSpacer", 4.186e-06)
modelRef.setConstantParam("sldShellLower", 0.078e-06)
modelRef.setConstantParam("sldShellTop", 0.078e-6)
modelRef.setConstantParam("sldPMMA", 1.059e-6)
modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()