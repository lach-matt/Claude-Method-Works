#!/usr/bin/env python3
"""charged_reduced.py -- Model A, the charged variant (RN-AdS5 slab), every convention and orientation, exact.

Both planes neutral (the Maxwell flux continuous: the outer bulks carry the same charge q, Q = q^2), outer masses 0
(129/179: no corridor in either universe's own bulk).  For a two-sided plane the tt balance eta_s s + eta_o t = -2 tau
and s^2 - t^2 = F_s - F_o = (1 - lam^2) - mu u^2 (k and Q cancel) make s, t polynomial in (u, mu):
t = eta_o (D - 4 tau^2)/(4 tau), s = eta_s(-2 tau - eta_o t).  What is left per plane: t^2 = F_o and the angular
balance.  Two planes: four polynomial equations in (mu, Q, u1, u2); Groebner over Q (computed, exact), then the real
solutions filtered by u1, u2 > 0, Q > 0, s, t > 0.  Imports sads5_balance (this directory) for the conventions.
A second pass sets the outer charges to 0 (the planes then carry surface charge: matter, against clause (B)).
python3 charged_reduced.py [--both] [--all]   (cross-check of charged_param.py by Groebner bases)
"""
import itertools
import sys
import time

import sympy as sp

import sads5_balance as S

mu, Q = sp.symbols("mu Q", real=True)


def plane(kc, spec, uu, signs=None, q_outer=True):
    """Returns (equations, s, t) for one plane with the charged corridor (mu, Q) in the slab."""
    kind = spec[0]
    if kind == "Z2":
        eta, tau = spec[1], spec[2]
        F = kc * uu + 1 - mu * uu**2 + Q * uu**3
        s = -eta * tau
        return [sp.expand(F - tau**2), sp.expand(sp.diff(F, uu))], sp.Integer(s), sp.Integer(s)
    if kind == "two":
        eta_s, eta_o, lam2, mu_o, tau = spec[1:]
    else:
        lam2, mu_o, tau = spec[1:]
        eta_s, eta_o = signs
    Fs = kc * uu + 1 - mu * uu**2 + Q * uu**3
    Fo = kc * uu + lam2 - mu_o * uu**2 + (Q * uu**3 if q_outer else 0)
    if q_outer:
        D = sp.expand(Fs - Fo)
        t = eta_o * (D - 4 * tau**2) / (4 * tau)
        s = eta_s * (-2 * tau - eta_o * t)
        e1 = sp.expand(t**2 - Fo)
        e2 = sp.expand(eta_s * sp.diff(Fs, uu) * t + eta_o * sp.diff(Fo, uu) * s)
        return [e1, e2], s, t
    D = sp.expand(Fs - Fo)                         # now carries Q u^3
    t = eta_o * (D - 4 * tau**2) / (4 * tau)
    s = eta_s * (-2 * tau - eta_o * t)
    e1 = sp.expand(t**2 - Fo)
    e2 = sp.expand(eta_s * sp.diff(Fs, uu) * t + eta_o * sp.diff(Fo, uu) * s)
    return [e1, e2], s, t


def solve(kc, ours, p2, combo=None, q_outer=True):
    u1, u2 = sp.symbols("u1 u2", real=True)
    e1, s1, t1 = plane(kc, ours, u1, combo[:2] if combo else None, q_outer)
    e2, s2, t2 = plane(kc, p2, u2, combo[2:] if combo else None, q_outer)
    unk = [mu, Q, u1, u2]
    G = sp.groebner([sp.numer(sp.together(e)) for e in e1 + e2], *unk, order="lex")
    if G.exprs == [1]:
        return "inconsistent", G, []
    if not G.is_zero_dimensional:
        return "positive-dim", G, []
    cands = []
    for sol in sp.solve(G.exprs, unk, dict=True):
        v = {k: complex(sp.N(x, 40)) for k, x in sol.items()}
        if any(abs(z.imag) > 1e-25 for z in v.values()):
            continue
        r = {k: z.real for k, z in v.items()}
        sv = [complex(sp.N(sp.sympify(x).subs(sol), 40)).real for x in (s1, t1, s2, t2)]
        ok = r[u1] > 0 and r[u2] > 0 and r[Q] > 0 and all(x > 0 for x in sv)
        cands.append((sol, r, sv, ok))
    return "zero-dim", G, cands


def run(q_outer=True, verbose=True, names=("T1-M4", "T2-sheet")):
    C = S.conventions()
    t0 = time.time()
    out = []
    for name in names:
        cv = C[name]
        combos = [None] if cv["ours"][0] != "two*" else list(itertools.product((1, -1), repeat=4))
        for kc in (1, 0, -1):
            for combo in combos:
                st, G, cands = solve(kc, cv["ours"], cv["p2"], combo, q_outer)
                good = [x for x in cands if x[3]]
                out.append((name, kc, combo, st, G, cands, good))
                if verbose and (good or st != "inconsistent"):
                    tag = "%s k=%+d %s: %s" % (name, kc, combo, st)
                    if st == "positive-dim":
                        tag += "  G=" + str(G.exprs[:5])
                    print(tag, "| real candidates:",
                          [(dict((str(k), round(v, 6)) for k, v in x[1].items()), [round(y, 4) for y in x[2]], x[3])
                           for x in cands], flush=True)
    if verbose:
        print("q_outer=%s: admissible charged two-plane solutions: %d  (%.1f s)"
              % (q_outer, sum(len(r[6]) for r in out), time.time() - t0), flush=True)
    return out


if __name__ == "__main__":
    # default: the repository's mirrored-ours conventions (seconds); --all adds the board's V1/V2 variants (the
    # Groebner basis there runs for hours -- charged_param.py's parametrisation is the route for those)
    nm = ("T1-M4", "T2-sheet", "V1-T1", "V2-T2") if "--all" in sys.argv else ("T1-M4", "T2-sheet")
    run(q_outer=True, names=nm)
    if "--both" in sys.argv:
        run(q_outer=False, names=nm)
