from modelexp.data import PrfData, XyData
import numpy as np

import sys, os
import matplotlib
import matplotlib.pyplot as plt
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
plt.style.use('phdthesis')

datfile = 'PMK18.dat'
prfFile = cwd + '/spinellPhase/fe2o3.prf'

chapter = 'looselyPackedNP'
sample_name = 'IOS-11'

savefile = chapter + '_XRD_Fe2O3' + sample_name

wavelength = 1.5406

# matplotlib.rcParams.update({'font.size': 18})
fig = plt.figure()
left, bottom = 0.19, 0.17
min_q, max_q = 1.1, 4.9
min_I, max_I = 0, 1.4
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

# left, bottom = 0.17, 0.15
# ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

data = XyData()
data.loadFromFile(datfile)
tth, Idata = data.getData()
qdata = 4*np.pi/wavelength *np.sin(tth/2 *np.pi/180)

data = PrfData()
data.loadFromFile(prfFile)
bg = data.getBackground()

tth, Iobs, Imodel = data.getData()
toQ = lambda x: 4*np.pi/wavelength *np.sin(x/2 *np.pi/180)
q = toQ(tth)

sf = max(Idata[np.logical_and(qdata>2, qdata<3)])
Imodel /= sf
Iobs /= sf
Idata /= sf
bg /= sf
ax.plot(qdata, Idata, ls='None', marker='.', markersize=1, label='Observed')
ax.plot(q, Imodel, color='black', marker='None', zorder=10, alpha=0.5, label='Calculated')
ax.plot(q, bg, marker='None', zorder=10, alpha=0.5, label='Background')
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
ax.text(0.02, 0.98, 'IOS-11',
  transform=ax.transAxes,
  verticalAlignment='top',
  horizontalAlignment='left')
legend = ax.legend(loc='upper right', fontsize=10)
legend.legendHandles[0]._legmarker.set_markersize(10)
legend.legendHandles[3]._legmarker.set_markersize(10)

plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)