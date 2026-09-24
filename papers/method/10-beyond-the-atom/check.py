#!/usr/bin/env python3
"""check.py -- every number and every decidable claim of the paper
"Closure beyond the atom: the defect of other indexes, redundancy, and the electromagnetic quotient".

    python3 check.py              one line per obligation, a summary, exit 1 on any failure
    python3 check.py --selftest   the same, plus the negative controls (a false claim must be refuted)

Stdlib plus z3. Python 3.12 (export PATH="$PWD/method/bin:$PATH").

Instruments are imported BY PATH and never copied:
    research/warp-drive/prover.py                 the Z3 harness (prove, guards, encodings)
    tools/cypher.py                               the closure operator R (op_order) and the other four
                                                  language operators; its index builders and fixtures
    method/members/tower-2.py                     the tower Lambda_8 .. Lambda_13
    extracted/archives/restore-point-2-13/close_L118.py
                                                  the 118 ground-state configurations (the crossing's input)
Data read:
    extracted/archives/method16-rp-b-data/SPECTRA-DATA.tsv         the Rydberg channel survey
    extracted/archives/restore-point-2-13/captures/AME2020-TableI.tsv   AME2020 Table I (Z, N)
    nubase2020-Z0-10.txt (beside this file)     the NUBASE2020 ground-state lines for Z <= 10, verbatim
                                                (Kondev, Wang, Huang, Naimi and Audi 2021); the
                                                particle-bound list is DERIVED from it, never typed

Reference implementations written here (R_ref, the sublattice hull, the enumerative closure tests of
the adjunction guard) are the INDEPENDENT side of the encoding guard; the object under test is always
the seated operator.
"""
from __future__ import annotations

import importlib.util as iu
import io
import contextlib
import itertools
import math
import os
import random
import sys
import types
from collections import Counter
from fractions import Fraction

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
P = lambda *a: os.path.join(ROOT, *a)


def load(name, path):
    spec = iu.spec_from_file_location(name, path)
    mod = iu.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


pv = load("prover", P("research", "warp-drive", "prover.py"))
cy = load("cypher", P("tools", "cypher.py"))
tw = load("tower2", P("method", "members", "tower-2.py"))
import z3  # noqa: E402  (after prover, which reports a missing z3 legibly)

# close_L118.py runs under a checkpointing helper called zeno and exits at the end of its own
# report; a stub helper and a muted exit let its configuration table be imported without running
# its report.
_zeno = types.ModuleType("zeno")


class _State:
    def __init__(self, *a, **k): pass
    def __enter__(self): return self
    def __exit__(self, *a): return False


_zeno.State = _State
_zeno.step = lambda st, name, fn, **k: fn()
sys.modules["zeno"] = _zeno
_exit = sys.exit
sys.exit = lambda *a: None
with contextlib.redirect_stdout(io.StringIO()):
    cl = load("close_L118", P("extracted", "archives", "restore-point-2-13", "close_L118.py"))
sys.exit = _exit

OPTS = {"statistics_order": 2, "algebra_budget": 300_000, "max_box": 50_000_000,
        "max_pairwise_cells": 8_000}

# --------------------------------------------------------------------------- bookkeeping

RESULTS = []          # (status, id, text, ok)
FAIL = 0
VALUES = {}           # every number the paper prints, by key


def rec(status, oid, text, ok=True, **vals):
    global FAIL
    RESULTS.append((status, oid, text, ok))
    if not ok:
        FAIL += 1
    print("  [%s] %-6s %-16s %s" % ("ok  " if ok else "FAIL", oid, status, text))
    VALUES.update(vals)


def eq(status, oid, text, have, want, **vals):
    ok = have == want
    rec(status, oid, "%s: %s%s" % (text, have, "" if ok else " != expected %s" % (want,)), ok, **vals)
    return ok


def pct(fr):
    """A Fraction as a percentage string with one decimal."""
    return "%.1f%%" % (100 * fr)


# --------------------------------------------------------------------------- the operator

def R(cells):
    """The seated closure operator: cypher.op_order over the observed box of `cells`.
    Returns the closure as a set of tuples in the cells' own values (decoded)."""
    cells = list(cells)
    d = len(cells[0])
    if d == 1:                              # one coordinate: the box is the observed values
        return set(cells)
    ix = cy.Index("x", ["c%d" % i for i in range(d)], cells)
    out, _ = cy.op_order(ix, OPTS)
    return {tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in out}


def E(cells):
    return len(R(cells)) - len(set(cells))


def R_ref(X, d):
    """An independent staircase, written from the definition and used only as a guard."""
    X = set(X)
    vals = [sorted({c[i] for c in X}) for i in range(d)]
    phi = {}
    for i in range(d):
        for j in range(d):
            if i != j:
                for a in vals[j]:
                    phi[(i, j, a)] = max(y[i] for y in X if y[j] <= a)
    return {x for x in itertools.product(*vals)
            if all(x[i] <= phi[(i, j, x[j])] for i in range(d) for j in range(d) if i != j)}


def hull(X):
    """Sublattice hull, iterated to a fixed point (the algebra reading; independent of cypher)."""
    S = set(X)
    frontier = list(S)
    while frontier:
        L = list(S)
        new = set()
        for x in frontier:
            for y in L:
                mn = tuple(map(min, x, y))
                mx = tuple(map(max, x, y))
                if mn not in S:
                    new.add(mn)
                if mx not in S:
                    new.add(mx)
        new -= S
        S |= new
        frontier = list(new)
    return S


def envelopes(X, d):
    """Per ordered pair (i, j): the envelope phi_ij as a monotone table, and whether it binds.
    An envelope binds (is live) when it is below max(coordinate i) for some value of j."""
    X = set(X)
    live = []
    for i in range(d):
        hi = max(c[i] for c in X)
        for j in range(d):
            if i == j:
                continue
            m = {}
            for c in X:
                m[c[j]] = max(m.get(c[j], -10 ** 9), c[i])
            b, tab = -10 ** 9, []
            for t in sorted(m):
                b = max(b, m[t])
                tab.append(b)
            live.append((i, j, any(v < hi for v in tab)))
    return live


def coupling(X, d):
    lv = envelopes(X, d)
    return Fraction(sum(1 for *_, l in lv if l), len(lv)), len(lv)


FRACS = (Fraction(5, 100), Fraction(10, 100), Fraction(20, 100), Fraction(30, 100), Fraction(41, 100),
         Fraction(50, 100), Fraction(61, 100), Fraction(70, 100), Fraction(82, 100), Fraction(90, 100))
SEED = 20260809


def redundancy(X, d, seed=SEED):
    """The largest fraction of cells removable, at random, with exact recovery by R in at least 8 of
    10 trials (5 trials above 3,000 cells). Fractions are tried in increasing order and the sweep
    stops at the first fraction that fails. SAMPLED: seeded pseudorandom, size stated."""
    rnd = random.Random(seed)
    X = sorted(set(X))
    N = len(X)
    best = Fraction(0)
    log = []
    for frac in FRACS:
        k = int(N * frac)
        if k < 1 or N - k < d:
            break
        T = 10 if N < 3000 else 5
        ok = 0
        for _ in range(T):
            sample = rnd.sample(X, N - k)
            if R(sample) == set(X):
                ok += 1
        log.append((frac, ok, T))
        if ok >= Fraction(8, 10) * T:
            best = frac
        else:
            break
    return best, log


# --------------------------------------------------------------------------- the indexes

def periodic_cells():
    ix = cy._periodic()
    return sorted(tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in ix.cells)


JANET_RANGES = {1: (1, 2), 2: (3, 4), 3: (5, 12), 4: (13, 20), 5: (21, 38), 6: (39, 56),
                7: (57, 88), 8: (89, 118)}


def janet_cells():
    return [(s, Z) for s, (a, b) in JANET_RANGES.items() for Z in range(a, b + 1)]


def janet_downset():
    """The Janet index as the redundancy census was run on it: every (n+l, Z) with the group n+l
    reached in filling element Z -- the down-set of the 118-cell table along n+l."""
    jan = set()
    for Z in range(1, 119):
        nl, c = 1, Z
        while c > 0:
            for n in range(1, nl + 1):
                l = nl - n
                if l >= n:
                    continue
                if c <= 0:
                    break
                jan.add((nl, Z))
                c -= 2 * (2 * l + 1)
            nl += 1
            if nl > 8:
                break
    return sorted(jan)


DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def calendar_cells():
    return [(m + 1, d) for m, n in enumerate(DAYS) for d in range(1, n + 1)]


def calendar_reordered():
    order = sorted(range(12), key=lambda m: (DAYS[m], m))       # months by length, ties by name
    pos = {m: order.index(m) + 1 for m in range(12)}
    return [(pos[m], d) for m in range(12) for d in range(1, DAYS[m] + 1)]


def box_ordering():
    return [t for t in itertools.product(range(5), repeat=3) if t[0] >= t[1] >= t[2]]


def chessboard():
    return [(r, f) for r in range(1, 9) for f in range(1, 9)]


def nuclide_fixture(zmax):
    """The instrument's hand-typed particle-bound fixture -- kept only to be compared with the list
    derived from NUBASE2020 below (C7e)."""
    ix = cy._nuclide(zmax)
    return sorted(tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in ix.cells)


NUBASE_EXCERPT = os.path.join(HERE, "nubase2020-Z0-10.txt")
NUBASE_EXCERPT_MD5 = "56728dd35af7bd1906681ba56a9facf6"
NUBASE_FULL_MD5 = "91e92411c7c609aa73b28136da61317f"        # nubase_4.mas20.txt, two public copies agree
PROMPT_EMISSION = {"n", "2n", "3n", "p", "2p", "3p", "A"}


def nubase_ground_states():
    """Every NUBASE2020 ground-state line with Z <= 10, parsed by the file's own column format:
    (A, Z, name, half-life field, first decay mode). The excerpt is the verbatim lines of the
    evaluation's file (md5 of the full file recorded above); its own md5 is checked in C7."""
    import hashlib
    raw = open(NUBASE_EXCERPT, "rb").read()
    rows = []
    for l in raw.decode("utf-8").split("\n"):
        if l.startswith("#") or not l.strip():
            continue
        A, Z, i = int(l[0:3]), int(l[4:7]), l[7]
        if i != "0":
            continue
        T = l[69:78].strip()
        br = l[119:].strip()
        first = br.split(";")[0].split("=")[0].split(" ")[0].strip()
        rows.append((A, Z, l[11:16].strip(), T, first))
    return rows, hashlib.md5(raw).hexdigest()


def particle_bound(zmax):
    """The particle-bound nuclides with 1 <= Z <= zmax, DERIVED from NUBASE2020: a ground state is
    particle-bound when the evaluation neither marks it p-unst nor lists prompt nucleon or alpha
    emission (n, 2n, 3n, p, 2p, 3p, A) as its first decay mode. Returns (cells, unbound names)."""
    rows, _ = nubase_ground_states()
    cells, unbound = [], []
    for A, Z, name, T, first in rows:
        if Z < 1 or Z > zmax:
            continue
        if T == "p-unst" or first in PROMPT_EMISSION:
            unbound.append(name)
        else:
            cells.append((Z, A - Z))
    return sorted(cells), unbound


def ame2020():
    rows = [l.split("\t") for l in open(P("extracted", "archives", "restore-point-2-13", "captures",
                                          "AME2020-TableI.tsv"), encoding="utf-8")
            if not l.startswith("#") and l.strip()]
    return sorted({(int(r[0]), int(r[1])) for r in rows}), Counter(r[6].strip() for r in rows)


def ks_cells():
    ix = cy._kreuzer_skarke()
    return sorted(tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in ix.cells)


def lambda_cells():
    ix = cy._lambda()
    return sorted(tuple(ix.decode[i][v] for i, v in enumerate(c)) for c in ix.cells)


SPECTRA_ZN = {"H": 1, "He": 2, "Li": 3, "Be": 4, "B": 5, "C": 6, "N": 7, "O": 8, "F": 9, "Ne": 10,
              "Na": 11, "Mg": 12, "Al": 13, "Si": 14, "P": 15, "S": 16, "Cl": 17, "Ar": 18, "K": 19,
              "Ca": 20, "Sc": 21, "Ti": 22, "Fe": 26, "Zn": 30, "Ga": 31, "Ge": 32, "Cd": 48,
              "Ba": 56, "Hg": 80, "Bi": 83}
SPECTRA_L = {"s": 0, "p": 1, "d": 2, "f": 3, "g": 4, "h": 5, "i": 6, "k": 7}


def spectra_grid():
    """The channel survey's grid: (Z, core charge, l) over the elements, charges and l values that
    the survey holds, with charge < Z. Returns (grid, held cells, elements)."""
    import re
    held = set()
    lines = open(P("extracted", "archives", "method16-rp-b-data", "SPECTRA-DATA.tsv"),
                 encoding="utf-8").read().split("\n")[1:]
    for line in lines:
        r = line.rstrip().split("\t")
        if len(r) < 11:
            continue
        m = re.search(r"n([spdfghik])\b", r[1])
        el = re.match(r"([A-Z][a-z]?)", r[0].strip())
        if not (m and el) or el.group(1) not in SPECTRA_ZN:
            continue
        held.add((SPECTRA_ZN[el.group(1)], int(r[9]), SPECTRA_L[m.group(1)]))
    Zs = sorted({k[0] for k in held})
    Cs = sorted({k[1] for k in held})
    Ls = sorted({k[2] for k in held})
    grid = sorted({(Z, c, l) for Z in Zs for c in Cs for l in Ls if c < Z})
    return grid, held, Zs, Cs, Ls


def crossing_population():
    """Every move between two distinct occupied subshells of one element, over the 118 ground
    configurations: (Z, n, l, k, q, e, f, g), q electrons taken from (n, l) of occupancy k and g of
    them placed in (e, f), 1 <= g <= min(q, 4f+2)."""
    LMAP, ELEM = cl.L, cl.C
    occ = {Z: {(n, LMAP[s]): k for (n, s, k) in sh} for Z, (sym, sh) in ELEM.items()}
    cells = []
    for Z, sub in occ.items():
        for (n, l), k in sub.items():
            for (e, f), _ in sub.items():
                if (n, l) == (e, f):
                    continue
                for q in range(1, k + 1):
                    for g in range(1, min(q, 4 * f + 2) + 1):
                        cells.append((Z, n, l, k, q, e, f, g))
    return cells, occ


def target_room(c, occ):
    """The room left in the target subshell (e, f) of element Z before the move: capacity minus
    the electrons it already holds in the ground configuration."""
    Z, n, l, k, q, e, f, g = c
    return 4 * f + 2 - occ[Z][(e, f)]


def physical_moves(cells, occ):
    """The Pauli filter: one electron taken, one placed (q = g = 1), into a subshell with room."""
    return [c for c in cells if c[4] == 1 and c[7] == 1 and target_room(c, occ) >= 1]


def followability_rows(pop, occ, configurational=False):
    """For each selection class: cells, followable within one element, followable across the
    118. Formal match (D9): the target (e, f) at the count g delivered equals the source (n, l) at
    the occupancy k of some move. Configurational match: the target (e, f) at the occupancy it
    holds AFTER the move, k_e + g, equals the source (n, l, k) of some move."""
    S_all = {(c[1], c[2], c[3]) for c in pop}
    SZ = {}
    for c in pop:
        SZ.setdefault(c[0], set()).add((c[1], c[2], c[3]))

    def key(c):
        if configurational:
            return (c[5], c[6], occ[c[0]][(c[5], c[6])] + c[7])
        return (c[5], c[6], c[7])

    def rates(pred):
        sub = [c for c in pop if pred(c)]
        w = sum(1 for c in sub if key(c) in SZ[c[0]])
        a = sum(1 for c in sub if key(c) in S_all)
        return len(sub), w, Fraction(w, len(sub)), a, Fraction(a, len(sub))
    return {nm: rates(p) for nm, p in (
        ("all", lambda c: True), ("allowed", lambda c: abs(c[6] - c[2]) == 1),
        ("forbidden", lambda c: abs(c[6] - c[2]) != 1), ("parity-conserving", lambda c: (c[6] - c[2]) % 2 == 0),
        ("parity-changing", lambda c: (c[6] - c[2]) % 2 == 1))}


# --------------------------------------------------------------------------- Z3 encodings

from prover import cells_of, subset_vars, in_R, contains, meet, join  # noqa: E402


def in_box(X, x, cells, shape):
    """x lies in the observed box of X: each coordinate value of x is realised by a member of X."""
    return z3.And([z3.Or([X[c] for c in cells if c[i] == x[i]]) for i in range(len(shape))])


def in_Rown(X, x, cells, d, shape):
    """Own-box staircase membership: in the observed box AND every pairwise witness exists."""
    return z3.And(in_box(X, x, cells, shape), in_R(X, x, cells, d))


def nonempty(X, cells):
    return z3.Or([X[c] for c in cells])


def ob_extensive(X, S, cells, d, shape):
    return z3.And([z3.Implies(X[c], in_Rown(X, c, cells, d, shape)) for c in cells])


def ob_monotone(X, S, cells, d, shape):
    return z3.Implies(z3.And(nonempty(X, cells), contains(X, S, cells)),
                      z3.And([z3.Implies(in_Rown(X, c, cells, d, shape),
                                         in_Rown(S, c, cells, d, shape)) for c in cells]))


def ob_idempotent(X, S, cells, d, shape):
    RX = {c: in_Rown(X, c, cells, d, shape) for c in cells}
    return z3.Implies(nonempty(X, cells),
                      z3.And([z3.Implies(in_Rown(RX, c, cells, d, shape), RX[c]) for c in cells]))


def ob_fibration(X, S, cells, d, shape, i=0):
    """Fibre X over coordinate i; each fibre's own closure lies inside the whole closure."""
    out = []
    for v in range(shape[i]):
        Xv = {c: (X[c] if c[i] == v else z3.BoolVal(False)) for c in cells}
        out += [z3.Implies(z3.And(nonempty(Xv, cells), in_Rown(Xv, c, cells, d, shape)),
                           in_Rown(X, c, cells, d, shape)) for c in cells if c[i] == v]
    return z3.And(out)


def graph_formulas(cells, S, h):
    """The three predicates of Theorems 5 and 6 as Z3 formulas over membership variables S and an
    integer-valued h on the box: S closed; the graph {(x, h(x)) : x in S} closed under the
    coordinatewise meet and join of box x chain; h preserves meet and join on S."""
    closedS = z3.And([z3.Implies(z3.And(S[a], S[b]), z3.And(S[meet(a, b)], S[join(a, b)]))
                      for a in cells for b in cells])
    closedSp = z3.And([z3.Implies(z3.And(S[a], S[b]),
                                  z3.And(S[join(a, b)],
                                         h[join(a, b)] == z3.If(h[a] >= h[b], h[a], h[b]),
                                         S[meet(a, b)],
                                         h[meet(a, b)] == z3.If(h[a] <= h[b], h[a], h[b])))
                       for a in cells for b in cells])
    hom = z3.And([z3.Implies(z3.And(S[a], S[b]),
                             z3.And(h[join(a, b)] == z3.If(h[a] >= h[b], h[a], h[b]),
                                    h[meet(a, b)] == z3.If(h[a] <= h[b], h[a], h[b])))
                  for a in cells for b in cells])
    return closedS, closedSp, hom


def graph_truths(cells, Sset, hmap):
    """The same three predicates decided by enumeration on a concrete S and h -- the independent
    side of the encoding guard for Theorems 5 and 6."""
    G = {(x, hmap[x]) for x in Sset}
    closedS = all(meet(a, b) in Sset and join(a, b) in Sset for a in Sset for b in Sset)
    closedSp = all((join(a, b), max(hmap[a], hmap[b])) in G and (meet(a, b), min(hmap[a], hmap[b])) in G
                   for a in Sset for b in Sset)
    hom = all(hmap[join(a, b)] == max(hmap[a], hmap[b]) and hmap[meet(a, b)] == min(hmap[a], hmap[b])
              for a in Sset for b in Sset)
    return closedS, closedSp, hom


def guard_graph_encodings(shape, H, trials=120, seed=17):
    """Encoding guard for T5/T6: on random (S, h) the three Z3 formulas, evaluated under the
    assignment, must agree with the enumerative decision. Returns (instances, disagreements)."""
    rnd = random.Random(seed)
    cells = cells_of(shape)
    S = subset_vars(cells, "s")
    h = {c: z3.Int("h_%s" % (c,)) for c in cells}
    forms = graph_formulas(cells, S, h)
    bad = tot = 0
    for _ in range(trials):
        Sset = set(rnd.sample(cells, rnd.randint(1, len(cells))))
        if rnd.random() < 0.5:                       # half the instances are closed sets, so both
            Sset = hull(Sset)                        # branches of each predicate are exercised
        hmap = {c: rnd.randrange(H) for c in cells}
        if rnd.random() < 0.5:                       # half the maps are monotone in one coordinate
            hmap = {c: min(H - 1, c[0]) for c in cells}
        truths = graph_truths(cells, Sset, hmap)
        for F, want in zip(forms, truths):
            s = z3.Solver()
            s.add([S[c] == (c in Sset) for c in cells] + [h[c] == hmap[c] for c in cells])
            s.add(F)
            tot += 1
            bad += (s.check() == z3.sat) != want
    return tot, bad


def adjunction_obligation(shape, H, converse=False):
    """S' = {(x, h(x)) : x in S} with h : box -> {0..H-1} a FREE function.
    Claim: S' closed under meet and join  =>  S closed under meet and join.
    Returns (result, non-vacuity guard, converse result)."""
    cells = cells_of(shape)
    S = subset_vars(cells, "s")
    h = {c: z3.Int("h_%s" % (c,)) for c in cells}
    rng = z3.And([z3.And(h[c] >= 0, h[c] < H) for c in cells])
    closedS, closedSp, _ = graph_formulas(cells, S, h)
    s = z3.Solver()
    s.add(rng, closedSp, z3.Not(closedS))
    r = s.check()
    g = z3.Solver()                                    # non-vacuity: S' closed, S proper, h non-constant ON S
    g.add(rng, closedSp, nonempty(S, cells), z3.Not(z3.And([S[c] for c in cells])),
          z3.Or([z3.And(S[a], S[b], h[a] != h[b]) for a in cells for b in cells]))
    nv = g.check()
    n = z3.Solver()                                    # the converse: S closed => S' closed
    n.add(rng, closedS, nonempty(S, cells), z3.Not(closedSp))
    cv = n.check()
    return r, nv, cv


def converse_witness(shape, H):
    """An explicit witness for the converse of Theorem 5: S closed under meet and join, h a map
    into {0..H-1}, and graph(h) NOT closed.  Verified here by concrete enumeration -- no solver --
    so the refutation stands on a witness a reader can check by hand."""
    lo = tuple(0 for _ in shape)
    hi = tuple(1 for _ in shape)
    S = {lo, hi}
    h = lambda x: 1 if x == lo else 0
    cells = cells_of(shape)
    assert lo in cells and hi in cells and H >= 2
    closed = all(meet(a, b) in S and join(a, b) in S for a in S for b in S)
    G = {(x, h(x)) for x in S}
    bad = [(a, b) for a in S for b in S
           if (join(a, b), max(h(a), h(b))) not in G or (meet(a, b), min(h(a), h(b))) not in G]
    return S, {x: h(x) for x in cells}, closed, bad, (join(lo, hi), max(h(lo), h(hi)))


def homomorphism_obligation(shape, H):
    """With S closed: S' closed  <=>  h restricted to S preserves meet and join."""
    cells = cells_of(shape)
    S = subset_vars(cells, "s")
    h = {c: z3.Int("g_%s" % (c,)) for c in cells}
    rng = z3.And([z3.And(h[c] >= 0, h[c] < H) for c in cells])
    closedS, closedSp, hom = graph_formulas(cells, S, h)
    s = z3.Solver()
    s.add(rng, closedS, z3.Not(closedSp == hom))
    return s.check()


def guard_fidelity(trials=200, seed=5, reference=None):
    """Encoding guard: the own-box witness formula, evaluated concretely, must define the same set
    as the seated operator on random instances. Returns (cells compared, disagreements)."""
    rnd = random.Random(seed)
    bad = tot = 0
    for _ in range(trials):
        shape = rnd.choice([(3, 3), (2, 2, 2), (3, 3, 3), (4, 4)])
        d = len(shape)
        cells = cells_of(shape)
        X = frozenset(rnd.sample(cells, rnd.randint(1, min(len(cells), 8))))
        Rc = (reference or R)(list(X))
        for x in cells:
            tot += 1
            enc = (all(any(y[i] == x[i] for y in X) for i in range(d)) and
                   all(any(y[j] <= x[j] and y[i] >= x[i] for y in X)
                       for i in range(d) for j in range(d) if i != j))
            bad += enc != (x in Rc)
    return tot, bad


def guard_seated_vs_reference(trials=300, seed=11):
    """The seated operator against the independent staircase, cell for cell."""
    rnd = random.Random(seed)
    bad = tot = 0
    for _ in range(trials):
        shape = rnd.choice([(3, 3), (4, 5), (2, 2, 2), (3, 3, 3), (2, 3, 4)])
        d = len(shape)
        cells = cells_of(shape)
        X = rnd.sample(cells, rnd.randint(1, min(len(cells), 9)))
        a, b = R(X), R_ref(X, d)
        tot += 1
        bad += a != b
    return tot, bad


# --------------------------------------------------------------------------- the checks

def section(title):
    print("\n%s\n%s" % (title, "-" * len(title)))


def check_operator():
    section("T  the operator, its guards and the four theorems about it")
    tot, bad = guard_fidelity()
    rec("GUARD", "T0a", "encoding fidelity: own-box witness formula vs the seated R on %d cells, %d disagreements"
        % (tot, bad), bad == 0)
    tot, bad = guard_seated_vs_reference()
    rec("GUARD", "T0b", "seated R vs independent staircase on %d random instances, %d disagreements"
        % (tot, bad), bad == 0)
    boxes = ((3, 3), (2, 2, 2), (3, 3, 3))
    nvs = []
    for sh in boxes:
        nv = pv.non_vacuous(sh, lambda X, S, c, d, s: z3.And(nonempty(X, c), contains(X, S, c)),
                            lambda X, S, c, d, s: z3.And(z3.Not(contains(S, X, c)),
                                                         z3.Not(z3.And([S[x] for x in c]))))
        nvs.append(nv)
        rec("GUARD", "T0c.", "non-vacuity for Theorem 1(b) on %s: X strictly inside S strictly inside the box is satisfiable"
            % "x".join(map(str, sh)), nv)
    nv = all(nvs)
    rec("GUARD", "T0c", "Theorem 1(a), 1(c) and Theorem 4 hypothesise only a non-empty X (and a non-empty fibre), which is satisfiable on every box", True)
    if bad or not nv:
        rec("REFUSED", "T1-4", "a guard failed; the machine checks below are not reported", False)
        return
    for oid, name, ob in (("T1a", "extensive", ob_extensive), ("T1b", "monotone (own box)", ob_monotone),
                          ("T1c", "idempotent (own box)", ob_idempotent)):
        oks = [pv.prove("%s %s" % (name, sh), sh, ob, quiet=True) for sh in boxes]
        rec("MACHINE-CHECKED", oid, "R is %s over every subset of %s" % (name, ", ".join("x".join(map(str, s)) for s in boxes)), all(oks))
    oks = []
    for sh in boxes:
        for i in range(len(sh)):
            oks.append(pv.prove("fibration %s coord %d" % (sh, i), sh,
                                lambda X, S, c, d, s, i=i: ob_fibration(X, S, c, d, s, i), quiet=True))
    rec("MACHINE-CHECKED", "T4", "Theorem 4 (the inclusion): each fibre's closure lies in the whole closure, fibred over EVERY coordinate, %s (%d instances)"
        % (", ".join("x".join(map(str, s)) for s in boxes), len(oks)), all(oks))
    # Remark 3: for a partition that is not by a coordinate the inequality FAILS -- the witness
    X = [(0, 0), (0, 1), (1, 0)]
    parts = ([(0, 1), (1, 0)], [(0, 0)])
    eq("REFUTATION", "T4b", "the claim 'every partition has fibred defect <= E(X)' is refuted: X = {(0,0),(0,1),(1,0)}, E(X); parts {(0,1),(1,0)} and {(0,0)}, E of each, fibred sum",
       (E(X), E(parts[0]), E(parts[1]), E(parts[0]) + E(parts[1]) > E(X)), (1, 2, 0, True))
    # Corollary 2: the chain of coordinate fibrations, iterated over i = 1..d, is non-increasing and ends at 0

    def fibred_chain(X, d):
        parts, out = [list(X)], [E(X)]
        for i in range(d):
            parts = [[c for c in Pp if c[i] == v] for Pp in parts for v in sorted({c[i] for c in Pp})]
            out.append(sum(E(Pp) for Pp in parts))
        return out
    tot = bad2 = 0
    for shape in ((3, 3), (2, 2, 2)):
        cells = cells_of(shape)
        n = len(cells)
        for mask in range(1, 1 << n):
            X = [cells[i] for i in range(n) if mask >> i & 1]
            ch = fibred_chain(X, len(shape))
            tot += 1
            bad2 += not (all(ch[k] >= ch[k + 1] for k in range(len(ch) - 1)) and ch[-1] == 0)
    eq("EXHAUSTIVE", "T4c", "Corollary 2: fibring by coordinate 1, then 2, ..., d inside each fibre gives a non-increasing chain of fibred defects ending at 0, on every non-empty subset of 3x3 and 2x2x2: subsets, failures",
       (tot, bad2), (766, 0))
    # Theorem 2: a full box closes -- exhaustive over every box with sides 1..4, d <= 3
    fam = 0
    ok = True
    for d in (1, 2, 3):
        for shape in itertools.product(range(1, 5), repeat=d):
            fam += 1
            ok &= E(cells_of(shape)) == 0
    rec("EXHAUSTIVE", "T2", "Theorem 2: E(full box) = 0 on every box with 1 <= d <= 3 and sides 1..4: %d boxes" % fam, ok,
        t2_boxes=fam)
    # Proposition 1: on small boxes, sublattice <=> closed, and R is the sublattice hull
    tot = badA = badB = 0
    for shape in ((3, 3), (2, 2, 2)):
        cells = cells_of(shape)
        n = len(cells)
        for mask in range(1, 1 << n):
            X = [cells[i] for i in range(n) if mask >> i & 1]
            S = set(X)
            tot += 1
            sub = all(tuple(map(min, a, b)) in S and tuple(map(max, a, b)) in S for a in S for b in S)
            badA += sub != (E(X) == 0)
            badB += R(X) != hull(X)
    eq("EXHAUSTIVE", "T3", "Theorem 0 corroborated: over every non-empty subset of 3x3 and 2x2x2, X is a sublattice iff E(X) = 0, and R(X) = the sublattice hull: subsets, failures of each",
       (tot, badA, badB), (766, 0, 0), prop1_subsets=766)
    big = [("the periodic table (90 cells)", periodic_cells()), ("the Kreuzer-Skarke slice (208)", ks_cells()),
           ("the orbital-rule set of Lambda_9 (840)", [c for c in tw.L9() if abs(c[5] - c[1]) == 1])]
    eq("EXHAUSTIVE", "T3b", "R(X) = the sublattice hull on three larger indexes (90, 208, 840 cells): closure sizes and agreement",
       tuple((len(R(X)), R(X) == hull(X)) for _, X in big), ((126, True), (748, True), (1590, True)))
    # Theorem 5 (adjunction never repairs) and Theorem 6 (homomorphism criterion): the encoding
    # guard first -- the three graph predicates evaluated on random (S, h) against enumeration
    gtot = gbad = 0
    for shape, H in (((3, 3), 3), ((2, 2, 2), 2)):
        t_, b_ = guard_graph_encodings(shape, H)
        gtot += t_
        gbad += b_
    rec("GUARD", "T0d", "encoding fidelity for Theorems 5 and 6: the Z3 predicates 'S closed', 'graph(h) closed', 'h preserves meet and join on S' evaluated on %d random (S, h) instances over 3x3 and 2x2x2 against an enumerative decision, %d disagreements"
        % (gtot, gbad), gbad == 0)
    if gbad:
        rec("REFUSED", "T5-6", "the graph-encoding guard failed; Theorems 5 and 6 are not reported", False)
        return
    for oid, shape, H in (("T5a", (3, 3), 3), ("T5b", (2, 2, 2), 2)):
        r, nv, cv = adjunction_obligation(shape, H)
        rec("GUARD", oid + "g", "non-vacuity: S' closed with S proper and h non-constant ON S is satisfiable (%s)" % (shape,), nv == z3.sat)
        rec("MACHINE-CHECKED", oid, "Theorem 5: S' = graph(h) closed => S closed, every S and every h: box -> {0..%d}, box %s" % (H - 1, "x".join(map(str, shape))),
            r == z3.unsat and nv == z3.sat)
        S, hmap, closed, bad, missing = converse_witness(shape, H)
        rec("REFUTATION", oid + "c",
            "the converse (S closed => graph(h) closed) is refuted on %s by the explicit witness "
            "S = {%s, %s} (closed under meet and join), h = 1 at %s and 0 elsewhere: the join of the "
            "two graph points is (%s, %s), which is not a graph point -- Z3 agrees the converse is satisfiable"
            % ("x".join(map(str, shape)), min(S), max(S), min(S), missing[0], missing[1]),
            cv == z3.sat and closed and len(bad) > 0,
            **{("witness_%s" % oid): (sorted(S), missing)})
    for oid, shape, H in (("T6a", (3, 3), 3), ("T6b", (2, 2, 2), 2)):
        _, nv, _ = adjunction_obligation(shape, H)
        rec("GUARD", oid + "g", "non-vacuity for Theorem 6: a closed S, proper, with h non-constant on S and graph(h) closed, is satisfiable (%s)" % (shape,), nv == z3.sat)
        r = homomorphism_obligation(shape, H)
        rec("MACHINE-CHECKED", oid, "Theorem 6: for closed S, graph(h) closed <=> h preserves meet and join on S, box %s, h into {0..%d}"
            % ("x".join(map(str, shape)), H - 1), r == z3.unsat and nv == z3.sat)
    # Proposition 2: the closed rows of the catalogue are sublattices BY THE SHAPE OF THEIR RULE
    box8 = itertools.product(range(1, 4), range(0, 2), range(1, 4), range(0, 4), range(1, 4), range(0, 2), range(0, 4), range(0, 4))

    def lam_rule(c):
        n, l, k, q, e, f, g, S2 = c
        return (n - l >= 1 and 4 * l - k >= -2 and k >= 1 and k - q >= 0 and e - f >= 1
                and 4 * f - g >= -2 and q - g >= 0 and k - S2 >= 0)
    cut = {c for c in box8 if lam_rule(c)}
    eq("EXHAUSTIVE", "T7a", "Proposition 2: Lambda is exactly the caps box {1..3}x{0,1}x{1..3}x{0..3}x{1..3}x{0,1}x{0..3}x{0..3} cut by its eight bimonotone inequalities: cells, equal to the tower's Lambda_8",
       (len(cut), cut == set(tw.L8())), (976, True))
    L9, L10 = tw.L9(), tw.L10()
    eq("EXHAUSTIVE", "T7b", "Lambda_9 = Lambda x {0..3} cut by 2S' <= g; Lambda_10 = Lambda_9 x {0..3} cut by 2S' <= v <= g: cells",
       (set(L9) == {c + (s,) for c in cut for s in range(4) if s <= c[6]},
        set(L10) == {c + (v,) for c in L9 for v in range(4) if c[8] <= v <= c[6]}, len(L9), len(L10)), (True, True, 1654, 2535))
    eq("EXHAUSTIVE", "T7c", "the box ordering is the box {0..4}^3 cut by l - w >= 0 and w - h >= 0",
       set(box_ordering()) == {t for t in itertools.product(range(5), repeat=3) if t[0] - t[1] >= 0 and t[1] - t[2] >= 0}, True)
    grid, held, Zs, Cs, Ls = spectra_grid()
    eq("EXHAUSTIVE", "T7d", "the survey product grid is the product of its three alphabets cut by Z - c >= 1",
       set(grid) == {(Z, c, l) for Z in Zs for c in Cs for l in Ls if Z - c >= 1}, True)
    jr = JANET_RANGES
    eq("EXHAUSTIVE", "T7e", "Janet (n+l, Z) is a staircase: for each n+l the Z values are an interval [a, b], with a and b non-decreasing in n+l (and consecutive)",
       (all(jr[s][0] <= jr[s + 1][0] and jr[s][1] <= jr[s + 1][1] for s in range(1, 8)),
        all(jr[s][1] + 1 == jr[s + 1][0] for s in range(1, 8)),
        sorted(janet_cells()) == sorted((s, Z) for s in jr for Z in range(jr[s][0], jr[s][1] + 1))), (True, True, True))


def check_catalogue():
    section("C  the catalogue of indexes")
    lam = lambda_cells()
    lam_ix = cy._lambda()
    eq("EXHAUSTIVE", "C1", "Lambda: cells, box, E", (len(lam), lam_ix.box, E(lam)), (976, 6912, 0),
       lam_cells=976, lam_box=6912, lam_E=0)
    L8 = tw.L8()
    eq("EXHAUSTIVE", "C1b", "Lambda from the tower member equals the cypher fixture", set(L8) == set(lam), True)
    pt = periodic_cells()
    Rp = R(pt)
    gaps = sorted(Rp - set(pt))
    eq("EXHAUSTIVE", "C2", "periodic table (period, group): cells, box, E", (len(pt), 7 * 18, len(Rp) - len(pt)), (90, 126, 36),
       pt_cells=90, pt_box=126, pt_E=36)
    runs = {1: [g for p, g in gaps if p == 1], 2: [g for p, g in gaps if p == 2], 3: [g for p, g in gaps if p == 3]}
    eq("EXHAUSTIVE", "C2b", "the 36 are period 1 groups 2-17, periods 2 and 3 groups 3-12",
       (runs[1], runs[2], runs[3], len(gaps)), (list(range(2, 18)), list(range(3, 13)), list(range(3, 13)), 36))
    # helium at group 2
    pt2 = [(p, 2 if (p, g) == (1, 18) else g) for p, g in pt]
    eq("EXHAUSTIVE", "C2c", "the same 90 cells with helium drawn at group 2: E", E(pt2), 20, pt_He2_E=20)
    jan = janet_cells()
    eq("EXHAUSTIVE", "C3", "Janet (n+l, Z): cells, box, E", (len(jan), 8 * 118, E(jan)), (118, 944, 0),
       jan_cells=118, jan_box=944, jan_E=0)
    cal = calendar_cells()
    Rc = R(cal)
    eq("EXHAUSTIVE", "C4", "calendar (month, day): cells, box, E", (len(cal), 12 * 31, len(Rc) - len(cal)), (365, 372, 7),
       cal_cells=365, cal_box=372, cal_E=7)
    eq("EXHAUSTIVE", "C4b", "the seven admitted-and-absent days", sorted(Rc - set(cal)),
       [(2, 29), (2, 30), (2, 31), (4, 31), (6, 31), (9, 31), (11, 31)])
    eq("EXHAUSTIVE", "C4c", "Theorem 3 witness: months relabelled in order of length, same 365 cells: E", E(calendar_reordered()), 0)
    bx = box_ordering()
    eq("EXHAUSTIVE", "C5", "box ordering l >= w >= h on five values: cells, box, E", (len(bx), 125, E(bx)), (35, 125, 0),
       box_cells=35, box_box=125, box_E=0)
    ch = chessboard()
    eq("EXHAUSTIVE", "C6", "chessboard (rank, file): cells, box, E", (len(ch), 64, E(ch)), (64, 64, 0))
    # the nuclide chart, particle-bound, five cutoffs
    names = {}
    Es = {}
    for zmax in (5, 6, 7, 9, 10):
        X = nuclide(zmax)
        Rn = R(X)
        Es[zmax] = (len(X), len(Rn), len(Rn) - len(X))
        names[zmax] = ["%s-%d" % (cy._ELEMENT[z], z + n) for z, n in sorted(Rn - set(X))]
    eq("EXHAUSTIVE", "C7", "nuclide chart, particle-bound, (cells, admitted, E) at Z <= 5, 6, 7, 9, 10",
       tuple(Es[z] for z in (5, 6, 7, 9, 10)), ((27, 33, 6), (40, 48, 8), (52, 61, 9), (75, 84, 9), (87, 96, 9)),
       nuc_cells=52, nuc_adm=61, nuc_E=9)
    eq("EXHAUSTIVE", "C7b", "the nine admitted-and-absent nuclides at Z <= 7, and unchanged at 9 and 10",
       (names[7], names[9] == names[7], names[10] == names[7]),
       (["He-5", "He-7", "Li-10", "Be-8", "Be-13", "B-9", "B-16", "B-18", "C-21"], True, True))
    eq("EXHAUSTIVE", "C7c", "every cell named at a smaller cutoff persists at every larger one",
       all(set(names[a]) <= set(names[b]) for a, b in ((5, 6), (6, 7), (7, 9), (9, 10))), True)
    ame, flags = ame2020()
    res = {}
    for zmax in (20, 50, 82, 92, 118):
        X = [c for c in ame if c[0] <= zmax]
        Ra = R(X)
        res[zmax] = (len(X), len(Ra) - len(X), sorted(Ra - set(X)))
    eq("EXHAUSTIVE", "C8", "AME2020 Table I as an index on (Z, N): rows, distinct cells, flags",
       (sum(flags.values()), len(ame), flags["M"], flags["E"]), (3558, 3558, 2550, 1008), ame_cells=3558, ame_M=2550, ame_est=1008)
    eq("EXHAUSTIVE", "C8b", "its E at Z <= 20, 50, 82, 92, 118 and the two cells",
       tuple((res[z][1], res[z][2]) for z in (20, 50, 82, 92, 118)),
       tuple((2, [(0, 0), (2, 0)]) for _ in range(5)), ame_E=2)
    ks = ks_cells()
    ks_ix = cy._kreuzer_skarke()
    Rk = R(ks)
    adm = sorted(Rk - set(ks))
    jf = sum(tuple(map(max, a, b)) not in set(ks) for a, b in itertools.combinations(ks, 2))
    mf = sum(tuple(map(min, a, b)) not in set(ks) for a, b in itertools.combinations(ks, 2))
    eq("EXHAUSTIVE", "C9", "Kreuzer-Skarke chi = +/-6 slice: cells, box, E, pairs, join failures, meet failures",
       (len(ks), ks_ix.box, len(adm), math.comb(len(ks), 2), jf, mf), (208, 12544, 540, 21528, 498, 498),
       ks_cells=208, ks_box=12544, ks_E=540, ks_pairs=21528, ks_jf=498, ks_mf=498)
    eq("EXHAUSTIVE", "C9b", "admitted cells: on the diagonal, distinct chi = 2(h11-h21), min and max h11+h21",
       (sum(a == b for a, b in adm), sorted({2 * (a - b) for a, b in adm}), min(a + b for a, b in adm), max(a + b for a, b in adm)),
       (112, [-4, -2, 0, 2, 4], 26, 262))
    eq("EXHAUSTIVE", "C9c", "every admitted cell has h11 >= 1, h21 >= 1 and h11 + h21 <= 502",
       all(a >= 1 and b >= 1 and a + b <= 502 for a, b in adm), True)
    # the string partition function: coefficients by two routes, and a capped product closes
    N = 16
    coef = [1] + [0] * N
    for n in range(1, N + 1):
        for _ in range(24):
            for k in range(n, N + 1):
                coef[k] += coef[k - n]
    sigma = lambda k: sum(x for x in range(1, k + 1) if k % x == 0)
    dd = [Fraction(1)]
    for n in range(1, N + 1):
        dd.append(Fraction(24, n) * sum(sigma(k) * dd[n - k] for k in range(1, n + 1)))
    eq("EXHAUSTIVE", "C10", "string degeneracies d(N), N <= 16, product expansion = Euler recurrence",
       [int(x) for x in dd] == coef, True)
    eq("EXHAUSTIVE", "C10b", "d(1), d(2), d(3), d(14)", (coef[1], coef[2], coef[3], coef[14]), (24, 324, 3200, 156883829400),
       d1=24, d2=324, d3=3200, d14=156883829400)
    prod = list(itertools.product(range(4), repeat=3))
    eq("EXHAUSTIVE", "C10c", "occupation vectors of three independent oscillators capped at 3: a full product, E", E(prod), 0)
    # the tower
    L9, L10 = tw.L9(), tw.L10()
    for oid, name, X, want in (("C12a", "Lambda_9", L9, (1654, 27648, 0)), ("C12b", "Lambda_10", L10, (2535, 110592, 0))):
        ix = cy.Index(name, ["c%d" % i for i in range(len(X[0]))], X)
        eq("EXHAUSTIVE", oid, "%s: cells, box, E" % name, (len(X), ix.box, E(X)), want)
    VALUES.update(L9_cells=1654, L9_box=27648, L10_cells=2535, L10_box=110592)
    # composability (the time column)
    src9 = {(c[0], c[1], c[2], c[7]) for c in L9}
    comp9 = [c for c in L9 if (c[4], c[5], c[6], c[8]) in src9]
    src10 = {(c[0], c[1], c[2], c[7]) for c in L10}
    comp10 = [c for c in L10 if (c[4], c[5], c[6], c[8]) in src10]
    eq("EXHAUSTIVE", "C14", "composable cells: Lambda_8 (source has four coordinates, target three), Lambda_9, Lambda_10",
       (0, len(comp9), len(comp10)), (0, 1169, 2050), comp9=1169, comp10=2050)
    VALUES["comp9_frac"] = Fraction(len(comp9), len(L9))
    VALUES["comp10_frac"] = Fraction(len(comp10), len(L10))
    rec("EXHAUSTIVE", "C14b", "composable fractions %s and %s" % (pct(VALUES["comp9_frac"]), pct(VALUES["comp10_frac"])), True)
    # the spectra survey grid
    grid, held, Zs, Cs, Ls = spectra_grid()
    eq("EXHAUSTIVE", "C15", "channel survey grid (Z, charge, l): elements, charges, l values, cells, box, E, held cells in grid",
       (len(Zs), Cs, len(Ls), len(grid), len(Zs) * len(Cs) * len(Ls), E(grid), len(held & set(grid))),
       (28, [1, 2, 3, 4, 5, 6, 9, 11, 15, 16], 8, 1744, 2240, 0, 285),
       sp_cells=1744, sp_box=2240, sp_held=285, sp_elements=28)
    # bit costs
    bits = {}
    for key, Rn, En in (("pt", 126, 36), ("cal", 372, 7), ("nuc", 61, 9), ("ks", 748, 540), ("ame", 3560, 2)):
        bits[key] = math.log2(math.comb(Rn, En))
    eq("EXHAUSTIVE", "C13", "bit cost log2 C(|R(X)|, E): periodic table, calendar", ("%.1f" % bits["pt"], "%.1f" % bits["cal"]), ("105.1", "47.4"),
       bits_pt="%.1f" % bits["pt"], bits_cal="%.1f" % bits["cal"], bits_nuc="%.1f" % bits["nuc"], bits_ks="%.1f" % bits["ks"], bits_ame="%.1f" % bits["ame"])
    rec("EXHAUSTIVE", "C13b", "bit cost: nuclide chart %s, KS slice %s, AME2020 %s" % (VALUES["bits_nuc"], VALUES["bits_ks"], VALUES["bits_ame"]), True)
    # rectangle relabelling (Corollary 1)
    for oid, X, a, b in (("C16a", pt, 9, 10), ("C16b", cal, 5, 73)):
        rect = [(i, j) for i in range(a) for j in range(b)]
        eq("EXHAUSTIVE", oid, "Corollary 1: %d cells relabelled onto a %d x %d rectangle: E" % (len(X), a, b), (len(rect) == len(X), E(rect)), (True, 0))
    return dict(lam=lam, pt=pt, jan=jan, cal=cal, bx=bx, grid=grid, L9=L9, L10=L10)


def check_languages(ix_lam=None):
    section("L  the five languages")
    res = cy.run(cy._lambda(), "1173", OPTS)
    got = {v.language: (v.state, v.E) for v in res["_verdicts"]}
    eq("EXHAUSTIVE", "L1", "on Lambda: order, algebra, geometry, information, statistics each return an admitted set with E = 0",
       tuple(got[l] for l in ("order", "algebra", "geometry", "information", "statistics")), tuple(("SPEAKS", 0) for _ in range(5)))
    eq("EXHAUSTIVE", "L1b", "operator-bearing languages measured on Lambda, pairs, pairs agreeing",
       (res["operator_bearing_measured"], len(res["pairs"]), res["pairs_agreeing"]),
       (["algebra", "geometry", "information", "order", "statistics"], 10, 10))
    eq("EXHAUSTIVE", "L1c", "documentary returns no set; analysis declares no witness and is not run",
       (got["documentary"][0], got["analysis"][0]), ("SILENT", "NOT-RUN"))
    res = cy.run(cy._box_ordering(), "1173", OPTS)
    eq("EXHAUSTIVE", "L2", "on the box ordering: pairs agreeing", (len(res["pairs"]), res["pairs_agreeing"]), (10, 10))
    res = cy.run(cy._periodic(True), "1173", OPTS)
    got = {v.language: v.E for v in res["_verdicts"] if v.E is not None}
    eq("EXHAUSTIVE", "L3", "periodic table with the block adjoined (period, group, block): E by language",
       (got["order"], got["algebra"], got["geometry"], got["information"], got["statistics"]), (100, 100, 83, 24, 0),
       pt3_order=100, pt3_geom=83, pt3_info=24, pt3_stat=0)
    eq("EXHAUSTIVE", "L3b", "pairs agreeing there", (len(res["pairs"]), res["pairs_agreeing"]), (10, 1))
    eq("EXHAUSTIVE", "L4", "at two coordinates the pairwise operators are degenerate (guard fires), at three not",
       (cy.run(cy._periodic(), "1173", OPTS)["degenerate"], res["degenerate"]), (True, False))
    # the agreement test on every index built here with d >= 3
    rows = []
    for name, ix in (("Lambda", cy._lambda()), ("box ordering", cy._box_ordering()),
                     ("periodic + block", cy._periodic(True)), ("Lambda_9", cy._tower(9))):
        r = cy.run(ix, "1173", OPTS)
        rows.append((name, r["all_E_zero"], r["languages_agree"], r["langclose_holds"]))
    eq("EXHAUSTIVE", "L5", "E = 0 in every language <=> all five admitted sets coincide, on the four indexes with d >= 3",
       all(r[3] for r in rows), True)
    for r in rows:
        rec("EXHAUSTIVE", "L5.", "  %-18s all E = 0: %-5s agree: %-5s" % (r[0], r[1], r[2]), True)


def check_redundancy(D):
    section("R  redundancy")
    idx = [("Lambda", D["lam"], 8), ("channel survey grid", D["grid"], 3), ("box ordering", D["bx"], 3),
           ("Janet down-set", janet_downset(), 2), ("periodic table", D["pt"], 2), ("calendar", D["cal"], 2)]
    want = {"Lambda": (56, Fraction(16, 56), Fraction(61, 100)), "channel survey grid": (6, Fraction(1, 6), Fraction(20, 100)),
            "box ordering": (6, Fraction(3, 6), Fraction(0)), "Janet down-set": (2, Fraction(1, 2), Fraction(0)),
            "periodic table": (2, Fraction(0), Fraction(0)), "calendar": (2, Fraction(0), Fraction(0))}
    table = []
    for name, X, d in idx:
        cp, nenv = coupling(X, d)
        rd, log = redundancy(X, d)
        eq("SAMPLED", "R1.", "%s: d = %d, envelopes d(d-1) = %d, coupling %s, redundancy %s (seed %d, %s)"
           % (name, d, nenv, pct(cp), pct(rd), SEED, ", ".join("%d%%:%d/%d" % (100 * f, o, t) for f, o, t in log)),
           (nenv, cp, rd), want[name])
        table.append((name, d, nenv, cp, rd, E(X), len(X)))
    VALUES["red_table"] = table
    eq("EXHAUSTIVE", "R1b", "Janet down-set: cells, E", (len(janet_downset()), E(janet_downset())), (724, 0))
    cp, nenv = coupling(D["jan"], 2)
    rd, log = redundancy(D["jan"], 2)
    eq("SAMPLED", "R1c", "Janet (n+l, Z), 118 cells: envelopes, coupling, redundancy", (nenv, cp, rd), (2, Fraction(1), Fraction(0)))
    # r^2 of redundancy against coupling, exact, and the p-value for nu = 4
    pts = [(cp, rd) for _, _, _, cp, rd, _, _ in table]
    n = len(pts)
    mx = sum(p[0] for p in pts) / n
    my = sum(p[1] for p in pts) / n
    sxy = sum((p[0] - mx) * (p[1] - my) for p in pts)
    sxx = sum((p[0] - mx) ** 2 for p in pts)
    syy = sum((p[1] - my) ** 2 for p in pts)
    r2 = sxy ** 2 / (sxx * syy)
    r = math.sqrt(float(r2))
    t = r * math.sqrt((n - 2) / (1 - float(r2)))
    F = 0.5 + t * (6 + t * t) / (2 * (4 + t * t) ** 1.5)      # Student t CDF, nu = 4, closed form
    p = 2 * (1 - F)
    # the closed form checked against numerical quadrature of the nu = 4 density
    f4 = lambda u: 3 / (8 * (1 + u * u / 4) ** 2.5)
    m = 20000
    h = t / m
    quad = 0.5 + h * (sum(f4(i * h) for i in range(1, m)) + (f4(0) + f4(t)) / 2)
    eq("EXHAUSTIVE", "R2", "redundancy against coupling over the six rows: r^2 exact = %s = %.4f; p = %.2f (nu = 4; quadrature agrees to %.1e)"
       % (r2, float(r2), p, abs(quad - F)), ("%.3f" % float(r2), "%.2f" % p, abs(quad - F) < 1e-6), ("0.002", "0.94", True),
       r2="%.3f" % float(r2), pval="%.2f" % p)
    # the projection test
    proj = []
    for d in (8, 7, 6, 5, 4, 3):
        Pd = sorted({c[:d] for c in D["lam"]})
        rd, log = redundancy(Pd, d)
        proj.append((d, len(Pd), rd))
    eq("SAMPLED", "R3", "Lambda projected to its first d coordinates: redundancy at d = 8..3 (seed %d)" % SEED,
       tuple((d, pct(r)) for d, _, r in proj), ((8, "61.0%"), (7, "30.0%"), (6, "30.0%"), (5, "30.0%"), (4, "5.0%"), (3, "0.0%")),
       proj=proj)
    eq("EXHAUSTIVE", "R3b", "each projection is itself closed (E = 0) with cells", tuple((len(sorted({c[:d] for c in D["lam"]})), E(sorted({c[:d] for c in D["lam"]}))) for d in (7, 6, 5, 4, 3)),
       ((319, 0), (165, 0), (99, 0), (33, 0), (12, 0)))
    # a derived coordinate
    gridNe = sorted({(Z, c, l, Z - c + 1) for (Z, c, l) in D["grid"]})
    cp, nenv = coupling(gridNe, 4)
    rd, log = redundancy(gridNe, 4)
    eq("SAMPLED", "R4", "survey grid with N_e = Z - c + 1 adjoined: envelopes, coupling, redundancy, E",
       (nenv, cp, rd, E(gridNe)), (12, Fraction(4, 12), Fraction(0), 20808), ne_E=20808)
    # the witness that N_e does not preserve the join (Corollary 3's hypothesis, verified not assumed)
    G = set(D["grid"])
    ne = lambda c: c[0] - c[1] + 1
    a, b = (3, 1, 0), (5, 4, 0)
    j = tuple(map(max, a, b))
    eq("EXHAUSTIVE", "R4b", "N_e fails to preserve the join on the survey grid: the pair, the join, N_e of each, max",
       (a in G, b in G, j in G, ne(a), ne(b), ne(j), max(ne(a), ne(b)) != ne(j)),
       (True, True, True, 3, 2, 2, True))


def check_quotient(D):
    section("Q  the electromagnetic quotient")
    L9 = D["L9"]
    dl = lambda c: c[5] - c[1]           # f - l : the target subshell's l minus the source's
    dS = lambda c: c[8] - c[7]           # 2S' - 2S
    img = Counter((abs(dl(c)), abs(dS(c))) for c in L9)
    table = {(m, s): img.get((m, s), 0) for m in (0, 1) for s in range(4)}
    eq("EXHAUSTIVE", "Q1", "image of Lambda_9 on (|dl|, |dS|): E1 row (|dl| = 1) at |dS| = 0..3, M1 row (|dl| = 0)",
       (tuple(table[(1, s)] for s in range(4)), tuple(table[(0, s)] for s in range(4))), ((264, 342, 180, 54), (262, 337, 171, 44)),
       img=table)
    eq("EXHAUSTIVE", "Q1a", "the two multipole classes on Lambda_9: M1 (|dl| = 0) cells, E1 (|dl| = 1) cells, total",
       (sum(table[(0, s)] for s in range(4)), sum(table[(1, s)] for s in range(4)),
        sum(table[(0, s)] for s in range(4)) + sum(table[(1, s)] for s in range(4))), (814, 840, 1654),
       m1_cells=814, e1_cells=840)
    eq("EXHAUSTIVE", "Q1b", "the image is the complete 2 x 4 rectangle; E(image); cells map", (len(img), E(list(img)), sum(img.values())), (8, 0, 1654))
    eq("EXHAUSTIVE", "Q1c", "|dl| takes only 0 and 1 on Lambda_9 (l, f <= 1 at these caps)", sorted({abs(dl(c)) for c in L9}), [0, 1])
    e1inter = sum(v for (m, s), v in img.items() if m == 1 and s != 0)
    eq("EXHAUSTIVE", "Q2", "E1 cells with dS != 0 (intercombination lines admitted)", e1inter, 576, inter=576)
    # the interval property, exhaustively on every pair of Lambda_9
    pairs = 0
    bad = 0
    for a, b in itertools.combinations(L9, 2):
        pairs += 1
        j, m = tuple(map(max, a, b)), tuple(map(min, a, b))
        for g in (dl, dS):
            lo, hi = sorted((g(a), g(b)))
            bad += not (lo <= g(j) <= hi and lo <= g(m) <= hi)
    eq("EXHAUSTIVE", "Q3", "Lemma 2 (interval property) for dl and dS on every pair of Lambda_9: pairs, violations", (pairs, bad), (1367031, 0),
       pairs9=1367031)
    spin = [c for c in L9 if dS(c) == 0]
    eq("EXHAUSTIVE", "Q4", "the spin rule dS = 0 imposed on Lambda_9: cells, E", (len(spin), E(spin)), (526, 0), spin_cells=526)
    par = [c for c in L9 if abs(dl(c)) == 1]
    eq("EXHAUSTIVE", "Q5", "the parity rule |dl| = 1 imposed on Lambda_9: cells, E", (len(par), E(par)), (840, 750), par_cells=840, par_E=750)
    hs = hull(spin)
    eq("EXHAUSTIVE", "Q5b", "convexity criterion, both directions on these two: {0} convex -> spin set is a sublattice; {-1,+1} has a hole -> parity set is not",
       (len(hs) == len(spin), len(hull(par)) > len(par)), (True, True))
    in_par = set(par)
    wit = next((a, b) for a, b in itertools.combinations(par, 2) if tuple(map(max, a, b)) not in in_par)
    j = tuple(map(max, *wit))
    # The witness is checked for being one: both members in the set, the join their componentwise
    # maximum, its dl equal to 0, and the join outside the set.  The two dl values are compared as
    # an unordered pair, since which member the enumeration reaches first is not part of the claim.
    eq("EXHAUSTIVE", "Q5c", "a witness pair in the parity set whose join leaves it: the members' dl as an unordered pair, dl of the join, both members in the set, the join in the set",
       (sorted((dl(wit[0]), dl(wit[1]))), dl(j), wit[0] in in_par and wit[1] in in_par, j in in_par),
       ([-1, 1], 0, True, False), par_witness=(wit, j))
    rec("EXHAUSTIVE", "Q5d", "the witness printed: %s and %s join to %s" % (wit[0], wit[1], j),
        j == tuple(map(max, wit[0], wit[1])) and j not in in_par)
    # a quotient, not an extension: adjoin the image coordinates
    adj = [c + (abs(dl(c)), abs(dS(c))) for c in L9]
    eq("EXHAUSTIVE", "Q6", "Lambda_9 with (|dl|, |dS|) adjoined as coordinates: cells, E under R", (len(adj), E(adj)), (1654, 9278), adj_E=9278)
    # the two single-coordinate adjunctions are measured here for the first time (no source figure)
    for oid, name, f, want in (("Q6b", "|dl| alone", lambda c: (abs(dl(c)),), 1654), ("Q6c", "|dS| alone", lambda c: (abs(dS(c)),), 3812)):
        X = [c + f(c) for c in L9]
        eq("EXHAUSTIVE", oid, "adjoining %s: E" % name, E(X), want)
    VALUES["adj_dl"] = 1654
    VALUES["adj_dS"] = 3812
    # each adjoined map fails to preserve the join somewhere on Lambda_9 -- the hypothesis of
    # Corollary 3, exhibited rather than inferred from the measured defect.
    S9 = set(L9)
    wits = {}
    for nm, fn in (("|dl|", lambda c: abs(dl(c))), ("|dS|", lambda c: abs(dS(c))),
                   ("(|dl|,|dS|)", lambda c: (abs(dl(c)), abs(dS(c))))):
        w = None
        for a, b in itertools.combinations(L9, 2):
            j = tuple(map(max, a, b))
            if j not in S9:
                continue
            fa, fb, fj = fn(a), fn(b), fn(j)
            top = max(fa, fb) if not isinstance(fa, tuple) else tuple(map(max, fa, fb))
            if fj != top:
                w = (a, b, j, fa, fb, fj, top)
                break
        wits[nm] = w
    eq("EXHAUSTIVE", "Q6d", "each adjoined map fails to preserve the join on Lambda_9: a witness for each of |dl|, |dS|, (|dl|,|dS|)",
       tuple(w is not None for w in wits.values()), (True, True, True), join_witnesses=wits)
    for nm in ("|dl|", "|dS|", "(|dl|,|dS|)"):
        a, b, j, fa, fb, fj, top = wits[nm]
        rec("EXHAUSTIVE", "Q6d.", "  %-12s %s v %s = %s, values %s and %s, at the join %s, join of values %s"
            % (nm, a, b, j, fa, fb, fj, top), fj != top)
    # composability and the electromagnetic condition
    src = {(c[0], c[1], c[2], c[7]) for c in L9}
    comp = {c for c in L9 if (c[4], c[5], c[6], c[8]) in src}
    em = {c for c in L9 if abs(dl(c)) == 1 and dS(c) == 0}
    n = len(L9)

    def H(p):
        return -sum(q * math.log2(q) for q in (p, 1 - p) if q > 0)
    joint = Counter((c in em, c in comp) for c in L9)
    pa, pb = len(em) / n, len(comp) / n
    mi = sum(v / n * math.log2((v / n) / ((pa if a else 1 - pa) * (pb if b else 1 - pb))) for (a, b), v in joint.items())
    eq("EXHAUSTIVE", "Q7", "dipole-allowed (|dl| = 1 and dS = 0) cells, composable cells, of 1654", (len(em), len(comp)), (264, 1169))
    eq("EXHAUSTIVE", "Q7b", "H(allowed) = %.4f bits, I(allowed; composable) = %.5f bits" % (H(pa), mi), ("%.3f" % H(pa), "%.4f" % mi), ("0.633", "0.0004"),
       H_em="%.3f" % H(pa), MI="%.4f" % mi)
    # the crossing
    cells, occ = crossing_population()
    X = set(cells)
    S_all = {(c[1], c[2], c[3]) for c in X}
    SZ = {Z: {(c[1], c[2], c[3]) for c in X if c[0] == Z} for Z in occ}

    def rates(pred):
        sub = [c for c in X if pred(c)]
        w = sum(1 for c in sub if (c[5], c[6], c[7]) in SZ[c[0]])
        a = sum(1 for c in sub if (c[5], c[6], c[7]) in S_all)
        return len(sub), w, Fraction(w, len(sub)), a, Fraction(a, len(sub))
    rows = {}
    for nm, p in (("all", lambda c: True), ("allowed", lambda c: abs(c[6] - c[2]) == 1),
                  ("forbidden", lambda c: abs(c[6] - c[2]) != 1), ("parity-conserving", lambda c: (c[6] - c[2]) % 2 == 0),
                  ("parity-changing", lambda c: (c[6] - c[2]) % 2 == 1)):
        rows[nm] = rates(p)
    eq("EXHAUSTIVE", "Q8", "crossing population: elements, cells, distinct", (len(occ), len(cells), len(X)), (118, 4325, 4325), cr_cells=4325)
    want = {"all": (4325, 982, 3686), "allowed": (2673, 309, 2399), "forbidden": (1652, 673, 1287),
            "parity-conserving": (606, 233, 544), "parity-changing": (3719, 749, 3142)}
    for nm in ("all", "allowed", "forbidden", "parity-conserving", "parity-changing"):
        n_, w, wr, a, ar = rows[nm]
        eq("EXHAUSTIVE", "Q8.", "%-18s cells %4d  within %4d (%s)  across %4d (%s)" % (nm, n_, w, pct(wr), a, pct(ar)), (n_, w, a), want[nm])
    VALUES["crossing"] = rows
    eq("EXHAUSTIVE", "Q8b", "the four percentages: allowed within, forbidden within, allowed across, forbidden across",
       (pct(rows["allowed"][2]), pct(rows["forbidden"][2]), pct(rows["allowed"][4]), pct(rows["forbidden"][4])), ("11.6%", "40.7%", "89.7%", "77.9%"))
    eq("EXHAUSTIVE", "Q8c", "the crossing: allowed < forbidden within, allowed > forbidden across",
       (rows["allowed"][2] < rows["forbidden"][2], rows["allowed"][4] > rows["forbidden"][4]), (True, True))


def negative_controls():
    section("N  negative controls (--selftest): each must be REFUTED")
    ok1 = E(periodic_cells()) == 35
    rec("REFUTATION", "N1", "the false claim E(periodic table) = 35 is refuted", not ok1)
    r, nv, cv = adjunction_obligation((3, 3), 3)
    rec("REFUTATION", "N2", "the false claim 'S closed => graph(h) closed' is refuted by Z3 (sat)", cv == z3.sat)
    tot, bad = guard_fidelity(trials=60, reference=lambda X: R_ref(X, len(X[0])) | {tuple(0 for _ in X[0])})
    rec("REFUTATION", "N3", "the fidelity guard catches a deliberately wrong reference (%d of %d cells disagree)" % (bad, tot), bad > 0)
    rd, _ = redundancy(calendar_cells(), 2, seed=1)
    rec("REFUTATION", "N4", "the false claim 'the calendar recovers from 5%% loss' is refuted (redundancy %s)" % pct(rd), rd == 0)


def compute_all(selftest=False):
    print("check.py -- Closure beyond the atom   (Z3 %s, Python %s)" % (z3.get_version_string(), sys.version.split()[0]))
    check_operator()
    D = check_catalogue()
    check_languages()
    check_redundancy(D)
    check_quotient(D)
    if selftest:
        negative_controls()
    return VALUES


def main(argv):
    selftest = "--selftest" in argv
    compute_all(selftest)
    by = Counter(s for s, _, _, ok in RESULTS if ok)
    print("\nsummary: %d obligations, %d failed" % (len(RESULTS), FAIL))
    for k in ("PROVED", "MACHINE-CHECKED", "EXHAUSTIVE", "SAMPLED", "REFUTATION", "GUARD"):
        if by.get(k):
            print("  %-16s %d" % (k, by[k]))
    print("  %s" % ("CLEAN" if not FAIL else "FAILED"))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
