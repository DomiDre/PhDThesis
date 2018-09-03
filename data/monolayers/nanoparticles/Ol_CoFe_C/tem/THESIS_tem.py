#Initialized ScriptFactory v0.2
#Date: 2018-07-06 15:48:50.136633
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS

import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import uzkChemTem

temFilepath = cwd+"/EF2851_4.tif"
chapter = 'monolayers'
sample_name = 'Ol_CoFe_C'

savefile = chapter+'_TEM_'+sample_name

fig, ax = uzkChemTem.pretty_plot(
  temFilepath, y0=200, pixel_per_nm=2.01)
fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')
