#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SphereCSSCoupled, DataResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
app.setExperiment(Sans)
dataRef = app.setData(XyeData)


dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_sa.dat', ['sa'])
dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_la_scaled.dat', ['la'])
dataRef.sliceDomain(0.004, 0.26)
dataRef.plotData()

modelRef = app.setModel(SphereCSSCoupled, DataResolution)

modelRef.setParam("particleSize", 63.2,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("dShell", 2.96,  minVal = 0, maxVal = 80, vary = False)
modelRef.setParam("dSurfactant", 42.160000000000004,  minVal = 0, maxVal = 80, vary = True)
modelRef.setParam("sigParticleSize", 0.08925,  minVal = 0, maxVal = 0.25, vary = False)
modelRef.setParam("i0", 0.0181,  minVal = 0, maxVal = 0.1, vary = False)
modelRef.setParam("bg", 0.0161,  minVal = 0, maxVal = 0.1, vary = True)

modelRef.setConstantParam("sigD", 0)
modelRef.setConstantParam("sldCore", 7.082e-6)
modelRef.setConstantParam("sldShell", 5.938e-6)
modelRef.setConstantParam("sldSurfactant", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.664e-6)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()