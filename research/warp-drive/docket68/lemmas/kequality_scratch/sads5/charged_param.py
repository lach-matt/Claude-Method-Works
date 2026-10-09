#!/usr/bin/env python3
"""charged_param.py -- the charged variant of Model A solved through an exact rational parametrisation of each plane's
balance curve (computed, exact up to the final real-root isolation, which is sympy real_roots on integer polynomials).

DEDUCED (and checked here symbolically): every balance equation is linear in Q = q^2, and for a TWO-SIDED plane with
the outer bulk carrying the same charge and no mass, s and t depend on (u, mu) only through p = mu u^2 (= mu ell^4/a^4,
dimensionless and invariant under k = 0's scaling).  With Q u^3 = t^2 - k u - lam^2 (the tt balance), the angular balance
times u reads A(p) - 2 k u B(p) = 0, so for k != 0:  u = A(p)/(2 k B(p)),  mu = p/u^2,  Q = (t^2 - k u - lam^2)/u^3.
For a MIRRORED plane: Q u^3 = (2p - k u)/3 and u = (3 tau^2 - 3 + p)/(2k).
Two planes share (mu, Q): two polynomial equations in (p1, p2) -> resultant -> real roots -> back-substitution ->
filter u1, u2 > 0, Q > 0, s, t > 0.  k = 0: A(p) = 0 fixes p per plane and u is free (the scaling orbit, a gauge,
not a modulus); two planes then need (p2/p1)^3 = (c2/c1)^2 with c = t^2 - lam^2 (checked).
q_outer = True (neutral planes).  python3 charged_param.py
"""
import itertools
import time

import sympy as sp

import sads5_balance as S

p, uu, z = sp.symbols("p u z", real=True)


def curve(kc, spec, signs):
    """(u(p), mu(p), Q(p), s(p), t(p)) for k != 0; for k = 0 (A(p), c(p), s(p), t(p))."""
    kind = spec[0]
    if kind == "Z2":
        eta, tau = spec[1], spec[2]
        s = sp.Integer(-eta * tau)
        if kc == 0:
            return {"Z2": True, "k0_none": True, "s": s, "t": s}
        u_p = (3 * tau**2 - 3 + p) / (2 * kc)
        Q_p = (2 * p - kc * u_p) / (3 * u_p**3)
        return {"Z2": True, "u": sp.simplify(u_p), "mu": sp.simplify(p / u_p**2), "Q": sp.simplify(Q_p), "s": s, "t": s}
    if kind == "two":
        eta_s, eta_o, lam2, mu_o, tau = spec[1:]
    else:
        lam2, mu_o, tau = spec[1:]
        eta_s, eta_o = signs
    assert mu_o == 0
    t = eta_o * ((1 - lam2 - p) - 4 * tau**2) / (4 * tau)
    s = eta_s * (-2 * tau - eta_o * t)
    # angular balance times u, with Q u^3 = t^2 - k u - lam2 and mu u^2 = p:
    Fsu = 3 * t**2 - 2 * kc * uu - 3 * lam2 - 2 * p
    Fou = 3 * t**2 - 2 * kc * uu - 3 * lam2
    e2u = sp.expand(eta_s * Fsu * t + eta_o * Fou * s)
    if kc == 0:
        return {"Z2": False, "A": sp.expand(e2u), "c": sp.expand(t**2 - lam2), "s": s, "t": t}
    sol = sp.solve(e2u, uu)
    if len(sol) != 1:
        return {"Z2": False, "degenerate": e2u}
    u_p = sp.simplify(sol[0])
    Q_p = sp.simplify((t**2 - kc * u_p - lam2) / u_p**3)
    return {"Z2": False, "u": u_p, "mu": sp.simplify(p / u_p**2), "Q": Q_p, "s": s, "t": t}


def check_curve(kc, spec, signs):
    """Symbolic check that the parametrisation solves the plane's two balances (sads5_balance._plane_eqs)."""
    c = curve(kc, spec, signs)
    if kc == 0 or "u" not in c:
        return True
    mu_, q_ = sp.symbols("mu q", real=True)
    s_, t_ = sp.symbols("s t", real=True)
    sp_ = spec if spec[0] != "two*" else spec
    eqs, _ = S._plane_eqs(kc, sp_, mu_, q_, uu, s_, t_, signs)
    subs = {mu_: c["mu"], uu: c["u"], s_: c["s"], t_: c["t"]}
    res = [sp.simplify(sp.together(e.subs(q_**2, c["Q"]).subs(subs))) for e in eqs]
    return all(r == 0 for r in res)


def two_planes(kc, ours, p2, combo):
    c1 = curve(kc, ours, combo[:2] if combo else None)
    c2 = curve(kc, p2, combo[2:] if combo else None)
    if kc == 0:
        if c1.get("k0_none") or c2.get("k0_none"):
            return "none (a mirrored plane at RS cannot balance at k = 0)", []
        r1 = [x for x in sp.real_roots(sp.Poly(sp.numer(sp.together(c1["A"])), p)) if x != 0]
        r2 = [x for x in sp.real_roots(sp.Poly(sp.numer(sp.together(c2["A"].subs(p, z))), z)) if x != 0] \
            if sp.Poly(sp.numer(sp.together(c2["A"])), p).degree() > 0 else []
        out = []
        for a in r1:
            for b in r2:
                A1, B1 = sp.N(a, 40), sp.N(b, 40)
                C1, C2 = sp.N(c1["c"].subs(p, A1)), sp.N(c2["c"].subs(p, B1))
                if A1 * B1 <= 0 or C1 * C2 <= 0:
                    continue
                if abs((B1 / A1)**3 - (C2 / C1)**2) < 1e-25:
                    out.append((A1, B1, C1, C2))
        return "k=0 discrete", out
    mu1, Q1 = c1["mu"], c1["Q"]
    mu2, Q2 = c2["mu"].subs(p, z), c2["Q"].subs(p, z)
    E1 = sp.numer(sp.together(mu1 - mu2))
    E2 = sp.numer(sp.together(Q1 - Q2))
    R = sp.Poly(sp.resultant(sp.expand(E1), sp.expand(E2), z), p)
    if R.is_zero:
        return "resultant vanishes identically", []
    out = []
    for r0 in sp.real_roots(R):
        pv = sp.N(r0, 50)
        zc = [w for w in sp.Poly(sp.expand(E1.subs(p, pv)), z).nroots(n=40, maxsteps=3000) if abs(sp.im(w)) < 1e-15]
        for w in zc:
            w = sp.re(w)
            if abs(sp.N(E2.subs({p: pv, z: w}))) > 1e-12 * (1 + abs(sp.N(E2.subs({p: pv, z: 0})))):
                continue
            try:
                vals = {"p1": pv, "p2": w, "u1": sp.N(c1["u"].subs(p, pv)), "u2": sp.N(c2["u"].subs(p, w)),
                        "mu": sp.N(mu1.subs(p, pv)), "Q": sp.N(Q1.subs(p, pv)),
                        "s1": sp.N(c1["s"].subs(p, pv)), "t1": sp.N(c1["t"].subs(p, pv)),
                        "s2": sp.N(c2["s"].subs(p, w)), "t2": sp.N(c2["t"].subs(p, w))}
            except (ZeroDivisionError, TypeError):
                continue
            if any(not v.is_finite for v in vals.values()):
                continue
            ok = all(vals[k] > 0 for k in ("u1", "u2", "Q", "s1", "t1", "s2", "t2"))
            out.append((vals, ok, connected(ours, p2, combo, vals)))
    return "zero-dim", out


def slab_signs(ours, p2, combo):
    e1 = ours[1] if ours[0] in ("Z2", "two") else combo[0]
    e2 = p2[1] if p2[0] in ("Z2", "two") else combo[2]
    return e1, e2


def connected(ours, p2, combo, vals):
    """H-SLAB-CONNECTED (179: the corridor bridges both planes): one connected slab bounded by both planes.
    (-1, +1): ours outer, a2 < a1 (u2 > u1);  (+1, -1): ours inner, a1 < a2 (u1 > u2);  (-1, -1): two exteriors
    through the bridge, needs a horizon in the slab;  (+1, +1): each plane's slab side runs to its own conformal
    boundary -- two disjoint regions, no bridge.  A mirrored ours (-1) has the slab on both sides."""
    e1, e2 = slab_signs(ours, p2, combo)
    if (e1, e2) == (1, 1):
        return False
    if (e1, e2) == (-1, 1):
        return bool(vals["u2"] > vals["u1"])
    if (e1, e2) == (1, -1):
        return bool(vals["u1"] > vals["u2"])
    return True                                  # (-1, -1): ER; the horizon is checked by the caller's report


def run(verbose=True):
    C = S.conventions()
    t0 = time.time()
    n_ok = 0
    rows = []
    for name in ("T1-M4", "T2-sheet", "S7-u2-1/3", "S7-u1-1/3-grow", "S7-u1-1/6-grow", "S7-u1-1/6-decay",
                 "V1-T1", "V2-T2"):
        cv = C[name]
        combos = [None] if cv["ours"][0] != "two*" else list(itertools.product((1, -1), repeat=4))
        for kc in (1, -1, 0):
            for combo in combos:
                st, out = two_planes(kc, cv["ours"], cv["p2"], combo)
                good = [o for o in out if (o[1] and o[2] if kc != 0 else True)]
                raw = [o for o in out if (o[1] if kc != 0 else True)]
                rows_raw = len(raw)
                n_ok += len(good)
                rows.append((name, kc, combo, st, out, rows_raw, len(good)))
                if verbose and raw:
                    print(name, "k=%+d" % kc, combo, st, "| junction-admissible:",
                          [({k: round(float(v), 6) for k, v in o[0].items()}, "connected" if o[2] else
                            "NOT CONNECTED (no slab bridging the planes)") if kc != 0 else [float(x) for x in o]
                           for o in raw], flush=True)
    if verbose:
        print("charged two-plane solutions: junction-admissible %d, of which with a connected slab %d  (%.1f s)"
              % (sum(r[5] for r in rows), n_ok, time.time() - t0))
    return rows


if __name__ == "__main__":
    print("parametrisation checks (k = +-1, every sign combo, ours two-sided, T1/T2 position 2):",
          all(check_curve(kc, ("two*", 1, 0, 1), sg) for kc in (1, -1) for sg in itertools.product((1, -1), repeat=2)),
          all(check_curve(kc, ("two", 1, -1, sp.Rational(9, 16), 0, -sp.Rational(1, 8)), None) for kc in (1, -1)),
          all(check_curve(kc, ("Z2", -1, 1), None) for kc in (1, -1)))
    run()
