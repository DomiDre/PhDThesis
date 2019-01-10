import numpy as np
import matplotlib.pyplot as plt

import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')
from PlottingTemplates.saxssanssanspol import color_variant
import lmfit

chapter = 'doubleLayers'
savefile = chapter+'_XRR_MinimaPositions'


data = np.genfromtxt('./minimaPosition.xy')
idx = data[:, 0]
q = data[:, 1]

idx_0_25 = idx[:2]
q_0_25 = q[:2]*10

idx_1_25 = idx[2:6]
q_1_25 = q[2:6]*10

idx_2_5 = idx[6:]
q_2_5 = q[6:]*10

def linear(p, x):
  return p['m']*x + p['n']

def residuum(p, x, y):
  return (y - (p['m']*x + p['n']))

p_0_25 = lmfit.Parameters()
p_0_25.add('m', 0.01)
p_0_25.add('n', 0)
p_1_25 = lmfit.Parameters()
p_1_25.add('m', 0.01)
p_1_25.add('n', 0)
p_2_5 = lmfit.Parameters()
p_2_5.add('m', 0.01)
p_2_5.add('n', 0)

fit_result_0_25 = lmfit.minimize(residuum, p_0_25, args=(idx_0_25, q_0_25))
fit_result_1_25 = lmfit.minimize(residuum, p_1_25, args=(idx_1_25, q_1_25))
fit_result_2_5  = lmfit.minimize(residuum, p_2_5, args=(idx_2_5, q_2_5))

p_0_25 = fit_result_0_25.params
p_1_25 = fit_result_1_25.params
p_2_5 = fit_result_2_5.params

# p_0_25 = np.polyfit(idx_0_25, q_0_25, 1)
# p_1_25 = np.polyfit(idx_1_25, q_1_25, 1)
# p_2_5 = np.polyfit(idx_2_5, q_2_5, 1)

L_0_25 = 2*np.pi/p_0_25['m']
# sigL_0_25 = 2*np.pi/p_0_25['m']**2 * p_0_25['m'].stderr

L_1_25 = 2*np.pi/p_1_25['m']
sigL_1_25 = 2*np.pi/p_1_25['m']**2 * p_1_25['m'].stderr

L_2_5 = 2*np.pi/p_2_5['m']
sigL_2_5 = 2*np.pi/p_2_5['m']**2 * p_2_5['m'].stderr

L_0_25 = int(np.round(L_0_25))
# sigL_0_25 = int(np.round(sigL_0_25))
L_1_25 = int(np.round(L_1_25))
sigL_1_25 = int(np.round(sigL_1_25))
L_2_5 = int(np.round(L_2_5))
sigL_2_5 = int(np.round(sigL_2_5))

print(L_0_25)#, sigL_0_25)
print(L_1_25, sigL_1_25)
print(L_2_5, sigL_2_5)



left, bottom = 0.19, 0.17
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
lin_range = np.arange(0, 10)
# ax.plot(idx_0_25, q_0_25, color='#EE292F',marker='x', ls='None', label='DL-0.25%', zorder=1)
ax.plot(idx_1_25, q_1_25, color='#FAAB2D',marker='x', ls='None', label='DL-1.25%', zorder=1)
ax.plot(idx_2_5, q_2_5, color='#76C152',marker='x', ls='None', label='DL-2.5%', zorder=1)

ax.plot(lin_range, linear(p_1_25, lin_range), color='black', ls='-', marker='None', zorder=0)
ax.plot(lin_range, linear(p_2_5 ,lin_range) , color='black', ls='-', marker='None', zorder=0)
# ax.text(0.4, 0.23, 'XRR',
#   horizontalalignment='left',
#   verticalalignment='bottom',
#   transform=ax.transAxes
#   )
ax.text(0.4, 0.13, '$d_\mathrm{sample}$'+f' = {L_1_25}({sigL_1_25}) nm',
  horizontalalignment='left',
  verticalalignment='bottom',
  color=color_variant('#FAAB2D', -100),
  transform=ax.transAxes
  )
ax.text(0.4, 0.03, '$d_\mathrm{sample}$'+f' = {L_2_5}({sigL_2_5}) nm',
  horizontalalignment='left',
  verticalalignment='bottom',
  color=color_variant('#76C152', -100),
  transform=ax.transAxes
  )
ax.set_xlabel('$\mathit{i}$')
ax.set_ylabel('$\mathit{q} \, / \, nm^{-1}$')
ax.set_xlim(0.5, 6.5)
ax.set_ylim(0.3, 0.65)
ax.legend(loc='upper left')

fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')