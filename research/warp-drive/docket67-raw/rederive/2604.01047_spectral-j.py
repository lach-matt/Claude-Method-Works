#!/usr/bin/env python3
"""DOCKET 67 re-derivation: GMMPS (arXiv 2604.01047v1) spectral density rho(M) (4.5)
and its Stieltjes transform J(z) (4.17), as linstab.py uses them.

Independent of linstab.py (nothing imported from the tree).  Checks:
 C1  (4.5) = (3.13)/M  and  Thm 1.1 kernel:  rho = sqrt(1-4m^2/M)/(16 pi^2 M) >= 0 on M >= 4m^2
 C2  J(0) = INT rho/M dM = 1/(96 pi^2 m^2)   (sympy, exact)
 C3  lim_{z->0} of printed (4.17) = 1/(96 pi^2 m^2), from BOTH sides (z->0+ and z->0-)
 C4  printed (4.17), principal branches, against the defining integral:
       real z in (-200, 4m^2) (both signs), incl. Im part of the closed form on the real axis;
       complex z in all four quadrants, incl. Re z > 4m^2 with small |Im z| (domain D (4.18))
 C5  printed (4.17) at z = -w^2 against Prop. 4.5's printed L(K) closed form (asinh / log form)
 C6  J strictly increasing on real z < 4m^2 (J' = INT rho/(M-z)^2 > 0) -- numeric grid
 C7  linstab's bracket bound for g < 0 (m = 1): 4 J(0)/(4+|g|) <= J(g) <= J(0)
       z3: for M >= 4, g <= 0 : 4/(4-g) <= M/(M-g) <= 1   (the pointwise step)
       numeric: the bound on a grid
 C8  Lemma 4.13's A''(gamma) integrand identity:
       d^2/dg^2 [(a1-g)(a2-g)/(M-g)] = 2 (M-a1)(M-a2)/(M-g)^3   (sympy)
 C10 normalisation of (3.13) against AMM gr-qc/0209075 (B37a,b), independently derived there
 C9  Lemma 4.13's endpoint limit A'(4m^2-) = +inf needs a_i < 4m^2 strictly; at a1=a2=4m^2
       (the TT value a = 4m^2 of 5.2) A'(4m^2-) is FINITE -- numeric (scoping note only)
Exit 0 iff every assertion passes.
"""
import sys
import sympy as sp
import mpmath as mp

ok = True


def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


# ---------------------------------------------------------------- C1, C2
m, M = sp.symbols('m M', positive=True)
varrho = sp.sqrt(1 - 4 * m**2 / M) / (16 * sp.pi**2)          # (3.13), M >= 4m^2
rho = sp.sqrt(1 - 4 * m**2 / M) / (16 * sp.pi**2 * M)          # (4.5)
chk("C1 (4.5) rho == (3.13) varrho / M  [(3.12): K0 = Box INT varrho/M G_ret]",
    sp.simplify(rho - varrho / M) == 0)
u = sp.symbols('u', positive=True)
# rho >= 0 on M >= 4m^2: write M = 4m^2 (1+u), u >= 0
rho_u = sp.simplify(rho.subs(M, 4 * m**2 * (1 + u)))
chk("C1 rho >= 0 on M >= 4m^2 (sympy sign on M = 4m^2(1+u), u > 0)", sp.ask(sp.Q.nonnegative(rho_u),
    sp.Q.positive(u) & sp.Q.positive(m)) is not False and rho_u.is_nonnegative is not False)
J0 = sp.simplify(sp.integrate(rho / M, (M, 4 * m**2, sp.oo)))
print("   J(0) =", J0)
chk("C2 J(0) = 1/(96 pi^2 m^2) from the (4.5) integral", sp.simplify(J0 - 1 / (96 * sp.pi**2 * m**2)) == 0)

# ---------------------------------------------------------------- C3 (printed 4.17)
z = sp.symbols('z')
J417 = (1 / (8 * sp.pi**2)) * (1 / z - (4 * m**2 - z) * m * sp.acsc(2 * m / sp.sqrt(z))
                               / (m * sp.sqrt(4 * m**2 - z) * z**sp.Rational(3, 2)))
Lp = sp.simplify(sp.limit(J417.subs(m, 1), z, 0, '+'))
Lm = sp.simplify(sp.limit(J417.subs(m, 1), z, 0, '-'))
print("   lim z->0+ =", Lp, "  lim z->0- =", Lm)
chk("C3 lim_{z->0+} (4.17) = 1/(96 pi^2) (m=1)", sp.simplify(Lp - 1 / (96 * sp.pi**2)) == 0)
chk("C3 lim_{z->0-} (4.17) = 1/(96 pi^2) (m=1)", sp.simplify(Lm - 1 / (96 * sp.pi**2)) == 0)

# ---------------------------------------------------------------- C4
mp.mp.dps = 40


def J_int(zv, mm=1):
    f = lambda Mv: mp.sqrt(1 - 4 * mm**2 / Mv) / (16 * mp.pi**2 * Mv) / (Mv - zv)
    pts = [4 * mm**2, 4 * mm**2 + 1, 8 * mm**2]
    zr = mp.re(zv)
    if zr > 4 * mm**2:
        pts = sorted(set([4 * mm**2, zr - 1 if zr - 1 > 4 * mm**2 else (4 * mm**2 + zr) / 2, zr,
                          zr + 1, 2 * zr + 8]))
    return mp.quad(f, pts + [mp.inf])


def J_417(zv, mm=1):
    zv = mp.mpc(zv)
    return (1 / (8 * mp.pi**2)) * (1 / zv - (4 * mm**2 - zv) * mm * mp.acsc(2 * mm / mp.sqrt(zv))
                                   / (mm * mp.sqrt(4 * mm**2 - zv) * zv**mp.mpf(1.5)))


worst_real, worst_im = mp.mpf(0), mp.mpf(0)
reals = [-200, -50, -10, -5, -1, -0.1, -1e-6, 1e-6, 0.5, 1, 2, 3, 3.9, 3.999]
for zv in reals:
    a, b = J_417(zv), J_int(mp.mpf(zv))
    worst_real = max(worst_real, abs(mp.re(a) - b) / abs(b))
    worst_im = max(worst_im, abs(mp.im(a)) / abs(b))
print("   real axis: max rel |Re(4.17) - integral| = %s ; max |Im(4.17)|/|J| = %s"
      % (mp.nstr(worst_real, 5), mp.nstr(worst_im, 5)))
chk("C4 (4.17) = integral on real z in [-200, 3.999], rel err < 1e-25", worst_real < mp.mpf('1e-25'))
chk("C4 (4.17) is real (Im ~ 0) on real z < 4m^2", worst_im < mp.mpf('1e-25'))
cplx = [1 + 1j, 1 - 1j, -3 + 2j, -3 - 2j, 10j, -10j, 5 + 0.01j, 5 - 0.01j, 20 + 3j, 20 - 3j,
        4 + 1j, -100 + 50j]
worst_c, rows = mp.mpf(0), []
for zv in cplx:
    a, b = J_417(zv), J_int(mp.mpc(zv))
    e = abs(a - b) / abs(b)
    rows.append((zv, e))
    worst_c = max(worst_c, e)
for zv, e in rows:
    print("   z = %-14s rel err (4.17 principal branch vs integral) = %s" % (zv, mp.nstr(e, 4)))
chk("C4 (4.17) = integral on complex z in all quadrants incl. Re z > 4m^2 (domain D), rel err < 1e-20",
    worst_c < mp.mpf('1e-20'))

# ---------------------------------------------------------------- C5 Prop 4.5 L(K) form
worst5 = mp.mpf(0)
for w in [0.01, 0.3, 1, 2, 5, 17, 300]:
    w = mp.mpf(w)
    stuff = (1 / (16 * mp.pi**2)) * (2 * 1 / w**3 * mp.sqrt(4 + w**2) * mp.log(w / 2 + mp.sqrt(1 + w**2 / 4))
                                     - 2 / w**2)
    worst5 = max(worst5, abs(J_417(-w**2) - stuff) / abs(stuff))
print("   Prop 4.5 L(K) closed form vs (4.17) at z = -w^2: max rel diff =", mp.nstr(worst5, 5))
chk("C5 Prop 4.5's printed L(K) = -[(w^2+c) J(-w^2)]^{-1} with J from (4.17) (m=1)", worst5 < mp.mpf('1e-25'))

# ---------------------------------------------------------------- C6 monotone
grid = [mp.mpf(-400) + k * mp.mpf('0.5') for k in range(0, 808)]   # -400 .. 3.5
vals = [mp.re(J_417(g)) for g in grid if g != 0]
chk("C6 J strictly increasing on the grid [-400, 3.5] (m=1)", all(vals[i] < vals[i + 1] for i in range(len(vals) - 1)))
Jp = lambda g: mp.quad(lambda Mv: mp.sqrt(1 - 4 / Mv) / (16 * mp.pi**2 * Mv) / (Mv - g)**2, [4, 8, mp.inf])
chk("C6 J'(g) = INT rho/(M-g)^2 > 0 at g = -100, -1, 0, 3.9", all(Jp(g) > 0 for g in (-100, -1, 0, 3.9)))
# derivative of closed form vs integral at one point
chk("C6 d/dz (4.17) = INT rho/(M-z)^2 at z = -2", abs(mp.diff(lambda t: mp.re(J_417(t)), -2) - Jp(-2)) < mp.mpf('1e-20'))

# ---------------------------------------------------------------- C7 bracket bound
import z3
Mz, gz = z3.Reals('M g')
s = z3.Solver()
s.add(Mz >= 4, gz <= 0, z3.Not(z3.And(4 * (Mz - gz) <= Mz * (4 - gz), Mz <= Mz - gz)))
r = s.check()
chk("C7 z3: M >= 4, g <= 0  =>  4/(4-g) <= M/(M-g) <= 1  (negation unsat)", r == z3.unsat)
s2 = z3.Solver()
s2.add(Mz >= 4, gz > 0, gz < 4, 4 * (Mz - gz) > Mz * (4 - gz))
chk("C7 CONTROL: the lower bound fails for g in (0,4) (sat) -- the guard g < 0 is load-bearing",
    s2.check() == z3.sat)
J00 = 1 / (96 * mp.pi**2)
bad = [g for g in [-1e-8, -0.01, -1, -4, -37, -1e3, -1e6]
       if not (J00 * 4 / (4 + abs(g)) <= mp.re(J_417(g)) <= J00)]
chk("C7 numeric: 4 J(0)/(4+|g|) <= J(g) <= J(0) at g = -1e-8 .. -1e6", not bad)

# ---------------------------------------------------------------- C8 Lemma 4.13 A''
a1, a2, g, Ms = sp.symbols('a1 a2 gamma M')
expr = (a1 - g) * (a2 - g) / (Ms - g)
chk("C8 d^2/dg^2[(a1-g)(a2-g)/(M-g)] = 2(M-a1)(M-a2)/(M-g)^3",
    sp.simplify(sp.diff(expr, g, 2) - 2 * (Ms - a1) * (Ms - a2) / (Ms - g)**3) == 0)

# ---------------------------------------------------------------- C9 scoping note
def Aprime(gv, A1, A2):
    return ((gv - A1) * (gv - A2) * Jp(gv) + (2 * gv - A1 - A2) * mp.re(J_417(gv)))


tt = [Aprime(4 - mp.mpf(10)**(-k), 4, 4) for k in (2, 4, 6, 8)]
st = [Aprime(4 - mp.mpf(10)**(-k), 1, 1) for k in (2, 4, 6, 8)]
print("   A'(4-eps), a1=a2=4 (TT):", [mp.nstr(x, 6) for x in tt])
print("   A'(4-eps), a1=a2=1     :", [mp.nstr(x, 6) for x in st])
chk("C9 at a1=a2=4m^2, A'(4m^2-) stays bounded (Lemma 4.13's '+inf' needs a_i < 4m^2, as Prop 4.12 states)",
    abs(tt[-1] - tt[-2]) < mp.mpf('1e-2') and st[-1] > 100 * st[0])

# ---------------------------------------------------------------- C10 independent normalisation
# AMM gr-qc/0209075 (B37a,b), READ: rho_T(s) = th/(60 pi^2) sqrt(1-4m^2/s) (s/4 - m^2)^2,
#   rho_S(s) = th/(24 pi^2) sqrt(1-4m^2/s) (m^2 + (1-6xi) s/2)^2.
# GMMPS (3.11)+(3.12)/(3.13): T = (1/60)(Box-4m^2)^2, S = (2/3)(m^2 + (1/2)(1-6xi)Box)^2 acting on
#   K0 = Box INT varrho/M G_ret, varrho = sqrt(1-4m^2/M)/(16 pi^2).  On the mass shell Box -> M, the
#   sector weights are T(M) varrho(M), S(M) varrho(M).  They must equal AMM's rho_T, rho_S.
xi_ = sp.symbols('xi', real=True)
wT = sp.Rational(1, 60) * (M - 4 * m**2)**2 * varrho
wS = sp.Rational(2, 3) * (m**2 + sp.Rational(1, 2) * (1 - 6 * xi_) * M)**2 * varrho
aT = sp.sqrt(1 - 4 * m**2 / M) / (60 * sp.pi**2) * (M / 4 - m**2)**2
aS = sp.sqrt(1 - 4 * m**2 / M) / (24 * sp.pi**2) * (m**2 + (1 - 6 * xi_) * M / 2)**2
chk("C10 GMMPS T*varrho == AMM (B37a) rho_T (independent normalisation of (3.13)/(4.5))",
    sp.simplify(wT - aT) == 0)
chk("C10 GMMPS S*varrho == AMM (B37b) rho_S", sp.simplify(wS - aS) == 0)

print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
