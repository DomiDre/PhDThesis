import sys, os
thesisimgs = os.environ['phdthesisimgs']
cwd = sys.path[0]
import matplotlib.pyplot as plt
plt.style.use('phdthesis')

import numpy as np
from modelexp.data import MftData

from matplotlib.legend_handler import HandlerTuple


chapter = 'doubleLayers'
savefile = chapter+'_NR_compareThickness'

def load_xye(file):
  data = MftData()
  data.loadFromFile(file)
  q, I, sI = data.getData()
  q = np.array(q)
  I = np.array(I)
  sI = np.array(sI)
  valid_data = sI/I < 0.9
  q = q[valid_data]
  I = I[valid_data]
  sI = sI[valid_data]
  return q*10, I, sI

rPlus_file_0_25 =  '../dl_0-25/pnr/mftFiles/DD205_10_5K_10mT_u.mft'
rMinus_file_0_25 = '../dl_0-25/pnr/mftFiles/DD205_10_5K_10mT_d.mft'
rPlus_file_1_25 =  '../dl_1-25/pnr/mftFiles/DD205_3_5K_10mT_u.mft'
rMinus_file_1_25 = '../dl_1-25/pnr/mftFiles/DD205_3_5K_10mT_d.mft'
rPlus_file_2_5  =  '../dl_2-5/pnr/mftFiles/DD205_5_5K_10mT_u.mft'
rMinus_file_2_5  = '../dl_2-5/pnr/mftFiles/DD205_5_5K_10mT_d.mft'

q_p_1, I_p_1, sI_p_1 = load_xye(rPlus_file_0_25)
q_m_1, I_m_1, sI_m_1 = load_xye(rMinus_file_0_25)

q_p_2, I_p_2, sI_p_2 = load_xye(rPlus_file_1_25)
q_m_2, I_m_2, sI_m_2 = load_xye(rMinus_file_1_25)

q_p_3, I_p_3, sI_p_3 = load_xye(rPlus_file_2_5)
q_m_3, I_m_3, sI_m_3 = load_xye(rMinus_file_2_5)

left, bottom = 0.19, 0.17
fig = plt.figure()
ax = fig.add_axes([left,bottom, 1-left-0.01, 1-bottom-0.01])

ax.errorbar(q_p_1, I_p_1*1e2, sI_p_1*1e2, alpha=0.8, marker='None', capsize=0, label='DL-0.25% R+')
ax.errorbar(q_m_1, I_m_1*1e2, sI_m_1*1e2, alpha=0.8, marker='None', capsize=0, label='DL-0.25% R-')
ax.errorbar(q_p_2, I_p_2*1e1, sI_p_2*1e1, alpha=0.8, marker='None', capsize=0, label='DL-1.25% R+')
ax.errorbar(q_m_2, I_m_2*1e1, sI_m_2*1e1, alpha=0.8, marker='None', capsize=0, label='DL-1.25% R-')
ax.errorbar(q_p_3, I_p_3, sI_p_3,         alpha=0.8, marker='None', capsize=0, label='DL-2.5% R+')
ax.errorbar(q_m_3, I_m_3, sI_m_3,         alpha=0.8, marker='None', capsize=0, label='DL-2.5% R-')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('$\mathit{q_z} \, / \, nm^{-1}$')
ax.set_ylabel('$\mathit{R}$')
ax.set_xlim(0.06, 2.5)
ax.set_ylim(5e-7, 2.5e2)

handles, labels = ax.get_legend_handles_labels()
ax.legend(
  [(handles[0], handles[1]),
   (handles[2], handles[3]),
   (handles[4], handles[5])],
  ['DL-0.25%', 'DL-1.25%', 'DL-2.5%'],
  handler_map={tuple: HandlerTuple(ndivide=None)},
  fontsize=10,
  loc='lower left',
  bbox_to_anchor = [0.0, 0.0])

fig.savefig(cwd+'/'+savefile, bbox_inches='tight')
fig.savefig(thesisimgs+'/'+savefile, bbox_inches='tight')
plt.show()