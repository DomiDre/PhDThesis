from modelexp.data import PrfData, XyData
import numpy as np

import sys, os
import matplotlib
import matplotlib.pyplot as plt
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
plt.style.use('phdthesis')

datfile = 'AH11.dat'
prfFile = 'CoFe2O4.prf'

chapter = 'monolayer'
sample_name = 'Ac_CoFe_C'

savefile = chapter + '_XRD_' + sample_name

wavelength = 1.54056

# matplotlib.rcParams.update({'font.size': 18})
fig = plt.figure()
left, bottom = 0.19, 0.17
min_q, max_q = 1.9, 4.9
min_I, max_I = 0, 1.24
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

# left, bottom = 0.17, 0.15
# ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

data = XyData()
data.loadFromFile(datfile)
tth, Idata = data.getData()
qdata = 4*np.pi/wavelength *np.sin(tth/2 *np.pi/180)

data = PrfData()
data.loadFromFile(prfFile)

tth, Iobs, Imodel = data.getData()
toQ = lambda x: 4*np.pi/wavelength *np.sin(x/2 *np.pi/180)
q = toQ(tth)

sf = max(Idata[np.logical_and(qdata>2, qdata<3)])
Imodel /= sf
Iobs /= sf
Idata /= sf
ax.plot(qdata, Idata, ls='None', marker='.', markersize=1, label='Observed')
ax.plot(q, Imodel, color='black', marker='None', zorder=10, alpha=0.5, label='Calculated')
ax.plot(q, 0.1 + Imodel - Iobs, ls='None', color='black', marker='.', markersize=1, label='Difference')

for reflex in data.hkl:
  reflex_positions = data.hkl[reflex]
  for i in reflex_positions:
    tth_reflex = reflex_positions[i]
    qReflex = toQ(tth_reflex)
    closestIobs = Imodel[data.getClosestIdx(tth, tth_reflex)]
    ax.plot(
      [qReflex, qReflex], [0.15, closestIobs],
      marker='None', ls='-', color='black', lw=0.5, alpha=0.5
    )
ax.set_xlim([min_q, max_q])
ax.set_ylim([min_I, max_I])
ax.set_xlabel("$\mathit{q} \, / \, \AA^{-1}$")
ax.set_ylabel("$\mathit{I} \, / \, a.u.$")
legend = ax.legend()
legend.legendHandles[0]._legmarker.set_markersize(10)
legend.legendHandles[2]._legmarker.set_markersize(10)

plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)