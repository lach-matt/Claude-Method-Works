#!/usr/bin/env python3
r"""
DOCKET 67 -- audit of Kuo & Ford gr-qc/9304008 v1, Eq. (2.16).
Independent of research/warp-drive/fluctuation.py (no import, no shared code).

Source text (arXiv v1 PDF text layer, cached at d67/src/casmag/all/gr-qc_9304008v1.txt,
md5 f1a6628604751cf61b2a4bd411b00153, harvested from earlier alphaXiv tool results):

  (2.11) T_mn[g,h] = (d_m g)(d_n h) - 1/2 eta_mn (d_s g)(d^s h)
  (2.12) T[f,f]   = -K e^{2 i th}     (2.13) T[f*,f] = T[f,f*] = K     (2.14) T[f*,f*] = -K e^{-2 i th}
         th = k_r x^r,  K_ab = (k_a k_b - 1/2 eta_ab k^2)/(2 w L^3)
  (2.15) |Psi> = (|0> + eps|2>)/sqrt(1+eps^2), eps real
  (2.16) <:T_ab:> = eps/(1+eps^2) { sqrt2 (T[f,f]+T[f*,f*]) + 2 eps (T[f,f*]+T[f*,f]) }   [middle]
                  = K_ab eps/(1+eps^2) (2 eps - sqrt2 cos 2th)                               [final]

Checks:
  C1  (2.12)-(2.14) re-derived from (2.11) for a massless box plane wave f = e^{i k.x}/sqrt(2 w L^3)
  C2  <Psi|:T00:|Psi> from exact Fock matrices (first principles)
  C3  KF's own general-state formula (2.10) evaluated at c0, c2  (their route)
  C4  middle line == C2 ; final line == C2/2  (identically in eps, th)
  C5  z3: final == exact  <=>  rho == 0   (so the slip is nowhere harmless except on the zero set)
  C6  sign of rho, hence the negativity condition cos2th > sqrt2 eps, is the same under both lines
  C7  consequence for Delta = 1 - rho^2/<:T00^2:>: exact <:T00^2:> by Fock; Delta with the final line
  C8  context: does (3.8) follow from the final line (or the middle) with printed or exact (3.7)?
"""
import sys
import sympy as sp
import z3

ok_all = True


def chk(label, cond, detail=""):
    global ok_all
    ok_all &= bool(cond)
    print("  [%s] %s %s" % ("ok" if cond else "XX", label, detail))


# ---------------------------------------------------------------- C1
t, x, y, zc = sp.symbols('t x y z', real=True)
kx, ky, kz, L = sp.symbols('k_x k_y k_z L', positive=True)
w = sp.sqrt(kx**2 + ky**2 + kz**2)
X = (t, x, y, zc)
eta = sp.diag(-1, 1, 1, 1)
k_up = (w, kx, ky, kz)
k_dn = tuple(eta[i, i] * k_up[i] for i in range(4))
theta = sum(k_dn[i] * X[i] for i in range(4))           # k_r x^r = -w t + k.x
f = sp.exp(sp.I * theta) / sp.sqrt(2 * w * L**3)
fc = sp.exp(-sp.I * theta) / sp.sqrt(2 * w * L**3)


def Tbil(g, h, m, n):
    dg = [sp.diff(g, X[i]) for i in range(4)]
    dh = [sp.diff(h, X[i]) for i in range(4)]
    contr = sum(eta[s, s] * dg[s] * dh[s] for s in range(4))     # eta^{ss} = eta_{ss}
    return sp.simplify(dg[m] * dh[n] - sp.Rational(1, 2) * eta[m, n] * contr)


ksq = sum(eta[i, i] * k_up[i]**2 for i in range(4))
chk("massless: k^r k_r = 0", sp.simplify(ksq) == 0)
Kmn = lambda m, n: (k_dn[m] * k_dn[n] - sp.Rational(1, 2) * eta[m, n] * ksq) / (2 * w * L**3)
c1 = True
for (m, n) in [(0, 0), (0, 1), (1, 2), (3, 3)]:
    K = Kmn(m, n)
    c1 &= sp.simplify(Tbil(f, f, m, n) - (-K * sp.exp(2 * sp.I * theta))) == 0
    c1 &= sp.simplify(Tbil(fc, f, m, n) - K) == 0
    c1 &= sp.simplify(Tbil(f, fc, m, n) - K) == 0
    c1 &= sp.simplify(Tbil(fc, fc, m, n) - (-K * sp.exp(-2 * sp.I * theta))) == 0
chk("C1 (2.12)-(2.14) follow from (2.11) with K_ab as printed", c1)
chk("C1 K_00 = w/(2 L^3)", sp.simplify(Kmn(0, 0) - w / (2 * L**3)) == 0)

# ---------------------------------------------------------------- C2
Ks, eps = sp.symbols('K epsilon', positive=True)
th = sp.symbols('theta', real=True)
Nmax = 8
a = sp.zeros(Nmax, Nmax)
for n in range(1, Nmax):
    a[n - 1, n] = sp.sqrt(n)
ad = a.T
e2 = sp.exp(2 * sp.I * th)
# :T00: = a a T[f,f] + a+ a (T[f,f*]+T[f*,f]) + a+ a+ T[f*,f*]
T00 = a * a * (-Ks * e2) + ad * a * (2 * Ks) + ad * ad * (-Ks / e2)
Nn = 1 + eps**2
psi = sp.zeros(Nmax, 1)
psi[0] = 1 / sp.sqrt(Nn)
psi[2] = eps / sp.sqrt(Nn)
chk("state normalised", sp.simplify((psi.T * psi)[0] - 1) == 0)
rho = sp.simplify(sp.expand((psi.T * T00 * psi)[0]).rewrite(sp.cos))
rho = sp.simplify(sp.expand_complex(rho))
print("      exact <:T00:> =", sp.factor(rho))

# ---------------------------------------------------------------- C3 (KF (2.10) route)
c = {0: 1 / sp.sqrt(Nn), 2: eps / sp.sqrt(Nn)}
cc = lambda n: c.get(n, 0)
kf210 = 0
for n in range(0, 5):
    kf210 += 2 * n * cc(n)**2 * Ks
    if n >= 2:
        kf210 += sp.sqrt(n) * sp.sqrt(n - 1) * cc(n) * cc(n - 2) * (-Ks * e2)
        kf210 += sp.sqrt(n) * sp.sqrt(n - 1) * cc(n) * cc(n - 2) * (-Ks / e2)
kf210 = sp.simplify(sp.expand_complex(sp.expand(kf210)))
chk("C3 KF (2.10) at c0,c2 equals Fock result", sp.simplify(kf210 - rho) == 0)

# ---------------------------------------------------------------- C4
Tff, Tcc, Tfc = -Ks * e2, -Ks / e2, Ks
middle = eps / Nn * (sp.sqrt(2) * (Tff + Tcc) + 2 * eps * (Tfc + Tfc))
middle = sp.simplify(sp.expand_complex(middle))
final = Ks * eps / Nn * (2 * eps - sp.sqrt(2) * sp.cos(2 * th))
chk("C4 middle line == exact", sp.simplify(middle - rho) == 0)
ratio = sp.simplify(final / rho)
chk("C4 final line == exact/2 identically", ratio == sp.Rational(1, 2), "(final/exact = %s)" % ratio)

# ---------------------------------------------------------------- C5 (z3)
e_, cz, q, Kz = z3.Reals('e c q K')
H = [q > 0, q * q == 2, cz >= -1, cz <= 1, Kz > 0, e_ > 0]
rho_z = 2 * Kz * e_ * (2 * e_ - q * cz)           # times 1/(1+eps^2) > 0, dropped
fin_z = Kz * e_ * (2 * e_ - q * cz)
s = z3.Solver(); s.add(*H); s.add(z3.Not((fin_z == rho_z) == (rho_z == 0)))
chk("C5 z3: final == exact <=> rho == 0 (unsat of negation)", s.check() == z3.unsat)
s = z3.Solver(); s.add(*H); s.add(fin_z != rho_z)
chk("C5 z3 vacuity guard: a point with final != exact exists", s.check() == z3.sat)
s = z3.Solver(); s.add(*H); s.add(z3.Not((fin_z < 0) == (rho_z < 0)))
chk("C6 z3: sign(final) == sign(exact) everywhere (negativity region unchanged)", s.check() == z3.unsat)
s = z3.Solver(); s.add(*H); s.add(z3.Not((rho_z < 0) == (cz * q > 2 * e_)))
chk("C6 z3: rho < 0 <=> cos2th > sqrt2 eps (KF's stated condition)", s.check() == z3.unsat)

# ---------------------------------------------------------------- C7
T2 = sp.simplify(sp.expand_complex(sp.expand((psi.T * (T00 * T00) * psi)[0])))
# normal-ordered square: :T00^2: -- build normal-ordered product explicitly
A, Ad = sp.symbols('A Ad', commutative=False)
# :T00 T00: in terms of normal-ordered monomials (a+^m a^n) with c-number coefficients
coef = {(0, 2): -Ks * e2, (1, 1): 2 * Ks, (2, 0): -Ks / e2}
prod = {}
for (m1, n1), c1_ in coef.items():
    for (m2, n2), c2_ in coef.items():
        prod[(m1 + m2, n1 + n2)] = prod.get((m1 + m2, n1 + n2), 0) + c1_ * c2_


def mono(m, n):
    M = sp.eye(Nmax)
    for _ in range(m):
        M = M * ad
    for _ in range(n):
        M = M * a
    return M


T2no = sum((prod[k] * mono(*k) for k in prod), sp.zeros(Nmax, Nmax))
T2n = sp.simplify(sp.expand_complex(sp.expand((psi.T * T2no * psi)[0])))
chk("C7 exact <:T00^2:> = 12 K^2 eps^2/(1+eps^2)", sp.simplify(T2n - 12 * Ks**2 * eps**2 / Nn) == 0,
    "(= %s)" % sp.factor(T2n))
cth = sp.cos(2 * th)
D_exact = sp.simplify(1 - rho**2 / T2n)
D_final = sp.simplify(1 - final**2 / T2n)
chk("C7 Delta_exact = 1 - (2eps - sqrt2 cos2th)^2/(3(1+eps^2))",
    sp.simplify(D_exact - (1 - (2 * eps - sp.sqrt(2) * cth)**2 / (3 * Nn))) == 0)
chk("C7 Delta with final line = 1 - (2eps - sqrt2 cos2th)^2/(12(1+eps^2))",
    sp.simplify(D_final - (1 - (2 * eps - sp.sqrt(2) * cth)**2 / (12 * Nn))) == 0)
at = {eps: sp.Rational(1, 10), th: 0}
print("      at eps=1/10, th=0:  rho_exact/K = %.6f  rho_final/K = %.6f  Delta_exact = %.4f  Delta_final = %.4f"
      % (float((rho / Ks).subs(at)), float((final / Ks).subs(at)), float(D_exact.subs(at)), float(D_final.subs(at))))
# min of Delta over rho<0 region under each line (numeric scan)
import math
mins = {"exact": 9, "final": 9}
for i in range(1, 400):
    ev = i / 100
    for j in range(0, 181):
        cv = math.cos(2 * math.radians(j))
        X_ = 2 * ev - math.sqrt(2) * cv
        if ev * X_ < 0:
            mins["exact"] = min(mins["exact"], 1 - X_**2 / (3 * (1 + ev**2)))
            mins["final"] = min(mins["final"], 1 - X_**2 / (12 * (1 + ev**2)))
print("      scan over rho<0: inf Delta_exact ~ %.4f (-> 1/3), inf Delta_final ~ %.4f (-> 5/6)"
      % (mins["exact"], mins["final"]))
# prove the two infima with z3: X^2 < 2(1+e^2) on rho<0
s = z3.Solver(); s.add(*H); Xz = 2 * e_ - q * cz; s.add(e_ * Xz < 0); s.add(z3.Not(Xz * Xz < 2 * (1 + e_ * e_)))
chk("C7 z3: rho<0 => (2eps-sqrt2 c)^2 < 2(1+eps^2) => Delta_exact > 1/3, Delta_final > 5/6", s.check() == z3.unsat)

# ---------------------------------------------------------------- C8 (context only)
kf37 = 12 * Ks**2 * eps**2 / Nn**2
kf38 = (10 * eps + sp.sqrt(2) * cth) / (12 * eps)
cands = {"final,printed(3.7)": 1 - final**2 / kf37, "final,exact": D_final,
         "middle,printed(3.7)": 1 - rho**2 / kf37, "middle,exact": D_exact}
for name, expr in cands.items():
    same = sp.simplify(expr - kf38) == 0
    print("      C8 context: (3.8) from %-22s %s" % (name, "REPRODUCED" if same else "not reproduced"))

print("\nALL CHECKS PASS" if ok_all else "\nSOME CHECK FAILED")
sys.exit(0 if ok_all else 1)
