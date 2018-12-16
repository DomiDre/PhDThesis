import fabio
import matplotlib
from matplotlib import pyplot as plt
import numpy as np

wavelength = 1.033202
pixelsize = 0.172 #mm
sdd = 2907.08 #mm
beam_center_y = 324.5
beam_center_z = 62.09


left_point = (-0.057, .038)
right_point = (0.111, 0.0398)
qz_val = 0.038
width = 0.002

edf_file_path = "./ES-S14_pos02_.tif"

slope = 0#(right_point[1] - left_point[1])/(right_point[0] - left_point[0])
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
        return matplotlib.colors.LinearSegmentedColormap('CustomMap', cdict)
    #Nice Coloring:
    c = matplotlib.colors.ColorConverter().to_rgb
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

def axis_to_qyqz(y, z):
    k0 = 2*np.pi/wavelength
    psi = np.arctan((y-beam_center_y)*pixelsize/sdd)
    theta = np.arctan((z-beam_center_z)*pixelsize/sdd)
    qy = k0*np.sin(psi)
    qz = k0*np.sin(theta)
    return qy, qz

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

data_file = fabio.open(edf_file_path)
header = data_file.header
data = data_file.data

x_axis = np.arange(data.shape[0])
y_axis = np.arange(data.shape[1])


qy, qz = axis_to_qyqz(x_axis, y_axis)

idx_width = get_idx(qz, qz_val + width/2.) - get_idx(qz, qz_val - width/2.)

yoneda_data = []
for ix, xval in enumerate(qy):
    y_low = qz_val - width/2. + slope*xval
    y_idx_low = get_idx(qz, y_low)
    yoneda_data.append(np.sum(data[ix, y_idx_low:y_idx_low+idx_width]))
yoneda_data = np.asarray(yoneda_data)

background_line = np.sum(data[:, -10:-10+idx_width], axis=1)
print(background_line)
bg_est = np.mean(background_line)
sbg_est = np.std(background_line, ddof=1)
print(bg_est)
print(sbg_est)
headerstring = "Extracted data from " + edf_file_path + "\n"+\
               "Projected data from qz = "+str(qz_val)+" with width " + str(width)+"\n"+\
               "Background estimate: " + str(bg_est) + " +/- " + str(sbg_est) +"\n"+\
               "q_y / A-1 \t I / Counts"
valid_data = yoneda_data > 0
qy_save = qy[valid_data]
yoneda_save = yoneda_data[valid_data]
np.savetxt("yoneda_line.xy",\
    np.c_[qy_save, yoneda_save],\
    header=headerstring)
fig, ax = plt.subplots()
im = ax.pcolormesh(qy, qz, data.T,
                norm=matplotlib.colors.LogNorm(),
                cmap=get_custom_cmap(),
                vmin=50, vmax=1e5)
#cb = plt.colorbar(im)
#cb.set_label(r'Intensity (a. u.)')
ax.plot(qy[qy>0], slope*qy[qy>0] + qz_val - width/2., lw=1, color='white',\
                ls='-', marker='None', alpha=1)
ax.plot(qy[qy>0], slope*qy[qy>0] + qz_val + width/2., lw=1, color='white',\
                ls='-', marker='None', alpha=1)

ax.set_xlabel(r'$\mathit{q_y} \, / \, \AA^{-1}$')
ax.set_ylabel(r'$\mathit{q_z} \, / \, \AA^{-1}$')
#ax.set_xlim([min(qy), max(qy)])
#ax.set_ylim([min(qz), max(qz)])
ax.set_xlim([-0.1, 0.22])
ax.set_ylim([0., 0.32])
ax.set_aspect('equal')
ax.text(0.21, 0.31, "GISAXS @ BM26B", color='white',\
            verticalalignment='top', horizontalalignment='right')
#fig.tight_layout()
plt.savefig("ES-S14_gisaxs.png")
plt.show()
