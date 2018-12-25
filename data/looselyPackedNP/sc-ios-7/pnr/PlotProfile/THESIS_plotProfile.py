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
#    packingDensity1:   0.99200000 +/- 0.01186954 (1.20%) (init = 1)
#    packingDensity2:   0.77400000 +/- 0.00852093 (1.10%) (init = 0.772)
#    packingDensity3:   0.59800000 +/- 0.01197739 (2.00%) (init = 0.59)
#    packingDensity4:   0.49000000 +/- 0.01203245 (2.46%) (init = 0.48)
#    packingDensity5:   0.45400000 +/- 0.01163689 (2.56%) (init = 0.456)
#    packingDensity6:   0.50000000 +/- 0.00978449 (1.96%) (init = 0.508)
#    packingDensity7:   0.54054250 +/- 0.00741074 (1.37%) (init = 0.54)
#    packingDensity8:   0.55200000 +/- 0.00824744 (1.49%) (init = 0.55)
#    packingDensity9:   0.51200000 +/- 0.01045665 (2.04%) (init = 0.514)
#    packingDensity10:  0.35400000 +/- 0.01888324 (5.33%) (init = 0.36)
#    packingDensity11:  0 (fixed)
#    layerDistance1:   -8.80000000 +/- 157689.100 (1791921.59%) (init = -0.3)
#    layerDistance2:   -0.10000000 +/- 0.65304392 (653.04%) (init = 0.3)
#    layerDistance3:   -6.30000000 +/- 0.41865491 (6.65%) (init = -6.8)
#    layerDistance4:   -14.5000000 +/- 0.64036218 (4.42%) (init = -16)
#    layerDistance5:   -22.6000000 +/- 0.92142774 (4.08%) (init = -23.4)
#    layerDistance6:   -25.9000000 +/- 0.99828618 (3.85%) (init = -25)
#    layerDistance7:   -24.6000000 +/- 0.57915997 (2.35%) (init = -24.2)
#    layerDistance8:   -24.4000000 +/- 0.65892818 (2.70%) (init = -24.5)
#    layerDistance9:   -26.8000000 +/- 0.66543584 (2.48%) (init = -27)
#    layerDistance10:  -32.0000000 +/- 0.96211142 (3.01%) (init = -31.7)
#    layerDistance11:  -50 (fixed)
#    r:                 35.4 (fixed)
#    d:                 16.9 (fixed)
#    dSpacer:           60.8000000 +/- 157689.208 (259357.25%) (init = 58.9)

sample_name = 'SC-IOS-7'
Chapter = 'looselyPackedNP'
save_file = f"{Chapter}_VerticalStructure_{sample_name}_PNRDepiction.png"

circ_core_color = '#FAAB2D'
circ_shell_color = 'white'
substrate_color = '#0EA8DF'
spacer_color = color_variant('#0EA8DF', -50)

dense_packing = np.pi / (2 * np.sqrt(3))
Rcore = 3.54
dshell = 1.69
Rd = Rcore + dshell
x = np.linspace(-10, 10)
z = np.linspace(-100, 800, 900)

d_spacer = 60.8000000/10
packing_densities = np.array([
  0.99200000,
  0.77400000,
  0.59800000,
  0.49000000,
  0.45400000,
  0.50000000,
  0.54054250,
  0.55200000,
  0.51200000,
  0.35400000,
  0.0])
delta_z = np.array([
  -8.80000000,
  -0.10000000,
  -6.30000000,
  -14.5000000,
  -22.6000000,
  -25.9000000,
  -24.6000000,
  -24.4000000,
  -26.8000000,
  -32.0000000,
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
