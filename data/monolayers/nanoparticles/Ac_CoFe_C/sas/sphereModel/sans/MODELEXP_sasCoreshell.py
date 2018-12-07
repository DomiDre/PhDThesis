#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.sas import Sans
from modelexp.models.sas import SphereCSOA, InstrumentalResolution, DataResolution
from modelexp.data import XyerData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_GALAXI, sld_neutrons_5A

app = App()
app.setExperiment(Sans)
dataRef = app.setData(XyerData)


dataRef.loadFromFile('../../experimental_data/AH11_nuclear_SA.dat', ['sa'])
dataRef.loadFromFile('../../experimental_data/AH11_nuclear_LA_scaled.dat', ['la'])
dataRef.sliceDomain(0., 0.25)
dataRef.plotData()
#    bg:          0 (fixed)

modelRef = app.setModel(SphereCSOA, DataResolution)
modelRef.setResolution()
modelRef.setParam("i0", 0.034,  minVal = 0, maxVal = 0.2, vary = True)
modelRef.setParam("d", 17.88,  minVal = 0, maxVal = 30, vary = True)
modelRef.setParam("bg", 0.00638,  minVal = 0, maxVal = 0.02, vary = True)
modelRef.setParam("i0Oleic", 0.44,  minVal = 0, maxVal = 10, vary = True)
modelRef.setParam("rOleic", 22.950000000000003,  minVal = 0, maxVal = 50, vary = True)

# modelRef.setParam("dTheta_sa", 0.0,  minVal = 0, maxVal = 0.01, vary = False)
# modelRef.setParam("dTheta_la", 0.0,  minVal = 0, maxVal = 0.01, vary = False)

modelRef.setConstantParam("sldCore", 6.198e-6)
modelRef.setConstantParam("sldShell", 0.078e-6)
modelRef.setConstantParam("sldSolvent", 5.664e-6)
modelRef.setConstantParam("sldOleic", 0.078e-6)
modelRef.setConstantParam("r", 55.6445134)
modelRef.setConstantParam("sigR", 0.12989754)
modelRef.setConstantParam("sigD", 0)
# modelRef.setConstantParam('wavelength', 7.208)
# modelRef.setConstantParam('dWavelength', 0.085)

modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()