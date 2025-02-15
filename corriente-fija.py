import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.odr import *

data_location = '/content/Voltajes y corrientes.xlsx'

column_names = pd.read_excel(data_location, sheet_name='Corriente fija', skiprows=1, nrows=1, usecols=range(1,10))
err_names = pd.read_excel(data_location, sheet_name='Errores C fijo', usecols=range(0,11), nrows=1)

df = pd.read_excel(data_location, header=None, names=column_names, skiprows=2, nrows=11, usecols=range(1,10), sheet_name='Corriente fija')
uncertainty_sheet = pd.read_excel(data_location, header=None, names=err_names, usecols=range(0,11), skiprows=1, nrows=11, sheet_name='Errores C fijo')


## El eje de las absisas representará el cuadrado del campo magnético.
## El eje de las ordenadas será una función del radio de color azul que provoca el haz de electrones a su paso.

avg_radius = (df['Radio izq. [cm]'] + df['Radio der. [cm]']) / 200

magnetic_field = df['Corriente [A]'] * 0.00077929

volRadius = df['Voltaje [V]']

x = magnetic_field**2 * avg_radius**2
y = 2 * df['Voltaje [V]']
sx = uncertainty_sheet['Err (BR)^2']
sy = uncertainty_sheet['Err 2V']

## Fitting
def function(B, x):
    return x * B[0] + B[1]

linear = Model(function)
mydata = RealData(x, y, sx=sx, sy=sy)
myodr = ODR(mydata, linear, beta0=[10**11., 0])

myoutput = myodr.run()
slope, intersect = myoutput.beta

f_x = np.arange(np.amin(x),np.amax(x), (np.amax(x)-np.amin(x))/100)
f_y = slope * f_x + intersect

myoutput.pprint()

# Plot
fig, ax = plt.subplots()

ax.set(xlabel=r'$B^2$ $R^2$ $[T^2 m^2]$', ylabel = r'$2V$ $[V]$', title=r'1,74(9) $A$ fija')

ax.errorbar(x, y, xerr=sx, yerr=sy, fmt='o', capsize=3, color='k', elinewidth=1) ## Puntos
ax.plot(f_x,f_y, color='mediumvioletred') ## Función

fig.autofmt_xdate()

plt.show()
