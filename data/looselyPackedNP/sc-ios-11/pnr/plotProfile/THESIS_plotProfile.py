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
#    roughness:               5.60659278 +/- 0.25471418 (4.54%) (init = 5.606671)
#    roughnessSlope:          0.05236433 +/- 0.00100331 (1.92%) (init = 0.052364)
#    packingDensity1:         0.95815 (fixed)
#    packingDensity2:         1.028049 (fixed)
#    packingDensity3:         0.8898551 (fixed)
#    packingDensity4:         0.7914817 (fixed)
#    packingDensity5:         0.7802482 (fixed)
#    packingDensity6:         0.1814358 (fixed)
#    layerDistance1:         -17.73307 (fixed)
#    layerDistance2:         -20.80183 (fixed)
#    layerDistance3:         -18.42797 (fixed)
#    layerDistance4:         -18.77368 (fixed)
#    layerDistance5:         -6.880126 (fixed)
#    layerDistance6:          6.04442 (fixed)
#    r:                       52.9 (fixed)
#    dShell:                  0 (fixed)
#    dSurfactant:             14.7 (fixed)
#    dSpacer:                 49.5998880 +/- 0.27341205 (0.55%) (init = 49.5)
sample_name = 'SC-IOS-11'
Chapter = 'looselyPackedNP'
save_file = f"{Chapter}_VerticalStructure_{sample_name}_PNRDepiction.png"

circ_core_color = '#FAAB2D'
circ_shell_color = color_variant('#FAAB2D', -50)
circ_surf_color = 'white'
substrate_color = '#0EA8DF'
spacer_color = color_variant('#0EA8DF', -50)

dense_packing = np.pi / (2 * np.sqrt(3))
Rcore = 5.290
dshell = 0.0
dsurf = 1.47
Rd = Rcore + dshell + dsurf
sigR = 0#0.05445854
x = np.linspace(-10, 10)
z = np.linspace(-100, 800, 900)
d_spacer = 49.5998880/10
packing_densities = np.array([
  0.95815,
  1.028049,
  0.8898551,
  0.7914817,
  0.7802482,
  0.1814358])
delta_z = np.array([
  -17.73307,
  -20.80183,
  -18.42797,
  -18.77368,
  -6.880126,
   6.04442])/10

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
