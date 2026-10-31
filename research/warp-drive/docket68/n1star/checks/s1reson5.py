"""s1reson5.py -- LOSS-D LD9 (D412): is the rho^(2 + d1) term of the s1 state forced by the local expansion?

The s1 state of III.D'' Proposition 3.1 is omega = dx^1 + w on Tangherlini, with box^Ups omega = 0 and w in
A^((2,0) u (2 + E_ind)). Here, with genstates5.py's box^Ups (polar coordinates, E^Ups at the trace weight 2/3,
c = r^-1 dt):

  R1 (exact) the indicial matrix I(lam) of the flat operator on w = r^-lam (kappa C dt + alpha C dr - beta r S dchi)
     (C = cos chi, S = sin chi, the l = 1 harmonic), free of r and chi; det I(lam) = lam (lam - 4) q(lam) with q's root
     lam_s1,2 = 2 + z/12 + O(z^2), z = 4 e gam^2; det I(2) = 16 e gam^2 = 4z.
  R2 (exact) the forcing box^Ups_Tangherlini(dx^1) starts at rho^4 = rho^(2 + 2), the order resonant with the root
     2 + d1: F4 = mu (-2 gam (e + 2), -3, 1) on (dt, dr, chi).
  R3 (exact) at z = 0 the left null vector of I(2) is (0, 1, 3) and annihilates F4, so the forcing is not resonant:
     the particular solution -I(2)^-1 F4 = mu (0, (e - 4)/(4e), -(e + 4)/(4e)) stays finite as z -> 0 at fixed e
     (-99.75 mu, -100.25 mu at the record's point).
  Control: a forcing with a nonzero component along (0, 1, 3) gives a particular solution of order 1/z.
So the local expansion does not force a rho^(2 + d1) term: its coefficient is that of the homogeneous solution, fixed
by regularity at the horizon. Labels: computed (exact, sympy).

    python3 checks/s1reson5.py [--selftest]
"""
import os
import sys

import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import genstates5 as GS   # noqa: E402

r, ch, mu, gU, eU = GS.r, GS.ch, GS.mu, GS.gU, GS.eU
lam = sp.Symbol("lam")
rho = sp.Symbol("rho", positive=True)


def indicial():
    ka, al, be = sp.symbols("kappa alpha beta")
    C, S = sp.cos(ch), sp.sin(ch)
    w = [ka*C*r**-lam, al*C*r**-lam, -be*r*S*r**-lam, 0, 0]
    B = GS.boxU(w, GS.geo(4, True))
    comp = [sp.simplify(B[0]/(C*r**(-lam - 2))), sp.simplify(B[1]/(C*r**(-lam - 2))),
            sp.simplify(B[2]/(-r*S*r**(-lam - 2)))]
    return sp.Matrix(3, 3, lambda i, j: sp.expand(sp.diff(comp[i], (ka, al, be)[j])))


def forcing():
    C, S = sp.cos(ch), sp.sin(ch)
    F = GS.boxU([0, C, -r*S, 0, 0], GS.geo(4, False))
    Fc = [sp.simplify(F[0]/C), sp.simplify(F[1]/C), sp.simplify(F[2]/(-r*S))]
    ser = [sp.series(q.subs(r, 1/rho), rho, 0, 6).removeO() for q in Fc]
    return [[sp.factor(s.coeff(rho, k)) for s in ser] for k in range(6)], all(GS.zero(q) for q in F[3:])


def main():
    ok = {}
    z = 4*eU*gU**2
    I = sp.Matrix(indicial())
    ok["R1 form"] = all(q.free_symbols <= {lam, gU, eU} for q in I)
    det = sp.factor(I.det())
    q = sp.cancel(det/(lam*(lam - 4)))
    lam_s12 = (1 + sp.sqrt(17 + 2*z - 2*sp.sqrt(z**2 + 4*z + 16)))/2
    pt = {gU: sp.Rational(1, 100), eU: sp.Rational(1, 100)}
    ok["R1 root"] = abs(sp.N(q.subs(lam, lam_s12).subs(pt), 40)) < 1e-30
    I2 = I.subs(lam, 2)
    ok["R1 det I(2) = 4z"] = sp.simplify(I2.det() - 4*z) == 0
    rows, angular_zero = forcing()
    ok["R2"] = all(all(v == 0 for v in rows[k]) for k in (0, 1, 2, 3, 5)) and angular_zero and \
        sp.simplify(sp.Matrix(rows[4]) - mu*sp.Matrix([-2*gU*(eU + 2), -3, 1])) == sp.zeros(3, 1)
    F4 = sp.Matrix(rows[4])
    ell = sp.Matrix([[0, 1, 3]])
    ok["R3 null"] = (ell*I2.subs(gU, 0)).applyfunc(sp.simplify) == sp.zeros(1, 3) and sp.simplify((ell*F4)[0]) == 0
    cpart = (-I2.inv()*F4).applyfunc(sp.simplify)
    ok["R3 finite"] = sp.simplify(cpart - mu*sp.Matrix([0, (eU - 4)/(4*eU), -(eU + 4)/(4*eU)])) == sp.zeros(3, 1)
    Fbad = F4 + sp.Matrix([0, 0, mu])
    cbad = (-I2.inv()*Fbad).applyfunc(sp.simplify)
    ok["control"] = any(sp.limit(sp.simplify(c*z), gU, 0) != 0 for c in cbad)
    print("  R1: det I(lam) =", det)
    print("  R2: forcing at rho^4 (dt, dr, chi):", list(F4))
    print("  R3: (0,1,3).F4 = %s; -I(2)^-1 F4 = %s; at gam = e = 1/100: %s"
          % (sp.simplify((ell*F4)[0]), list(cpart), [sp.N(c.subs(pt), 6) for c in cpart]))
    for k, val in ok.items():
        print(k, "PASS" if val else "FAIL")
    if "--selftest" in sys.argv:
        sys.exit(0 if all(ok.values()) else 1)


if __name__ == "__main__":
    main()
