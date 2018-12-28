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

sample_name = '8BL-x-IOS-7'
Chapter = 'looselyPackedNP'

fit_file_15 = "../../8bl-15-ios-7/gisaxs/fit/fit_result.dat"
fit_file_40 = "../../8bl-30-ios-7/gisaxs/fit/fit_result.dat"

saxs_file_15 = '../../8bl-15-ios-7/gisaxs/rawdata/KWi338.xye'
saxs_file_40 = '../../8bl-30-ios-7/gisaxs/rawdata/KWi338.xye'

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

saxsdata = np.genfromtxt(saxs_file_40)
q_saxs = saxsdata[:, 0]
I_saxs = saxsdata[:, 1]
sI_saxs = saxsdata[:, 2]

p_15, q_15, I_15, sI_15, Imodel_15 = get_data(fit_file_15)
p_40, q_40, I_40, sI_40, Imodel_40 = get_data(fit_file_40)

sf_15 = p_15['i0']['value']/i0_saxs
sf_40 = p_40['i0']['value']/i0_saxs
bg_15 = p_15['bg']['value']
bg_40 = p_40['bg']['value']
left, bottom = 0.2, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

shift_40 = 10
ax.errorbar(q_40, (I_40-bg_40)*shift_40, sI_40*shift_40,
  linestyle='None',
  color='#0EA8DF',
  label='8BL-30-IOS-7', zorder=0, capsize=0, marker='.', alpha=1)

ax.errorbar(q_15, I_15-bg_15, sI_15,
  linestyle='None',
  color='#FAAB2D',
  label='8BL-15-IOS-7', zorder=0, capsize=0, marker='.', alpha=1)

ax.errorbar(q_saxs, I_saxs*sf_40*shift_40, sI_saxs*sf_40*shift_40,
  linestyle='None',
  color='#EE292F',
  label='IOS-7', zorder=1, capsize=0, marker='.', alpha=0.2)

ax.errorbar(q_saxs, I_saxs*sf_15, sI_saxs*sf_15,
  linestyle='None',
  color='#EE292F',
  label='IOS-7', zorder=1, capsize=0, marker='.', alpha=0.2)

ax.plot(q_40, (Imodel_40-bg_40)*shift_40, marker='None',
  color=color_variant('#0EA8DF', -100),
  linestyle='-', zorder=2, alpha=0.8)
ax.plot(q_15, Imodel_15-bg_15, marker='None',
  color=color_variant('#FAAB2D', -100), linestyle='-', zorder=2, alpha=0.8)

# ax.text(0.01, 0.01,
#   '$\mathit{R}_\mathrm{HS} \, = \, ' + f'{getValueWithErrorString(p["hardSphereRadius"], 0.1)} nm$\n'+
#   '$\mathit{\eta} \, = \, ' + f'{getValueWithErrorString(p["eta"], 100)} \% $',
#   verticalalignment='bottom',
#   horizontalalignment='left',
#   transform=ax.transAxes)
ax.legend(loc='lower left', fontsize=10)
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q}\,/\,\AA^{-1}$")
ax.set_ylabel("$\mathit{I}\,/\, a.u.$")
ax.set_xlim([1.5e-2, 0.25])
ax.set_ylim([1e2, 5e7])
fig.savefig(cwd + '/' + pngfile)
fig.savefig(thesisimgs + '/' + pngfile)