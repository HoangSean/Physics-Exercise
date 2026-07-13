import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.optimize import minimize
from scipy.optimize import curve_fit
from scipy.integrate import dblquad
import scienceplots

plt.style.use(['science', 'notebook', 'grid'])
fig, ax = plt.subplots(figsize = (12,5))
t = np.linspace(0, 10, 1000)
t_data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
I_data = np.array([102.1, 71.3, 48.9, 36.2, 24.1, 17.8, 11.9, 8.4, 6.2, 4.1, 2.9])
ax.scatter(t_data, I_data, c = 'r',label = "Dữ liệu")
ax.legend()
def decay(t, I0, lmbda):
    return I0 * np.exp(-lmbda*t)
popt, pcov = curve_fit(decay, t_data, I_data, p0=(10,3))
ax.plot(t, popt[0] * np.exp(-popt[1] * t), label = "Lý thuyết")

ax.legend()
plt.xlabel("Thời gian [s]")
plt.ylabel("Độ phóng xạ")
plt.show()





