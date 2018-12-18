#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import SphereCSStackedLinearSpacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S14.xye')
dataRef.sliceDomain(0, 0.15)
dataRef.plotData()

modelRef = app.setModel(SphereCSStackedLinearSpacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 1.9000000000000002e-06,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 6.413432866975644,  minVal = 0.0, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.054400000000000004,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("packingDensity", 0.263,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensitySlope", 0.0007849027134417307,  minVal = -0.005, maxVal = 0.005, vary = True)
modelRef.setParam("layerDistance", -45.3,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistanceSlope", -0.15132265954272872,  minVal = -1, maxVal = 1, vary = True)
modelRef.setParam("dSpacer", 74.3,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 7.440000000000001e-06,  minVal = 0, maxVal = 3e-05, vary = True)
modelRef.setParam("dWavelength", 0.0248543525248589,  minVal = 0, maxVal = 0.1, vary = True)
modelRef.setParam("qShift", 0.0015552241259844165,  minVal = -0.01, maxVal = 0.01, vary = True)

modelRef.setConstantParam("r", 54.1)
modelRef.setConstantParam("d", 18.2)
modelRef.setConstantParam("sigR", 0.0545)
modelRef.setConstantParam('sldCore', sld_xray_D8['Magnetite'].real)
modelRef.setConstantParam('sldShell', sld_xray_D8['Oleic Acid'].real)
modelRef.setConstantParam('sldSubstrate', sld_xray_D8['Silicon'].real)
modelRef.setConstantParam('sldBackground', 0e-6)
modelRef.setConstantParam('nPeriods', 5)

# D8 properties
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0)
modelRef.setConstantParam('wavelength', 1.5418)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 700, 150))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()