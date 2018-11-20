from GALAXI.dd_gisaxs.dd_gisaxs import DDGISAXS
import matplotlib.pyplot as plt
import numpy as np
obj = DDGISAXS()
obj.set_sdd(1733.5)
obj.set_beamcenter(610.41, 338.41)
obj.load_h5('DD175_28.h5')
q_min = 0.024
q_max = 0.029
obj.yoneda(q_min, q_max, vmin=1e-9, vmax=1e-5,\
           save='DD175_28_yoneda.xy', save_yoneda='GisaxsYonedaDD175_28.png',\
           save_2d='GISAXS_YonedaLines.png')
# qyslice, I_qyslice = obj.get_qy_slice(q_min, q_max)


# obj.plot(vmin=1e-9, vmax=1e-5)
# obj.ax.axhline(q_min, color='red')
# obj.ax.axhline(q_max, color='red')



# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.plot(qyslice, I_qyslice, label='Slice Along q_y')
# ax.set_yscale('log')
# ax.set_xlabel('$\mathit{q_y} \, / \, \mathrm{\AA^{-1}}$')
# ax.set_ylabel('$\mathit{I} \, / \, \mathrm{a.u.}$')
# ax.legend(loc='best')
# fig.tight_layout()
# fig.savefig()
plt.show()