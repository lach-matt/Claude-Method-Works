#!/usr/bin/env python3
# Toroidal Hamiltonian constraint, source-first.
#   lap psi = -2 pi psi^5 rho ,  axisymmetric in (x,s), lap = d2x + d2s + (1/s) ds
# Picard outer loop; inner linear solve by RED-BLACK Gauss-Seidel with SOR,
# which unlike the all-at-once Jacobi update is stable for omega up to 2.
import numpy as np, sys
G, c = 6.67430e-11, 299792458.0
R0, A, M = 15.0, 5.0, 4.4886e27
L, N = 30.0, 241
x = np.linspace(-L, L, N); s = np.linspace(0.0, L, N)
dx = x[1]-x[0]; ds = s[1]-s[0]
X, S = np.meshgrid(x, s, indexing='ij')
d = np.sqrt((S-R0)**2 + X**2)
w = 0.5*(1.0-np.tanh((d-A)/0.8))
vol = 2.0*np.pi*np.sum(w*S)*dx*ds
rho = (M/vol)*w
f = -2.0*np.pi*rho*G/c**2
mg = M*G/c**2
r = np.sqrt(X**2+S**2); bc = 1.0 + mg/(2.0*np.maximum(r, 0.5))
psi = bc.copy()
Sax = np.maximum(S, ds*0.5)
ax = 1.0/dx**2; a1 = 1.0/ds**2
ap = a1 + 1.0/(2*ds*Sax)          # coefficient of psi[:, j+1]
am = a1 - 1.0/(2*ds*Sax)          # coefficient of psi[:, j-1]
den = 2.0*ax + 2.0*a1
I, J = np.meshgrid(np.arange(N), np.arange(N), indexing='ij')
red = ((I+J) % 2 == 0); black = ~red
interior = np.zeros((N,N), bool); interior[1:-1,1:-1] = True
OM = 1.85
def sweep(mask, rhs):
    nb = (np.roll(psi,1,0)+np.roll(psi,-1,0))*ax + np.roll(psi,-1,1)*ap + np.roll(psi,1,1)*am
    tgt = (nb - rhs)/den
    m = mask & interior
    psi[m] = psi[m] + OM*(tgt[m]-psi[m])
def resid():
    nb = (np.roll(psi,1,0)+np.roll(psi,-1,0))*ax + np.roll(psi,-1,1)*ap + np.roll(psi,1,1)*am
    return (nb - den*psi) - f*psi**5
for outer in range(80):
    rhs = f*psi**5
    for k in range(300):
        sweep(red, rhs); sweep(black, rhs)
        psi[0,:]=bc[0,:]; psi[-1,:]=bc[-1,:]; psi[:,-1]=bc[:,-1]; psi[:,0]=psi[:,1]
    R = np.max(np.abs(resid()[2:-2,2:-2]))
    if not np.all(np.isfinite(psi)):
        print("DIVERGED outer", outer, file=sys.stderr); sys.exit(1)
    if R < 1e-17: break
print("psi %.9f .. %.9f  residual %.3e  outers %d" % (psi.min(), psi.max(), R, outer), file=sys.stderr)
print("rho_max %.4e kg/m^3  vol %.4e m^3  r_s/R0 %.4f" % (rho.max(), vol, 2*mg/R0), file=sys.stderr)
np.savetxt("psi.dat", psi, fmt="%.12e")
np.savetxt("grid.dat", np.array([-L, L, 0.0, L, float(N)]), fmt="%.12e")
