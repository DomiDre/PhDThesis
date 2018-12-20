import numpy as np
import sys, glob, datetime
import matplotlib.pyplot as plt
import lmfit
wavelength = 1.54055
numargs = len(sys.argv) - 1
# sample: 17 x 30mm
beam_size_T = 0.2 # mm
sample_size_L = 17 # mm
qmin, qmax = 0.02, np.inf

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
    validRange = np.logical_and(q > qmin, q < qmax)
    ai = ai[validRange]
    q = q[validRange]
    I = I[validRange]
    sI = sI[validRange]

    valid_q = q > 0.00
    valid_I = I > 1e-8
    validData = np.logical_and(valid_q, valid_I)
    ai = ai[validData]
    q = q[validData]
    I = I[validData]
    sI = sI[validData]

    I = I / (sample_size_L * np.sin(ai) / beam_size_T)
    sI = sI / (sample_size_L * np.sin(ai) / beam_size_T)


    plateau_q = np.logical_and(q>qmin, q<0.025)
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

data_list = sorted(glob.glob('./*.txt'))
for file in data_list:
    q,I,sI = read_file(file)
    saveto_path = file.replace('.txt', '.xye')
    save_file(q, I, sI, saveto_path)
