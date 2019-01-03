from modelexp.data import MultiData, XyemData
import numpy as np

dataRef = MultiData(XyemData)
dataRef.loadFromFile('fit_result.dat')

data = dataRef.getDataset(0)

q = np.array(data.x)
I = np.array(data.y)
sI = np.array(data.e)
Im = np.array(data.m)

dof = len(q) - len(dataRef.params)
chi2 = sum (((np.log(I) - np.log(Im))**2))
R = sum(np.abs(np.abs(I) - np.abs(Im))) / sum(np.abs(I))
print(R)