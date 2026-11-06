#!/usr/bin/env python3
"""stagen5.py -- stage N's data (EQUALITY5-LAYER.md, Round 3, R3.4; open item O6 of rounds 1-2).

  S1 (READ, located by content; the file's md5 printed) N1STAR-PROOF.md: Theorem A of order N solves stages m = 1, ...,
     N, with gh_{N+1} from stage N (section 5.4); Lemma 6.2 states stage data "for every N", and its proof (as amended
     at D615, after this check first found it fixing stages m = 1, ..., N - 1 only) fixes stages m = 1, ..., N, noting
     that stage N's data are not needed for (F1), (F2) and that at m = N step (iii) runs inside Theorem A of order N
     (S3); Lemma 6.1 needs (F1) at orders 1, ..., N - 1 and (F2) at 1, ..., N - 2; Proposition 6.5 and section 6.4 take
     "the stage data of Lemma 6.2 with N := K + 3"; section 6.4 asserts the data equal the seed's on Sigma cap
     {r < v_start - tau0}.  Control: the pre-D615 wording (stages 1, ..., N - 1) is no longer present.
  S2 (exact, the weights of the supplement's Lemma 5.1) The lowest order at which each unknown of stage m enters the
     two-scale expansions: the gauge vector D (first order): m_m, phi_m and gh_{m+1} at order m; Ric^H: m_m, phi_m at
     m - 1 only through e_m (which stage m's own transport (b) makes zero), gh_{m+1} at m (the lam^-2 part of Ric^H
     vanishes on oscillating profiles); the constraint map (second order, through Ric): gh_{m+1} at m - 1 (through the
     lam^-2 part, the Pol-combination), m_m and phi_m at m - 1.  Hence stage N's data reach D only at orders >= N, past
     (F1) (orders <= N - 1) and (F2) (<= N - 2), and the constraint map at order >= N - 1, inside Lemma 6.1's bound
     O(lam^(N-2)): Theorems A, D and E hold for every smooth choice of stage N's data.  Control: stage N - 1's gh_N
     enters D at order N - 1, which (F1) constrains -- the same ledger does not call stage N - 1 free.
  S3 (exact) Lemma 6.2's step at m = N runs inside Theorem A of order N: after stage N, Rm^(N) = -(1/2) e_{N+1}
     d_th^2 W with e_{N+1} = -q_{N+1} independent of th, and its th-mean vanishes (W a sum of first and second
     harmonics), which is all step (iii) uses of the order-m residual.  Control: a th-dependent coefficient (cos th)
     gives a nonzero mean.
  S4 (computed, mpmath, unit constants; exp(-1/x) edge, lam = 1e-6, N = 9) The two choices -- the rule of Lemma 6.2 at
     m = N, or zero data for stage N -- change the approximant's top slice data at the very edge (x = 0.3 lam^(1/2)):
     the top term lam^(N+1) (N - 1) E^(N-2) of the first is larger than lam^N (N - 2) E^(N-3) of the second by a factor
     above 10 (the choice is visible at leading order there, R3.2 (e)).  Control: in the window (env = lam^14) the ratio
     is below 10^-1 (the expansion is ordered there; the choice enters at relative order lam/x^2).

Labels: S1 READ; S2, S3 computed (exact); S4 computed (mpmath, a model with unit constants).
Run: python3 checks/stagen5.py   (a few seconds)
"""
import hashlib
import os
import sys
import textwrap

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
PROOF = os.path.join(HERE, '..', 'N1STAR-PROOF.md')


def out(msg):
    print(textwrap.fill(msg, width=121, subsequent_indent="      ", break_on_hyphens=False), flush=True)


PINS = {
    "5.4 stages 1..N": "Solve stage 0 (5.1) and the stages m = 1, ..., N (Lemma 5.3), with gh_{N+1} from stage N",
    "6.2 statement": "For every N there are stage data for Theorem A satisfying (F1)",
    "6.2 proof range": "Stage m = 1, ..., N, everything of the earlier stages given",
    "6.2 stage N fixed": "(stage N's data are not needed for (F1), (F2) but are fixed here",
    "6.2 step at m = N": "at m = N step (iii) runs inside Theorem A of order N",
    "(F1)": "- (F1) D^(m)(X, th) = 0 for all th, m = 1, ..., N - 1;",
    "(F2)": "- (F2) d_tau <D^(m)> = 0, m = 1, ..., N - 2.",
    "6.5 uses 6.2": "Let the stage data be those of Lemma 6.2 with N >= K + 3",
    "6.4 uses 6.2": "Take the stage data of Lemma 6.2 with N := K + 3",
    "6.4 seed data": "equal to the seed's data on Sigma cap {r <",
}


def s1(control=False):
    raw = open(PROOF, 'rb').read()
    lines = raw.decode('utf-8').split('\n')
    if control:
        return any("Stage m = 1, ..., N - 1, everything of the earlier stages given" in ln for ln in lines)
    found = {}
    for key, pat in PINS.items():
        hits = [k + 1 for k, ln in enumerate(lines) if pat in ln]
        found[key] = hits
    ok = all(len(h) == 1 for h in found.values())
    out("  S1 N1STAR-PROOF.md md5 %s; lines: %s" % (hashlib.md5(raw).hexdigest(), "; ".join(
        "%s %s" % (k, ",".join(map(str, h)) or "missing") for k, h in found.items())))
    return ok


# --------------------------------------------------------------------------------------------------------- S2
# Weights (Lemma 5.1): a mean m_j has weight j; an oscillating profile gh_j weight j (W: 1); a derivative is d_X
# (weight 0), the phase derivative lam^-1 dv d_th (weight -1), or lam^(j-1) dphi_j d_th (weight j - 1); d_th needs an
# oscillating factor.  A monomial linear in the unknown: the unknown times derivatives (and, for phi_j, the factor W it
# differentiates).  Ric^H: its lam^-2 part on an oscillating profile vanishes (layerlin5 N1: g0^-1(dv, dv) = 0 and the
# gauge term), so two phase derivatives on one oscillating factor do not occur; Ric (the constraint map) keeps it.
def lowest(unknown, j, op):
    """lowest order at which the stage-m unknown of index j enters op, with its route"""
    best = []
    if unknown == "mean":                                  # m_j: weight j; no d_th on it
        best.append((j, "m_j with d_X"))
        if op in ("RicH", "Ric"):
            best.append((j - 1, "m_j(ell, ell) in e_j, against d_th^2 W"))   # (5.2): gbar^-1(du, du) d_th^2 (lam W)
    if unknown == "phase":                                 # lam^(j-1) dphi_j d_th acting on lam W (weight 1)
        best.append((j - 1 + 1, "dphi_j d_th W"))
        if op in ("RicH", "Ric"):
            best.append((j - 1 + 1 - 1, "dv x dphi_j d_th^2 W (in e_j)"))
    if unknown == "osc":                                   # gh_j, weight j
        best.append((j - 1, "lam^-1 d_th gh_j"))
        if op == "Ric":
            best.append((j - 2, "lam^-2 d_th^2 gh_j: the Pol-combination"))
    return min(best)


def s2(control=False):
    N = sp.Symbol('N', integer=True, positive=True)
    rows = {}
    for op in ("D", "RicH", "Ric"):
        for unk, jj in (("mean", N), ("phase", N), ("osc", N + 1)):
            o, route = lowest(unk, jj, op)
            rows[(op, unk)] = (sp.simplify(o - N), route)
    if control:
        o, _ = lowest("osc", N, "D")                    # stage N - 1's oscillating profile gh_N
        return sp.simplify(o - (N - 1)) > 0
    D_ok = all(rows[("D", u)][0] >= 0 for u in ("mean", "phase", "osc"))
    # Ric^H at order N - 1 only through e_N, which stage N's (b) makes zero; Ric (constraints) at order >= N - 1
    ric_ok = all(rows[("Ric", u)][0] >= -1 for u in ("mean", "phase", "osc"))
    ricH_e = rows[("RicH", "mean")][0] == -1 and rows[("RicH", "phase")][0] == -1 and rows[("RicH", "osc")][0] == 0
    out("  S2 lowest order - N at which stage N's unknowns enter: " + "; ".join(
        "%s %s: %s (%s)" % (op, u, v[0], v[1]) for (op, u), v in rows.items()) + ".  D: >= N, past (F1)'s N - 1: %s;"
        " constraint map: >= N - 1, inside O(lam^(N-2)): %s; Ric^H at N - 1 only through e_N: %s"
        % (D_ok, ric_ok, ricH_e))
    return D_ok and ric_ok and ricH_e


def s3(control=False):
    th, a1, b1, a2, b2, e = sp.symbols('theta a1 b1 a2 b2 e', real=True)
    W = a1*sp.cos(th) + b1*sp.sin(th) + a2*sp.cos(2*th) + b2*sp.sin(2*th)
    coeff = sp.cos(th) if control else e
    mean = sp.integrate(sp.expand(coeff*sp.diff(W, th, 2)), (th, 0, 2*sp.pi))/(2*sp.pi)
    ok = sp.simplify(mean) == 0
    if control:
        return ok
    out("  S3 the th-mean of e_(N+1) d_th^2 W (e_(N+1) independent of th, W first and second harmonics): %s" % mean)
    return ok


def s4(control=False):
    mp.mp.dps = 40
    lam = mp.mpf(10)**-6
    N = 9
    u = sp.Symbol('u')
    Ps = [sp.Integer(1)]
    for _ in range(N):
        Ps.append(sp.expand(u**2*(Ps[-1] - sp.diff(Ps[-1], u))))
    P = [sp.lambdify(u, p, 'mpmath') for p in Ps]
    ratio = {}
    for nm, x in (("edge", mp.mpf('0.3')*mp.sqrt(lam)), ("window", 1/(14*mp.log(1/lam)))):
        rule = lam**(N + 1)*(N - 1)*abs(P[N - 2](1/x))
        zero = lam**N*(N - 2)*abs(P[N - 3](1/x))
        ratio[nm] = rule/zero
    if control:
        return ratio["window"] > mp.mpf('1e-1')
    out("  S4 top slice data, Lemma 6.2's rule at m = N over zero data for stage N: at the very edge %s, in the window"
        " %s" % (mp.nstr(ratio["edge"], 6), mp.nstr(ratio["window"], 6)))
    return ratio["edge"] > 10


def main():
    ok = True
    for name, f in (("S1", s1), ("S2", s2), ("S3", s3), ("S4", s4)):
        good = f()
        ctl = f(control=True)
        out("%s %s%s" % (name, "PASS" if good and not ctl else "FAIL", " (control passed)" if ctl else ""))
        ok &= good and not ctl
    out("stagen5: %s" % ("all checks pass, every control fails" if ok else "FAILURES"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
