import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from modelexp.data import MultiData, XyData, XyeData

from matplotlib.legend_handler import HandlerTuple


chapter = 'doubleLayers'
savefile = chapter+'_NR_simPNR_2'

def load_xy(file):
  data = MultiData(XyData)
  data.loadFromFile(file)
  q_p, I_p = data.getDatasetBySuffix('p').getData()
  q_m, I_m = data.getDatasetBySuffix('m').getData()
  q_p = np.array(q_p)*10
  I_p = np.array(I_p)
  q_m = np.array(q_m)*10
  I_m = np.array(I_m)
  return q_p, I_p, q_m, I_m

def load_sld(file):
  data = MultiData(XyeData)
  data.loadFromFile(file)
  z, rho, rhoMag = data.getDataset(0).getData()
  z = np.array(z)/10
  rho = np.array(rho)*1e6
  rhoMag = np.array(rhoMag)*1e6
  return z, rho, rhoMag

fm_file =  './simulation_FM.xy'
afm_file =  './simulation_AFM.xy'
afm2_file =  './simulation_AFM2.xy'

q_p_fm, I_p_fm, q_m_fm, I_m_fm = load_xy(fm_file)
q_p_afm, I_p_afm, q_m_afm, I_m_afm = load_xy(afm_file)
q_p_afm2, I_p_afm2, q_m_afm2, I_m_afm2 = load_xy(afm2_file)

z_fm, rho_fm, rhoMag_fm = load_sld('./sld_FM.xy')
z_afm, rho_afm, rhoMag_afm = load_sld('./sld_AFM.xy')
z_afm2, rho_afm2, rhoMag_afm2 = load_sld('./sld_AFM2.xy')

left, bottom = 0.19, 0.17
x0in = 0.6
y0in = 0.7
widthin = 1-x0in-0.01
heightin= 1-y0in-0.01

fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])
ax_sld = fig.add_axes([x0in, y0in, widthin, heightin])
ax.plot(q_p_fm, I_p_fm*1e0, alpha=0.8, marker='None', label='FM R+')
ax.plot(q_m_fm, I_m_fm*1e0, alpha=0.8, marker='None', label='FM R-')
ax.plot(q_p_afm, I_p_afm*1e-1, alpha=0.8, marker='None', label='AFM R+')
ax.plot(q_m_afm, I_m_afm*1e-1, alpha=0.8, marker='None', label='AFM R-')
# ax.plot(q_p_afm2, I_p_afm2*1e0, alpha=0.8, marker='None', label='AFM2 R+')
# ax.plot(q_m_afm2, I_m_afm2*1e0, alpha=0.8, marker='None', label='AFM2 R-')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('$\mathit{q_z} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{R}$')
ax.set_xlim(0.06, 2.5)
ax.set_ylim(1e-8, 2.5e2)

ax_sld.plot(z_fm, rho_fm, marker='None', ls='-', color='black', alpha=0.5)
ax_sld.plot(z_fm, rhoMag_fm, marker='None', ls='-', color='#0EA8DF')
ax_sld.plot(z_afm, rhoMag_afm-0.1, marker='None', ls='-', color='#FAAB2D')
ax_sld.set_xlabel("$\mathit{z} \,/\,nm$", fontsize=8)
ax_sld.set_ylabel(r"$\rho \, / \, 10^{-6} \AA^{-2}$", fontsize=8)
ax_sld.set_xticks([0, 25, 50, 75, 100])
ax_sld.set_yticks([0, 1, 2, 3])
ax_sld.set_xlim([-10, 125])
ax_sld.set_ylim([-0.8, 3.4])
ax_sld.tick_params(axis='both', which='major', labelsize=8)


ax.text(0.03, 0.25, '$R^{+}, \, R^{-}$',
  transform=ax.transAxes, fontsize=10)
handles, labels = ax.get_legend_handles_labels()
ax.legend(
  [(handles[0], handles[1]),
   (handles[2], handles[3])
   ],
  ['FM-coupled', 'AFM-coupled'],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  loc='lower left',
  bbox_to_anchor = [0.0, 0.0])

fig.savefig(cwd+'/'+savefile, bbox_inches='tight')