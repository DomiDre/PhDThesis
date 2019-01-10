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

semFilepath = cwd+"/DD205_3_2L_08.tif"
chapter = 'doubleLayers'
sample_name = 'DL-1_25'
label = 'DL-1.25%'
x0_label = 0.7
savefile = chapter+'_SEM_'+sample_name

semFFT = SEM_FFT()
semFFT.load_tif_file(semFilepath)
# semFFT.plot_sem_image()
# semFFT.show()
semFFT.pretty_plot(200, 100, 736, 624, 100, label, x0_label, 0.9)

semFFT.fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
semFFT.fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')