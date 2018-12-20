from PyQt5.QtWidgets import QApplication
from Reflectivity.refl_data_correct import ReflCorrSliderApp, cReflCorrectD8

import numpy as np
import sys

class CorrectionApp(cReflCorrectD8):
    def init_data(self):
        # Load experimental data
        self.qmin = 0.005
        self.qmax = np.inf
        self.mode = 0
        self.data_path = "ES-S14.txt"
        self.reflsavefile = self.data_path.rsplit(".", 1)[0] + "_corrected.xy"

        # Bruker D8 properties
        self.wavelength = 1.54055
        self.beamwidth = 0.2
        self.samplelength = 10

if __name__ == "__main__":
    app = QApplication(sys.argv)
    aw = ReflCorrSliderApp(CorrectionApp)
    aw.show()
    app.exec_()
