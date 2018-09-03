#Initialized ScriptFactory v0.2
#Date: 2018-07-08 21:01:22.881954
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
#Initialized ScriptFactory v0.2
#Date: 2018-05-17 13:18:02.855070
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: EM
import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

from EM.tem import TEMSpheres
import numpy as np

cycle = plt.rcParams['axes.prop_cycle'].by_key()['color']

def color_variant(hex_color, brightness_offset=1):
    if len(hex_color) != 7:
        raise Exception("Passed %s into color_variant(), needs to be in #87c95f format." % hex_color)
    rgb_hex = [hex_color[x:x+2] for x in [1, 3, 5]]
    new_rgb_int = [int(hex_value, 16) + brightness_offset for hex_value in rgb_hex]
    new_rgb_int = [min([255, max([0, i])]) for i in new_rgb_int] # make sure new values are between 0 and 255
    # hex() produces "0x88", we want just "88"
    new_rgb_hex = []
    for i in new_rgb_int:
      new_hex = hex(i)[2:]
      if len(new_hex) == 1:
        new_rgb_hex.append('0')
      new_rgb_hex.append(new_hex)
    return "#" + "".join(new_rgb_hex)

chapter = 'monolayers'
sample_name = 'Ol_CoFe_C'
savefile = f'{chapter}_TEM_{sample_name}_sizeDist'

left_xlim, right_xlim = 7, 17
left, bottom = 0.16, 0.15

bins = 20

temOlCoFeC = TEMSpheres()
temOlCoFeC.Nbins = bins
lengths = temOlCoFeC.load_csv(cwd + "/EF2851_4_counted.xls")
temOlCoFeC.load(lengths)
temOlCoFeC.prepare_length_histogram(density=True)
temOlCoFeC.fit_lognormal(11, 0.1, density=True)
temOlCoFeC.export_fit_result(cwd + "/Ol_CoFe_C_size_dist.xy")

#Plot Fit:
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

b10 = ax.hist(
  temOlCoFeC.raw_data,
  bins=temOlCoFeC.Nbins,
  alpha=0.7,
  density=True,
  facecolor = cycle[0]
)

ax.errorbar(
  temOlCoFeC.bins, temOlCoFeC.counts, temOlCoFeC.errors, ls='None',
  color=color_variant(cycle[0], -100),
  alpha=0.7,
  label='Ol-CoFe-C'
)

x_for_fit_display = np.linspace(left_xlim, right_xlim, 500)

ax.plot(x_for_fit_display,\
  temOlCoFeC.lognormal(temOlCoFeC.p_result, x_for_fit_display),\
  color='black', marker='None')
ax.set_xlabel('$\mathit{d} \, / \, nm$')
ax.set_ylabel("$p(d)$")
ax.set_xlim([left_xlim, right_xlim])
ax.set_ylim([0, 0.55])
ax.legend(loc='upper left')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs + '/' + savefile)
