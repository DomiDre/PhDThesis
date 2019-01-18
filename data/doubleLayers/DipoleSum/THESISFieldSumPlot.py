import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import lmfit

chapter = 'doublelayers'
savefile = chapter + '_simulatedFieldStrenghs'

sumdata = np.genfromtxt('./field_sums.xy')
z = sumdata[:, 0]
f = sumdata[:, 1]
muB = 9.274009994e-24
mu0 = 4*np.pi*1e-7
mu = 23e3 * muB
a = 13e-9
prefac = mu * mu0 / 4/np.pi/a**3 * 1e3 # in mT

z = z#*a*1e9
Bx = prefac*f

x0, y0 = 0.23, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()

c_lin = np.linspace(0, 10, 100)
ax = fig.add_axes([x0, y0, width, height])
ax.plot(z, Bx, ls='-', marker='None', zorder=1)
ax.set_xlim(0, 2.5)
ax.set_ylim(-39, 1)
ax.set_xlabel(r'$\mathit{\tilde{z}} \, / \, a$')
ax.set_ylabel('$\mathit{B}_x \, / \, mT$')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
