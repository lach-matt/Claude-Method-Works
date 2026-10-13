"""cheb() from cheb_tail.py"""
import numpy as np
def cheb(v):          # nodal values at x_j = (1 - cos(pi j/N))/2, j = 0..N  ->  Chebyshev coefficients
    N = len(v) - 1; j = np.arange(N + 1); c = np.zeros(N + 1)
    w = np.ones(N + 1); w[0] = w[-1] = 0.5
    for k in range(N + 1):
        c[k] = (2.0 / N) * np.sum(w * v * np.cos(np.pi * k * j / N)) * (0.5 if k in (0, N) else 1.0)
    return np.abs(c)
