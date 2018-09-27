import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from GALAXI.dd_gisaxs.dd_gisaxs import DDGISAXS

from utils import load_xye, gaussian, residuum, residuum_no_error, get_power
import lmfit
import matplotlib.pyplot as plt

savefile = 'appendix_instruments_GALAXIDirectBeam'

q, I, sI = load_xye('DirectBeam_Projection_qy.xye')

q_cutoff = 0.005
data_range = np.logical_and(-q_cutoff < q, q<q_cutoff)

q = q[data_range]
I = I[data_range]
sI = sI[data_range]
q *= 10

maxI = max(I)
I /= maxI
sI /= maxI

p = lmfit.Parameters()
p.add('A', 1, min=0, vary=False)
p.add('mu', 0, vary=True)
p.add('sig', 0.008, min=0)
p.add('c', 00, min=0, vary=False)

fit_result = lmfit.minimize(residuum_no_error, p, args=(q, I, sI, gaussian))
print(lmfit.fit_report(fit_result))
p_result = fit_result.params

q_plot = np.linspace(min(q), max(q), 200)

left, bottom = 0.17, 0.17
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.errorbar(q, I, sI, ls='None', marker='.', label='Direct Beam')
pow_mu, stdmu, form_mu = get_power(p_result['mu'].stderr)
pow_sig, stdsig, form_sig = get_power(p_result['sig'].stderr)
ax.plot(q_plot, gaussian(q_plot, p_result), marker='None',\
        label='$\mu\,=\,'+form_mu.format(p_result['mu'].value)+'('+stdmu+')'+'\,nm^{-1}$\n'+\
              '$\sigma\,=\,'+form_sig.format(p_result['sig'].value)+'('+stdsig+')'+'\,nm^{-1}$')
            #   r'$\exp (-\frac{1}{2}(\frac{x-\mu}{\sigma})^2)$'+'\n'+\
            #   '$A\,=\,'+str(p_result['A'].value)+'$\n'+\
# ax.set_yscale('log')
handles, labels = ax.get_legend_handles_labels()

ax.legend(handles[::-1], labels[::-1], loc='upper left')
ax.set_xlabel('$\mathit{q} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{I} \, / \, a.u.$')
ax.set_xlim(-0.032, 0.032)
ax.set_ylim(0, 1.7)
fig.tight_layout()

fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
plt.show()