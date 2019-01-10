import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import lmfit

chapter = 'doublelayers'
savefile = chapter + '_SEM_Thickness'

def openResults(results):
  lengths = []
  with open(results, 'r') as f:
    next(f)
    for line in f:
      split_line = line.strip().split(',')
      lengths.append(float(split_line[-1]))
  return np.array(lengths)

def get_mean_std(lengths):
  mean = np.mean(lengths)
  std= np.std(lengths, ddof=1)
  return mean, std

def treat_file(file, L_list, sL_list):
  L = openResults(file)
  mean, std = get_mean_std(L)
  L_list.append(mean)
  sL_list.append(std)

def linear(p, x):
  return p['m']*x + p['b']

def residuum(p, x,y,sy):
  return (y - (p['m']*x + p['b']))/sy

p = lmfit.Parameters()
p.add('m', 1)
p.add('b', 0)


c = [0.125, 0.25, 1.25, 2.5, 5]
L = []
sL = []
treat_file('./dl_0-125/sem/Results.csv', L, sL)
treat_file('./dl_0-25/sem/Results.csv', L, sL)
treat_file('./dl_1-25/sem/Results.csv', L, sL)
treat_file('./dl_2-5/sem/Results.csv', L, sL)
treat_file('./dl_5/sem/Results.csv', L, sL)
c = np.array(c)
L = np.array(L)
sL = np.array(sL)
print(L, sL)

fit_params = lmfit.minimize(residuum, p, args=(c, L, sL))
print(lmfit.fit_report(fit_params))
p_result = fit_params.params

x0, y0 = 0.18, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()

a = 9.38
c_lin = np.linspace(0, 10, 100)
ax = fig.add_axes([x0, y0, width, height])
ax.errorbar(c, L, sL, ls='None', zorder=1)
ax.plot([0,0.5], [2*a, 2*a], marker='None', color='black', ls='-')
ax.plot(c_lin, linear(p_result, c_lin), ls='-', marker='None', zorder=0)
# ax.text(0.05, 0.1, '2a', transform=data)
ax.set_xlim(0, 5.2)
ax.set_ylim(0, 350)
ax.set_xlabel('$\mathit{c}_V^\mathrm{PMMA} \, / \, \%$')
ax.set_ylabel('$\mathit{d}_\mathrm{sample} \, / \, nm$')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)
