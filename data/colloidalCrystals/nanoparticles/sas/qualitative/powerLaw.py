#Initialized ScriptFactory v0.2
#Date: 2018-07-23
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: MODELEXP
from modelexp.data import XyeData

import datetime, lmfit
import numpy as np
import matplotlib.pyplot as plt

dataRef = XyeData()
dataRef.loadFromFile('../experimental_data/DD144.xye')
q, I, sI = dataRef.getData()

def linear(p, x):
  return p['a']*x**(p['n'].value)

def residuum(p, x, y, sy):
  return (linear(p, x) - y)/sy

p = lmfit.Parameters()
p.add('a', 0.1)
p.add('n', -1.5)

fit_range = np.logical_and(q > 1e-2, q < 0.024)
fit_result = lmfit.minimize(residuum, p, args=(q[fit_range], I[fit_range], sI[fit_range]))
print(lmfit.fit_report(fit_result))
fig, ax = plt.subplots()
ax.errorbar(q, I, sI)
ax.plot(q, linear(fit_result.params, q), ls='-', marker='None', color='black')
ax.set_xlim([1e-2,0.22])
ax.set_xscale('log')
ax.set_yscale('log')
plt.show()
# modelData = modelRef.getModelset(0)
# q = modelData.getDomain()
# I = modelData.getValues()
# with open(f'simulated_model.xy', 'w') as f:
#   f.write(f'#Superball Data generated at {datetime.datetime.now()}\n')
#   f.write(f'#[[Parameters]]\n')
#   for param in modelRef.params:
#     f.write(f'#{param}\t{modelRef.params[param].value}\n')
#   f.write(f'#\n')
#   f.write(f'#[[Data]]\n')
#   f.write(f'#q\tI\n')
#   for j in range(len(q)):
#     f.write(f'{q[j]}\t{I[j]}\n')

# r = modelData.r
# sld = modelData.sld

# with open(f'simulated_model_sld.xy', 'w') as f:
#   f.write(f'#Superball Data generated at {datetime.datetime.now()}\n')
#   f.write(f'#[[Parameters]]\n')
#   for param in modelRef.params:
#     f.write(f'#{param}\t{modelRef.params[param].value}\n')
#   f.write(f'#\n')
#   f.write(f'#[[Data]] sa\n')
#   f.write(f'#r\tsld\n')
#   for j in range(len(r)):
#     f.write(f'{r[j]}\t{sld[j]}\n')