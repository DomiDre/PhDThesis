import numpy as np
q_min_pos = [0.552287, 0.428388, 0.308654, 0.18892]

p = np.polyfit(np.arange(len(q_min_pos)), q_min_pos, 1)
print(2*np.pi/p[0])
