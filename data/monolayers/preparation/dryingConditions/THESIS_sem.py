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


def plot_tiffile(semFilepath, sample_name, label):
  chapter = 'monolayers'
  savefile = chapter + '_SEM_' + label

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  # semFFT.plot_sem_image()
  # semFFT.show()
  semFFT.pretty_plot(200, 100, 736, 624, 100, sample_name)
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')
  semFFT.fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')

def plot_tiffile_with_arrow(semFilepath, sample_name, label):
  chapter = 'monolayers'
  savefile = chapter + '_SEM_' + label

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  # semFFT.plot_sem_image()
  # semFFT.show()
  semFFT.pretty_plot(200, 100, 736, 624, 100, sample_name)
  semFFT.ax.arrow(1400, 1200, 200, 100, color='white', width=10)
  semFFT.ax.text(1500, 1170, "$B_{dry}$", color='white')
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')
  semFFT.fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')

# plot_tiffile(cwd+"/DD202_1_05.tif", 'Before Washing')
# plot_tiffile(cwd+"/DD202_1_washed_09.tif", 'After Washing')
plot_tiffile(cwd+"/DD224_4_01.tif", 'Without Magnetic Field', 'without_mag_field')
plot_tiffile_with_arrow(cwd+"/DD224_5_Mag_03.tif", 'With Magnetic Field', 'with_mag_field')