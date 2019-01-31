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

def plot_tiffile(semFilepath, sample_name, x0=None, y0=None, savelabel=None):
  chapter = 'monolayers'
  if savelabel is None:
    savefile = chapter + '_SEM_' + sample_name
  else:
    savefile = chapter + '_SEM_' + savelabel

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  # semFFT.plot_sem_image()
  # semFFT.show()
  semFFT.pretty_plot(200, 100, 736, 624, 100, sample_name, x0, y0)
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')
  semFFT.fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')

plot_tiffile(cwd+"/DD200_8_05.tif", 'Ol-Fe-C-ML-HepOct', 0.44, 0.9)
plot_tiffile(cwd+"/DD117_03_09.tif", 'Ol-CoFe-S-HexOct', 0.475, 0.9)