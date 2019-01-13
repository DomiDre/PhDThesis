#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import CubeCSDoubleLayerNoSpacer, Magnetic, DataResolution
from modelexp.data import MftData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_neutrons_5A

app = App()
expRef = app.setExperiment(PolarizedReflectometry)
expRef.setResiduumFormula('log chi2')
dataRef = app.setData(MftData)

dataRef.loadFromFile('../mftFiles/DD205_3_5K_10mT_u.mft', ['m'])
dataRef.loadFromFile('../mftFiles/DD205_3_5K_10mT_d.mft', ['p'])
dataRef.sliceDomain(0.007, 0.25)
dataRef.plotData()

modelRef = app.setModel(CubeCSDoubleLayerNoSpacer, [Magnetic, DataResolution])
modelRef.setResolution()

modelRef.setParam("i0", 0.924,  minVal = 0, maxVal = 1.5, vary = False)
modelRef.setParam("bg", 5.2e-07,  minVal = 0, maxVal = 1e-05, vary = False)
modelRef.setParam("roughnessSubstrate", 13.26,  minVal = 0, maxVal = 60, vary = False)
modelRef.setParam("roughnessShellCube1", 13.32,  minVal = 0, maxVal = 60, vary = False)
modelRef.setParam("roughnessCubeShell1", 14.82,  minVal = 0, maxVal = 60, vary = False)
modelRef.setParam("roughnessShellPMMA", 15.059999999999999,  minVal = 0, maxVal = 60, vary = False)
modelRef.setParam("roughnessPMMAShell", 15.54,  minVal = 0, maxVal = 60, vary = False)
modelRef.setParam("roughnessShellCube2", 15.059999999999999,  minVal = 0, maxVal = 60, vary = False)
modelRef.setParam("roughnessCubeShell2", 4.5,  minVal = 0, maxVal = 60, vary = False)
modelRef.setParam("packingDensity1", 0.442,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity2", 0.435,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("thicknessPMMA", 702.7530245474359,  minVal = 500, maxVal = 1000, vary = True)
modelRef.setParam("thicknessShell1Lower", 14.863218612022077,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell1Top", 18.726382389545147,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("thicknessShell2Lower", 8.0,  minVal = 0, maxVal = 100, vary = False)

# modelRef.combineParameters('thicknessShell1Lower', 'thicknessShell1Top')
# modelRef.combineParameters('thicknessShell1Lower', 'thicknessShell2Lower')
# modelRef.combineParameters('thicknessShell1Lower', 'thicknessShell2Top')

# modelRef.combineParameters('roughnessShellCube1', 'roughnessCubeShell1')
# modelRef.combineParameters('roughnessShellCube2', 'roughnessCubeShell2')

modelRef.setConstantParam('roughnessShellAir', 0)
modelRef.setConstantParam('thicknessShell2Top', 0)
modelRef.setConstantParam("magSldCore", 0)
modelRef.setConstantParam("gamma", 0)
modelRef.setConstantParam("polarizationEfficiency", 0.98)

modelRef.setConstantParam("a", 93.84)

modelRef.setConstantParam("sldCore", 6.194e-06)
modelRef.setConstantParam("sldSubstrate", 2.079e-6)
modelRef.setConstantParam("sldShellLower", 0.078e-06)
modelRef.setConstantParam("sldShellTop", 0.078e-6)
modelRef.setConstantParam("sldPMMA", 1.059e-6)

modelRef.updateModel()

fit = app.setFit(LevenbergMarquardt)

app.show()