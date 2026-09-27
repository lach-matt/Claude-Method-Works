#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation of Ford & Roman, gr-qc/9607003 (PRD 55, 2082 (1997)),
"Restrictions on Negative Energy Density in Flat Spacetime".

Everything here is checked against the source text READ at alphaXiv (v2, 24 Jan 1997).
Units hbar = c = 1 unless stated.  Exits 1 if any check fails.

  A  Lorentzian sampler: normalised, and (t0/pi) INT e^{i W t}/(t^2+t0^2) dt = e^{-|W| t0}
     (the step Eq.(7)+(8) -> Eq.(9))
  B  mode sum -> integral and Eq.(13) at m=0 -> Eq.(17): -3/(32 pi^2 t0^4)
  C  G(0) = 1 (Eq.15), G decreasing (massive bound tighter), 4D massive -> massless
  D  EM Eq.(47) -> Eq.(48): -3/(16 pi^2 t0^4) (factor 2)
  E  2D: Eq.(19) at m=0 -> -1/(8 pi t0^2); F(y) -> 1 as y -> 0 (Eq.23)
  F  Lemma B kernel e^{-|wi-wj|t0} - e^{-(wi+wj)t0} is PSD (numeric, random spectra)
  G  END-TO-END: random multimode Bogoliubov (squeezed) states on a finite set of box
     modes; Eq.(9) evaluated exactly is >= the finite-V bound Eq.(12) restricted to the
     occupied modes (a STRONGER statement than Eq.(12), which sums over all modes)
  H  SI form: 3 hbar/(32 pi^2 c^3 t0^4) == 3 hbar c/(32 pi^2 L^4) at L = c t0;
     candidates.ford_roman(1e-9) = 3.0031e8 J/m^3; achievable's 105.276 = 32 pi^2/3
  I  STATIC corollary: for a time-independent <T00> at the point, rho-hat = rho0 and
     Eq.(1) for ALL t0 forces rho0 >= 0 (flat, no boundaries)
  J  Fewster-Eveson (gr-qc/9805024 Eq.(5.5)-(5.6), READ) flat massless bound (1/16pi^2) INT (g'')^2
     with g = sqrt(Lorentzian): ratio to Ford-Roman = 9/64 (FE's own printed figure; fewsterteo.py's)
  L  2D cross-check of FE Sec. V.A (READ): at the Lorentzian, Flanagan's optimal 2D bound
     -(1/24 pi) INT f'^2/f is 1/6 of Ford-Roman's 2D -1/(8 pi t0^2), and FE's 2D bound
     -(1/16 pi) INT f'^2/f is 1/4 of it; the Lorentzian tail ~ t^-2 (not rapidly decreasing)
  K  the tree's crossover 0.307933 l_P and shortfall 4.037e52 (tree arithmetic, not source)
"""
import math
import sys

import numpy as np
import sympy as sp

FAIL = []


def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + (("   " + str(detail)) if detail else ""))
    if not ok:
        FAIL.append(name)


t, t0, w, W, x, y = sp.symbols('t t_0 omega W x y', positive=True)

# ---- A
f = t0 / (sp.pi * (t ** 2 + t0 ** 2))
tt = sp.Symbol('tt', real=True)
fr = t0 / (sp.pi * (tt ** 2 + t0 ** 2))
norm = sp.simplify(sp.integrate(fr, (tt, -sp.oo, sp.oo)))
chk("A1 Lorentzian sampler integrates to 1", sp.simplify(norm - 1) == 0, norm)
ft = sp.simplify(sp.integrate(fr * sp.cos(W * tt), (tt, -sp.oo, sp.oo)))
chk("A2 (t0/pi) INT cos(W t)/(t^2+t0^2) = exp(-W t0), W>0",
    sp.simplify(ft - sp.exp(-W * t0)) == 0, ft)

# ---- B
# -1/(2V) sum_k w e^{-2 w t0},  sum_k -> V/(8 pi^3) INT d^3k = V/(8pi^3) 4 pi INT w^2 dw
bound_int = -sp.Rational(1, 2) * (4 * sp.pi / (8 * sp.pi ** 3)) * sp.integrate(
    w ** 3 * sp.exp(-2 * w * t0), (w, 0, sp.oo))
eq17 = -3 / (32 * sp.pi ** 2 * t0 ** 4)
chk("B1 Eq.(12) -> V->oo integral -> Eq.(17) = -3/(32 pi^2 t0^4)",
    sp.simplify(bound_int - eq17) == 0, sp.simplify(bound_int))
eq13_m0 = -1 / (4 * sp.pi ** 2) * sp.integrate(w ** 3 * sp.exp(-2 * w * t0), (w, 0, sp.oo))
chk("B2 Eq.(13) at m=0 equals Eq.(17)", sp.simplify(eq13_m0 - eq17) == 0)

# ---- C
G0 = sp.Rational(1, 6) * sp.integrate(x ** 3 * sp.exp(-x), (x, 0, sp.oo))
chk("C1 G(0) = 1", G0 == 1, G0)
from scipy.integrate import quad


def Gnum(yv):
    return quad(lambda xv: math.sqrt(xv * xv - yv * yv) * xv * xv * math.exp(-xv), yv, np.inf)[0] / 6


gs = [Gnum(v) for v in (0.0, 0.5, 1, 2, 5, 10)]
chk("C2 G(y) strictly decreasing on 0..10 (massive bound tighter)",
    all(a > b for a, b in zip(gs, gs[1:])), [round(g, 5) for g in gs])
# Eq.(13)->(14): substitution x = 2 w t0, y = 2 m t0
m = sp.Symbol('m', positive=True)
lhs = -1 / (4 * sp.pi ** 2) * sp.sqrt(w ** 2 - m ** 2) * w ** 2 * sp.exp(-2 * w * t0)
sub = lhs.subs({w: x / (2 * t0), m: y / (2 * t0)}) * (1 / (2 * t0))
rhs = -1 / (64 * sp.pi ** 2 * t0 ** 4) * sp.sqrt(x ** 2 - y ** 2) * x ** 2 * sp.exp(-x)
chk("C3 substitution Eq.(13) -> Eq.(14) integrand", sp.simplify(sub - rhs) == 0)

# ---- D
em = -1 / (2 * sp.pi ** 2) * sp.integrate(w ** 3 * sp.exp(-2 * w * t0), (w, 0, sp.oo))
chk("D1 EM Eq.(47) -> Eq.(48) = -3/(16 pi^2 t0^4) = 2 x scalar",
    sp.simplify(em + 3 / (16 * sp.pi ** 2 * t0 ** 4)) == 0 and sp.simplify(em / eq17) == 2)

# ---- E
two_d = -1 / (2 * sp.pi) * sp.integrate(w * sp.exp(-2 * w * t0), (w, 0, sp.oo))
chk("E1 2D massless Eq.(19) at m=0 = -1/(8 pi t0^2)",
    sp.simplify(two_d + 1 / (8 * sp.pi * t0 ** 2)) == 0)
Fy = y ** 2 / 2 * (sp.besselk(0, y) + sp.besselk(2, y))
chk("E2 F(y) = (y^2/2)[K0+K2] -> 1 as y -> 0", sp.limit(Fy, y, 0) == 1)

# ---- F
rng = np.random.default_rng(67)
minev = 1e9
for _ in range(400):
    n = rng.integers(2, 25)
    om = np.sort(rng.uniform(0.01, 10, n))
    T0 = rng.uniform(0.01, 3)
    K = np.exp(-np.abs(om[:, None] - om[None, :]) * T0) - np.exp(-(om[:, None] + om[None, :]) * T0)
    ev = np.linalg.eigvalsh(K).min() / np.abs(K).max()
    minev = min(minev, ev)
chk("F1 Lemma-B kernel PSD on 400 random spectra (min normalised eigenvalue >= -1e-12)",
    minev >= -1e-12, "%.3e" % minev)

# ---- G  end-to-end
from scipy.linalg import expm


def bogoliubov(n, scale):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    A = 1j * (A + A.conj().T) / 2 * scale          # anti-Hermitian i*H
    B = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    B = (B + B.T) / 2 * scale                       # complex symmetric
    Mgen = np.block([[A, B], [B.conj(), A.conj()]])
    T = expm(Mgen)
    return T[:n, :n], T[:n, n:]


worst = -1e9
ccr_err = 0.0
nstates = 0
nneg = 0
for trial in range(300):
    n = int(rng.integers(1, 9))
    Lbox = 1.0
    V = Lbox ** 3
    ks = rng.integers(-3, 4, size=(n, 3)) * 2 * np.pi / Lbox
    ks = ks[np.linalg.norm(ks, axis=1) > 0]
    ks = np.unique(ks, axis=0)
    n = len(ks)
    if n == 0:
        continue
    om = np.linalg.norm(ks, axis=1)
    al, be = bogoliubov(n, rng.uniform(0.05, 1.5))
    ccr_err = max(ccr_err, np.abs(al @ al.conj().T - be @ be.conj().T - np.eye(n)).max(),
                  np.abs(al @ be.T - be @ al.T).max())
    N = be.conj().T @ be            # <a_i^dag a_j>
    Mm = -(al.conj().T @ be)        # <a_i a_j>
    Mm = (Mm + Mm.T) / 2            # symmetric by CCR (a_i a_j = a_j a_i)
    T0 = 10 ** rng.uniform(-4, -0.5)   # q = e^{-2 w t0} spans ~1 down to small
    pref = (np.outer(om, om) + ks @ ks.T) / np.sqrt(np.outer(om, om))
    Wm = np.abs(om[:, None] - om[None, :])
    S = om[:, None] + om[None, :]
    bnd = -np.sum(om * np.exp(-2 * om * T0)) / (2 * V)
    # a global phase rotation a -> e^{i th/2} a is unitary: N fixed, M -> e^{i th} M.
    # Take the most negative rho-hat over th, so the check is not vacuous.
    for th in np.linspace(0, 2 * np.pi, 73):
        rho_hat = np.real(np.sum(pref * (N * np.exp(-Wm * T0)
                                         + np.exp(1j * th) * Mm * np.exp(-S * T0)))) / (2 * V)
        nstates += 1
        worst = max(worst, (bnd - rho_hat) / abs(bnd))
        if rho_hat < 0:
            nneg += 1
chk("G0 Bogoliubov transformations preserve the CCR (max err < 1e-8)", ccr_err < 1e-8, "%.2e" % ccr_err)
chk("G1 Eq.(9) exact >= Eq.(12) (occupied modes) on %d random squeezed states" % nstates,
    worst <= 1e-10, "max (bound - rho_hat)/|bound| = %.3e (must be <= 0)" % worst)
chk("G2 guard: the test is not vacuous -- negative rho-hat occurs", nneg > 100,
    "%d of %d (state, phase) pairs negative" % (nneg, nstates))
# G3 single mode squeezed vacuum: rho-hat = (w/V)[s^2 - s sqrt(1+s^2) q], q = e^{-2 w t0};
# approaches the finite-V bound -w q/(2V) only as q -> 1 and s -> oo; never crosses it.
wv, Vv = 2 * np.pi, 1.0
vals = []
for q in (0.5, 0.9, 0.99, 0.999999):
    ss = np.logspace(-3, 4, 4000)
    rh = wv / Vv * (ss ** 2 - ss * np.sqrt(1 + ss ** 2) * q)
    vals.append((rh.min() / (-wv * q / (2 * Vv))))
chk("G3 single-mode squeezed: min rho-hat / finite-V bound < 1 always, -> 1 as q -> 1",
    all(v < 1 for v in vals) and vals[-1] > 0.99, [round(v, 6) for v in vals])
# G4 control: the same machinery DOES flag a bound made 2x too tight
chk("G4 control: a bound with half the magnitude is violated by the q->1 single mode",
    vals[-1] > 0.5)

# ---- H
HBAR, C, Gn = 1.054571817e-34, 299792458.0, 6.67430e-11
L = sp.Symbol('L', positive=True)
hb, cc = sp.symbols('hbar c', positive=True)
si_t = 3 * hb / (32 * sp.pi ** 2 * cc ** 3 * t0 ** 4)
si_L = 3 * hb * cc / (32 * sp.pi ** 2 * L ** 4)
chk("H1 3hbar/(32pi^2 c^3 t0^4) at t0=L/c == 3 hbar c/(32 pi^2 L^4)",
    sp.simplify(si_t.subs(t0, L / cc) - si_L) == 0)
fr_1nm = 3 * HBAR * C / (32 * math.pi ** 2 * 1e-9 ** 4)
chk("H2 ford_roman(1 nm) = 3.0031e8 J/m^3", abs(fr_1nm / 3.0031e8 - 1) < 1e-4, "%.5e" % fr_1nm)
r = (HBAR * C / 1.0) / (3 * HBAR / (32 * math.pi ** 2 * C ** 3 * (1 / C) ** 4))
chk("H3 achievable quantum_bound(1)/ford_roman_allow(1/c) = 32 pi^2/3 = 105.276",
    abs(r - 105.276) < 1e-3 and abs(r - 32 * math.pi ** 2 / 3) < 1e-9, "%.6f" % r)

# ---- I
rho0 = sp.Symbol('rho0', real=True)
rh = sp.integrate(fr * rho0, (tt, -sp.oo, sp.oo))
chk("I1 static <T00>=rho0: rho-hat = rho0 for every t0", sp.simplify(rh - rho0) == 0)
chk("I2 Eq.(1) for all t0 => rho0 >= lim_{t0->oo} -3/(32pi^2 t0^4) = 0",
    sp.limit(eq17, t0, sp.oo) == 0)

# ---- J  Fewster-Eveson flat massless: rho-hat >= -(1/16 pi^2) INT (g'')^2 dt, f = g^2
g = sp.sqrt(t0 / sp.pi) / sp.sqrt(tt ** 2 + t0 ** 2)
fe = sp.simplify(sp.integrate(sp.diff(g, tt, 2) ** 2, (tt, -sp.oo, sp.oo)) / (16 * sp.pi ** 2))
ratio = sp.nsimplify(sp.simplify(fe / (3 / (32 * sp.pi ** 2 * t0 ** 4))))
chk("J1 Fewster-Eveson bound with Ford-Roman's Lorentzian = 9/64 of Ford-Roman's",
    ratio == sp.Rational(9, 64), "FE = %s, ratio = %s" % (fe, ratio))

# ---- K  tree arithmetic (candidates.py), with Lambda = phase1.lam()
LAM = 9.982529174194637
lp = math.sqrt(HBAR * Gn / C ** 3)
xo = math.sqrt(3 * LAM / (32 * math.pi ** 2))
chk("K1 crossover sqrt(3 Lambda/(32 pi^2)) = 0.307933 l_P", abs(xo - 0.307933) < 1e-6, "%.6f" % xo)
need = C ** 4 / (Gn * LAM * 1e-18)
chk("K2 shortfall(1 nm) = 4.037e52", abs(need / fr_1nm / 4.037e52 - 1) < 1e-3, "%.4e" % (need / fr_1nm))
# CODATA 2022: G = 6.67430(15)e-11 (unchanged from 2018); hbar, c exact since 2019 SI
Gold = 6.67430e-11 + 3 * 0.00015e-11
xo2 = math.sqrt(3 * HBAR * (Gold) * LAM / (32 * math.pi ** 2 * C ** 3)) / math.sqrt(HBAR * Gold / C ** 3)
chk("K3 crossover in l_P units is independent of G, hbar, c (only Lambda enters)", abs(xo2 - xo) < 1e-12)

# ---- L  2D: Flanagan (optimal) and Fewster-Eveson at the Lorentzian, vs Ford-Roman Eq.(25)
fp = sp.diff(fr, tt)
I2 = sp.simplify(sp.integrate(sp.simplify(fp ** 2 / fr), (tt, -sp.oo, sp.oo)))
fl = I2 / (24 * sp.pi)
fe2 = I2 / (16 * sp.pi)
fr2 = 1 / (8 * sp.pi * t0 ** 2)
chk("L1 Flanagan optimal 2D bound at the Lorentzian = 1/6 of Ford-Roman 2D (FE p.8: 'six times stronger')",
    sp.simplify(fl / fr2) == sp.Rational(1, 6), "INT f'^2/f = %s" % I2)
chk("L2 Fewster-Eveson 2D bound at the Lorentzian = 1/4 of Ford-Roman 2D (FE p.8: 'four times stronger')",
    sp.simplify(fe2 / fr2) == sp.Rational(1, 4))
chk("L3 Lorentzian tail: t^2 f(t) -> t0/pi (decays as t^-2, outside FE's 'rapid decay' class)",
    sp.simplify(sp.limit(tt ** 2 * fr, tt, sp.oo) - t0 / sp.pi) == 0)

print("\n%d FAIL" % len(FAIL) if FAIL else "\nALL PASS")
sys.exit(1 if FAIL else 0)
