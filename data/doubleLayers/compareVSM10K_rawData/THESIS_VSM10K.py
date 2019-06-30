import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from EverPPMS import PPMS

from modelexp.data import XyeData
from matplotlib.legend_handler import HandlerTuple

from PlottingTemplates.saxssanssanspol import color_variant
import lmfit
chapter = 'doublelayers'
sample_name = 'allSamples'
savefile = f'{chapter}_PPMS_10K_{sample_name}'

def linear(p, x):
  return p['m']*x + p['n']

def residuum(p, x, y, sy):
  return (y - linear(p, x))/sy

def fit(x, y, sy):
  p = lmfit.Parameters()
  p.add('m', -30)
  p.add('n', 100)
  fit_range = np.logical_and(x > 5, x<9)
  fit_x = x[fit_range]
  fit_y = y[fit_range]
  fit_sy = sy[fit_range]
  fit_result = lmfit.minimize(residuum, p, args=(fit_x,fit_y,fit_sy))
  return fit_result.params

def find_nearest_idx(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return idx

def get_Hc(x, y, sy):
  positive_vals = x > 0
  x_positive = x[positive_vals]
  y_positive = y[positive_vals]
  idx = find_nearest_idx(y_positive, 0)
  return x_positive[idx], y_positive[idx]

def determine_jump(x, y, sy):
  positive_area = np.logical_and(np.logical_and(x > 0.2, x < 0.4), y > 0)
  negative_area = np.logical_and(np.logical_and(x < -0.2, x > -0.4), y > 0)
  p = lmfit.Parameters()
  p.add('m', 10)
  p.add('n', 75)
  fit_x = x[positive_area]
  fit_y = y[positive_area]
  fit_sy = sy[positive_area]
  fit_result_pos = lmfit.minimize(residuum, p, args=(fit_x,fit_y,fit_sy))

  fit_x = x[negative_area]
  fit_y = y[negative_area]
  fit_sy = sy[negative_area]
  fit_result_neg = lmfit.minimize(residuum, p, args=(fit_x,fit_y,fit_sy))
  return fit_result_pos, fit_result_neg

def load_file(datafile):
  obj = PPMS(verbose=False)
  obj.load(datafile)
  obj.remove_virgin_data()
  B, M = obj.get_BM()
  sM = obj.get_sM()
  M *= 1e3
  sM *= 1e3

  p = fit(B, M, sM)
  print(f'{datafile.split("/")[-1].split(".DAT")[0]}\n\tchi = {p["m"].value} +/- {p["m"].stderr}\n\tMs = {p["n"].value} +/- {p["n"].stderr}')
  chi = p['m'].value
  M = M - chi*B

  B_Hc, M_Hc = get_Hc(B, M, sM)
  print(f'\tHc = {B_Hc} T \t M_Hc = {M_Hc}')

  fit_res_pos, fit_res_neg = determine_jump(B, M, sM)
  extra_data = {
    'slope_fit_positive': fit_res_pos,
    'slope_fit_negative': fit_res_neg,
  }
  deltaM = fit_res_pos.params['n'].value - fit_res_neg.params['n'].value
  print(f'\tDelta M = {deltaM} muemu')
  return B, M, sM, extra_data

B_1, M_1, sM_1, extra_data_1 = load_file('../dl_0-125/ppms/data/DD213_7_HYST_100OE_10K.DAT')
B_2, M_2, sM_2, extra_data_2 = load_file('../dl_0-25/ppms/data/DD205_10_HYST_100OE_10K.DAT')
B_3, M_3, sM_3, extra_data_3 = load_file('../dl_1-25/ppms/data/DD205_3_HYST_FC100OE_10KREPEAT.DAT')
B_4, M_4, sM_4, extra_data_4 = load_file('../dl_2-5/ppms/data/DD205_5_HYST_FC100OE_10KREPEAT.DAT')
B_5, M_5, sM_5, extra_data_5 = load_file('../dl_5/ppms/data/DD205_6_HYST_100OE_10K.DAT')

shift = 0

B_slope_pos = np.linspace(0., 0.4, 100)
B_slope_neg = np.linspace(-0.4, 0., 100)
fig = plt.figure()
left, bottom = 0.16, 0.16 #0.09, 0.16
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
# ax.axhline(0, color='lightgray', marker='None', zorder=0)
# ax.axvline(0, color='lightgray', marker='None', zorder=0)

ax.errorbar(B_1, M_1, sM_1, linestyle='None', marker='.', capsize=0, markersize=1, zorder=1, color=color_variant('#0EA8DF', 0), label='DL-0.125%')

ax.errorbar(B_2, M_2+shift, sM_2, linestyle='None', marker='.', capsize=0, markersize=1, zorder=1, color=color_variant('#0EA8DF', -50), label='DL-0.25%')

ax.errorbar(B_3, M_3+2*shift, sM_3, linestyle='None', marker='.', capsize=0, markersize=1, zorder=1, color=color_variant('#0EA8DF', -100), label='DL-1.25%')

ax.errorbar(B_4, M_4+3*shift, sM_4, linestyle='None', marker='.', capsize=0, markersize=1, zorder=1, color=color_variant('#0EA8DF', -150), label='DL-2.5%')

ax.errorbar(B_5, M_5+4*shift, sM_5, linestyle='None', marker='.', capsize=0, markersize=1, zorder=1, color=color_variant('#0EA8DF', -200), label='DL-5%')

ax.plot(B_slope_pos, linear(extra_data_1['slope_fit_positive'].params, B_slope_pos),
  color=color_variant('#FF0000', 0), marker='None', ls='-')
ax.plot(B_slope_neg, linear(extra_data_1['slope_fit_negative'].params, B_slope_neg),
  color=color_variant('#FF0000', 0), marker='None', ls='-')

ax.plot(B_slope_pos, linear(extra_data_2['slope_fit_positive'].params, B_slope_pos),
  color=color_variant('#FF0000', -50), marker='None', ls='-')
ax.plot(B_slope_neg, linear(extra_data_2['slope_fit_negative'].params, B_slope_neg),
  color=color_variant('#FF0000', -50), marker='None', ls='-')


ax.plot(B_slope_pos, linear(extra_data_3['slope_fit_positive'].params, B_slope_pos),
  color=color_variant('#FF0000', -100), marker='None', ls='-')
ax.plot(B_slope_neg, linear(extra_data_3['slope_fit_negative'].params, B_slope_neg),
  color=color_variant('#FF0000', -100), marker='None', ls='-')


ax.plot(B_slope_pos, linear(extra_data_4['slope_fit_positive'].params, B_slope_pos),
  color=color_variant('#FF0000', -150), marker='None', ls='-')
ax.plot(B_slope_neg, linear(extra_data_4['slope_fit_negative'].params, B_slope_neg),
  color=color_variant('#FF0000', -150), marker='None', ls='-')


ax.plot(B_slope_pos, linear(extra_data_5['slope_fit_positive'].params, B_slope_pos),
  color=color_variant('#FF0000', -200), marker='None', ls='-')
ax.plot(B_slope_neg, linear(extra_data_5['slope_fit_negative'].params, B_slope_neg),
  color=color_variant('#FF0000', -200), marker='None', ls='-')

ax.axvline(0.2, color='darkgrey', marker='None')
ax.axvline(0.4, color='darkgrey', marker='None')
ax.axvline(-0.2, color='darkgrey', marker='None')
ax.axvline(-0.4, color='darkgrey', marker='None')
handles, labels = ax.get_legend_handles_labels()

def add_legend(handle, title, height):
  legend = ax.legend([handle],[title],
    handler_map={tuple: HandlerTuple(ndivide=None)},
    fontsize=10,
    handletextpad=0,
    loc='upper left',
    bbox_to_anchor = [0.65, height],
    bbox_transform=fig.transFigure)
  return legend

legend1 = add_legend(handles[4], 'DL-5%', 0.58)
legend2 = add_legend(handles[3], 'DL-2.5%', 0.51)
legend3 = add_legend(handles[2], 'DL-1.25%', 0.44)
legend4 = add_legend(handles[1], 'DL-0.25%', 0.37)
legend5 = add_legend(handles[0], 'DL-0.125%', 0.3)

plt.gca().add_artist(legend1)
plt.gca().add_artist(legend2)
plt.gca().add_artist(legend3)
plt.gca().add_artist(legend4)


ax.set_xlabel("$\mathit{\mu_0 H} \, / \, T$")
ax.set_ylabel("$\mathit{M} \, / \, \mu emu$", labelpad=-10)
ax.set_xlim(-0.6, 0.6)
ax.set_ylim(60, 90)
plt.savefig(cwd + '/' + savefile)

# plt.show()