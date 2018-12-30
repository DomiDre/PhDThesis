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


def plot_tiffile(semFilepath, sample_name, label, x0=None, y0=None, y1=None, im_x0=200, im_y0=100, im_w=736, im_h=624):
  chapter = 'monolayers'
  savefile = chapter + '_SEM_' + label

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  # semFFT.plot_sem_image()
  # semFFT.show()
  semFFT.pretty_plot(im_x0, im_y0, im_w, im_h, 100, sample_name, x0, y0, y1)
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')
  semFFT.fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')

def plot_tiffile_with_arrow(semFilepath, sample_name, label, x0=None, y0=None, y1=None, im_x0=200, im_y0=100, im_w=736, im_h=624):
  chapter = 'monolayers'
  savefile = chapter + '_SEM_' + label

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  # semFFT.plot_sem_image()
  # semFFT.show()
  
  semFFT.pretty_plot(im_x0, im_y0, im_w, im_h, 100, sample_name, x0, y0, y1)
  semFFT.ax.arrow(1400, 1200, 200, 100, color='white', width=10)
  semFFT.ax.text(1500, 1170, "$B_{dry}$", color='white')
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')
  semFFT.fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')

# plot_tiffile(cwd+"/DD202_1_05.tif", 'Before Washing')
# plot_tiffile(cwd+"/DD202_1_washed_09.tif", 'After Washing')
# plot_tiffile(cwd+"/DD224_4_03.tif", 'Without Magnetic Field', 'without_mag_field', 0.37, 0.89, 0.96, 0, 100, 368, 312)
plot_tiffile_with_arrow(cwd+"/DD224_5_Mag_03.tif", 'With Magnetic Field', 'with_mag_field', 0.45, 0.89, 0.96)