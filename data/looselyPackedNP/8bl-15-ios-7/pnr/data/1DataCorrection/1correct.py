from PyQt5.QtWidgets import QApplication
from refl_data_correct import ReflCorrSliderApp, cReflCorrect

import numpy as np
import sys

if __name__ == "__main__":
    exp_files = ["ES_S15_30K_FC_7Oe_Remanence_tranformed_angs_uu_masked_qz_I.xy",\
                 "ES_S15_30K_FC_7Oe_Remanence_tranformed_angs_du_masked_qz_I.xy",\
                 "ES_S15_30K_FC_7300Oe_tranformed_angs_uu_masked_qz_I.xy",\
                 "ES_S15_30K_FC_7300Oe_tranformed_angs_du_masked_qz_I.xy",\
                 "ES_S15_30K_ZFC_7Oe_Remanence_tranformed_angs_uu_masked_qz_I.xy",\
                 "ES_S15_30K_ZFC_7Oe_Remanence_tranformed_angs_du_masked_qz_I.xy",\
                 "ES_S15_30K_ZFC_7Oe_virgin_tranformed_angs_uu_masked_qz_I.xy",\
                 "ES_S15_30K_ZFC_7Oe_virgin_tranformed_angs_du_masked_qz_I.xy",\
                 "ES_S15_30K_ZFC_7300Oe_tranformed_angs_uu_masked_qz_I.xy",\
                 "ES_S15_30K_ZFC_7300Oe_tranformed_angs_du_masked_qz_I.xy"]

    app = QApplication(sys.argv)
    for exp_file in exp_files:
        class CorrectionApp(cReflCorrect):
            def init_data(self):
                # Load experimental data
                self.qmin = 0.005
                self.qmax = np.inf
                self.data_path = exp_file
                self.reflsavefile = self.data_path.rsplit(".", 1)[0] + "_corrected.xy"
                # Galaxi properties
                self.wavelength = 5.1386
                self.beamwidth = 1
                self.samplelength = 14

        aw = ReflCorrSliderApp(CorrectionApp)
        aw.plot_window.scale_and_footprint()
        aw.plot_window.export_corr_curve()
        aw.plot_window.save_plot()
        aw.fileQuit()
#        aw.show()
#        app.exit(app.exec_())
