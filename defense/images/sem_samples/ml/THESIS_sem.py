#Initialized ScriptFactory v0.2
#Date: 2018-07-25 11:04:23.326529
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

from EM.sem_fft import SEM_FFT
import matplotlib.patches as patches

semFilepath = cwd+"/DD175_23xs_09.tif"
sample_name = 'ML-Ac-CoFe-C-2'
outfile = 'ML-Ac-CoFe-C-2_img3'
scalebar = 100

chapter = 'monolayers'
savefile = chapter + '_SEM_' + outfile

semFFT = SEM_FFT()
semFFT.load_tif_file(semFilepath)
# semFFT.plot_sem_image()
# semFFT.show()
semFFT.pretty_plot(200, 100, 736, 624, scalebar, vmin=150,vmax=240)
semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')

