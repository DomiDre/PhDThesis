#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Saxs
from modelexp.models.sas import SphereCSCoupled
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
expRef = app.setExperiment(Saxs)
expRef.setFitRange(0.03, 0.4)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/DD144.xye')
# dataRef.sliceDomain(0., 0.25)
dataRef.plotData()

modelRef = app.setModel(SphereCSCoupled)
modelRef.setParam("particleSize", 70.61297745016725,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("d", 0.0,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigParticleSize", 0.08975,  minVal = 0, maxVal = 0.25, vary = True)
modelRef.setParam("i0", 0.01633013962278655,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("bg", 0.00062,  minVal = 0, maxVal = 0.02, vary = True)

modelRef.setConstantParam("sldCore", 52.1122e-6) # FeO 4.1809 A
modelRef.setConstantParam("sldShell", 41.8489e-6) # Magnetite 8.3841 A
modelRef.setConstantParam("sldSolvent", 8.01e-6) # Toluene
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()