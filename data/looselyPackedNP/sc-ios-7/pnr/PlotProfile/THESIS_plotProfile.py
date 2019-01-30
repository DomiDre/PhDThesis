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

#    roughness:         9.56 (fixed)
#    roughnessSlope:    0.0266 (fixed)
#    packingDensity1:   0.8686337 (fixed)
#    packingDensity2:   0.7193376 (fixed)
#    packingDensity3:   0.57 (fixed)
#    packingDensity4:   0.442 (fixed)
#    packingDensity5:   0.3 (fixed)
#    packingDensity6:   0.4469171 (fixed)
#    packingDensity7:   0.5330438 (fixed)
#    packingDensity8:   0.5388016 (fixed)
#    packingDensity9:   0.5320628 (fixed)
#    packingDensity10:  0.538 (fixed)
#    packingDensity11:  0 (fixed)
#    layerDistance1:    16.4000000 +/- 0.33613209 (2.05%) (init = 16.5)
#    layerDistance2:   -0.58359825 +/- 0.30373346 (52.04%) (init = -0.5413965)
#    layerDistance3:   -4.23059930 +/- 0.28043369 (6.63%) (init = -4.3)
#    layerDistance4:   -11.5000000 +/- 0.40698961 (3.54%) (init = -11.4)
#    layerDistance5:   -29.9000000 +/- 0.76463619 (2.56%) (init = -29.7)
#    layerDistance6:   -30.5208384 +/- 0.54508696 (1.79%) (init = -30.6)
#    layerDistance7:   -17.3000000 +/- 0.40090168 (2.32%) (init = -17.32231)
#    layerDistance8:   -16.1000000 +/- 0.40344606 (2.51%) (init = -16.2)
#    layerDistance9:   -19.6000000 +/- 0.43726117 (2.23%) (init = -19.5)
#    layerDistance10:  -18.2000000 +/- 0.46035547 (2.53%) (init = -18.20955)

sample_name = 'SC-IOS-7'
Chapter = 'looselyPackedNP'
save_file = f"{Chapter}_VerticalStructure_{sample_name}_PNRDepiction.png"

circ_core_color = '#FAAB2D'
circ_shell_color = 'white'
substrate_color = '#0EA8DF'
spacer_color = color_variant('#0EA8DF', -50)

dense_packing = np.pi / (2 * np.sqrt(3))
Rcore = 3.488
dshell = 1.47
Rd = Rcore + dshell
x = np.linspace(-10, 10)
z = np.linspace(-100, 800, 900)

d_spacer = 51.39/10
packing_densities = np.array([
  0.8686337,
  0.7193376,
  0.57,
  0.442,
  0.3,
  0.4469171,
  0.5330438,
  0.5388016,
  0.5320628,
  0.538,
  0.0])
delta_z = np.array([
  -0.7,
  -0.58359825,
  -4.23059930,
  -11.5000000,
  -29.9000000,
  -30.5208384,
  -17.3000000,
  -16.1000000,
  -19.6000000,
  -18.2000000,
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
