#Initialized ScriptFactory v0.2
#Date: 2018-07-11 20:36:37.178142
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
import warnings
from modelexp.data import MultiData, XyemData, XyData

from PlottingTemplates.saxssanssanspol import colors, inset_fontsize, color_variant
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'SC-IOS-7'
Chapter = 'looselyPackedNP'

fit_file = cwd + "/fit/fit_result.dat"
saxs_file = cwd + '/rawdata/KWi338.xye'
i0_saxs = 1.63

pngfile = Chapter + '_GISAXS_StructureFactor_' + sample_name + ".png"

#load data
def get_data(fit_result):
  data = MultiData(XyemData)
  data.loadFromFile(fit_result)
  q, I, sI, Imodel = data.getDataset(0).getData()
  params = data.params
  return params, q, np.array(I), np.array(sI), np.array(Imodel)

def getValueWithErrorString(parameter, modifier=1):
  val = parameter['value']*modifier
  std = parameter['std']*modifier
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

saxsdata = np.genfromtxt(saxs_file)
q_saxs = saxsdata[:, 0]
I_saxs = saxsdata[:, 1]
sI_saxs = saxsdata[:, 2]

p, q, I, sI, Imodel = get_data(fit_file)

sf = p['i0']['value']/i0_saxs
bg = p['bg']['value']
left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.errorbar(q, I-bg, sI,
  linestyle='None',
  label='SC-IOS-7', zorder=0, capsize=0, marker='.', alpha=1)

ax.errorbar(q_saxs, I_saxs*sf, sI_saxs*sf,
  linestyle='None',
  label='IOS-7', zorder=1, capsize=0, marker='.', alpha=0.2)

ax.plot(q, Imodel-bg, marker='None',
  color='black', linestyle='-', zorder=2, alpha=0.8)

ax.text(0.01, 0.01,
  '$\mathit{R}_\mathrm{HS} \, = \, ' + f'{getValueWithErrorString(p["hardSphereRadius"], 0.1)} nm$\n'+
  '$\mathit{\eta} \, = \, ' + f'{getValueWithErrorString(p["eta"], 100)} \% $',
  verticalalignment='bottom',
  horizontalalignment='left',
  transform=ax.transAxes)
ax.legend(loc='upper right')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\, a.u.$")
ax.set_xlim([1.5e-2, 0.25])
ax.set_ylim([1e2, 5e6])
fig.savefig(thesisimgs + '/' + pngfile)
fig.savefig(cwd + '/' + pngfile)