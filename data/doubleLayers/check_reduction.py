import numpy as np
import sys, glob, datetime
import matplotlib.pyplot as plt
import lmfit
wavelength = 1.54055
numargs = len(sys.argv) - 1

beam_size_T = 0.2 # mm
sample_size_L = 10 # mm

def gaussian(p, x):
    return p['A'] * np.exp(-( (x - p['mu'])/p['sigma'] )**2 /2)

def residuum(p, x, y, sy, function):
    return (function(p,x) - y)/sy

def read_file(file, mode=0):
    start_reading_lines = False
    skipped_line = False

    ai = []
    counts = []
    loadfile = open(file, "r", errors="ignore")
    for line in loadfile:
        if start_reading_lines and skipped_line:
            split_line = line.strip().split(",")
            aival = float(split_line[0])
            if mode==1:
                aival /= 2.
            countval = float(split_line[1])
            if countval <= 0.:
                continue
            ai.append(aival)
            counts.append(countval)
            
        
        elif start_reading_lines:
            skipped_line = True
            continue
        else:
            if "[Data]" in line:
                start_reading_lines = True
                continue

    ai = np.asarray(ai)
    I = np.asarray(counts)
    sI = np.sqrt(I)
    q = 4*np.pi/wavelength * np.sin(ai * np.pi/180)
    valid_q = q > 0.00
    ai = ai[valid_q]
    q = q[valid_q]
    I = I[valid_q]
    sI = sI[valid_q]

    I = I / (sample_size_L * np.sin(ai) / beam_size_T)
    sI = sI / (sample_size_L * np.sin(ai) / beam_size_T)


    plateau_q = np.logical_and(q>0.01, q<0.015)
    meanI = np.mean(I[plateau_q])
    I /= meanI
    sI /= meanI
    return q, I, sI

def save_file(q, I, sI, filename):
    with open(saveto_path, 'w') as f:
        f.write('#Transformed D8 data to q on ' + str(datetime.datetime.now()) + '\n')
        f.write('#Used wavelength ' + str(wavelength) + '\n')
        f.write('#Footprint correction using beamsize ' + str(beam_size_T) +\
                ' and sample size ' + str(sample_size_L) + '\n')
        f.write('#q / A-1 \t Counts \t sqrt(Counts)\n')

        for iq, qval in enumerate(q):
            f.write(str(qval) + '\t'+ str(I[iq]) + '\t'+ str(sI[iq]) +'\n')

fig, ax = plt.subplots()
q,I,sI = read_file('./txt_files/SiScan.txt', mode=1)
ax.errorbar(q, I, sI, label='silicon')
q2,I2,sI2 = read_file('./txt_files/SiliconWafer_2gestapelt.txt')
# q,I,sI = read_file('./txt_files/ES-S14.txt')
ax.errorbar(q, I, sI, label='raw')
ax.errorbar(q2, I2, sI2, label='2nd Wafer')

# p = lmfit.Parameters()
# p.add('A', 50, min=0)
# p.add('mu', 0)
# p.add('sigma', 0.001)
# result = lmfit.minimize(residuum, p, args=(q[q<0.004], I[q<0.004], sI[q<0.004], gaussian))

# Icorr = I - gaussian(result.params, q)
# ax.errorbar(q, Icorr, sI, label='corrected')

# ax.plot(q, gaussian(result.params, q), marker='None', color='black')
ax.set_yscale('log')
ax.set_xlim(0, 0.2)
ax.set_ylim( 1e-5, 50)
plt.show()

# data_list = sorted(glob.glob('./txt_files/*.txt'))
# for file in data_list:
#     q,I,sI = read_file(file)
#     saveto_path = file.replace('.txt', '.xye').replace('txt_files/', '')
#     save_file(q, I, sI, saveto_path)
#     # plot_data(q, I, sI)

