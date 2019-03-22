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

chapter = 'monolayers'

semFFT = SEM_FFT()
semFFT.load_tif_file(cwd+"/DD226_2_03.tif")
semFFT.pretty_plot(250, 100, 363, 312, 100, vmin=30,vmax=210, legendcolor='white')
savefile = chapter + '_SEM_' + 'disorderedML'
semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')