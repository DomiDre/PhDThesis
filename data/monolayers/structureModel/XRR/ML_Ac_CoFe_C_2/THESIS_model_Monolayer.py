# Initialized ScriptFactory v0.2
# Date: 2018-07-11 20:36:37.178142
# Author(s)/Contact:
# Dominique Dresen	 Dominique.Dresen@uni-koeln.de

# Preparing Script for Experiment: THESIS
from modelexp.data import MultiData, XyemData, XyData
import warnings
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
plt.style.use('phdthesis')

inset_fontsize = 8
# remove some annoying warnings
warnings.filterwarnings("ignore", category=UserWarning, module='matplotlib')

sample_name = 'ML_Ac-CoFe-C-2_WithSpacer'
Chapter = 'monolayers'
fit_file = cwd + "/models/MonolayerWithSpacerModel/fit_result.dat"
sld_file = cwd + "/models/MonolayerWithSpacerModel/fit_sld.dat"

labeltext = 'ML-Ac-CoFe-C-2'
q_min, q_max = 1e-1, 3.99
I_min, I_max = 5e-7, 1.9e0

refl_pngfile = f"{Chapter}_SquareArrayParacrystal_{sample_name}_XRR.png"


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

def get_clean_data(data):
    q, I, sI, Imodel = data.getDataset(0).getData()
    q = np.array(q)
    I = np.array(I)
    sI = np.array(sI)
    Imodel = np.array(Imodel)
    valid_data = sI/I < 1
    q = q[valid_data]
    I = I[valid_data]
    sI = sI[valid_data]
    Imodel = Imodel[valid_data]
    return q*10, I, sI, Imodel


# load data
data = MultiData(XyemData)
data.loadFromFile(fit_file)
q, I, sI, Imodel = get_clean_data(data)
print(data.chi2)
# load sld
sldData = MultiData(XyData)
sldData.loadFromFile(sld_file)
r, sld = sldData.getDataset(0).getData()

left, bottom = 0.19, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin = 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left, bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])
ax.errorbar(q, I, sI,
            linestyle='None',
            label='XRR', zorder=0, capsize=0, marker='.')
ax.plot(q, Imodel, zorder=1, color='black', marker='None')
ax.legend(loc='lower left', fontsize=inset_fontsize)
ax.set_yscale('log')
ax.set_xlabel("$\mathit{q_z} \, / \, nm^{-1}$")
ax.set_ylabel("$\mathit{R}$")
ax.set_xlim([q_min, q_max])
ax.set_ylim([I_min, I_max])

ax.text(0.05, 0.15, labeltext,
        transform=ax.transAxes, fontsize=inset_fontsize)
ax_sld.plot(r, sld, marker='None',
            color='black')
ax_sld.set_xlabel("$\mathit{z} \,/\,nm$", fontsize=inset_fontsize)
ax_sld.set_ylabel(
    r"$\rho_\mathrm{el.} \, / \, 10^{-6} \AA^{-2}$", fontsize=inset_fontsize)
ax_sld.set_xticks([0, 10, 20])
ax_sld.set_yticks([0, 10, 20])
ax_sld.set_xlim([-4, 25])
ax_sld.set_ylim([0, 24])
ax_sld.tick_params(axis='both', which='major', labelsize=inset_fontsize)

fig.savefig(thesisimgs + '/' + refl_pngfile)
fig.savefig(cwd + '/' + refl_pngfile)
