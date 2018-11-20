import numpy as np
import matplotlib.pyplot as plt

def load_xygrasp(datafile):
    data = open(datafile, "r")
    
    x = []
    y = []
    sy = []
    for line in data:
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        split_line = line.split()
        
        if len(split_line) != 3:
            continue
        
        try:
            xval = float(split_line[0])
            yval = float(split_line[1])
            syval = float(split_line[2])
        except ValueError:
            continue
        x.append(xval)
        y.append(yval)
        sy.append(syval)
    data.close()
    return np.asarray(x), np.asarray(y), np.asarray(sy)

xp, yp, syp = load_xygrasp("004184_dd117_3_rf-.dat")
xm, ym, sym = load_xygrasp("004185_dd117_3_rf+.dat")

wavelength = 6#A
xp = 4*np.pi/wavelength * np.sin(xp*np.pi/180/2.)
xm = 4*np.pi/wavelength * np.sin(xm*np.pi/180/2.)

fig, ax = plt.subplots()
ax.errorbar(xp, yp, syp, label="I+")
ax.errorbar(xm, ym, sym, label="I-")

ax.set_xlabel(r"$ \mathit{q} \, / \, A^{-1}$")
ax.set_ylabel("$ \mathit{I} \, / \, a.u. $")
ax.set_yscale('log')
plt.legend()
fig.tight_layout()
plt.show()
