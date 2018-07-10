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

chapter = 'looselyPackedNP'
sample_name = 'PMK18_KWi338'
savefile = chapter + '_TEM_' + sample_name+'_sizeDist'

left_xlim, right_xlim = 2, 17
left, bottom = 0.16, 0.15

bins = 20

temIOS10 = TEMSpheres()
temIOS10.Nbins = bins
lengths = temIOS10.load_csv(cwd + "/10nmIO/PMK18_001_counted.csv")
temIOS10.load(lengths)
temIOS10.prepare_length_histogram(density=True)
temIOS10.fit_lognormal(11, 0.1, density=True)
temIOS10.export_fit_result(cwd + "/PMK18_size_dist.xy")


temIOS7 = TEMSpheres()
temIOS7.Nbins = bins
lengths = temIOS7.load_csv(cwd + "/7nmIO/KWi338_001_counted.csv")
temIOS7.load(lengths)
temIOS7.prepare_length_histogram(density=True)
temIOS7.fit_lognormal_bimodal_density(7, 0.13, 0.1, 4, 0.1)
temIOS7.export_fit_result(cwd + "/KWi338_size_dist.xy")

#Plot Fit:
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

b10 = ax.hist(
  temIOS10.raw_data,
  bins=temIOS10.Nbins,
  alpha=0.7,
  density=True,
  facecolor = cycle[0]
)

b7 = ax.hist(
  temIOS7.raw_data,
  bins=temIOS7.Nbins,
  alpha=0.7,
  density=True,
  facecolor = cycle[1]
)
ax.errorbar(
  temIOS10.bins, temIOS10.counts, temIOS10.errors, ls='None',
  color=color_variant(cycle[0], -100),
  alpha=0.7,
  label='IOS-11'
)

ax.errorbar(
  temIOS7.bins, temIOS7.counts, temIOS7.errors, ls='None',
  color=color_variant(cycle[1], -100),
  alpha=0.7,
  label='IOS-7'
)

x_for_fit_display = np.linspace(left_xlim, right_xlim, 500)

ax.plot(x_for_fit_display,\
  temIOS7.lognormal_bimodal_density(temIOS7.p_result, x_for_fit_display),\
  color='black', marker='None')
  # label=\
  #   "$\mu_{log}\,=\,"+\
  #     "{:.1f}".format(temIOS7.p_result["logmu"].value)+\
  #     "\, nm$\n"+
  #   "$\sigma_{log}\,=\,"+\
  #     "{:.1f}".format(temIOS7.p_result["logstd"].value*100)+\
  #     "\, \%$")
ax.plot(x_for_fit_display,\
  temIOS10.lognormal(temIOS10.p_result, x_for_fit_display),\
  color='black', marker='None')
  # label=\
  #   "$\mu_{log}\,=\,"+\
  #     "{:.1f}".format(temIOS10.p_result["logmu"].value)+\
  #     "\, nm$\n"+
  #   "$\sigma_{log}\,=\,"+\
  #     "{:.1f}".format(temIOS10.p_result["logstd"].value*100)+\
  #     "\, \%$")

ax.set_xlabel('$\mathit{d} \, / \, nm$')
ax.set_ylabel("$p(d)$")
ax.set_xlim([left_xlim, right_xlim])
ax.set_ylim([0, 0.9])
ax.legend(loc='upper left')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs + '/' + savefile)
