import h5py, sys, os.path
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker as ticker

class GisansD33():
    def __init__(self, transpose=False):
        self.__version__ = 0.2
        
        self.transpose = transpose
        self.pixelsize_x = 5 # mm
        self.pixelsize_y = 2.5 # mm
        if transpose:
            self.pixelsize_x, self.pixelsize_y = self.pixelsize_y, self.pixelsize_x
        self.beamcenter_x = 315 # mm
        self.beamcenter_y = 315 # mm
        self.wavelength = 6 # Angstrom
        self.sdd = 2500 # mm
        
        self.data = None

        self.scale_to_time = True
        self.log = ""
        self.temperature = None
        self.temperature_p = None
        self.temperature_m = None
        self.loaded_file = False
        self.loaded_plusminus = False
        self.cmap = self.get_custom_cmap()
    
    def printlog(self, message):
        self.log += "#" + message + "\n"
        print(message)
        
### Load Data Methods
    def open_nexus_file(self, nexus_file):
        if not os.path.isfile(nexus_file):
            sys.exit("Could not find file: " + nexus_file)
        data_list = []
        param_dict = {}
        print("Reading " + nexus_file)
        f = h5py.File(nexus_file, 'r')
        for i in range(1,6):
            data_list.append(f["entry0/data"+str(i)+"/MultiDetector"+\
                               str(i)+"_linear_data"][:,:,0])

        param_dict["duration"] = f["entry0/duration"][0]
        param_dict["monitor"] = f["entry0/monitor1/data"][0,0,0]
        param_dict["temperature"] = f["entry0/sample/temperature"][0]
        param_dict["electromag"] = f["entry0/sample/pselectromag_actual_current"][0]
        f.close()
        return data_list, param_dict

    def calc_q(self, x, y):
        k0 = 2*np.pi/self.wavelength
        tthf = np.arctan(x/self.sdd)
        aiaf = np.arctan(y/self.sdd)
        qy = k0*np.sin(tthf)
        qz = k0*np.sin(aiaf)
        return qy, qz
        
    def load_file(self, nexus_file, detector_num=1):
        data_list, param_dict = self.open_nexus_file(nexus_file)
        
        self.data = data_list[detector_num-1]
        if self.transpose:
            self.data = self.data.T[:,::-1]
        self.temperature = param_dict["temperature"]
        self.data_list = data_list
        self.param_dict = param_dict
        if self.scale_to_time:
            self.monitor = param_dict['duration']
        else:
            self.monitor = param_dict['monitor']

        self.Nx, self.Ny = self.data.shape
        self.x = np.arange(self.Nx)*self.pixelsize_y - self.beamcenter_y
        self.y = np.arange(self.Ny)*self.pixelsize_x - self.beamcenter_x
        self.qy, self.qz = self.calc_q(self.x, self.y)
        self.loaded_file = True
    
    def load_file_range(self, nexus_file_prefix, nexus_file_range,\
                              nexus_file_suffix='.nxs'):
        for range_string in nexus_file_range:
            datafile = nexus_file_prefix+str(range_string)+nexus_file_suffix
            if self.data is not None:
                prev_data = np.copy(self.data)
                prev_monitor = np.copy(self.monitor)
            else:
                prev_data = 0
                prev_monitor = 0
            self.load_file(datafile)
            self.data += prev_data
            self.monitor += prev_monitor


    def load_plusminus(self, nexus_file_plus, nexus_file_minus):
        data_list, param_dict = self.open_nexus_file(nexus_file_plus)
        self.data_p = data_list[0].T
        self.temperature_p = param_dict["temperature"]
        self.datalist_p = data_list
        self.param_dict_p = param_dict

        data_list, param_dict = self.open_nexus_file(nexus_file_minus)
        self.data_m = data_list[0].T
        self.temperature_m = param_dict["temperature"]
        self.datalist_m = data_list
        self.param_dict_m = param_dict

        self.Nx, self.Ny = self.data_p.shape
        self.x = np.arange(self.Nx)*self.pixelsize_y - self.beamcenter_y
        self.y = np.arange(self.Ny)*self.pixelsize_x - self.beamcenter_x
        self.qy, self.qz = self.calc_q(self.x, self.y)

        self.data_sum = self.data_p + self.data_m
        self.data_diff = self.data_p - self.data_m
        self.loaded_plusminus = True
        
    def add_plusminus(self, nexus_file_plus, nexus_file_minus):
        data_list, param_dict = self.open_nexus_file(nexus_file_plus)
        self.data_p += data_list[0].T
        self.param_dict_p["monitor"] += param_dict["monitor"]
        if not (self.temperature_p == param_dict["temperature"]):
            print("WARNING: Adding plus files but temperatures do not match:")
            print("T_previous: "+str(self.temperature_p)+" K")
            print("T_addend: "+str(param_dict["temperature"])+" K")
        self.addend_datalist_p = data_list
        self.addend_param_dict_p = param_dict

        data_list, param_dict = self.open_nexus_file(nexus_file_minus)
        self.data_m += data_list[0].T
        self.param_dict_m["monitor"] += param_dict["monitor"]
        if not (self.temperature_m == param_dict["temperature"]):
            print("WARNING: Adding minus files but temperatures do not match:")
            print("T_previous: "+str(self.temperature_m)+" K")
            print("T_addend: "+str(param_dict["temperature"])+" K")
        self.addend_datalist_m = data_list
        self.addend_param_dict_m = param_dict

        self.data_sum = self.data_p + self.data_m
        self.data_diff = self.data_p - self.data_m

    def divide_by_monitor(self):
        if self.loaded_file:
            self.data = self.data/self.param_dict["monitor"]
        if self.loaded_plusminus:
            self.data_p = self.data_p / self.param_dict_p["monitor"]
            self.data_m = self.data_m / self.param_dict_m["monitor"]
                        
            self.data_sum = self.data_p + self.data_m
            self.data_diff = self.data_p - self.data_m
            
### Plotting Methods
    def plot(self, x, y, data, vmin=None, vmax=None, logscale=True):
        self.fig, self.ax = plt.subplots()
        if logscale:
            pcm = self.ax.pcolormesh(x, y, data.T, cmap=self.cmap,\
                        norm=mcolors.LogNorm(), vmin=vmin, vmax=vmax)
        else:
            pcm = self.ax.pcolormesh(x, y, data.T, cmap=self.cmap,\
                        vmin=vmin, vmax=vmax)
        self.ax.set_xlabel("$ \mathit{x}$")
        self.ax.set_ylabel("$ \mathit{y}$")
        self.ax.set_xlim([min(x), max(x)])
        self.ax.set_ylim([min(y), max(y)])
        self.ax.set_aspect('equal')
        divider3 = make_axes_locatable(self.ax)
        self.cax = divider3.append_axes("right", size="10%", pad=0.05)

        if logscale:
            self.cbar = plt.colorbar(pcm, cax=self.cax)
        else:
            def fmt(x, pos):
                a, b = '{:.0e}'.format(x).split('e')
                b = int(b)
                return r'${} \cdot 10^{{{}}}$'.format(a, b)
            self.cbar = plt.colorbar(pcm, cax=self.cax,\
                        format=ticker.FuncFormatter(fmt))
        self.fig.tight_layout()

    def plot_in_xy(self, vmin=None, vmax=None):
        self.plot(self.x, self.y, self.data, vmin=vmin, vmax=vmax)
        self.ax.set_xlabel("$ \mathit{x} \, / \, mm$")
        self.ax.set_ylabel("$ \mathit{y} \, / \, mm$")

    def plot_in_q(self, vmin=None, vmax=None):
        self.plot(self.qy, self.qz, self.data, vmin=vmin, vmax=vmax)
        self.ax.set_xlabel("$ \mathit{q_y} \, / \, \AA^{-1}$")
        self.ax.set_ylabel("$ \mathit{q_z} \, / \, \AA^{-1}$")

    def plot_sum_in_q(self, vmin=None, vmax=None):
        self.plot(self.qy, self.qz, self.data_sum, vmin=vmin, vmax=vmax)
        self.ax.set_xlabel("$ \mathit{q_y} \, / \, \AA^{-1}$")
        self.ax.set_ylabel("$ \mathit{q_z} \, / \, \AA^{-1}$")

    def plot_diff_in_q(self, vmin=None, vmax=None):
        self.plot(self.qy, self.qz, self.data_diff, vmin=vmin, vmax=vmax,\
                            logscale=False)
        self.ax.set_xlabel("$ \mathit{q_y} \, / \, \AA^{-1}$")
        self.ax.set_ylabel("$ \mathit{q_z} \, / \, \AA^{-1}$")

    def show(self):
        plt.show()

    def get_qyz_data(self):
        return self.qy, self.qz, self.data
    
    def get_monitor(self):
        return self.monitor
### Help Methods
    def get_idx(self, array, value):
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
    
    def get_custom_cmap(self):
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
