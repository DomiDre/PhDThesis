import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')
import numpy as np
    # gisaxs_background:  149.704355 +/- 1.79838928 (1.20%) (init = 115.3874)
    # gisaxs_scale:       6.9518e-05 +/- 2.7618e-07 (0.40%) (init = 6.643e-05)
    # R:                  3.85388464 +/- 0.00794085 (0.21%) (init = 3.972)
    # vol_frac:           0.32408185 +/- 0.00223137 (0.69%) (init = 0.3452)
    # q_offset:           0 (fixed)

constant_saxs_background = 0
constant_gisaxs_backgorund = 149.704355
scale_gisaxs_to_saxs = 6.9518e-5
R = 3.85388464
vol_frac = 0.32408

qmin = 0.3
qsf = 4e-4

chapter = 'looselyPackedNP'
sample_name = 'SC-IOS-7'
tiffile = cwd + "/rawdata/ES-S17_pos02_.tif"
savefile = chapter + '_GISAXS_Yoneda_' + sample_name

def get_idx(array, value):
  idx_sorted = np.argsort(array)
  sorted_array = np.array(array[idx_sorted])
  idx = np.searchsorted(sorted_array, value, side="left")
  if idx >= len(array):
    idx_nearest = idx_sorted[len(array)-1]
    return idx_nearest
  elif idx == 0:
    idx_nearest = idx_sorted[0]
    return idx_nearest
  else:
    if abs(value - sorted_array[idx-1]) < abs(value - sorted_array[idx]):
      idx_nearest = idx_sorted[idx-1]
      return idx_nearest
    else:
      idx_nearest = idx_sorted[idx]
      return idx_nearest

# Load Data
gisaxsdata = np.genfromtxt(cwd + "/SC-IOS-7_Yoneda.xy")
q_gisaxs = (gisaxsdata[:, 0])
I_gisaxs = gisaxsdata[:, 1]
sI_gisaxs = np.sqrt(I_gisaxs + constant_gisaxs_backgorund)

q_pos = q_gisaxs > qmin
q_gisaxs = q_gisaxs[q_pos]
I_gisaxs = I_gisaxs[q_pos]
sI_gisaxs = sI_gisaxs[q_pos]

saxsdata = np.genfromtxt(cwd + "/rawdata/KWi338.xye")
q_saxs = saxsdata[:, 0]*10
I_saxs = saxsdata[:, 1]
sI_saxs = saxsdata[:, 2]

q_pos = q_saxs > qmin
q_saxs = q_saxs[q_pos]
I_saxs = I_saxs[q_pos]
sI_saxs = sI_saxs[q_pos]




# Transform Data
I_gisaxs -= constant_gisaxs_backgorund
I_gisaxs *= scale_gisaxs_to_saxs
sI_gisaxs *= scale_gisaxs_to_saxs

I_saxs -= constant_saxs_background
# Get Form Factor
qFF = []
IFF = []
sIFF= []
for iq, qval in enumerate(q_gisaxs):
  i_saxs = get_idx(q_saxs, qval)
  qval_saxs = q_saxs[i_saxs]
  if (qval_saxs - qval)/qval > 0.05:
    print("Warning! Far apart: " +str(qval_saxs) + " - " + str(qval))

  IFFval = I_gisaxs[iq]/I_saxs[i_saxs]
  qFF.append(qval)
  IFF.append(IFFval)
  sIFF.append(np.sqrt((sI_gisaxs[iq]/I_gisaxs[iq])**2 +
    (sI_saxs[i_saxs]/I_saxs[i_saxs])**2)*IFFval)
qFF = np.asarray(qFF)
# Simulate Structure Factor

alpha = (1+2*vol_frac)**2 / (1-vol_frac)**4
beta = -6*vol_frac*(1+vol_frac/2.)**2 / (1-vol_frac)**4
gamma = vol_frac*alpha/2.

x = 2*qFF*R
sinx = np.sin(x)
cosx = np.cos(x)
G = alpha/x**2 * (sinx - x*cosx) +\
    beta/x**3 * (2*x*sinx + (2-x**2)*cosx - 2) +\
    gamma/x**5 * (-x**4*cosx + 4*((3*x**2-6)*cosx +\
    (x**3 - 6*x)*sinx + 6))

S = 1/(1+ 24*vol_frac*G/x)

# Plot Data
x0, y0 = 0.13, 0.17
width, height = 1 - x0 - 0.01, 1 - y0 - 0.01
fig = plt.figure()
ax = fig.add_axes([x0, y0 + height/2, width, height/2])
axff = fig.add_axes([x0, y0, width, height/2])
ax.axhline(0, color='black')
ax.axvline(0, color='black')
ax.errorbar(q_saxs, I_saxs, sI_saxs, linestyle='None', color='gray',\
                        label="SAXS @ GALAXI")
ax.errorbar(q_gisaxs, I_gisaxs, sI_gisaxs, linestyle='None', color='#ca0020',\
                        label="GISAXS @ BM26B")
axff.axhline(1, color='gray')
axff.errorbar(qFF, IFF, sIFF, linestyle='None',\
          label="$\mathit{I}_{GISAXS} \, / \, \mathit{I}_{SAXS}$", zorder=0)
axff.plot(qFF, S,
            color='black', marker='None', zorder=2)
            # label="\nHard-sphere liquid\n(Percus-Yevick approximation)\n $R\,=\,"+\
            # "{:.1f}".format(R/10)+" nm$\n $\eta \,=\,"+"{:.0f}".format(vol_frac*100)+"$ %",\
ax.set_xlim([qmin, 2.4])
axff.set_xlim([qmin, 2.4])
axff.set_ylim([0, 2.5])
ax.set_ylim([0.01, 1000])
ax.set_yscale('log')
ax.set_xlabel("")
ax.set_ylabel("$\mathit{I} \, / \, cm^{-1}$")
ax.legend(loc='upper right')
axff.legend(loc='upper right')
axff.set_yticks([0,1,2])
axff.set_xlabel("$\mathit{q} \, / \, \AA^{-1}$")
axff.set_ylabel("$\mathit{S}(\mathit{q})$")
plt.setp(ax.get_xticklabels(), visible=False)

fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)

