#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import PolarizedReflectometry
from modelexp.models.reflectometry import SphereCSStacked11Spacer, InstrumentalResolution, Magnetic
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(PolarizedReflectometry)
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0.005, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('../../data/footprint_corrected/ES_S17_30K_FC_73000Oe_reduced_in_x_ai_uu_masked_qz_I_fcorrected.xye', ['p'])
dataRef.loadFromFile('../../data/footprint_corrected/ES_S17_30K_FC_73000Oe_reduced_in_x_ai_du_masked_qz_I_fcorrected.xye', ['m'])
dataRef.sliceDomain(0.007, 1)
dataRef.plotData()
modelRef = app.setModel(SphereCSStacked11Spacer, [Magnetic, InstrumentalResolution])


modelRef.setParam("magSldCore", 4.35e-07,  minVal = 0, maxVal = 3e-06, vary = True)
modelRef.combineParameters('magSldCore', 'magSldShell')

modelRef.setConstantParam("polarizationEfficiency", 1.0)
modelRef.setConstantParam("bg", 1.7000000000000002e-06)
modelRef.setConstantParam("roughness", 9.60706155435272)
modelRef.setConstantParam("roughnessSlope", 0.0004242190508670918)
modelRef.setConstantParam("packingDensity1", 0.8094435466098029)
modelRef.setConstantParam("packingDensity2", 0.6889707737681452)
modelRef.setConstantParam("packingDensity3", 0.6178498513937996)
modelRef.setConstantParam("packingDensity4", 0.612296893901263)
modelRef.setConstantParam("packingDensity5", 0.6496893761538566)
modelRef.setConstantParam("packingDensity6", 0.6281554882604345)
modelRef.setConstantParam("packingDensity7", 0.6076174324895113)
modelRef.setConstantParam("packingDensity8", 0.5677610415585745)
modelRef.setConstantParam("packingDensity9", 0.5151829912424655)
modelRef.setConstantParam("packingDensity10", 0.4043711162261666)
modelRef.setConstantParam("packingDensity11", 0.0)
modelRef.setConstantParam("layerDistance1", -7.099999999999994)
modelRef.setConstantParam("layerDistance2", -19.299999999999997)
modelRef.setConstantParam("layerDistance3", -28.299999999999997)
modelRef.setConstantParam("layerDistance4", -29.7)
modelRef.setConstantParam("layerDistance5", -26.9)
modelRef.setConstantParam("layerDistance6", -23.5)
modelRef.setConstantParam("layerDistance7", -22.099999999999998)
modelRef.setConstantParam("layerDistance8", -20.9)
modelRef.setConstantParam("layerDistance9", -20.799999999999997)
modelRef.setConstantParam("layerDistance10", -22.599999999999998)
modelRef.setConstantParam("layerDistance11", -48.0)
modelRef.setConstantParam("dSpacer", 37.50041227348886)
modelRef.setConstantParam("sldSpacer", 0.0)


modelRef.setConstantParam("r", 34.88)
modelRef.setConstantParam("d", 14.7)

modelRef.setConstantParam('sldCore', 7.00e-6)
modelRef.setConstantParam('sldShell', 0.078e-6)
modelRef.setConstantParam('sldSubstrate', 2.072e-6)
modelRef.setConstantParam('sldBackground', 0e-6)

# SADAM properties
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0003)
modelRef.setConstantParam("dWavelength", 0.0021)
modelRef.setConstantParam('wavelength', 5.14)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 1200, 500))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()