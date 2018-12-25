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
#    packingDensity1:  0.96254190 +/- 0.00928796 (0.96%) (init = 0.962)
#    packingDensity2:  1.03310641 +/- 0.00309948 (0.30%) (init = 1.033033)
#    packingDensity3:  0.89382287 +/- 0.00415709 (0.47%) (init = 0.8938432)
#    packingDensity4:  0.79377190 +/- 0.00581214 (0.73%) (init = 0.792)
#    packingDensity5:  0.78293796 +/- 0.01289499 (1.65%) (init = 0.782)
#    packingDensity6:  0.18200000 +/- 0.01226776 (6.74%) (init = 0.1840058)
#    layerDistance1:  -22.1733049 +/- 4508.99696 (20335.25%) (init = -22.2)
#    layerDistance2:  -28.1157902 +/- 0.18298453 (0.65%) (init = -28.2)
#    layerDistance3:  -25.7816749 +/- 0.23444571 (0.91%) (init = -25.78749)
#    layerDistance4:  -26.2668009 +/- 0.32314767 (1.23%) (init = -26.3)
#    layerDistance5:  -14.5267741 +/- 0.45267322 (3.12%) (init = -14.6)
#    layerDistance6:  -1.80000000 +/- 1.32316210 (73.51%) (init = -1.7)
#    r:                38 (fixed)
#    dShell:           16 (fixed)
#    dSurfactant:      18.2 (fixed)
#    dSpacer:          49.8257842 +/- 4508.44335 (9048.41%) (init = 49.8)
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
d_spacer = 49.8257842/10
packing_densities = np.array([
  0.96254190,
  1.03310641,
  0.89382287,
  0.79377190,
  0.78293796,
  0.18200000])
delta_z = np.array([
  -22.1733049,
  -28.1157902,
  -25.7816749,
  -26.2668009,
  -14.5267741,
  -1.80000000])/10

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
