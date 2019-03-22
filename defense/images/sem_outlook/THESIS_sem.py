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

def plot_tiffile(semFilepath, outfile, vmin, vmax, legendcolor):
  chapter = 'monolayers'
  savefile = chapter + '_SEM_' + outfile

  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  semFFT.pretty_plot(200, 100, 363, 312, 100, vmin=vmin,vmax=vmax, legendcolor=legendcolor)
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')

chapter = 'monolayers'

semFFT = SEM_FFT()
semFFT.load_tif_file(cwd+"/DD200_8_05.tif")
semFFT.pretty_plot(200, 100, 363, 312, 100, 'Iron Oxide Cubes', 0.5, 0.9, vmin=70,vmax=140, legendcolor='black')
savefile = chapter + '_SEM_' + 'Ol-Fe-C-ML-HepOct'
semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')


semFFT = SEM_FFT()
semFFT.load_tif_file(cwd+"/DD117_03_09.tif")
semFFT.pretty_plot(200, 100, 363, 312, 100, '$CoFe_2O_4$ Spheres', 0.49, 0.89, vmin=30,vmax=140, legendcolor='white')
savefile = chapter + '_SEM_' + 'Ol-CoFe-S-HexOct'
semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')
