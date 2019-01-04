#Initialized ScriptFactory v0.2
#Date: 2018-06-29 18:48:40.453330
#Author(s)/Contact:
#Dominique Dresen	 Dominique.Dresen@uni-koeln.de

#Preparing Script for Experiment: THESIS
import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np

from modelexp.data import XyeData, XyemData, MultiData


datfile = './rescale/Ac_CoFe_C_Dispersion_300K_LangevinSAXSscaled.xye'
paramfile = './fit_result.dat'

chapter = 'monolayer'
sample_name = 'Ac_CoFe_C'

savefile = chapter + '_VSM_300K_' + sample_name

# data = XyeData()
# data.loadFromFile(datfile)
# B, M, sM = data.getData()

# def getValueWithErrorString(parameter, modifier=1):
#   val = parameter['value']*modifier
#   std = parameter['std']*modifier
#   result = ''
#   if (std > 0):
#     power = np.floor(np.log10(std))
#     cutted_std = int(np.round(std/(10**power)))
#     cutted_val = np.round(val, int(-power))
#     if power < 0:
#       format_str = '{:.'+str(int(-power))+'f}'
#       cutted_val = format_str.format(cutted_val)
#       # cutted_val = str(cutted_val).ljust(int(-power)+2,'0')
#     elif power >= 0:
#       cutted_val = str(int(cutted_val))
#       cutted_std = str(int(cutted_std * 10**power))

#     result = f"{cutted_val}({cutted_std})"
#   else:
#     result = f"{val}"
#   return result

fitData = MultiData(XyemData)
fitData.loadFromFile(paramfile)
B, M, sM, Mmodel = fitData.getDataset(0).getData()
# fit_params = fitData.params

# chi = fit_params['chi']['value']
# # chi = -0.0366315 * 4.631539113631906 * 1000
# M -= chi*B
# Mmodel -= chi*B

min_B, max_B = -2.2, 2.2
min_M, max_M = -350, 350
T = 300

fig = plt.figure()
left, bottom = 0.21, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.axhline(0, color='lightgray', marker='None', zorder=0)
ax.axvline(0, color='lightgray', marker='None', zorder=0)
ax.errorbar(B, M, sM, linestyle='None', marker='.', zorder=1,\
            label='Dispersion', capsize=0)
ax.plot(B, Mmodel, marker='None', zorder=2, color='black')

ax.set_xlabel(r"$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel(r"$\mathit{M} \, / \, kAm^{-1}$")

ax.text(0.95,0.1,'Ac-CoFe-C',
  transform=ax.transAxes,
  horizontalalignment='right',
  verticalalignment='top')

ax.set_xlim(min_B, max_B)
ax.set_ylim(min_M, max_M)
ax.legend(bbox_to_anchor=[0.53, 1.0])
plt.savefig(cwd + '/' + savefile)
plt.savefig(thesisimgs + '/' + savefile)