# Initialized ScriptFactory v0.2
# Date: 2018-07-11 20:36:37.178142
# Author(s)/Contact:
# Dominique Dresen	 Dominique.Dresen@uni-koeln.de

# Preparing Script for Experiment: THESIS
from matplotlib.legend_handler import HandlerTuple
from modelexp.data import MultiData, XyemData, XyeData
import warnings
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
plt.style.use('phdthesis')

inset_fontsize = 8

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

# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'ML_Ac-CoFe-C_WithSpacer'
Chapter = 'monolayers'
fit_file = cwd + "/models/MonolayerWithSpacerModel/fit_result.dat"
sld_file = cwd + "/models/MonolayerWithSpacerModel/fit_sld.dat"

labeltext = 'ML-Ac-CoFe-C'
q_min, q_max = 0.05, 1.99
I_min, I_max = 5e-8, 1.9e0

refl_pngfile = f"{Chapter}_VerticalStructure_{sample_name}_NR.png"


def get_clean_data(data, suffix, i0=1):
    q, I, sI, Imodel = data.getDatasetBySuffix(suffix).getData()
    q = np.array(q)
    I = np.array(I)
    sI = np.array(sI)
    Imodel = np.array(Imodel)
    q *= 10
    I /= i0
    sI /= i0
    Imodel /= i0
    # valid_data = sI/I < 0.5
    # q = q[valid_data]
    # I = I[valid_data]
    # sI = sI[valid_data]
    # Imodel = Imodel[valid_data]
    return q, I, sI, Imodel


# load data
data = MultiData(XyemData)
data.loadFromFile(fit_file)
i0 = data.params['i0']['value']
q_p, I_p, sI_p, Imodel_p = get_clean_data(data, 'p', i0)
q_m, I_m, sI_m, Imodel_m = get_clean_data(data, 'm', i0)

# load sld
sldData = MultiData(XyeData)
sldData.loadFromFile(sld_file)
r, sld, sldMag = sldData.getDataset(0).getData()

left, bottom = 0.19, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin = 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left, bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])
ax.errorbar(q_p, I_p, sI_p,
            linestyle='None',
            label='NR, $I_u$', zorder=0, capsize=0, marker='.')
ax.errorbar(q_m, I_m, sI_m,
            linestyle='None',
            label='NR, $I_d$', zorder=0, capsize=0, marker='.')
ax.plot(q_p, Imodel_p, zorder=1,
        color=color_variant('#0EA8DF', -150),    marker='None')
ax.plot(q_m, Imodel_m, zorder=1, color=color_variant('#EE292F', -150),
        marker='None')


handles, labels = ax.get_legend_handles_labels()

ax.text(0.05, 0.13, labeltext,
        transform=ax.transAxes, fontsize=inset_fontsize)
ax.legend(
    [(handles[0], handles[1])],
    ['$R^{+},\,R^{-}$'],
    handler_map={tuple: HandlerTuple(ndivide=None)},
    fontsize=inset_fontsize,
    loc='lower left')

# ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, nm^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax_sld.plot(r, sld, marker='None',
            color='black')
ax_sld.set_xlabel("$\mathit{z} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(
    r"$\rho_\mathrm{nuc.} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 10, 20])
ax_sld.set_yticks([0, 1, 2, 3])
ax_sld.set_xlim([-7, 25])
ax_sld.set_ylim([0, 3.6])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)

fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)
