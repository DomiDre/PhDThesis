import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from EM.sem_fft import SEM_FFT

semFilepath = cwd+"/ES-S14_side_03.tif"
chapter = 'looselyPackedNP'
sample_name = 'SC-IOS-11'
savefile = chapter+'_SEMprojection_'+sample_name

y0 = 150

Osem = SEM_FFT()
Osem.load_tif_file(semFilepath)
Osem.cut_data(0, 135, 800)
Osem.y -= y0

projected_data = np.mean(Osem.data, axis=0)

left, bottom = 0.18, 0.15
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax.plot(Osem.y, projected_data, marker='None')
Osem.annotate_point_pair(ax, "68 nm", (0, 140), (68,140), text_offset=15, x_shift=15)

ax.text(0.03, 0.03, sample_name, horizontalalignment='left', verticalalignment='bottom', transform=ax.transAxes)
ax.set_xlabel("$ \mathit{z} \, / \, nm$")
ax.set_ylabel("$ I \, / \, a.u.$")
ax.set_xlim(-30, 106)


fig.savefig(cwd+'/'+savefile)
fig.savefig(thesisimgs+'/'+savefile)