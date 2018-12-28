import numpy as np
import matplotlib.pyplot as plt

import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')
from PlottingTemplates.saxssanssanspol import color_variant
import lmfit

chapter = 'looselyPackedNP'
savefile = chapter+'_BilayersPNR_8BL-15-IOS-7_PeakPositions'


data = np.genfromtxt('./peakPosition.xy')
idx = data[:, 0]
q = data[:, 1]

idx_300K = idx[:4]
q_300K = q[:4]*10
idx_30K = idx[4:]
q_30K = q[4:]*10

def residuum(p, x, y):
  return (y - (p['m']*x + p['n']))
p_300K = lmfit.Parameters()
p_300K.add('m', 0.01)
p_300K.add('n', 0)
p_30K = lmfit.Parameters()
p_30K.add('m', 0.01)
p_30K.add('n', 0)

fit_result_300K = lmfit.minimize(residuum, p_300K, args=(idx_300K, q_300K))
fit_result_30K = lmfit.minimize(residuum, p_30K, args=(idx_30K, q_30K))

p_300K = fit_result_300K.params
p_30K = fit_result_30K.params

# p_300K = np.polyfit(idx_300K, q_300K, 1)
# p_30K = np.polyfit(idx_30K, q_30K, 1)
L_300K = 2*np.pi/p_300K['m']
sigL_300K = 2*np.pi/p_300K['m']**2 * p_300K['m'].stderr
L_30K = 2*np.pi/p_30K['m']
sigL_30K = 2*np.pi/p_30K['m']**2 * p_30K['m'].stderr
L_300K = int(np.round(L_300K))
sigL_300K = int(np.round(sigL_300K))
L_30K = int(np.round(L_30K))
sigL_30K = int(np.round(sigL_30K))

print(L_300K, sigL_300K)
print(L_30K, sigL_30K)



left, bottom = 0.19, 0.17
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
lin_range = np.arange(0, 10)
ax.plot(idx_300K, q_300K, color='#EE292F',marker='x', ls='None', label='300K', zorder=1)
ax.plot(idx_30K, q_30K, color='#0EA8DF',marker='x', ls='None', label='30K', zorder=1)
ax.plot(lin_range, p_300K['m']*lin_range + p_300K['n'], color=color_variant('#EE292F', -100),marker='None', zorder=0)
ax.plot(lin_range, p_30K['m']*lin_range + p_30K['n'], color=color_variant('#0EA8DF', -100),marker='None', zorder=0)

ax.text(0.4, 0.23, 'PNR',
  horizontalalignment='left',
  verticalalignment='bottom',
  transform=ax.transAxes
  )
ax.text(0.4, 0.13, '$L_\mathrm{period}$'+f' = {L_300K}({sigL_300K}) nm',
  horizontalalignment='left',
  verticalalignment='bottom',
  color=color_variant('#EE292F', -100),
  transform=ax.transAxes
  )
ax.text(0.4, 0.03, '$L_\mathrm{period}$'+f' = {L_30K}({sigL_30K}) nm',
  horizontalalignment='left',
  verticalalignment='bottom',
  color=color_variant('#0EA8DF', -100),
  transform=ax.transAxes
  )
ax.set_xlabel('$\mathit{i}$')
ax.set_ylabel('$\mathit{q} \, / \, nm^{-1}$')
ax.set_xlim(0.5, 8.5)
ax.set_ylim(0.0, 0.7)
ax.legend(loc='upper left')

fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
# fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')
