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

        if len(split_line) != 4:
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

lafile = "AH11_nuclear_LA.dat"
x1, y1, sy1 = load_xygrasp("AH11_nuclear_SA.dat")
x2, y2, sy2 = load_xygrasp(lafile)

sf = 0.8596564519696263
y2 *= sf
sy2 *= sf


savefile = open("AH11_nuclear_LA_scaled.dat", "w")
savefile.write("#Scaled file " + lafile+"\n")
savefile.write("#Using factor: " + str(sf)+"\n")
savefile.write("#q / A-1 \t I / cm-1 \t sI / cm-1")
for ix, xval in enumerate(x2):
    savefile.write(f"{xval}\t{y2[ix]}\t{sy2[ix]}\n")

savefile.close()
fig, ax = plt.subplots()
ax.errorbar(x1, y1, sy1, ls='None', marker='.', label="SA")
ax.errorbar(x2, y2, sy2, ls='None', marker='.', label="SA")

ax.set_xlabel("$ \mathit{q} \, / \, \AA^{-1} $")
ax.set_ylabel("$ \mathit{I} \, / \, cm^{-1}$")
ax.set_xscale('log')
ax.set_yscale('log')
fig.tight_layout()
plt.show()
