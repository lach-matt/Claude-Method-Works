#!/usr/bin/env python3
"""DOCKET 67 audit 1208.5399-sec5.1 -- re-derivation.

Fewster, Lectures on QEIs (arXiv:1208.5399v1) Sec. 5.1 summarises Fewster &
Osterbrink (FO) arXiv:0708.2450 Sec. 3: the massless NONMINIMALLY coupled scalar
in 4D Minkowski admits Hadamard states with arbitrarily negative energy density
over arbitrarily large regions, hence no state-independent QEI.  FO prove it
for xi > 0.  This script:

  A  re-derives FO eq.(28) (energy density at the spatial origin of the
     one-particle state Psi_kappa) symbolically, and eq.(29) at t = 0;
  B  checks normalisation <Psi|Psi> = 1 and eq.(26) <H> = 2 kappa / 3;
  C  checks the scaling relation eq.(27) rho_{lambda kappa}(t) = lambda^4 rho_kappa(lambda t);
  D  checks the additivity used for the j-particle state (eq.(33)):
     <a^dag(f) a(g)> in (a^dag(h))^n / sqrt(n!) Omega equals n <h,f><g,h>,
     and the pair terms vanish -- on an explicit finite Fock space;
  E  (EXTENSION COMPUTED HERE, not in any source read) shows that for EVERY
     xi < 0 a normalisable, rapidly decaying, isotropic one-particle state has
     NEGATIVE energy density at the origin, so FO's continuity + scaling +
     tensoring argument carries over verbatim to xi < 0 (massless, 4D Minkowski);
  F  records that the single-exponential FO profile is NOT negative at the
     origin for -1/6 <= xi < 0 (so FO's own state does not cover xi < 0);
  G  section attribution: the phrase 'one cannot expect state-independent QEIs
     to hold' is in Sec. 5.2, not 5.1 (checked against the page text saved in
     src/1208.5399-sec5.txt, read through alphaXiv).
Exit 0 iff every check passes.
"""
import itertools
import math
import os
import sys

import sympy as sp

OK = True


def check(name, cond, detail=""):
    global OK
    print(("PASS " if cond else "FAIL ") + name + ((" -- " + detail) if detail else ""))
    OK = OK and bool(cond)


t, k, kap, xi, lam = sp.symbols("t k kappa xi lambda", real=True)
kp = sp.Symbol("kappa", positive=True)
lp = sp.Symbol("lambda", positive=True)
kk = sp.Symbol("k", positive=True)

# dmu(k) = d^3k / ((2 pi)^3 2|k|).  For an isotropic h and x = 0 the angular
# integral is 4 pi, so F(t) = <Omega|Phi(t,0)Psi> = (1/(4 pi^2)) INT_0^oo k e^{-itk} h(k) dk.
C = 4 * sp.pi / (2 * (2 * sp.pi) ** 3)
h_FO = 4 * sp.pi * sp.sqrt(2) * (kp - kk / 3) * sp.exp(-kk / kp) / kp ** 2


def F_of(h):
    return sp.simplify(C * sp.integrate(kk * sp.exp(-sp.I * t * kk) * h, (kk, 0, sp.oo), conds="none"))


def rho_origin(h, xi_):
    """FO eq.(24) at x = 0 for real isotropic h (spatial gradient vanishes there
    by isotropy): rho = |F'|^2 - 4 xi Re(conj(F) F'')."""
    F = F_of(h)
    Fp = sp.diff(F, t)
    Fpp = sp.diff(F, t, 2)
    r = sp.simplify(sp.expand_complex(Fp * sp.conjugate(Fp)
                                      - 4 * xi_ * sp.re(sp.conjugate(F) * Fpp)))
    return sp.simplify(r)


# ---- A: eq.(28), eq.(29)
rho = rho_origin(h_FO, xi)
eq28 = 8 * kp ** 4 / (3 * (1 + t ** 2 * kp ** 2) ** 5 * sp.pi ** 2) * (
    (3 * t ** 4 * kp ** 4 + 3 * t ** 2 * kp ** 2) - xi * (18 * t ** 4 * kp ** 4 - 44 * t ** 2 * kp ** 2 + 2))
check("A1 FO eq.(28) re-derived symbolically", sp.simplify(rho - eq28) == 0, str(sp.factor(rho)))
check("A2 FO eq.(29): rho(0,0) = -xi (2 kappa)^4 / (3 pi^2)",
      sp.simplify(rho.subs(t, 0) + xi * (2 * kp) ** 4 / (3 * sp.pi ** 2)) == 0)
# gradient at the origin vanishes by isotropy: INT over angles of k_b = 0
th = sp.Symbol("theta")
check("A3 spatial gradient at origin vanishes (angular integral of cos(theta) sin(theta))",
      sp.integrate(sp.cos(th) * sp.sin(th), (th, 0, sp.pi)) == 0)

# ---- B: normalisation and energy
norm = sp.simplify(4 * sp.pi / (2 * (2 * sp.pi) ** 3) * sp.integrate(kk * h_FO ** 2, (kk, 0, sp.oo)))
energy = sp.simplify(4 * sp.pi / (2 * (2 * sp.pi) ** 3) * sp.integrate(kk ** 2 * h_FO ** 2, (kk, 0, sp.oo)))
check("B1 <Psi_kappa|Psi_kappa> = 1", sp.simplify(norm - 1) == 0, str(norm))
check("B2 FO eq.(26) <H> = 2 kappa/3", sp.simplify(energy - 2 * kp / 3) == 0, str(energy))

# ---- C: scaling eq.(27)
rho_l = rho.subs(kp, lp * kp)
check("C1 FO eq.(27) rho_{lambda kappa}(t) = lambda^4 rho_kappa(lambda t)",
      sp.simplify(rho_l - lp ** 4 * rho.subs(t, lp * t)) == 0)
# ball radius: FO eq.(30) -- rho <= -xi(2k)^4/(6pi^2) on a ball; check at xi = 1/6, kappa = 1
# along t that rho(t,0) stays <= half its t=0 value for |t| <= 0.1 (numeric sample)
r16 = sp.lambdify(t, rho.subs({xi: sp.Rational(1, 6), kp: 1}))
samples = [r16(0.1 * i / 50) for i in range(51)]
check("C2 continuity: at xi=1/6, kappa=1, rho(t,0) <= rho(0,0)/2 for |t|<=0.1",
      max(samples) <= r16(0.0) / 2, "rho(0,0)=%.6g max=%.6g" % (r16(0.0), max(samples)))

# ---- D: additivity on an explicit Fock space (2 modes, n up to 4)
def fock_check(nmax=4):
    import cmath
    modes = 2
    h = [0.6, 0.8j]          # normalised: 0.36 + 0.64 = 1
    f = [0.3 - 0.2j, 1.1]
    g = [0.7j, -0.4 + 0.5j]
    for n in range(1, nmax + 1):
        # state (sum_i h_i a_i^dag)^n / sqrt(n!) |0>, stored as dict occupation->amp
        state = {(0, 0): 1.0 + 0j}
        for _ in range(n):
            new = {}
            for occ, amp in state.items():
                for i in range(modes):
                    o = list(occ); o[i] += 1; o = tuple(o)
                    new[o] = new.get(o, 0) + amp * h[i] * math.sqrt(o[i])
            state = new
        state = {o: a / math.sqrt(math.factorial(n)) for o, a in state.items()}
        nrm = sum(abs(a) ** 2 for a in state.values())

        def apply_a(st, i):
            out = {}
            for occ, amp in st.items():
                if occ[i] == 0:
                    continue
                o = list(occ); o[i] -= 1; o = tuple(o)
                out[o] = out.get(o, 0) + amp * math.sqrt(occ[i])
            return out

        def inner(s1, s2):
            return sum(s1[o].conjugate() * s2.get(o, 0) for o in s1)

        # <a^dag(f) a(g)> with a(g) = sum conj(g_i) a_i, a^dag(f) = sum f_i a_i^dag
        ag = {}
        for i in range(modes):
            for o, a in apply_a(state, i).items():
                ag[o] = ag.get(o, 0) + g[i].conjugate() * a
        af = {}
        for i in range(modes):
            for o, a in apply_a(state, i).items():
                af[o] = af.get(o, 0) + f[i].conjugate() * a
        lhs = inner(af, ag)
        fh = sum(f[i].conjugate() * h[i] for i in range(modes))
        hg = sum(h[i].conjugate() * g[i] for i in range(modes))
        # <psi|a^dag(f) a(g)|psi> = <a(f)psi, a(g)psi>; one-particle density matrix n|h><h|
        # gives n * <h,f> * <g,h> with the inner product antilinear in its FIRST slot
        rhs = n * fh.conjugate() * hg.conjugate()
        # pair term <a(f) a(g)> vanishes (number eigenstate)
        aag = {}
        for i in range(modes):
            for o, a in apply_a(ag, i).items():
                aag[o] = aag.get(o, 0) + f[i].conjugate() * a
        pair = inner(state, aag) if all(o in state for o in aag) else 0
        if abs(nrm - 1) > 1e-12 or abs(lhs - rhs) > 1e-12 or abs(pair) > 1e-12:
            return False, "n=%d nrm=%s lhs=%s rhs=%s pair=%s" % (n, nrm, lhs, rhs, pair)
    return True, "n = 1..%d" % nmax


ok, det = fock_check()
check("D1 j-particle additivity: <a^dag(f)a(g)> = n <h,f><g,h> (density matrix n|h><h|), pair terms 0", ok, det)

# ---- E: extension to xi < 0 (computed here)
# For real isotropic h >= 0 with A_n = INT_0^oo k^n h dk:
#   F(0) = C A1, F'(0) = -i C A2, F''(0) = -C A3  ->  rho(0,0) = C^2 (A2^2 + 4 xi A1 A3).
A = sp.symbols("A1 A2 A3", positive=True)
Fsym0, Fp0, Fpp0 = C * A[0], -sp.I * C * A[1], -C * A[2]
rho00 = sp.simplify(sp.expand_complex(Fp0 * sp.conjugate(Fp0) - 4 * xi * sp.re(sp.conjugate(Fsym0) * Fpp0)))
check("E1 rho(0,0) = C^2 (A2^2 + 4 xi A1 A3) for real isotropic h",
      sp.simplify(rho00 - C ** 2 * (A[1] ** 2 + 4 * xi * A[0] * A[2])) == 0)
# two-scale profile h = e^{-k} + c e^{-k/K}: A_n = n! (1 + c K^{n+1})
Kc, cc = sp.symbols("K c", positive=True)
An = [sp.factorial(n) * (1 + cc * Kc ** (n + 1)) for n in (1, 2, 3)]
ratio = sp.simplify((An[0] * An[2] / An[1] ** 2).subs(cc, Kc ** -3))
check("E2 A1 A3 / A2^2 -> oo as K -> oo (c = K^-3)", sp.limit(ratio, Kc, sp.oo) == sp.oo, str(sp.factor(ratio)))
# explicit witnesses with direct symbolic evaluation of rho(0,0) via rho_origin
wit = []
for xv, Kv in ((sp.Rational(-1, 100), 400), (sp.Rational(-1, 1000), 4000), (sp.Rational(-1, 10), 40)):
    hK = sp.exp(-kk) + sp.Rational(1, Kv ** 3) * sp.exp(-kk / Kv)
    r0 = sp.nsimplify(rho_origin(hK, xv).subs(t, 0))
    nrm = sp.integrate(C * kk * hK ** 2, (kk, 0, sp.oo))   # finite -> normalisable
    wit.append((xv, Kv, float(r0 / nrm), float(nrm)))
check("E3 xi<0 witnesses: normalised rho(0,0) < 0 at xi = -1/100, -1/1000, -1/10",
      all(w[2] < 0 for w in wit), "; ".join("xi=%s K=%d rho/norm=%.3e" % (w[0], w[1], w[2]) for w in wit))

# ---- F: FO's own single-exponential state at xi < 0
# h ~ e^{-k/kappa}: A1 A3 / A2^2 = 6/4 -> rho00 ∝ 4 + 24 xi, negative only for xi < -1/6
e1 = sp.factorial(1) * sp.factorial(3) / sp.factorial(2) ** 2
check("F1 single exponential: A1A3/A2^2 = 3/2 (negative at origin only for xi < -1/6)", e1 == sp.Rational(3, 2))
rhoFO_neg = rho.subs(t, 0).subs(xi, sp.Rational(-1, 10))
check("F2 FO's h_kappa at xi = -1/10 gives rho(0,0) > 0 (FO's state does not cover xi<0)",
      sp.simplify(rhoFO_neg) > 0, str(rhoFO_neg))

# ---- G: section attribution (page text read through alphaXiv, saved verbatim excerpt)
here = os.path.dirname(os.path.abspath(__file__))
txt = open(os.path.join(here, "..", "src", "1208.5399-sec5.txt"), encoding="utf-8").read()
s51 = txt.split("5.1 Nonminimal coupling", 1)[1].split("5.2 Interacting fields", 1)[0]
s52 = txt.split("5.2 Interacting fields", 1)[1].split("5.3 Singularity theorems", 1)[0]
check("G1 'arbitrarily negative energy density can be sustained over arbitrarily large spacetime volumes' is in Sec. 5.1",
      "arbitrarily negative energy density can be sustained over arbitrarily large spacetime volumes" in " ".join(s51.split()))
check("G2 'One cannot expect state-independent QEIs to hold' is in Sec. 5.2, not 5.1",
      "One cannot expect state-independent QEIs to hold" in " ".join(s52.split())
      and "cannot expect" not in s51)
check("G3 Sec. 5.1 never says 'no state-independent QEI'; its only 'state-independent' is 'state-independent terms' inside the state-dependent bound",
      "state-independent QEI" not in s51 and s51.count("state-independent") == 1
      and "state-independent terms" in s51 and "that are state-dependent [29]" in " ".join(s51.split()))
check("G4 Sec. 5.1 scopes the quantum argument to 'the case of Minkowski space'",
      "for the case of Minkowski space" in " ".join(s51.split()))

print("ALL PASS" if OK else "SOME FAIL")
sys.exit(0 if OK else 1)
