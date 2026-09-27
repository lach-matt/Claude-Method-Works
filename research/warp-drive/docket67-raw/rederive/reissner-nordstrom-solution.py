#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the Reissner-Nordstrom facts the warp board uses.

Independent of the board: nothing here imports research/warp-drive.  sympy + z3.
Every check prints PASS/FAIL; exit 1 on any FAIL.

Conventions: G = c = 1, Gaussian EM (T_ab = (1/4pi)(F_ac F_b^c - g_ab F^2/4)),
signature (-,+,+,+), metric ds^2 = -f dt^2 + dr^2/f + r^2 dOmega^2,
f = 1 - 2M/r + Q^2/r^2 (Reissner 1916, Nordstrom 1918, as restated in
arXiv:2608.16534 eq. (38)).  Misner-Sharp: m = (r/2)(1 - g^{ab} d_a r d_b r)
(Hayward gr-qc/9408002 eq. (4)).
"""
import sys
from fractions import Fraction as Fr
import sympy as sp
import z3

FAILS = []


def chk(name, ok):
    ok = bool(ok)
    print(("PASS " if ok else "FAIL ") + name)
    if not ok:
        FAILS.append(name)


t, r, th, ph = sp.symbols('t r theta phi')
M, Q = sp.symbols('M Q', positive=True)
X = [t, r, th, ph]
f = 1 - 2 * M / r + Q ** 2 / r ** 2
g = sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(th) ** 2)
gi = g.inv()

# ---- 1. Einstein tensor, mixed components --------------------------------
Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                     - sp.diff(g[b, c], X[d])) for d in range(4)) / 2)
         for c in range(4)] for b in range(4)] for a in range(4)]


def Ric(b, c):
    return sp.simplify(sum(sp.diff(Gam[a][b][c], X[a]) - sp.diff(Gam[a][b][a], X[c])
                           + sum(Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
                                 for d in range(4)) for a in range(4)))


Rdd = sp.Matrix(4, 4, lambda b, c: Ric(b, c))
Rs = sp.simplify(sum(gi[a, b] * Rdd[a, b] for a in range(4) for b in range(4)))
Gmix = sp.simplify(gi * Rdd - sp.eye(4) * Rs / 2)   # G^a_b

# ---- 2. Maxwell field of a charge Q: A = -Q/r dt  -> F_tr = -Q/r^2 ----------
A = [Q / r, 0, 0, 0]   # sign irrelevant for T; F_rt = dA_t/dr
F = sp.Matrix(4, 4, lambda a, b: sp.diff(A[b], X[a]) - sp.diff(A[a], X[b]))
Fup = gi * F * gi
F2 = sp.simplify(sum(F[a, b] * Fup[a, b] for a in range(4) for b in range(4)))
Tdd = sp.Matrix(4, 4, lambda a, b: sp.simplify(
    (sum(F[a, c] * F[b, d] * gi[c, d] for c in range(4) for d in range(4))
     - g[a, b] * F2 / 4) / (4 * sp.pi)))
Tmix = sp.simplify(gi * Tdd)
chk("Einstein-Maxwell: G^a_b - 8 pi T^a_b == 0 for all a,b (r > 0)",
    sp.simplify(Gmix - 8 * sp.pi * Tmix) == sp.zeros(4, 4))
sqrtg = r ** 2 * sp.sin(th)
chk("source-free Maxwell d_a(sqrt(-g) F^{ab}) == 0 for r > 0",
    all(sp.simplify(sum(sp.diff(sqrtg * Fup[a, b], X[a]) for a in range(4))) == 0
        for b in range(4)))

rho = sp.simplify(-Tmix[0, 0])
p_r = sp.simplify(Tmix[1, 1])
p_t = sp.simplify(Tmix[2, 2])
chk("rho = -T^t_t = Q^2/(8 pi r^4)", sp.simplify(rho - Q ** 2 / (8 * sp.pi * r ** 4)) == 0)
chk("p_r = -rho", sp.simplify(p_r + rho) == 0)
chk("p_t = +rho", sp.simplify(p_t - rho) == 0)
chk("traceless: -rho + p_r + 2 p_t == 0", sp.simplify(-rho + p_r + 2 * p_t) == 0)

# ---- 3. Misner-Sharp mass --------------------------------------------------
m = sp.simplify(r / 2 * (1 - gi[1, 1]))
chk("Misner-Sharp m = (r/2)(1 - g^rr) = M - Q^2/(2r)", sp.simplify(m - (M - Q ** 2 / (2 * r))) == 0)
chk("dm/dr = 4 pi r^2 rho", sp.simplify(sp.diff(m, r) - 4 * sp.pi * r ** 2 * rho) == 0)
chk("m zero at r = Q^2/(2M) only", sp.solve(sp.Eq(m, 0), r) == [Q ** 2 / (2 * M)])
chk("lim_{r->0+} m = -oo", sp.limit(m, r, 0, '+') == -sp.oo)
eps, R = sp.symbols('epsilon R', positive=True)
Eint = sp.integrate(4 * sp.pi * r ** 2 * rho, (r, eps, R))
chk("int_eps^R 4 pi r^2 rho = Q^2/(2 eps) - Q^2/(2R) -> +oo as eps -> 0",
    sp.simplify(Eint - (Q ** 2 / (2 * eps) - Q ** 2 / (2 * R))) == 0
    and sp.limit(Eint, eps, 0, '+') == sp.oo)
chk("m(R) - 4 pi R^3 p_r(R) == M exactly (tolman V13)",
    sp.simplify(m - 4 * sp.pi * r ** 3 * p_r - M) == 0)
chk("lim r^3 p_r = -oo at centre (tolman 389-393)", sp.limit(r ** 3 * p_r, r, 0, '+') == -sp.oo)

# regular centre (Hayward p.4): g^{-1}(dr,dr) - 1 = O(r^2).  Here it is -2M/r + Q^2/r^2.
chk("centre is NOT regular: (g^rr - 1)/r^2 unbounded as r->0+",
    sp.limit((gi[1, 1] - 1) / r ** 2, r, 0, '+') == sp.oo)

# ---- 4. Energy conditions (DEC): rho >= |p_i| holds with equality ------------
rp = sp.Symbol('rp', positive=True)   # r > 0 made explicit so |.| simplifies
chk("DEC holds pointwise: rho - |p_r| = 0, rho - |p_t| = 0, rho > 0 (r > 0)",
    sp.simplify((rho - sp.Abs(p_r)).subs(r, rp)) == 0
    and sp.simplify((rho - sp.Abs(p_t)).subs(r, rp)) == 0
    and sp.ask(sp.Q.positive(rho.subs(r, rp))))

# ---- 5. z3: region and staticity ------------------------------------------
Rz, Mz, Qz, mz, fz = z3.Reals('R M Q m f')
base = [Rz > 0, Mz > 0, Qz > 0, mz == Mz - Qz * Qz / (2 * Rz), fz == 1 - 2 * mz / Rz]


def proved(name, hyps, goal):
    s = z3.Solver()
    s.add(*hyps)
    s.add(z3.Not(goal))
    res = s.check()
    chk(name + "  [z3: negation %s]" % res, res == z3.unsat)


def satis(name, hyps):
    s = z3.Solver()
    s.add(*hyps)
    res = s.check()
    chk(name + "  [z3: %s]" % res, res == z3.sat)


satis("vacuity guard: RN with m < 0 is satisfiable", base + [mz < 0])
proved("E1: m < 0 <=> 2 M R < Q^2", base, (mz < 0) == (2 * Mz * Rz < Qz * Qz))
proved("where m < 0, f = 1 - 2m/R > 1 > 0: the region is STATIC (Killing d_t timelike) for EVERY Q, incl. Q > M",
       base + [mz < 0], fz > 1)
# r_- >= Q^2/(2M) when Q <= M:  r_- = Q^2/(M + s), s = sqrt(M^2 - Q^2) in [0, M]
s_ = z3.Real('s')
proved("Q <= M: r_- = Q^2/(M+s) >= Q^2/(2M), equality iff Q = 0 (so region is inside inner horizon)",
       [Mz > 0, Qz > 0, Qz <= Mz, s_ >= 0, s_ * s_ == Mz * Mz - Qz * Qz],
       Qz * Qz / (Mz + s_) > Qz * Qz / (2 * Mz))
y = sp.symbols('y', positive=True)
ser = sp.series(1 - sp.sqrt(1 - y) - y / 2, y, 0, 4).removeO()
chk("r_-/M - (Q^2/2M)/M = y^2/8 + y^3/16 + O(y^4), y = Q^2/M^2 (tolman 460-465)",
    sp.simplify(ser - (y ** 2 / 8 + y ** 3 / 16)) == 0)

# ---- 6. uniqueness of u = K/r^4 given tracelessness, u + p_r = 0, conservation
u = sp.Function('u')
sol = sp.dsolve(sp.Eq(sp.diff(-u(r), r) + 2 / r * (-u(r) - u(r)), 0), u(r))
chk("traceless + p_r = -u + static conservation => u = C/r^4 (tolman 389-393)",
    sp.simplify(sol.rhs * r ** 4).free_symbols <= {sp.Symbol('C1')})

# ---- 7. the board's numerical instances, exact -----------------------------
def inst(Mv, Q2v):
    zero = Q2v / (2 * Mv)
    disc = Mv * Mv - Q2v
    return zero, disc


z, d = inst(Fr(1), Fr(16, 25))
chk("M = 1, Q = 0.8: m = 0 at R = 8/25 = 0.32", z == Fr(8, 25))
chk("M = 1, Q = 0.8: horizons 1 +- sqrt(9/25) = 0.4, 1.6", d == Fr(9, 25))
m_row = lambda R_: Fr(1) - Fr(16, 25) / (2 * R_)
chk("M = 1, Q = 0.8: m(0.1) = -11/5 < 0, m(0.32) = 0, m(1) = 17/25 > 0",
    m_row(Fr(1, 10)) == Fr(-11, 5) and m_row(Fr(8, 25)) == 0 and m_row(Fr(1)) == Fr(17, 25))
z2, d2 = inst(Fr(7, 3), Fr(9, 16))
chk("M = 7/3, Q^2 = 9/16: zero at 27/224, M^2 - Q^2 = 703/144 > 0", z2 == Fr(27, 224) and d2 == Fr(703, 144))
chk("M = 0 limit: m = -Q^2/(2R) < 0 at every R > 0 with rho > 0",
    sp.simplify(m.subs(M, 0) + Q ** 2 / (2 * r)) == 0)

# ---- 8. units: Heaviside-Lorentz form (G = c = 1, eps0 = 1) ----------------
# f_HL = 1 - 2M/r + Q^2/(4 pi r^2): the Gaussian Q^2 is Q_HL^2/(4 pi).  Same qualitative result.
m_HL = M - Q ** 2 / (8 * sp.pi * r)
chk("Heaviside-Lorentz: zero moves to Q^2/(8 pi M) = (Gaussian Q^2 := Q^2/4pi)/(2M); sign structure unchanged",
    sp.solve(sp.Eq(m_HL, 0), r) == [Q ** 2 / (8 * sp.pi * M)])

# ---- 9. the one physical datum: r_c for an electron -----------------------
# r_c = Q^2/(2M) geometric -> e^2/(4 pi eps0 * 2 m_e c^2) = r_e/2.  CODATA 2022 (arXiv:2409.03787, Table XXXIII)
e = 1.602176634e-19; eps0 = 8.8541878188e-12; me = 9.1093837139e-31; c = 299792458.0
re_codata = 2.8179403205e-15
re_calc = e ** 2 / (4 * 3.141592653589793 * eps0 * me * c ** 2)
chk("r_e from CODATA 2022 e, eps0, m_e, c agrees with tabulated r_e to 1e-9 rel",
    abs(re_calc / re_codata - 1) < 1e-9)
print("     electron r_c = r_e/2 = %.10e m" % (re_codata / 2))
G = 6.67430e-11; hbar = 1.054571817e-34
QoverM = e / (4 * 3.141592653589793 * eps0 * G) ** 0.5 / me
lamC = hbar / (me * c)
print("     electron Q/M (geometric) = %.4e  -> Q > M: no horizon, naked singularity" % QoverM)
print("     reduced Compton wavelength / r_c = %.1f  (classical Maxwell not valid at r_c)" % (lamC / (re_codata / 2)))
chk("electron: Q/M > 1e21 and lambda_C/r_c = 2/alpha ~ 274 (CODATA 2022 G, hbar)",
    QoverM > 1e21 and abs(lamC / (re_codata / 2) - 2 * 137.035999177) < 1e-3)

print("\n%d FAIL(s)" % len(FAILS))
sys.exit(1 if FAILS else 0)
