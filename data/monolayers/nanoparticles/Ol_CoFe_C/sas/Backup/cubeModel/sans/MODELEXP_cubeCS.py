#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sans
from modelexp.models.sas import CubeCS, InstrumentalResolution
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
app.setExperiment(Sans)
dataRef = app.setData(XyeData)


dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_sa.dat', ['sa'])
dataRef.loadFromFile('../../experimental_data/DD67_nuclear20_la_scaled.dat', ['la'])
dataRef.sliceDomain(0.004, 0.5)
dataRef.plotData()

modelRef = app.setModel(CubeCS, InstrumentalResolution)
modelRef.setParam("i0", 0.2105,  minVal = 0, maxVal = 0.5, vary = True)
modelRef.setParam("sldCore", 6.5609720000000004e-06,  minVal = 4.293e-06, maxVal = 7.289e-06, vary = True)
modelRef.setParam("d", 14.300790488568504,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("bg", 0.014660000000000001,  minVal = 0, maxVal = 0.02, vary = False)
modelRef.setParam("dTheta_sa", 0.0016664352022439611,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("dTheta_la", 0.00198,  minVal = 0, maxVal = 0.01, vary = True)
modelRef.setParam("sldShell", 1.8972e-07,  minVal = 7.8e-08, maxVal = 5.664e-06, vary = True)

modelRef.setConstantParam("a", 100.95075087881172)
modelRef.setConstantParam("sigA", 0.06253789531504311)

modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()