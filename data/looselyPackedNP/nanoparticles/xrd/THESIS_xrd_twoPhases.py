from modelexp.data import PrfData, XyData
import numpy as np

import sys, os
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
plt.style.use('phdthesis')

datfile = 'PMK18.dat'
prfFile = cwd + '/spinellAndWustite/fe2o3_feo.prf'
outFile = cwd + '/spinellAndWustite/fe2o3_feo.out'

chapter = 'looselyPackedNP'
sample_name = 'IOS-11'

savefile = chapter + '_XRD_Fe2O3WustiteFit_' + sample_name

wavelength = 1.5406

def readOutFile():
  reflexes = {}
  patternName = ''
  with open(outFile, 'r') as f:
    readReflexes = False
    for line in f:
      if readReflexes:
        if '--------------' in line:
          readReflexes = False
          continue
        split_line = line.split()
        if len(split_line) > 0:
          reflexes[patternName]['h'].append(int(split_line[2]))
          reflexes[patternName]['k'].append(int(split_line[3]))
          reflexes[patternName]['l'].append(int(split_line[4]))
          reflexes[patternName]['tth'].append(float(split_line[7]))
          reflexes[patternName]['Icalc'].append(float(split_line[8]))
          reflexes[patternName]['Iobs'].append(float(split_line[9]))

      if 'Pattern#' in line and "Phase No." in line:
        readReflexes = True
        patternName = line.split()[-1]
        reflexes[patternName] = {
          'h': [],
          'k': [],
          'l': [],
          'tth': [],
          'Icalc': [],
          'Iobs': []
        }
        for i in range(4):
          f.readline()
  return reflexes

fit_reflexes = readOutFile()
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

for i, tth_reflex in enumerate(fit_reflexes['Fe2O3']['tth']):
  qReflex = toQ(tth_reflex)
  closestIobs = Imodel[data.getClosestIdx(tth, tth_reflex)] #fit_reflexes['CoFe2O4']['Iobs'][i] #
  ax.plot(
    [qReflex, qReflex], [0.15, closestIobs],
    marker='None', ls='-', color='green', lw=0.5, alpha=0.5
  )
for i, tth_reflex in enumerate(fit_reflexes['FeO']['tth']):
  qReflex = toQ(tth_reflex)
  closestIobs = Imodel[data.getClosestIdx(tth, tth_reflex)] #fit_reflexes['CoFe2O4']['Iobs'][i] #
  ax.plot(
    [qReflex, qReflex], [0.15, closestIobs],
    marker='None', ls='-', color='red', lw=0.5, alpha=0.5
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

# handles, labels = ax.get_legend_handles_labels()
green_patch = Line2D([0], [0], color='green', lw=1, marker='None')
red_patch = Line2D([0], [0], color='red', lw=1, marker='None')
ax.legend([green_patch, red_patch], ['Inv. Spinell', 'Wüstite'], loc='upper left', fontsize=10, bbox_to_anchor=(0, 0.9))
plt.gca().add_artist(legend)


plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)