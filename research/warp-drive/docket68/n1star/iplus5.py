#!/usr/bin/env python3
"""iplus5.py -- [Hin26] section 11.2 in five dimensions: the structure at I+ and its formal solutions
(N1STAR-PROOF.md section 10.44; ROUTES 4.46; D112).

His Lemma 11.15 and Propositions 11.14 and 11.16 integrate, component by component, the I+ normal operator (11.34),
rho_I^-1 rho_+^-2 L_b = L_0 + L~, L_0 = -(rho_I d_rho_I - (I + A_0))(rho_I d_rho_I - rho_+ d_rho_+), L~ in rho_I
Diff^2_b, in his coordinates rho_I = t*/r, rho_+ = 1/t* (p. 235), with the b-ODE lemmas 2.12, 2.22, 2.23 (stated on
[0, 1) x H, H any compact manifold with corners, and on [0, 2)^2 x (-2, 2)^d).

  P1 (computed, exact) The leading part.  For the wave operator of R^(1,n) on u(t*, r) Y, Y a spherical harmonic of
     S^(n-1) with eigenvalue -kappa, t* = t - r: rho_I^-1 rho_+^-2 (-box/2) = -(rho_I d_rho_I - (n - 1)/2)(rho_I d_rho_I -
     rho_+ d_rho_+) + rho_I R, R a b-operator whose coefficients are polynomials in rho_I, rho_+, kappa: his I = 1 at
     n = 3, and 3/2 at n = 4, the conjugation r^-((n-1)/2) of 10.38(a).  The angular term and the potential lie in R.
     Control: the exponent claimed n/2.
  P2 (computed, exact) The bookkeeping in five dimensions, from scri5.py's five-dimensional A_0 (10.38(i)): A_0 lower
     triangular, diagonal 2 (1 - v) gam_C, (1 - v) gam_C, (1 - e_C)(1 - v) gam_C, (1 - e_Ups) gam_Ups, gam_Ups, 0,
     2 gam_Ups; the I+ exponents 3/2 + that diagonal; the exceptional exponents of the 11-component, 2 (the (7, 6)
     coupling, half an order below his) and 3/2 + (1 - e_Ups) gam_Ups (the (7, 4) coupling, his entry); and the
     non-resonance his Steps 1-3 need: 2 != 3/2 + 2 gam_Ups (gam_Ups != 1/4), (1 + e_Ups) gam_Ups != 0, and z - 3/2 -
     A_0 invertible for 3/2 + 2 gam_Ups < Re z < 3/2 + (1 - e_C)(1 - v) gam_C -- at the record's point (v, e_C, gam_C,
     e_Ups, gam_Ups) = (1/2, 1/102400, 10^6, 1/100, 1/100) the interval reaches past 5 x 10^5.  Control: four
     dimensions' exceptional exponents 1 and 1 + (1 - e_Ups) gam_Ups from his matrix with I = 1.
  P3 (computed, exact) Proposition 11.16's Steps 1-2 in five dimensions: for the ansatz chi rho_I^z u^(z,0) (dx^1)^2,
     z = 2 and 3/2 + (1 - e_Ups) gam_Ups, L_0 reduces to -(z - 3/2 - 2 gam_Ups)(z - rho_+ d_rho_+) on the 11-component,
     with nonzero coefficient; the solution of (rho_+ d_rho_+ - z) u = g from rho_+ = 1 adds (z, 0) at iota+ (Lemma
     2.12): E^#(1)_+ = E-breve_+ u {(2, 0)} u {(3/2 + (1 - e_Ups) gam_Ups, 0)}.  Control: the four-dimensional exponents.

Run: python3 iplus5.py --selftest | --mutants | --only k [--verbose]   (seconds).
"""
import sys
import time

import sympy as sp

from damping5 import Checklist
import scri5 as S5
import lin5
from sbar5 import v, eC, gC, eU, gU

_LIN = {"v": v, "eC": eC, "gC": gC, "eU": eU, "gU": gU}               # lin5.py's names for sbar5.py's symbols
POINT = {_LIN[k.name]: val for k, val in lin5.POINT.items()}

q, p, a, b, kap = sp.symbols("rho_I rho_+ a b kappa", positive=True)
HALF = sp.Rational(1, 2)


# ------------------------------------------------------------------------------------------------- P1
def leading(n, expo=None):
    """rho_I^-1 rho_+^-2 (-box/2) on q^a p^b Y, divided by q^a p^b, minus -(a - expo)(a - b): the remainder (his L
    is -box/2 to leading order, 2 L being wave-type)"""
    expo = sp.Rational(n - 1, 2) if expo is None else expo
    ts, r = sp.symbols("tstar r", positive=True)
    F = sp.Function("F")
    u = F(ts, r)
    box = sp.diff(u, r, 2) - 2 * sp.diff(u, r, ts) + (n - 1) / r * (sp.diff(u, r) - sp.diff(u, ts)) - kap * u / r**2
    mono = (ts / r)**a * (1 / ts)**b
    e = box.subs(u, mono).doit()
    e = sp.simplify(e / mono)
    e = e.subs({ts: 1 / p, r: 1 / (q * p)})
    e = sp.simplify(-e / (2 * q * p**2))
    rem = sp.expand(sp.simplify(e + (a - expo) * (a - b)))
    return rem


def c1(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    for n in (3, 4):
        expo = sp.Rational(n, 2) if control == 1 else None
        rem = leading(n, expo)
        num = sp.numer(sp.together(rem))
        den = sp.denom(sp.together(rem))
        ok = sp.Poly(den, q, p).is_monomial and sp.degree(den, q) == 0 and num.subs(q, 0) == 0
        chk(f"n = {n}: rho_I^-1 rho_+^-2 (-box/2) = -(rho_I d - {sp.Rational(n - 1, 2)})(rho_I d - rho_+ d) + rho_I R; "
            f"R = {sp.factor(sp.expand(rem / q))}", ok)
    return chk.ok


# ------------------------------------------------------------------------------------------------- P2
def exceptional(I0, A):
    """the 11-component's exceptional I+ exponents: the (7, 6) entry -(1/2) d_1(r h_ab), of I+ order I0 - 1, acts on
    pi-slash_0 u at I0, giving 2 I0 - 1 (his (1, 0), p. 228; 10.38(c)); the (7, 4) entry couples pi_01 u at I0 + (1 -
    e_U) gam_U"""
    return {2 * I0 - 1, I0 + A[3, 3]}


def c2(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    A = S5.five528()
    I0 = sp.Rational(3, 2) if control != 1 else sp.Integer(1)
    lower = all(A[i, j] == 0 for i in range(7) for j in range(i + 1, 7))
    diag = [sp.factor(A[i, i]) for i in range(7)]
    want = [2 * (1 - v) * gC, (1 - v) * gC, (1 - eC) * (1 - v) * gC, (1 - eU) * gU, gU, 0, 2 * gU]
    chk(f"A_0 lower triangular, diagonal {diag}", lower and all(sp.simplify(x - y) == 0 for x, y in zip(diag, want)))
    ex = exceptional(I0, A)
    chk(f"exceptional exponents of the 11-component {sorted(ex, key=str)}; the (7, 4) entry {sp.factor(A[6, 3])} nonzero",
        ex == {2, sp.Rational(3, 2) + (1 - eU) * gU} and sp.simplify(A[6, 3] - 2 * (1 - eU) * gU) == 0)
    ex4 = exceptional(sp.Integer(1), S5.his528())
    chk(f"control: four dimensions (I = 1, his (5.28)) gives his {sorted(ex4, key=str)} ((11.33a), p. 229)",
        ex4 == {1, 1 + (1 - eU) * gU})
    d11 = I0 + 2 * gU
    c_st1 = sp.factor(2 * I0 - 1 - d11)
    c_st2 = sp.factor(I0 + (1 - eU) * gU - d11)
    pt = dict(POINT)
    lo, hi = d11.subs(pt), (I0 + (1 - eC) * (1 - v) * gC).subs(pt)
    ups = [I0 + x for x in (0, (1 - eU) * gU, gU, 2 * gU)]
    cons = [I0 + x for x in want[:3]]
    ok_gap = all(u.subs(pt) <= lo for u in ups) and all(cc.subs(pt) >= hi for cc in cons)
    chk(f"Step 1's coefficient (2 I0 - 1) - (I0 + 2 gam_Ups) = {c_st1}, zero only at gam_Ups = 1/4; Step 2's {c_st2}; "
        f"at the point: {c_st1.subs(pt)}, {c_st2.subs(pt)}", sp.solve(c_st1, gU) == [sp.Rational(1, 4)]
        and c_st1.subs(pt) != 0 and c_st2.subs(pt) != 0)
    chk(f"z - 3/2 - A_0 invertible for {lo} < Re z < {float(hi):.6g} at the point (gauge exponents below, constraint "
        f"exponents above)", ok_gap and hi > 3)
    return chk.ok


# ------------------------------------------------------------------------------------------------- P3
def c3(control=0, verbose=False):
    chk = Checklist(verbose, quiet=control != 0)
    I0 = sp.Rational(3, 2) if control != 1 else sp.Integer(1)
    A = S5.five528()
    U = sp.Function("U")
    zs = sorted(exceptional(I0, A), key=str)
    for z in zs:
        u11 = U(p)
        inner = z * u11 - p * sp.diff(u11, p)                         # (rho_I d - rho_+ d)(rho_I^z u)/rho_I^z
        coeff = sp.factor(-(z - (I0 + A[6, 6])))                       # L_0's 11-entry on rho_I^z
        Lu = coeff * inner
        ok = sp.simplify(Lu - coeff * (z * u11 - p * sp.diff(u11, p))) == 0 and coeff.subs(dict(POINT)) != 0
        chk(f"z = {z}: L_0 on rho_I^z u (dx^1)^2 is {coeff} (z - rho_+ d_rho_+) u; nonzero at the point", ok)
    chk(f"E#(1)_+ adds {zs} at iota+ (his: 1 and 1 + (1 - e_Ups) gam_Ups)",
        set(zs) == {2, sp.Rational(3, 2) + (1 - eU) * gU})
    return chk.ok


CHECKS = [("P1 the leading part at I+: (rho_I d - (n - 1)/2)(rho_I d - rho_+ d), remainder in rho_I Diff_b; n = 3, 4", c1),
          ("P2 five-dimensional A_0: diagonal, exceptional exponents 2 and 3/2 + (1 - e_U) gam_U, non-resonance", c2),
          ("P3 Proposition 11.16's Steps 1-2: coefficients nonzero, E#(1)_+ = {(2, 0), (3/2 + (1 - e_U) gam_U, 0)}", c3)]


def run(only=None, verbose=False):
    ok = True
    for k, (name, f) in enumerate(CHECKS, 1):
        if only and k != only:
            continue
        t0 = time.time()
        res = f(0, verbose)
        ok &= res
        print(f"{name[:104]:<104} {'PASS' if res else 'FAIL'} {time.time() - t0:3.0f}s", flush=True)
    print(f"iplus5.py: {len(CHECKS) if ok else 'not all'}/{len(CHECKS)}")
    return ok


def mutants():
    caught = total = 0
    for name, f in CHECKS:
        total += 1
        res = f(1, False)
        caught += not res
        print(f"mutant 1 of {name[:2]}: {'caught' if not res else 'NOT caught'}", flush=True)
    print(f"iplus5.py mutants: {caught}/{total}")
    return caught == total


if __name__ == "__main__":
    args = sys.argv[1:]
    vb = "--verbose" in args
    if "--selftest" in args:
        sys.exit(0 if run(verbose=vb) else 1)
    elif "--mutants" in args:
        sys.exit(0 if mutants() else 1)
    elif "--only" in args:
        sys.exit(0 if run(int(args[args.index("--only") + 1]), vb) else 1)
    print(__doc__)
