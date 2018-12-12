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


def plot_tiffile(semFilepath, sample_name, sample_label, x0=None, y0=None, y1=None, im_x0=200, im_y0=100):
  chapter = 'monolayers'
  savefile = chapter + '_SEM_' + sample_name

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  semFFT.pretty_plot(im_x0, im_y0, 368, 312, 100, sample_label, x0, y0, y1)
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')
  semFFT.fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')

plot_tiffile(cwd+"/DD212_4_06.tif", 'ML-OA-0', 'ML-OA-0', 0.72, 0.89, 0.96, 400, 400)
plot_tiffile(cwd+"/DD212_5_05.tif", 'ML-OA-5e-6', 'ML-OA-5$\cdot10^{-6}$', 0.6, 0.9, 0.96, 200, 100)
plot_tiffile(cwd+"/DD212_6_06.tif", 'ML-OA-1e-5', 'ML-OA-1$\cdot10^{-5}$', 0.6, 0.9, 0.96, 200, 100)
plot_tiffile(cwd+"/DD212_7_03.tif", 'ML-OA-5e-5', 'ML-OA-5$\cdot10^{-5}$', 0.6, 0.9, 0.96, 200, 100)
plot_tiffile(cwd+"/DD212_8_04.tif", 'ML-OA-1e-4', 'ML-OA-1$\cdot10^{-4}$', 0.6, 0.9, 0.96, 200, 100)