#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sanspol
from modelexp.models.sas import CubeCS, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_neutrons_5A

app = App()
app.setExperiment(Sanspol)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../experimental_data/dd67_rfm_la_scaled.dat', ['p', 'la'])
dataRef.loadFromFile('../../experimental_data/dd67_rfp_la_scaled.dat', ['m', 'la'])
dataRef.loadFromFile('../../experimental_data/dd67_rfm_sa.dat', ['p', 'sa'])
dataRef.loadFromFile('../../experimental_data/dd67_rfp_sa.dat', ['m', 'sa'])
dataRef.onlyPositiveValues()
dataRef.sliceDomain(0, 0.5)
dataRef.plotData()

modelRef = app.setModel(CubeCS, [Magnetic, InstrumentalResolution])
modelRef.setParam("magSldCore", 2.6799999999999996e-07,  minVal = 0, maxVal = 2e-06, vary = True)
modelRef.setConstantParam("sin2alpha", 0.9974654)

modelRef.setConstantParam("i0", 0.2105)
modelRef.setConstantParam("sldCore", 6.5609720000000004e-06)
modelRef.setConstantParam("d", 14.300790488568504)
modelRef.setConstantParam("bg", 0.014660000000000001)
modelRef.setConstantParam("dTheta_sa", 0.0016664352022439611)
modelRef.setConstantParam("dTheta_la", 0.00198)
modelRef.setConstantParam("sldShell", 1.8972e-07)

modelRef.setConstantParam("a", 100.95075087881172)
modelRef.setConstantParam("sigA", 0.06253789531504311)

modelRef.setConstantParam("sldSolvent", sld_neutrons_5A['Toluene-d8'])
modelRef.setConstantParam('wavelength', 5.9984)
modelRef.setConstantParam('dWavelength', 0.04247)

modelRef.updateModel()
app.setFit(LevenbergMarquardt)

app.show()