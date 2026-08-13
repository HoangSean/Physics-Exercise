#Giải PT Schrodinger bằng PP số, bài toán infinite square well
import numpy as np 
import matplotlib.pyplot as plt 
import scipy as sp 
from scipy.integrate import quad 
from matplotlib.animation import FuncAnimation 
import scienceplots 
plt.style.use(['science', 'notebook', 'grid'])

a = 2
N=1000
x = np.linspace(0, a, N)
V = 0
dx = np.diff(x)[0]
main_diag = -2*np.ones(N)
off_diag = np.ones(N-1)
H =  -(np.diag(main_diag) + np.diag(off_diag, -1) + np.diag(off_diag, 1))/(2*dx**2)


E_n, psi_n = np.linalg.eigh(H)

for n in range(5):
    Psi = psi_n[:, n] * 2 / np.sqrt(sum(np.ravel(psi_n[:, n]**2)) * dx) + E_n[n]

    line, = plt.plot(x, Psi, label=f'$E_{n} = {E_n[n]:.1f}$')
    plt.axhline(
        E_n[n],
        linestyle='--',
        linewidth=1.5,
        color=line.get_color()
    )
    plt.axvline(x=2, linestyle ='--', c = 'gray')
    plt.legend(loc = 'upper right', fontsize = '15')
    plt.ylim(-3, 35)
    plt.xlim(0, 2.5)
    plt.title("5 mức năng lượng đầu trong giếng thế")
    plt.xlabel("Vị trí [m]")
    plt.ylabel("Năng lượng")


plt.show()


