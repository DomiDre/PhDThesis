import numpy as np
import matplotlib.pyplot as plt
from math import floor

def load_xye(datafile):
    rawdata = np.genfromtxt(datafile)
    x = rawdata[:, 0]
    y = rawdata[:, 1]
    sy = rawdata[:, 2]
    return x,y,sy

def gaussian(x, p):
    A, mu, sig, c = p['A'], p['mu'], p['sig'], p['c']
    return A*np.exp(- ((x-mu)/sig)**2 / 2.)+c

def lorentzian(x, p):
    A, mu, sig, c = p['A'], p['mu'], p['sig'], p['c']
    return A* 1/(1 + (2*(x-mu)/sig)**2 ) +c

def residuum(p, q, I, sI, Imodel):
    return (I - Imodel(q, p))/sI

def residuum_no_error(p, q, I, sI, Imodel):
    return (I - Imodel(q, p))

def get_power(num):
    power = floor(np.log10(num))
    cutted_num = int(np.round(num/(10**power)))
    if power > 0:
        format_power = 0
    else:
        format_power = abs(power)
    format_power = "{:."+str(format_power)+"f}"
    return power, str(cutted_num), format_power

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

def divide_arrays_with_different_grids(x1, y1, e1, x2, y2, e2):
    xres, yres, eres = [], [], []
    for i1, xval_1 in enumerate(x1):
        yval_1 = y1[i1]
        eval_1 = e1[i1]

        i2 = get_idx(x2, xval_1)
        xval_2 = x2[i2]        
        yval_2 = y2[i2]
        eval_2 = e2[i2]

        xval = (xval_1+xval_2)/2
        yval = yval_1 / yval_2
        syval = yval*np.sqrt((eval_1/yval_1)**2 + (eval_2/yval_2)**2)
        xres.append(xval)
        yres.append(yval)
        eres.append(syval)
    xres = np.asarray(xres)
    yres = np.asarray(yres)
    eres = np.asarray(eres)
    return xres, yres, eres