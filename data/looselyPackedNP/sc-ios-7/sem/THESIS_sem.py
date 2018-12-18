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

semFilepath = cwd+"/ES-S17_xs_05.tif"
chapter = 'looselyPackedNP'
sample_name = 'SC-IOS-7'
savefile = chapter+'_SEM_'+sample_name

semFFT = SEM_FFT()
semFFT.load_tif_file(semFilepath)
# semFFT.plot_sem_image()
# semFFT.show()
semFFT.pretty_plot(200, 100, 736, 624, 100, 'SC-IOS-7', 0.7, 0.9)

semFFT.fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
semFFT.fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')