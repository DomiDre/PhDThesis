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
savefile = chapter+'_BilayersXRR_PeakPositions'


data = np.genfromtxt('./peakPosition.xy')
idx = data[:, 0]
q = data[:, 1]

idx_15 = idx[:6]
q_15 = q[:6]*10
idx_40 = idx[6:]
q_40 = q[6:]*10

def residuum(p, x, y):
  return (y - (p['m']*x + p['n']))
p_15 = lmfit.Parameters()
p_15.add('m', 0.01)
p_15.add('n', 0)
p_40 = lmfit.Parameters()
p_40.add('m', 0.01)
p_40.add('n', 0)

fit_result_15 = lmfit.minimize(residuum, p_15, args=(idx_15, q_15))
fit_result_40 = lmfit.minimize(residuum, p_40, args=(idx_40, q_40))

p_15 = fit_result_15.params
p_40 = fit_result_40.params

# p_15 = np.polyfit(idx_15, q_15, 1)
# p_40 = np.polyfit(idx_40, q_40, 1)
L_15 = 2*np.pi/p_15['m']
sigL_15 = 2*np.pi/p_15['m']**2 * p_15['m'].stderr
L_40 = 2*np.pi/p_40['m']
sigL_40 = 2*np.pi/p_40['m']**2 * p_40['m'].stderr
L_15 = int(np.round(L_15))
sigL_15 = int(np.round(sigL_15))
L_40 = int(np.round(L_40))
sigL_40 = int(np.round(sigL_40))

print(L_15, sigL_15)
print(L_40, sigL_40)



left, bottom = 0.19, 0.17
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
lin_range = np.arange(0, 10)
ax.plot(idx_15, q_15, color='#EE292F',marker='x', ls='None', label='8BL-15-IOS-11', zorder=1)
ax.plot(idx_40, q_40, color='#0EA8DF',marker='x', ls='None', label='8BL-40-IOS-11', zorder=1)
ax.plot(lin_range, p_15['m']*lin_range + p_15['n'], color=color_variant('#EE292F', -100),marker='None', zorder=0)
ax.plot(lin_range, p_40['m']*lin_range + p_40['n'], color=color_variant('#0EA8DF', -100),marker='None', zorder=0)

ax.text(0.4, 0.23, 'XRR',
  horizontalalignment='left',
  verticalalignment='bottom',
  transform=ax.transAxes
  )
ax.text(0.4, 0.13, '$L_\mathrm{period}$'+f' = {L_15}({sigL_15}) nm',
  horizontalalignment='left',
  verticalalignment='bottom',
  color=color_variant('#EE292F', -100),
  transform=ax.transAxes
  )
ax.text(0.4, 0.03, '$L_\mathrm{period}$'+f' = {L_40}({sigL_40}) nm',
  horizontalalignment='left',
  verticalalignment='bottom',
  color=color_variant('#0EA8DF', -100),
  transform=ax.transAxes
  )
ax.set_xlabel('$\mathit{i}$')
ax.set_ylabel('$\mathit{q} \, / \, nm^{-1}$')
ax.set_xlim(0.5, 7.5)
ax.set_ylim(0.3, 0.9)
ax.legend(loc='upper left')

fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')
