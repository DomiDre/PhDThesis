import numpy as np
import matplotlib.pyplot as plt

def load_xygrasp(datafile):
    data = open(datafile, "r")
    x = []
    y = []
    sy = []
    dy = []
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
            dyval = float(split_line[3])
        except ValueError:
            continue
        x.append(xval)
        y.append(yval)
        sy.append(syval)
        dy.append(dyval)
    data.close()
    return np.asarray(x), np.asarray(y), np.asarray(sy), np.asarray(dy)

# sf = 0.8596564519696263
sf = 0.75
def treat_dataset(la_file):
    sa_file = la_file.replace("_la", "_sa")
    x1, y1, sy1, dy1 = load_xygrasp(sa_file)
    x2, y2, sy2, dy2 = load_xygrasp(la_file)

    y2 *= sf
    sy2 *= sf


    savefile = open(la_file.replace('.dat', '_scaled.dat'), "w")
    savefile.write("#Scaled file " + la_file+"\n")
    savefile.write("#Using factor: " + str(sf)+"\n")
    savefile.write("#q / A-1 \t I / cm-1 \t sI / cm-1 \t dI / cm-1\n")
    for ix, xval in enumerate(x2):
        savefile.write(f"{xval}\t{y2[ix]}\t{sy2[ix]}\t{dy2[ix]}\n")

    savefile.close()
    fig, ax = plt.subplots()
    ax.errorbar(x1, y1, sy1, ls='None', marker='.', label="SA")
    ax.errorbar(x2, y2, sy2, ls='None', marker='.', label="SA")

    ax.set_xlabel("$ \mathit{q} \, / \, \AA^{-1} $")
    ax.set_ylabel("$ \mathit{I} \, / \, cm^{-1}$")
    ax.set_xscale('log')
    ax.set_yscale('log')
    fig.tight_layout()
    fig.savefig(la_file.replace('.dat', '.png'))
    plt.show()
treat_dataset('./DD67_nuclear20_la.dat')
treat_dataset('./dd67_rfp_la.dat')
treat_dataset('./dd67_rfm_la.dat')

