import numpy as np
import matplotlib.pyplot as plt


exp_points_colorp = '#92c5de'
exp_points_colorm = '#f4a582'

folderpath = './mftFiles/'
files = {
  'Monolayer, 10 mT, I(+)': 'DD205_4_5K_10mT_u.mft',
  'Monolayer, 10 mT, I(-)': 'DD205_4_5K_10mT_d.mft',
  'Monolayer, 6 T, I(+)': 'DD205_4_5K_6000mT_u.mft',
  'Monolayer, 6 T, I(-)': 'DD205_4_5K_6000mT_d.mft',
  'Monolayer, -100 mT, I(+)': 'DD205_4_5K_-100mT_u.mft',
  'Monolayer, -100 mT, I(-)': 'DD205_4_5K_-100mT_d.mft',
  'DL 2.5%, 10 mT, I(+)': 'DD205_5_5K_10mT_u.mft',
  'DL 2.5%, 10 mT, I(-)': 'DD205_5_5K_10mT_d.mft',
  'DL 2.5%, 6 T, I(+)': 'DD205_5_5K_6000mT_u.mft',
  'DL 2.5%, 6 T, I(-)': 'DD205_5_5K_6000mT_d.mft',
  'DL 2.5%, -100 mT, I(+)': 'DD205_5_5K_-100mT_u.mft',
  'DL 2.5%, -100 mT, I(-)': 'DD205_5_5K_-100mT_d.mft',
  'DL 1.25%, 10 mT, I(+)': 'DD205_3_5K_10mT_u.mft',
  'DL 1.25%, 10 mT, I(-)': 'DD205_3_5K_10mT_d.mft',
  'DL 1.25%, 6 T, I(+)': 'DD205_3_5K_6000mT_u.mft',
  'DL 1.25%, 6 T, I(-)': 'DD205_3_5K_6000mT_d.mft',
  'DL 1.25%, -100 mT, I(+)': 'DD205_3_5K_-100mT_u.mft',
  'DL 1.25%, -100 mT, I(-)': 'DD205_3_5K_-100mT_d.mft',
  'DL 0.25%, 10 mT, I(+)': 'DD205_10_5K_10mT_u.mft',
  'DL 0.25%, 10 mT, I(-)': 'DD205_10_5K_10mT_d.mft',
  'DL 0.25%, 6 T, I(+)': 'DD205_10_5K_6000mT_u.mft',
  'DL 0.25%, 6 T, I(-)': 'DD205_10_5K_6000mT_d.mft',
  'DL 0.25%, -100 mT, I(+)': 'DD205_10_5K_-100mT_u.mft',
  'DL 0.25%, -100 mT, I(-)': 'DD205_10_5K_-100mT_d.mft',
  'DL 0.125%, 6 T, I(+)': 'DD213_7_5K_6000mT_u.mft',
  'DL 0.125%, 6 T, I(-)': 'DD213_7_5K_6000mT_d.mft',
  'DL 0.125%, -100 mT, I(+)': 'DD213_7_5K_-100mT_u.mft',
  'DL 0.125%, -100 mT, I(-)': 'DD213_7_5K_-100mT_d.mft',
  }


def readMFT(name):
  filename = files[name]
  rawdata = np.genfromtxt(folderpath+filename, skip_header=23)
  q = rawdata[:, 0]
  I = rawdata[:, 1]
  sI = rawdata[:, 2]
  dq_fwhm = rawdata[:, 3]
  return q, I, sI, dq_fwhm

def readAndPlot(name, color=None, sf=1):
  q, I, sI, dQ = readMFT(name)

  ax.errorbar(q, I*sf, sI*sf,\
            marker='o', linestyle='-', color=color,\
            label=name, markersize=2, capsize=2,\
            elinewidth=1)

def save_ax(savename):
  ax.set_xlabel("$\mathit{q_z} \, / \, \AA^{-1}$")
  ax.set_ylabel("$\mathit{I} \, / \, a.u.$")
  ax.set_xlim([0.005, 0.22])
  ax.set_ylim([5e-8, 120])
  ax.legend(loc='upper right')
  ax.set_yscale('log')
  # #        ax.set_yticks([1e-7, 1e-5, 1e-4,1e-3, 1e-2, 1e-1, 1, 1e1, 1e2])

  fig.savefig(savename)

fig, ax = plt.subplots()
readAndPlot('Monolayer, 10 mT, I(+)', sf=1e-2)
readAndPlot('Monolayer, 10 mT, I(-)', sf=1e-2)
readAndPlot('DL 0.25%, 10 mT, I(+)', sf=1e0)
readAndPlot('DL 0.25%, 10 mT, I(-)', sf=1e0)
readAndPlot('DL 1.25%, 10 mT, I(+)', sf=1e1)
readAndPlot('DL 1.25%, 10 mT, I(-)', sf=1e1)
readAndPlot('DL 2.5%, 10 mT, I(+)', sf=1e2)
readAndPlot('DL 2.5%, 10 mT, I(-)', sf=1e2)
save_ax('DD205_10mT.png')

fig, ax = plt.subplots()
readAndPlot('Monolayer, 6 T, I(+)', sf=1e-2)
readAndPlot('Monolayer, 6 T, I(-)', sf=1e-2)
readAndPlot('DL 0.125%, 6 T, I(+)', sf=1e-1)
readAndPlot('DL 0.125%, 6 T, I(-)', sf=1e-1)
readAndPlot('DL 0.25%, 6 T, I(+)', sf=1e0)
readAndPlot('DL 0.25%, 6 T, I(-)', sf=1e0)
readAndPlot('DL 1.25%, 6 T, I(+)', sf=1e1)
readAndPlot('DL 1.25%, 6 T, I(-)', sf=1e1)
readAndPlot('DL 2.5%, 6 T, I(+)', sf=1e2)
readAndPlot('DL 2.5%, 6 T, I(-)', sf=1e2)
save_ax('DD205_6T.png')

fig, ax = plt.subplots()
readAndPlot('Monolayer, -100 mT, I(+)', sf=1e-2)
readAndPlot('Monolayer, -100 mT, I(-)', sf=1e-2)
readAndPlot('DL 0.125%, -100 mT, I(+)', sf=1e-1)
readAndPlot('DL 0.125%, -100 mT, I(-)', sf=1e-1)
readAndPlot('DL 0.25%, -100 mT, I(+)', sf=1e0)
readAndPlot('DL 0.25%, -100 mT, I(-)', sf=1e0)
readAndPlot('DL 1.25%, -100 mT, I(+)', sf=1e1)
readAndPlot('DL 1.25%, -100 mT, I(-)', sf=1e1)
readAndPlot('DL 2.5%, -100 mT, I(+)', sf=1e2)
readAndPlot('DL 2.5%, -100 mT, I(-)', sf=1e2)
save_ax('DD205_-100mT.png')
plt.show()
