import math
from fractions import Fraction as Fr
from math import factorial as f
print("  THE HYDROGENIC RADIAL INTEGRALS, EXACTLY\n")
print("      R_nl(r) = N r^l L(r) e^(−Zr/n) with L a Laguerre polynomial.")
print("      every Slater integral over two such is a finite rational in")
print("      n, n', l, l' times a power of Z. computing them directly.\n")
def Rnl_coeffs(n,l,Z=1):
    """R_nl(r) = sum_j c_j r^(l+j) e^(-Zr/n); returns [(c_j, power)]"""
    # R = N (2Zr/n)^l e^(-Zr/n) L^{2l+1}_{n-l-1}(2Zr/n)
    N=math.sqrt((2*Z/n)**3 * f(n-l-1)/(2*n*f(n+l)))
    a=2*Z/n
    out=[]
    for j in range(n-l):
        # generalised Laguerre coefficient
        c=((-1)**j)*f(n+l)/(f(n-l-1-j)*f(2*l+1+j)*f(j))
        out.append((N*(a**l)*c*(a**j), l+j))
    return out
def slater(k,n1,l1,n2,l2,Z=1,NR=4000,RMAX=None):
    """R^k(n1l1,n2l2) = ∫∫ r_<^k/r_>^(k+1) R1(r1)^2 R2(r2)^2 r1^2 r2^2"""
    if RMAX is None: RMAX=40*max(n1,n2)**2/Z
    r=np.linspace(1e-6,RMAX,NR); dr=r[1]-r[0]
    def R(n,l):
        cs=Rnl_coeffs(n,l,Z)
        v=np.zeros_like(r)
        for c,p in cs: v+=c*r**p
        return v*np.exp(-Z*r/n)
    A=R(n1,l1)**2*r**2; B=R(n2,l2)**2*r**2
    # cumulative inner integral
    cA=np.cumsum(A*r**k)*dr                       # ∫_0^r A s^k ds
    tA=np.cumsum((A/r**(k+1))[::-1])[::-1]*dr     # ∫_r^∞ A s^-(k+1) ds
    val=np.sum(B*(cA/r**(k+1) + tA*r**k))*dr
    return val
import numpy as np
print("  CHECK — normalisation of the radial functions\n")
for n,l in ((1,0),(2,0),(3,2),(4,0),(4,2)):
    r=np.linspace(1e-6,60*n*n,6000); dr=r[1]-r[0]
    cs=Rnl_coeffs(n,l); v=np.zeros_like(r)
    for c,p in cs: v+=c*r**p
    v*=np.exp(-r/n)
    print(f"      ∫R²r²dr for {n}{'spdfg'[l]} = {np.sum(v*v*r*r)*dr:.6f}")
print()
print("  THE RATIO G^ℓ / F⁰  FOR EACH LADDER'S PAIR  (hydrogenic, Z = 1)\n")
print(f"      {'pair':>8}{'F⁰':>12}{'G^ℓ':>12}{'G/F':>12}{'×1/(2ℓ+1)':>13}")
P=[(4,0,3,2),(5,0,4,2),(6,0,5,2),(7,0,6,2)]
OUT=[]
for n1,l1,n2,l2 in P:
    F0=slater(0,n1,l1,n2,l2)
    Gk=slater(l2,n1,l1,n2,l2)
    ang=1/(2*l2+1)
    print(f"      {f'{n1}s/{n2}d':>8}{F0:>12.6f}{Gk:>12.6f}{Gk/F0:>12.6f}"
          f"{Gk/F0*ang:>13.6f}")
    OUT.append((n1,Gk/F0))
print()
print("  AND AGAINST THE CROSSING CHARGES\n")
CC={4:2,5:2,6:2,7:3}
print(f"      {'pair':>8}{'G/F':>12}{'crosses at c':>14}")
for (n1,r),(n1b,l1,n2,l2) in zip(OUT,P):
    print(f"      {f'{n1}s/{n2}d':>8}{r:>12.6f}{CC[n1]:>14}")
