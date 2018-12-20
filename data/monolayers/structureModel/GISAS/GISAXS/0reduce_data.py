from GALAXI.dd_gisaxs.dd_gisaxs import DDGISAXS
import numpy as np
def treat_file(dat_file, save):
    obj = DDGISAXS()
    obj.set_sdd(1733.5)
    obj.set_beamcenter(610.41, 338.41)
    obj.load_and_merge(dat_file)
    obj.data_container.merged_data *= np.mean(np.mean(obj.data_container.merged_monitor))
    obj.save(save)
    # obj.plot(vmin=1e-9, vmax=1e-5, save=save)

treat_file("./rawdata/DresenDisch_DD175_28_18143.dat",\
           'DD175_28')
# treat_file("./rawdata/DresenDisch_DD175_28_18144.dat",\
#            'DD175_28_without_absorber')
