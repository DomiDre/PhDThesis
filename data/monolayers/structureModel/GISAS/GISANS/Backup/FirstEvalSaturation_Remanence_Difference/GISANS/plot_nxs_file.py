import h5py, sys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors


pixel_size_x = 2.5
pixel_size_y = 5
beam_center_x = 394.5
beam_center_y = 638.6

def open_nexus(nexus_file):
    print("Reading " + nexus_file)
    f = h5py.File(nexus_file, 'r')

    if "-det" in sys.argv:
        read_detector = int(sys.argv[sys.argv.index("-det")+1])
        if read_detector < 1 or read_detector > 5:
            sys.exit("Selected detector must be either 1, 2, 3, 4 or 5")
    else:
        read_detector = 1
    stri = str(read_detector)
    data = f["entry0/data"+stri+"/MultiDetector"+stri+"_linear_data"][:,:,0]
    f.close()
    
    return data

def get_custom_cmap():
    def make_colormap(seq):
        """Return a LinearSegmentedColormap
        seq: a sequence of floats and RGB-tuples. The floats should be increasing
        and in the interval (0,1).
        """
        cdict = {'red': [], 'green': [], 'blue': []}
        for i, item in enumerate(seq):
            pos, r, g, b = item
            cdict['red'].append([pos, r, r])
            cdict['green'].append([pos, g, g])
            cdict['blue'].append([pos, b, b])
        return mcolors.LinearSegmentedColormap('CustomMap', cdict)
    #Nice Coloring:
    c = mcolors.ColorConverter().to_rgb
    sabrina_colors = [(0, 0, 0, 0),\
             (0.18, 0.05, 0.05, 0.2),\
             (0.28, 0, 0, 1),\
             (0.4, 0.7, 0.85, 0.9),\
             (0.45, 0, 0.75, 0),\
             (0.6, 1, 1, 0),\
             (0.75, 1, 0, 0),\

             (0.92 , 0.6, 0.6, 0.6),\
             (1  , 0.95, 0.95, 0.95)]
    custom_cmap = make_colormap(sabrina_colors)
    custom_cmap.set_bad(color='black')
    return custom_cmap
    
if __name__ == '__main__':
    numargs = len(sys.argv) - 1
    if numargs < 1 or "-help" in sys.argv or "-h" in sys.argv:
        print("Usage of this script: nxs_file [...]")
        print("Possible parameters:")
        print("-det \t -- \t Select detector to save [Default: 1]")
        print("\t \t 1:center, 2:right, 3:left, 4:bottom, 5:top detector")
        sys.exit()

    filepath = sys.argv[1]
    #Step 1: Load data from nexus file
    detector_data = open_nexus(filepath)    
    
    Nx, Ny = detector_data.shape
    
    x_axis = np.arange(Nx)*pixel_size_x
    y_axis = np.arange(Ny)*pixel_size_y
    fig, ax = plt.subplots()
    ax.pcolormesh(x_axis, y_axis, detector_data.T, cmap=get_custom_cmap(),\
                norm=mcolors.LogNorm())
    
    ax.set_xlabel("$ \mathit{x} \, / \, mm$")
    ax.set_ylabel("$ \mathit{y} \, / \, mm$")
    ax.set_xlim([x_axis[0], x_axis[-1]])
    ax.set_ylim([y_axis[0], y_axis[-1]])
    ax.set_aspect('equal')
    fig.tight_layout()
    plt.show()
#    #Step 2: Save qx, qy, I to text file
#    save_file = open(sys.argv[2], "w")
#    save_file.write("#qx \t\tqy \t\t I \n")
#    for j in range(intensity.shape[1]):
#        for i in range(intensity.shape[0]):
#            save_file.write(str(qx[i, j])+"\t"+str(qy[i, j])+"\t"+str(intensity[i, j])+"\n")
#        save_file.write("\n")
#    save_file.close()
#    print("Saved data"+stri+" to " + sys.argv[2])

