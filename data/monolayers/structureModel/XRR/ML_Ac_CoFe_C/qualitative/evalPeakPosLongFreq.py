import numpy as np
import matplotlib.pyplot as plt

import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')
from PlottingTemplates.saxssanssanspol import color_variant
import lmfit

chapter = 'monolayer'
savefile = chapter+'_XRR_MinimaPositionsLongFreq'


data = np.genfromtxt('./minimaPositionLongFreq.xy')
idx = data[:, 0]
q = data[:, 1]*10

def linear(p, x):
  return p['m']*x + p['n']

def residuum(p, x, y):
  return (y - (p['m']*x + p['n']))

p = lmfit.Parameters()
p.add('m', 0.01)
p.add('n', 0)

fit_result = lmfit.minimize(residuum, p, args=(idx, q))

p = fit_result.params
L = 2*np.pi/p['m']
sigL = 2*np.pi/p['m']**2 * p['m'].stderr

L = int(np.round(L))
sigL = int(np.round(sigL))
print(L, sigL)

left, bottom = 0.19, 0.17
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
lin_range = np.arange(0, 10)
ax.plot(idx, q, color='#EE292F',marker='x', ls='None', label='DL-0.25%', zorder=1)
ax.plot(lin_range, linear(p, lin_range), color='black', ls='-', marker='None', zorder=0)
ax.text(0.4, 0.13, '$L_\mathrm{period}$'+f' = {L}({sigL}) nm',
  horizontalalignment='left',
  verticalalignment='bottom',
  color=color_variant('#EE292F', -100),
  transform=ax.transAxes
  )

ax.set_xlabel('$\mathit{i}$')
ax.set_ylabel('$\mathit{q} \, / \, nm^{-1}$')
ax.set_xlim(0.5, 3.5)
ax.set_ylim(0.1, 1.45)
# ax.legend(loc='upper left')

fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
# fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')
