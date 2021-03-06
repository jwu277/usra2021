### Reproduction of Andre Longtin's stochastic bistable model ###


from util import ito
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def compute_eta(lam, sig, tmax, dt):

    a = lambda t, x: -lam * x
    b = lambda t, x: lam * sig

    return ito.sim(a, b, tmax, dt)


def compute_x(m, w, lam, sig, tmax, dt):

    eta = compute_eta(lam, sig, tmax, dt)

    # Laziness: solve deterministic dynamics as special case of stochastic dyanmics
    a = lambda t, x: x * (1 - x * x) + eta[int(t/dt)] + m * np.sin(w * t)
    b = lambda t, x: 0

    return ito.sim(a, b, tmax, dt)


def compute_isi(x, dt):
    
    zc = []

    for i in range(len(x) - 1):
        # Detect zero-crossing on falling edge
        if x[i] > 0 and x[i+1] < 0:
            zc.append(i * dt)

    return np.diff(zc)


def main():

    # Time in s
    tmax = 200
    w = 500 * np.pi
    tc = 0.1
    lam = 1 / tc
    m = 1.0
    D = 0.1
    sig = np.sqrt(2 * D)

    dt = 0.0001

    x = compute_x(m, w, lam, sig, tmax, dt)
    t = np.arange(len(x)) * dt

    # isi = compute_isi(x, dt)

    plt.plot(t, x)
    # plt.hist(isi, bins=200, range=(0, 0.04))
    plt.xlabel('t (s)')
    plt.ylabel('x')
    plt.show()


if __name__ == "__main__":
    main()

