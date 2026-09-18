#!/usr/bin/env python3
"""lowdin_walk.py -- a RECONSTRUCTION of the Löwdin solution's entrant walk.

The record (THE-LOWDIN-SOLUTION-2.md §II, Mathematical Compendium family LS, registers
1701-1706) states the construction and its results, but the construction itself -- the SCF
chain code, Λ_chain (119 rows) and Λ_cinf (107 rows) -- is sealed in LOWDIN-HANDOFF-103.tgz,
which is not held here and is not coming (LW1-ADDENDUM-REPLY.md; the Löwdin project has
concluded). This instrument rebuilds the walk from the record's own statement of it:

    cfg(1) := 1s¹
    for Z = 2 … 120:
        F := converged self-consistent field of the ion with nuclear charge Z
             and the electron configuration cfg(Z−1)          (the V^{N−1} field)
        for each unfilled frontier channel (n, ℓ):
            D(n,ℓ) := binding depth of one electron placed in channel (n, ℓ)
                      of the frozen field F
        entrant(Z) := the channel of greatest depth
        cfg(Z)     := cfg(Z−1) + one electron in entrant(Z)

and runs it twice, at c = 137.035999 (the record's one entered constant, register 1701)
and at c → ∞ (the twin, register 1706).

WHAT IS RECONSTRUCTED, AND WHAT IS NOT.  The record's mean field is Hartree–Fock in the
Koelling–Harmon scalar-relativistic reduction.  This instrument's mean field is the
Koelling–Harmon scalar-relativistic equation in a LOCAL-exchange self-consistent field
(Kohn–Sham exchange, V_x = −(3ρ/π)^{1/3}, with Latter's tail for the occupied orbitals) --
the Hartree–Fock–Slater construction of Herman & Skillman (1963), not Hartree–Fock.  The
non-local exchange of the record's field is NOT reproduced.  Every number this instrument
prints therefore carries the status RECONSTRUCTED: measured by a construction the record
describes, in a field the record does not use.  Where the reconstruction agrees with the
record that is a measurement; where it disagrees that is a measurement too, and neither is
repaired.  Λ_chain and Λ_cinf as the record holds them stay READ (registers 1702, 1706) and
are never overwritten by this file's output.

Numerics.  Logarithmic radial grid r = e^x, x ∈ [ln 1e-7, ln 300], step 0.005.  Radial
equation integrated as a first-order pair in x by fourth-order Runge–Kutta, outward from the
r^γ series at the nucleus (γ² = ℓ(ℓ+1) + 1 − (Z/c)², the Koelling–Harmon exponent; ℓ+1 at
c → ∞) and inward from the WKB tail, matched at the outer classical turning point; the
eigenvalue is bracketed by node count and refined by the Hartree matching correction.  For
ℓ = 0 the Koelling–Harmon equation IS the Dirac κ = −1 equation, so the hydrogenic 1s at
every Z is an exact fixture, ε = c²(√(1 − (Z/c)²) − 1); at c → ∞ every hydrogenic level is,
ε = −Z²/(2n²).  The selftest asserts both, and asserts that a deliberately wrong sign on the
relativistic term FAILS them (the record's own demand, §III: every instrument carries a
demonstrable failure mode).

Stdlib only.  Runs on python3 (3.11) as well as python3.12.

    python3 tools/lowdin_walk.py --selftest
    python3 tools/lowdin_walk.py --z 47 --c 137.035999 --from observed   # one step, < 200 s
    python3 tools/lowdin_walk.py --chain --c 137.035999 --out LOWDIN-WALK-c137.tsv
    python3 tools/lowdin_walk.py --chain --c inf       --out LOWDIN-WALK-cinf.tsv
    python3 tools/lowdin_walk.py --merge LOWDIN-WALK-c137.tsv LOWDIN-WALK-cinf.tsv --out LOWDIN-WALK.tsv
    python3 tools/lowdin_walk.py --report LOWDIN-WALK.tsv [--json]
    python3 tools/lowdin_walk.py --verify LOWDIN-WALK.tsv
"""
import argparse
import hashlib
import importlib.util
import json
import math
import os
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
MEMBERS = os.path.join(ROOT, "method", "members")

C_LIGHT = 137.035999          # register 1701: the one entered constant
L_LETTERS = "spdfg"
L_OF = {ch: i for i, ch in enumerate(L_LETTERS)}
N_MAX, L_MAX = 8, 4           # the frontier the record's spectrum shows: up to 8s and 8g
Z_MAX = 120

STATUS = "RECONSTRUCTED"

# symbols beyond the observed table (Z = 109-120): IUPAC names, and the systematic
# Uue/Ubn for 119 and 120, as the site's spectra rows already use.
SYMBOLS_BEYOND = {109: "Mt", 110: "Ds", 111: "Rg", 112: "Cn", 113: "Nh", 114: "Fl",
                  115: "Mc", 116: "Lv", 117: "Ts", 118: "Og", 119: "Uue", 120: "Ubn"}

# register 1706 -- the eleven the record's c → ∞ twin displaces (READ, never a fixture
# of this instrument's own correctness; compared, not asserted)
ELEVEN_1706 = ["Mn", "Zn", "Ag", "Cd", "Nd", "Pm", "Sm", "Lu", "Hg", "Lr", "Rf"]


# ----------------------------------------------------------------------------------------
# the observed table (LW1-ground.py, register 1306) -- imported by path, never copied
# ----------------------------------------------------------------------------------------

def _load(name, fname):
    p = os.path.join(MEMBERS, fname)
    spec = importlib.util.spec_from_file_location(name, p)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


_LW1 = None


def lw1():
    global _LW1
    if _LW1 is None:
        _LW1 = _load("lw1_ground", "LW1-ground.py")
    return _LW1


def symbol(Z):
    if Z <= 108:
        return lw1().GROUND[Z][0]
    return SYMBOLS_BEYOND[Z]


def observed_cfg(Z):
    """{(n, l): occ} of the observed ground configuration, Z ≤ 108."""
    return {(n, l): o for n, l, o in lw1().expand(Z)}


def observed_gain(Z):
    """the channel(s) that gained electrons from Z−1 to Z in the observed table, as
    'nl' strings joined by '+', or '-' beyond the table.  More than one channel means the
    observed step rearranged (Cr → Mn is 4s alone; Pd → Ag is 5s; Ni → Cu is 4s−... no:
    Ni 3d8 4s2 → Cu 3d10 4s: 3d gains 2, 4s loses 1 → '3d')."""
    if Z < 2 or Z > 108:
        return "-"
    a, b = observed_cfg(Z - 1), observed_cfg(Z)
    gained = [k for k in b if b[k] > a.get(k, 0)]
    gained.sort(key=lambda k: (k[0] + k[1], k[0]))
    return "+".join(ch_name(k) for k in gained) if gained else "-"


def ch_name(nl):
    return f"{nl[0]}{L_LETTERS[nl[1]]}"


def parse_ch(s):
    return (int(s[:-1]), L_OF[s[-1]])


def cfg_str(cfg):
    keys = sorted(cfg, key=lambda k: (k[0] + k[1], k[0]))
    return " ".join(f"{ch_name(k)}{cfg[k]}" for k in keys if cfg[k] > 0)


def parse_cfg(s):
    out = {}
    for tok in s.split():
        n, l = parse_ch(tok[: (2 if tok[1] in L_LETTERS else 3)])
        out[(n, l)] = int(tok[(2 if tok[1] in L_LETTERS else 3):])
    return out


def capacity(nl):
    return 2 * (2 * nl[1] + 1)


# ----------------------------------------------------------------------------------------
# the grid and the quadratures
# ----------------------------------------------------------------------------------------

class Grid:
    def __init__(self, xmin=math.log(1e-7), xmax=math.log(300.0), h=0.005):
        n = int(round((xmax - xmin) / h))
        if n % 2:                       # even number of intervals: RK4 steps of 2h
            n += 1
        self.h = h
        self.n = n + 1
        self.x = [xmin + i * h for i in range(self.n)]
        self.r = [math.exp(v) for v in self.x]
        self.r2 = [v * v for v in self.r]


def cumint(f, h):
    """cumulative integral on a uniform grid, fourth order (Simpson stepping)."""
    n = len(f)
    out = [0.0] * n
    for i in range(0, n - 2, 2):
        out[i + 1] = out[i] + h / 12.0 * (5 * f[i] + 8 * f[i + 1] - f[i + 2])
        out[i + 2] = out[i] + h / 3.0 * (f[i] + 4 * f[i + 1] + f[i + 2])
    if (n - 1) % 2:                     # odd last index: one trapezoid step
        out[n - 1] = out[n - 2] + h / 2.0 * (f[n - 2] + f[n - 1])
    return out


def integral(f, h):
    return cumint(f, h)[-1]


# ----------------------------------------------------------------------------------------
# the radial equation: Koelling–Harmon, first-order pair in x = ln r
#
#   P'' − (M'/M)(P' − P/r) = [ℓ(ℓ+1)/r² + 2M(V − ε)] P ,   M = 1 + (ε − V)/(2c²)
#
# (the Dirac radial pair with the spin-orbit part of the κ-dependence averaged out:
#  κ(κ+1) → ℓ(ℓ+1) and the (M'/M)κP/r term at its j-average κ = −1).  In x with
# p = P, s = dP/dx:  p' = s ;  s' = s + A (s − p) + B p ,  A = r M'/M = −(dV/dx)/(2c² M),
# B = ℓ(ℓ+1) + 2 M r² (V − ε).  At c → ∞: M = 1, A = 0.
# ----------------------------------------------------------------------------------------

class Field:
    """a potential on the grid: V(x) and dV/dx, with the nuclear term exact."""

    def __init__(self, grid, Z, Vel):
        """Vel: the electronic part of the potential (Hartree + exchange [+ Latter]) on the
        grid; the −Z/r term is added here so its derivative is analytic."""
        self.grid = grid
        self.Z = Z
        r = grid.r
        h = grid.h
        n = grid.n
        self.V = [Vel[i] - Z / r[i] for i in range(n)]
        d = [0.0] * n
        for i in range(1, n - 1):
            d[i] = (Vel[i + 1] - Vel[i - 1]) / (2 * h)
        d[0] = (Vel[1] - Vel[0]) / h
        d[n - 1] = (Vel[n - 1] - Vel[n - 2]) / h
        self.dVdx = [d[i] + Z / r[i] for i in range(n)]
        self.r2V = [grid.r2[i] * self.V[i] for i in range(n)]


def integrate(field, l, eps, c, sign=1.0):
    """one shot at energy eps.  Returns (nodes, mismatch, p_match, norm_r, s_out, s_in,
    p_out list, ok) -- or None when eps is not bracketed by the potential on the grid.
    sign flips the relativistic term (the demonstrable failure mode); it is 1.0 in use."""
    g = field.grid
    r, r2, V, dV, r2V = g.r, g.r2, field.V, field.dVdx, field.r2V
    n = g.n
    H = 2 * g.h
    ll = l * (l + 1)
    rel = c is not None
    inv2c2 = 1.0 / (2 * c * c) if rel else 0.0

    # coefficient arrays for this eps
    A = [0.0] * n
    B = [0.0] * n
    if rel:
        for i in range(n):
            M = 1.0 + (eps - V[i]) * inv2c2
            if M <= 0.0:
                return None              # ε below −2c²: no such state
            A[i] = -sign * dV[i] * inv2c2 / M
            B[i] = ll + 2.0 * M * (r2V[i] - eps * r2[i])
    else:
        for i in range(n):
            B[i] = ll + 2.0 * (r2V[i] - eps * r2[i])

    # matching point: the outermost index where B < 0 (classically allowed), stepping by 2
    m = -1
    for i in range(n - 1, -1, -1):
        if B[i] < 0.0:
            m = i
            break
    if m < 4:
        return None                      # eps below the potential everywhere: too low
    if m >= n - 4:
        return None                      # allowed region reaches the grid edge: too high
    if m % 2:
        m -= 1

    # outward: the r^γ series at the nucleus
    Z = field.Z
    if rel:
        g2 = ll + 1.0 - (Z / c) ** 2 * sign
        gam = math.sqrt(g2) if g2 > 0 else 0.5
    else:
        gam = l + 1.0
    p = 1.0
    s = gam
    pout = [0.0] * (m + 1)
    pout[0] = p
    nodes = 0
    scale_shift = 0
    for i in range(0, m, 2):
        a0, b0 = A[i], B[i]
        a1, b1 = A[i + 1], B[i + 1]
        a2, b2 = A[i + 2], B[i + 2]
        k1p = s
        k1s = s + a0 * (s - p) + b0 * p
        p1 = p + 0.5 * H * k1p
        s1 = s + 0.5 * H * k1s
        k2p = s1
        k2s = s1 + a1 * (s1 - p1) + b1 * p1
        p2 = p + 0.5 * H * k2p
        s2 = s + 0.5 * H * k2s
        k3p = s2
        k3s = s2 + a1 * (s2 - p2) + b1 * p2
        p3 = p + H * k3p
        s3 = s + H * k3s
        k4p = s3
        k4s = s3 + a2 * (s3 - p3) + b2 * p3
        pn = p + H / 6.0 * (k1p + 2 * k2p + 2 * k3p + k4p)
        sn = s + H / 6.0 * (k1s + 2 * k2s + 2 * k3s + k4s)
        if pn * p < 0.0:
            nodes += 1
        p, s = pn, sn
        if abs(p) > 1e100:
            p *= 1e-100
            s *= 1e-100
            pout = [v * 1e-100 for v in pout]
        pout[i + 1] = 0.0                # midpoints are not carried
        pout[i + 2] = p
    p_out, s_out = p, s
    # fill the midpoints of the outward solution by a second pass is unnecessary: the
    # norm uses the even points only (Simpson on the coarse step H).

    # inward: WKB tail from the last point
    bN = B[n - 1]
    p = 1e-30
    s = -math.sqrt(bN) * p if bN > 0 else -p
    pin = {}
    pin[n - 1] = p
    for i in range(n - 1, m, -2):
        a0, b0 = A[i], B[i]
        a1, b1 = A[i - 1], B[i - 1]
        a2, b2 = A[i - 2], B[i - 2]
        hh = -H
        k1p = s
        k1s = s + a0 * (s - p) + b0 * p
        p1 = p + 0.5 * hh * k1p
        s1 = s + 0.5 * hh * k1s
        k2p = s1
        k2s = s1 + a1 * (s1 - p1) + b1 * p1
        p2 = p + 0.5 * hh * k2p
        s2 = s + 0.5 * hh * k2s
        k3p = s2
        k3s = s2 + a1 * (s2 - p2) + b1 * p2
        p3 = p + hh * k3p
        s3 = s + hh * k3s
        k4p = s3
        k4s = s3 + a2 * (s3 - p3) + b2 * p3
        p = p + hh / 6.0 * (k1p + 2 * k2p + 2 * k3p + k4p)
        s = s + hh / 6.0 * (k1s + 2 * k2s + 2 * k3s + k4s)
        if abs(p) > 1e100:
            p *= 1e-100
            s *= 1e-100
            for k in pin:
                pin[k] *= 1e-100
        pin[i - 2] = p
    p_in, s_in = p, s
    if p_out == 0.0 or p_in == 0.0:
        return None

    # scale the inward branch onto the outward one at m
    f = p_out / p_in
    s_in *= f
    for k in pin:
        pin[k] *= f

    # the full function on the coarse (even) points, and its norm ∫P² dr = ∫ p² r dx
    P = [0.0] * n
    for i in range(0, m + 1, 2):
        P[i] = pout[i]
    for i in range(m, n, 2):
        P[i] = pin.get(i, 0.0)
    f2 = [P[i] * P[i] * r[i] for i in range(0, n, 2)]
    norm = integral(f2, H)
    mismatch = (s_out - s_in) / r[m]     # (dP/dr)_out − (dP/dr)_in at the match, P(m) = p_out
    # Hartree's correction: Δε = P(m) [P'_out − P'_in] / (2 ∫P² dr)
    deps = p_out * mismatch / (2.0 * norm)
    return nodes, deps, P, norm, m


def solve(field, n, l, c, eps0=None, tol=1e-9, sign=1.0, maxit=80, trace=None):
    """the bound state (n, l) of the field: returns (eps, P_normalised) or None when the
    grid holds no such bound state (eps ≥ 0)."""
    target = n - l - 1
    Z = field.Z
    if eps0 is None:
        eps = -0.5 * (Z / n) ** 2
    else:
        eps = eps0
    if eps >= 0:
        eps = -1e-3
    lo, hi = None, 0.0                   # bounds: lo < eps_true < hi
    floor = -4.0 * Z * Z - 10.0          # below the deepest level any field here holds
    for it in range(maxit):
        if eps < floor:
            return None
        res = integrate(field, l, eps, c, sign)
        if trace:
            trace(f"      it {it:2d} eps {eps: .8f} lo {lo} hi {hi} -> " +
                  ("none" if res is None else f"nodes {res[0]} deps {res[1]: .3e}"))
        if res is None:
            # too low or too high?  decide by where the allowed region sits
            g = field.grid
            # if eps is above V at the grid edge the region reaches the edge -> too high
            if eps > field.V[g.n - 1] + l * (l + 1) / (2 * g.r2[g.n - 1]):
                hi = eps
                eps = (lo + hi) / 2 if lo is not None else eps * 2.0 - 1e-6
            else:
                lo = eps
                eps = (lo + hi) / 2
            continue
        nodes, deps, P, norm, m = res
        if nodes > target:
            hi = eps
            eps = (lo + hi) / 2 if lo is not None else eps * 2.0 - 1e-6
            continue
        if nodes < target:
            lo = eps
            eps = (lo + hi) / 2
            continue
        # right node count: the sign of the correction tightens the bracket, and the
        # Newton-like step is capped and kept inside it (the Hartree correction is
        # first-order; from a distant start it overshoots past the node boundary)
        if deps > 0:
            lo = eps if lo is None else max(lo, eps)
        else:
            hi = min(hi, eps)
        if abs(deps) > 0.5 * abs(eps):
            deps = math.copysign(0.5 * abs(eps), deps)
        new = eps + deps
        if lo is not None and new <= lo:
            new = (eps + lo) / 2
        if new >= hi:
            new = (eps + hi) / 2
        if abs(new - eps) < tol * max(1.0, abs(eps)):
            eps = new
            res = integrate(field, l, eps, c, sign)
            if res is None:
                return None
            nodes, deps, P, norm, m = res
            if nodes != target:
                return None
            inv = 1.0 / math.sqrt(norm)
            P = [v * inv for v in P]
            # the integration carries the even points (RK4 steps of 2h); the odd points
            # are filled by four-point Lagrange interpolation, fourth order like the rest
            nn = len(P)
            for i in range(1, nn - 1, 2):
                if 3 <= i <= nn - 4:
                    P[i] = (-P[i - 3] + 9 * P[i - 1] + 9 * P[i + 1] - P[i + 3]) / 16.0
                else:
                    P[i] = 0.5 * (P[i - 1] + P[i + 1])
            return eps, P
        eps = new
        if eps >= 0:
            return None
    return None


# ----------------------------------------------------------------------------------------
# the self-consistent field: local exchange (Kohn–Sham), Latter tail for occupied orbitals
# ----------------------------------------------------------------------------------------

XC = (3.0 / math.pi) ** (1.0 / 3.0)


def potentials(grid, Z, N, D):
    """from D(x) = Σ q P² (= 4πr²ρ) return (V_cand, V_occ): the electronic part of the
    field an ADDED electron sees (Hartree + local exchange; asymptote −(Z−N)/r with the
    nucleus) and the part the OCCUPIED orbitals see (the same, Latter-tailed to
    −(Z−N+1)/r)."""
    r = grid.r
    h = grid.h
    n = grid.n
    Q = cumint([D[i] * r[i] for i in range(n)], h)          # charge inside r
    tail = cumint(D, h)                                     # ∫_0^x D dx'
    total = tail[-1]
    Vh = [Q[i] / r[i] + (total - tail[i]) for i in range(n)]
    Vx = [-XC * (D[i] / (4 * math.pi * grid.r2[i])) ** (1.0 / 3.0) if D[i] > 0 else 0.0
          for i in range(n)]
    Vc = [Vh[i] + Vx[i] for i in range(n)]
    lat = Z - N + 1                                         # Latter: V ≥ … in magnitude
    Vo = [min(Vc[i], (Z - lat) / r[i]) for i in range(n)]   # total = Vo − Z/r ≤ −lat/r
    return Vc, Vo


def scf(grid, Z, cfg, c, Vstart=None, eps_start=None, mix=0.35, tol=1e-7, maxit=300,
        log=None):
    """converge the field of the ion (Z, cfg).  Returns a dict with V_cand (electronic
    part), orbitals {(n,l): (eps, P)}, iterations, converged flag, N."""
    N = sum(cfg.values())
    n = grid.n
    r = grid.r
    if Vstart is None:
        # a screened start: N−1 electrons at the Thomas–Fermi scale
        a = 0.8853 / Z ** (1.0 / 3.0)
        Vel = [max(N - 1, 0) * (1.0 - math.exp(-r[i] / a)) / r[i] for i in range(n)]
    else:
        Vel = list(Vstart)
    eps = dict(eps_start or {})
    orbs = {}
    converged = False
    it = 0
    beta = mix
    last_res = None
    Vcand = Vel
    for it in range(1, maxit + 1):
        field = Field(grid, Z, Vel)
        D = [0.0] * n
        for nl, q in sorted(cfg.items()):
            if q <= 0:
                continue
            sol = solve(field, nl[0], nl[1], c, eps.get(nl))
            if sol is None:
                sol = solve(field, nl[0], nl[1], c, None)
            if sol is None:
                raise RuntimeError(f"Z={Z} cfg={cfg_str(cfg)}: no bound {ch_name(nl)}")
            e, P = sol
            eps[nl] = e
            orbs[nl] = (e, P)
            for i in range(n):
                D[i] += q * P[i] * P[i]
        Vc, Vo = potentials(grid, Z, N, D)
        res = max(abs(Vo[i] - Vel[i]) * r[i] for i in range(n))
        if log:
            log(f"    scf it {it:3d}  residual {res:.3e}  beta {beta:.2f}")
        if res < tol:
            converged = True
            Vcand = Vc
            break
        if last_res is not None and res > last_res:
            beta = max(0.05, beta * 0.5)
        elif last_res is not None and res < 0.3 * last_res:
            beta = min(0.6, beta * 1.25)
        last_res = res
        Vel = [(1 - beta) * Vel[i] + beta * Vo[i] for i in range(n)]
        Vcand = Vc
    return {"Z": Z, "N": N, "cfg": dict(cfg), "V_cand": Vcand, "V_occ": Vel,
            "orbitals": orbs, "eps": eps, "iterations": it, "converged": converged,
            "D": D}


def frontier(cfg):
    out = []
    for n in range(1, N_MAX + 1):
        for l in range(0, min(n, L_MAX + 1)):
            if cfg.get((n, l), 0) < capacity((n, l)):
                out.append((n, l))
    return out


def scan(grid, Z, state, c, eps_hint=None):
    """the candidate spectrum of one electron added to the frozen field: [(eps, (n,l))]
    sorted deepest first."""
    field = Field(grid, Z, state["V_cand"])
    eps_hint = eps_hint or {}
    spec = []
    for nl in frontier(state["cfg"]):
        guess = eps_hint.get(nl)
        if guess is None:
            guess = -0.5 / nl[0] ** 2 * max(1.0, (Z - state["N"])) ** 2
            occ = state["eps"].get(nl)
            if occ is not None:
                guess = occ * 0.7
        sol = solve(field, nl[0], nl[1], c, guess)
        if sol is None:
            continue
        spec.append((sol[0], nl))
    spec.sort()
    return spec


# ----------------------------------------------------------------------------------------
# the walk
# ----------------------------------------------------------------------------------------

COLUMNS = ["c", "Z", "symbol", "cfg_prev", "entrant", "D_ent", "runner_up", "D_runner",
           "margin", "observed_gain", "agree", "spectrum", "scf_iterations", "converged",
           "status"]


def c_label(c):
    return "inf" if c is None else f"{c:.6f}"


def parse_c(s):
    if s in ("inf", "infinity", "∞"):
        return None
    return float(s)


def step(grid, Z, cfg_prev, c, prev_state=None, prev_spec=None, log=None):
    Vstart = None
    eps_start = None
    if prev_state is not None:
        # the previous ion's field, with one more proton and one more electron: a close
        # start; the SCF does the rest
        r = grid.r
        Vstart = [prev_state["V_occ"][i] + (1.0 - math.exp(-r[i])) / r[i]
                  for i in range(grid.n)]
        eps_start = {k: v * (Z / (Z - 1)) ** 2 for k, v in prev_state["eps"].items()}
    state = scf(grid, Z, cfg_prev, c, Vstart, eps_start, log=log)
    hint = {nl: e for e, nl in (prev_spec or [])}
    spec = scan(grid, Z, state, c, hint)
    return state, spec


def row_of(c, Z, cfg_prev, spec, state):
    ent = spec[0][1]
    D_ent = spec[0][0]
    if len(spec) > 1:
        ru, D_ru = spec[1][1], spec[1][0]
        margin = abs(D_ent) - abs(D_ru)
    else:
        ru, D_ru, margin = None, float("nan"), float("nan")
    og = observed_gain(Z)
    agree = "-" if og == "-" else ("yes" if ch_name(ent) == og else "no")
    return {
        "c": c_label(c), "Z": Z, "symbol": symbol(Z), "cfg_prev": cfg_str(cfg_prev),
        "entrant": ch_name(ent), "D_ent": f"{D_ent:.8f}",
        "runner_up": ch_name(ru) if ru else "-", "D_runner": f"{D_ru:.8f}",
        "margin": f"{margin:.8f}", "observed_gain": og, "agree": agree,
        "spectrum": ";".join(f"{ch_name(nl)}:{e:.8f}" for e, nl in spec),
        "scf_iterations": state["iterations"],
        "converged": "yes" if state["converged"] else "no",
        "status": STATUS,
    }


def write_rows(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(COLUMNS) + "\n")
        for row in rows:
            f.write("\t".join(str(row[k]) for k in COLUMNS) + "\n")


def read_rows(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        cols = f.readline().rstrip("\n").split("\t")
        for line in f:
            if not line.strip():
                continue
            rows.append(dict(zip(cols, line.rstrip("\n").split("\t"))))
    return rows


def chain(c, out, zmax=Z_MAX, log=print, fields_dir=None, resume=True):
    grid = Grid()
    rows = []
    cfg = {(1, 0): 1}
    prev_state = None
    prev_spec = None
    start = 2
    if resume and out and os.path.exists(out):
        rows = read_rows(out)
        if rows:
            last = rows[-1]
            cfg = parse_cfg(last["cfg_prev"])
            cfg[parse_ch(last["entrant"])] = cfg.get(parse_ch(last["entrant"]), 0) + 1
            start = int(last["Z"]) + 1
            log(f"resuming from Z = {start} ({len(rows)} rows held in {out})")
    t0 = time.time()
    for Z in range(start, zmax + 1):
        t1 = time.time()
        state, spec = step(grid, Z, cfg, c, prev_state, prev_spec)
        row = row_of(c, Z, cfg, spec, state)
        rows.append(row)
        ent = parse_ch(row["entrant"])
        cfg = dict(cfg)
        cfg[ent] = cfg.get(ent, 0) + 1
        prev_state, prev_spec = state, spec
        log(f"c={row['c']:>10} Z={Z:3d} {row['symbol']:>3}  entrant {row['entrant']} "
            f"({row['D_ent']})  runner {row['runner_up']} margin {row['margin']}  "
            f"obs {row['observed_gain']:>5} {row['agree']:>3}  scf {state['iterations']:3d}"
            f"{'' if state['converged'] else ' NOT CONVERGED'}  {time.time() - t1:5.1f}s")
        if out:
            write_rows(out, rows)
        if fields_dir:
            os.makedirs(fields_dir, exist_ok=True)
            with open(os.path.join(fields_dir, f"{c_label(c)}-{Z}.json"), "w") as f:
                json.dump({"c": c_label(c), "Z": Z, "cfg": cfg_str(state["cfg"]),
                           "V_cand": [round(v, 10) for v in state["V_cand"]],
                           "eps": {ch_name(k): v for k, v in state["eps"].items()},
                           "grid": {"xmin": grid.x[0], "h": grid.h, "n": grid.n}}, f)
    log(f"done: {len(rows)} rows in {time.time() - t0:.0f} s")
    return rows


# ----------------------------------------------------------------------------------------
# one step, standalone
# ----------------------------------------------------------------------------------------

def one_step(Z, c, source="observed", chain_file=None, log=print):
    if source == "observed":
        if Z < 2 or Z > 109:
            raise SystemExit("--from observed needs 2 ≤ Z ≤ 109 (cfg(Z−1) from the table)")
        cfg_prev = observed_cfg(Z - 1)
        src = f"cfg({Z - 1}) READ from LW1-ground.py (register 1306)"
    else:
        rows = [r for r in read_rows(chain_file) if int(r["Z"]) == Z and
                r["c"] == c_label(c)]
        if not rows:
            raise SystemExit(f"no row Z={Z} c={c_label(c)} in {chain_file}")
        cfg_prev = parse_cfg(rows[0]["cfg_prev"])
        src = f"cfg({Z - 1}) from the chain in {chain_file}"
    grid = Grid()
    t0 = time.time()
    state, spec = step(grid, Z, cfg_prev, c, log=None)
    row = row_of(c, Z, cfg_prev, spec, state)
    log(f"lowdin_walk one step  Z = {Z} ({symbol(Z)})  c = {c_label(c)}  [{STATUS}]")
    log(f"  {src}: {cfg_str(cfg_prev)}  (N = {state['N']})")
    log(f"  scf: {state['iterations']} iterations, "
        f"{'converged' if state['converged'] else 'NOT CONVERGED'}  {time.time() - t0:.1f} s")
    log(f"  occupied eigenvalues (Latter-tailed field):")
    for nl in sorted(state["eps"], key=lambda k: state["eps"][k]):
        log(f"    {ch_name(nl):>3}  {state['eps'][nl]: .6f}")
    log(f"  candidate spectrum, one electron in the frozen field (asymptote −{Z - state['N']}/r):")
    for e, nl in spec:
        mark = "  ← entrant" if nl == spec[0][1] else ("  ← runner-up" if len(spec) > 1 and nl == spec[1][1] else "")
        log(f"    {ch_name(nl):>3}  {e: .8f}{mark}")
    log(f"  entrant {row['entrant']}  margin {row['margin']}  observed gain {row['observed_gain']}  agree {row['agree']}")
    return row, state, spec


# ----------------------------------------------------------------------------------------
# the report
# ----------------------------------------------------------------------------------------

def openings(rows):
    """first Z at which each channel is the entrant, in order."""
    seen = []
    for r in rows:
        if r["entrant"] not in [s[0] for s in seen]:
            seen.append((r["entrant"], int(r["Z"])))
    return seen


def observed_openings():
    seq = [("1s", 1)]
    for Z in range(2, 109):
        for ch in observed_gain(Z).split("+"):
            if ch != "-" and ch not in [s[0] for s in seq]:
                seq.append((ch, Z))
    return seq


def _nl_sum(ch):
    n, l = parse_ch(ch)
    return n + l


def summarise(rows):
    """everything the report states, as data: per setting the openings, the clauses, the
    scores under each reading, the g-channel pins and the smallest margins; across the two
    settings the displaced elements against register 1706 and the thorium control.  Nothing
    here is asserted against the record; it is measured and placed beside it."""
    by_c = {}
    for r in rows:
        by_c.setdefault(r["c"], []).append(r)
    out = {"status": STATUS, "rows": len(rows), "settings": {}, "compare": None}
    oo = observed_openings()
    for c, rs in by_c.items():
        rs = sorted(rs, key=lambda r: int(r["Z"]))
        op = openings(rs)
        same_order = [ch for ch, _ in op if ch in dict(oo)] == [ch for ch, _ in oo if ch in dict(op)]
        c1 = [(a, b) for a, b in zip(op, op[1:]) if _nl_sum(a[0]) > _nl_sum(b[0])]
        c2 = [(a, b) for a, b in zip(op, op[1:]) if _nl_sum(a[0]) == _nl_sum(b[0]) and parse_ch(a[0])[0] > parse_ch(b[0])[0]]
        scored = [r for r in rs if r["agree"] != "-"]
        exact = 0
        for r in rs:
            cfg = parse_cfg(r["cfg_prev"])
            cfg[parse_ch(r["entrant"])] = cfg.get(parse_ch(r["entrant"]), 0) + 1
            if int(r["Z"]) <= 108 and cfg == observed_cfg(int(r["Z"])):
                exact += 1
        g = {}
        for r in rs:
            for tok in r["spectrum"].split(";"):
                ch, e = tok.split(":")
                if ch.endswith("g"):
                    g.setdefault(ch, []).append(float(e))
        gpins = []
        for ch in sorted(g):
            n = int(ch[:-1])
            gpins.append({"channel": ch, "offered": len(g[ch]),
                          "max_dev": max(abs(e + 1.0 / (2 * n * n)) for e in g[ch])})
        margins = sorted(rs, key=lambda r: float(r["margin"]) if r["margin"] != "nan" else 9e9)[:5]
        out["settings"][c] = {
            "rows": len(rs), "Z_first": int(rs[0]["Z"]), "Z_last": int(rs[-1]["Z"]),
            "not_converged": [r["symbol"] for r in rs if r["converged"] != "yes"],
            "openings": [{"channel": ch, "Z": Z} for ch, Z in op],
            "openings_observed": [{"channel": ch, "Z": Z} for ch, Z in oo],
            "same_order": same_order,
            "openings_displaced": [{"channel": ch, "Z": Z, "observed_Z": dict(oo).get(ch)}
                                   for ch, Z in op if dict(oo).get(ch) not in (None, Z)],
            "clause1_violations": [f"{a[0]}@{a[1]}>{b[0]}@{b[1]}" for a, b in c1],
            "clause2_exceptions": [f"{a[0]}@{a[1]} before {b[0]}@{b[1]}" for a, b in c2],
            "scored": len(scored),
            "agree": sum(1 for r in scored if r["agree"] == "yes"),
            "disagree": [{"symbol": r["symbol"], "Z": int(r["Z"]), "entrant": r["entrant"],
                          "observed_gain": r["observed_gain"]} for r in scored if r["agree"] == "no"],
            "cfg_identical": exact,
            "g_pins": gpins,
            "smallest_margins": [{"symbol": r["symbol"], "Z": int(r["Z"]), "entrant": r["entrant"],
                                  "runner_up": r["runner_up"], "margin": float(r["margin"])} for r in margins],
        }
    if "137.035999" in by_c and "inf" in by_c:
        a = {int(r["Z"]): r for r in by_c["137.035999"]}
        b = {int(r["Z"]): r for r in by_c["inf"]}
        common = sorted(set(a) & set(b))
        diffs = [Z for Z in common if a[Z]["entrant"] != b[Z]["entrant"]]
        names = [a[Z]["symbol"] for Z in diffs]
        out["compare"] = {
            "Z_first": common[0], "Z_last": common[-1], "rows": len(common),
            "displaced": [{"symbol": a[Z]["symbol"], "Z": Z, "entrant_c137": a[Z]["entrant"],
                           "entrant_cinf": b[Z]["entrant"]} for Z in diffs],
            "eleven_1706": list(ELEVEN_1706),
            "in_eleven": [s for s in names if s in ELEVEN_1706],
            "not_in_eleven": [s for s in names if s not in ELEVEN_1706],
            "eleven_not_displaced": [s for s in ELEVEN_1706 if s not in names],
            "thorium": ({"entrant_c137": a[90]["entrant"], "entrant_cinf": b[90]["entrant"],
                         "identical": a[90]["entrant"] == b[90]["entrant"],
                         "top3_c137": a[90]["spectrum"].split(";")[:3],
                         "top3_cinf": b[90]["spectrum"].split(";")[:3]} if 90 in a and 90 in b else None),
            "named_rows": [{"symbol": a[Z]["symbol"], "Z": Z,
                            "top3_c137": a[Z]["spectrum"].split(";")[:3],
                            "top3_cinf": b[Z]["spectrum"].split(";")[:3]}
                           for Z in (25, 30, 47, 48, 60, 71, 80, 90, 103, 104) if Z in a and Z in b],
        }
    return out


def report(rows, log=print):
    sm = summarise(rows)
    for c in sorted(sm["settings"], key=lambda k: (k == "inf", k)):
        s = sm["settings"][c]
        log(f"\n== c = {c}  ({s['rows']} rows, Z = {s['Z_first']}–{s['Z_last']})  [{STATUS}]")
        if s["not_converged"]:
            log(f"   NOT CONVERGED at {len(s['not_converged'])} rows: " + " ".join(s["not_converged"]))
        log("   opening sequence, derived:  " + " ".join(f"{o['channel']}@{o['Z']}" for o in s["openings"]))
        log("   opening sequence, observed: " + " ".join(f"{o['channel']}@{o['Z']}" for o in s["openings_observed"]))
        log(f"   same order of the channels both open: {s['same_order']}")
        log("   openings at a different Z: " + (" ".join(f"{o['channel']} derived@{o['Z']} observed@{o['observed_Z']}" for o in s["openings_displaced"]) or "none"))
        log(f"   clause 1 (smaller n+ℓ opens first) violations on the derived openings: {len(s['clause1_violations'])}  " + " ".join(s["clause1_violations"]))
        log(f"   clause 2 (equal n+ℓ, smaller n first) exceptions on the derived openings: {len(s['clause2_exceptions'])}  " + " ".join(s["clause2_exceptions"]))
        log(f"   entrant = the observed gain (differentiating-electron reading): {s['agree']} of {s['scored']}")
        log("   disagreements: " + (" ".join(f"{d['symbol']}({d['entrant']}≠{d['observed_gain']})" for d in s["disagree"]) or "none"))
        log(f"   chain configuration identical to the observed one: {s['cfg_identical']} of {min(s['rows'], 107)}")
        for gp in s["g_pins"]:
            log(f"   {gp['channel']} offered at {gp['offered']} elements; max |D + 1/(2n²)| = {gp['max_dev']:.2e}  (record: 5g 65, 6g 70, 7g 57, 8g 28; −1/(2n²) to storage precision)")
        log("   five smallest margins: " + " ".join(f"{m['symbol']}({m['entrant']} over {m['runner_up']} by {m['margin']:.4f})" for m in s["smallest_margins"]))
    cp = sm["compare"]
    if cp:
        log(f"\n== c = 137.035999 against c = ∞ over Z = {cp['Z_first']}–{cp['Z_last']} ({cp['rows']} rows)")
        log(f"   entrants differ at {len(cp['displaced'])}: " + (" ".join(f"{d['symbol']}({d['entrant_c137']}|{d['entrant_cinf']})" for d in cp["displaced"]) or "none"))
        log(f"   register 1706's eleven: {' '.join(cp['eleven_1706'])}")
        log(f"   of the record's eleven, displaced here too: {len(cp['in_eleven'])}  {' '.join(cp['in_eleven'])}")
        log(f"   displaced here and not in the record's eleven: {len(cp['not_in_eleven'])}  {' '.join(cp['not_in_eleven'])}")
        log(f"   in the record's eleven and not displaced here: {len(cp['eleven_not_displaced'])}  {' '.join(cp['eleven_not_displaced'])}")
        th = cp["thorium"]
        if th:
            log(f"   Th (90): entrant {th['entrant_c137']} at c = 137.035999, {th['entrant_cinf']} at c = ∞ -> "
                f"{'identical (the null-difference control holds)' if th['identical'] else 'DIFFERENT'}; "
                f"the record: entrant survives by path, the competition inverts")
        for nr in cp["named_rows"]:
            log(f"   {nr['symbol']:>3} ({nr['Z']}): c=137 {' '.join(nr['top3_c137'])}   |   c=∞ {' '.join(nr['top3_cinf'])}")
    return sm


def verify(path, log=print):
    """the output table against its own contract: the columns, the statuses, the row
    count per setting, one row recomputed (Z = 3 at both settings, seconds) against what the
    file states.  A hand edit that changes a value is caught; a rerun that changes one is a
    measurement and shows as such."""
    rows = read_rows(path)
    bad = 0
    cols = list(rows[0].keys()) if rows else []
    if cols != COLUMNS:
        bad += 1
        log(f"  columns differ from the contract: {cols}")
    if any(r["status"] != STATUS for r in rows):
        bad += 1
        log("  a row carries a status other than RECONSTRUCTED")
    by_c = {}
    for r in rows:
        by_c.setdefault(r["c"], []).append(int(r["Z"]))
    for c, zs in by_c.items():
        if zs != list(range(zs[0], zs[-1] + 1)):
            bad += 1
            log(f"  c = {c}: Z not contiguous")
        log(f"  c = {c}: {len(zs)} rows, Z = {zs[0]}–{zs[-1]}")
    grid = Grid()
    for c in ("137.035999", "inf"):
        held = [r for r in rows if r["c"] == c and r["Z"] == "3"]
        if not held:
            continue
        cfg_prev = parse_cfg(held[0]["cfg_prev"])
        state, spec = step(grid, 3, cfg_prev, parse_c(c))
        row = row_of(parse_c(c), 3, cfg_prev, spec, state)
        same = all(row[k] == held[0][k] for k in ("entrant", "D_ent", "runner_up", "margin", "spectrum"))
        log(f"  Z = 3 at c = {c} recomputed: {'identical to the file' if same else 'DIFFERS from the file'}")
        if not same:
            bad += 1
            log(f"    file {held[0]['spectrum'][:60]}\n    now  {row['spectrum'][:60]}")
    log("VERIFY OK" if bad == 0 else "VERIFY FAILED")
    return bad == 0


# ----------------------------------------------------------------------------------------
# selftest
# ----------------------------------------------------------------------------------------

def selftest(log=print):
    grid = Grid()
    fails = 0
    checks = 0

    def check(name, ok, detail=""):
        nonlocal fails, checks
        checks += 1
        if not ok:
            fails += 1
        log(f"   {'ok  ' if ok else 'FAIL'}  {name}  {detail}")

    zero = [0.0] * grid.n
    log("lowdin_walk --selftest")
    log("1. hydrogenic levels at c → ∞ (exact −Z²/2n²)")
    for Z, n, l in [(1, 1, 0), (1, 2, 0), (1, 2, 1), (1, 3, 2), (1, 4, 3), (1, 5, 4), (1, 8, 4),
                    (30, 1, 0), (80, 3, 1), (120, 1, 0), (120, 7, 0)]:
        f = Field(grid, Z, zero)
        sol = solve(f, n, l, None)
        exact = -0.5 * (Z / n) ** 2
        got = sol[0] if sol else float("nan")
        check(f"Z={Z} {n}{L_LETTERS[l]}", sol is not None and abs(got - exact) < 2e-7 * abs(exact),
              f"got {got:.9f} exact {exact:.9f}")
    log("2. hydrogenic 1s at c = 137.035999 (Koelling–Harmon at ℓ = 0 is Dirac κ = −1: exact c²(√(1−(Z/c)²)−1))")
    c = C_LIGHT
    for Z in (1, 30, 50, 80, 100, 120):
        f = Field(grid, Z, zero)
        sol = solve(f, 1, 0, c)
        exact = c * c * (math.sqrt(1 - (Z / c) ** 2) - 1)
        got = sol[0] if sol else float("nan")
        check(f"Z={Z} 1s", sol is not None and abs(got - exact) < 2e-7 * abs(exact),
              f"got {got:.6f} exact {exact:.6f}")
    log("3. the failure mode: the relativistic term with the wrong sign must FAIL the Dirac fixture at Z = 80")
    f = Field(grid, 80, zero)
    sol = solve(f, 1, 0, c, sign=-1.0)
    exact = c * c * (math.sqrt(1 - (80 / c) ** 2) - 1)
    got = sol[0] if sol else float("nan")
    check("wrong sign fails", (sol is None) or abs(got - exact) > 1e-3 * abs(exact),
          f"got {got:.6f} exact {exact:.6f}")
    log("4. c → ∞ recovers the non-relativistic level: c = 1e6 against c = ∞ at Z = 80, 2p")
    f = Field(grid, 80, zero)
    a = solve(f, 2, 1, 1e6)[0]
    b = solve(f, 2, 1, None)[0]
    check("c=1e6 vs inf", abs(a - b) < 1e-7 * abs(b), f"{a:.9f} vs {b:.9f}")
    log("5. the observed table imports (register 1306) and the electron count holds")
    check("108 elements, count = Z", all(lw1().occ_count(Z) == Z for Z in range(1, 109)))
    check("observed gain at Mn is 4s, at Ag 5s, at Hg 6s, at Th 6d (r2-scf.out §3)",
          (observed_gain(25), observed_gain(47), observed_gain(80), observed_gain(90)) == ("4s", "5s", "6s", "6d"))
    log("6. one self-consistent field: He (Z = 2, 1s²) at c = ∞ -- charge, asymptote, one bound electron")
    st = scf(grid, 2, {(1, 0): 2}, None)
    Dint = integral([st["D"][i] * grid.r[i] for i in range(grid.n)], grid.h)
    check("scf converged", st["converged"], f"{st['iterations']} iterations")
    check("∫ρ = 2", abs(Dint - 2.0) < 1e-6, f"{Dint:.8f}")
    i = grid.n - 1
    Vtot = st["V_cand"][i] - 2 / grid.r[i]
    check("candidate field asymptote −(Z−N)/r = 0 at the grid edge", abs(Vtot * grid.r[i]) < 1e-6, f"rV = {Vtot * grid.r[i]:.2e}")
    check("1s eigenvalue bound and below −0.5", st["eps"][(1, 0)] < -0.5, f"{st['eps'][(1, 0)]:.6f}")
    log("7. the frozen-field scan at Z = 3 (Li: field of 1s² with Z = 3): 2s is the entrant, and the g channels are hydrogenic")
    st = scf(grid, 3, {(1, 0): 2}, None)
    sp = scan(grid, 3, st, None)
    top = sp[0][1]
    check("entrant 2s", top == (2, 0), f"spectrum {' '.join(f'{ch_name(nl)}:{e:.5f}' for e, nl in sp[:4])}")
    g5 = [e for e, nl in sp if nl == (5, 4)]
    check("5g at −1/50 to 1e-6", bool(g5) and abs(g5[0] + 0.02) < 1e-6, f"{g5[0] if g5 else float('nan'):.8f}")
    log("8. the row and configuration codecs round-trip")
    cfg = observed_cfg(79)
    check("cfg_str/parse_cfg", parse_cfg(cfg_str(cfg)) == cfg, cfg_str(cfg))
    check("frontier of Au's configuration holds 6p and 5f and not 4f", (6, 1) in frontier(cfg) and (5, 3) in frontier(cfg) and (4, 3) not in frontier(cfg))
    log(f"\n{checks - fails} of {checks} checks pass" + ("" if not fails else f"  --  {fails} FAIL"))
    return fails == 0


# ----------------------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--chain", action="store_true", help="run the walk Z = 2..--zmax")
    ap.add_argument("--c", default="137.035999", help="the speed of light, or 'inf'")
    ap.add_argument("--zmax", type=int, default=Z_MAX)
    ap.add_argument("--out", help="TSV to write (chain, merge)")
    ap.add_argument("--fields", help="directory to store each converged field as JSON")
    ap.add_argument("--no-resume", action="store_true")
    ap.add_argument("--z", type=int, help="one step at this Z")
    ap.add_argument("--from", dest="source", default="observed", choices=["observed", "chain"])
    ap.add_argument("--chain-file", help="the TSV to read cfg(Z−1) from with --from chain")
    ap.add_argument("--merge", nargs="+", help="TSVs to merge into --out")
    ap.add_argument("--report", help="TSV to report on")
    ap.add_argument("--json", action="store_true", help="with --report: print the summary as JSON")
    ap.add_argument("--verify", help="TSV to verify against its contract")
    ap.add_argument("--goldens", action="store_true", help="Ag, Hg, Th at both settings from the observed table")
    a = ap.parse_args(argv)
    if a.selftest:
        return 0 if selftest() else 1
    if a.chain:
        if not a.out:
            ap.error("--chain needs --out")
        chain(parse_c(a.c), a.out, a.zmax, fields_dir=a.fields, resume=not a.no_resume)
        return 0
    if a.z:
        one_step(a.z, parse_c(a.c), a.source, a.chain_file)
        return 0
    if a.goldens:
        for Z in (47, 80, 90):
            for c in (C_LIGHT, None):
                one_step(Z, c, "observed")
                print()
        return 0
    if a.merge:
        if not a.out:
            ap.error("--merge needs --out")
        rows = []
        for p in a.merge:
            rows.extend(read_rows(p))
        rows.sort(key=lambda r: (r["c"] == "inf", int(r["Z"])))
        write_rows(a.out, rows)
        print(f"{len(rows)} rows -> {a.out}")
        return 0
    if a.report:
        if a.json:
            print(json.dumps(summarise(read_rows(a.report)), ensure_ascii=False, indent=1))
        else:
            report(read_rows(a.report))
        return 0
    if a.verify:
        return 0 if verify(a.verify) else 1
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
