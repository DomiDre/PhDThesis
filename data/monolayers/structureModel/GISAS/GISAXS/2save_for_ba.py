from GALAXI.dd_gisaxs.dd_gisaxs import DDGISAXS
import matplotlib.pyplot as plt
import numpy as np
import gzip, shutil
obj = DDGISAXS()
obj.set_sdd(1733.5)
obj.set_beamcenter(610.41, 338.41)
obj.load_h5('DD175_28.h5')

# with open() as f:
np.savetxt('DD175_28_data.txt', obj.get_data().T[::-1])
with open('DD175_28_data.txt', 'rb') as f_in, gzip.open('DD175_28_data.txt.gz', 'wb') as f_out:
    shutil.copyfileobj(f_in, f_out)