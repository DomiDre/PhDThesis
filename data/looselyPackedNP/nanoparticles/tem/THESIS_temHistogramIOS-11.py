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
def getValueWithErrorString(parameter, modifier=1):
  val = parameter.value*modifier
  std = parameter.stderr*modifier
  result = ''
  if (std > 0):
    power = np.floor(np.log10(std))
    cutted_std = int(np.round(std/(10**power)))
    cutted_val = np.round(val, int(-power))
    if power < 0:
      format_str = '{:.'+str(int(-power))+'f}'
      cutted_val = format_str.format(cutted_val)
      # cutted_val = str(cutted_val).ljust(int(-power)+2,'0')
    elif power >= 0:
      cutted_val = str(int(cutted_val))
      cutted_std = str(int(cutted_std * 10**power))

    result = f"{cutted_val}({cutted_std})"
  else:
    result = f"{val}"
  return result
chapter = 'looselyPackedNP'
sample_name = 'IOS-11'
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
fit_params = temIOS10.fitresults.params
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

ax.errorbar(
  temIOS10.bins, temIOS10.counts, temIOS10.errors, ls='None',
  color=color_variant(cycle[0], -100),
  alpha=0.7,
  label='IOS-11'
)

x_for_fit_display = np.linspace(left_xlim, right_xlim, 500)

ax.plot(x_for_fit_display,\
  temIOS10.lognormal(temIOS10.p_result, x_for_fit_display),\
  color='black', marker='None')

ax.text(0.07, 0.85,
  f'$\mu \,=\,{getValueWithErrorString(fit_params["logmu"])}\, nm$\n'+
  f'$\sigma \,=\,{getValueWithErrorString(fit_params["logstd"], 100)}\, \%$',
  color='black',
  horizontalalignment='left',
  verticalalignment='top',
  transform=ax.transAxes)

ax.set_xlabel('$\mathit{d} \, / \, nm$')
ax.set_ylabel("$p(d)$")
ax.set_xlim([left_xlim, right_xlim])
ax.set_ylim([0, 0.9])
ax.legend(loc='upper left')
fig.savefig(cwd + '/' + savefile)
fig.savefig(thesisimgs + '/' + savefile)
