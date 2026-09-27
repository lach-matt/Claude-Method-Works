#!/usr/bin/env python3
"""
D67 re-derivation for arXiv:1608.05687v3 (Gao, Jafferis, Wall), eq. (3.18).

What is checked, and only this:
 (1) SYMBOLIC (sympy): the prefactor of (3.18) follows from the appendix result (A.10)
     times -4 h Delta C0, with C0 = r_h^(2D-2) sin(D pi)/(2 (2^D pi)^2) (2pi/beta)^(2-2D),
     beta = 2 pi l^2/r_h, l = 1   (sec. 3, below (3.5); sec. 2 below (2.1)).
 (2) SYMBOLIC+NUMERIC: identity (A.14), Gauss's second summation theorem at z = 1/2.
 (3) NUMERIC: the closed form (A.10) K(D,U0) against a direct numerical evaluation of the
     triple integral in the second line of (A.9)
        K = int_{U0}^inf dU1 int_{U1}^inf dU int_1^{U/U1} dy/sqrt(y^2-1)
            (D+1) U1^(D+1) / [ (U-U1 y)^D (U U1 + y)^(D+2) ].
     This tests the appendix's chain of hypergeometric identities (A.9)->(A.10) end to end.
 (4) NUMERIC: sign of (3.18) on a grid 0 < D < 1, and the D -> 0 limit (paper: 'exactly zero').
 (5) NUMERIC: the tree's traversal-window numbers (amortize.py:26-31) from GJW's
     Delta t ~ R ln(R/(h L_planck)) (GJW sec. 5), h = 1, L_planck = 1.616255e-35 m (CODATA 2018 = 2022).
NOT checked: the 1-loop two-point function (2.9) itself, the regularity choice of footnote 4
(the authors say the construction 'is very tricky' and not included), the linearised
Einstein equation (1.3)-(1.5), the flat-space discussion (sec. 5), which is prose, not a computation.
"""
import math, sys
import sympy as sp
import mpmath as mp
from scipy.integrate import quad

ok_all = True
def chk(name, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + detail if detail else ""))

# ---------- (1) prefactor of (3.18) from (A.10) ----------
D, h, rh, U0 = sp.symbols('Delta h r_h U_0', positive=True)
beta = 2*sp.pi/rh
C0 = rh**(2*D-2)*sp.sin(D*sp.pi)/(2*(2**D*sp.pi)**2)*(2*sp.pi/beta)**(2-2*D)
C0 = sp.simplify(C0)
K_pref = sp.pi*sp.gamma(1-D)*sp.gamma(2*D+1)**2/(2**(2*D+2)*(D+sp.Rational(1,2))*sp.gamma(D+1)**3)
lhs = -4*h*D*C0*K_pref
rhs = -h*sp.gamma(2*D+1)**2/(2**(4*D)*(2*D+1)*sp.gamma(D)**2*sp.gamma(D+1)**2)
# use reflection Gamma(1-D) sin(pi D) = pi/Gamma(D)
ratio = sp.simplify(sp.gammasimp((lhs/rhs).rewrite(sp.gamma)))
num_ratios = [float((lhs/rhs).subs({D: d, h: 1, rh: 1.7})) for d in (0.1, 0.37, 0.5, 0.83)]
chk("(1) -4hDC0*(A.10 prefactor) == (3.18) prefactor", all(abs(r-1) < 1e-12 for r in num_ratios),
    f"sympy ratio -> {ratio}; numeric ratios {num_ratios}")
chk("(1b) C0 is independent of r_h (only via 2pi/beta = r_h/l^2)", sp.simplify(sp.diff(C0, rh)) == 0,
    f"C0 = {C0}")

# ---------- (2) (A.14) ----------
bad = []
for d in (0.05, 0.3, 0.5, 0.77, 0.95):
    a = mp.hyp2f1(2*d+1, 2*d+1, 1.5+2*d, 0.5)
    b = mp.sqrt(mp.pi)*mp.gamma(1.5+2*d)/mp.gamma(1+d)**2
    if abs(a/b-1) > 1e-12: bad.append((d, a, b))
chk("(2) (A.14) 2F1(2D+1,2D+1;3/2+2D;1/2) = sqrt(pi)Gamma(3/2+2D)/Gamma(1+D)^2", not bad, str(bad))

# ---------- (3) (A.10) closed form against direct triple integral (A.9) ----------
def K_closed(d, u0):
    return float(mp.pi*mp.gamma(1-d)*mp.gamma(2*d+1)**2/(2**(2*d+2)*(d+0.5)*mp.gamma(d+1)**3)
                 * mp.hyp2f1(0.5+d, 0.5-d, 1.5+d, 1/(1+u0**2))/(1+u0**2)**(d+0.5))

def K_direct(d, u0):
    def inner(U, U1):           # y = cosh(tau)  -> dy/sqrt(y^2-1) = dtau
        tmax = math.acosh(U/U1)
        # U - U1 cosh t = 2 U1 sinh((tmax+t)/2) sinh((tmax-t)/2); factor out (tmax-t)^(-d) exactly
        def shc(x):
            return 0.5 if x == 0 else math.sinh(x/2)/x
        def g(t):
            reg = 2*U1*math.sinh((tmax+t)/2)*shc(tmax-t)      # (U-U1 cosh t)/(tmax-t) > 0
            return reg**(-d) * (U*U1 + math.cosh(t))**(-d-2)
        if tmax == 0.0:
            return 0.0
        v, _ = quad(g, 0.0, tmax, weight='alg', wvar=(0.0, -d), limit=200, epsabs=0, epsrel=1e-10)
        return v
    def middle(U1):             # U = U1/s, s in (0,1)
        f = lambda s: inner(U1/s, U1) * U1/s**2 if s < 1 else 0.0
        v, _ = quad(f, 0.0, 1.0, limit=200, epsabs=0, epsrel=1e-8)
        return (d+1) * U1**(d+1) * v
    f = lambda t: middle(u0/t) * u0/t**2 if t > 0 else 0.0   # U1 = u0/t
    v, _ = quad(f, 0.0, 1.0, limit=100, epsabs=0, epsrel=1e-6)
    return v

for d, u0 in ((0.2, 1.0), (0.4, 1.0), (0.6, 2.0), (0.8, 1.0)):
    kc, kd = K_closed(d, u0), K_direct(d, u0)
    chk(f"(3) (A.10) closed form = (A.9) triple integral at Delta={d}, U0={u0}",
        abs(kd/kc - 1) < 2e-4, f"closed {kc:.8g}  direct {kd:.8g}  rel {kd/kc-1:+.2e}")

# ---------- (4) sign of (3.18) on (0,1) and Delta -> 0 ----------
def ane(d, u0, hh=1.0, l=1.0):
    return float(-hh*mp.gamma(2*d+1)**2/(2**(4*d)*(2*d+1)*mp.gamma(d)**2*mp.gamma(d+1)**2*l)
                 * mp.hyp2f1(0.5+d, 0.5-d, 1.5+d, 1/(1+u0**2))/(1+u0**2)**(d+0.5))
grid = [i/100 for i in range(1, 100)]
neg = all(ane(d, u0) < 0 for d in grid for u0 in (0.1, 1.0, 2.0, 10.0))
chk("(4) (3.18) < 0 for all Delta in (0,1), U0 in {0.1,1,2,10}, h>0", neg)
chk("(4b) (3.18) -> 0 as Delta -> 0", abs(ane(1e-8, 1.0)) < 1e-7, f"{ane(1e-8,1.0):.3e}")
mono = all(abs(ane(d, 1.0)) > abs(ane(d, 2.0)) for d in grid)
chk("(4c) earlier turn-on (U0=1) gives larger |ANE| than U0=2 (paper: 'the earlier we turn on ... the larger')", mono)
# the turn-on/turn-off case is the difference (paper, below (3.18)); check it stays negative for U0=1,Uf=2
chk("(4d) U0=1, Uf=2: ANE(1)-ANE(2) < 0 on grid", all(ane(d,1.0)-ane(d,2.0) < 0 for d in grid))
print("     sample ANE(U0=1): ", {d: round(ane(d, 1.0), 6) for d in (0.1, 0.25, 0.5, 0.75, 0.9)})

# ---------- (5) the tree's window numbers ----------
C = 299792458.0; LP = 1.616255e-35
for R, want in ((1.0, 2.672e-7), (1e3, 2.903e-4), (1e6, 3.133e-1)):
    w = R*math.log(R/LP)/C
    chk(f"(5) amortize.py window R={R:g} m: R ln(R/l_P)/c", abs(w/want-1) < 2e-3, f"{w:.4e} s vs tree {want:.3e}")

print("\nALL PASS" if ok_all else "\nSOME FAIL")
sys.exit(0 if ok_all else 1)
