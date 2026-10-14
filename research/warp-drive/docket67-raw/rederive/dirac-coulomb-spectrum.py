#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of the Dirac-Coulomb (Sommerfeld) spectrum as
excite.py uses it (excite.py:962-968, 1601-1605, 1805-1823).

Independent of excite.py: nothing is imported from the tree.

  R1  the formula E = m[1+(Za/(n-|k|+g))^2]^{-1/2}, g = sqrt(k^2-Za^2), IS an
      eigenvalue of the radial Dirac-Coulomb pair in the tree's own sign
      convention (excite.py:1811-1812): exact polynomial x r^g e^{-lam r}
      eigenfunctions for n_r = 0 and n_r = 1, solved as a linear system, the
      determinant evaluated at 60 digits.  CONTROLS: the Klein-Gordon
      (spinless, l in place of |k|) level and a shifted n_r must FAIL.
  R2  the same formula from an independent route: RK4 shooting on the radial
      pair at 1/alpha = 137.035999177 for five states (numeric).
  R3  nonrelativistic expansion equals Suslov 2401.07485 eq (33).
  R4  degree-1 homogeneity in m (the D18 spectrum side): sympy, exact.
  R5  the float check E(2m)/E(m)=2 is an exact binary scaling: it passes for
      ANY function m*f(alpha), including a WRONG spectrum (control).
  R6  domain: g real needs Za < |k|; Z_crit = 1/alpha for |k|=1 under CODATA
      2018 and 2022; n_r = 0 exists only for k < 0.
  R7  alpha datum moved (CODATA 2018 -> 2022): the D18 ratio is unmoved;
      the absolute levels move by a computed amount.
  R8  named-hypothesis size: finite nuclear size breaks the dilation;
      E_nucl^(4) propto m^3 r_N^2 (CODATA 2022 eq 50) -- computed.
"""
import sys
import sympy as sp
import mpmath as mp

mp.mp.dps = 60
ok = True


def chk(label, cond):
    global ok
    ok = ok and bool(cond)
    print("  %-70s %s" % (label, "PASS" if cond else "FAIL"))


def E_formula(m, Za, n, k):
    g = mp.sqrt(k * k - Za * Za)
    return m / mp.sqrt(1 + (Za / (n - abs(k) + g)) ** 2)


# --------------------------------------------------------------- R1
print("R1  exact eigenfunctions in the tree's sign convention")
r = sp.symbols("r", positive=True)


def det_for(Eval, m, Za, k, nr, gam=None):
    """Ansatz G = r^gam e^{-lam r} P(r), F = r^gam e^{-lam r} Q(r), deg nr.
    Tree's pair:  G' + k/r G - (E + m + Za/r) F = 0
                  F' - k/r F + (E - m + Za/r) G = 0
    Return |det| of the coefficient system (0 <=> eigenvalue)."""
    if gam is None:
        gam = sp.sqrt(sp.Integer(k) ** 2 - Za ** 2)
    lam_v = sp.sqrt(m ** 2 - Eval ** 2)
    gs, ls = sp.symbols("gamma_s lambda_s", positive=True)
    gam_v, gam, lam = gam, gs, ls
    a = sp.symbols("a0:%d" % (nr + 1))
    b = sp.symbols("b0:%d" % (nr + 1))
    P = sum(a[i] * r ** i for i in range(nr + 1))
    Q = sum(b[i] * r ** i for i in range(nr + 1))
    G = r ** gam * sp.exp(-lam * r) * P
    F = r ** gam * sp.exp(-lam * r) * Q
    e1 = sp.diff(G, r) + k / r * G - (Eval + m + Za / r) * F
    e2 = sp.diff(F, r) - k / r * F + (Eval - m + Za / r) * G
    pre = r ** (gam - 1) * sp.exp(-lam * r)
    rows = []
    for e in (e1, e2):
        poly = sp.expand(sp.powsimp(sp.expand(e / pre), force=True))
        poly = sp.Poly(poly, r)
        rows += [poly.coeff_monomial(r ** i).subs({gs: gam_v, ls: lam_v})
                 for i in range(nr + 2)]
    unk = list(a) + list(b)
    M = sp.Matrix([[sp.diff(row, u) for u in unk] for row in rows])
    # overdetermined (2nr+4 eqs, 2nr+2 unknowns): nontrivial solution iff
    # rank < 2nr+2; test the smallest singular value numerically at 60 digits
    Mn = mp.matrix([[mp.mpf(sp.N(x, 70)) for x in M.row(i)]
                    for i in range(M.rows)])
    s = mp.svd_r(Mn, compute_uv=False)
    return min(abs(x) for x in s)


m = sp.Integer(1)
Za = sp.Rational(1, 137)          # exact rational stand-in; any Za<1 works
cases = [(1, -1, 0), (2, -2, 0), (3, -3, 0), (2, -1, 1), (2, 1, 1),
         (3, 2, 1), (3, -2, 1)]
for n, k, nr in cases:
    g = sp.sqrt(sp.Integer(k) ** 2 - Za ** 2)
    E = m / sp.sqrt(1 + (Za / (n - abs(k) + g)) ** 2)
    smin = det_for(E, m, Za, k, nr)
    chk("n=%d kappa=%+d (n_r=%d): smallest singular value %.1e" %
        (n, k, nr, smin), smin < mp.mpf("1e-45"))
# at Za = 1/2 (strong field) the formula still solves the pair exactly
Zb = sp.Rational(1, 2)
for n, k, nr in [(1, -1, 0), (2, 1, 1)]:
    g = sp.sqrt(sp.Integer(k) ** 2 - Zb ** 2)
    E = m / sp.sqrt(1 + (Zb / (n - abs(k) + g)) ** 2)
    smin = det_for(E, m, Zb, k, nr)
    chk("Za=1/2 n=%d kappa=%+d: exact eigenvalue (s_min %.1e)" % (n, k, smin),
        smin < mp.mpf("1e-45"))
# CONTROLS that must fail
kg = m / sp.sqrt(1 + (Za / (0 + sp.Rational(1, 2) +
                            sp.sqrt(sp.Rational(1, 4) - Za ** 2))) ** 2)
smin = det_for(kg, m, Za, -1, 0)
chk("CONTROL Klein-Gordon 1s level is NOT a Dirac eigenvalue (s_min %.1e)"
    % smin, smin > mp.mpf("1e-12"))
wrong = m / sp.sqrt(1 + (Za / (1 + sp.sqrt(1 - Za ** 2))) ** 2)   # n_r shifted
smin = det_for(wrong, m, Za, -1, 0)
chk("CONTROL shifted n_r is NOT an n_r=0 eigenvalue (s_min %.1e)" % smin,
    smin > mp.mpf("1e-12"))
# kappa>0 with n_r = 0 (the non-existent 1p1/2): formula returns a number,
# but no normalisable solution exists
g1 = sp.sqrt(1 - Za ** 2)
E1p = m / sp.sqrt(1 + (Za / g1) ** 2)
smin = det_for(E1p, m, Za, +1, 0)
chk("DOMAIN n=1 kappa=+1: formula gives a value but NO eigenfunction "
    "(s_min %.1e)" % smin, smin > mp.mpf("1e-12"))

# --------------------------------------------------------------- R2
print("R2  RK4 shooting on the radial pair, 1/alpha = 137.035999177")
alpha22 = mp.mpf(1) / mp.mpf("137.035999177")
mp.mp.dps = 30


def shoot(E, k, Za, mm=1):
    """Integrate outward from r0 with the regular Frobenius start; return
    G at large r scaled by its envelope (sign change brackets eigenvalue)."""
    g = mp.sqrt(k * k - Za * Za)
    lam = mp.sqrt(mm * mm - E * E)
    # regular start: G = r^g, F = c r^g, c from the 1/r terms of the pair
    c = (g + k) / Za       # from  g G/r + k G/r - Za F/r = 0
    x0, x1, N = mp.mpf("1e-6"), 60 / lam, 12000
    h = (x1 - x0) / N
    y = [x0 ** g, c * x0 ** g]

    def f(x, y):
        G, F = y
        return [-k / x * G + (E + mm + Za / x) * F,
                k / x * F - (E - mm + Za / x) * G]
    x = x0
    for _ in range(N):
        k1 = f(x, y)
        k2 = f(x + h / 2, [y[i] + h / 2 * k1[i] for i in range(2)])
        k3 = f(x + h / 2, [y[i] + h / 2 * k2[i] for i in range(2)])
        k4 = f(x + h, [y[i] + h * k3[i] for i in range(2)])
        y = [y[i] + h / 6 * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i])
             for i in range(2)]
        x += h
        s = abs(y[0]) + abs(y[1])
        if s > 1e20:
            y = [y[0] / s, y[1] / s]
    return y[0]


for n, k in [(1, -1), (2, -1), (2, 1), (2, -2), (3, 2)]:
    Ef = E_formula(1, alpha22, n, k)
    B = 1 - Ef                      # binding in units of m
    lo, hi = Ef - B * mp.mpf("1e-4"), Ef + B * mp.mpf("1e-4")
    slo, shi = shoot(lo, k, alpha22), shoot(hi, k, alpha22)
    chk("n=%d kappa=%+d: sign change of G(r_max) brackets formula E to "
        "1e-4 of binding" % (n, k), slo * shi < 0)
mp.mp.dps = 60

# --------------------------------------------------------------- R3
print("R3  nonrelativistic expansion vs Suslov 2401.07485 eq (33)")
mu, n_, k_ = sp.symbols("mu n kappa", positive=True)
Es = 1 / sp.sqrt(1 + (mu / (n_ - k_ + sp.sqrt(k_ ** 2 - mu ** 2))) ** 2)
ser = sp.series(Es, mu, 0, 6).removeO()
target = 1 - mu ** 2 / (2 * n_ ** 2) - mu ** 4 / (2 * n_ ** 4) * (n_ / k_ -
                                                                 sp.Rational(3, 4))
chk("E/m = 1 - mu^2/2n^2 - mu^4/2n^4 (n/(j+1/2) - 3/4) + O(mu^6), |k|=j+1/2",
    sp.simplify(ser - target) == 0)

# --------------------------------------------------------------- R4
print("R4  degree-1 homogeneity in m (spectrum side of D18)")
M_, lam_ = sp.symbols("m lambda", positive=True)
Ed = M_ * Es
chk("E(lambda m) = lambda E(m) exactly",
    sp.simplify(Ed.subs(M_, lam_ * M_) - lam_ * Ed) == 0)
chk("d ln E / d ln m = 1 exactly", sp.simplify(sp.diff(Ed, M_) * M_ / Ed - 1) == 0)
# the ODE side (independent of excite.py): substitute r = x/m in the pair
x, ee = sp.symbols("x e", real=True)
gf, hf = sp.Function("g"), sp.Function("h")
kap = sp.symbols("kappa", real=True)
Zs = sp.symbols("Za", positive=True)
G, F = gf(M_ * r), hf(M_ * r)
p1 = sp.diff(G, r) + kap / r * G - (M_ * ee + M_ + Zs / r) * F
p2 = sp.diff(F, r) - kap / r * F + (M_ * ee - M_ + Zs / r) * G
for lab, p in (("first", p1), ("second", p2)):
    ex = sp.simplify(p.subs(r, x / M_).doit() / M_)
    chk("radial pair (%s eqn): residual/m is m-free after r = x/m" % lab,
        sp.simplify(sp.diff(ex, M_)) == 0)

# --------------------------------------------------------------- R5
print("R5  the float ratio check is an exact binary scaling")
import math


def good(mm, a, n, kk):
    kk = abs(kk)
    g = math.sqrt(kk * kk - a * a)
    return mm / math.sqrt(1.0 + (a / (n - kk + g)) ** 2)


def bad(mm, a, n, kk):          # a WRONG spectrum: Bohr levels, sign flipped
    return mm * (1.0 + a * a / (2 * n * n))


a18 = 1.0 / 137.035999084
st = [(1, -1), (2, -1), (2, 1), (2, -2), (3, 2)]
rg = [good(2.0, a18, n, kk) / good(1.0, a18, n, kk) for n, kk in st]
rb = [bad(2.0, a18, n, kk) / bad(1.0, a18, n, kk) for n, kk in st]
chk("true spectrum: ratio == 2.0 EXACTLY (not merely to 1e-15)",
    all(v == 2.0 for v in rg))
chk("CONTROL a wrong spectrum m*f(alpha) ALSO gives exactly 2.0 -> the float "
    "check tests linearity in m only", all(v == 2.0 for v in rb))

# --------------------------------------------------------------- R6
print("R6  domain")
for lab, ainv in (("CODATA 2018", "137.035999084"), ("CODATA 2022", "137.035999177")):
    zc = mp.mpf(ainv)
    chk("%s: g real for |k|=1 iff Z < %s -> Z_max integer 137" % (lab, ainv),
        int(mp.floor(zc)) == 137)
chk("Z=1 cases used by excite.py (|k|>=1) are all inside the domain",
    all(1 * a18 < abs(kk) for _n, kk in st))
chk("all five excite.py states have n_r=n-|k|>=0 and n_r=0 only with k<0",
    all((n - abs(kk) > 0) or (n - abs(kk) == 0 and kk < 0) for n, kk in st))

# --------------------------------------------------------------- R7
print("R7  the alpha datum")
a18m = 1 / mp.mpf("137.035999084")
a22m = 1 / mp.mpf("137.035999177")
shift_sig = (mp.mpf("137.035999177") - mp.mpf("137.035999084")) / mp.mpf("0.000000021")
print("      1/alpha 2018 -> 2022: +9.3e-8 = %.2f x u(2022)" % shift_sig)
for n, k in st:
    r18 = E_formula(2, a18m, n, k) / E_formula(1, a18m, n, k)
    r22 = E_formula(2, a22m, n, k) / E_formula(1, a22m, n, k)
    B18, B22 = 1 - E_formula(1, a18m, n, k), 1 - E_formula(1, a22m, n, k)
    chk("n=%d k=%+d: E(2m)/E(m) = 2 under both (|r-2| < 1e-55); binding moves "
        "rel %.2e" % (n, k, float((B22 - B18) / B18)),
        abs(r18 - 2) < mp.mpf("1e-55") and abs(r22 - 2) < mp.mpf("1e-55"))

# --------------------------------------------------------------- R8
print("R8  size of the dropped-by-name physics under the dilation")
# CODATA 2022 eq (50): E4 = (2/3) m (Za)^4/n^3 (m_r/m)^3 (r_N / lambda_C)^2,
# lambda_C = hbar/(m c) -> E4 propto m^3 r_N^2 at fixed r_N.
rp = mp.mpf("0.84075e-15")         # CODATA 2022 r_p (m), value not load-bearing
lamC = mp.mpf("3.8615926744e-13")  # hbar/(m_e c), m
E4 = mp.mpf(2) / 3 * a22m ** 4 * (rp / lamC) ** 2      # units of m_e c^2, n=1
Eb = 1 - E_formula(1, a22m, 1, -1)
print("      1S: E_nucl^(4)/E_bind = %.2e  (point-nucleus model omits it)" % (E4 / Eb))
eps = mp.mpf("0.01")
# under m -> m(1+eps), E_bind scales (1+eps); E4 scales (1+eps)^3
drel = (E4 * (1 + eps) ** 3 + Eb * (1 + eps)) / ((E4 + Eb) * (1 + eps)) - 1
print("      eps=1e-2 -> 1S binding/m moves (relative, beyond the dilation) by %.2e with a "
      "fixed-radius nucleus" % drel)
chk("finite nuclear size breaks the exact dilation (nonzero shift)", drel != 0)
chk("... but at a level ~1e-11 for eps=1e-2 in hydrogen", abs(drel) < 1e-10)

print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
