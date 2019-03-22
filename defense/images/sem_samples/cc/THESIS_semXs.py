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

semFilepath = cwd+"/DD151_28_24.tif"
chapter = 'colloidalCrystals'
sample_name = 'CC-Fe-0_37_xs'
savefile = chapter+'_SEM_'+sample_name

semFFT = SEM_FFT()
semFFT.load_tif_file(semFilepath)
# semFFT.plot_sem_image()
# semFFT.show()
semFFT.pretty_plot(200, 100, 736, 624, 100, vmin=60, vmax=225)

semFFT.fig.savefig(cwd+'/'+savefile, bbox_inches='tight')