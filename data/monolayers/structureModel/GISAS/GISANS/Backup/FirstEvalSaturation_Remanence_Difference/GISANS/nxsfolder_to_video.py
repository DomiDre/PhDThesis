import sys, glob
import numpy as np
import h5py
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as manimation
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable


pixel_size_x = 2.5
pixel_size_y = 5
beam_center_x = 127.69*pixel_size_x#394.5
beam_center_y = 65.23*pixel_size_y#638.6
wavelength = 6 # Angstrom
sdd = 2504 # mm

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

def axis_to_qyqz(y, z):
    k0 = 2*np.pi/wavelength
    tthf = np.arctan(y/sdd)
    aiaf = np.arctan(z/sdd)
    qy = k0*np.sin(tthf)
    qz = k0*np.sin(aiaf)
    return qy, qz
    
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
    custom_colors = [(0, 0, 0, 0),\
             (0.18, 0.05, 0.05, 0.2),\
             (0.28, 0, 0, 1),\
             (0.4, 0.7, 0.85, 0.9),\
             (0.45, 0, 0.75, 0),\
             (0.6, 1, 1, 0),\
             (0.75, 1, 0, 0),\

             (0.92 , 0.6, 0.6, 0.6),\
             (1  , 0.95, 0.95, 0.95)]
    custom_cmap = make_colormap(custom_colors)
    custom_cmap.set_bad(color='black')
    return custom_cmap

def get_title(nxs_files):
    f = h5py.File(nxs_files, 'r')
    title = f["entry0/sample_description"][0].decode('UTF-8')
    f.close()
    return title
    
if __name__=='__main__':
    numargs = len(sys.argv) -1
    if numargs == 0 or "-help" in sys.argv or "-h" in sys.argv:
        print("Usage: nxsfolder [saveto] [...]")
        print("Possible Parameters: None")
        sys.exit()

    data_folder_path = sys.argv[1]
    
    if numargs > 1:
        saveto = sys.argv[2]
    else:
        saveto = "ShowFirstImageOfFiles.mp4"
        
    nxs_files = sorted(glob.glob(data_folder_path+"/*.nxs"))
    
    N_files = len(nxs_files)
    if N_files == 0:
        sys.exit("No .nxs in folder " + data_folder_path)
    
    nxs_data = open_nexus(nxs_files[0])
    nxs_title = get_title(nxs_files[0])
    cmap = get_custom_cmap()
    fig = plt.figure()
    ax1 = plt.subplot2grid((1,1),(0, 0))
    #Plot NRM
    Nx, Ny = nxs_data.shape
    x_axis = np.arange(Nx)*pixel_size_x - beam_center_x
    y_axis = np.arange(Ny)*pixel_size_y - beam_center_y
    x_axis, y_axis = axis_to_qyqz(x_axis, y_axis)
    xlabel = "$ \mathit{q_x} \, / \, \AA^{-1}$"
    ylabel = "$ \mathit{q_z} \, / \, \AA^{-1}$"

#    ax1.set_xlim([0,Nx])
#    ax1.set_ylim([0,Ny])
    pcm_nrm = ax1.pcolormesh(x_axis, y_axis, nxs_data.T,\
                    norm=mcolors.LogNorm(), cmap=cmap)
    divider3 = make_axes_locatable(ax1)
    cax = divider3.append_axes("right", size="5%", pad=0.05)
    cbar = fig.colorbar(pcm_nrm, cax=cax)
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    ax1.set_title(nxs_title)
#    ax1.set_xticks([])
#    ax1.set_yticks([])
    
    ax1.set_aspect('equal')
    fig.tight_layout()

    print("Creating video file...")
    fps = 3
    FFMpegWriter = manimation.writers['ffmpeg']
    writer = FFMpegWriter(fps=fps)#, codec="libx264")#, extra_args=["-")
    
    with writer.saving(fig, saveto, 500):
        for t in range(N_files):
            nxs_data = open_nexus(nxs_files[t])
            nxs_title = get_title(nxs_files[t])
            #ang_data = get_ang_data(nxs_files[t].split("nrm.edf")[0] + "ang.edf")
            ax1.set_title(nxs_title)
            pcm_nrm.set_array(nxs_data.T[:-1, :-1].ravel())
            writer.grab_frame()
            print("{:.0f}".format((t+1)/N_files*100.), " % \r", end='')
    print("\nSaved video to: " + saveto)
