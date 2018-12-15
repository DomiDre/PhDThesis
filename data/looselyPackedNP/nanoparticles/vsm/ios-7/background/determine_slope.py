#Initialized ScriptFactory v0.1
#Date: 2018-03-13 14:15:05.637807
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: PPMS
#Using experiment.py from PPMS folder to generate script.
import matplotlib.pyplot as plt
import numpy as np
from PPMS.ppms import PPMS

datfiles = ['./DTOLUENE_HYS300K.DAT']
slopes = []
def get_slope(datfile):
  ppms = PPMS()
  ppms.load(datfile)
  ppms.do_diamagnetic_correction = False
  ppms.fit_diamagnetism(2, 3, show=False)
  slope = ppms.get_diamagnetic_slope()
  slopes.append(slope)

for datfile in datfiles:
  get_slope(datfile)

for i, datfile in enumerate(datfiles):
  print(f'{datfile.replace(".DAT", "")}\t{slopes[i].value}')
