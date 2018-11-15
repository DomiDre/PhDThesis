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

def plot_tiffile(semFilepath, sample_name, outfile, scalebar=100, x0=None, y0=None):
  chapter = 'monolayers'
  savefile = chapter + '_SEM_' + outfile

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  # semFFT.plot_sem_image()
  # semFFT.show()
  semFFT.pretty_plot(200, 100, 736, 624, scalebar, sample_name, x0, y0)
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')
  semFFT.fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')

# plot_tiffile(cwd+"/DD205_4_1L_02.tif", 'ML-Ac-CoFe-C', 'ML-Ac-CoFe-C_img1', 500, 0.57, 0.9)
# plot_tiffile(cwd+"/DD205_4_1L_08.tif", 'ML-Ac-CoFe-C', 'ML-Ac-CoFe-C_img2', 100, 0.57, 0.9)
plot_tiffile(cwd+"/DD205_4xs_08.tif", 'ML-Ac-CoFe-C', 'ML-Ac-CoFe-C_img3', 500, 0.57, 0.9)
# plot_tiffile(cwd+"/DD205_4xs_06.tif", 'ML-Ac-CoFe-C', 'ML-Ac-CoFe-C_img4', 100, 0.57, 0.9)
