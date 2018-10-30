import numpy as np
import matplotlib.pyplot as plt

def load_xygrasp(datafile):
    data = open(datafile, "r")
    x = []
    y = []
    sy = []
    for line in data:
        line = line.strip()
        if line.startswith("#") or line == "":
            continue
        split_line = line.split()

        if len(split_line) != 4:
            continue

        try:
            xval = float(split_line[0])
            yval = float(split_line[1])
            syval = float(split_line[2])
        except ValueError:
            continue
        x.append(xval)
        y.append(yval)
        sy.append(syval)
    data.close()
    return np.asarray(x), np.asarray(y), np.asarray(sy)

sf = 0.8596564519696263

def scale_file(infile):
    assert infile.endswith('.dat'), 'only supporting .dat file'
    x1, y1, sy1 = load_xygrasp(infile.replace('_la', '_sa'))
    x2, y2, sy2 = load_xygrasp(infile)

    y2 *= sf
    sy2 *= sf


    savefile = open(infile.replace('.dat',  "_scaled.dat"), "w")
    savefile.write("#Scaled file " + infile+"\n")
    savefile.write("#Using factor: " + str(sf)+"\n")
    savefile.write("#q / A-1 \t I / cm-1 \t sI / cm-1")
    for ix, xval in enumerate(x2):
        savefile.write(str(xval) + "\t" + str(y2[ix]) + "\t"+\
                str(sy2[ix]) + "\n")

    savefile.close()
    fig, ax = plt.subplots()
    ax.errorbar(x1, y1, sy1, ls='None', marker='.', label="SA")
    ax.errorbar(x2, y2, sy2, ls='None', marker='.', label="SA")

    ax.set_xlabel("$ \mathit{q} \, / \, \AA^{-1} $")
    ax.set_ylabel("$ \mathit{I} \, / \, cm^{-1}$")
    ax.set_xscale('log')
    ax.set_yscale('log')
    fig.tight_layout()
    plt.show()

scale_file("dd67_rfm_la.dat")
scale_file("dd67_rfp_la.dat")

