#!/usr/bin/env python3
"""offrs_control.py -- control C2 for Model A (computed, exact up to the final real-root isolation): release our
tension from the RS value (tau1 = w unknown), keep position 2's at the convention's ratio to ours (T1: -1/8 on one
sheet, outer 1/L^2 = 9/16; T2: -1/4, outer 1/4), and ask whether the two balances then pin u1, u2, mu and w.
Ours mirrored (the LR orbifold plane): F1' = 0, sqrt F1 = w  =>  u1 = k/(2 mu), w^2 = 1 + k^2/(4 mu)  (k = +-1), so
mu = 1/(4 (w^2 - 1)) [k = 1 needs w > 1, k = -1 needs w < 1].  Position 2 (slab side R > a2, outer R < a2):
s2 - t2 = -2 r w,  s2 + t2 = (1 - lam2 - mu u2^2)/(s2 - t2); remaining: t2^2 = F_o and the angular balance.
Resultant in u2 -> a polynomial in w; real roots isolated exactly (sympy real_roots), back-substituted, filtered.
python3 offrs_control.py
"""
import sympy as sp

w, u2 = sp.symbols("w u2", real=True)


def run(kc, lam2, r):
    mu = 1 / (4 * (w**2 - 1)) if kc != 0 else None
    if kc == 0:
        return "k = 0: a mirrored plane in SAdS5 with mu != 0 has F' = -2 mu u != 0: no static ours at any tension"
    d = -2 * r * w                                   # s2 - t2
    S = (1 - lam2 - mu * u2**2) / d                  # s2 + t2
    s2, t2 = (S + d) / 2, (S - d) / 2
    Fs = kc * u2 + 1 - mu * u2**2
    Fo = kc * u2 + lam2
    e1 = sp.numer(sp.together(t2**2 - Fo))
    e2 = sp.numer(sp.together(sp.diff(Fs, u2) * t2 - sp.diff(Fo, u2) * s2))
    res = sp.Poly(sp.resultant(sp.expand(e1), sp.expand(e2), u2), w)
    roots = [x for x in sp.real_roots(res) if (x > 1 if kc == 1 else (0 < x < 1))]
    out = []
    for x0 in roots:
        xv = sp.N(x0, 40)
        cand_u = [z for z in sp.Poly(sp.expand(e1.subs(w, xv)), u2).nroots(n=30, maxsteps=2000)
                  if abs(sp.im(z)) < 1e-12]                 # 1e-12: double roots come back with ~1e-16 imaginary parts
        for z in cand_u:
            z = sp.re(z)
            if abs(sp.N(e2.subs({w: xv, u2: z}))) > 1e-12:
                continue
            m = sp.N(mu.subs(w, xv))
            vals = {"w=tau1*ell": xv, "mu/ell^2": m, "u1": sp.N(kc / (2 * m)), "u2": z,
                    "s2": sp.re(sp.N(s2.subs({w: xv, u2: z}))), "t2": sp.re(sp.N(t2.subs({w: xv, u2: z})))}
            ok = all(vals[k] > 0 for k in ("u1", "u2", "s2", "t2"))
            out.append((vals, ok, sp.Poly(sp.factor_list(res)[1][0][0], w) if False else None))
    return res.degree(), roots, out


if __name__ == "__main__":
    for name, lam2, r in (("T1", sp.Rational(9, 16), sp.Rational(-1, 8)), ("T2", sp.Rational(1, 4), sp.Rational(-1, 4))):
        for kc in (1, -1, 0):
            o = run(kc, lam2, r)
            if isinstance(o, str):
                print(name, kc, o)
                continue
            deg, roots, out = o
            print(name, "k=%+d" % kc, "resultant degree", deg, "admissible-range roots:", [sp.N(x, 12) for x in roots])
            for vals, ok, _ in out:
                print("    ", {k: float(v) for k, v in vals.items()}, "ADMISSIBLE" if ok else "not admissible")
