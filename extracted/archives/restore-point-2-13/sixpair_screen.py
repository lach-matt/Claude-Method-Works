#!/usr/bin/env python3
"""sixpair_screen.py — the corridor's own screen for candidate replacement terms.

Registers 1371, 1372, 1394.

THE IDENTITY (1371). Write the spin-orbit expectation in closed form:
    <L.S> = l/2            for j = l + 1/2   (spin-parallel)
    <L.S> = -(l+1)/2       for j = l - 1/2   (spin-antiparallel)
For any two levels of ONE oscillator shell with l_hi = l_lo + 2, the higher
spin-antiparallel and the lower spin-parallel:
    D[l(l+1)] = 4*l_lo + 6        D<L.S> = -(l_lo + 3/2)
so the ratio is 4 for every l -- an identity, not an accident on three pairs.
With E = HO + beta*l(l+1) - alpha*<L.S> the pair inequality collapses to
    (l_lo + 3/2) * (4*beta + alpha)
and since l_lo + 3/2 > 0 always, such a pair fixes the sign of the single
combination 4*beta + alpha and nothing else. On these pairs the two-parameter
family is a one-parameter family.

THE SCREEN (1372, 1394). A candidate term gamma*T enters each inequality as
gamma*DT, and everything else has already collapsed. So gamma*T restores
feasibility only if DT is NON-DEGENERATE across the six pairs -- it must separate
the three demanding positive from the three demanding negative.

The correct test is 2-D LINEAR FEASIBILITY, not sign-matching: the six vectors
(DS', DT) must lie strictly within one open half-plane. Register 1394 records
that a sign-matching screen passed the controls when it should have failed them,
because on these pairs l(l+1) and <L.S> are PROPORTIONAL -- which is the ratio-4
identity itself. Without the controls, two viable candidates would have been
reported. The controls are therefore run on every invocation, not optionally.

Exact rational arithmetic throughout. No fitting, no sampling.
"""
from fractions import Fraction as F
import itertools
import sys

# ---------------------------------------------------------------------------
# levels: label -> (n, l, t) with t = +1 spin-parallel (j = l+1/2), -1 anti
# ---------------------------------------------------------------------------
LEVELS = {
    "2s1/2":  (2, 0, +1), "1d3/2": (1, 2, -1), "2d5/2": (2, 2, +1),
    "2p3/2":  (2, 1, +1), "1f5/2": (1, 3, -1), "2f7/2": (2, 3, +1),
    "3p3/2":  (3, 1, +1), "2f5/2": (2, 3, -1), "3s1/2": (3, 0, +1),
    "2d3/2":  (2, 2, -1), "1g7/2": (1, 4, -1), "1h9/2": (1, 5, -1),
}

def N_shell(lab):
    n, l, _ = LEVELS[lab]
    return 2 * (n - 1) + l

def ls(lab):
    _, l, t = LEVELS[lab]
    return F(l, 2) if t > 0 else F(-(l + 1), 2)

def cent(lab):
    _, l, _ = LEVELS[lab]
    return F(l * (l + 1))

# the six consecutive pairs of the observed nuclear ordering (register 1371).
# sense +1: the pair demands 4*beta + alpha > 0;  -1: demands < 0.
PAIRS = [
    ("2s1/2", "1d3/2", +1, "8-20"),
    ("2p3/2", "1f5/2", +1, "28-50"),
    ("3p3/2", "2f5/2", +1, "82-126"),
    ("2d3/2", "3s1/2", -1, "50-82"),
    ("1g7/2", "2d5/2", -1, "50-82"),
    ("1h9/2", "2f7/2", -1, "82-126"),
]

# ---------------------------------------------------------------------------
def identity_check():
    """Every pair shares an oscillator shell, has Dl = 2, and gives ratio 4."""
    ok = True
    print("  THE IDENTITY, pair by pair (exact rationals)")
    print(f"    {'pair':<22}{'N':>3}{'  Dl':>5}{'  D[l(l+1)]':>12}{'  D<L.S>':>10}{'  ratio':>8}")
    for a, b, sense, shell in PAIRS:
        hi, lo = (a, b) if LEVELS[a][1] > LEVELS[b][1] else (b, a)
        dcent = cent(hi) - cent(lo)
        dls = ls(hi) - ls(lo)
        ratio = dcent / dls
        same = N_shell(a) == N_shell(b)
        dl = abs(LEVELS[a][1] - LEVELS[b][1])
        ok &= same and dl == 2 and ratio == -4
        print(f"    {a+' -> '+b:<22}{N_shell(a):>3}{dl:>5}{str(dcent):>12}{str(dls):>10}{str(ratio):>8}")
    print(f"    ratio is -4 on all six, same shell, Dl = 2 throughout: {ok}")
    # and the collapse: dE = (l_lo + 3/2)(4 beta + alpha)
    print("    each inequality collapses to (l_lo + 3/2)(4*beta + alpha), l_lo + 3/2 > 0 always")
    print(f"    three pairs demand > 0, three demand < 0  ->  feasible set EMPTY\n")
    return ok

# ---------------------------------------------------------------------------
def base_vector(a, b, sense):
    """DS' — the collapsed base coefficient, oriented by the pair's demand."""
    hi, lo = (a, b) if LEVELS[a][1] > LEVELS[b][1] else (b, a)
    l_lo = LEVELS[lo][1]
    return sense * (F(l_lo) + F(3, 2))

def screen(name, T):
    """Is gamma*T admissible? The six (DS', DT) must lie in one OPEN half-plane."""
    V = []
    for a, b, sense, _ in PAIRS:
        hi, lo = (a, b) if LEVELS[a][1] > LEVELS[b][1] else (b, a)
        V.append((base_vector(a, b, sense), sense * (T(hi) - T(lo))))
    degenerate = all(v == 0 for _, v in V)
    # exact 2-D feasibility: exists (x, g) with u*x + v*g > 0 for all six.
    # the feasible directions form an open convex cone; test every edge normal.
    feasible = False
    cands = []
    for u, v in V:
        cands += [(-v, u), (v, -u)]
    cands += [(1, 0), (-1, 0), (0, 1), (0, -1)]
    for x, g in cands:
        if all(u * x + v * g > 0 for u, v in V):
            feasible = True
            break
    return {"name": name, "vectors": V, "degenerate": degenerate, "feasible": feasible}

def report(r):
    print(f"  {r['name']}")
    print("    (DS', DT) = " + ", ".join(f"({u},{v})" for u, v in r["vectors"]))
    if r["degenerate"]:
        print("    DT = 0 on every pair -- DEGENERATE, the term cannot be seen here")
    print("    VERDICT   " + ("feasible" if r["feasible"] else "FEASIBLE SET EMPTY"))

# ---------------------------------------------------------------------------
def nilsson():
    """4*beta + alpha under Nilsson's own parameters (registers 1393, 1430).

    H = HO - kappa*hbar*w0 [ 2 l.s + mu (l^2 - <l^2>_N) ]  gives
    beta = -kappa*mu*hbar*w0 and alpha = 2*kappa*hbar*w0, so
    4*beta + alpha = 2*kappa*hbar*w0 (1 - 2*mu), which VANISHES at mu = 1/2.
    """
    print("  NILSSON'S OWN PARAMETERS, as quoted in registers 1393 and 1430")
    print("    4*beta + alpha = 2*kappa*hbar*w0 (1 - 2*mu)   ->   zero exactly at mu = 1/2")
    quoted = [("light nuclei", F(601, 10000), F(448, 1000)),
              ("actinides (n)", F(588, 10000), F(328, 1000)),
              ("50-82 protons", F(637, 10000), F(60, 100)),
              ("82-126 neutrons", F(637, 10000), F(42, 100))]
    for region, k, mu in quoted:
        s = 2 * k * (1 - 2 * mu)
        sign = "> 0" if s > 0 else ("< 0" if s < 0 else "= 0")
        print(f"    {region:<18} kappa={float(k):.4f} mu={float(mu):.3f}   4b+a {sign}")
    print("    the 50-82 shell comes out negative, which is the sense both its pairs demand;")
    print("    the 82-126 shell comes out positive, and that shell demands BOTH senses.")
    print("    regional freedom does not save it, because the contradiction is inside one region.\n")

# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("=== THE SIX-PAIR SCREEN ===\n")
    ok = identity_check()

    print("  CONTROLS — these MUST come back empty (register 1394)")
    report(screen("control: T = l(l+1)  [the beta slot]", cent))
    report(screen("control: T = <L.S>   [the alpha slot]", ls))
    report(screen("control: T = f(N) alone  [Woods-Saxon, any N-only shape]",
                  lambda lab: F(N_shell(lab))))
    print()
    nilsson()

    ctrl = [screen("a", cent), screen("b", ls), screen("c", lambda l: F(N_shell(l)))]
    if any(c["feasible"] for c in ctrl):
        print("  CONTROLS PASSED WHEN THEY SHOULD HAVE FAILED — the screen is wrong.")
        sys.exit(1)
    print("  all three controls correctly return an empty feasible set.")
    print("  a candidate gamma*T is admissible only if screen(T)['feasible'] is True.")
    sys.exit(0 if ok else 1)
