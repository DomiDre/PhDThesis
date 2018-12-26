import numpy as np
import matplotlib.pyplot as plt
# , 
q_min_pos = [0.145873, 0.223803, 0.311169]
x = np.arange(len(q_min_pos))

p = np.polyfit(x, q_min_pos, 1)
print(2*np.pi/p[0])

fig, ax =plt.subplots()
ax.plot(x, q_min_pos)
ax.plot(x, p[0]*x + p[1], marker='None', ls='-')
plt.show()