import sys, lmfit, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np

def read_file(file, mode=0):
  start_reading_lines = False
  skipped_line = False

  ai = []
  counts = []
  loadfile = open(file, "r", errors="ignore")
  for line in loadfile:
    if start_reading_lines and skipped_line:
      split_line = line.strip().split(",")
      aival = float(split_line[0])
      if mode==1:
        aival /= 2.
      countval = float(split_line[1])
      if countval <= 0.:
        continue
      ai.append(aival)
      counts.append(countval)


    elif start_reading_lines:
      skipped_line = True
      continue
    else:
      if "[Data]" in line:
        start_reading_lines = True
        continue

  ai = np.asarray(ai)
  I = np.asarray(counts)
  sI = np.sqrt(I)
  return ai, I, sI

def gaussian(p, x):
  return np.exp(-( (x - p['mu'])/p['sigma'] )**2 /2)

def residuum(p, x, y, sy, function):
  return (function(p,x) - y)/sy


chapter = 'appendix'
sample_name = 'brukerD8DirectBeam'
savefile = chapter+'_instruments_'+sample_name


ai, I, sI = read_file('DirectBeamDetectorScan.txt')
maxI = max(I)
I /= maxI
sI /= maxI

p = lmfit.Parameters()

p.add('mu', 0)
p.add('sigma', 0.05, min=0)

fit_range = np.logical_and(ai>-0.03,ai<0.03)
ai_fit = ai[fit_range]
I_fit = I[fit_range]
sI_fit = sI[fit_range]

fit_result = lmfit.minimize(residuum, p, args=(ai_fit, I_fit, sI_fit, gaussian))
print(lmfit.fit_report(fit_result))
p_fit = fit_result.params

left, bottom = 0.18, 0.16
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.errorbar(ai, I, sI, label='Direct Beam', zorder=1, ls='None')
ax.plot(ai, gaussian(p_fit, ai), color='black', marker="None",\
    label='Gaussian Fit.', zorder=2)
# ax.set_yscale('log')
ax.set_xlabel(r'$\alpha_i \, / \, ^\circ$')
ax.set_ylabel('$\mathit{I} \, / \, a.u.$')
ax.set_xlim(-0.09, 0.09)
# ax.set_ylim(1e-6, 1.2e2)
# ax.legend().draw_frame(True)
# fig.savefig('DirectBeam.png')

fig.savefig(cwd+'/'+savefile)
fig.savefig(thesisimgs+'/'+savefile)