import footprintCorrect
import os, glob

# 30 K files ES-S12
sample_width = 15
datafiles = sorted(glob.glob('../boxed_data/*uu.xy'))

for file in datafiles:
  app = footprintCorrect.App()
  app.qmin = 0.0038
  app.set_wavelength(5.1836)
  app.load_xye(file)
  if len(app.q) > 0:
    if '300K' in file:
      beam_width = 0.5
    else:
      beam_width = 1
    app.footprint_correct_and_rescale(sample_width, beam_width, q_plateau_min=0.0066, q_plateau_max=0.0092)
    app.save('./'+file.rsplit('/', 1)[-1].replace('.xy', '_fcorrected.xye'))

  if '30K' in file:
    app.load_xye(file.replace('uu.xy', 'dd.xy'))
    if len(app.q) > 0:
      app.footprint_correct_and_rescale(sample_width, beam_width, q_plateau_min=0.0066, q_plateau_max=0.0092)
      app.save('./'+file.rsplit('/', 1)[-1].replace('uu.xy', 'dd_fcorrected.xye'))

  app.load_xye(file.replace('uu.xy', 'du.xy'))
  if len(app.q) > 0:
    if '300K' in file:
      beam_width = 0.5
    else:
      beam_width = 1
    app.footprint_correct_and_rescale(sample_width, beam_width, q_plateau_min=0.0066, q_plateau_max=0.0092)
    app.save('./'+file.rsplit('/', 1)[-1].replace('uu.xy', 'du_fcorrected.xye'))


# app.load_xye(file_Rminus)
# ax.errorbar(app.q, app.I, app.sI, label='R- Raw')
# app.footprint_correct_and_rescale(sample_width, beam_width, q_plateau_max=0.0113)
# ax.errorbar(app.q, app.I, app.sI, label='R- Footprint Corrected & Rescaled')
# app.save(file_Rminus.replace('.xye', '_fcorrected.xye'))

# ax.set_yscale('log')
# ax.legend()
# fig.savefig('FootprintCorrection.png')
# os.system('cp ./reduced_data/*fcorrected.xye .')
# plt.show()
