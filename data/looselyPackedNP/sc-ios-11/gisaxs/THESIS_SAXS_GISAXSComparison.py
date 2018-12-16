import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')
import numpy as np

    # gisaxs_background:  456.141933 +/- 3.75819852 (0.82%) (init = 455)
    # gisaxs_scale:       1.3177e-04 +/- 7.5766e-07 (0.57%) (init = 0.00013177)
    # R:                  5.70167337 +/- 0.00938003 (0.16%) (init = 5.7)
    # vol_frac:           0.44735838 +/- 0.00229140 (0.51%) (init = 0.4472)

constant_saxs_background = 0
constant_gisaxs_backgorund = 456.1419
scale_gisaxs_to_saxs = 1.3177e-4
R = 5.70167337
vol_frac = 0.44735838

qmin = 0.12
qsf = 4e-4

chapter = 'looselyPackedNP'
sample_name = 'SC-IOS-11'
tiffile = cwd + "/rawdata/ES-S14_pos02_.tif"
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
gisaxsdata = np.genfromtxt(cwd + "/SC-IOS-11_Yoneda.xye")
q_gisaxs = (gisaxsdata[:, 0])*10
I_gisaxs = gisaxsdata[:, 1]
sI_gisaxs = np.sqrt(I_gisaxs + constant_gisaxs_backgorund)

q_pos = q_gisaxs > qmin
q_gisaxs = q_gisaxs[q_pos]
I_gisaxs = I_gisaxs[q_pos]
sI_gisaxs = sI_gisaxs[q_pos]

saxsdata = np.genfromtxt(cwd + "/rawdata/PMK18.xye")
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
axff.set_ylim([0, 2.9])
ax.set_ylim([0.01, 1000])
ax.set_yscale('log')
ax.set_xlabel("")
ax.set_ylabel("$\mathit{I} \, / \, cm^{-1}$")
ax.legend(loc='upper right')
axff.legend(loc='upper right')
axff.set_xlabel("$\mathit{q} \, / \, \AA^{-1}$")
axff.set_ylabel("$\mathit{S}(\mathit{q})$")
plt.setp(ax.get_xticklabels(), visible=False)

fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs+'/'+savefile)

