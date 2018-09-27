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


def plot_tiffile(semFilepath, sample_name, sample_label):
  chapter = 'monolayers'
  savefile = chapter + '_SEM_' + sample_name

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  # semFFT.plot_sem_image()
  # semFFT.show()
  semFFT.pretty_plot(200, 100, 736, 624, 100, sample_label)
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')
  semFFT.fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')

plot_tiffile(cwd+"/DD212_5_05.tif", 'ML-OA-5e-6', 'ML-OA-5$\cdot10^{-6}$')
plot_tiffile(cwd+"/DD212_6_06.tif", 'ML-OA-1e-5', 'ML-OA-1$\cdot10^{-5}$')
plot_tiffile(cwd+"/DD212_7_03.tif", 'ML-OA-5e-5', 'ML-OA-5$\cdot10^{-5}$')
plot_tiffile(cwd+"/DD212_8_04.tif", 'ML-OA-1e-4', 'ML-OA-1$\cdot10^{-4}$')