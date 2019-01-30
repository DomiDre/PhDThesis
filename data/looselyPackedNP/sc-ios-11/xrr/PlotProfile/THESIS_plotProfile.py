import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import warnings
from modelexp.data import MultiData, XyemData, XyData
import matplotlib.patches as mplpatch
from PlottingTemplates.saxssanssanspol import color_variant


sample_name = 'SC-IOS-11'
Chapter = 'looselyPackedNP'
save_file = f"{Chapter}_VerticalStructure_{sample_name}_XRRDepiction.png"

circ_core_color = '#FAAB2D'
circ_shell_color = color_variant('#FAAB2D', -50)
circ_surf_color = 'white'
substrate_color = '#0EA8DF'
spacer_color = color_variant('#0EA8DF', -50)

dense_packing = np.pi / (2 * np.sqrt(3))
Rcore = 5.29
dshell = 0
dsurf = 1.47
Rd = Rcore + dshell + dsurf
sigR = 0#0.05445854
x = np.linspace(-10, 10)
z = np.linspace(-100, 800, 900)
#    i0:               1.16 (fixed)
#    bg:               1.4e-06 (fixed)
#    roughness:        3.46000000 +/- 0.24860136 (7.19%) (init = 3.3)
#    roughnessSlope:   0.02540000 +/- 0.00236169 (9.30%) (init = 0.0265)
#    packingDensity1:  0.64200000 +/- 0.01277521 (1.99%) (init = 0.652)
#    packingDensity2:  0.82445840 +/- 0.00623538 (0.76%) (init = 0.824)
#    packingDensity3:  0.85200000 +/- 0.00518885 (0.61%) (init = 0.8553459)
#    packingDensity4:  0.85200000 +/- 0.00845582 (0.99%) (init = 0.856)
#    packingDensity5:  0.77453617 +/- 0.02399899 (3.10%) (init = 0.774)
#    packingDensity6:  0.18400000 +/- 0.01910410 (10.38%) (init = 0.194)
#    layerDistance1:  -19.4000000 +/- 277086.637 (1428281.63%) (init = -19.3)
#    layerDistance2:  -30.9000000 +/- 0.29584225 (0.96%) (init = -30.9589)
#    layerDistance3:  -27.0000000 +/- 0.47599746 (1.76%) (init = -27.1)
#    layerDistance4:  -24.4000000 +/- 0.60693738 (2.49%) (init = -24)
#    layerDistance5:  -17.9000000 +/- 0.69559230 (3.89%) (init = -17.4)
#    layerDistance6:  -6.10000000 +/- 1.56847735 (25.71%) (init = -5.9)
#    r:                52.9 (fixed)
#    dShell:           0 (fixed)
#    dSurfactant:      14.7 (fixed)
#    dSpacer:          56.4000000 +/- 277086.608 (491288.31%) (init = 56.5)
#    reSldCore:        4.0501e-05 (fixed)
#    reSldShell:       4.0501e-05 (fixed)
#    reSldSurfactant:  8.52e-06 (fixed)
#    reSldSpacer:      7.6500e-06 +/- 2.1695e-07 (2.84%) (init = 7.92e-06)
#    reSldSubstrate:   2.0062e-05 (fixed)
#    reSldBackground:  0 (fixed)
#    imSldCore:        0 (fixed)
#    imSldShell:       0 (fixed)
#    imSldSurfactant:  0 (fixed)
#    imSldSpacer:      0 (fixed)
#    imSldSubstrate:   0 (fixed)
#    imSldBackground:  0 (fixed)
#    dTheta:           0 (fixed)
#    wavelength:       1.5418 (fixed)
#    dWavelength:      0.02080000 +/- 5.3128e-04 (2.55%) (init = 0.0195)
d_spacer = 49.1379792/10
packing_densities = np.array([
  0.64200000,
  0.82445840,
  0.85200000,
  0.85200000,
  0.77453617,
  0.18400000])
delta_z = np.array([
  -19.4000000,
  -30.9000000,
  -27.0000000,
  -24.4000000,
  -17.9000000,
  -6.10000000])/10

h = np.sqrt(3.)*Rd
x0 = d_spacer +  Rd + delta_z[0]
x1 = x0 + h + delta_z[1]
x2 = x1 + h + delta_z[2]
x3 = x2 + h + delta_z[3]
x4 = x3 + h + delta_z[4]
x5 = x4 + h + delta_z[5]
z_0 = [x0, x1, x2, x3, x4, x5]

def plot_circle(ax, x0, y0):
  circ = mplpatch.Circle(
    (x0, y0), Rcore+dshell+dsurf,
    facecolor=circ_surf_color,
    edgecolor='black', lw=0.5, alpha=0.5)
  ax.add_artist(circ)
  circ = mplpatch.Circle(
    (x0, y0), Rcore+dshell,
    facecolor=circ_shell_color,
    edgecolor='black', lw=0.5)
  ax.add_artist(circ)
  circ = mplpatch.Circle((x0, y0), Rcore, facecolor=circ_core_color, edgecolor='None', lw=1)
  ax.add_artist(circ)

def plot_A_line(ax, h, dens):
  sqdens = np.sqrt(dens/dense_packing)
  for i in range(-10, 10):
     plot_circle(ax, i*2*Rd/sqdens, h)

def plot_B_line(ax, h, dens, shift=0):
  sqdens = np.sqrt(dens/dense_packing)
  for i in range(-10, 10):
     plot_circle(ax, (2*i+1)*Rd/sqdens + shift, h)

def plot_B_line_empty(ax, h, dens):
  plot_circle(ax, Rd/np.sqrt(dens), h)

left, bottom = 0.12, 0.15

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

rect = mplpatch.Rectangle((-100, -20), 200, 20, facecolor=substrate_color, edgecolor='black', lw=0.25)
ax.add_artist(rect)
rect = mplpatch.Rectangle((-100, 0), 200, d_spacer, facecolor=spacer_color, edgecolor='black', lw=0.25)
ax.add_artist(rect)
plot_A_line(ax, z_0[0], packing_densities[0])
plot_B_line(ax, z_0[1], packing_densities[1])
plot_A_line(ax, z_0[2], packing_densities[2])
plot_B_line(ax, z_0[3], packing_densities[3])
plot_A_line(ax, z_0[4], packing_densities[4])
plot_B_line(ax, z_0[5], packing_densities[5])

ax.set_xlim([-50, 50])
ax.set_ylim([-10, 99])
ax.set_xticks([-40, -20, 0, 20, 40])
ax.set_yticks([0, 20, 40, 60, 80])
ax.set_xlabel("$\mathit{x}\,/\, nm$")
ax.set_ylabel("$\mathit{z}\,/\, nm$", labelpad=0)
ax.set_aspect('equal')
ax.tick_params(axis='both', which='major')
ax.tick_params(axis='both', which='minor')

fig.savefig(thesisimgs + '/' + save_file)
fig.savefig(cwd + '/' + save_file)
