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

#    packingDensity1:   0.62800000 +/- 0.06245542 (9.95%) (init = 0.564)
#    packingDensity2:   0.67600000 +/- 0.09260149 (13.70%) (init = 0.628)
#    packingDensity3:   0.71800000 +/- 0.10741977 (14.96%) (init = 0.708)
#    packingDensity4:   0.64800000 +/- 0.18783836 (28.99%) (init = 0.624)
#    packingDensity5:   0.57400000 +/- 0.31183063 (54.33%) (init = 0.6)
#    packingDensity6:   0.70800000 +/- 0.29300111 (41.38%) (init = 0.83)
#    packingDensity7:   0.87000000 +/- 0.17965116 (20.65%) (init = 1.03)
#    packingDensity8:   0.97000000 +/- 0.14947596 (15.41%) (init = 0.902)
#    packingDensity9:   1.22400000 +/- 0.21135578 (17.27%) (init = 1.286)
#    packingDensity10:  0.75600000 +/- 0.42130305 (55.73%) (init = 0.75)
#    packingDensity11:  0 (fixed)
#    layerDistance1:   -8.00000000 +/- 1.70712830 (21.34%) (init = -4.5)
#    layerDistance2:   -8.80000000 +/- 2.44256821 (27.76%) (init = -4.3)
#    layerDistance3:   -9.30000000 +/- 2.34921020 (25.26%) (init = -7.2)
#    layerDistance4:   -10.6000000 +/- 3.81155966 (35.96%) (init = -7.5)
#    layerDistance5:   -7.50000000 +/- 6.14585333 (81.94%) (init = -2.4)
#    layerDistance6:   -6.60000000 +/- 7.79612472 (118.12%) (init = -4.6)
#    layerDistance7:   -11.5000000 +/- 4.77891405 (41.56%) (init = -6.6)
#    layerDistance8:   -14.5000000 +/- 5.28215463 (36.43%) (init = -12)
#    layerDistance9:    1.70000000 +/- 12.3984534 (729.32%) (init = -9.7)
#    layerDistance10:  -10.2000000 +/- 15.8218310 (155.12%) (init = -4.4)
#    layerDistance11:  -50 (fixed)
#    r:                 35.4 (fixed)
#    d:                 16.9 (fixed)
#    dSpacer:           52.6 (fixed)

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
  0.62800000,
  0.67600000,
  0.71800000,
  0.64800000,
  0.57400000,
  0.70800000,
  0.87000000,
  0.97000000,
  1.22400000,
  0.75600000,
  0.0])
delta_z = np.array([
-8.00000000,
-8.80000000,
-9.30000000,
-10.6000000,
-7.50000000,
-6.60000000,
-11.5000000,
-14.5000000,
 1.70000000,
-10.2000000,
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
