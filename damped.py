import numpy as np 
import matplotlib.pyplot as plt 
import scienceplots
import scipy as sp
from scipy.integrate import quad
from scipy.integrate import dblquad
from scipy.integrate import odeint
plt.style.use(['science', 'notebook', 'grid'])
fig, axes = plt.subplots(1, 2, figsize = (10,5))
def dSdt(S,t):
    omega, theta = S 
    return [-9.81*np.sin(theta) -0.5* omega, omega]
t = np.linspace(0, 20, 1000)
theta0 = np.pi /3 
omega0 = 0
S0 = (omega0, theta0)
sol = odeint(dSdt, S0, t)
ax = axes[0]
ax.set_title("Vận tốc góc [rad/s]")

ax.plot(t, sol.T[0], c = 'r')



ax = axes[1]
ax.set_title("Li độ góc [rad]")
ax.plot(t, sol.T[1])



plt.show()
