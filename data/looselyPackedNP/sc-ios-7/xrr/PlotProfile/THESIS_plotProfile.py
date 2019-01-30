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

#[[Variables]]
#    i0:                1 (fixed)
#    bg:                7e-06 (fixed)
#    roughness:         6.3 (fixed)
#    roughnessSlope:    0.0391 (fixed)
#    packingDensity1:   0.584 (fixed)
#    packingDensity2:   0.614 (fixed)
#    packingDensity3:   0.634 (fixed)
#    packingDensity4:   0.57 (fixed)
#    packingDensity5:   0.562 (fixed)
#    packingDensity6:   0.738 (fixed)
#    packingDensity7:   0.882 (fixed)
#    packingDensity8:   0.994 (fixed)
#    packingDensity9:   1.196 (fixed)
#    packingDensity10:  0.74 (fixed)
#    packingDensity11:  0 (fixed)
#    layerDistance1:   -1.10000000 +/- 1.59075059 (144.61%) (init = -1.2)
#    layerDistance2:   -5.86174505 +/- 1.75251623 (29.90%) (init = -5.9)
#    layerDistance3:   -5.17045479 +/- 1.99706730 (38.62%) (init = -5.2)
#    layerDistance4:   -6.07859540 +/- 2.55658826 (42.06%) (init = -6.1)
#    layerDistance5:   -2.88843899 +/- 3.79680256 (131.45%) (init = -2.9)
#    layerDistance6:   -4.44036642 +/- 4.07142557 (91.69%) (init = -4.5)
#    layerDistance7:   -8.26007229 +/- 3.56721950 (43.19%) (init = -8.3)
#    layerDistance8:   -9.39566023 +/- 4.07273173 (43.35%) (init = -9.4)
#    layerDistance9:    7.40000000 +/- 4.26823878 (57.68%) (init = 7.5)
#    layerDistance10:  -6.90000000 +/- 7.76624196 (112.55%) (init = -6.8)
#    layerDistance11:  -50 (fixed)
#    r:                 34.88 (fixed)
#    d:                 14.7 (fixed)
#    dSpacer:           47.9 (fixed)
#    sldCore:           4.0501e-05 (fixed)
#    sldShell:          8.52e-06 (fixed)
#    sldSubstrate:      2.0062e-05 (fixed)
#    sldSpacer:         1.98e-06 (fixed)
#    sldBackground:     0 (fixed)
#    dTheta:            0 (fixed)
#    wavelength:        1.5418 (fixed)
#    dWavelength:       0.0221 (fixed)

sample_name = 'SC-IOS-7'
Chapter = 'looselyPackedNP'
save_file = f"{Chapter}_VerticalStructure_{sample_name}_XRRDepiction.png"

circ_core_color = '#FAAB2D'
circ_shell_color = 'white'
substrate_color = '#0EA8DF'
spacer_color = color_variant('#0EA8DF', -50)

dense_packing = np.pi / (2 * np.sqrt(3))
Rcore = 3.488
dshell = 1.47
Rd = Rcore + dshell
sigR = 0#0.05445854
x = np.linspace(-10, 10)
z = np.linspace(-100, 800, 900)

d_spacer = 5.26
packing_densities = np.array([
  0.584,
  0.614,
  0.634,
  0.57,
  0.562,
  0.738,
  0.882,
  0.994,
  1.196,
  0.74,
  0.0])
delta_z = np.array([
-1.10000000,
-5.86174505,
-5.17045479,
-6.07859540,
-2.88843899,
-4.44036642,
-8.26007229,
-9.39566023,
 7.40000000,
-6.90000000,
  0.0])/10

h = np.sqrt(3.)*Rd
x0 = d_spacer +  Rd + delta_z[0]
x1 = x0 + h + delta_z[1]
x2 = x1 + h + delta_z[2]
x3 = x2 + h + delta_z[3]
x4 = x3 + h + delta_z[4]
x5 = x4 + h + delta_z[5]
x6 = x5 + h + delta_z[6]
x7 = x6 + h + delta_z[7]
x8 = x7 + h + delta_z[8]
x9 = x8 + h + delta_z[9]
x10 = x9 + h + delta_z[10]
z_0 = [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10]

def plot_circle(ax, x0, y0):
  circ = mplpatch.Circle(
    (x0, y0), Rcore+dshell,
    facecolor=circ_shell_color,
    edgecolor='black', lw=0.5, alpha=0.5)
  ax.add_artist(circ)
  circ = mplpatch.Circle((x0, y0), Rcore, facecolor=circ_core_color, edgecolor='None', lw=1)
  ax.add_artist(circ)

def plot_A_line(ax, h, dens):
  if dens > 0:
    sqdens = np.sqrt(dens/dense_packing)
    for i in range(-10, 10):
      plot_circle(ax, i*2*Rd/sqdens, h)

def plot_B_line(ax, h, dens, shift=0):
  if dens > 0:
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
plot_A_line(ax, z_0[6], packing_densities[6])
plot_B_line(ax, z_0[7], packing_densities[7])
plot_A_line(ax, z_0[8], packing_densities[8])
plot_B_line(ax, z_0[9], packing_densities[9])
plot_A_line(ax, z_0[10], packing_densities[10])

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
