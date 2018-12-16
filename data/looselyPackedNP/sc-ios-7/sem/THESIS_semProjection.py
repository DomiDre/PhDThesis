import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from EM.sem_fft import SEM_FFT

semFilepath = cwd+"/ES-S17_xs_05.tif"
chapter = 'looselyPackedNP'
sample_name = 'ES_S17'
savefile = chapter+'_SEMprojection_'+sample_name

y0 = 213

Osem = SEM_FFT()
Osem.load_tif_file(semFilepath)
Osem.cut_data(0, 135, 800)
Osem.y -= y0

projected_data = np.mean(Osem.data, axis=0)

left, bottom = 0.18, 0.15
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax.plot(Osem.y, projected_data, marker='None')
Osem.annotate_point_pair(ax, "50 nm", (0, 200), (50,200), text_offset=15, x_shift=15)
ax.set_xlabel("$ \mathit{z} \, / \, nm$")
ax.set_ylabel("$ I \, / \, a.u.$")
ax.set_xlim(-50, 149)
ax.set_ylim(110, 249)


fig.savefig(cwd+'/'+savefile)
fig.savefig(thesisimgs+'/'+savefile)