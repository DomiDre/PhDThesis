import footprintCorrect
import os, glob

# 30 K files ES-S12
sample_width = 14
datafiles = sorted(glob.glob('../gaussFits300K/*uu_masked_qz_I.xy'))

for file in datafiles:
  app = footprintCorrect.App()
  app.qmin = 0.0038
  app.set_wavelength(5.1386)
  app.load_xye(file)
  if len(app.q) > 0:
    if '300K' in file:
      beam_width = 0.5
    else:
      beam_width = 1
    app.footprint_correct_and_rescale(sample_width, beam_width, q_plateau_min=0.0066, q_plateau_max=0.0092)
    app.save('./'+file.rsplit('/', 1)[-1].replace('.xy', '_fcorrected.xye'))

  app.load_xye(file.replace('uu_masked_qz_I.xy', 'du_masked_qz_I.xy'))
  if len(app.q) > 0:
    if '300K' in file:
      beam_width = 0.5
    else:
      beam_width = 1
    app.footprint_correct_and_rescale(sample_width, beam_width, q_plateau_min=0.0066, q_plateau_max=0.0092)
    app.save('./'+file.rsplit('/', 1)[-1].replace('uu_masked_qz_I.xy', 'du_masked_qz_I_fcorrected.xye'))
