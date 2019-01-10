#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import CubeCSCoupledSigD
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
app.setExperiment(Saxs)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/DD144.xye')
dataRef.sliceDomain(0.006, 0.25)
dataRef.plotData()

modelRef = app.setModel(CubeCSCoupledSigD)
modelRef.setParam("i0", 0.0281,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("particleSize", 116.12,  minVal = 80, maxVal = 200, vary = True)
modelRef.setParam("d", 37.32,  minVal = 0, maxVal = 60, vary = True)
modelRef.setParam("sigD", 0.152,  minVal = 0, maxVal = 1, vary = True)
modelRef.setParam("sigParticleSize", 0.04475,  minVal = 0, maxVal = 0.25, vary = True)

modelRef.setConstantParam("sldCore", 52.1122e-6) # FeO 4.1809 A
modelRef.setConstantParam("sldShell", 41.8489e-6) # Magnetite 8.3841 A
modelRef.setConstantParam("sldSolvent", 8.01e-6) # Toluene
modelRef.setConstantParam("bg", 0.0)
modelRef.setConstantParam('orderHermite', 10)
modelRef.setConstantParam('orderLegendre', 10)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()