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

im_w, im_h = 363, 312
def plot_tiffile(semFilepath, sample_name, label, x0=None, y0=None, y1=None, im_x0=200, im_y0=100, vmin=None, vmax=None):
  chapter = 'monolayers'
  savefile = chapter + '_SEM_' + label

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  semFFT.pretty_plot(im_x0, im_y0, im_w, im_h, 500, sample_name, x0, y0, y1, vmin=vmin, vmax=vmax, legendcolor='black')
  semFFT.ax.arrow(500, 1400, 250, 50, color='black', width=10)
  semFFT.ax.arrow(800, 1100, 250, -50, color='black', width=10)
  semFFT.ax.arrow(500, 500, 250, 200, color='black', width=10)
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')

def plot_tiffile_with_arrow(semFilepath, sample_name, label, x0=None, y0=None, y1=None, im_x0=200, im_y0=100, vmin=None, vmax=None):
  chapter = 'monolayers'
  savefile = chapter + '_SEM_' + label

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)

  semFFT.pretty_plot(im_x0, im_y0, im_w*2, im_h*2, 500, sample_name, x0, y0, y1, vmin=vmin, vmax=vmax,  legendcolor='black')
  semFFT.ax.arrow(700, 600, 400, 160, color='black', width=10)
  semFFT.ax.text(950, 615, "$B_{dry}$", color='black')

  semFFT.ax.add_patch(
    patches.Rectangle(
      (950, 580),   # (x,y)
      150,          # width
      105,          # height
      color='#FAFAFA',
      alpha=0.75,
      linewidth=0
    )
  )
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')

# plot_tiffile(cwd+"/DD224_4_03.tif", 'Without Magnetic Field', 'without_mag_field', 0.37, 0.89, 0.96, 0, 100, vmin=80, vmax=180)
plot_tiffile_with_arrow(cwd+"/DD224_5_Mag_03.tif", 'With Magnetic Field', 'with_mag_field', 0.45, 0.89, 0.96, vmin=50, vmax=200)