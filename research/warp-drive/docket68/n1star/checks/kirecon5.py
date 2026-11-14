#!/usr/bin/env python3
"""kirecon5.py -- c7: supplement Proposition 10.1 (iii)'s coefficients, bounded on r >= r_h uniformly in l, computed.

(10.1) reconstructs a scalar mode's gauge invariants from [KI03]'s master field Phi at n = 3, with m = l (l + 2) - 3 >=
5, x = mu/r^2, H = m + 6 x, f = 1 - x, Phi~ = r^(3/2) H Phi:

    r F = (1/(12 r^2 H)) [ (2H - 3 r f') Phi~ + 6 r Dr . DPhi~ ],
    r F_ab + r F g_ab = (1/H) ( D_a D_b Phi~ - (1/2) (box Phi~) g_ab ),

D the orbit metric's derivative. In ingoing Eddington-Finkelstein coordinates (v, r), g_ab = -f dv^2 + 2 dv dr, regular
at the horizon r_h = mu^(1/2), the components of r F_ab and r F are computed as combinations of psi := r^(3/2) Phi =
Phi~/H and its derivatives to order two. Each coefficient is rewritten with m = H - 6x as a Laurent polynomial in H and
r (mu fixed), and its monomials H^a r^b are read off.

  P1 (exact) Every coefficient of the traceless bracket [] = r F_ab + r F g_ab is a sum of monomials H^a r^b with a <= 0
     and b <= 0, so bounded on r >= r_h uniformly in l (H >= 5); so is every coefficient of r F except that of psi
     itself, which is m/(6 r^2) plus such monomials: the factor m of Proposition 10.1 (iii), two angular derivatives on
     the sphere of radius r (its Laplacian's eigenvalue is -(m + 3)/r^2), entering r F_ab = [] - r F g_ab only through
     the trace (so not r F_rr, g_rr = 0). With F_ab = (r F_ab)/r and the spheres' orthonormal components 2 F S of h_S,
     every component of h_S is so bounded; the tensor type's, 2 H_T T = 2 r^(-3) psi T, trivially. So the
     proposition's 'coefficients bounded on r >= r_h uniformly in l' holds for the master field normalised as psi =
     r^(3/2) Phi, with the factor m counted as two angular derivatives; psi is not a field [HKW18] bound (P2).
  P2 (exact) The fields [HKW18] bound (arXiv:1809.05144): Phi itself, of which their r^p energies are taken ((124),
     p. 43, Phi := r^(n/2) Psi; (127), p. 46), and phi = r^(-3/2) Phi, the pointwise norm of their scalar master
     quantity (r^(1/2) Phi) Y_ab ((173), p. 60; k = (4 - n)/2, p. 61). Every coefficient is a sum of H^a r^b with
     a <= 0 and b <= 3/2 in Phi, b <= 3 in phi (but the factor m), uniformly in l, and those powers are attained
     (r F_rr's d_r^2 coefficient): in the fields their energies control the coefficients grow as r^(3/2) and r^3,
     so the decay passes to the metric components on each region r <= R; uniformly in r it is not shown. Control: the
     bound r^1 in Phi must fail.
  P1's control: the same monomial test run on the components as combinations of Phi itself (r = s^2, so half-integer
     powers of r are read exactly): the coefficient of d_r^2 Phi in r F_rr is r^(3/2), unbounded on r >= r_h, so the test
     must reject it; a monomial reader that found nothing would pass the control and fail main(). A coefficient whose
     denominator is not a monomial in H and r raises (there is no fallback).

Labels: computed (exact, sympy).

Run: python3 checks/kirecon5.py   (about half a minute)
"""
import sys

import sympy as sp

v, r, mu, m, Hs = sp.symbols("v r mu m H", positive=True)
X = [v, r]


def reconstruction(field):
    """(r F, r F_ab) as expressions in the jets of the field: psi (r^(3/2) Phi), Phi, or phi (r^(-3/2) Phi)"""
    f = 1 - mu/r**2
    g = sp.Matrix([[-f, 1], [1, 0]])
    gi = g.inv()
    Gam = [[[sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(2))/2 for c in range(2)] for b in range(2)] for a in range(2)]
    H = m + 6*mu/r**2
    u = sp.Function("u")(v, r)
    Pt = {"psi": H*u, "Phi": r**sp.Rational(3, 2)*H*u, "phi": r**3*H*u}[field]          # Phi~
    dP = [sp.diff(Pt, x) for x in X]
    DD = [[sp.diff(Pt, X[a], X[b]) - sum(Gam[c][a][b]*dP[c] for c in range(2)) for b in range(2)] for a in range(2)]
    box = sum(gi[a, b]*DD[a][b] for a in range(2) for b in range(2))
    Drdp = sum(gi[1, b]*dP[b] for b in range(2))                      # Dr . DPhi~ = g^(r b) d_b Phi~
    rF = ((2*H - 3*r*sp.diff(f, r))*Pt + 6*r*Drdp)/(12*r**2*H)
    brk = [[(DD[a][b] - box*g[a, b]/2)/H for b in range(2)] for a in range(2)]        # traceless, r F_ab + r F g_ab
    rFab = [[brk[a][b] - rF*g[a, b] for b in range(2)] for a in range(2)]
    return u, rF, rFab, brk


def jets(e, u):
    J = {u: "u"}
    for i in range(3):
        for j in range(3 - i):
            if i + j:
                J[sp.Derivative(u, *([v]*i + [r]*j))] = "u_" + "v"*i + "r"*j
    J[sp.Derivative(u, r, v)] = "u_vr"                                # the mixed derivative in either order
    sym = {k: sp.Symbol(nm) for k, nm in J.items()}
    x = sp.expand(e.doit()).xreplace(sym)
    out = {}
    for s_ in set(sym.values()):
        out[str(s_)] = sp.expand(x.coeff(s_))
    rest = sp.simplify(x - sum(out[str(s_)]*s_ for s_ in set(sym.values())))
    assert rest == 0, rest
    return {k: c for k, c in out.items() if c != 0}


def monomials(c):
    """the monomials H^a r^b of c with m = H - 6 mu/r^2, mu kept as a constant; r = s^2, so b may be a half-integer"""
    s = sp.Symbol("s", positive=True)
    x = sp.expand(sp.together(c.subs(m, Hs - 6*mu/r**2).subs(r, s**2)))
    num, den = sp.fraction(sp.factor(x))
    out = []
    dpoly = sp.Poly(den, Hs, s)
    if len(dpoly.terms()) != 1:
        return None                                                   # the denominator is not a monomial
    (da, db), dc = dpoly.terms()[0]
    for (a, b), cc in sp.Poly(sp.expand(num), Hs, s).terms():
        out.append((a - da, sp.Rational(b - db, 2)))
    return out


SHIFT = {"psi": 0, "Phi": sp.Rational(3, 2), "phi": 3}


def check(field, bmax=0):
    """every coefficient a sum of H^a r^b with a <= 0 and b <= bmax, but the factor m of r F's u-coefficient; returns
    (ok, worst, the largest r-power met outside that factor)"""
    u, rF, rFab, brk = reconstruction(field)
    worst = {}
    ok = True
    top = None
    items = [("rF", rF, True)]
    items += [("[]_%s%s" % ("vr"[a], "vr"[b]), brk[a][b], False) for a in range(2) for b in range(a, 2)]
    items += [("rF_%s%s" % ("vr"[a], "vr"[b]), rFab[a][b], True) for a in range(2) for b in range(a, 2)]
    for name, e, allow in items:
        for jet, c in jets(e, u).items():
            mons = monomials(c)
            if mons is None:
                raise ValueError("%s %s %s: denominator not a monomial in H, r" % (field, name, jet))
            free = [(a, b) for a, b in mons if not (allow and jet == "u" and a == 1 and b <= -2 + SHIFT[field])]
            bad = [(a, b) for a, b in free if not (a <= 0 and b <= bmax)]
            if free:
                top = max(b for _, b in free) if top is None else max(top, max(b for _, b in free))
            worst[(name, jet)] = "max H-power %s, max r-power %s" % (max(a for a, _ in mons), max(b for _, b in mons))
            ok &= not bad
    return ok, worst, top


def p1(control=False):
    ok, worst, _ = check("Phi" if control else "psi")
    if control:
        print("  control (in Phi, same monomial test): r F_rr's d_r^2 coefficient has %s; test rejects: %s"
              % (worst[("rF_rr", "u_rr")], not ok), flush=True)
        return ok
    print("  P1: coefficients in psi = r^(3/2) Phi, as monomials H^a r^b:", flush=True)
    for (name, jet), w in sorted(worst.items()):
        print("      %-6s %-5s %s" % (name, jet, w), flush=True)
    return ok


def p2(control=False):
    """the fields [HKW18] bound: Phi (their r^p energies, of r^(n/2) Psi, (124), (127)) and phi = r^(-3/2) Phi (the
    pointwise norm of their master quantity (r^(1/2) Phi) Y, (173)): the coefficients are O(r^(3/2)) and O(r^3),
    uniformly in l (H-power <= 0), and those powers are attained"""
    if control:
        ok, _, top = check("Phi", 1)                                       # the bound r^1 in Phi must fail
        print("  P2 control: in Phi with the bound r^1 the test passes: %s (largest r-power %s)" % (ok, top), flush=True)
        return ok
    ok1, _, t1 = check("Phi", SHIFT["Phi"])
    ok2, _, t2 = check("phi", SHIFT["phi"])
    print("  P2: in Phi every coefficient is O(r^(3/2)) uniformly in l: %s, largest r-power %s; in phi = r^(-3/2) Phi"
          " O(r^3): %s, largest r-power %s" % (ok1, t1, ok2, t2), flush=True)
    return ok1 and ok2 and t1 == SHIFT["Phi"] and t2 == SHIFT["phi"]


CHECKS = [("P1", p1), ("P2", p2)]


def main():
    ok = True
    for name, f in CHECKS:
        good = f()
        ctl = f(control=True)
        print("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""),
              flush=True)
        ok &= good and not ctl
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
