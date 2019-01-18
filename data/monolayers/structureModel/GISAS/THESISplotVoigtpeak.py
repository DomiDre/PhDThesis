import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import lmfit
import datetime as dt

from GALAXI.dd_gisaxs.dd_gisaxs import DDGISAXS
import matplotlib.colors as mcolors
import matplotlib.patheffects as PathEffects
from mpl_toolkits.axes_grid1 import make_axes_locatable
from scipy.special import wofz

default_sdd = 1733.5
default_beamcenter = (610.41, 338.41)

qz_min = 0.24
qz_max = 0.3
vmin = 0.5
vmax = 1e3
ymin, ymax = 2e0, 2e4
chapter = 'monolayers'

def plot_q_square_lines(q10, ax):
  ymin = 0.1
  ymax = 0.2

  # rest position of peaks
  qsquare = lambda h,k: q10 * np.sqrt(h**2 + k**2)
  q11 = qsquare(1,1)
  q20 = qsquare(2,0)
  q21 = qsquare(2,1)
  q22 = qsquare(2,2)
  q30 = qsquare(3,0)
  q31 = qsquare(3,1)
  q32 = qsquare(3,2)
  q33 = qsquare(3,3)

  ax.axvline(q10, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q11, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q20, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q21, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q22, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q30, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q31, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q32, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(q33, color='black', ymin=ymin, ymax=ymax, marker='None')

  ax.axvline(-q10, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q11, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q20, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q21, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q22, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q30, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q31, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q32, color='black', ymin=ymin, ymax=ymax, marker='None')
  ax.axvline(-q33, color='black', ymin=ymin, ymax=ymax, marker='None')

def lorentzian(x, p):
  A = p['A'].value
  mu = p['mu'].value
  sig = p['sig'].value
  c = p['c'].value
  return A * 1./( 4*((x-mu)/sig)**2 + 1 ) + c

def fadeeva(x, p):
  A = p['A'].value
  mu = p['mu'].value
  sigG = p['sigG'].value
  sigL = p['sigL'].value
  c = p['c'].value
  z = ((x - mu) + 1j*sigL/2)/(sigG*np.sqrt(2))
  return A*wofz(z).real / (sigG*np.sqrt(2*np.pi)) + c

def fit_peak(f, Ainit, muinit, siginit, cinit, q, I, sI, vary_A=True, vary_mu=True, vary_sig=True, vary_c=False):
  def residuum(p, q, I, sI):
    return (I - fadeeva(q, p))/sI
  dq = 0.03
  sig_beam_width = 0.0195 # nm-1
  error_sig_beam_width = 0.0007 # nm-1

  p = lmfit.Parameters()
  p.add('A', Ainit, min=0, vary=vary_A)
  p.add('mu', muinit, vary=vary_mu)
  p.add('sigL', siginit, min=0, vary=vary_sig)
  p.add('sigG', 0.0084, min=0, vary=False)
  p.add('c', cinit, min=0, vary=vary_c)
  fit_range = np.logical_and(muinit-dq < q, q < muinit+dq)
  fit_result = lmfit.minimize(residuum,\
            p, args=(q[fit_range], I[fit_range], sI[fit_range]))
  p_result = fit_result.params
  print(lmfit.fit_report(fit_result))
  f.write(lmfit.fit_report(fit_result)+'\n')
  aLattice = 2*np.pi/p_result['mu'].value
  error_aLattice = aLattice * p_result['mu'].stderr/p_result['mu'].value
  f.write(f"a = {aLattice} +/- {error_aLattice}\n")

  d_coh = 4*np.pi**2 / p_result['sigL'].value
  error_d_coh = d_coh  * p_result['sigL'].stderr/ p_result['sigL'].value
  f.write(f"d_coh = {d_coh} +/- {error_d_coh}\n")
  return p_result

def plot_gisas(filepath, sample_name, f, A10, q10, dq10, c10):
  savefile = chapter + '_GISAXS_' + sample_name
  obj = DDGISAXS()
  obj.set_sdd(default_sdd)
  obj.set_beamcenter(default_beamcenter[0], default_beamcenter[1])
  obj.load_h5(filepath)
  qy, qz = obj.get_qyqz()
  qy *= 10 #transform to nm-1
  qz *= 10 #transform to nm-1

  data = obj.get_data()
  qyslice, I_qyslice, sI_qyslice = obj.get_qy_slice(qz_min, qz_max)
  if dq10 is not None:
    f.write(f'#Fitting {filepath}\n')
    p_lorentzian = fit_peak(f, A10, q10, dq10, c10, qyslice, I_qyslice, sI_qyslice)

  x0, y0 = 0.13, 0.17
  width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
  fig = plt.figure()

  ax = fig.add_axes([x0, 0.42, width, 0.57])
  ax2 = fig.add_axes([x0, y0, width, 0.25])

  pcm = ax.pcolormesh(qy, qz, data.T,\
                      norm=mcolors.LogNorm(),\
                      cmap=obj.cmap, vmin=vmin, vmax=vmax)
  ax.axhline(qz_min, color='white', marker='None', alpha=0.5)
  ax.axhline(qz_max, color='white', marker='None', alpha=0.5)
  # divider3 = make_axes_locatable(ax)
  # cax = divider3.append_axes('right', size="2.5%", pad=0.1)
  # cbar = fig.colorbar(pcm, cax=cax, orientation='vertical')
  ax.set_xticks([])
  ax.set_yticks([0, 1])
  ax2.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
  ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')

  txt = ax.text(0.95, 0.95,\
          sample_name,\
          color='white',\
          horizontalalignment='right',
          verticalalignment='top',\
          transform=ax.transAxes)
  # txt.set_path_effects([PathEffects.withStroke(linewidth=2, foreground='black')])

  plot_q_square_lines(q10, ax2)
  data_left = qyslice<-0.06
  data_right = qyslice>0.06
  ax2.errorbar(
    qyslice[data_left], I_qyslice[data_left], sI_qyslice[data_left],
    linestyle='None', marker='.', capsize=0, elinewidth=1, color='#ca0020'
  )
  ax2.errorbar(
    qyslice[data_right], I_qyslice[data_right], sI_qyslice[data_right],
    linestyle='None', marker='.', capsize=0, elinewidth=1, color='#ca0020'
  )
  if dq10 is not None:
    plot_width = 0.5
    plot_lorentzian = np.logical_and(p_lorentzian['mu'].value-plot_width < qyslice, qyslice < p_lorentzian['mu'].value+plot_width)
    ax2.plot(
      qyslice[plot_lorentzian], fadeeva(qyslice[plot_lorentzian], p_lorentzian),
      linestyle='-', marker='None', color='black', zorder=10, alpha=0.5
    )
  ax2.set_yscale('log')
  ax2.get_yaxis().set_visible(False)
  plt.setp(ax.get_xticklabels(), visible=False)
  # ax.set_xlim(-1.1,1.6)
  # ax2.set_xlim(-1.1,1.6)
  # ax.set_ylim(0, 1.5)
  ax.set_xlim(-2.7,1.6)
  ax2.set_xlim(-2.7,1.6)
  ax.set_ylim(0, 2.4)
  ax2.set_ylim([ymin, ymax])
  ax.set_aspect('equal')
  fig.savefig(cwd + '/' + savefile)
  fig.savefig(thesisimgs+'/'+savefile)

with open('peak_fit_parameters', 'w') as f:
  f.write('#Fitting first order peak of GISAXS data\n')
  f.write(f'#Date of execution: {dt.datetime.now()}\n')
  plot_gisas(cwd+"/GISAXS/DD175_28.h5", 'ML-Ac-CoFe-C-2', f, 3e2, 0.4726, 0.01, 2e-7)