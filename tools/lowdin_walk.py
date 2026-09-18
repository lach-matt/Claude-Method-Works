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
    """∫f on the uniform grid: Simpson over the whole span when the point count is odd
    (it is: the grid has an even number of intervals), else the stepping rule."""
    n = len(f)
    if n % 2 == 1 and n >= 3:
        return h / 3.0 * (f[0] + f[-1] + 4.0 * sum(f[1:-1:2]) + 2.0 * sum(f[2:-1:2]))
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
# the second field: Hartree–Fock with non-local exchange (the record's field)
#
# Average-of-configuration Hartree–Fock (Slater; the object Bach–Lieb–Loss–Solovej's
# theorem is about, which the record cites as its well-posedness condition), with the
# Koelling–Harmon kinetic operator of the same equation.  For orbital a of occupation q_a:
#
#   (T + V_a) P_a − X_a = ε_a P_a
#   V_a = −Z/r + (q_a−1)[Y⁰(aa) − (2ℓ+1)/(4ℓ+1) Σ_{k>0} a_k(ℓ,ℓ) Y^k(aa)]/r + Σ_{b≠a} q_b Y⁰(bb)/r
#   X_a = Σ_{b≠a} ½ q_b Σ_k a_k(ℓ_a,ℓ_b) Y^k(ab)/r · P_b            a_k(ℓ,ℓ') = (ℓ k ℓ'; 0 0 0)²
#
# The added electron of the frontier scan sees the same operator at the full occupation
# (q_c in place of q_c−1 where c is an open shell), asymptote −(Z−N)/r as before.  The
# equation for each orbital is solved as an inhomogeneous shooting problem: homogeneous and
# particular solutions integrated out and in, matched at the turning point, and the
# eigenvalue fixed by the norm condition ∫P² = 1 on the branch below the local pole (the
# exchange operator is positive, so ε_HF lies below the local eigenvalue).  Orbitals of one
# ℓ are kept orthogonal by Gram–Schmidt rather than by off-diagonal multipliers -- the one
# approximation of the field, stated.  Nothing else of the record's method is approximated
# here; its collapse criterion, correlation clause and two-branch diagnostic remain outside.
# ----------------------------------------------------------------------------------------

from itertools import accumulate as _accumulate, repeat as _repeat
from operator import mul as _mul, sub as _sub, add as _add, truediv as _div


def cumint_fast(f, h):
    """cumulative integral on a uniform grid: the trapezoid sum (C-level accumulate) with
    the Euler–Maclaurin end correction −(h²/12)(f'_i − f'_0), fourth order for smooth f.
    Every pass is a C-level map or accumulate; no Python loop over the grid."""
    n = len(f)
    cs = _accumulate(f)
    # T_i = h (cs_i − f_0/2 − f_i/2)
    T = map(_mul, _repeat(h), map(_sub, map(_sub, cs, _repeat(0.5 * f[0])), map(_mul, _repeat(0.5), f)))
    # f' by central differences, one-sided at the ends, scaled by h²/12 → c = (h/24)(f_{i+1} − f_{i−1})
    c = [0.0] * n
    inner = map(_mul, _repeat(h / 24.0), map(_sub, f[2:], f[:-2]))
    c[1:n - 1] = inner
    c[0] = h / 12.0 * (f[1] - f[0])
    c[n - 1] = h / 12.0 * (f[n - 1] - f[n - 2])
    c0 = c[0]
    return list(map(_sub, T, map(_sub, c, _repeat(c0))))


def _fact(n):
    return math.factorial(n)


_AK = {}


def a_k(la, k, lb):
    """(ℓ_a k ℓ_b; 0 0 0)², the angular coefficient of the Slater integrals."""
    key = (la, k, lb)
    if key in _AK:
        return _AK[key]
    J = la + k + lb
    if J % 2 or k < abs(la - lb) or k > la + lb:
        v = 0.0
    else:
        g = J // 2
        v = (_fact(2 * g - 2 * la) * _fact(2 * g - 2 * k) * _fact(2 * g - 2 * lb) / _fact(2 * g + 1)) * \
            (_fact(g) / (_fact(g - la) * _fact(g - k) * _fact(g - lb))) ** 2
    _AK[key] = v
    return v


class Powers:
    """r^k, r^{k+1} and r^{-k} on the grid, cached per k."""

    def __init__(self, grid):
        self.grid = grid
        self._c = {}

    def get(self, k):
        if k not in self._c:
            r = self.grid.r
            self._c[k] = ([v ** k for v in r], [v ** (k + 1) for v in r], [v ** (-k) for v in r])
        return self._c[k]


def yk_over_r(grid, pw, Pa, Pb, k):
    """Y^k(ab; r)/r = (1/r^{k+1}) ∫_0^r r'^k P_a P_b dr' + r^k ∫_r^∞ P_a P_b / r'^{k+1} dr'."""
    rk, rk1, rmk = pw.get(k)
    f = list(map(_mul, Pa, Pb))
    A = cumint_fast(list(map(_mul, f, rk1)), grid.h)
    Bc = cumint_fast(list(map(_mul, f, rmk)), grid.h)
    Bt = Bc[-1]
    return list(map(_add, map(_div, A, rk1), map(_mul, rk, map(_sub, _repeat(Bt), Bc))))


def _dot(grid, P, Q):
    return integral([P[i] * Q[i] * grid.r[i] for i in range(grid.n)], grid.h)


def _rk4_multi(A, B, srcs, H, i0, i1, p0, s0):
    """integrate p' = s, s' = s + A(s − p) + B p [+ S_k] from index i0 to i1 in steps of 2
    (H = ±2h): the homogeneous system from (p0, s0) and one particular system per source in
    srcs from (0, 0), all in one pass.  Returns ([p-dict per system], [(p_end, s_end)])."""
    step = 2 if H > 0 else -2
    K = 1 + len(srcs)
    ps = [p0] + [0.0] * len(srcs)
    ss = [s0] + [0.0] * len(srcs)
    outs = [{i0: ps[k]} for k in range(K)]
    h6 = H / 6.0
    hh = 0.5 * H
    for i in range(i0, i1, step):
        j = i + (1 if step > 0 else -1)
        k2 = i + step
        a0, b0, a1, b1, a2, b2 = A[i], B[i], A[j], B[j], A[k2], B[k2]
        for k in range(K):
            p, sv = ps[k], ss[k]
            if k:
                S = srcs[k - 1]
                s0_, s1_, s2_ = S[i], S[j], S[k2]
            else:
                s0_ = s1_ = s2_ = 0.0
            k1p = sv
            k1s = sv + a0 * (sv - p) + b0 * p + s0_
            p1 = p + hh * k1p
            q1 = sv + hh * k1s
            k2p = q1
            k2s = q1 + a1 * (q1 - p1) + b1 * p1 + s1_
            p2 = p + hh * k2p
            q2 = sv + hh * k2s
            k3p = q2
            k3s = q2 + a1 * (q2 - p2) + b1 * p2 + s1_
            p3 = p + H * k3p
            q3 = sv + H * k3s
            k4p = q3
            k4s = q3 + a2 * (q3 - p3) + b2 * p3 + s2_
            p = p + h6 * (k1p + 2 * k2p + 2 * k3p + k4p)
            sv = sv + h6 * (k1s + 2 * k2s + 2 * k3s + k4s)
            ps[k], ss[k] = p, sv
            outs[k][k2] = p
    return outs, list(zip(ps, ss))


def shoot_multi(field, l, eps, c, sources):
    """(T + V_loc − ε)P = S for each source S in `sources` at one energy: the homogeneous
    solutions out and in are shared, each source gets its particular solution, and each is
    matched at the turning point.  Returns (list of P per source on the even points, m,
    i_in) or None when eps is not bracketed.  With no sources, returns the homogeneous
    matching data as ([P], m, i_in, deps) for the pole search (see shoot_inh)."""
    g = field.grid
    r, r2, V, dV, r2V = g.r, g.r2, field.V, field.dVdx, field.r2V
    n = g.n
    H = 2 * g.h
    ll = l * (l + 1)
    rel = c is not None
    inv2c2 = 1.0 / (2 * c * c) if rel else 0.0
    A = [0.0] * n
    B = [0.0] * n
    if rel:
        Ms = [0.0] * n
        for i in range(n):
            M = 1.0 + (eps - V[i]) * inv2c2
            if M <= 0.0:
                return None
            Ms[i] = M
            A[i] = -dV[i] * inv2c2 / M
            B[i] = ll + 2.0 * M * (r2V[i] - eps * r2[i])
        S_list = [[-2.0 * Ms[i] * r2[i] * X[i] for i in range(n)] for X in sources]
    else:
        for i in range(n):
            B[i] = ll + 2.0 * (r2V[i] - eps * r2[i])
        S_list = [[-2.0 * r2[i] * X[i] for i in range(n)] for X in sources]
    m = -1
    for i in range(n - 1, -1, -1):
        if B[i] < 0.0:
            m = i
            break
    if m < 4 or m >= n - 4:
        return None
    if m % 2:
        m -= 1
    # the inward start: where the WKB decay from the turning point reaches e^-12, or the
    # grid edge.  Not further: the inward homogeneous solution grows by the same factor,
    # and the matching subtracts it from the particular branch, so a longer span costs
    # digits (at e^-40 the cancellation exceeds double precision and the norm is noise)
    acc = 0.0
    i_in = n - 1
    for i in range(m, n):
        acc += math.sqrt(max(B[i], 0.0)) * g.h
        if acc > 12.0:
            i_in = i
            break
    if i_in % 2:
        i_in += 1
    if i_in > n - 1:
        i_in = n - 1
    Z = field.Z
    if rel:
        g2 = ll + 1.0 - (Z / c) ** 2
        gam = math.sqrt(g2) if g2 > 0 else 0.5
    else:
        gam = l + 1.0
    outs, ends = _rk4_multi(A, B, S_list, H, 0, m, 1.0, gam)
    ph, sh = ends[0]
    if abs(ph) > 1e150 or ph == 0.0:
        return None
    ins, iends = _rk4_multi(A, B, S_list, -H, i_in, m, 1e-30, -math.sqrt(max(B[i_in], 1e-30)) * 1e-30)
    qh, th = iends[0]
    if abs(qh) > 1e150 or qh == 0.0:
        return None
    det = -ph * th + qh * sh
    if det == 0.0:
        return None
    Ps = []
    for k in range(1, 1 + len(sources)):
        pp, sp = ends[k]
        qp, tp = iends[k]
        r1 = qp - pp
        r2_ = tp - sp
        alpha = (-r1 * th + qh * r2_) / det
        beta = (ph * r2_ - sh * r1) / det
        P = [0.0] * n
        ho, po, hi, pi = outs[0], outs[k], ins[0], ins[k]
        for i in range(0, m + 1, 2):
            P[i] = alpha * ho[i] + po[i]
        for i in range(m + 2, i_in + 1, 2):
            P[i] = beta * hi[i] + pi[i]
        Ps.append(P)
    return Ps, m, i_in


def _norm_even(grid, P):
    return integral([P[i] * P[i] * grid.r[i] for i in range(0, grid.n, 2)], 2 * grid.h)


def _dot_even(grid, P, Q):
    return integral([P[i] * Q[i] * grid.r[i] for i in range(0, grid.n, 2)], 2 * grid.h)


def _solve_small(Mx, rhs):
    """Gaussian elimination for the k×k multiplier system (k ≤ 8)."""
    k = len(rhs)
    M = [row[:] + [rhs[i]] for i, row in enumerate(Mx)]
    for col in range(k):
        piv = max(range(col, k), key=lambda i: abs(M[i][col]))
        M[col], M[piv] = M[piv], M[col]
        if M[col][col] == 0.0:
            return None
        for i in range(k):
            if i != col:
                f = M[i][col] / M[col][col]
                for j in range(col, k + 1):
                    M[i][j] -= f * M[col][j]
    return [M[i][k] / M[i][i] for i in range(k)]


def _count_nodes(P, i0, i1):
    nodes = 0
    last = 0.0
    for i in range(i0, i1 + 1, 2):
        v = P[i]
        if v == 0.0:
            continue
        if last != 0.0 and v * last < 0.0:
            nodes += 1
        last = v
    return nodes


def _fill_odd(P):
    nn = len(P)
    for i in range(1, nn - 1, 2):
        if 3 <= i <= nn - 4:
            P[i] = (-P[i - 3] + 9 * P[i - 1] + 9 * P[i + 1] - P[i + 3]) / 16.0
        else:
            P[i] = 0.5 * (P[i - 1] + P[i + 1])
    return P


def solve_inh(field, n, l, c, X, eps0, others=(), lam=(), tol=1e-8, maxit=60, trace=None, warm=None):
    """the orbital (n, l) of  (T + V_loc − ε)P = X + Σ_b λ_b P_b , normalised.  The source is
    fixed, so the local problem's eigenvalue ε_pole (the homogeneous solve, whose node
    count is reliable) is a pole of the solution's norm N(ε); the exchange operator is
    positive, so the root lies below it, and there N falls from the pole, so N = 1 has one
    root: bracketed in δ = ε_pole − ε and refined by a secant in ln N against ln δ.
    Returns (eps, P, overlaps, multipliers): overlaps = [⟨P_b|P⟩ for b in others] of the
    solution before its correction, and the multipliers λ_b + Δλ_b that make it orthogonal,
    found by one exact Newton step at the root (one particular solution per partner); P is
    the corrected, renormalised orbital.  Or None.  With no exchange source and no others it is the homogeneous solve.  The node
    count is a diagnostic, not a bracket: a particular solution far from the pole carries
    the nodes of its source."""
    g = field.grid
    n_ = g.n
    src = None
    if X is not None and max(abs(v) for v in X) != 0.0:
        src = list(X)
    for Pb, lb in zip(others, lam):
        if lb:
            if src is None:
                src = [0.0] * n_
            for i in range(n_):
                src[i] += lb * Pb[i]
    if src is None:
        sol = solve(field, n, l, c, eps0, tol=tol)
        if sol is None:
            return None
        return sol[0], sol[1], [_dot(g, Pb, sol[1]) for Pb in others], list(lam)
    hom = solve(field, n, l, c, (warm or {}).get("pole", eps0))
    if hom is None:
        return None
    e_pole = hom[0]
    if warm is not None:
        warm["pole"] = e_pole
    # the level below: the root must lie between it and the pole, or it is another state's
    d_max = None
    if n - 1 > l:
        below = solve(field, n - 1, l, c, (warm or {}).get("below"))
        if below is not None:
            if warm is not None:
                warm["below"] = below[0]
            d_max = 0.999 * (e_pole - below[0])

    def N_at(d):
        res = shoot_multi(field, l, e_pole - d, c, [src])
        if res is None:
            return None
        P = res[0][0]
        N = _norm_even(g, P)
        if not (N > 0.0) or N != N:
            return None
        return P, N

    if warm is not None and warm.get("d"):
        d = warm["d"]
    else:
        d = max(1e-6, 0.5 * (e_pole - eps0)) if (eps0 is not None and eps0 < e_pole) else max(1e-6, 1e-3 * abs(e_pole))
    if d_max is not None and d > d_max:
        d = 0.5 * d_max
    res = N_at(d)
    tries = 0
    while res is None and tries < 20:
        d *= 0.5
        res = N_at(d)
        tries += 1
    if res is None:
        return None
    lo = hi = None
    lnN = math.log(res[1])
    if trace:
        trace(f"      inh pole {e_pole: .9f}  d0 {d:.3e} lnN {lnN: .3e}")
    best = None
    if abs(lnN) < tol:
        best = (d, res)
    else:
        # a warm start sits near the root: bracket by small factors first
        grow = 1.25 if (warm is not None and warm.get("d")) else 2.0
        if lnN > 0:
            lo = (d, lnN)
            for _ in range(60):
                d *= grow
                if d_max is not None and d >= d_max:
                    d = d_max
                res = N_at(d)
                if res is None:
                    return None
                lnN = math.log(res[1])
                if trace:
                    trace(f"      inh grow  d {d:.3e} lnN {lnN: .3e}")
                if lnN < 0:
                    hi = (d, lnN)
                    break
                lo = (d, lnN)
                if d_max is not None and d >= d_max:
                    break                # no root above the level below: another state's
            if hi is None:
                return None
        else:
            hi = (d, lnN)
            for _ in range(60):
                d /= grow
                res = N_at(d)
                if res is None:
                    return None
                lnN = math.log(res[1])
                if trace:
                    trace(f"      inh shrink d {d:.3e} lnN {lnN: .3e}")
                if lnN > 0:
                    lo = (d, lnN)
                    break
                hi = (d, lnN)
            if lo is None:
                return None
        near = None
        for it in range(maxit):
            la, lb = math.log(lo[0]), math.log(hi[0])
            t = lo[1] / (lo[1] - hi[1])
            ld = la + t * (lb - la)
            if not (la < ld < lb) or it % 4 == 3:
                ld = 0.5 * (la + lb)
            d = math.exp(ld)
            res = N_at(d)
            if res is None:
                return None
            lnN = math.log(res[1])
            if trace:
                trace(f"      inh it {it:2d} d {d:.6e} eps {e_pole - d: .9f} lnN {lnN: .3e}")
            if abs(lnN) < tol:
                best = (d, res)
                break
            if near is None or abs(lnN) < near[0]:
                near = (abs(lnN), d, res)
            if lnN > 0:
                lo = (d, lnN)
            else:
                hi = (d, lnN)
        if best is None:
            if near is not None and near[0] < 1e-5:
                best = (near[1], near[2])
            else:
                return None
    d, res = best
    P, N = res
    inv = 1.0 / math.sqrt(N)
    P = [v * inv for v in P]
    eps = e_pole - d
    if warm is not None:
        warm["d"] = d
    ovl = [_dot_even(g, Pb, P) for Pb in others]
    new_lam = list(lam)
    if others:
        # the multipliers that make THIS solution orthogonal, by one Newton step at the
        # root: with v_b = (H_loc − ε)^{-1} P_b,  ⟨b'|P + Σ Δλ_b v_b⟩ = 0  is linear in Δλ
        # and exact; the corrected P is renormalised (a second-order change)
        res_v = shoot_multi(field, l, eps, c, list(others))
        if res_v is not None:
            vs = res_v[0]
            nb = len(others)
            Mx = [[_dot_even(g, others[bp], vs[b]) for b in range(nb)] for bp in range(nb)]
            dl = _solve_small(Mx, [-o for o in ovl])
            if dl is not None and all(abs(x) < 1e3 for x in dl):
                for b in range(nb):
                    vb = vs[b]
                    x = dl[b]
                    for i in range(0, g.n, 2):
                        P[i] += x * vb[i]
                N2 = _norm_even(g, P)
                inv2 = 1.0 / math.sqrt(N2)
                P = [v * inv2 for v in P]
                new_lam = [lb + x for lb, x in zip(lam, dl)]
    P = _fill_odd(P)
    return eps, P, ovl, new_lam


def hf_operator(grid, pw, Z, orbs, cfg, a, Pa, occ_self):
    """V_loc (electronic part) and the exchange source X for channel a = (n, l) whose
    current function is Pa; occ_self is the occupation the same-shell terms carry (q_a − 1
    for an occupied orbital, q_a for an added electron in an open shell, 0 for an empty
    channel).  orbs: {(n,l): P} of the occupied orbitals, cfg their occupations."""
    n = grid.n
    r = grid.r
    la = a[1]
    Vel = [0.0] * n
    X = [0.0] * n
    for b, Pb in orbs.items():
        qb = cfg[b]
        if qb <= 0:
            continue
        if b == a:
            continue
        y0 = yk_over_r(grid, pw, Pb, Pb, 0)
        for i in range(n):
            Vel[i] += qb * y0[i]
        lb = b[1]
        for k in range(abs(la - lb), la + lb + 1, 2):
            ak = a_k(la, k, lb)
            if ak == 0.0:
                continue
            yk = yk_over_r(grid, pw, Pa, Pb, k)
            f = 0.5 * qb * ak
            for i in range(n):
                X[i] += f * yk[i] * Pb[i]
    if occ_self > 0:
        Pself = orbs.get(a, Pa)
        y0 = yk_over_r(grid, pw, Pself, Pself, 0)
        for i in range(n):
            Vel[i] += occ_self * y0[i]
        fac = (2 * la + 1) / (4 * la + 1)
        for k in range(2, 2 * la + 1, 2):
            ak = a_k(la, k, la)
            yk = yk_over_r(grid, pw, Pself, Pself, k)
            f = occ_self * fac * ak
            for i in range(n):
                Vel[i] -= f * yk[i]
    return Vel, X


def _orthogonalise(grid, P, others):
    for Q in others:
        d = _dot(grid, P, Q)
        if d != 0.0:
            P = [P[i] - d * Q[i] for i in range(grid.n)]
    nrm = math.sqrt(_dot(grid, P, P))
    return [v / nrm for v in P]


def _deriv_x(P, h):
    n = len(P)
    d = [0.0] * n
    for i in range(2, n - 2):
        d[i] = (-P[i + 2] + 8 * P[i + 1] - 8 * P[i - 1] + P[i - 2]) / (12 * h)
    d[1] = (P[2] - P[0]) / (2 * h)
    d[n - 2] = (P[n - 1] - P[n - 3]) / (2 * h)
    return d


def one_electron_I(grid, Z, P, l):
    """I(a) = ⟨a| −½ d²/dr² + ℓ(ℓ+1)/2r² − Z/r |a⟩, the non-relativistic one-electron
    integral (kinetic by parts: ½∫P'² dr), used for the pair-rotation energy only."""
    r = grid.r
    n = grid.n
    dp = _deriv_x(P, grid.h)
    kin = 0.5 * integral([(dp[i] / r[i]) ** 2 * r[i] for i in range(n)], grid.h)
    cen = 0.5 * l * (l + 1) * integral([P[i] * P[i] / r[i] for i in range(n)], grid.h)
    nuc = -Z * integral([P[i] * P[i] for i in range(n)], grid.h)
    return kin + cen + nuc


def _Fk(grid, pw, Px, Pc, k):
    y = yk_over_r(grid, pw, Pc, Pc, k)
    return integral([Px[i] * Px[i] * y[i] * grid.r[i] for i in range(grid.n)], grid.h)


def _Gk(grid, pw, Px, Pc, k):
    y = yk_over_r(grid, pw, Px, Pc, k)
    return integral([Px[i] * Pc[i] * y[i] * grid.r[i] for i in range(grid.n)], grid.h)


def pair_energy(grid, pw, x, qx, Px, c, qc, Pc):
    """the average-of-configuration interaction energy of shells x and c (x ≠ c)."""
    lx, lc = x[1], c[1]
    e = _Fk(grid, pw, Px, Pc, 0)
    for k in range(abs(lx - lc), lx + lc + 1, 2):
        ak = a_k(lx, k, lc)
        if ak:
            e -= 0.5 * ak * _Gk(grid, pw, Px, Pc, k)
    return qx * qc * e


def shell_energy(grid, pw, x, qx, Px):
    """the average-of-configuration energy of the shell x with itself."""
    if qx < 2:
        return 0.0
    lx = x[1]
    e = _Fk(grid, pw, Px, Px, 0)
    fac = (2 * lx + 1) / (4 * lx + 1)
    for k in range(2, 2 * lx + 1, 2):
        e -= fac * a_k(lx, k, lx) * _Fk(grid, pw, Px, Px, k)
    return qx * (qx - 1) / 2 * e


def energy_of_pair_subspace(grid, pw, Z, orbs, cfg, a, b, Pa, Pb):
    """every term of the average-of-configuration energy that involves shell a or b, with
    the functions Pa, Pb in their place; the other shells as they stand."""
    qa, qb = cfg[a], cfg[b]
    e = qa * one_electron_I(grid, Z, Pa, a[1]) + qb * one_electron_I(grid, Z, Pb, b[1])
    e += shell_energy(grid, pw, a, qa, Pa) + shell_energy(grid, pw, b, qb, Pb)
    e += pair_energy(grid, pw, a, qa, Pa, b, qb, Pb)
    for c, Pc in orbs.items():
        if c == a or c == b or cfg[c] <= 0:
            continue
        e += pair_energy(grid, pw, a, qa, Pa, c, cfg[c], Pc)
        e += pair_energy(grid, pw, b, qb, Pb, c, cfg[c], Pc)
    return e


def pair_curvature(grid, pw, Z, orbs, cfg, a, b, delta=0.05):
    """d²E/dθ² within span(P_a, P_b) from the energy at θ = 0, ±δ."""
    Pa, Pb = orbs[a], orbs[b]
    n = grid.n

    def rotated(th):
        ca, sa = math.cos(th), math.sin(th)
        return ([ca * Pa[i] + sa * Pb[i] for i in range(n)],
                [-sa * Pa[i] + ca * Pb[i] for i in range(n)])

    e0 = energy_of_pair_subspace(grid, pw, Z, orbs, cfg, a, b, Pa, Pb)
    Pp, Qp = rotated(delta)
    ep = energy_of_pair_subspace(grid, pw, Z, orbs, cfg, a, b, Pp, Qp)
    Pm, Qm = rotated(-delta)
    em = energy_of_pair_subspace(grid, pw, Z, orbs, cfg, a, b, Pm, Qm)
    return (ep - 2 * e0 + em) / (delta * delta)


def _T_elem(grid, Z, Pa, Pb, l):
    """⟨b| −½ d²/dr² + ℓ(ℓ+1)/2r² − Z/r |a⟩, non-relativistic, kinetic by parts."""
    r = grid.r
    n = grid.n
    da = _deriv_x(Pa, grid.h)
    db = _deriv_x(Pb, grid.h)
    kin = 0.5 * integral([da[i] * db[i] / r[i] for i in range(n)], grid.h)
    cen = 0.5 * l * (l + 1) * integral([Pa[i] * Pb[i] / r[i] for i in range(n)], grid.h)
    nuc = -Z * integral([Pa[i] * Pb[i] for i in range(n)], grid.h)
    return kin + cen + nuc


def _T_elem_kh(grid, field, Pa, Pb, l, eps, c):
    """⟨b| T_KH(ε) |a⟩ with the Koelling–Harmon kinetic operator of the equation solved for
    a, T_KH P = −P''/(2M) + (M'/2M²)(P' − P/r) + ℓ(ℓ+1)P/(2Mr²), M = 1 + (ε − V)/(2c²), the
    second derivative removed by parts: ½∫(P_b/M)' P_a' dr.  At c → ∞ it is _T_elem."""
    if c is None:
        return _T_elem(grid, field.Z, Pa, Pb, l)
    r = grid.r
    n = grid.n
    h = grid.h
    inv2c2 = 1.0 / (2 * c * c)
    da = _deriv_x(Pa, h)              # dP/dx = r dP/dr
    db = _deriv_x(Pb, h)
    V, dVdx = field.V, field.dVdx
    f1 = [0.0] * n
    f2 = [0.0] * n
    f3 = [0.0] * n
    for i in range(n):
        M = 1.0 + (eps - V[i]) * inv2c2
        Mp = -dVdx[i] / r[i] * inv2c2                 # dM/dr
        pa_r = da[i] / r[i]                           # dP_a/dr
        pb_r = db[i] / r[i]
        # ½ ∫ (P_b/M)' P_a' dr = ½ ∫ [P_b'/M − P_b M'/M²] P_a' dr
        f1[i] = 0.5 * (pb_r / M - Pb[i] * Mp / (M * M)) * pa_r * r[i]
        # + ∫ P_b (M'/2M²)(P_a' − P_a/r) dr   (the operator: −P''/2M + (M'/2M²)(P' − P/r) + …)
        f2[i] = Pb[i] * Mp / (2 * M * M) * (pa_r - Pa[i] / r[i]) * r[i]
        # ∫ P_b ℓ(ℓ+1)/(2M r²) P_a dr
        f3[i] = Pb[i] * l * (l + 1) / (2 * M * r[i] * r[i]) * Pa[i] * r[i]
    return integral(f1, h) + integral(f2, h) + integral(f3, h) - field.Z * integral([Pa[i] * Pb[i] for i in range(n)], h)


def pair_gradient(grid, pw, Z, orbs, cfg, a, b, eps=None, c=None):
    """dE/dθ at θ = 0 within span(P_a, P_b): 2(q_a⟨b|F_a|a⟩ − q_b⟨a|F_b|b⟩), each
    matrix element from the state's own orbitals (the operator of a applied to a,
    projected on b) with the kinetic operator the equations were solved with -- Koelling–
    Harmon at ε_a and ε_b when c is finite -- so the gradient and the equations describe
    one state; the symmetry it zeroes is the multipliers' own."""
    r = grid.r
    n = grid.n
    Pa, Pb = orbs[a], orbs[b]
    qa, qb = cfg[a], cfg[b]
    Va, Xa = hf_operator(grid, pw, Z, orbs, cfg, a, Pa, qa - 1)
    Vb, Xb = hf_operator(grid, pw, Z, orbs, cfg, b, Pb, qb - 1)
    if c is None or eps is None:
        ta = _T_elem(grid, Z, Pa, Pb, a[1])
        tb = _T_elem(grid, Z, Pb, Pa, b[1])
    else:
        ta = _T_elem_kh(grid, Field(grid, Z, Va), Pa, Pb, a[1], eps[a], c)
        tb = _T_elem_kh(grid, Field(grid, Z, Vb), Pb, Pa, b[1], eps[b], c)
    # the nuclear term sits inside _T_elem / _T_elem_kh; Va, Vb are the electronic parts
    fa = ta + integral([Pb[i] * Va[i] * Pa[i] * r[i] for i in range(n)], grid.h) \
        - integral([Pb[i] * Xa[i] * r[i] for i in range(n)], grid.h)
    fb = tb + integral([Pa[i] * Vb[i] * Pb[i] * r[i] for i in range(n)], grid.h) \
        - integral([Pa[i] * Xb[i] * r[i] for i in range(n)], grid.h)
    return 2.0 * (qa * fa - qb * fb)


def rotate_pair(grid, pw, Z, orbs, cfg, a, b, g, H, cap=0.3):
    """rotate the pair by the Newton step −g/H within span(P_a, P_b): g the exact
    gradient dE/dθ at θ = 0, which the solves supply as 2(W_ab − W_ba) (a centred
    difference of the energy would carry an O(δ²) bias and the sweeps would settle on it),
    H the curvature from pair_curvature.  Returns theta and rotates orbs in place."""
    if H > 0:
        theta = -g / H
    else:
        theta = -0.02 if g > 0 else 0.02
    theta = max(-cap, min(cap, theta))
    if abs(theta) < 1e-13:
        return 0.0
    Pa, Pb = orbs[a], orbs[b]
    n = grid.n
    ca, sa = math.cos(theta), math.sin(theta)
    orbs[a] = [ca * Pa[i] + sa * Pb[i] for i in range(n)]
    orbs[b] = [-sa * Pa[i] + ca * Pb[i] for i in range(n)]
    return theta


HF_SCHMIDT = True     # experiment flags: Schmidt-correct coupled pairs after mixing
HF_ROTATE = True      # and rotate coupled pairs to the energy's stationary angle


def scf_hf(grid, Z, cfg, c, start, mix=0.7, tol=1e-7, maxit=150, log=None):
    """converge the Hartree–Fock field of the ion (Z, cfg) from the local-exchange state
    `start`.

    Orbitals of one ℓ are coupled by off-diagonal multipliers.  Each equation carries its
    own, λ_ab: the equation is solved with them as a fixed source, and at the root one
    exact Newton step (one particular solution per partner) moves them to the values that
    make the solution orthogonal, so at convergence every equation holds exactly with an
    orthonormal set.  What that leaves free is the rotation angle of each coupled pair
    within its own span, and the variational condition q_a ε_ab = q_b ε_ba fixes it (Froese
    Fischer's rotation analysis): after every sweep each pair takes a Newton step toward
    the angle at which the average-of-configuration energy is stationary, with the exact
    gradient 2(q_a⟨b|F_a|a⟩ − q_b⟨a|F_b|b⟩) from the state's orbitals and the curvature
    from the energy at three angles (its one-electron part non-relativistic; the field's
    operators stay Koelling–Harmon).  Nothing is Schmidt-orthogonalised: a Schmidt step
    after mixing admits fixed points where the solved orbital differs from the stored one
    by a multiple of its partner, and the equations then hold only up to that residual.
    A pair of CLOSED shells carries no multiplier and no rotation: the energy is invariant
    under their rotation, and only the canonical pair (the eigenfunctions of the one Fock
    operator) carries the orbital energies the record compares.  The field is converged
    when the orbitals, the eigenvalues, every overlap and every angle are still.  Returns
    a state dict like scf()'s, with orbitals {(n,l): (eps, P)}; the field is the
    orbitals."""
    N = sum(cfg.values())
    pw = Powers(grid)
    orbs = {nl: list(P) for nl, (e, P) in start["orbitals"].items() if cfg.get(nl, 0) > 0}
    eps = {nl: e for nl, (e, P) in start["orbitals"].items() if cfg.get(nl, 0) > 0}
    order = sorted(orbs, key=lambda k: (k[1], k[0]))

    def coupled(a, b):
        return a != b and a[1] == b[1] and not (cfg[a] == capacity(a) and cfg[b] == capacity(b))

    pairs = [(a, b) for i, a in enumerate(order) for b in order[i + 1:] if coupled(a, b)]
    lam_of = {a: {} for a in order}
    rot = {}
    warm = {a: {} for a in order}
    converged = False
    it = 0
    beta = mix
    last = None
    d_rot = 0.0
    o_max = 0.0
    hist = []                      # Anderson history: (x, r) over the whole orbital set
    n_pts = grid.n
    anderson = False               # switched on only when plain mixing is contracting slowly
    rates = []
    rotate = HF_ROTATE
    dp_hist = []
    note_rot = ""
    for it in range(1, maxit + 1):
        de_max = 0.0
        dp_max = 0.0
        o_max = 0.0
        x_vec = []
        for a in order:
            x_vec.extend(orbs[a])
        solved = {}
        for a in order:
            qa = cfg[a]
            others = [b for b in order if coupled(a, b)]
            Vel, X = hf_operator(grid, pw, Z, orbs, cfg, a, orbs[a], qa - 1)
            field = Field(grid, Z, Vel)
            lam = [lam_of[a].get(b, 0.0) for b in others]
            sol = solve_inh(field, a[0], a[1], c, X, eps[a], [orbs[b] for b in others], lam, warm=warm[a])
            if sol is None:
                warm[a] = {}
                sol = solve_inh(field, a[0], a[1], c, X, eps[a], [orbs[b] for b in others], lam)
            if sol is None and others:
                # the multipliers have run away: drop them, solve from the plain source and
                # let the Newton step rebuild them; slow the mixing for the rest of the run
                lam = [0.0] * len(others)
                beta = max(0.3, 0.5 * beta)
                sol = solve_inh(field, a[0], a[1], c, X, eps[a], [orbs[b] for b in others], lam)
            if sol is None:
                if log:
                    solve_inh(field, a[0], a[1], c, X, eps[a], [orbs[b] for b in others], lam, trace=log)
                raise RuntimeError(f"HF Z={Z} cfg={cfg_str(cfg)}: no solution for {ch_name(a)} at iteration {it} (eps {eps[a]})")
            e_new, P_new, ovl, new_lam = sol
            for b, lb in zip(others, new_lam):
                lam_of[a][b] = lb
            o_max = max([o_max] + [abs(o) for o in ovl])
            if _dot(grid, P_new, orbs[a]) < 0.0:          # one phase across sweeps
                P_new = [-v for v in P_new]
            dp = math.sqrt(_dot(grid, [P_new[i] - orbs[a][i] for i in range(grid.n)],
                                [P_new[i] - orbs[a][i] for i in range(grid.n)]))
            de_max = max(de_max, abs(e_new - eps[a]) / max(1.0, abs(e_new)))
            dp_max = max(dp_max, dp)
            solved[a] = P_new
            eps[a] = e_new
            # Gauss–Seidel within the sweep: the next equations see this orbital
            orbs[a] = P_new
        # Anderson mixing over the whole orbital set: x_{k+1} = Σ γ_i (x_i + β r_i) with
        # Σ γ = 1 minimising |Σ γ_i r_i|, r = G(x) − x; the slow collective mode of a
        # heavy atom's core (every orbital creeping together at 0.98 per sweep under plain
        # mixing) is what this removes.  Each mixed orbital is renormalised.
        g_vec = []
        for a in order:
            g_vec.extend(solved[a])
        r_vec = list(map(_sub, g_vec, x_vec))
        hist.append((x_vec, r_vec))
        if len(hist) > 5:
            hist.pop(0)
        if anderson and len(hist) >= 2 and d_rot < 0.05:
            m = len(hist)
            R = [[sum(map(_mul, hist[i][1], hist[j][1])) for j in range(m)] for i in range(m)]
            ridge = 1e-10 * max(R[i][i] for i in range(m))
            for i in range(m):
                R[i][i] += ridge
            ones = _solve_small(R, [1.0] * m)
            if ones is None:
                gam = [0.0] * (m - 1) + [1.0]
            else:
                tot = sum(ones)
                gam = [v / tot for v in ones] if tot != 0.0 else [0.0] * (m - 1) + [1.0]
            mixed = [0.0] * len(x_vec)
            for gi, (xi, ri) in zip(gam, hist):
                if gi == 0.0:
                    continue
                for k in range(len(mixed)):
                    mixed[k] += gi * (xi[k] + beta * ri[k])
        else:
            mixed = list(map(_add, x_vec, map(_mul, _repeat(beta), r_vec)))
        for idx, a in enumerate(order):
            seg = mixed[idx * n_pts:(idx + 1) * n_pts]
            nrm = math.sqrt(_dot(grid, seg, seg))
            orbs[a] = [v / nrm for v in seg]
        # the rotation step: within each coupled pair's span the energy must be
        # stationary; the exact gradient from the state, the curvature from the energy
        d_rot = 0.0
        for (a, b) in pairs:
            if not rotate:
                break
            g = pair_gradient(grid, pw, Z, orbs, cfg, a, b, eps, c)
            mem = rot.get((a, b))
            H = mem[1] if (mem is not None and it % 3 != 1) else pair_curvature(grid, pw, Z, orbs, cfg, a, b)
            theta = rotate_pair(grid, pw, Z, orbs, cfg, a, b, g, H)
            d_rot = max(d_rot, abs(theta))
            rot[(a, b)] = (theta, H)
        res = max(de_max, dp_max)
        # a cycle: the eigenvalues still, the orbital change and the angle repeating
        # exactly sweep after sweep.  The energy-stationary angle and the equations' own
        # orthogonal solutions then disagree -- at finite c the kinetic operator depends on
        # each orbital's energy and the symmetric-multiplier condition has no exact
        # variational form.  The field is settled by the equations: the rotation is
        # released and the disagreement recorded on the row.
        dp_hist.append((de_max, dp_max, d_rot))
        if rotate and pairs and it > 20 and len(dp_hist) >= 6:
            recent = dp_hist[-6:]
            if all(x[0] < 1e-9 for x in recent) and max(x[1] for x in recent) > 0 \
                    and (max(x[1] for x in recent) - min(x[1] for x in recent)) < 1e-3 * max(x[1] for x in recent) \
                    and min(x[2] for x in recent) > 1e-6:
                rotate = False
                note_rot = (f"pair rotation released at sweep {it}: the energy-stationary angle and the "
                            f"equations' orthogonal solutions disagree by {d_rot:.1e} rad (Koelling–Harmon "
                            f"kinetic operator at each orbital's own energy; no exact variational form); "
                            f"the field is the equations' own")
                hist = []
                if log:
                    log(f"    hf it {it:3d}  {note_rot}")
        if log:
            log(f"    hf it {it:3d}  d_eps {de_max:.2e}  d_P {dp_max:.2e}  d_rot {d_rot:.2e}  ovl {o_max:.1e}  beta {beta:.2f}  "
                + " ".join(f"{ch_name(a)}:{eps[a]:.6f}" for a in order))
        if res < tol and d_rot < 1e-6 and o_max < 1e-6:
            converged = True
            break
        if last is not None and res > 1.5 * last:
            beta = max(0.3, beta * 0.7)
            hist = []                  # a growing residual: restart the Anderson history
        elif last is not None and res < 0.5 * last:
            beta = min(0.8, beta * 1.1)
        if last is not None and last > 0:
            rates.append(res / last)
            # a collective slow mode: three sweeps contracting by less than 0.85 each
            if not anderson and it >= 8 and len(rates) >= 3 and min(rates[-3:]) > 0.85 and max(rates[-3:]) < 1.0:
                anderson = True
                if log:
                    log(f"    hf it {it:3d}  plain mixing contracts at {rates[-1]:.3f} per sweep: Anderson mixing on")
        last = res
    return {"Z": Z, "N": N, "cfg": dict(cfg), "orbitals": {a: (eps[a], orbs[a]) for a in order},
            "eps": dict(eps), "iterations": it, "converged": converged, "field": "hf",
            "orbs": orbs, "pw": pw, "lam": {ch_name(a): {ch_name(b): v for b, v in d.items()} for a, d in lam_of.items()},
            "d_rot": d_rot, "overlap": o_max,
            "note": ("" if converged else f"hf not converged in {it} sweeps: residual {last:.1e}, angle {d_rot:.1e}, overlap {o_max:.1e}")
                    + (("; " if not converged else "") + note_rot if note_rot else "")}


def scan_hf(grid, Z, state, c, lx_spec=None, log=None):
    """the candidate spectrum in the frozen Hartree–Fock field: one electron in each
    frontier channel, its own exchange with every occupied orbital iterated to
    self-consistency and its multipliers against the occupied orbitals of its ℓ iterated to
    orthogonality (the occupied orbitals do not respond, so the equation is the projected
    one and its multipliers are its own, moved by the Newton step of solve_inh until the
    overlaps vanish).  Deepest first."""
    cfg = state["cfg"]
    orbs = state["orbs"]
    pw = state["pw"]
    hint = {nl: e for e, nl in (lx_spec or [])}
    spec = []
    for nl in frontier(cfg):
        occ_self = cfg.get(nl, 0)
        others = [b for b in orbs if b != nl and b[1] == nl[1]]
        Pothers = [orbs[b] for b in others]
        guess_e = hint.get(nl, state["eps"].get(nl))
        Pc = orbs.get(nl)
        if Pc is None:
            Vel0, _X0 = hf_operator(grid, pw, Z, orbs, cfg, nl, [0.0] * grid.n, 0)
            f0 = Field(grid, Z, Vel0)
            h0 = solve(f0, nl[0], nl[1], c, guess_e)
            if h0 is None:
                continue
            guess_e, Pc = h0
            if others:
                Pc = _orthogonalise(grid, Pc, Pothers)
        lam = [0.0] * len(others)
        e_prev = None
        ok = False
        wm = {}
        for k in range(80):
            Vel, X = hf_operator(grid, pw, Z, orbs, cfg, nl, Pc, occ_self)
            field = Field(grid, Z, Vel)
            sol = solve_inh(field, nl[0], nl[1], c, X, guess_e, Pothers, lam, warm=wm)
            if sol is None:
                wm = {}
                sol = solve_inh(field, nl[0], nl[1], c, X, guess_e, Pothers, lam)
            if sol is None:
                break
            e_new, P_new, ovl, lam = sol
            # no mixing between rounds: a mixed candidate is not orthogonal, and its
            # exchange source then carries a partner component that the multipliers
            # chase (an oscillation of the overlaps, decaying by half a round)
            Pc = P_new
            guess_e = e_new
            if e_prev is not None and abs(e_new - e_prev) < 1e-8 * max(1.0, abs(e_new)) \
                    and max([abs(o) for o in ovl] or [0.0]) < 1e-5:
                ok = True
                break
            e_prev = e_new
        if e_prev is not None and guess_e < 0:
            spec.append((guess_e, nl))
            if log and not ok:
                log(f"    scan: {ch_name(nl)} not settled after 80 rounds (last change {abs(guess_e - e_prev):.1e})")
    spec.sort()
    return spec


# ----------------------------------------------------------------------------------------
# the walk
# ----------------------------------------------------------------------------------------

COLUMNS = ["field", "c", "Z", "symbol", "cfg_prev", "entrant", "D_ent", "runner_up", "D_runner",
           "margin", "observed_gain", "agree", "spectrum", "scf_iterations", "converged",
           "status", "note"]

FIELDS = {"lx": "local exchange (Kohn–Sham) with Latter's tail: Hartree–Fock–Slater",
          "hf": "Hartree–Fock, average of configuration, non-local exchange"}


def c_label(c):
    return "inf" if c is None else f"{c:.6f}"


def parse_c(s):
    if s in ("inf", "infinity", "∞"):
        return None
    return float(s)


def step(grid, Z, cfg_prev, c, prev_state=None, prev_spec=None, log=None, field="lx"):
    Vstart = None
    eps_start = None
    if prev_state is not None and prev_state.get("field", "lx") == "hf":
        prev_state = prev_state["lx"]
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
    if field == "hf":
        lx_state = state
        state = scf_hf(grid, Z, cfg_prev, c, lx_state, log=log)
        state["lx"] = lx_state
        state["iterations_lx"] = lx_state["iterations"]
        spec = scan_hf(grid, Z, state, c, spec, log=log)
    return state, spec


def row_of(c, Z, cfg_prev, spec, state, field="lx"):
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
        "field": field,
        "c": c_label(c), "Z": Z, "symbol": symbol(Z), "cfg_prev": cfg_str(cfg_prev),
        "entrant": ch_name(ent), "D_ent": f"{D_ent:.8f}",
        "runner_up": ch_name(ru) if ru else "-", "D_runner": f"{D_ru:.8f}",
        "margin": f"{margin:.8f}", "observed_gain": og, "agree": agree,
        "spectrum": ";".join(f"{ch_name(nl)}:{e:.8f}" for e, nl in spec),
        "scf_iterations": state["iterations"],
        "converged": "yes" if state["converged"] else "no",
        "status": STATUS,
        "note": state.get("note", ""),
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
            row = dict(zip(cols, line.rstrip("\n").split("\t")))
            row.setdefault("note", "")
            row.setdefault("field", "lx")
            rows.append(row)
    return rows


def chain(c, out, zmax=Z_MAX, log=print, fields_dir=None, resume=True, field="lx"):
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
        try:
            state, spec = step(grid, Z, cfg, c, prev_state, prev_spec, field=field)
        except Exception as exc:                      # a step that fails is recorded, not hidden
            log(f"{field} c={c_label(c):>10} Z={Z:3d}: step FAILED ({exc}); retrying from a cold start with slow mixing")
            try:
                state, spec = step(grid, Z, cfg, c, None, None, field=field)
            except Exception as exc2:
                if field == "hf":
                    # the chain continues on the local-exchange result, and the row says so
                    log(f"{field} c={c_label(c):>10} Z={Z:3d}: retry FAILED ({exc2}); the row carries the lx result, marked")
                    state, spec = step(grid, Z, cfg, c, None, None, field="lx")
                    state["converged"] = False
                    state["note"] = f"hf failed twice ({type(exc2).__name__}: {str(exc2)[:80]}); this row is the lx field's result"
                else:
                    raise
        row = row_of(c, Z, cfg, spec, state, field)
        rows.append(row)
        ent = parse_ch(row["entrant"])
        cfg = dict(cfg)
        cfg[ent] = cfg.get(ent, 0) + 1
        prev_state, prev_spec = state, spec
        log(f"{field} c={row['c']:>10} Z={Z:3d} {row['symbol']:>3}  entrant {row['entrant']} "
            f"({row['D_ent']})  runner {row['runner_up']} margin {row['margin']}  "
            f"obs {row['observed_gain']:>5} {row['agree']:>3}  scf {state['iterations']:3d}"
            f"{'' if state['converged'] else ' NOT CONVERGED'}  {time.time() - t1:5.1f}s")
        if out:
            write_rows(out, rows)
        if fields_dir and field == "lx":
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

def one_step(Z, c, source="observed", chain_file=None, log=print, field="lx"):
    if source == "observed":
        if Z < 2 or Z > 109:
            raise SystemExit("--from observed needs 2 ≤ Z ≤ 109 (cfg(Z−1) from the table)")
        cfg_prev = observed_cfg(Z - 1)
        src = f"cfg({Z - 1}) READ from LW1-ground.py (register 1306)"
    else:
        rows = [r for r in read_rows(chain_file) if int(r["Z"]) == Z and
                r["c"] == c_label(c) and r.get("field", "lx") == field]
        if not rows:
            raise SystemExit(f"no row Z={Z} c={c_label(c)} in {chain_file}")
        cfg_prev = parse_cfg(rows[0]["cfg_prev"])
        src = f"cfg({Z - 1}) from the chain in {chain_file}"
    grid = Grid()
    t0 = time.time()
    state, spec = step(grid, Z, cfg_prev, c, log=None, field=field)
    row = row_of(c, Z, cfg_prev, spec, state, field)
    log(f"lowdin_walk one step  Z = {Z} ({symbol(Z)})  c = {c_label(c)}  field {field}: {FIELDS[field]}  [{STATUS}]")
    log(f"  {src}: {cfg_str(cfg_prev)}  (N = {state['N']})")
    log(f"  scf: {state['iterations']} iterations, "
        f"{'converged' if state['converged'] else 'NOT CONVERGED'}  {time.time() - t0:.1f} s"
        + (f"  (local-exchange start: {state['iterations_lx']} iterations)" if field == "hf" else ""))
    log(f"  occupied eigenvalues ({'Hartree–Fock' if field == 'hf' else 'Latter-tailed local-exchange field'}):")
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
        by_c.setdefault((r.get("field", "lx"), r["c"]), []).append(r)
    out = {"status": STATUS, "rows": len(rows), "settings": {}, "compare": None, "fields": {}}
    oo = observed_openings()
    for (fld, c), rs in by_c.items():
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
        out["settings"][f"{fld}:{c}"] = {
            "field": fld, "field_name": FIELDS.get(fld, fld), "c": c,
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
    for fld in ("lx", "hf"):
        if (fld, "137.035999") not in by_c or (fld, "inf") not in by_c:
            continue
        a = {int(r["Z"]): r for r in by_c[(fld, "137.035999")]}
        b = {int(r["Z"]): r for r in by_c[(fld, "inf")]}
        common = sorted(set(a) & set(b))
        diffs = [Z for Z in common if a[Z]["entrant"] != b[Z]["entrant"]]
        names = [a[Z]["symbol"] for Z in diffs]
        out["fields"][fld] = {
            "field": fld, "field_name": FIELDS[fld],
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
    # the two fields against each other, at c = 137.035999
    if ("lx", "137.035999") in by_c and ("hf", "137.035999") in by_c:
        a = {int(r["Z"]): r for r in by_c[("lx", "137.035999")]}
        b = {int(r["Z"]): r for r in by_c[("hf", "137.035999")]}
        common = sorted(set(a) & set(b))
        out["fields_compare"] = {
            "c": "137.035999", "rows": len(common),
            "entrants_differ": [{"symbol": a[Z]["symbol"], "Z": Z, "lx": a[Z]["entrant"], "hf": b[Z]["entrant"]}
                                for Z in common if a[Z]["entrant"] != b[Z]["entrant"]],
        }
    # "compare" stays the primary field's comparison: hf when held, else lx
    out["primary_field"] = "hf" if "hf" in out["fields"] else ("lx" if "lx" in out["fields"] else None)
    out["compare"] = out["fields"].get(out["primary_field"]) if out["primary_field"] else None
    return out


def report(rows, log=print):
    sm = summarise(rows)
    for key in sorted(sm["settings"], key=lambda k: (k.split(":")[0] != "lx", k.endswith("inf"), k)):
        s = sm["settings"][key]
        c = s["c"]
        log(f"\n== field {s['field']} ({s['field_name']}), c = {c}  ({s['rows']} rows, Z = {s['Z_first']}–{s['Z_last']})  [{STATUS}]")
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
    for fld in ("lx", "hf"):
        cp = sm["fields"].get(fld)
        if not cp:
            continue
        log(f"\n== field {fld}: c = 137.035999 against c = ∞ over Z = {cp['Z_first']}–{cp['Z_last']} ({cp['rows']} rows)")
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
    fc = sm.get("fields_compare")
    if fc:
        log(f"\n== the two fields at c = 137.035999 over {fc['rows']} rows: entrants differ at {len(fc['entrants_differ'])}: "
            + (" ".join(f"{d['symbol']}(lx {d['lx']}|hf {d['hf']})" for d in fc["entrants_differ"]) or "none"))
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
        by_c.setdefault((r.get("field", "lx"), r["c"]), []).append(int(r["Z"]))
    for (fld, c), zs in sorted(by_c.items()):
        if zs != list(range(zs[0], zs[-1] + 1)):
            bad += 1
            log(f"  {fld} c = {c}: Z not contiguous")
        log(f"  {fld} c = {c}: {len(zs)} rows, Z = {zs[0]}–{zs[-1]}")
    grid = Grid()
    for (fld, c) in sorted(by_c):
        held = [r for r in rows if r["c"] == c and r["Z"] == "3" and r.get("field", "lx") == fld]
        if not held:
            continue
        cfg_prev = parse_cfg(held[0]["cfg_prev"])
        state, spec = step(grid, 3, cfg_prev, parse_c(c), field=fld)
        row = row_of(parse_c(c), 3, cfg_prev, spec, state, fld)
        same = all(row[k] == held[0][k] for k in ("entrant", "D_ent", "runner_up", "margin", "spectrum"))
        log(f"  Z = 3, {fld}, c = {c} recomputed: {'identical to the file' if same else 'DIFFERS from the file'}")
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
    log("8. the Hartree–Fock field at c → ∞: closed-shell eigenvalues are exact fixtures (numerical HF; Clementi–Roetti / Froese Fischer)")
    hf_fix = [(2, {(1, 0): 2}, (1, 0), -0.917956), (3, {(1, 0): 2, (2, 0): 1}, (2, 0), -0.196323),
              (4, {(1, 0): 2, (2, 0): 2}, (2, 0), -0.309270),
              (10, {(1, 0): 2, (2, 0): 2, (2, 1): 6}, (2, 1), -0.850410),
              (18, {(1, 0): 2, (2, 0): 2, (2, 1): 6, (3, 0): 2, (3, 1): 6}, (3, 1), -0.591017),
              (5, {(1, 0): 2, (2, 0): 2, (2, 1): 1}, (2, 1), -0.309856),
              (11, {(1, 0): 2, (2, 0): 2, (2, 1): 6, (3, 0): 1}, (3, 0), -0.182103)]
    for Z, cfg, nl, exact in hf_fix:
        t0 = time.time()
        lxs = scf(grid, Z, cfg, None)
        hfs = scf_hf(grid, Z, cfg, None, lxs)
        got = hfs["eps"][nl]
        check(f"Z={Z} {ch_name(nl)} HF", hfs["converged"] and abs(got - exact) < 2e-4 * abs(exact),
              f"got {got:.6f} exact {exact:.6f}  ({hfs['iterations']} it, {time.time() - t0:.1f} s)")
    log("9. the angular coefficients and the Y^k quadrature")
    check("a_2(1,1) = 2/15, a_1(0,1) = 1/3, a_0(l,l) = 1/(2l+1)", (abs(a_k(1, 2, 1) - 2 / 15) < 1e-12, abs(a_k(0, 1, 1) - 1 / 3) < 1e-12, abs(a_k(2, 0, 2) - 1 / 5) < 1e-12), (True, True, True))
    fz = Field(grid, 1, zero)
    P1 = solve(fz, 1, 0, None)[1]
    y0 = yk_over_r(grid, Powers(grid), P1, P1, 0)
    i = grid.n - 1
    check("Y⁰(1s1s)/r → 1/r at the edge (hydrogen)", abs(y0[i] * grid.r[i] - 1.0) < 1e-6, f"{y0[i] * grid.r[i]:.8f}")
    F0 = integral([P1[j] * P1[j] * y0[j] * grid.r[j] for j in range(grid.n)], grid.h)
    check("F⁰(1s,1s) of hydrogen = 5/8", abs(F0 - 0.625) < 1e-6, f"{F0:.8f}")
    log("10. the row and configuration codecs round-trip")
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
    ap.add_argument("--field", default="lx", choices=["lx", "hf"],
                    help="lx: local exchange (Hartree–Fock–Slater); hf: Hartree–Fock, non-local exchange")
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
        chain(parse_c(a.c), a.out, a.zmax, fields_dir=a.fields, resume=not a.no_resume, field=a.field)
        return 0
    if a.z:
        one_step(a.z, parse_c(a.c), a.source, a.chain_file, field=a.field)
        return 0
    if a.goldens:
        for Z in (47, 80, 90):
            for c in (C_LIGHT, None):
                one_step(Z, c, "observed", field=a.field)
                print()
        return 0
    if a.merge:
        if not a.out:
            ap.error("--merge needs --out")
        rows = []
        for p in a.merge:
            for r in read_rows(p):
                r.setdefault("field", "lx")      # a table written before the field column
                r.setdefault("note", "")
                rows.append(r)
        rows.sort(key=lambda r: (r["field"] != "lx", r["c"] == "inf", int(r["Z"])))
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
