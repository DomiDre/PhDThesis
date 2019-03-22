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

scalebar = 100
chapter = 'monolayers'

def plotFile(semFilepath, outfile, x0=300, vmin=None, vmax=None):
  savefile = chapter + '_SEM_' + outfile
  semFFT = SEM_FFT()
  semFFT.load_tif_file(semFilepath)
  semFFT.pretty_plot(x0, 100, 363, 312, scalebar, vmin=vmin,vmax=vmax)
  semFFT.fig.savefig(cwd + '/' + savefile, bbox_inches='tight')


plotFile('./DD192_Pen2_2_109.tif', 'pentane', 300, 100, 190)
plotFile('./DD192_Hex1_2_10.tif', 'hexane', 200, 100, 190)
plotFile('./DD192_Hep_1_2_control_08.tif', 'heptane', 0, 100, 150)