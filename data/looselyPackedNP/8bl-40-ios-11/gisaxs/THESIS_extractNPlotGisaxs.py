import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import lmfit
import fabio
import datetime as dt

from GALAXI.dd_gisaxs.dd_gisaxs import DDGISAXS
import matplotlib.colors as mcolors
import matplotlib.patheffects as PathEffects
from mpl_toolkits.axes_grid1 import make_axes_locatable

wavelength = 1.033202
pixelsize = 0.172 #mm
sdd = 2907.08 #mm
beam_center_y = 324.5
beam_center_z = 62.09

qz_width = 0.02
qz_min = 0.39 - qz_width/2
qz_max = 0.39 + qz_width/2
vmin = 1e1 #1e-8
vmax = 5e4 #1.5e-5
chapter = 'looselyPackedNP'
sample_name = '8BL-40-IOS-11'
tiffile = cwd + "/rawdata/ES-S13_pos02_.tif"
savefile = chapter + '_GISAXS_' + sample_name


obj = DDGISAXS()
data_file = fabio.open(tiffile)
header = data_file.header
data = data_file.data
y = np.arange(data.shape[0])
z = np.arange(data.shape[1])

k0 = 2*np.pi/wavelength
tth = np.arctan((y-beam_center_y)*pixelsize/sdd/2)
aiplusaf = np.arctan((z-beam_center_z)*pixelsize/sdd/2)
qy = 2*k0*np.sin(tth)
qz = 2*k0*np.sin(aiplusaf)

qy *= 10 #transform to nm-1
qz *= 10 #transform to nm-1

yoneda_data = []
qz_range = np.logical_and(qz> qz_min, qz<qz_max)
yoneda_data = np.sum(data[:, qz_range], axis=1)
print(np.sum(qz_range))
background_line = np.sum(data[:, -1*np.sum(qz_range):], axis=1)
bg_est = np.mean(background_line)
sbg_est = np.std(background_line, ddof=1)

headerstring = f"Extracted data from {tiffile}\n"+\
               f"Projected data from qz = {qz_min} .. {qz_max}\n"+\
               f"Background estimate: {bg_est} +/- {sbg_est}\n"+\
               f"q_y / A-1 \t I / Counts"
valid_data = yoneda_data > 0
qy_save = qy[valid_data]
yoneda_save = yoneda_data[valid_data]
np.savetxt(f"{sample_name}_Yoneda.xye",\
    np.c_[qy_save/10, yoneda_save, np.sqrt(yoneda_save)],\
    header=headerstring)

x0, y0 = 0.13, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()
ax = fig.add_axes([x0, y0, width, height])

pcm = ax.pcolormesh(qy, qz, data.T,\
                    norm=mcolors.LogNorm(),\
                    cmap=obj.cmap, vmin=vmin, vmax=vmax)
ax.axhline(qz_min, color='white', marker='None', alpha=0.5)
ax.axhline(qz_max, color='white', marker='None', alpha=0.5)

ax.set_yticks([0, 1])
ax.set_xlabel('$\mathit{q_y} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{q_z} \, / \, nm^{-1}$')

txt = ax.text(0.95, 0.95,\
        sample_name,\
        color='white',\
        horizontalalignment='right',
        verticalalignment='top',\
        transform=ax.transAxes)

ax.set_xlim(-1.1,2.2)
ax.set_ylim(-0.2, 2.8)
ax.set_aspect('equal')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)

# def plot_q_square_lines(q10, ax):
#   ymin = 0.1
#   ymax = 0.2

#   # rest position of peaks
#   qsquare = lambda h,k: q10 * np.sqrt(h**2 + k**2)
#   q11 = qsquare(1,1)
#   q20 = qsquare(2,0)
#   q21 = qsquare(2,1)
#   q22 = qsquare(2,2)
#   q30 = qsquare(3,0)
#   q31 = qsquare(3,1)
#   q32 = qsquare(3,2)
#   q33 = qsquare(3,3)

#   ax.axvline(q10, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(q11, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(q20, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(q21, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(q22, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(q30, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(q31, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(q32, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(q33, color='black', ymin=ymin, ymax=ymax, marker='None')

#   ax.axvline(-q10, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(-q11, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(-q20, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(-q21, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(-q22, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(-q30, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(-q31, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(-q32, color='black', ymin=ymin, ymax=ymax, marker='None')
#   ax.axvline(-q33, color='black', ymin=ymin, ymax=ymax, marker='None')

# def lorentzian(x, p):
#   A = p['A'].value
#   mu = p['mu'].value
#   sig = p['sig'].value
#   c = p['c'].value
#   return A * 1./( 4*((x-mu)/sig)**2 + 1 ) + c

# def fit_peak(f, Ainit, muinit, siginit, cinit, q, I, sI, vary_A=True, vary_mu=True, vary_sig=True, vary_c=False):
#   def residuum(p, q, I, sI):
#     return (I - lorentzian(q, p))/sI
#   dq = 0.03
#   sig_beam_width = 0.0195 # nm-1
#   error_sig_beam_width = 0.0007 # nm-1

#   p = lmfit.Parameters()
#   p.add('A', Ainit, min=0, vary=vary_A)
#   p.add('mu', muinit, vary=vary_mu)
#   p.add('sig', siginit, min=0, vary=vary_sig)
#   p.add('c', cinit, min=0, vary=vary_c)
#   print(p)
#   fit_range = np.logical_and(muinit-dq < q, q < muinit+dq)
#   fit_result = lmfit.minimize(residuum,\
#             p, args=(q[fit_range], I[fit_range], sI[fit_range]))
#   p_result = fit_result.params
#   print(lmfit.fit_report(fit_result))
#   f.write(lmfit.fit_report(fit_result)+'\n')
#   f.write(f"a = {2*np.pi/p_result['mu'].value} +/- {2*np.pi*p_result['mu'].stderr/p_result['mu'].value**2}\n")
#   corrected_sig = np.sqrt(p_result['sig'].value**2 - sig_beam_width**2)
#   error_corrected_sig = np.sqrt(
#     (p_result['sig'].value/np.sqrt(p_result['sig'].value**2 - sig_beam_width**2) * p_result['sig'].stderr)**2 +
#     (sig_beam_width/np.sqrt(p_result['sig'].value**2 - sig_beam_width**2) * error_sig_beam_width)**2
#   )
#   f.write(f"BeamWidthCorrectedSig = {corrected_sig} +/- {error_corrected_sig}\n")
#   d_coh = 4*np.pi**2 / corrected_sig
#   error_d_coh = 4*np.pi**2 / corrected_sig**2 * error_corrected_sig
#   f.write(f"d_coh = {d_coh} +/- {error_d_coh}\n")
#   return p_result

