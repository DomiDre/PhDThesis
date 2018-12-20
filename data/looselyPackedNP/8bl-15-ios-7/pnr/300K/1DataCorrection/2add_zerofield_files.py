import numpy as np
import matplotlib.pyplot as plt
import scipy.constants as sc
from numpy import sqrt, log, exp, cos, sin, tan, mean, std


def load_data(datafile):
    rawdata = np.loadtxt(datafile)
    x = rawdata[:,0]
    y = rawdata[:,1]
    sy = rawdata[:,2]
    return x, y, sy
    
plus_file = "ES_S15_300K_7Oe_virgin_tranformed_angs_uu_masked_qz_I_corrected.xy"
minus_file = "ES_S15_300K_7Oe_virgin_tranformed_angs_du_masked_qz_I_corrected.xy"
save_to = "ES_S15_300K_7Oe_virgin_tranformed_angs_masked_qz_I_corrected_combined.xy"
x_plus, y_plus, sy_plus = load_data(plus_file)
x_minus, y_minus, sy_minus = load_data(minus_file)

x = []
y = []
sy = []
for ix, xp in enumerate(x_plus):
    yp, syp = y_plus[ix], sy_plus[ix]
    xm, ym, sym = x_minus[ix], y_minus[ix], sy_minus[ix]
    
    if xm != xp:
        print(str(xm) + " and " + str(xp) + " are not equal.")
    x.append(xp)
    y.append((yp + ym) / 2.)
    sy.append(np.sqrt(syp**2 + sym**2) / 2.)

x = np.asarray(x)
y = np.asarray(y)
sy = np.asarray(sy)

savefile = open(save_to, "w")
savefile.write("#Generated data by combining files:\n")
savefile.write("#"+plus_file+"\n")
savefile.write("#"+minus_file+"\n")
savefile.write("#q/A-1\tI/a.u.\tsI /a.u.\n")

for ix, xval in enumerate(x):
    savefile.write(str(xval) + "\t" + str(y[ix]) + "\t" + str(sy[ix]) + "\n")
savefile.close()
print("Saved combined data to " + save_to)

fig, ax = plt.subplots()
ax.errorbar(x_plus, y_plus, sy_plus, color='blue')
ax.errorbar(x_minus, y_minus, sy_minus, color='red')
ax.errorbar(x, y, sy, color='black')
ax.set_xlabel("$ \mathit{q} \, / \, \AA^{-1}$")
ax.set_ylabel("$ \mathit{I} \, / \, a.u. $")
ax.set_yscale('log')
ax.set_xlim(min(x), max(x))
ax.set_ylim(min(y)*0.8, max(y)*1.2)
fig.tight_layout()
plt.savefig(save_to.rsplit(".",1)[0]+".png")
plt.show()
