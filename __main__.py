from netCDF4 import Dataset
import functools
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

# Importing data from NetCDF
fh1 = Dataset('output1.nc')

# Get relevant parameters from NetCDF
x = fh1.variables['x'][:]
y = fh1.variables['y'][:]
time = fh1.variables['time'][:]
energy_time = fh1.variables['energy_time'][:]
electrons = fh1.variables['electrons'][:]

# Defining blob as electron density at time 0
blob1 = electrons[0][:][:]
blob2 = electrons[50][:][:]
blob3 = electrons[100][:][:]
blob4 = electrons[200][:][:]
blob = np.array(blob1 + blob2 + blob3 + blob4)

# Printing the choosen times in "real values"
print(time[0], time[50], time[100], time[200])

# Adding color bar to density plot
fig, ax = plt.subplots()

# Interpolation between points
f = interpolate.interp2d(x, y, blob, kind='cubic')

Xnew = np.linspace(0, 179, 1000)
Ynew = np.linspace(0, 179, 1000)

test = f(Xnew, Ynew)

cax = plt.pcolormesh(Xnew, Ynew, test, cmap='twilight')
plt.xlabel(r'x $[\rho_s]$', fontsize=14)
plt.ylabel(r'y $[\rho_s]$', fontsize=14)

# Defining variables for plot of color bar
mini = round(blob.min(), 3)
maxi = round(blob.max(), 3)
gen = round((mini + maxi)/2, 3)

# Add color bar, make sure to specify tick locations to match desired ticklabels
cbar = fig.colorbar(cax, ticks=[0, gen, 0.5])
cbar.set_label(r'Electron density, $n$', rotation=270)
cbar.ax.set_yticklabels([0, gen, 0.5])  # vertically oriented color bar

# Save figure
# fig.savefig('blob.eps')

plt.show()




