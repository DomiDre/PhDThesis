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


#    packingDensity1:   0.69378053 +/- 0.01208770 (1.74%) (init = 0.692)
#    packingDensity2:   0.64347201 +/- 0.01837646 (2.86%) (init = 0.642)
#    packingDensity3:   0.61836446 +/- 0.02220210 (3.59%) (init = 0.618)
#    packingDensity4:   0.66955983 +/- 0.04027818 (6.02%) (init = 0.668)
#    packingDensity5:   0.71064937 +/- 0.05703680 (8.03%) (init = 0.71)
#    packingDensity6:   0.73971669 +/- 0.05953412 (8.05%) (init = 0.738)
#    packingDensity7:   0.80624262 +/- 0.03773170 (4.68%) (init = 0.806)
#    packingDensity8:   0.94385917 +/- 0.02734093 (2.90%) (init = 0.942)
#    packingDensity9:   0.98708863 +/- 0.10851637 (10.99%) (init = 0.986)
#    packingDensity10:  0.64579908 +/- 0.08063425 (12.49%) (init = 0.644)
#    packingDensity11:  0 (fixed)
#    layerDistance1:   -13.7015186 +/- 0.56702426 (4.14%) (init = -13.8)
#    layerDistance2:   -12.6491152 +/- 0.62830269 (4.97%) (init = -12.7)
#    layerDistance3:   -11.3058075 +/- 0.76880774 (6.80%) (init = -11.4)
#    layerDistance4:   -12.9280512 +/- 0.62250807 (4.82%) (init = -13)
#    layerDistance5:   -14.1000000 +/- 0.71712440 (5.09%) (init = -14.2)
#    layerDistance6:   -13.8144894 +/- 0.78741525 (5.70%) (init = -13.9)
#    layerDistance7:   -13.5658363 +/- 0.87330233 (6.44%) (init = -13.6)
#    layerDistance8:   -13.1000000 +/- 1.22131181 (9.32%) (init = -13.2)
#    layerDistance9:   -5.46994995 +/- 3.73058987 (68.20%) (init = -5.5)
#    layerDistance10:  -30.8158813 +/- 3.86755685 (12.55%) (init = -30.9)
#    layerDistance11:  -50 (fixed)
#    r:                 35.4 (fixed)
#    d:                 16.9 (fixed)
#    dSpacer:           52.6 (fixed)
#    sldCore:           4.0501e-05 (fixed)
#    sldShell:          8.52e-06 (fixed)
#    sldSubstrate:      2.0062e-05 (fixed)
#    sldSpacer:         2.16e-06 (fixed)
#    sldBackground:     0 (fixed)
#    dTheta:            0 (fixed)
#    wavelength:        1.5418 (fixed)
#    dWavelength:       0.0221 (fixed)
#    qShift:           -0.0016 (fixed)

sample_name = 'SC-IOS-7'
Chapter = 'looselyPackedNP'
save_file = f"{Chapter}_VerticalStructure_{sample_name}_XRRDepiction.png"

circ_core_color = '#FAAB2D'
circ_shell_color = 'white'
substrate_color = '#0EA8DF'
spacer_color = color_variant('#0EA8DF', -50)

dense_packing = np.pi / (2 * np.sqrt(3))
Rcore = 3.54
dshell = 1.69
Rd = Rcore + dshell
sigR = 0#0.05445854
x = np.linspace(-10, 10)
z = np.linspace(-100, 800, 900)

d_spacer = 5.26
packing_densities = np.array([
  0.37594406,
  0.73350533,
  0.77174115,
  0.85528297,
  0.76460859,
  0.77348059,
  0.89360165,
  1.09000000,
  0.85489530,
  1.18079805,
  0.0])
delta_z = np.array([
  -42.9048318,
  -11.4816800,
  -20.7218922,
  -33.7846330,
  -25.7000000,
  -16.0523175,
  -11.7092073,
  -17.7457167,
  -13.2661415,
  -8.01873307,
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
