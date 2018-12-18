#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import SphereCSStacked11Spacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2 noError')
expRef.setFitRange(0, 0.15)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../ES-S17.xye')
dataRef.sliceDomain(0, 0.15)
dataRef.plotData()
modelRef = app.setModel(SphereCSStacked11Spacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 0.0,  minVal = 0.0, maxVal = 0.0001, vary = False)
modelRef.setParam("roughness", 6.992477752130664,  minVal = 0.0, maxVal = 20, vary = False)
modelRef.setParam("roughnessSlope", 0.0357,  minVal = 0.0, maxVal = 0.1, vary = False)
modelRef.setParam("packingDensity1", 0.3418736204532456,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity2", 0.3201972892226115,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity3", 0.29997068051048337,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity4", 0.3311662405276756,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity5", 0.37635961660341605,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity6", 0.4022638610346042,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity7", 0.4112342887431363,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity8", 0.4350218561115085,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity9", 0.42557823053945254,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity10", 0.335,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("packingDensity11", 0.07800266850752036,  minVal = 0.0, maxVal = 1.0, vary = False)
modelRef.setParam("layerDistance1", -13.316998702765915,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance2", -13.273426145456376,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance3", -11.34413751841798,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance4", -12.229535565460445,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance5", -14.199999999999996,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance6", -14.699999999999996,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance7", -14.199999999999996,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance8", -12.285399259394012,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance9", -4.295376595490673,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance10", -24.84561718547702,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("layerDistance11", -15.321633610259745,  minVal = -50, maxVal = 50, vary = False)
modelRef.setParam("dSpacer", 52.6,  minVal = 0, maxVal = 100, vary = True)
modelRef.setParam("sldSpacer", 2.1600000000000005e-06,  minVal = 0, maxVal = 3e-05, vary = True)
modelRef.setParam("dWavelength", 0.011000000000000001,  minVal = 0, maxVal = 0.1, vary = False)
modelRef.setParam("qShift", -0.0016000000000000042,  minVal = -0.1, maxVal = 0.1, vary = False)

modelRef.setConstantParam("r", 35.4)
modelRef.setConstantParam("d", 16.9)
modelRef.setConstantParam("sigR", 0.0752)
modelRef.setConstantParam('sldCore', sld_xray_D8['Magnetite'].real)
modelRef.setConstantParam('sldShell', sld_xray_D8['Oleic Acid'].real)
modelRef.setConstantParam('sldSubstrate', sld_xray_D8['Silicon'].real)
modelRef.setConstantParam('sldBackground', 0e-6)

# D8 properties
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0)
modelRef.setConstantParam('wavelength', 1.5418)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 1200, 500))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()