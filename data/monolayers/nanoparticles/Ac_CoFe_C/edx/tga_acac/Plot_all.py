import numpy as np
import matplotlib.pyplot as plt
import glob2, sys
from scipy import optimize
from numpy import diff
import scipy.signal
from scipy.interpolate import splrep, splev, UnivariateSpline


def load_data(datafile, m_init):
  data = open(datafile, "r", errors='ignore')
  x = []
  y = []
  for _ in range(35):
    next(data)
  for line in data:
    if line.startswith('#'):
      continue
    if line.startswith('2)'):
      continue
    if line.startswith('3)'):
      continue
    strip_line = line.split()
    if len(strip_line) < 5:
      continue
    try:
      float(strip_line[0])
    except ValueError:
      continue
    x.append(float(strip_line[4])) # Sample Temperature
    w_sample = float(strip_line[1])#sample_weight
    w_baseline = float(strip_line[2])
    y.append((w_sample - w_baseline)/m_init)
  data.close()
  return np.asarray(x), np.asarray(y)

x_FeAcac, y_FeAcac = load_data("feacac.txt", 5.018)
x_CoAcac, y_CoAcac = load_data("coacac.txt", 5.815)
x_FeOleate, y_FeOleate = load_data("Fe_Oleate.txt", 5.018)
x_CoOleate, y_CoOleate = load_data("Co_Oleate.txt", 5.815)

fig, ax = plt.subplots()
ax.plot(x_FeAcac, y_FeAcac, label="Fe-Oleate")
ax.plot(x_CoAcac, y_CoAcac, label="Co-Oleate")
ax.plot(x_FeOleate, y_FeOleate, label="Fe-AcAc")
ax.plot(x_CoOleate, y_CoOleate, label="Co-AcAc")

ax.set_xlabel("$\mathit{T} \, / \, \mathrm{^\circ C}$")
ax.set_ylabel("$ \mathit{(m_{sample} - m_{base})} \, / \, \mathit{m_0}$")
ax.set_xlim(100, 450)
ax.axvline(319, color='r', lw=3)
ax.text(290,0.8, "Reflux")
plt.legend()
fig.tight_layout()
plt.grid()
plt.savefig("Oleate_TGA.png")
plt.show()



