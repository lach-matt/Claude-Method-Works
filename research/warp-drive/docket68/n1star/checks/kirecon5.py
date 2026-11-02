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
     r^(3/2) Phi (the field whose energy [HKW18] bounds carries this weight), with the factor m counted as two angular
     derivatives.
  Control: the same components as combinations of Phi itself: the coefficient of d_r^2 Phi in r F_rr is r^(3/2),
     unbounded on r >= r_h, so the normalisation matters and the check sees it.

Labels: computed (exact, sympy).

Run: python3 checks/kirecon5.py   (a few seconds)
"""
import sys

import sympy as sp

v, r, mu, m, Hs = sp.symbols("v r mu m H", positive=True)
X = [v, r]


def reconstruction(field):
    """(r F, r F_ab) as expressions in the jets of the field: psi (r^(3/2) Phi) or Phi"""
    f = 1 - mu/r**2
    g = sp.Matrix([[-f, 1], [1, 0]])
    gi = g.inv()
    Gam = [[[sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b]) - sp.diff(g[b, c], X[d]))
                 for d in range(2))/2 for c in range(2)] for b in range(2)] for a in range(2)]
    H = m + 6*mu/r**2
    u = sp.Function("u")(v, r)
    Pt = H*u if field == "psi" else r**sp.Rational(3, 2)*H*u          # Phi~
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
    """the monomials H^a r^b of c with m = H - 6 mu/r^2, mu kept as a constant"""
    x = sp.expand(sp.together(c.subs(m, Hs - 6*mu/r**2)))
    num, den = sp.fraction(sp.factor(x))
    out = []
    dpoly = sp.Poly(den, Hs, r)
    if len(dpoly.terms()) != 1:
        return None                                                   # the denominator is not a monomial
    (da, db), dc = dpoly.terms()[0]
    for (a, b), cc in sp.Poly(sp.expand(num), Hs, r).terms():
        out.append((a - da, b - db))
    return out


def check(field):
    u, rF, rFab, brk = reconstruction(field)
    worst = {}
    ok = True
    items = [("rF", rF, True)]
    items += [("[]_%s%s" % ("vr"[a], "vr"[b]), brk[a][b], False) for a in range(2) for b in range(a, 2)]
    items += [("rF_%s%s" % ("vr"[a], "vr"[b]), rFab[a][b], True) for a in range(2) for b in range(a, 2)]
    for name, e, allow in items:
        for jet, c in jets(e, u).items():
            mons = monomials(c) if field == "psi" else None
            if mons is None:
                p_r = sp.limit(sp.log(abs(c.subs({m: 7, mu: 1})))/sp.log(r), r, sp.oo)
                worst[(name, jet)] = "r^%s" % p_r
                ok &= p_r <= 0
                continue
            bad = [(a, b) for a, b in mons if not (a <= 0 and b <= 0)
                   and not (allow and jet == "u" and a == 1 and b <= -2)]
            worst[(name, jet)] = "max H-power %d, max r-power %d" % (max(a for a, _ in mons), max(b for _, b in mons))
            ok &= not bad
    return ok, worst


def p1(control=False):
    ok, worst = check("Phi" if control else "psi")
    if control:
        print("  control (in Phi): r F_rr's d_r^2 coefficient grows as %s" % worst[("rF_rr", "u_rr")], flush=True)
        return ok
    print("  P1: coefficients in psi = r^(3/2) Phi, as monomials H^a r^b:", flush=True)
    for (name, jet), w in sorted(worst.items()):
        print("      %-6s %-5s %s" % (name, jet, w), flush=True)
    return ok


CHECKS = [("P1", p1)]


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
