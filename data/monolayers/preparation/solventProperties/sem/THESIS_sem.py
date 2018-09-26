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


def plot_tiffile(semFilepath, sample_name):
  chapter = 'monolayers'
  savefile = chapter + '_SEM_' + sample_name

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  # semFFT.plot_sem_image()
  # semFFT.show()
  semFFT.pretty_plot(200, 100, 736, 624, 100, sample_name)
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')
  semFFT.fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')

plot_tiffile(cwd+"/DD192_Hep_1_2_control_08.tif", 'ML-SV-HepOct')
plot_tiffile(cwd+"/DD192_Hex1_2_10.tif", 'ML-SV-HexOct')
plot_tiffile(cwd+"/DD192_Hex2_2_03.tif", 'ML-SV-HexTet')
plot_tiffile(cwd+"/DD192_Pen2_2_109.tif", 'ML-SV-PenOct')
