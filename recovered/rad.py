# rad.py -- one-electron radial eigenvalues, Numerov on a log mesh with node-count bisection.
# x = ln r, u = e^{x/2} y:  y'' = q(x) y,  q = (l+1/2)^2 + 2 r^2 (V(r) - E).
import numpy as np

def _shoot(q, h, l):
    n = len(q); y = np.zeros(n)
    y[0] = 1e-30; y[1] = y[0]*np.exp((l+0.5)*h)   # y ~ r^{l+1/2} near origin
    f = 1 - h*h*q/12.0
    nodes = 0
    for i in range(1, n-1):
        y[i+1] = ((12 - 10*f[i])*y[i] - f[i-1]*y[i-1])/f[i+1]
        if y[i+1]*y[i] < 0: nodes += 1
        if abs(y[i+1]) > 1e200: y[:i+2] /= 1e200
    return y, nodes

def eigen(V, l, n, zeta, Z, npts=6000):
    rmin, rmax = 1e-5/Z, max(80.0, 4.0*n*n/zeta)
    x = np.linspace(np.log(rmin), np.log(rmax), npts); h = x[1]-x[0]; r = np.exp(x)
    base = (l+0.5)**2 + 2*r*r*V(r)
    target = n - l - 1
    Elo, Ehi = -0.6*Z*Z/(l+1)**2 - 1.0, -1e-9
    for _ in range(200):
        E = 0.5*(Elo+Ehi)
        y, nd = _shoot(base - 2*r*r*E, h, l)
        if nd > target or (nd == target and y[-1]*(-1)**target < 0): Ehi = E
        else: Elo = E
        if Ehi - Elo < 1e-11*abs(E) + 1e-13: break
    return 0.5*(Elo+Ehi)

def defect(V, l, n, zeta, Z, **kw):
    E = eigen(V, l, n, zeta, Z, **kw)
    return n - zeta/np.sqrt(-2*E), E

if __name__ == "__main__":
    Vh = lambda r: -1.0/r
    for l in (0, 1, 2):
        print("H l=%d " % l, " ".join("%d:%+.6f" % (n, defect(Vh, l, n, 1.0, 1)[0]) for n in range(l+1, l+6)))