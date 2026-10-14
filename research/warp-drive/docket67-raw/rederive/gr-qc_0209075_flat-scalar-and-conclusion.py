#!/usr/bin/env python3
"""DOCKET 67 re-derivation: AMM gr-qc/0209075 flat-space scalar sector (4.4),(4.5b),(4.11),
(B37),(B45) and the 'stable on scales >> Planck' conclusion vs its H6 (O(1) fourth-order
coefficients).  Units: hbar = c = 1; G = 1 (Planck units) in section 5.
Inputs taken from the source (text layer drops Greek letters and some minus signs; every
reconstruction is CHECKED here, not assumed):
  (B37b) rho_S(s) = theta(s-4m^2)/(24 pi^2) sqrt(1-4m^2/s) [m^2 + (1-6 xi) s/2]^2
  (B37a) rho_T(s) = theta(s-4m^2)/(60 pi^2) sqrt(1-4m^2/s) (s/4 - m^2)^2
  (4.8)/(B45) F(k^2) = k^2 int_{4m^2}^inf ds rho(s)/(s^3 (s+k^2))
  (4.5b) bracket  B_S = sigma*12 beta k^2 - 1/(4 pi G) + k^2 F_S   (sigma = +-1: the sign of the
         beta term is not legible in the text layer; every conclusion below is sigma-independent)
"""
import sympy as sp, mpmath as mp, sys
mp.mp.dps = 30
ok = True
def check(name, cond, detail=""):
    global ok
    ok &= bool(cond)
    print(("PASS " if cond else "FAIL ") + name + ("  " + detail if detail else ""))

# 1. (4.4): three subtractions at k^2=0 of Pi(k^2)=int rho/(s+k^2) leave -(k^2)^3 int rho/(s^3(s+k^2))
s, x = sp.symbols('s x', positive=True)
lhs = 1/(s+x) - (1/s - x/s**2 + x**2/s**3)
check("(4.4) subtraction identity", sp.simplify(lhs + x**3/(s**3*(s+x))) == 0)
# and the k-independent term vanishes: remainder is O(x^3) -> (4.5b) carries overall k^2 and no constant
check("(4.4) remainder is O((k^2)^3): no k-independent term", sp.simplify(sp.limit(lhs/x**3, x, 0) + 1/s**4) == 0)

# 2. large-s coefficient of rho/s^2 = coefficient of the log in (4.9),(4.11)
m, xi = sp.symbols('m xi', positive=True)
rhoS = sp.sqrt(1-4*m**2/s)/(24*sp.pi**2)*(m**2+(1-6*xi)*s/2)**2
rhoT = sp.sqrt(1-4*m**2/s)/(60*sp.pi**2)*(s/4-m**2)**2
CS = sp.limit(rhoS/s**2, s, sp.oo); CT = sp.limit(rhoT/s**2, s, sp.oo)
check("(4.11) log coefficient (1-6xi)^2/(96 pi^2)", sp.simplify(CS-(1-6*xi)**2/(96*sp.pi**2)) == 0, str(CS))
check("(4.9) log coefficient 1/(960 pi^2)", sp.simplify(CT-1/(960*sp.pi**2)) == 0, str(CT))
check("(B38) conformal xi=1/6: rho_S = m^4/(24pi^2) sqrt(...)", sp.simplify(rhoS.subs(xi, sp.Rational(1,6)) - m**4*sp.sqrt(1-4*m**2/s)/(24*sp.pi**2)) == 0)
check("positivity of rho_S, rho_T above threshold (squares x sqrt)", True, "manifest from (B37)")

# numeric F from the spectral integral (k^2>0: real)
def Fnum(rho, k2, mm=1.0, xv=0.0):
    f = lambda ss: rho(ss, mm, xv)/(ss**3*(ss+k2))
    return k2*mp.quad(f, [4*mm**2, 40*mm**2, 4e3*mm**2, mp.inf])
rS = lambda ss, mm, xv: mp.sqrt(1-4*mm**2/ss)/(24*mp.pi**2)*(mm**2+(1-6*xv)*ss/2)**2
rT = lambda ss, mm, xv: mp.sqrt(1-4*mm**2/ss)/(60*mp.pi**2)*(ss/4-mm**2)**2
def ffun(k2, mm=1.0):  # (B43): f = z log((z+1)/(z-1)), z = sqrt(1+4m^2/k^2), k^2>0
    z = mp.sqrt(1+4*mm**2/k2); return z*mp.log((z+1)/(z-1))

# 3. (B44) closed form vs spectral integral
worst = 0
for k2 in [0.1, 1.0, 7.0, 100.0, 1e4]:
    xx = 1.0/k2
    closed = (mp.mpf(-46)/15 - mp.mpf(56)/3*xx - 32*xx**2 + (1+4*xx)**2*ffun(k2))/(960*mp.pi**2)
    worst = max(worst, abs(closed/Fnum(rT, k2) - 1))
check("(B44) F_T closed form = spectral integral", worst < 1e-12, "max rel dev %.2e" % worst)

# 4. (B45): fit F_S*96pi^2 = a0 + a1(1-6xi) + a2 m^2/k^2 + [(1-6xi) + b m^2/k^2]^2(-2+f)
#    over sample points, then compare |a0|=1/15, |a1|=2/3, |a2|=2/3, |b|=2 (printed magnitudes)
pts = [(k2, xv) for k2 in [0.3, 2.0, 11.0, 150.0] for xv in [0.0, 0.1, 0.3, -0.2]]
def resid(a0, a1, a2, b):
    out = []
    for k2, xv in pts:
        q = 1-6*xv; xx = 1/k2
        model = a0 + a1*q + a2*xx + (q + b*xx)**2*(-2+ffun(k2))
        out.append(model - 96*mp.pi**2*Fnum(rS, k2, 1.0, xv))
    return out
best = None
for sa0 in (1, -1):
    for sa1 in (1, -1):
        for sa2 in (1, -1):
            for sb in (1, -1):
                r = resid(sa0*mp.mpf(1)/15, sa1*mp.mpf(2)/3, sa2*mp.mpf(2)/3, sb*2)
                e = max(abs(v) for v in r)
                if best is None or e < best[0]: best = (e, sa0, sa1, sa2, sb)
e, sa0, sa1, sa2, sb = best
check("(B45) printed magnitudes reproduce F_S for one sign assignment", e < 1e-12,
      "signs (a0,a1,a2,b)=(%+d,%+d,%+d,%+d)  max abs dev %.1e" % (sa0, sa1, sa2, sb, e))
B45_SIGNS = (sa0, sa1, sa2, sb)
def FS_closed(k2, xv, mm=1.0, fval=None):
    q = 1-6*xv; xx = mm**2/k2; fv = ffun(k2, mm) if fval is None else fval
    return (sa0*mp.mpf(1)/15 + sa1*mp.mpf(2)/3*q + sa2*mp.mpf(2)/3*xx + (q+sb*2*xx)**2*(-2+fv))/(96*mp.pi**2)

# asymptotic (4.11): F_S - C ln(k^2/m^2) -> const
d1 = FS_closed(mp.mpf(1e10), 0) - (1/(96*mp.pi**2))*mp.log(1e10)
d2 = FS_closed(mp.mpf(1e14), 0) - (1/(96*mp.pi**2))*mp.log(1e14)
check("(4.11) Re F_S ~ (1-6xi)^2/(96pi^2) ln(k^2/m^2)", abs(d1-d2) < 1e-10, "offset const %.6f" % d1)

# 5. The conclusion and H6.  Planck units G = 1; m in Planck units.
mp.mp.dps = 120
G = mp.mpf(1)
def smallest_root(beta_eff, N=1, xv=0.0, mm=mp.mpf('1e-19')):
    """smallest k^2>0 (tachyonic side, imaginary frequency) with
       1 - 48 pi G beta_eff k^2 - 4 pi G N k^2 F_S(k^2) = 0  (beta_eff = sigma*beta)."""
    g = lambda lk: 1 - 48*mp.pi*G*beta_eff*mp.e**lk - 4*mp.pi*G*N*mp.e**lk*FS_closed(mp.e**lk, xv, mm)
    lo = mp.log(mp.mpf("1e-70")); hi = mp.log(mp.mpf(1e6))
    grid = [lo + (hi-lo)*i/6000 for i in range(6001)]
    for a, b in zip(grid, grid[1:]):
        if g(a)*g(b) < 0:
            ga = g(a)
            for _ in range(200):
                c = (a+b)/2; gc = g(c)
                if ga*gc <= 0: b = c
                else: a, ga = c, gc
            return mp.e**((a+b)/2)
    return None
print("\n-- scalar-sector root on the growing side (k^2>0), Planck units, m = 1e-19 M_P --")
rows = []
for beta in [0, 1, 1e3, 1e9, 1e58]:
    r = smallest_root(mp.mpf(beta))
    lam = 1/mp.sqrt(r) if r else None
    rows.append((beta, r, lam))
    print("  sigma*beta = %-8g  k^2 G = %-12s  4piG k^2 = %-12s  length/l_P = %s" %
          (beta, mp.nstr(r, 4), mp.nstr(4*mp.pi*r, 4), mp.nstr(lam, 4)))
r0 = rows[0][1]; r1 = rows[1][1]; r9 = rows[3][1]
check("beta=0: growing root only at Planck scale (length < 10 l_P)", 1/mp.sqrt(r0) < 10, mp.nstr(1/mp.sqrt(r0), 4))
check("beta=O(1): root at Planck scale (length < 20 l_P)", 1/mp.sqrt(r1) < 20)
check("H6 is load-bearing: beta=1e9 gives a growing mode at length > 1e5 l_P",
      1/mp.sqrt(r9) > 1e5, "length = %s l_P, predicted sqrt(48 pi beta) = %s" %
      (mp.nstr(1/mp.sqrt(r9), 5), mp.nstr(mp.sqrt(48*mp.pi*1e9), 5)))
# opposite sign: the beta-term root moves to k^2 < 0 (timelike): a NEW massive scalar mode,
# M^2 ~ 1/(48 pi G |beta|): stable (real frequency) but new -> AMM's "no new solutions, stable or
# unstable, far from the Planck regime" also needs |beta| not >> 1
Mb = 1/mp.sqrt(48*mp.pi*mp.mpf(1e9))
print("  sigma*beta = -1e9: beta-term root at k^2 = -1/(48 pi G |beta|) -> mass %s M_P (a new mode)" % mp.nstr(Mb, 4))
# N species: root with beta=0 scales like 1/N  (AMM p.7: G^-1, alpha, beta rescaled by N)
rN = smallest_root(mp.mpf(0), N=10**4)
check("species: N=1e4 moves the beta=0 root length by ~sqrt(N)=100",
      60 < (1/mp.sqrt(rN))/(1/mp.sqrt(r0)) < 140, "ratio %s" % mp.nstr((1/mp.sqrt(rN))/(1/mp.sqrt(r0)), 4))

# 6. data: the only bounds on beta are sub-mm Yukawa tests.  In AMM's normalisation a beta-mode
#    has range lambda = sqrt(48 pi G |beta|);  lambda < 0.03 cm (Hoyle 2004, as used by
#    Calmet-Hsu-Reeb 0803.1836 fn 11) gives:
lP = mp.mpf('1.616255e-35')
for lam_m, lab in [(3e-4, "0.03 cm (Hoyle 2004 via 0803.1836)"), (5e-5, "~50 um (later torsion balances; NAMED-NOT-READ)")]:
    print("  |beta| < %s   for lambda < %s" % (mp.nstr((lam_m/lP)**2/(48*mp.pi), 3), lab))
bmax = (mp.mpf(3e-4)/lP)**2/(48*mp.pi)
check("allowed |beta| spans O(1) .. ~1e60: H6 is not fixed by data", 1e59 < bmax < 1e62, mp.nstr(bmax, 3))
print("\nALL PASS" if ok else "\nSOME FAIL"); sys.exit(0 if ok else 1)
