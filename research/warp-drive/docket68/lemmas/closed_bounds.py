#!/usr/bin/env python3
"""closed_bounds.py -- item 243: the constant bounds as bounds of a closed index.  M, on the board's report of item 242:
"They are not invariant bounds. They are likely bounds of a closed index, the constant bounds that always apply
regardless of the other 3 categories".  The first sentence withdraws item 242's name and its fourth category; the rest
is carried as M's hypothesis H-CONSTANT-BOUNDS and put to the cypher here (196).  Worked in the conversation (computed,
exact where marked; READ where marked; deduced where marked; not verified by a separate session; not seated);
2026-10-11.

"Closed index" is The Method's (READ, method/members/The_Method_1_6-2.md).  §15.2: "A closed index satisfies X = ℛ(X)",
X = { x ∈ ∏ᵢ Âᵢ(X) : xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j } -- "the envelope set determines the index completely": a closed index
is its alphabet (S1, Âᵢ, "Always succeeds, no conditions.") and its envelopes (S3, φ̂ᵢⱼ).  §15.5: "ℛ(X) = X recovers
alphabet and bounds for any closed index".  §16: "A closed index contains its own contradiction" -- ⅅ = dim q − rank
∂Φ/∂p, each unit "a test the index must pass"; ⅅ_def realised by "two disjoint paths", the defence being their
disagreement; "Without surplus there is no check" (for Λ: dim p 4, dim q 6, rank 4, ⅅ = 2).  Item 121 names the two
criteria (self-referencing, self-defending) and item 8 (H-CLOSED-INDEX) makes each universe a closed index.  How each is
translated to these forms is the board's reading, named below.

  C0 (read) M's item-243 words, verbatim in the rulings file; the Method's sentences above, verbatim in the member.
  C1 (computed, exact) The acting bounds' rows from the stated forms.  Every quantity a bound uses is written as an
     exponent of 2 against ours from the instruments' own relations (p2_planck.sector and window, p2_gravity.corridor):
     G, the tension and the offset; kappa5^4 (SMS), ell^2 (the window's kap / sigma), Lambda4, the bit area, the one-bit
     throat m1 = G E1 / c^4, E1, sigma_P and N_max, with N bits multiplying the throat by sqrt N.  Each of the sixteen
     acting bounds' slacks is then computed and its row read off by unit steps (exact Fractions, linearity checked):
     all sixteen equal bounds.py's table, constants and coefficients, exactly.  The forms agree with p2_planck.sector
     at all twelve bulk members to 1e-12.  This is the check item 242's critic asked for: the table's rows now come out
     of the forms by computation, not by transcription.
  C2 (computed; by construction) The constants hold at every universe of the bulk.  Each constant that has a form is
     evaluated on each of the twelve members' computed sectors: shared SI (hbar and c recovered from sigma_P and the
     Planck length), SMS, the bit area, and four found in the forms (item 243 (d), candidates): the bulk's curvature from
     the plane (ell^2 = 3 c^4 / 4 pi G (sigma - 2 delta sigma)), the plane's vacuum (Lambda4 = 8 pi G delta sigma / c^4),
     the horizon (m1 = G E1 / c^4) and the capacity's form (N_max = sigma_P / 8 ln2 delta sigma).  Each is 1 at every
     member to 1e-12.  The README match and the build using the closing energy are definitions (240 (b), 111 (a)); the
     null energy per ray has no form in these instruments and is not evaluated.  Through the cypher (roster 1173) on
     the bulk index (item 233's 5D basis; the seven position universes, and all twelve members), each evaluated
     constant entered as a coordinate has a one-value alphabet, adds nothing, leaves every language's E unchanged, and
     its envelope (S3) is flat against every other coordinate: in §15.2's terms a constant bound is the alphabet's part
     of a closed index's bounds, a box that is a point -- applying in every cell, regardless of the cell.  The index it
     bounds is not closed: order and algebra E are 8 over the seven and 6 over the twelve (the combinations item 233
     predicted, and more).  Give any one constant a second value at one universe (2b) and order and algebra E rise to
     15: held, a constant never opens the index; lifted, it does -- the same for every constant, because it is what a
     second value on any coordinate does, not a property of the constant's physics.  By construction: every member was
     built under these forms, so this shows what the constants are in the index, not evidence for them.
  C3 (computed, exact) What each constant reaches.  Lift one constant at a time at position 2 (hbar or c x 2; the
     power of the tension in SMS, of G in the bit area, of sigma in the curvature, of G in the vacuum, to 3/2; the
     README, the build's energy, the horizon and the capacity by a factor 2) and recompute every acting row.  Shared SI,
     the bit area and the README match move bounds in all three of M's categories; the curvature and the horizon in two;
     SMS, the vacuum, the capacity's form and the build's energy in one each; the null energy per ray enters no bound's
     form.  Every constant applies at every universe; how many categories it shapes varies.  The reach is relative to
     the forms as the record states them: the curvature is stated directly in G and the tension, so lifting SMS moves
     only the coupling; taken together (the Randall-Sundrum pair), SMS and the curvature reach universal and structural
     bounds, and a different choice of which relation is primary would move reach between them.  The constants also set
     which bounds close the open direction (j -> -inf, bounds.py B3): the closing-energy tolerance closes it while the
     bit area's power of G is below 2, the dark-energy ceiling while the vacuum's power of G is below 2, one coupling
     while the tension's power in SMS is above -1/2 -- the stated values (1, 1, 1) sit inside all three.
  C4 (computed, exact; the board's translation of P2) The self-defence the constants supply.  Position 2's universe as
     the map from its parameters (G, the tension, the offset's ratio, the README) to the quantities each constant
     fixes (hbar and c, kappa5^4, ell^2, Lambda4, the bit area, E1, N_max, position 2's README, the build's energy):
     dim q 10, rank 4, so ⅅ = 6.  Free a constant -- give its quantity a parameter of its own -- and ⅅ falls by the
     number of quantities it fixed (shared SI 2, each other 1); free all and ⅅ = 0: without the constants there is no
     check.  Each is functionally independent of the rest.  Two disjoint paths to G (§16.4): through the bulk's coupling
     (SMS) and through its curvature as the window states it (ell^2 = kap / sigma); with the curvature as the sector
     states it (with the offset) the two agree exactly, and the paths disagree by exactly (sigma - 2 delta sigma) /
     sigma -- by 2^-(the plane positivity's slack), 2^-206.457 at ours, reaching total disagreement exactly where the
     positivity bound fails (exact rational algebra).  A universal bound is the measure of the defence two constants
     supply.
  C5 (computed; bounds.py B6, re-read) The constants leave the kind coordinate: the sixteen acting bounds in M's three
     categories give fifteen cells and kind adds nothing; no constant is a cell.

What this does not show.
  - Whether the address space or the bulk is closed: the bulk index's E (C2) is reported as the cypher gives it, and
    the constants do not change it.  P1 for the bulk is item 121's open construction.
  - The roles of the null energy per ray, and the four candidates as M's: they are the board's finds in the forms.
  - C2 and C4 are by construction; C3's lifts are one value each (the reach is linear in each hook, so one value
    decides whether a row moves).
  - "Regardless of the other 3 categories" is read two ways and both are measured: every constant with a form applies at
    every universe (C2); three of M's six -- shared SI, the bit area, the README match -- shape bounds in all three
    categories, the other three in one or none (C3).

Imports bounds.py (and through it bulk5_index.py, p2_planck.py, p2_gravity.py), tools/cypher.py and index_audit.py by
path.  Stdlib.  python3 closed_bounds.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
METHOD = os.path.join(ROOT, "method", "members", "The_Method_1_6-2.md")
MUT = {}
M243 = ("They are not invariant bounds. They are likely bounds of a closed index, the constant bounds that always apply "
        "regardless of the other 3 categories")
READS = ["A closed index satisfies X = ℛ(X)", "X = { x ∈ ∏ᵢ Âᵢ(X) : xᵢ ≤ φ̂ᵢⱼ(xⱼ) for all i ≠ j }",
         "the envelope set determines the index completely", "Always succeeds, no conditions.",
         "ℛ(X) = X recovers alphabet and bounds for any closed index", "A closed index contains its own contradiction",
         "ⅅ = dim q − rank ∂Φ/∂p ≥ dim q − dim p", "is reachable by two disjoint paths, and the defence is the DISAGREEMENT",
         "Without surplus there is no check", "dim p = 4, dim q = 6, rank 4, ⅅ = 2"]
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}


def _load(path, key):
    spec = importlib.util.spec_from_file_location(key, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[key] = mod
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path)]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


BD = _load(os.path.join(HERE, "bounds.py"), "cb_bd")
B5M, PG = BD.B5M, BD.PG
PP = B5M.PP
VARS = BD.VARS

# ================================================================================ the constants and their hooks
# (name, source, whose, hooks).  "the six (243)" are the bounds M's item 243 speaks of; "candidate" marks a relation found
# in the instruments' forms that holds at every universe (243 (d)), entered as the board's find, not M's.
CONSTANTS = [
    ("shared SI", "225 A", "the six (243)", ("h", "cc")),
    ("G from the bulk and the plane", "SMS; 234 V6", "the six (243)", ("b",)),
    ("the throat's bit area", "clause (H)", "the six (243)", ("a", "qN")),
    ("README match", "240 (b); copy_p2 C1", "the six (243)", ("r",)),
    ("build uses the closing energy", "111 (a); 239", "the six (243)", ("e",)),
    ("null energy per ray", "183 (Z)", "the six (243)", ()),
    ("the bulk's curvature from the plane", "p2_planck: ell^2 = 3 c^4 / 4 pi G (sigma - 2 dsigma)", "candidate", ("beta",)),
    ("the plane's vacuum", "p2_planck: Lambda4 = 8 pi G dsigma / c^4", "candidate", ("gamma",)),
    ("the horizon", "p2_gravity: m1 = G E1 / c^4", "candidate", ("eta",)),
    ("the capacity's form", "p2_gravity: N_max = sigma_P / 8 ln2 dsigma", "candidate", ("kappa", "pc")),
]
# h, cc: log2 of position 2's hbar and c against ours; b: the tension's power in SMS (kappa5^4 = 48 pi G / sigma^b c^4);
# a: G's power in the bit area; r: log2 of position 2's README against position 1's; e: log2 of the build's energy
# against the closing energy; beta: sigma's power in the curvature (ell^2 = kap / sigma^beta); gamma: G's power in the
# vacuum; eta: log2 of the horizon's factor (E1 = 2^-eta m1 c^4 / G); kappa: log2 of the capacity's factor; qN: N's power
# in the throat's area (4 pi r0^2 = N^qN A_bit, item 244); pc: delta sigma's power in the capacity (N_max ~ dsigma^-pc)
DEFAULT = dict(h=F(0), cc=F(0), b=F(1), a=F(1), r=F(0), e=F(0), beta=F(1), gamma=F(1), eta=F(0), kappa=F(0), qN=F(1),
               pc=F(1))
LIFT = dict(h=F(1), cc=F(1), b=F(3, 2), a=F(3, 2), r=F(1), e=F(1), beta=F(3, 2), gamma=F(3, 2), eta=F(1), kappa=F(1),
            qN=F(3, 2), pc=F(3, 2))


# ================================================================================ C1 the forms, as exponents of 2
def ex(i, j, w, z, n, P):
    """each quantity's exponent of 2 against ours, at lattice address (i, j) (G x 2^(i+j), tension x 2^(-2j)), our
    tension at S0 x 2^w, the offset's ratio x 2^z and a README of 2^n bits, under the constants P"""
    g, s = F(i) + F(j), -2 * F(j)
    sig, ds = F(w) + s, s + F(z)
    h, cc = P["h"], P["cc"]
    q = dict(G=g, sig=sig, ds=ds)
    q["k4"] = g - P["b"] * s - 4 * cc                     # SMS, against ours at the same place in the window
    q["ell2"] = 4 * cc - g - P["beta"] * sig              # the window's curvature, ell^2 = kap / sigma
    q["L4"] = P["gamma"] * g + ds - 4 * cc                # the plane's vacuum
    q["A"] = h + P["a"] * g - 3 * cc                      # clause (H): A_bit = 2 h G ln2 / pi c^3
    q["m1"] = q["A"] / 2 if not MUT.get("rows_drift") else q["A"]     # the one-bit throat, 4 pi (2 m1)^2 = A_bit
    q["E1"] = q["m1"] + 4 * cc - g - P["eta"]            # the horizon, m1 = G E1 / c^4
    q["n2"] = F(n) + P["r"]                               # position 2's README
    q["E"] = q["E1"] + P["qN"] * q["n2"] / 2              # N bits: the throat x sqrt N, its energy x sqrt N
    q["r0"] = q["m1"] + P["qN"] * q["n2"] / 2
    q["rho"] = q["E"] - 3 * q["r0"]
    q["sP"] = 7 * cc - h - 2 * g                          # sigma_P = c^7 / hbar G^2
    q["Nmax"] = q["sP"] - P["pc"] * ds + P["kappa"]       # N_max = sigma_P / 8 ln2 delta sigma
    return q


def slacks(v, P, c):
    """the sixteen acting bounds' slacks at v = {i, j, w, z, n, law, mu, field}, from the forms"""
    q = ex(v["i"], v["j"], v["w"], v["z"], v["n"], P)
    q1 = ex(0, 0, v["w"], 0, v["n"], DEFAULT)            # position 1: ours, the same README
    mu, law, fld = F(v["mu"]), F(v["law"]), F(v["field"])
    top = c["W"] + q["ell2"] - 2 * q["m1"]               # ITEM197: ell >= 8.5415 m1 (W where our tension tops out)
    floor_rel = -q["ell2"]                                # ell <= the table-top limit, read at the universe's own G
    return {
        "top (corridor inside the curvature)": top,
        "README capacity": c["lognmax0"] + q["Nmax"] - q["n2"],
        "plane positivity": c["c_pos"] + q["sig"] - q["ds"],
        "one coupling, above": -q["k4"] + fld,
        "one coupling, below": q["k4"] + fld,
        "table-top floor (relative)": floor_rel,
        "table-top floor (absolute)": P["beta"] * q["sig"],
        "matter exceptions (Cu2 off mirror)": F(3, 2) - law,
        "G ceiling": top + floor_rel,
        "throat matter regime": c["c_reg"] + q["rho"] - q["sig"],
        "survive: gravity, above": mu - q["G"],
        "survive: gravity, below": mu + q["G"],
        "survive: dark energy, above": mu - q["L4"],
        "survive: dark energy, below": mu + q["L4"],
        "survive: closing energy": mu - (q["E"] - q1["E"] + P["e"]),
        "survive: chemistry": mu - law,
    }


def rows(P, c):
    """each slack's constant and coefficients by unit steps; linearity checked at two further points"""
    zero = {v: 0 for v in VARS}
    f0 = slacks(zero, P, c)
    out = {n: {"const": f0[n]} for n in f0}
    for v in VARS:
        f1 = slacks(dict(zero, **{v: 1}), P, c)
        for n in f0:
            d = f1[n] - f0[n]
            if d:
                out[n][v] = d
    linear = True
    for pt in ({"i": 3, "j": -2, "w": 5, "z": 7, "n": 11, "law": 2, "mu": 13, "field": 1},
               {"i": -7, "j": 4, "w": 2, "z": -3, "n": 1, "law": 1, "mu": 2, "field": 0}):
        fp = slacks(pt, P, c)
        for n in f0:
            pred = out[n]["const"] + sum(out[n].get(v, 0) * pt[v] for v in VARS)
            linear &= fp[n] == pred
    return out, linear


def table_rows(b):
    return {n: {k: F(x) for k, x in coef.items() if F(x) != 0 or k == "const"} for n, (kk, s, coef, note) in b.items()
            if kk != "constant"}


def forms_vs_sector():
    """the forms' exponents against p2_planck.sector's floats at the twelve members"""
    base = PP.sector(1, F(1))
    co0 = PG.corridor(PG.G)
    worst = 0.0
    for name, (law, gf, sf) in PP.MEMBERS.items():
        g, s = int(math.log2(gf)), round(math.log2(float(sf)))
        j = -s // 2
        i = g - j
        q = ex(i, j, 0, 0, 0, DEFAULT)
        sec = PP.sector(gf, sf)
        co = PG.corridor(PG.G * gf)
        num = dict(k4=sec["k4"] / base["k4"], ell2=sec["ell"] ** 2 / base["ell"] ** 2, L4=sec["L4"] / base["L4"],
                   A=sec["A_bit"] / base["A_bit"], m1=sec["m1"] / base["m1"], E1=sec["E1"] / base["E1"],
                   sP=sec["sigma_P"] / base["sigma_P"], Nmax=sec["N_max"] / base["N_max"],
                   m1c=co["m1"] / co0["m1"])
        exp = dict(k4=q["k4"], ell2=q["ell2"], L4=q["L4"], A=q["A"], m1=q["m1"], E1=q["E1"], sP=q["sP"], Nmax=q["Nmax"],
                   m1c=q["m1"])
        worst = max(worst, max(abs(num[k] / 2 ** float(exp[k]) - 1) for k in num))
    return worst


# ================================================================================ C2 the constants at every universe
def evaluate_sector(sec, hbar_factor=1.0):
    """each constant with a form, evaluated on one computed sector (1 where it holds)"""
    Gx, sig, ds = sec["G"], sec["sigma"], sec["offset"]
    C, H, HBAR = PG.C, PG.H, PG.HBAR
    hb = C ** 7 / (sec["sigma_P"] * Gx ** 2) * hbar_factor              # hbar recovered from sigma_P
    cc = (hb * Gx / sec["lP"] ** 2) ** (1 / 3)                           # c recovered from the Planck length
    return {
        "shared SI": (hb / HBAR, cc / C),
        "G from the bulk and the plane": (48 * math.pi * Gx / (sec["k4"] * sig * C ** 4),),
        "the throat's bit area": (sec["A_bit"] / (2 * H * Gx * math.log(2) / (math.pi * C ** 3)),),
        "the bulk's curvature from the plane": (sec["ell"] ** 2 * 4 * math.pi * Gx * (sig - 2 * ds) / (3 * C ** 4),),
        "the plane's vacuum": (sec["L4"] * C ** 4 / (8 * math.pi * Gx * ds),),
        "the horizon": (sec["m1"] * C ** 4 / (Gx * sec["E1"]),),
        "the capacity's form": (sec["N_max"] * 8 * math.log(2) * ds / sec["sigma_P"],),
    }


def evaluate_members():
    """each constant with a form, evaluated on each member's computed sector"""
    return {name: evaluate_sector(PP.sector(gf, sf), 2.0 if MUT.get("si_not_shared") and name == "2b" else 1.0)
            for name, (law, gf, sf) in PP.MEMBERS.items()}


STATUS = {"README match": "DEFINED (240 (b): the README the same at both positions)",
          "build uses the closing energy": "DEFINED (111 (a); 239: the need is the energy given)",
          "null energy per ray": "NOT-EVALUATED (no form in these instruments; 183 (Z) holds net per ray)"}


def envelope(cells, i, j):
    """§15.2's S3: phi_ij(v) = max{ x_i : x in X, x_j <= v }, over the values v the cells take on axis j (in the index's
    own order, given as positions)"""
    vals = sorted({c[j] for c in cells})
    return [max(c[i] for c in cells if c[j] <= v) for v in vals]


def bulk_index(cy, ev, names, lift=None):
    """item 233's 5D basis (matter, 3 x ell/l5, kappa5^4) over the named universes, with each evaluated constant entered as
    a coordinate (lift = (constant, member): that constant takes a second value at that member)"""
    fd = B5M.five_d()
    base = {n: (B5M.LAW_ORDER.index(fd[n]["law"]), int(3 * fd[n]["e"]["ell_l5"]), int(fd[n]["e"]["k4"])) for n in names}
    cnames = [k for k in ev["ours"]]
    def cval(n, k):
        if lift and (k, n) == lift:
            return 2
        return 1 if all(abs(x - 1) < 1e-12 for x in ev[n][k]) else int(round(ev[n][k][0] * 1000))
    ext = {n: base[n] + tuple(cval(n, k) for k in cnames) for n in names}
    coords0 = ["matter", "ell_l5_x3", "kappa5_4"]
    def build(cells_by, coords):
        held = sorted(set(cells_by.values()))
        vals = [sorted({c[x] for c in held}, key=lambda t: (abs(t), t)) for x in range(len(coords))]
        ix = cy.Index("bulk5_closed", coords, [list(c) for c in held],
                      value_order={coords[x]: vals[x] for x in range(len(coords))})
        posn = [[vals[x].index(c[x]) for x in range(len(coords))] for c in held]       # each axis' declared order
        return held, ix, posn
    h0, ix0, p0 = build(base, coords0)
    h1, ix1, p1 = build(ext, coords0 + cnames)
    r0, r1 = cy.run(ix0, "1173", dict(OPTS)), cy.run(ix1, "1173", dict(OPTS))
    rep, keys = cy.coordinate_report(ix1)
    d = len(coords0) + len(cnames)
    return dict(n=len(h1), cnames=cnames, E0={v["language"]: v["E"] for v in r0["verdicts"]},
                E1={v["language"]: v["E"] for v in r1["verdicts"]}, alph={r["coordinate"]: r["values"] for r in rep},
                adds={r["coordinate"]: r["adds_nothing"] for r in rep}, keys=keys,
                flat={k: all(len(set(envelope(p1, 3 + x, jj))) == 1 for jj in range(d) if jj != 3 + x)
                      for x, k in enumerate(cnames)},
                base_flat={coords0[x]: all(len(set(envelope(p1, x, jj))) == 1 for jj in range(3) if jj != x)
                           for x in range(3)})


# ================================================================================ C3 what each constant reaches
def reach(c, kinds):
    base, _ = rows(DEFAULT, c)
    out = {}
    for name, src, whose, hooks in CONSTANTS:
        if not hooks:
            out[name] = dict(moved={}, cats=[])
            continue
        moved = {}
        for hk in hooks:
            P = dict(DEFAULT)
            P[hk] = LIFT[hk] if not MUT.get("lift_inert") else DEFAULT[hk]
            lr, _ = rows(P, c)
            for bn in base:
                rowd = {k: v for k, v in base[bn].items() if k != "const"} != {k: v for k, v in lr[bn].items() if k != "const"}
                cd = base[bn]["const"] != lr[bn]["const"]
                if rowd or cd:
                    moved[bn] = "row" if rowd else (moved.get(bn) or "constant")
        out[name] = dict(moved=moved, cats=sorted({kinds[bn] for bn in moved}, key=["universal", "structural",
                                                                                     "relativity"].index))
    return out


def thresholds(c):
    """the open direction (j -> -inf at fixed i) is closed by a bound whose j-coefficient is positive; for each hook, the
    value at which a closing bound's j-coefficient reaches zero (it is linear in the hook)"""
    base, _ = rows(DEFAULT, c)
    out = {}
    for hk in ("a", "gamma", "b"):
        P = dict(DEFAULT)
        P[hk] = DEFAULT[hk] + 1
        lr, _ = rows(P, c)
        for bn in base:
            j0, j1 = base[bn].get("j", F(0)), lr[bn].get("j", F(0))
            if j0 > 0 and j1 != j0:
                out[(hk, bn)] = (DEFAULT[hk], DEFAULT[hk] - j0 / (j1 - j0))
    return out


# ================================================================================ C4 the self-defence
def rank(M):
    M = [list(r) for r in M]
    rk, col = 0, 0
    ncol = len(M[0]) if M else 0
    while rk < len(M) and col < ncol:
        piv = next((r for r in range(rk, len(M)) if M[r][col] != 0), None)
        if piv is None:
            col += 1
            continue
        M[rk], M[piv] = M[piv], M[rk]
        for r in range(len(M)):
            if r != rk and M[r][col] != 0:
                f = M[r][col] / M[rk][col]
                M[r] = [x - f * y for x, y in zip(M[r], M[rk])]
        rk += 1
        col += 1
    return rk


QUANT = [("hbar2", "shared SI"), ("c2", "shared SI"), ("k4", "G from the bulk and the plane"),
         ("A", "the throat's bit area"), ("n2", "README match"), ("Eb", "build uses the closing energy"),
         ("ell2", "the bulk's curvature from the plane"), ("L4", "the plane's vacuum"), ("E1", "the horizon"),
         ("Nmax", "the capacity's form")]


def defence(freed=()):
    """position 2 as the map from its parameters (g, s, z, n) to the quantities the constants fix; ⅅ = dim q - rank J.
    A freed constant gives each quantity it fixes a parameter of its own"""
    def qv(g, s, z, n):
        P = DEFAULT
        # direct in (g, s): the lattice's (i, j) is a basis change and does not alter the rank
        sig, ds = s, s + z
        out = {"hbar2": F(0), "c2": F(0), "k4": g - P["b"] * s, "A": P["a"] * g, "n2": F(n), "ell2": -g - P["beta"] * sig,
               "L4": P["gamma"] * g + ds, "E1": P["a"] * g / 2 - g}
        out["Eb"] = out["E1"] + out["n2"] / 2
        out["Nmax"] = -2 * g - ds
        return out
    params = ["g", "s", "z", "n"]
    f0 = qv(0, 0, 0, 0)
    J = []
    for qn, owner in QUANT:
        row = []
        for p in params:
            a = dict(g=0, s=0, z=0, n=0)
            a[p] = 1
            row.append(qv(**a)[qn] - f0[qn])
        J.append(row)
    free_q = [k for k, (qn, owner) in enumerate(QUANT) if owner in freed]
    if MUT.get("free_relation") and not freed:
        free_q = [2]
    for k in free_q:
        for r, row in enumerate(J):
            row.append(F(1) if r == k else F(0))
    return dict(dim_q=len(J), dim_p=len(J[0]), rank=rank(J), D=len(J) - rank(J))


def two_paths():
    """G through the bulk's coupling (SMS) and through its curvature as the window states it (ell^2 = kap / sigma),
    with kappa5^4 and ell^2 as the sector states them -- exact rational algebra (pi and c cancel; test values rational)"""
    out = []
    for Gx, sig, ds, pi_, c in ((F(667, 10), F(5), F(1, 7), F(355, 113), F(3)), (F(2), F(1, 3), F(1, 19), F(22, 7), F(11)),
                                (F(9, 4), F(1000), F(1), F(3), F(1, 2))):
        ell2 = 3 * c ** 4 / (4 * pi_ * Gx * (sig - 2 * ds))
        k4 = 48 * pi_ * Gx / (sig * c ** 4)
        G_k = k4 * sig * c ** 4 / (48 * pi_)
        G_ell_sector = 3 * c ** 4 / (4 * pi_ * ell2 * (sig - 2 * ds))
        G_ell_window = 3 * c ** 4 / (4 * pi_ * ell2 * sig)
        out.append(dict(agree_sector=G_ell_sector == G_k, ratio=G_ell_window / G_k, expect=(sig - 2 * ds) / sig,
                        positivity=math.log2(sig / (2 * ds)), disagreement=1 - G_ell_window / G_k))
    return out


# ================================================================================ compute, report
def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "cb_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "cb_ia")
    c = {k: F(v) for k, v in BD.constants().items()}
    b = BD.bounds(BD.constants())
    kinds = {n: v[0] for n, v in b.items()}
    fr, linear = rows(DEFAULT, c)
    ev = evaluate_members()
    bo = BD.compute()
    return dict(c=c, b=b, kinds=kinds, rows=fr, linear=linear, table=table_rows(b), forms_err=forms_vs_sector(), ev=ev,
                bulk=bulk_index(cy, ev, B5M.POSITIONS), bulk12=bulk_index(cy, ev, list(PP.MEMBERS)),
                lifted={k: bulk_index(cy, ev, list(PP.MEMBERS), (k, "2b"))["E1"] for k in ev["ours"]},
                reach=reach(c, kinds), thr=thresholds(c),
                D=defence(), D_free={name: defence((name,)) for name, s, w, h in CONSTANTS},
                D_all=defence(tuple(n for n, s, w, h in CONSTANTS)), paths=two_paths(), b6=bo["cy"],
                pos_ours=float(c["c_pos"]))


def report(o):
    print("closed_bounds.py -- the constant bounds as bounds of a closed index (item 243)\n")
    print("C1 the acting bounds' rows from the forms (linear: %s; the forms against p2_planck.sector, worst %.1e):" % (
        o["linear"], o["forms_err"]))
    for n, r in o["rows"].items():
        same = r == o["table"][n]
        print("  %-38s %-10s %s %s" % (n, o["kinds"][n], {k: (str(v) if k != "const" else "%.3f" % float(v)) for k, v in r.items()},
                                       "= table" if same else "DIFFERS from table %s" % o["table"][n]))
    print("\nC2 the constants at the twelve members (1 where it holds):")
    for k in o["ev"]["ours"]:
        worst = max(abs(x - 1) for n in o["ev"] for x in o["ev"][n][k])
        print("  %-38s worst |x - 1| %.1e" % (k, worst))
    for k, st in STATUS.items():
        print("  %-38s %s" % (k, st))
    for label, bk in (("the seven position universes (item 233)", o["bulk"]), ("all twelve members", o["bulk12"])):
        print("  the bulk index, 5D basis, %s, with the constants as coordinates: %d cells; alphabet sizes %s" % (
            label, bk["n"], bk["alph"]))
        print("    adds nothing: %s; keys %s" % (bk["adds"], bk["keys"]))
        print("    E without the constants %s; with them %s" % (bk["E0"], bk["E1"]))
        print("    S3 envelopes flat against every other coordinate -- constants: %s; the basis' own: %s" % (
            bk["flat"], bk["base_flat"]))
    print("  all twelve, one constant given a second value at 2b -- E: %s" % o["lifted"])
    print("\nC3 what each constant reaches when lifted at position 2 (bound: row or constant moved):")
    for name, src, whose, hooks in CONSTANTS:
        r = o["reach"][name]
        print("  %-38s %-14s categories %s" % (name, whose, r["cats"]))
        for bn, how in r["moved"].items():
            print("      %-38s %-10s %s" % (bn, o["kinds"][bn], how))
    print("  the open direction: each closing bound's j-coefficient reaches zero at:")
    for (hk, bn), (d, t) in o["thr"].items():
        print("      %-6s stated %s, threshold %s  (%s)" % (hk, d, t, bn))
    print("\nC4 the self-defence: with every constant ⅅ = %d - %d = %d (dim p %d); without any: ⅅ = %d" % (
        o["D"]["dim_q"], o["D"]["rank"], o["D"]["D"], o["D"]["dim_p"], o["D_all"]["D"]))
    for name, d in o["D_free"].items():
        print("  freed %-38s ⅅ = %d (falls by %d)" % (name, d["D"], o["D"]["D"] - d["D"]))
    for p in o["paths"]:
        print("  two paths to G: coupling vs curvature with the offset agree: %s; vs the window's curvature: ratio %s = "
              "(sigma - 2 dsigma)/sigma: %s; disagreement 2^-%.6f, the positivity slack %.6f" % (
                  p["agree_sector"], p["ratio"], p["ratio"] == p["expect"], -math.log2(p["disagreement"]), p["positivity"]))
    print("  at ours the disagreement is 2^-%.3f (the plane positivity's constant)" % o["pos_ours"])
    y = o["b6"]
    print("\nC5 bounds.py B6: %d cells over the acting bounds; kind adds nothing: %s; constants in the index: %s" % (
        y["n"], "kind" in y["adds_nothing"], y["constants_in_index"]))


EXPECT_REACH = {
    "shared SI": ["universal", "structural", "relativity"],
    "G from the bulk and the plane": ["universal"],
    "the throat's bit area": ["universal", "structural", "relativity"],
    "README match": ["universal", "structural", "relativity"],
    "build uses the closing energy": ["relativity"],
    "null energy per ray": [],
    "the bulk's curvature from the plane": ["universal", "structural"],
    "the plane's vacuum": ["relativity"],
    "the horizon": ["structural", "relativity"],
    "the capacity's form": ["universal"],
}


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    met = " ".join(open(METHOD, encoding="utf-8").read().split())
    add("C0 M's item-243 words verbatim in the rulings file; the Method's closed-index sentences (§15.2, §15.5, §16, "
        "§16.1, §16.4) verbatim in The_Method_1_6-2.md", M243 in rul and all(q in met for q in READS))
    ok = o["linear"] and len(o["rows"]) == 16 and all(o["rows"][n] == o["table"][n] for n in o["rows"])
    ok &= o["forms_err"] < 1e-12
    add("C1 all sixteen acting rows computed from the stated forms equal bounds.py's table exactly (constants and "
        "coefficients); the forms agree with p2_planck.sector at the twelve members to 1e-12", ok)
    ev = o["ev"]
    ok = all(abs(x - 1) < 1e-12 for n in ev for k in ev[n] for x in ev[n][k]) and len(ev) == 12 and len(ev["ours"]) == 7
    for bk in (o["bulk"], o["bulk12"]):
        ok &= all(bk["alph"][k] == 1 and bk["adds"][k] for k in bk["cnames"]) and bk["E0"] == bk["E1"]
        ok &= all(bk["flat"].values()) and not bk["keys"]
    ok &= o["bulk"]["E0"]["order"] == 8 and o["bulk12"]["E0"]["order"] == 6 and o["bulk12"]["E0"]["algebra"] == 6
    ok &= all(o["lifted"][k]["order"] > o["bulk12"]["E0"]["order"] and o["lifted"][k]["algebra"] > o["bulk12"]["E0"]["algebra"]
              for k in o["lifted"])
    add("C2 seven constants with a form hold at all twelve bulk members (1e-12); on the bulk index (seven positions, and all "
        "twelve) each is a one-value coordinate that adds nothing, leaves every language's E unchanged (the index itself "
        "not closed: order E 8 and 6) and has a flat envelope; given a second value at one universe, each raises order and "
        "algebra E; README match and the build's energy defined; the null energy per ray not evaluated", ok)
    ok = {n: r["cats"] for n, r in o["reach"].items()} == EXPECT_REACH
    th = {k: v for k, v in o["thr"].items()}
    ok &= th.get(("a", "survive: closing energy")) == (F(1), F(2))
    ok &= th.get(("gamma", "survive: dark energy, above")) == (F(1), F(2))
    ok &= th.get(("b", "one coupling, below")) == (F(1), F(-1, 2))
    add("C3 lifted, shared SI, the bit area and the README match move bounds in all three categories; the curvature and "
        "the horizon in two; SMS, the vacuum, the capacity's form and the build's energy in one; the null energy per ray "
        "in none -- and the stated values keep the open direction closed (bit area's power of G 1 < 2, the vacuum's 1 < 2, "
        "SMS's tension power 1 > -1/2)", ok)
    D, Df, Da = o["D"], o["D_free"], o["D_all"]
    drops = {n: D["D"] - d["D"] for n, d in Df.items()}
    ok = D["dim_q"] == 10 and D["rank"] == 4 and D["D"] == 6 and Da["D"] == 0
    ok &= drops == {"shared SI": 2, "G from the bulk and the plane": 1, "the throat's bit area": 1, "README match": 1,
                    "build uses the closing energy": 1, "null energy per ray": 0, "the bulk's curvature from the plane": 1,
                    "the plane's vacuum": 1, "the horizon": 1, "the capacity's form": 1}
    ok &= all(p["agree_sector"] and p["ratio"] == p["expect"] and abs(-math.log2(p["disagreement"]) - p["positivity"]) < 1e-9
              for p in o["paths"])
    add("C4 the constants supply the self-defence: ⅅ = 10 - 4 = 6, each falls by the quantities it fixes when freed (shared "
        "SI 2, the rest 1, the null energy per ray 0), 0 with all freed; G's two paths (coupling, curvature) agree under the "
        "sector's curvature and disagree under the window's by exactly (sigma - 2 dsigma)/sigma = 2^-(positivity slack)", ok)
    y = o["b6"]
    add("C5 bounds.py B6: the acting bounds in M's three categories give 15 cells, kind adds nothing, no constant is a cell",
        y["n"] == 15 and "kind" in y["adds_nothing"] and not y["constants_in_index"])
    return res


MUTANTS = {"rows_drift": "the one-bit throat taken as the bit area, not its root",
           "si_not_shared": "hbar doubled at position 2b",
           "lift_inert": "a lift that moves nothing",
           "free_relation": "SMS freed in the default count"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-14s %-52s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
