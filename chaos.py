import numpy as np 
import matplotlib.pyplot as plt 
import scienceplots
import scipy as sp 
from scipy.optimize import curve_fit
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from matplotlib.animation import PillowWriter
import os


def dSdt(S,t):
    x,y,z =S 
    return [10*(y-x), x*(28-z)- y, x*y - 8*z/3]
t = np.linspace(0, 50, 5000)
S0 = (1,1,1)
sol = odeint(dSdt, S0, t)
x_sol = sol.T[0]
y_sol = sol.T[1]
z_sol = sol.T[2]


fig,ax = plt.subplots(figsize=(8, 8) ,subplot_kw = {'projection':'3d'})

ax.plot(x_sol, y_sol, z_sol, lw=0.75, color='crimson', label="Quỹ đạo Lorenz")
ax.view_init(elev = 10, azim = 3)
def animate(i):
    ax.view_init(elev = 10, azim = 3*i)
    return fig,
ani = animation.FuncAnimation(fig, animate, frames = 120, interval = 50)

writer = PillowWriter(fps=24)
ani.save('butter.gif', writer=writer, dpi=100)



plt.legend()
plt.show()