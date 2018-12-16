from PyQt5.QtWidgets import QApplication
from SliderApp.slider_fit_app import SliderFitApp, cPlotAndFit

import numpy as np
import fabio
import sys, lmfit

def get_idx(array, value):
  idx_sorted = np.argsort(array)
  sorted_array = np.array(array[idx_sorted])
  idx = np.searchsorted(sorted_array, value, side="left")
  if idx >= len(array):
    idx_nearest = idx_sorted[len(array)-1]
    return idx_nearest
  elif idx == 0:
    idx_nearest = idx_sorted[0]
    return idx_nearest
  else:
    if abs(value - sorted_array[idx-1]) < abs(value - sorted_array[idx]):
      idx_nearest = idx_sorted[idx-1]
      return idx_nearest
    else:
      idx_nearest = idx_sorted[idx]
      return idx_nearest

class GuiApp(cPlotAndFit):
  def init_data(self):
    qmin = 0.3
    qsf = 4e-4
    gisaxsdata = np.genfromtxt("../SC-IOS-7_Yoneda.xy")
    q_gisaxs = (gisaxsdata[:, 0])
    I_gisaxs = gisaxsdata[:, 1]
    sI_gisaxs = np.sqrt(I_gisaxs)

    q_pos = q_gisaxs > qmin
    self.q_gisaxs = q_gisaxs[q_pos]
    self.I_gisaxs = I_gisaxs[q_pos]
    self.sI_gisaxs = sI_gisaxs[q_pos]

    saxsdata = np.genfromtxt("../rawdata/KWi338.xye")
    q_saxs = saxsdata[:, 0]*10
    I_saxs = saxsdata[:, 1]
    sI_saxs = saxsdata[:, 2]

    q_pos = q_saxs > qmin
    self.q_saxs = q_saxs[q_pos]
    self.I_saxs = I_saxs[q_pos]
    self.sI_saxs = sI_saxs[q_pos]

    # Get Form Factor
    self.p = lmfit.Parameters()
    self.p.add("gisaxs_background", 145.0, min = 0, max = 5000, vary = True)
    self.p.add("gisaxs_scale", 6.94e-05, min = 1e-05, max = 0.001, vary = True)
    self.p.add("R", 3.852, min = 0, max = 6, vary = True)
    self.p.add("vol_frac", 0.324, min = 0.2, max = 0.6, vary = True)
    self.p.add("q_offset", 0.0, min = -0.02, max = 0.02, vary = False)
    self.get_model()

  def get_model(self):
    qFF = []
    IFF = []
    sIFF= []
    for iq, qval in enumerate(self.q_gisaxs - self.p["q_offset"].value):
      i_saxs = get_idx(self.q_saxs, qval)
      qval_saxs = self.q_saxs[i_saxs]
#      if (qval_saxs - qval)/qval > 0.1:
#        print("Warning! Far apart: " +str(qval_saxs) + " - " + str(qval))

      IFFval =\
        self.p["gisaxs_scale"]*(self.I_gisaxs[iq]-self.p["gisaxs_background"])/\
                  self.I_saxs[i_saxs]
      qFF.append(qval)
      IFF.append(IFFval)
      sIFF.append(np.sqrt(\
        (self.sI_gisaxs[iq]*self.p["gisaxs_scale"]/self.I_saxs[i_saxs])**2+\
        (self.sI_saxs[i_saxs]*self.p["gisaxs_scale"]*(self.I_gisaxs[iq]-\
          self.p["gisaxs_background"])/self.I_saxs[i_saxs]**2)**2))
    self.qFF = np.asarray(qFF)
    self.IFF = np.asarray(IFF)
    self.sIFF = np.asarray(sIFF)

    vol_frac = self.p["vol_frac"].value
    radius = self.p["R"].value
    alpha = (1+2*vol_frac)**2 / (1-vol_frac)**4
    beta = -6*vol_frac*(1+vol_frac/2.)**2 / (1-vol_frac)**4
    gamma = vol_frac*alpha/2.

    x = 2*self.qFF*radius
    sinx = np.sin(x)
    cosx = np.cos(x)
    G = alpha * (sinx - x*cosx)/x**2 +\
        beta * (2*x*sinx + (2-x**2)*cosx - 2)/x**3 +\
        gamma * (-x**4*cosx + 4*((3*x**2-6)*cosx + (x**3 - 6*x)*sinx + 6))/x**5

    self.S = 1/(1+ 24*vol_frac*G/x)

  def define_plot_canvas(self):
    self.ax1 = self.fig.add_subplot(211)
    self.ax1.set_xlabel("$\mathit{x}$")
    self.ax1.set_ylabel("$\mathit{y}$")
    self.ax1.errorbar(self.q_saxs, self.I_saxs, self.sI_saxs, marker='.',\
          linestyle='None', color='#4dac26', label="SAXS")
    self.gisaxs_plot, = self.ax1.plot(self.q_gisaxs - self.p["q_offset"].value,\
        self.p["gisaxs_scale"]*(self.I_gisaxs - self.p["gisaxs_background"]),\
         marker='.',\
        linestyle='None', color='#ca0020', label="GISAXS")
    self.ax1.set_yscale('log')
    self.ax1.set_xlim([min(self.q_gisaxs - self.p["q_offset"].value), max(self.q_gisaxs - self.p["q_offset"].value)])
    self.ax1.set_ylim([min(self.p["gisaxs_scale"]*(self.I_gisaxs - self.p["gisaxs_background"]))*0.1,\
              max(self.p["gisaxs_scale"]*(self.I_gisaxs - self.p["gisaxs_background"]))*10])
    self.ax2 = self.fig.add_subplot(212)
    self.ax2.axhline(1, color='gray')
    self.model_plot, = self.ax2.plot(self.qFF, self.IFF, marker='None',\
        linestyle='-', color='#ca0020', lw=1)
    self.model2_plot, = self.ax2.plot(self.qFF, self.S, marker='None',\
        linestyle='-', color='black', lw=1)

  def figure_of_merit(self, p):
    self.p = p
    self.get_model()
    return (self.S-self.IFF)

  def get_dof(self):
    return 1
  def update_plot(self):
    self.get_model()
    self.model_plot.set_ydata(self.IFF)
    self.model2_plot.set_ydata(self.S)
    self.gisaxs_plot.set_data(self.q_gisaxs - self.p["q_offset"].value, self.p["gisaxs_scale"]*(self.I_gisaxs - self.p["gisaxs_background"]))
    self.draw()

if __name__ == "__main__":
  app = QApplication(sys.argv)
  aw = SliderFitApp(GuiApp)
  aw.show()
  app.exec_()
