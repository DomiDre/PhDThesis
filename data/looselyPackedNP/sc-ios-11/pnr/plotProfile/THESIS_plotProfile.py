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

#    bg:               2.6280e-05 +/- 1.1839e-06 (4.51%) (init = 2.62e-05)
#    roughness:        10.3898187 +/- 0.69498647 (6.69%) (init = 10.38)
#    roughnessSlope:   0.04370000 +/- 0.00348819 (7.98%) (init = 0.0438)
#    packingDensity1:  0.96594142 +/- 0.03383912 (3.50%) (init = 0.964)
#    packingDensity2:  1.04860158 +/- 0.00524166 (0.50%) (init = 1.048)
#    packingDensity3:  0.89837154 +/- 0.00850590 (0.95%) (init = 0.898)
#    packingDensity4:  0.80621368 +/- 0.01910966 (2.37%) (init = 0.806)
#    packingDensity5:  0.77600000 +/- 0.03014638 (3.88%) (init = 0.778)
#    packingDensity6:  0.15800584 +/- 0.02083547 (13.19%) (init = 0.158)
#    layerDistance1:  -1.37628667 +/- 39872.9300 (2897138.44%) (init = -1.4)
#    layerDistance2:  -27.4000000 +/- 0.48116955 (1.76%) (init = -27.3)
#    layerDistance3:  -25.4000000 +/- 0.61547640 (2.42%) (init = -25.3)
#    layerDistance4:  -25.0693139 +/- 0.74602230 (2.98%) (init = -25.07133)
#    layerDistance5:  -11.9179327 +/- 2.07224948 (17.39%) (init = -12)
#    layerDistance6:  -0.60000000 +/- 1.96777115 (327.96%) (init = -0.4)

sample_name = 'SC-IOS-11'
Chapter = 'looselyPackedNP'
save_file = f"{Chapter}_VerticalStructure_{sample_name}_PNRDepiction.png"

circ_core_color = '#FAAB2D'
circ_shell_color = color_variant('#FAAB2D', -50)
circ_surf_color = 'white'
substrate_color = '#0EA8DF'
spacer_color = color_variant('#0EA8DF', -50)

dense_packing = np.pi / (2 * np.sqrt(3))
Rcore = 3.8
dshell = 1.6
dsurf = 1.82
Rd = Rcore + dshell + dsurf
sigR = 0#0.05445854
x = np.linspace(-10, 10)
z = np.linspace(-100, 800, 900)
d_spacer = 37.1237265/10
packing_densities = np.array([
  0.96594142,
  1.04860158,
  0.89837154,
  0.80621368,
  0.77600000,
  0.15800584])
delta_z = np.array([
  -1.37628667,
  -27.4000000,
  -25.4000000,
  -25.0693139,
  -11.9179327,
  -0.60000000])/10

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
