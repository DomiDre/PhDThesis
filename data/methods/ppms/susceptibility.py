import numpy as np
import matplotlib.pyplot as plt
import lmfit

class sample:
  def __init__(self, _name, _mass, _susceptibility):
    self.name = _name
    self.mass = _mass
    self.susceptibility = _susceptibility

samples = [
  sample('205.10', 27.44, -0.036),
  sample('213.7', 29.55, -0.037),
  sample('205.6', 30.27, -0.039),
  sample('205.3', 26.73, -0.034),
  sample('175.28', 28.98, -0.035),
]

def linear(p, x):
  return p['m']*x + p['b']
def residuum(p, x, y):
  return y - linear(p,x)

p = lmfit.Parameters()
p.add('m', -1)
p.add('b', 0, vary=False)

masses = []
susceptibilities = []
for sample in samples:
  masses.append(sample.mass)
  susceptibilities.append(sample.susceptibility)

masses = np.array(masses)
susceptibilities = np.array(susceptibilities)

fit_result = lmfit.minimize(residuum, p, args=(masses, susceptibilities))
p_result = fit_result.params
print(lmfit.fit_report(fit_result))

fig, ax = plt.subplots()
ax.errorbar(masses, susceptibilities, 0.001, ls='None', marker='.')
ax.plot(masses, linear(p_result, masses), color='black', marker='None', label='Fit')
ax.plot(masses, -0.00111*masses, color='blue', marker='None', label='Silicon Susc. Theo.')
ax.set_xlabel('m / mg')
ax.set_ylabel('$\chi \, / \, memu \, T^{-1}$')
ax.legend()
fig.savefig('susceptibilities.png')
