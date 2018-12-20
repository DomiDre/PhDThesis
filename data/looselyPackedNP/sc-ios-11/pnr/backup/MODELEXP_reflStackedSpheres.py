#Initialized ScriptFactory v0.2
#Date: 2018-07-09 16:10:34.437894
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments.reflectometry import Reflectometry
from modelexp.models.reflectometry import SphereCSStacked6Spacer, InstrumentalResolution, ShiftQ
from modelexp.data import XyeData
from modelexp.fit import LevenbergMarquardt

from thesis_utils.materials import sld_xray_D8
import numpy as np

app = App()
expRef = app.setExperiment(Reflectometry)
expRef.setResiduumFormula('log chi2')
expRef.setFitRange(0, 0.3)
dataRef = app.setData(XyeData)

dataRef.loadFromFile('./ES_S14_300K_4mT_refl_corrected_combined.xy')
dataRef.sliceDomain(0, 0.12)
dataRef.plotData()

modelRef = app.setModel(SphereCSStacked6Spacer, [InstrumentalResolution, ShiftQ])
modelRef.setParam("bg", 2.31847794323019e-05,  minVal = 0.0, maxVal = 0.0001, vary = True)
modelRef.setParam("roughness", 6.213397066346715,  minVal = 0.5, maxVal = 20, vary = True)
modelRef.setParam("roughnessSlope", 0.05831216759801573,  minVal = 0.0, maxVal = 0.1, vary = True)
modelRef.setParam("packingDensity1", 0.44459614546362636,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity2", 0.5265684787905262,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity3", 0.47095541337680985,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity4", 0.604688919773028,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity5", 0.7001133963165432,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("packingDensity6", 0.23836633650384775,  minVal = 0.0, maxVal = 1.0, vary = True)
modelRef.setParam("layerDistance1", 5.277466921526752,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance2", -28.53969018161934,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance3", -23.04706906759767,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance4", -20.710686437396618,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance5", -10.039595745898552,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("layerDistance6", -19.338611612563746,  minVal = -50, maxVal = 50, vary = True)
modelRef.setParam("dSpacer", 51.5,  minVal = 0, maxVal = 100, vary = False)
modelRef.setParam("sldSpacer", 2.6993456671429752e-06,  minVal = 0, maxVal = 3e-05, vary = True)

modelRef.setConstantParam("r", 54.1)
modelRef.setConstantParam("d", 18.2)
modelRef.setConstantParam('sldCore', 7.00e-6)
modelRef.setConstantParam('sldShell', 0.078e-6)
modelRef.setConstantParam('sldSubstrate', 2.072e-6)
modelRef.setConstantParam('sldBackground', 0e-6)

# D8 properties
modelRef.setConstantParam("i0", 1)
modelRef.setConstantParam("dTheta", 0.0003)
modelRef.setConstantParam("dWavelength", 0.005)
modelRef.setConstantParam('wavelength', 5.14)

#SLD Domain
modelRef.callModelFunctions('setSldDomain', np.linspace(-100, 900, 300))
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()