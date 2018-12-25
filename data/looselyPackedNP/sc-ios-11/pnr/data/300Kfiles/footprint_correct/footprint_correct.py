import footprintCorrect
import os, glob

sample_width = 14
beam_width = 0.5
datafiles = sorted(glob.glob('../reducedData/*uu.xy'))

for file in datafiles:
  app = footprintCorrect.App()
  app.qmin = 0.0038
  app.set_wavelength(5.1386)
  app.load_xye(file)
  if len(app.q) > 0:
    app.footprint_correct_and_rescale(sample_width, beam_width, q_plateau_min=0.0066, q_plateau_max=0.0092)
    app.save('./'+file.rsplit('/', 1)[-1].replace('.xy', '_fcorrected.xye'))

  app.load_xye(file.replace('uu.xy', 'du.xy'))
  if len(app.q) > 0:
    app.footprint_correct_and_rescale(sample_width, beam_width, q_plateau_min=0.0066, q_plateau_max=0.0092)
    app.save('./'+file.rsplit('/', 1)[-1].replace('uu.xy', 'du_fcorrected.xye'))
