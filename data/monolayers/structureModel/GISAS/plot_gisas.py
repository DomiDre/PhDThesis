import numpy as np
import matplotlib.pyplot as plt

def load_xy(datafile):
    rawdata = np.genfromtxt(datafile)
    x = rawdata[:, 0]
    y = rawdata[:, 1]
    return x,y


sf = 1e3
q_gisaxs, I_gisaxs = load_xy('GISAXS_DD175_28_yoneda.xy')
q_gisans_sat_plus, I_gisans_sat_plus = load_xy('GISANS_Yoneda_SatPlus.xy')
q_gisans_sat_minus, I_gisans_sat_minus = load_xy('GISANS_Yoneda_SatMinus.xy')
q_gisans_rem_plus, I_gisans_rem_plus = load_xy('GISANS_Yoneda_RemPlus.xy')
q_gisans_rem_minus, I_gisans_rem_minus = load_xy('GISANS_Yoneda_RemMinus.xy')


fig, ax = plt.subplots()
ax.plot(q_gisans_sat_plus, I_gisans_sat_plus, label='Saturation I+')
ax.plot(q_gisans_sat_minus, I_gisans_sat_minus, label='Saturation I-')
ax.plot(q_gisans_rem_plus, I_gisans_rem_plus, label='Remanence I+')
ax.plot(q_gisans_rem_minus, I_gisans_rem_minus, label='Remanence I-')
ax.plot(q_gisaxs, I_gisaxs*sf, label='GISAXS')

ax.legend(loc='best')
ax.set_yscale('log')
ax.set_xlabel("$ \mathit{q_y} \, / \, \AA^{-1}$")
ax.set_ylabel("$ \mathit{I} \, / \, a.u.$")
# ax.set_xlim(0,0.068)
# ax.set_ylim(1e-2, 2e-1)

fig.tight_layout()
fig.savefig('Gisas175_28.png')
plt.show()
