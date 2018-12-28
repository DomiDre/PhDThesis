import numpy as np

data = np.genfromtxt('./LayerThickness.csv')
l = data[:, -1]
d_pmma = l[:8]
d_np = l[8:]

print(f"PMMA: {np.mean(d_pmma)} +/- {np.std(d_pmma, ddof=1)}")
print(f"NP: {np.mean(d_np)} +/- {np.std(d_np, ddof=1)}")