from PyQt5.QtWidgets import QApplication
from refl_data_correct import ReflCorrSliderApp, cReflCorrect

import numpy as np
import sys

class CorrectionApp(cReflCorrect):
    def init_data(self):
        # Load experimental data
        self.qmin = 0.005
        self.qmax = np.inf
        self.data_path = "ES_S14_300K_4mT_refl_uu.xy"
        self.reflsavefile = self.data_path.rsplit(".", 1)[0] + "_corrected.xy"
        # Galaxi properties
        self.wavelength = 5.1386
        self.beamwidth = 0.5
        self.samplelength = 14

class CorrectionApp2(cReflCorrect):
    def init_data(self):
        # Load experimental data
        self.qmin = 0.005
        self.qmax = np.inf
        self.data_path = "ES_S14_300K_4mT_refl_du.xy"
        self.reflsavefile = self.data_path.rsplit(".", 1)[0] + "_corrected.xy"
        # Galaxi properties
        self.wavelength = 5.1386
        self.beamwidth = 0.5
        self.samplelength = 14
                

class CorrectionAppPlus(cReflCorrect):
    def init_data(self):
        # Load experimental data
        self.qmin = 0.005
        self.qmax = np.inf
        self.data_path = "ES_S14_300K_500mT_refl_uu.xy"
        self.reflsavefile = self.data_path.rsplit(".", 1)[0] + "_corrected.xy"
        # Galaxi properties
        self.wavelength = 5.1386
        self.beamwidth = 0.5
        self.samplelength = 14

class CorrectionAppMinus(cReflCorrect):
    def init_data(self):
        # Load experimental data
        self.qmin = 0.005
        self.qmax = np.inf
        self.data_path = "ES_S14_300K_500mT_refl_du.xy"
        self.reflsavefile = self.data_path.rsplit(".", 1)[0] + "_corrected.xy"
        # Galaxi properties
        self.wavelength = 5.1386
        self.beamwidth = 0.5
        self.samplelength = 14
        
class CorrectionAppRemPlus(cReflCorrect):
    def init_data(self):
        # Load experimental data
        self.qmin = 0.005
        self.qmax = np.inf
        self.data_path = "ES_S14_300K_4mT_Remanence_refl_uu.xy"
        self.reflsavefile = self.data_path.rsplit(".", 1)[0] + "_corrected.xy"
        # Galaxi properties
        self.wavelength = 5.1386
        self.beamwidth = 0.5
        self.samplelength = 14

class CorrectionAppRemMinus(cReflCorrect):
    def init_data(self):
        # Load experimental data
        self.qmin = 0.005
        self.qmax = np.inf
        self.data_path = "ES_S14_300K_4mT_Remanence_refl_du.xy"
        self.reflsavefile = self.data_path.rsplit(".", 1)[0] + "_corrected.xy"
        # Galaxi properties
        self.wavelength = 5.1386
        self.beamwidth = 0.5
        self.samplelength = 14

if __name__ == "__main__":
    app = QApplication(sys.argv)
    aw = ReflCorrSliderApp(CorrectionApp)
    aw.show()
    app.exec_()
    app.exit()

    app = QApplication(sys.argv)
    aw = ReflCorrSliderApp(CorrectionApp2)
    aw.show()
    app.exec_()
    app.exit()
    
#    app = QApplication(sys.argv)
#    aw = ReflCorrSliderApp(CorrectionAppPlus)
#    aw.show()
#    app.exec_()
#    app.exit()
#    
#    app = QApplication(sys.argv)
#    aw = ReflCorrSliderApp(CorrectionAppMinus)
#    aw.show()
#    app.exec_()
#    app.exit()
    
#    app = QApplication(sys.argv)
#    aw = ReflCorrSliderApp(CorrectionAppRemPlus)
#    aw.show()
#    app.exec_()
#    app.exit()
#    
#    app = QApplication(sys.argv)
#    aw = ReflCorrSliderApp(CorrectionAppRemMinus)
#    aw.show()
#    app.exec_()
#    app.exit()
