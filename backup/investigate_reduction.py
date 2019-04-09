from GALAXI.dd_saxs.dd_saxs import DDSAXS

import matplotlib.pyplot as plt

saxs = DDSAXS()
saxs.make_plots = False
datafolder = './rawdata/'

lsdd = 3386.155 + 140
lsdd_center = (595.811, 449.6049)
lsdd_mask = saxs.load_mask(datafolder+'Zakutna_Dresen_LSDD_AgBH_27623.1.mask.h5')

ssdd = 689.5715945008504 + 140
ssdd_center = (611.1067227605957, 528.6221448360504)
ssdd_mask = saxs.load_mask(datafolder+'Zakutna_Dresen_SSDD_AgBH_27646.1.mask.h5')

calibration_data = saxs.create_calibration()
calibration_data.set_FEP(27.9060, lsdd-140, 8279146.0)

empty_capillary = saxs.measurement('Empty Capillary',
               datafolder+'Zakutna_Dresen_LSDD_EC_27627.dat',\
               lsdd, lsdd_center, 0.7425, None, lsdd_mask,\
               datafolder+'Zakutna_Dresen_SSDD_EC_27649.dat',\
               ssdd, ssdd_center, 0.7398, None, ssdd_mask,\
               calibration_data=calibration_data)

toluene = saxs.measurement('Toluene',
               datafolder+'Zakutna_Dresen_LSDD_Toluene_27628.dat',\
               lsdd, lsdd_center, 0.5462, 0.1606, lsdd_mask,\
               datafolder+'Zakutna_Dresen_SSDD_Toluene_27650.dat',\
               ssdd, ssdd_center, 0.5440, 0.1605, ssdd_mask,\
               calibration_data=calibration_data,\
               empty_capillary=empty_capillary)

AH22 = saxs.measurement('AH22',
               datafolder+'Zakutna_Dresen_LSDD_AH22_27694.dat',\
               lsdd, lsdd_center, 0.5159, 0.1614, lsdd_mask,\
               datafolder+'Zakutna_Dresen_SSDD_AH22_27673.dat',\
               ssdd, ssdd_center, 0.5054, 0.1611, ssdd_mask,\
               calibration_data=calibration_data,\
               solvent=None,\
               empty_capillary=empty_capillary)

sf = 1.04
q_lsdd, I_lsdd, sI_lsdd, q_ssdd, I_ssdd, sI_ssdd = AH22.get_1d_data(True)
q_ec_lsdd, I_ec_lsdd, sI_ec_lsdd, q_ec_ssdd, I_ec_ssdd, sI_ec_ssdd = empty_capillary.get_1d_data(False)
q_solvent_lsdd, I_solvent_lsdd, sI_solvent_lsdd, q_solvent_ssdd, I_solvent_ssdd, sI_solvent_ssdd = toluene.get_1d_data(True)

fig, ax = plt.subplots()
ax.errorbar(q_ssdd, I_ssdd, sI_ssdd, label='Sample')
# ax.errorbar(q_ec_ssdd, I_ec_ssdd, sI_ec_ssdd)
ax.errorbar(q_solvent_ssdd, I_solvent_ssdd*sf, sI_solvent_ssdd*sf, label='Solvent')

ax.set_xlabel('$\mathit{q} \, / \, \AA^{-1}$')
ax.set_ylabel('$\mathit{I} \, / \, cm^{-1}$')
ax.set_xscale('log')
ax.set_yscale('log')
ax.legend().draw_frame(True)
plt.show()
