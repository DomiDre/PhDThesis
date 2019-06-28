import matplotlib.pyplot as plt
import numpy as np
from scipy.special import lpmv


def K14(x, phi):
  return 0.3046972*lpmv(0, 4, x) + 0.3641828*lpmv(4, 4, x)*np.cos(4*phi)

def K16(x, phi):
  return -0.1410474*lpmv(0, 6, x) + 0.527751*lpmv(4, 6, x)*np.cos(4*phi)


R00, R14, R16 = 22.699968, -15.959945, 13.099360

def xrd_func(x, phi):
  return R00 + R14 * K14(x, phi) + R16*K16(x, phi)

fig = plt.figure()
ax = fig.add_subplot(111, projection='polar')

phi = np.linspace(0, 2*np.pi, 360)
print(xrd_func(0.5, phi))
ax.plot(phi, xrd_func(0.9, phi))
# ax.plot(phi, xrd_func(0.2, phi))
# ax.plot(phi, xrd_func(0.3, phi))
# ax.plot(phi, xrd_func(0.4, phi))
# ax.plot(phi, xrd_func(0.5, phi))
# ax.plot(phi, xrd_func(0.6, phi))
# ax.plot(phi, xrd_func(0.7, phi))
# ax.plot(phi, xrd_func(0.8, phi))
plt.show()