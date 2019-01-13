#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import CubeCSDoubleLayerOnSpacer, Magnetic, DataResolution
from modelexp.data import MftData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_neutrons_5A

app = App()
expRef = app.setExperiment(PolarizedReflectometry)
expRef.setResiduumFormula('log chi2 noError')
dataRef = app.setData(MftData)

dataRef.loadFromFile('../mftFiles/DD205_3_5K_10mT_u.mft', ['m'])
dataRef.loadFromFile('../mftFiles/DD205_3_5K_10mT_d.mft', ['p'])
dataRef.sliceDomain(0.007, 0.25)
dataRef.plotData()

modelRef = app.setModel(CubeCSDoubleLayerOnSpacer, [Magnetic, DataResolution])
modelRef.setResolution()



modelRef.setParam("i0", 0.924,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setParam("roughnessSubstrate", 23.448159188181684,  minVal = 0, maxVal = 60, vary = True)
modelRef.setParam("roughnessSpacer", 5.196635926608026,  minVal = 0, maxVal = 60, vary = True)
modelRef.setParam("roughnessShellCube1", 11.725061693394611,  minVal = 0, maxVal = 60, vary = True)
modelRef.setParam("roughnessCubeShell1", 0.0,  minVal = 0, maxVal = 60, vary = False)
modelRef.setParam("roughnessShellPMMA", 0.0,  minVal = 0, maxVal = 60, vary = True)
modelRef.setParam("roughnessPMMAShell", 0.0,  minVal = 0, maxVal = 60, vary = True)
modelRef.setParam("roughnessShellCube2", 10.953328488597649,  minVal = 0, maxVal = 60, vary = True)
modelRef.setParam("roughnessCubeShell2", 0.0,  minVal = 0, maxVal = 60, vary = False)
modelRef.setParam("packingDensity1", 0.4193860989855474,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity2", 0.5906177412883803,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("thicknessPMMA", 721.0,  minVal = 500, maxVal = 1000, vary = True)
modelRef.setParam("thicknessShell1Lower", 4.6000000000000005,  minVal = 0, maxVal = 100, vary = True)
# modelRef.setParam("thicknessShell1Top", 1.8,  minVal = 0, maxVal = 100, vary = True)
# modelRef.setParam("thicknessShell2Lower", 14.100000000000001,  minVal = 0, maxVal = 100, vary = False)
# modelRef.setParam("thicknessShell2Top", 0,  minVal = -inf, maxVal = inf, vary = False)
modelRef.setParam("thicknessSpacer", 0.0,  minVal = 0, maxVal = 100, vary = False)

modelRef.combineParameters('thicknessShell1Lower', 'thicknessShell1Top')
modelRef.combineParameters('thicknessShell1Lower', 'thicknessShell2Lower')
modelRef.combineParameters('thicknessShell1Lower', 'thicknessShell2Top')

modelRef.combineParameters('roughnessShellCube1', 'roughnessCubeShell1')
modelRef.combineParameters('roughnessShellCube2', 'roughnessCubeShell2')

modelRef.setConstantParam('roughnessShellAir', 0)
modelRef.setConstantParam('thicknessShell2Top', 0)
modelRef.setConstantParam("magSldCore", 0)
modelRef.setConstantParam("gamma", 0)
modelRef.setConstantParam("polarizationEfficiency", 0.98)

modelRef.setConstantParam("a", 93.84)
modelRef.setConstantParam("bg", 0.0)

modelRef.setConstantParam("sldCore", 6.194e-06)
modelRef.setConstantParam("sldSubstrate", 2.079e-6)
modelRef.setConstantParam("sldSpacer", 4.186e-06)
modelRef.setConstantParam("sldShellLower", 0.078e-06)
modelRef.setConstantParam("sldShellTop", 0.078e-6)
modelRef.setConstantParam("sldPMMA", 1.059e-6)

modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()