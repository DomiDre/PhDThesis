#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp import App
from modelexp.experiments import GenericXy
from modelexp.models.generic import Lorentzian
from modelexp.data import XyData
from modelexp.fit import LevenbergMarquardt

from numpy import pi, sin
wavelength = 1.5406

app = App()
app.setExperiment(GenericXy)
dataRef = app.setData(XyData)

dataRef.loadFromFile('../DD67.dat')

# dataRef.transformDomain(lambda x: 4*pi/wavelength * sin(x/2 * pi/180))
# dataRef.sliceDomain(34.68, 36.3)
dataRef.sliceDomain(34, 36)

dataRef.plotData()

modelRef = app.setModel(Lorentzian)
modelRef.setParam("a", 2100.044816187937,  minVal = 0, maxVal = 6000, vary = True)
modelRef.setParam("x0", 35.153402111851584,  minVal = 34, maxVal = 37, vary = True)
modelRef.setParam("beta", 3.4875306045703054,  minVal = 1, maxVal = 5, vary = True)
modelRef.setParam("offset", 3336.341111205305,  minVal = 0, maxVal = 10000, vary = True)
modelRef.updateModel()

app.setFit(LevenbergMarquardt)

app.show()