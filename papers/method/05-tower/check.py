#!/usr/bin/env python3
"""check.py — the machine checks behind "The tower over Λ" (paper 05).

Every number the paper prints is produced here, and every decidable claim it makes is decided
here.  The object under test is the seated tower instrument, imported by path and never copied;
the reference implementations used by the guards are written fresh in this file.

    python3 check.py              one line per obligation, a summary, exit 1 on any failure
    python3 check.py --selftest   the guards plus the negative controls (false claims that must
                                  be reported as refuted)

Python 3.12, numpy, z3-solver.  ~5 minutes (the branch and bound at Λ_10 is most of it).
"""
import argparse, collections, importlib.util, itertools, os, random, sys, time
from fractions import Fraction

import numpy as np
import z3

ROOT = "/home/user/Claude-Method-Works"
PATHS = {
    "tower":    ROOT + "/method/members/tower-2.py",       # the six stages (the object under test)
    "cgraph":   ROOT + "/method/proofs/cgraph.py",         # the constraint-graph instrument
    "coupling": ROOT + "/method/proofs/coupling.py",       # the triangle-region instrument
    "prover":   ROOT + "/research/warp-drive/prover.py",   # the Z3 harness (finite-box form)
}


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


T = load("tower2", PATHS["tower"])
PROVER = load("prover", PATHS["prover"])
COORDS = ["n", "ℓ", "k", "q", "e", "f", "g", "2S", "2S′", "v", "2J_c", "2K", "2J"]
STAGES = (8, 9, 10, 11, 12, 13)
B_SIDE = {4, 5, 6, 8, 9}            # e f g 2S′ v — the target caterpillar
Q = 3                               # the transfer

# ----------------------------------------------------------------------------- reporting
RESULTS = []          # (status, name, ok, detail)
DATA = {}             # every figure the paper prints, by key; figures.py reads this


def ob(status, name, ok, detail=""):
    RESULTS.append((status, name, bool(ok), detail))
    print("  [%s] %-16s %-62s %s" % ("ok" if ok else "XX", status, name, detail))
    return bool(ok)


def section(title):
    print("\n" + title + "\n" + "-" * len(title))


# ----------------------------------------------------------------------------- the stages
def stages():
    if "L" not in DATA:
        DATA["L"] = {d: T.STAGES[d]() for d in STAGES}
    return DATA["L"]


def pairwise_closure(cells):
    """Exhaustive: every unordered pair, meet and join tested for membership.  numpy, chunked."""
    A = np.array(cells, dtype=np.int64)
    n, d = A.shape
    A = A - A.min(0)
    shape = A.max(0) + 1
    radix = np.cumprod(np.concatenate([[1], shape[:-1]]))
    member = np.zeros(int(np.prod(shape)), dtype=bool)
    member[(A * radix).sum(1)] = True
    bad_meet = bad_join = 0
    pairs = 0
    for i in range(n - 1):
        Y = A[i + 1:]
        m = np.minimum(A[i], Y)
        j = np.maximum(A[i], Y)
        bad_meet += int((~member[(m * radix).sum(1)]).sum())
        bad_join += int((~member[(j * radix).sum(1)]).sum())
        pairs += Y.shape[0]
    return pairs, bad_meet, bad_join


def staircase_sweep(cells):
    """|ℛ(X)| by a sweep of the whole ambient box (own alphabets), in numpy.
    ℛ(X) = {x in Box : x_i <= φ_ij(x_j) for all i != j}, φ_ij(a) = max{y_i : y in X, y_j <= a}.
    Returns (|ℛ(X)|, |Box|)."""
    C = np.array(cells)
    d = C.shape[1]
    alph = [sorted(set(C[:, i].tolist())) for i in range(d)]
    code = [{v: r for r, v in enumerate(a)} for a in alph]
    shape = tuple(len(a) for a in alph)
    enc = np.array([[code[i][v] for i, v in enumerate(c)] for c in cells])
    mask = np.ones(shape, dtype=bool)
    for i in range(d):
        for j in range(d):
            if i == j:
                continue
            allowed = np.zeros((shape[i], shape[j]), dtype=bool)
            for a in range(shape[j]):
                cand = enc[enc[:, j] <= a][:, i]
                if len(cand):
                    allowed[:cand.max() + 1, a] = True
            if i > j:
                allowed = allowed.T
            sh = [1] * d
            sh[i], sh[j] = shape[i], shape[j]
            mask &= allowed.reshape(sh)
    return int(mask.sum()), int(np.prod(shape))


def stair_py(G, box):
    """An independent, pure-Python staircase over a FIXED box: the reference for the seed guard."""
    d = len(box)
    ph = {}
    for i in range(d):
        for j in range(d):
            if i == j:
                continue
            for a in box[j]:
                cand = [y[i] for y in G if y[j] <= a]
                ph[(i, j, a)] = max(cand) if cand else None
    out = set()
    for x in itertools.product(*box):
        if all(ph[(i, j, x[j])] is not None and x[i] <= ph[(i, j, x[j])]
               for i in range(d) for j in range(d) if i != j):
            out.add(x)
    return out


def check_stages():
    section("§2  THE SIX STAGES — counts, projections, closure")
    L = stages()
    want = {8: 976, 9: 1654, 10: 2535, 11: 13585, 12: 70905, 13: 199130}
    DATA["counts"] = {d: len(L[d]) for d in STAGES}
    ob("EXHAUSTIVE", "stage counts from the tower instrument", DATA["counts"] == want,
       " ".join("%d" % len(L[d]) for d in STAGES))
    # duplicates and the coordinate order
    ob("EXHAUSTIVE", "no stage lists a cell twice", all(len(set(L[d])) == len(L[d]) for d in STAGES))
    # exact projection
    proj = all(set(c[:-1] for c in L[d]) == set(L[d - 1]) for d in STAGES[1:])
    ob("EXHAUSTIVE", "each stage projects exactly onto the one below", proj,
       "π(Λ_D+1) = Λ_D for D = 8..12")
    # ambient boxes and fill
    box = {}
    fill = {}
    for d in STAGES:
        r, b = staircase_sweep(L[d])
        box[d] = b
        fill[d] = Fraction(len(L[d]), b)
        DATA.setdefault("R", {})[d] = r
    DATA["box"] = box
    DATA["fill"] = fill
    ob("EXHAUSTIVE", "ambient boxes", [box[d] for d in STAGES] ==
       [6912, 27648, 110592, 663552, 5308416, 47775744], " ".join("%d" % box[d] for d in STAGES))
    fill_pct = ["%.2f" % (100 * float(fill[d])) for d in STAGES]
    ob("EXHAUSTIVE", "fill |Λ|/|Box| in per cent", fill_pct ==
       ["14.12", "5.98", "2.29", "2.05", "1.34", "0.42"], " ".join(fill_pct))
    ob("EXHAUSTIVE", "fill falls strictly at every stage",
       all(fill[a] > fill[b] for a, b in zip(STAGES, STAGES[1:])))
    # closure by the sweep: ℛ(X) = X at every stage
    ob("EXHAUSTIVE", "ℛ(Λ_D) = Λ_D at all six stages (ambient sweep)",
       all(DATA["R"][d] == len(L[d]) for d in STAGES),
       "swept " + " ".join("%d" % box[d] for d in STAGES) + " cells")
    # closure by pairs at the stages where pairs are countable in minutes
    DATA["pairs"] = {}
    for d in (8, 9, 10, 11):
        t0 = time.time()
        p, bm, bj = pairwise_closure(L[d])
        DATA["pairs"][d] = p
        ob("EXHAUSTIVE", "Λ_%d closed under meet and join, every pair" % d, bm == 0 and bj == 0,
           "%d pairs, %d meet / %d join failures, %.0fs" % (p, bm, bj, time.time() - t0))
    for d in (12, 13):
        n = len(L[d])
        DATA["pairs"][d] = n * (n - 1) // 2
    ob("EXHAUSTIVE", "pair counts at Λ_12 and Λ_13 (not pair-tested; the sweep decides them)",
       DATA["pairs"][12] == 70905 * 70904 // 2 == 2513724060 and DATA["pairs"][13] == 199130 * 199129 // 2 == 19826278885,
       "%d and %d" % (DATA["pairs"][12], DATA["pairs"][13]))
    tested = sum(DATA["pairs"][d] for d in (8, 9, 10, 11))
    ob("EXHAUSTIVE", "pairs tested at the first four stages sum to 97,323,996", tested == 97323996, "%d" % tested)
    # the ratios the paper's prose states
    grow = Fraction(len(L[13]), len(L[8]))
    boxgrow = Fraction(box[13], box[8])
    ratio13 = Fraction(DATA["pairs"][13], box[13])
    DATA["ratios"] = dict(grow=grow, boxgrow=boxgrow, sweep_vs_pairs=ratio13)
    ob("EXHAUSTIVE", "the object grows ×204 and its box ×6,912 across the tower; pairs/box = 415 at the top",
       round(grow) == 204 and boxgrow == 6912 and round(ratio13) == 415,
       "%.1f, %d, %.1f" % (float(grow), boxgrow, float(ratio13)))
    upper = sum(len(L[d]) for d in STAGES[1:])
    ob("EXHAUSTIVE", "cells across the five upper stages, 287,809; C(13, 3) = 286 vertex triples",
       upper == 287809 and 13 * 12 * 11 // 6 == 286, "%d; %d" % (upper, 13 * 12 * 11 // 6))


# ----------------------------------------------------------------------------- rank, Birkhoff, chains
def rank(c):
    return sum(c)


def check_rank_and_chains():
    section("§7  RANK, GENERATORS AND MAXIMAL CHAINS OF Λ_8")
    L = stages()
    prof = {}
    for d in STAGES:
        r = collections.Counter(rank(c) for c in L[d])
        mx = max(r.values())
        prof[d] = (len(r), min(r), max(r), mx, sorted(k for k, v in r.items() if v == mx))
    DATA["rank_profile"] = prof
    ob("EXHAUSTIVE", "rank values per stage (coordinate sum)",
       [prof[d][0] for d in STAGES] == [18, 21, 24, 29, 36, 44] and all(prof[d][1] == 3 for d in STAGES),
       " ".join("%d" % prof[d][0] for d in STAGES) + "; bottom rank 3 at every stage")
    ob("EXHAUSTIVE", "widest rank level of Λ_8 and Λ_9", prof[8][3:] == (122, [11]) and prof[9][3:] == (185, [12]),
       "122 at 11; 185 at 12")
    ob("EXHAUSTIVE", "|Λ_8| = 8 × its widest level", len(L[8]) == 8 * 122)
    seq8 = [collections.Counter(rank(c) for c in L[8])[r] for r in range(3, 21)]
    ob("EXHAUSTIVE", "rank sequence of Λ_8 is log-concave",
       all(seq8[i] ** 2 >= seq8[i - 1] * seq8[i + 1] for i in range(1, len(seq8) - 1)))
    DATA["rankseq8"] = seq8

    X = set(L[8])
    bot, top = min(L[8]), max(L[8])
    d = 8
    # join-irreducibles: exactly one lower cover in Λ_8 under unit steps
    def lower_covers(c):
        return [c[:i] + (c[i] - 1,) + c[i + 1:] for i in range(d) if c[i] > 0 and (c[:i] + (c[i] - 1,) + c[i + 1:]) in X]
    # generator form: min{x in Λ : x_c >= v}
    mins = [min(c[i] for c in L[8]) for i in range(d)]
    alph = [sorted(set(c[i] for c in L[8])) for i in range(d)]
    gens = {}
    for i in range(d):
        for v in alph[i]:
            if v == mins[i]:
                continue
            S = [c for c in L[8] if c[i] >= v]
            m = tuple(min(c[t] for c in S) for t in range(d))
            gens[(i, v)] = m if m in X else None
    ob("EXHAUSTIVE", "every generator min{x : x_c ≥ v} is a cell", all(g is not None for g in gens.values()),
       "Σ(|A_i| − 1) = %d" % len(gens))
    # ji count via 'number of generators below x' = rank - 3, and generators = the join-irreducibles
    le = lambda a, b: all(x <= y for x, y in zip(a, b))
    G = sorted(set(gens.values()))
    ji = [c for c in L[8] if c != bot and len(lower_covers(c)) == 1]
    ob("EXHAUSTIVE", "the 17 join-irreducibles are the 17 generators", len(ji) == 17 and set(ji) == set(G))
    below_ok = all(sum(1 for g in G if le(g, c)) == rank(c) - rank(bot) for c in L[8])
    ob("EXHAUSTIVE", "#{generators ≤ x} = rank(x) − 3 for every cell (Λ_8 is graded by the sum)", below_ok)
    cov = sum(1 for a in G for b in G if a != b and le(a, b) and not any(c != a and c != b and le(a, c) and le(c, b) for c in G))
    ob("EXHAUSTIVE", "covering relations of the generator poset P", cov == 20, "%d" % cov)
    order = sorted(range(len(G)), key=lambda i: rank(G[i]))
    P = [G[i] for i in order]
    idx = {p: i for i, p in enumerate(P)}
    below = [[idx[a] for a in P if a != b and le(a, b)] for b in P]

    def count_downsets(i, chosen):
        if i == len(P):
            return 1
        t = count_downsets(i + 1, chosen)
        if all(chosen[j] for j in below[i]):
            chosen[i] = True
            t += count_downsets(i + 1, chosen)
            chosen[i] = False
        return t
    nd = count_downsets(0, [False] * len(P))
    ob("EXHAUSTIVE", "down-sets of P number |Λ_8| (Birkhoff)", nd == 976, "%d" % nd)
    DATA["generators"] = P
    # maximal chains by dynamic programming over unit steps
    chains = {bot: 1}
    for c in sorted(L[8], key=rank):
        if c == bot:
            continue
        chains[c] = sum(chains[p] for p in lower_covers(c))
    DATA["maxchains"] = chains[top]
    ob("EXHAUSTIVE", "maximal chains of Λ_8 = linear extensions of P (DP over covers)",
       chains[top] == 1113045672, "%d, bottom %s top %s" % (chains[top], bot, top))
    ob("EXHAUSTIVE", "every maximal chain has length 17 = rank(top) − rank(bot)", rank(top) - rank(bot) == 17)
    cmin = tuple(min(c[i] for c in L[8]) for i in range(8))
    cmax = tuple(max(c[i] for c in L[8]) for i in range(8))
    ob("EXHAUSTIVE", "the coordinatewise extremes of Λ_8 are cells, so bottom and top are these",
       cmin in X and cmax in X and (cmin, cmax) == (bot, top) and (rank(cmin), rank(cmax)) == (3, 20),
       "%s at rank 3, %s at rank 20" % (cmin, cmax))
    ob("EXHAUSTIVE", "the rank sequence of Λ_8, ranks 3..20",
       seq8 == [1, 5, 15, 34, 59, 87, 108, 121, 122, 115, 100, 79, 57, 37, 21, 10, 4, 1] and sum(seq8) == 976,
       " ".join(map(str, seq8)))
    ob("EXHAUSTIVE", "the alphabet sizes of Λ_8 sum to 25 and Σ(|A_i| − 1) = 17",
       [len(a) for a in alph] == [3, 2, 3, 4, 3, 2, 4, 4] and sum(len(a) for a in alph) == 25,
       str([len(a) for a in alph]))


# ----------------------------------------------------------------------------- the cylinder
def sections_of(cells):
    A = collections.defaultdict(set)
    B = collections.defaultdict(set)
    for c in cells:
        q = c[Q]
        A[q].add(tuple(v for i, v in enumerate(c) if i not in B_SIDE and i != Q))
        B[q].add(tuple(v for i, v in enumerate(c) if i in B_SIDE))
    return [(q, len(A[q]), len(B[q])) for q in sorted(A)]


def check_cylinder():
    section("§6  THE CYLINDER OVER THE TRANSFER — sections, the tight bridge, orientation")
    L = stages()
    secs = {d: sections_of(L[d]) for d in STAGES}
    DATA["sections"] = secs
    ob("EXHAUSTIVE", "Λ_8 sections A(q) × B(q)", [(a, b) for q, a, b in secs[8]] == [(33, 5), (33, 10), (23, 15), (8, 17)],
       str(secs[8]))
    ob("EXHAUSTIVE", "Λ_11 sections", [(a, b) for q, a, b in secs[11]] == [(163, 5), (163, 20), (123, 50), (48, 70)],
       str([a * b for q, a, b in secs[11]]))
    ob("EXHAUSTIVE", "Λ_13 sections", [(a, b) for q, a, b in secs[13]] == [(2294, 5), (2294, 20), (1794, 50), (744, 70)],
       str([a * b for q, a, b in secs[13]]))
    ob("EXHAUSTIVE", "Σ_q |A(q)|·|B(q)| = |Λ| at every stage (defect 0)",
       all(sum(a * b for q, a, b in secs[d]) == len(L[d]) for d in STAGES))
    ob("EXHAUSTIVE", "A(q) non-increasing and B(q) non-decreasing at every stage",
       all(all(x[1] >= y[1] and x[2] <= y[2] for x, y in zip(secs[d], secs[d][1:])) for d in STAGES))
    ob("EXHAUSTIVE", "the section sequence is log-concave and peaks at q = 2, every stage",
       all(all((s[i][1] * s[i][2]) ** 2 >= (s[i - 1][1] * s[i - 1][2]) * (s[i + 1][1] * s[i + 1][2]) for i in (1, 2))
           and max(range(4), key=lambda i: s[i][1] * s[i][2]) == 2 for s in secs.values()))
    qm = {d: Fraction(sum(q * a * b for q, a, b in secs[d]), len(L[d])) for d in STAGES}
    DATA["qmean"] = qm
    ob("EXHAUSTIVE", "mean transfer ⟨q⟩ at all six stages: 1.4631 1.6850 1.8304 1.8874 1.9141 1.9159",
       ["%.4f" % float(qm[d]) for d in STAGES] == ["1.4631", "1.6850", "1.8304", "1.8874", "1.9141", "1.9159"],
       " ".join("%.4f" % float(qm[d]) for d in STAGES))
    # the (exact-product) fibre check per section: Λ restricted to q IS the product
    for d in (8, 13):
        Lq = collections.defaultdict(set)
        for c in L[d]:
            Lq[c[Q]].add(c)
        ok = True
        for q in Lq:
            A = {tuple(v for i, v in enumerate(c) if i not in B_SIDE and i != Q) for c in Lq[q]}
            B = {tuple(v for i, v in enumerate(c) if i in B_SIDE) for c in Lq[q]}
            ok &= len(Lq[q]) == len(A) * len(B)
        ob("EXHAUSTIVE", "Λ_%d ∩ {q} = A(q) × B(q) as a set, every q" % d, ok)

    # the tight two-parent K: 2K <= 2J_c + 2f with the cell's own f (upper bound only)
    L11 = L[11]
    L12u = [c + (K,) for c in L11 for K in range(0, c[10] + 2 * c[5] + 1)]
    L13u = [c + (J,) for c in L12u for J in range(max(0, c[11] - 1), c[11] + 2)]
    s12, s13 = sections_of(L12u), sections_of(L13u)
    p12, p13 = sum(a * b for q, a, b in s12), sum(a * b for q, a, b in s13)
    DATA["tightK"] = dict(n12=len(L12u), p12=p12, n13=len(L13u), p13=p13)
    ob("EXHAUSTIVE", "tight K (cell's f): cells and factorisation defect at stage 12",
       len(L12u) == 55755 and p12 - len(L12u) == 15150 and p12 == 70905,
       "%d cells, product %d, defect %d = %.1f%%" % (len(L12u), p12, p12 - len(L12u), 100 * (p12 - len(L12u)) / p12))
    ob("EXHAUSTIVE", "tight K: cells and defect at stage 13",
       len(L13u) == 153680 and p13 - len(L13u) == 45450 and p13 == 199130,
       "%d cells, product %d, defect %d = %.1f%%" % (len(L13u), p13, p13 - len(L13u), 100 * (p13 - len(L13u)) / p13))
    r12u, _ = staircase_sweep(L12u)
    DATA["tightK"]["E12"] = r12u - len(L12u)
    ob("REFUTATION", "tight K at stage 12 is not closed either: ℛ-defect E = |ℛ(X)| − |X|",
       r12u - len(L12u) == 12675, "E = %d" % (r12u - len(L12u)))
    # the exact triangle at axis 12: |2J_c − 2f| <= 2K <= 2J_c + 2f, 2K ≡ 2J_c (mod 2)
    L12t = [c + (K,) for c in L11 for K in range(0, c[10] + 2 * c[5] + 1)
            if abs(c[10] - 2 * c[5]) <= K and (K - c[10]) % 2 == 0]
    r12t, _ = staircase_sweep(L12t)
    L13t = [c + (J,) for c in L12t for J in range(max(0, c[11] - 1), c[11] + 2)]
    DATA["triangle12"] = dict(n=len(L12t), R=r12t, E=r12t - len(L12t), n13=len(L13t))
    ob("EXHAUSTIVE", "exact triangle at axis 12: cells, ℛ-defect, and stage 13 above it",
       len(L12t) == 22275 and r12t - len(L12t) == 35570 and len(L13t) == 64290,
       "%d cells, |ℛ| = %d, E = %d; %d cells at 13" % (len(L12t), r12t, r12t - len(L12t), len(L13t)))
    t0 = time.time()
    p, bm, bj = pairwise_closure(L12t)
    DATA["triangle12"].update(pairs=p, meet_fail=bm, join_fail=bj)
    ob("REFUTATION", "the exact-triangle stage 12 is not closed: 52,767,450 failing meets and 28,742,850 failing joins among 248,076,675 pairs",
       (p, bm, bj) == (248076675, 52767450, 28742850),
       "%d pairs, %d meet failures, %d join failures, %.0fs" % (p, bm, bj, time.time() - t0))
    X12t = set(L12t)
    wit = None
    for a in L12t:
        if (a[10], a[5], a[11]) == (4, 0, 4):
            for b in L12t:
                if (b[10], b[5], b[11]) == (2, 1, 0):
                    m = tuple(map(min, a, b))
                    if m not in X12t:
                        wit = (a, b, m)
                        break
            break
    DATA["triangle12"]["witness"] = wit
    ob("REFUTATION", "a meet witness inside the exact-triangle stage 12", wit is not None,
       "%s ∧ %s = %s ∉ X" % wit if wit else "none")

    # a difference of two coordinates is not a lattice homomorphism on Λ_8: witness
    X8 = L[8]
    h = lambda c: c[4] - c[3]            # e − q, a difference of two coordinates
    w = None
    for a in X8:
        for b in X8:
            j = tuple(map(max, a, b))
            if h(j) != max(h(a), h(b)):
                w = (a, b, j)
                break
        if w:
            break
    DATA["diffwitness"] = w
    ob("REFUTATION", "a difference of coordinates is not join-preserving on Λ_8 (witness)", w is not None,
       "h = e − q: h(%s ∨ %s) = %d ≠ max(%d, %d)" % (w[0], w[1], h(w[2]), h(w[0]), h(w[1])) if w else "")


# ----------------------------------------------------------------------------- the constraint graph
EDGES = {   # (parent, child): the child's bound has the parent as its one argument.  Transcribed by hand
            # from D10 (the instrument's own stage constructors name their parents); it is an independent
            # TRANSCRIPTION, not a derivation, and check_graph() compares it with the imported graph
            # instrument's own list.
    8:  [("n", "ℓ"), ("ℓ", "k"), ("k", "q"), ("e", "f"), ("f", "g"), ("q", "g"), ("k", "2S")],
    9:  [("g", "2S′")],
    10: [("2S′", "v"), ("g", "v")],
    11: [("k", "2J_c")],
    12: [("2J_c", "2K")],           # 2K ≤ 2J_c + 2·f_max: f_max is a cap, so one parent
    13: [("2K", "2J")],
}
NAMEMAP = {"l": "ℓ", "2S'": "2S′", "2Jc": "2J_c"}


def graph_rows(two_parent=False):
    cg = load("cgraph", PATHS["cgraph"])
    saved = list(cg.EDGES_BY_STAGE[12])
    if not two_parent:
        cg.EDGES_BY_STAGE[12] = [("2Jc", "2K")]
    rows = []
    for s in STAGES:
        V, E, adj = cg.graph(s)
        c = cg.components(V, adj)
        tr = cg.triangles(V, adj)
        rows.append(dict(stage=s, nodes=len(V), edges=len(E), comps=c, rank=len(E) - len(V) + c,
                         tris=len(tr), tri=tr, girth=cg.girth(V, adj), tw=cg.treewidth(V, adj),
                         E={tuple(NAMEMAP.get(x, x) for x in e) for e in E},
                         deg={NAMEMAP.get(v, v): len(adj[v]) for v in V}))
    cg.EDGES_BY_STAGE[12] = saved
    return rows


def check_graph():
    section("§5  THE CONSTRAINT GRAPH — vertices, edges, cycle rank, treewidth")
    rows = graph_rows()
    DATA["graph"] = rows
    mine = {}
    acc = set()
    for s in STAGES:
        acc |= set(EDGES[s])
        mine[s] = set(acc)
    ob("EXHAUSTIVE", "the instrument's edge list (one-parent K) equals this file's derivation",
       all(rows[i]["E"] == mine[s] for i, s in enumerate(STAGES)))
    ob("EXHAUSTIVE", "vertices per stage", [r["nodes"] for r in rows] == [8, 9, 10, 11, 12, 13])
    ob("EXHAUSTIVE", "edges per stage", [r["edges"] for r in rows] == [7, 8, 10, 11, 12, 13],
       " ".join(str(r["edges"]) for r in rows))
    ob("EXHAUSTIVE", "connected at every stage", all(r["comps"] == 1 for r in rows))
    ob("EXHAUSTIVE", "cycle rank per stage", [r["rank"] for r in rows] == [0, 0, 1, 1, 1, 1],
       str(tuple(r["rank"] for r in rows)))
    ob("EXHAUSTIVE", "triangles per stage, the one triangle being 2S′–g–v",
       [r["tris"] for r in rows] == [0, 0, 1, 1, 1, 1] and all(sorted(r["tri"][0]) == ["2S'", "g", "v"] for r in rows[2:]))
    ob("EXHAUSTIVE", "treewidth per stage (exact elimination search)", [r["tw"] for r in rows] == [1, 1, 2, 2, 2, 2],
       str(tuple(r["tw"] for r in rows)))
    ob("EXHAUSTIVE", "girth 3 from stage 10, none below", [r["girth"] for r in rows] == [None, None, 3, 3, 3, 3])
    ob("EXHAUSTIVE", "degrees at stage 13: k and g at 4, leaves n e 2S 2J",
       rows[-1]["deg"]["k"] == 4 and rows[-1]["deg"]["g"] == 4 and all(rows[-1]["deg"][v] == 1 for v in ("n", "e", "2S", "2J")))
    # q is a cut vertex separating the A side from the B side at every stage
    ok = True
    for i, s in enumerate(STAGES):
        adj = collections.defaultdict(set)
        for a, b in rows[i]["E"]:
            if "q" in (a, b):
                continue
            adj[a].add(b)
            adj[b].add(a)
        Bn = {COORDS[t] for t in B_SIDE if t < s}
        seen, stack = set(), ["e"]
        while stack:
            x = stack.pop()
            if x in seen:
                continue
            seen.add(x)
            stack += list(adj[x])
        ok &= seen == Bn
    ob("EXHAUSTIVE", "q is a cut vertex: deleting it leaves the B side {e f g 2S′ v} as one component", ok)
    # and exactly two components, so the rest is the parent block in one piece
    two_comp = True
    no_cross = True
    for i, s in enumerate(STAGES):
        V = {v for e in rows[i]["E"] for v in e} - {"q"}
        adj = collections.defaultdict(set)
        for a, b in rows[i]["E"]:
            if "q" in (a, b):
                continue
            adj[a].add(b)
            adj[b].add(a)
        seen, comps = set(), 0
        for v in sorted(V):
            if v in seen:
                continue
            comps += 1
            stack = [v]
            while stack:
                x = stack.pop()
                if x in seen:
                    continue
                seen.add(x)
                stack += list(adj[x])
        two_comp &= comps == 2
        Bn = {COORDS[t] for t in B_SIDE if t < s}
        no_cross &= not any(({a, b} & Bn) and ({a, b} - Bn - {"q"}) and "q" not in (a, b)
                            for a, b in rows[i]["E"])
    ob("EXHAUSTIVE", "no edge joins the parent block to the target block, at any stage", no_cross)
    ob("EXHAUSTIVE", "deleting q leaves exactly two components at every stage", two_comp)
    two = graph_rows(two_parent=True)
    DATA["graph_two_parent"] = two
    moved = sorted(v for v in two[-1]["deg"] if two[-1]["deg"][v] != rows[-1]["deg"][v])
    ob("EXHAUSTIVE", "the two-parent reading (cell's own f): 14 edges, cycle rank (0,0,1,1,2,2); triangles, treewidth, girth, hub degrees unchanged; only f and 2K move",
       two[-1]["edges"] == 14 and [r["rank"] for r in two] == [0, 0, 1, 1, 2, 2]
       and [r["tris"] for r in two] == [r["tris"] for r in rows] and [r["tw"] for r in two] == [r["tw"] for r in rows]
       and [r["girth"] for r in two] == [r["girth"] for r in rows]
       and (two[-1]["deg"]["k"], two[-1]["deg"]["g"]) == (4, 4) and moved == ["2K", "f"],
       "%d edges, cycle rank %s, degrees moved: %s" % (two[-1]["edges"], tuple(r["rank"] for r in two), moved))


# ----------------------------------------------------------------------------- the bracket system
def check_brackets():
    section("§8  THE BRACKET SYSTEM r(Λ_13) → … → r(Λ_8)")
    L = stages()
    br = {}
    branching = {}
    for d in STAGES[1:]:
        fib = collections.defaultdict(set)
        for c in L[d]:
            fib[rank(c)].add(rank(c[:-1]))
        rs = sorted(fib)
        gap = all(len(fib[r]) == max(fib[r]) - min(fib[r]) + 1 for r in rs)
        mono = all(min(fib[a]) <= min(fib[b]) and max(fib[a]) <= max(fib[b]) for a, b in zip(rs, rs[1:]))
        br[d] = {r: (min(fib[r]), max(fib[r])) for r in rs}
        branching[d] = max(len(fib[r]) for r in rs)
        ob("EXHAUSTIVE", "stage bracket Λ_%d → Λ_%d: gap-free interval, monotone endpoints" % (d, d - 1), gap and mono,
           "%d cells, branching %d" % (len(L[d]), branching[d]))
    DATA["brackets"] = br
    DATA["branching"] = branching
    ob("EXHAUSTIVE", "branching 4, 4, 6, 8, 9 grows with height", [branching[d] for d in STAGES[1:]] == [4, 4, 6, 8, 9])
    direct = collections.defaultdict(set)
    for c in L[13]:
        direct[rank(c)].add(rank(c[:8]))
    slack_lo = slack_hi = 0
    contained = True
    composed_image = set()
    for r in sorted(direct):
        lo = hi = r
        for d in (13, 12, 11, 10, 9):
            los = [br[d][x][0] for x in range(lo, hi + 1) if x in br[d]]
            his = [br[d][x][1] for x in range(lo, hi + 1) if x in br[d]]
            lo, hi = min(los), max(his)
        dl, dh = min(direct[r]), max(direct[r])
        contained &= lo <= dl and hi >= dh
        slack_lo = max(slack_lo, dl - lo)
        slack_hi = max(slack_hi, hi - dh)
        composed_image |= set(range(lo, hi + 1))
    DATA["slack"] = (slack_lo, slack_hi)
    ob("EXHAUSTIVE", "the composed bracket contains the direct bracket at every rank of Λ_13", contained)
    ob("EXHAUSTIVE", "slack of composition ≤ 2 rank units", max(slack_lo, slack_hi) <= 2,
       "lower end %d, upper end %d" % (slack_lo, slack_hi))
    ranks8 = set(range(3, 21))
    ob("EXHAUSTIVE", "χ(Λ_8) = {3..20} is covered from the top by both routes",
       set().union(*direct.values()) == ranks8 and composed_image == ranks8)
    ob("EXHAUSTIVE", "the direct bracket is itself gap-free at every rank",
       all(len(direct[r]) == max(direct[r]) - min(direct[r]) + 1 for r in direct))


# ----------------------------------------------------------------------------- the physics bounds
def terms(l, k):
    """LS terms (2S, 2L) of the configuration ℓ^k by microstate enumeration: the standard
    stripping of complete (2S, 2L) blocks from the (2M_L, 2M_S) census."""
    orbs = [(ml, ms) for ml in range(-l, l + 1) for ms in (-1, 1)]
    cnt = collections.Counter()
    for combo in itertools.combinations(orbs, k):
        cnt[(2 * sum(ml for ml, ms in combo), sum(ms for ml, ms in combo))] += 1
    out = []
    while cnt:
        ML, MS = max(cnt)
        out.append((MS, ML))
        for ml in range(-ML, ML + 1, 2):
            for ms in range(-MS, MS + 1, 2):
                cnt[(ml, ms)] -= 1
                if cnt[(ml, ms)] == 0:
                    del cnt[(ml, ms)]
    return sorted(out)


def check_physics_bounds():
    section("§3  THE BOUNDS OF THE COUPLING AXES, from microstate enumeration")
    p = {k: terms(1, k) for k in range(1, 7)}
    s = {k: terms(0, k) for k in (1, 2)}
    ob("EXHAUSTIVE", "terms of p^1, p^2, p^3", p[1] == [(1, 2)] and p[2] == [(0, 0), (0, 4), (2, 2)] and p[3] == [(1, 2), (1, 4), (3, 0)])
    max2J = {k: max(S2 + L2 for S2, L2 in p[k]) for k in p}
    max2S_p = {k: max(S2 for S2, L2 in p[k]) for k in p}
    max2S_s = {k: max(S2 for S2, L2 in s[k]) for k in s}
    DATA["max2J_p"] = max2J
    DATA["max2S_p"] = max2S_p
    DATA["max2S_s"] = max2S_s
    ob("EXHAUSTIVE", "φ̂(k) = max 2J over ℓ ≤ 1 at k = 1, 2, 3 equals the instrument's cap table",
       {k: max2J[k] for k in (1, 2, 3)} == T.PHI and T.PHI == {1: 3, 2: 4, 3: 5}, str(T.PHI))
    mu = {(l, k): max(S2 + L2 for S2, L2 in terms(l, k)) for l in (0, 1) for k in range(1, 4 * l + 3)}
    phihat = {k: max(mu[(l, kk)] for l in (0, 1) for kk in range(1, k + 1) if kk <= 4 * l + 2) for k in (1, 2, 3)}
    ob("EXHAUSTIVE", "φ̂(k) := max{μ(ℓ, k′) : ℓ ≤ 1, k′ ≤ k}, the running maximum of D12, equals {1:3, 2:4, 3:5}",
       phihat == T.PHI and all(phihat[a] <= phihat[b] for a, b in ((1, 2), (2, 3))), str(phihat))
    ob("EXHAUSTIVE", "μ(0, 1) = 1 and μ(0, 2) = 0 (the s shell)", (mu[(0, 1)], mu[(0, 2)]) == (1, 0), "%d, %d" % (mu[(0, 1)], mu[(0, 2)]))
    ob("EXHAUSTIVE", "the exact core bound is not monotone in k beyond the caps: max 2J(p^k), k = 1..6",
       [max2J[k] for k in range(1, 7)] == [3, 4, 5, 4, 3, 0], str([max2J[k] for k in range(1, 7)]))
    ob("EXHAUSTIVE", "the exact spin bound is not monotone: max 2S(s^k) = 1, 0; max 2S(p^k) = 1,2,3,2,1,0",
       [max2S_s[1], max2S_s[2]] == [1, 0] and [max2S_p[k] for k in range(1, 7)] == [1, 2, 3, 2, 1, 0])
    ob("EXHAUSTIVE", "particle–hole symmetry: terms(p^k) = terms(p^(6−k))", all(p[k] == p[6 - k] for k in (1, 2)))
    ob("EXHAUSTIVE", "min(g, 4f+2−g) reproduces max 2S of f^g for f = 0, 1",
       all(min(g, 4 * f + 2 - g) == max(S2 for S2, L2 in terms(f, g)) for f in (0, 1) for g in range(1, 4 * f + 3)))
    ob("EXHAUSTIVE", "the instrument's f_max = 1 and 2K ranges over 0..2J_c + 2", T.FMAX == 1 and
       all(max(c[11] for c in stages()[12] if c[10] == jc) == jc + 2 for jc in range(6)))


# ----------------------------------------------------------------------------- the envelope gap
def spin_set(f, g):
    """The 2S values terms(f^g) carries — the exact fibre of axis 9."""
    return {S2 for S2, L2 in terms(f, g)} if g else {0}


def new_at(f, v, S2):
    """Is a term of spin 2S' NEW at occupancy v — present in terms(f^v) and not carried up from
    terms(f^(v-2))?  That is Racah's seniority, read as a multiset difference."""
    a = collections.Counter(terms(f, v)) if v else collections.Counter({(0, 0): 1})
    if v >= 2:
        a.subtract(collections.Counter(terms(f, v - 2)))
    return any(S == S2 and c > 0 for (S, L), c in a.items())


def senior_set(c):
    """The exact fibre of axis 10 at a cell c of Λ_9: the seniorities v at which a term of the cell's own
    spin 2S′ is NEW in f^v, on the ladder 2S′ ≤ v ≤ g, v ≡ g (mod 2), and under the conjugate ceiling
    v ≤ 4f + 2 − g (a seniority-v term of f^g exists only up to the mirror occupancy 4f + 2 − v)."""
    f, g, S2 = c[5], c[6], c[8]
    return {v for v in range(S2, g + 1) if v <= 4 * f + 2 - g and v % 2 == g % 2 and new_at(f, v, S2)}


def core_J(l, k, S2):
    """The 2J values of the terms of l^k that carry the cell's own multiplicity 2S."""
    out = set()
    for S, L2 in terms(l, k):
        if S == S2:
            out |= set(range(abs(L2 - S), L2 + S + 1, 2))
    return out


def check_envelope_gap():
    section("§3  THE ENVELOPE GAP — the exact fibre against the admissible one, axis by axis")
    L = stages()
    rows = {}
    # axis 9: 2S' in [0, g] against the spin set of f^g
    ok9 = all(spin_set(f, g) == {S for S, _ in terms(f, g)} for f in (0, 1) for g in range(1, 4 * f + 3))
    e9 = sum(len(spin_set(c[5], c[6])) for c in L[8])
    rows[9] = (e9, len(L[9]))
    # axis 10: v in [2S', g] against the seniorities at which the cell's own 2S' is new
    e10 = sum(len(senior_set(c)) for c in L[9])
    rows[10] = (e10, len(L[10]))
    # axis 11, two readings
    mu = {(l, k): max(S + L2 for S, L2 in terms(l, k)) for l in (0, 1) for k in range(1, 4 * l + 3)}
    e11w = sum(mu[(c[1], c[2])] + 1 for c in L[10])
    e11s = sum(len(core_J(c[1], c[2], c[7])) for c in L[10])
    rows[11] = (e11s, len(L[11]))
    # axis 12: the exact triangle with the cell's own f and the parity congruence
    e12 = sum(1 for c in L[11] for K in range(0, c[10] + 2 * c[5] + 1)
              if abs(c[10] - 2 * c[5]) <= K and (K - c[10]) % 2 == 0)
    rows[12] = (e12, len(L[12]))
    # axis 13: 2J = 2K +/- 1 exactly, so the fibre is a doublet except at 2K = 0
    n0 = sum(1 for c in L[12] if c[11] == 0)
    e13 = 2 * len(L[12]) - n0
    rows[13] = (e13, len(L[13]))
    DATA["envelope_gap"] = dict(rows=rows, e11_wide=e11w, K0=n0, ok9=ok9)
    pct = lambda a, b: "%.1f" % (100.0 * a / b)
    ob("EXHAUSTIVE", "the exact fibre equals the microstate spin set at axis 9", ok9)
    ob("EXHAUSTIVE", "axis 9: exact 1,054 of 1,654 admitted = 63.7 %",
       rows[9] == (1054, 1654) and pct(*rows[9]) == "63.7", "%d / %d" % rows[9])
    ob("EXHAUSTIVE", "axis 10: exact 1,132 of 2,535 = 44.7 %",
       rows[10] == (1132, 2535) and pct(*rows[10]) == "44.7", "%d / %d" % rows[10])
    ob("EXHAUSTIVE", "axis 11: exact 2,310 of 13,585 = 17.0 % (terms at the cell's own 2S)",
       rows[11] == (2310, 13585) and pct(*rows[11]) == "17.0", "%d / %d" % rows[11])
    ob("EXHAUSTIVE", "axis 11, the wider reading: 10,585 of 13,585 = 77.9 % (largest 2J of any term)",
       e11w == 10585 and pct(e11w, 13585) == "77.9", "%d / 13585" % e11w)
    ob("EXHAUSTIVE", "axis 12: exact 22,275 of 70,905 = 31.4 % (the triangle with the cell's own f)",
       rows[12] == (22275, 70905) and pct(*rows[12]) == "31.4", "%d / %d" % rows[12])
    ob("EXHAUSTIVE", "axis 13: exact 128,225 of 199,130 = 64.4 %; the fibre is a doublet but at 2K = 0",
       rows[13] == (128225, 199130) and pct(*rows[13]) == "64.4" and n0 == 13585,
       "%d / %d, %d cells at 2K = 0" % (rows[13] + (n0,)))
    ob("EXHAUSTIVE", "the exact fibre is never larger than the admissible one, at any axis",
       all(a <= b for a, b in rows.values()))
    # the monotone envelope of a non-monotone realised maximum
    m = [max(S + L2 for S, L2 in terms(1, k)) for k in range(1, 7)]
    env, run = [], -1
    for x in m:
        run = max(run, x)
        env.append(run)
    DATA["mu_envelope"] = (m, env)
    ob("EXHAUSTIVE", "max 2J over p^k is not monotone; its monotone envelope is 3 4 5 5 5 5",
       m == [3, 4, 5, 4, 3, 0] and env == [3, 4, 5, 5, 5, 5] and all(e >= x for e, x in zip(env, m))
       and sum(1 for e, x in zip(env, m) if e > x) == 3,
       "realised %s, envelope %s, strict at k = 4, 5, 6" % (m, env))


# ----------------------------------------------------------------------------- the envelope family
def exact_fibres():
    """The exact fibre at each axis as a function of the cell of the stage below, with the parent
    indices (j, j′) of the construction's own bound there.  11s / 11w are the two readings of axis 11;
    13t is the constant-side triangle at axis 13 (before the parity congruence)."""
    mu = {(l, k): max(S + L2 for S, L2 in terms(l, k)) for l in (0, 1) for k in range(1, 4 * l + 3)}
    return {
        9:     (lambda c: spin_set(c[5], c[6]), 6, 6),
        10:    (senior_set, 8, 6),
        "11s": (lambda c: core_J(c[1], c[2], c[7]), 2, 2),
        "11w": (lambda c: set(range(0, mu[(c[1], c[2])] + 1)), 2, 2),
        12:    (lambda c: {K for K in range(0, c[10] + 2 * c[5] + 1) if abs(c[10] - 2 * c[5]) <= K and (K - c[10]) % 2 == 0}, 10, 10),
        13:    (lambda c: {J for J in (c[11] - 1, c[11] + 1) if J >= 0}, 11, 11),
        "13t": (lambda c: set(range(abs(c[11] - 1), c[11] + 2)), 11, 11),
    }


D10_INTERVAL = {   # the construction's own interval at each axis, as a function of the cell below
    9:  lambda c: (0, c[6]),
    10: lambda c: (c[8], c[6]),
    11: lambda c: (0, T.PHI[c[2]]),
    12: lambda c: (0, c[10] + 2 * T.FMAX),
    13: lambda c: (max(0, c[11] - 1), c[11] + 1),
}


def check_envelope_family():
    section("§3.1 / §4  THE ENVELOPE FAMILY — the least envelope at each axis, and the exact thirteenth stage")
    L = stages()
    fam = exact_fibres()
    below = {9: 8, 10: 9, "11s": 10, "11w": 10, 12: 11, 13: 12, "13t": 12}
    want = {9: (1638, 1654, 0), 10: (2535, 2535, 600), "11s": (12425, 13585, 1305), "11w": (13585, 13585, 0),
            12: (60320, 70905, 0), 13: (199130, 199130, 0), "13t": (199130, 199130, 0)}
    DATA["least"] = {}
    for ax in (9, 10, "11s", "11w", 12, 13, "13t"):
        F, j, jp = fam[ax]
        S = L[below[ax]]
        axn = int(str(ax)[:2])
        Fx = {x: F(x) for x in S}
        NE = [x for x in S if Fx[x]]
        Aj = sorted({x[j] for x in S})
        Ajp = sorted({x[jp] for x in S})
        lo = {a: min(min(Fx[x]) for x in NE if x[j] >= a) for a in Aj}
        hi = {b: max(max(Fx[x]) for x in NE if x[jp] <= b) for b in Ajp}
        mono = all(lo[a] <= lo[b] for a, b in zip(Aj, Aj[1:])) and all(hi[a] <= hi[b] for a, b in zip(Ajp, Ajp[1:]))
        nonempty = all(lo[x[j]] <= hi[x[jp]] for x in S)                       # every fibre of the envelope non-empty
        contains = all(all(lo[x[j]] <= y <= hi[x[jp]] for y in Fx[x]) for x in S)
        d10 = D10_INTERVAL[axn]
        member = all(all(d10(x)[0] <= y <= d10(x)[1] for y in Fx[x]) for x in S)  # D10's interval is in the family
        inside = all(d10(x)[0] <= lo[x[j]] and hi[x[jp]] <= d10(x)[1] for x in S)  # and contains the least member
        n = sum(hi[x[jp]] - lo[x[j]] + 1 for x in S)
        ex = sum(len(Fx[x]) for x in S)
        adm = sum(d10(x)[1] - d10(x)[0] + 1 for x in S)
        DATA["least"][ax] = dict(lo=lo, hi=hi, least=n, exact=ex, admitted=adm, empty=len(S) - len(NE))
        ob("EXHAUSTIVE", "axis %s: least envelope over (%s, %s) admits %d; the construction's bound admits %d; %d empty exact fibres"
           % (ax, COORDS[j], COORDS[jp], n, adm, len(S) - len(NE)),
           mono and nonempty and contains and member and inside and (n, adm, len(S) - len(NE)) == want[ax] and adm == len(L[axn]),
           "l⋆ = %s, h⋆ = %s" % ([lo[a] for a in Aj], [hi[b] for b in Ajp]))
    Ld = DATA["least"]
    ob("EXHAUSTIVE", "the construction's bound is the least envelope at axes 10, 11 (wider) and 13, and a larger member at 9, 11 (strict) and 12",
       all(Ld[a]["least"] == Ld[a]["admitted"] for a in (10, "11w", 13, "13t")) and all(Ld[a]["least"] < Ld[a]["admitted"] for a in (9, "11s", 12)),
       "1,654 − 1,638 = %d; 13,585 − 12,425 = %d; 70,905 − 60,320 = %d" % (1654 - Ld[9]["least"], 13585 - Ld["11s"]["least"], 70905 - Ld[12]["least"]))
    ob("EXHAUSTIVE", "the 16 cells of Λ_8 with g = 3 are where the axis-9 least envelope drops the value 0 (2S′ ≡ g mod 2)",
       sum(1 for c in L[8] if c[6] == 3) == 16 and Ld[9]["lo"][3] == 1 and 1654 - Ld[9]["least"] == 16)
    ob("EXHAUSTIVE", "the exact fibre is strictly smaller than the least envelope at every axis (so no exact set is of Theorem 5(i)'s shape)",
       all(Ld[a]["exact"] < Ld[a]["least"] for a in (9, 10, "11s", "11w", 12, 13)),
       " ".join("%d<%d" % (Ld[a]["exact"], Ld[a]["least"]) for a in (9, 10, "11s", "11w", 12, 13)))
    ob("EXHAUSTIVE", "every spin in the spin set of f^g has the parity of g: 2S′ ≡ g (mod 2), for f = 0, 1 and every g the caps admit",
       all(S2 % 2 == g % 2 for f in (0, 1) for g in range(0, 4 * f + 3) for S2 in spin_set(f, g)))
    # the exact thirteenth stage, two readings, against the band
    F13, F13t = fam[13][0], fam["13t"][0]
    L13d = [c + (J,) for c in L[12] for J in sorted(F13(c))]
    L13t = [c + (J,) for c in L[12] for J in sorted(F13t(c))]
    band = {c + (J,) for c in L[12] for J in range(max(0, c[11] - 1), c[11] + 2)}
    ob("EXHAUSTIVE", "the band |2J − 2K| ≤ 1, 2J ≥ 0 over Λ_12 IS Λ_13 as a set, and is the least envelope of the doublet",
       band == set(L[13]) and len(band) == 199130 and Ld[13]["least"] == 199130
       and all(Ld[13]["lo"][a] == max(0, a - 1) and Ld[13]["hi"][a] == a + 1 for a in Ld[13]["lo"]))
    n0 = sum(1 for c in L[12] if c[11] == 0)
    n1 = sum(1 for c in L[12] if c[11] >= 1)
    ob("EXHAUSTIVE", "the exact doublet 2J = 2K ± 1 gives 128,225 cells; the constant-side triangle 185,545; the band 199,130",
       (len(L13d), len(L13t), len(band)) == (128225, 185545, 199130))
    ob("EXHAUSTIVE", "the band's excess over the doublet is 70,905 = one value (2K) per cell: 57,320 by the congruence at 2K ≥ 1 and 13,585 at 2K = 0",
       len(band) - len(L13d) == 70905 == n0 + n1 and n1 == 57320 and n0 == 13585
       and len(L13t) - len(L13d) == n1 and len(band) - len(L13t) == n0, "%d + %d" % (n1, n0))
    base = (1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0)
    a, b = base + (0, 1), base + (1, 0)
    m = tuple(map(min, a, b))
    Sd, St = set(L13d), set(L13t)
    ob("REFUTATION", "neither exact thirteenth stage is meet-closed: (…,2K=0,2J=1) ∧ (…,2K=1,2J=0) = (…,0,0) leaves both",
       a in Sd and b in Sd and m not in Sd and a in St and b in St and m not in St, "%s ∧ %s = %s" % (a, b, m))
    t0 = time.time()
    rd, _ = staircase_sweep(L13d)
    rt, _ = staircase_sweep(L13t)
    DATA["exact13"] = dict(doublet=len(L13d), triangle=len(L13t), Ed=rd - len(L13d), Et=rt - len(L13t))
    ob("REFUTATION", "their staircase defects: E = 70,905 (doublet) and E = 13,585 (triangle); ℛ of each is the band, 199,130",
       (rd, rt) == (199130, 199130) and rd - len(L13d) == 70905 and rt - len(L13t) == 13585,
       "|ℛ| = %d, %d; %.0fs" % (rd, rt, time.time() - t0))
    # Theorem 5(iii)'s envelope, on alphabets {0..M}: l⋆(a) = max(0, a − k), h⋆(a) = a + k, for every k ≤ 6, M ≥ k
    ok = True
    cases = 0
    for k in range(0, 7):
        for M in range(k, 11):
            A = list(range(M + 1))
            F = {a: set(range(abs(a - k), a + k + 1)) for a in A}
            lo = {a: min(min(F[b]) for b in A if b >= a) for a in A}
            hi = {a: max(max(F[b]) for b in A if b <= a) for a in A}
            ok &= all(lo[a] == max(0, a - k) and hi[a] == a + k for a in A)
            ok &= all(set(range(lo[a], hi[a] + 1)) == {y for y in range(0, a + k + 1) if abs(y - a) <= k} for a in A)
            ok &= (k == 0) or any(len(F[a]) < hi[a] - lo[a] + 1 for a in A)      # strictly larger for k ≥ 1
            cases += 1
    ob("EXHAUSTIVE", "Theorem 5(iii): the least envelope of {|a − k| ≤ y ≤ a + k} on {0..M} is the band B_k, strictly larger for k ≥ 1",
       ok, "%d (k, M) cases, k ≤ 6, k ≤ M ≤ 10" % cases)


# ----------------------------------------------------------------------------- Z3, over the integers
def z3_prove(formula):
    s = z3.Solver()
    s.add(z3.Not(formula))
    return s.check()


def z3_sat(formula):
    s = z3.Solver()
    s.add(formula)
    r = s.check()
    return r, (s.model() if r == z3.sat else None)


def Abs(x):
    return z3.If(x >= 0, x, -x)


def Max(a, b):
    return z3.If(a >= b, a, b)


def Min(a, b):
    return z3.If(a <= b, a, b)


def counting_axis_formula():
    """Theorem 1 over the integers, with the two parent indices j and j′ allowed to differ.  Two cells:
    the lower bound's parent takes the values x1, x2 and the upper bound's parent u1, u2; (l1, h1) and
    (l2, h2) are the values at those points of ONE pair of monotone functions (lo, hi) — monotonicity
    is the only thing assumed of them, and is stated at the points that occur.  y_i in [l_i, h_i].
    Then the join (max x, max u, max y) and the meet (min x, min u, min y) satisfy the bounds at the
    joined and at the met parent values."""
    x1, x2, u1, u2, y1, y2, l1, l2, h1, h2 = z3.Ints("x1 x2 u1 u2 y1 y2 l1 l2 h1 h2")
    mono = z3.And(z3.Implies(x1 <= x2, l1 <= l2), z3.Implies(x2 <= x1, l2 <= l1),
                  z3.Implies(u1 <= u2, h1 <= h2), z3.Implies(u2 <= u1, h2 <= h1))
    hyp = z3.And(mono, l1 <= y1, y1 <= h1, l2 <= y2, y2 <= h2)
    lJ, hJ = z3.If(x1 >= x2, l1, l2), z3.If(u1 >= u2, h1, h2)      # lo at max(x1, x2), hi at max(u1, u2)
    lM, hM = z3.If(x1 <= x2, l1, l2), z3.If(u1 <= u2, h1, h2)      # lo at min(x1, x2), hi at min(u1, u2)
    concl = z3.And(lJ <= Max(y1, y2), Max(y1, y2) <= hJ, lM <= Min(y1, y2), Min(y1, y2) <= hM)
    return hyp, concl, (x1, x2, u1, u2, y1, y2, l1, l2, h1, h2)


def py_counting_axis(vals):
    """The same statement in ordinary arithmetic: the reference the fidelity guard compares against."""
    x1, x2, u1, u2, y1, y2, l1, l2, h1, h2 = vals
    mono = ((x1 > x2 or l1 <= l2) and (x2 > x1 or l2 <= l1) and (u1 > u2 or h1 <= h2) and (u2 > u1 or h2 <= h1))
    hyp = mono and l1 <= y1 <= h1 and l2 <= y2 <= h2
    lJ, hJ = (l1 if x1 >= x2 else l2), (h1 if u1 >= u2 else h2)
    lM, hM = (l1 if x1 <= x2 else l2), (h1 if u1 <= u2 else h2)
    concl = lJ <= max(y1, y2) <= hJ and lM <= min(y1, y2) <= hM
    return hyp, concl


def z3_eval(f, subst):
    """Evaluate a Z3 formula at concrete integers: substitute, simplify, read off the Boolean."""
    r = z3.simplify(z3.substitute(f, *[(v, z3.IntVal(int(n))) for v, n in subst]))
    if z3.is_true(r):
        return True
    if z3.is_false(r):
        return False
    raise ValueError("the formula did not reduce to a constant: %s" % r)


def triangle_formulas():
    a1, b1, c1, a2, b2, c2 = z3.Ints("a1 b1 c1 a2 b2 c2")
    inT = lambda a, b, c: z3.And(a >= 0, b >= 0, c >= 0, Abs(a - b) <= c, c <= a + b)
    hyp = z3.And(inT(a1, b1, c1), inT(a2, b2, c2))
    join = inT(Max(a1, a2), Max(b1, b2), Max(c1, c2))
    meet = inT(Min(a1, a2), Min(b1, b2), Min(c1, c2))
    return hyp, join, meet, (a1, b1, c1, a2, b2, c2)


def band_formulas():
    k, a1, b1, a2, b2 = z3.Ints("k a1 b1 a2 b2")
    inB = lambda a, b: z3.And(a >= 0, b >= 0, Abs(a - b) <= k)
    hyp = z3.And(k >= 0, inB(a1, b1), inB(a2, b2))
    join = inB(Max(a1, a2), Max(b1, b2))
    meet = inB(Min(a1, a2), Min(b1, b2))
    return hyp, join, meet, (k, a1, b1, a2, b2)


def cband_formulas():
    a1, b1, c1, a2, b2, c2 = z3.Ints("a1 b1 c1 a2 b2 c2")
    inC = lambda a, b, c: z3.And(a >= 0, b >= 0, c >= 0, Abs(a - b) <= c)
    hyp = z3.And(inC(a1, b1, c1), inC(a2, b2, c2))
    join = inC(Max(a1, a2), Max(b1, b2), Max(c1, c2))
    meet = inC(Min(a1, a2), Min(b1, b2), Min(c1, c2))
    return hyp, join, meet, (a1, b1, c1, a2, b2, c2)


def cst_formulas():
    """Theorem 5(iii): the triangle with one side the constant k, {x ≥ 0, y ≥ 0, |x − k| ≤ y ≤ x + k}."""
    k, x1, y1, x2, y2 = z3.Ints("k x1 y1 x2 y2")
    inS = lambda x, y: z3.And(x >= 0, y >= 0, Abs(x - k) <= y, y <= x + k)
    hyp = z3.And(k >= 1, inS(x1, y1), inS(x2, y2))
    join = inS(Max(x1, x2), Max(y1, y2))
    meet = inS(Min(x1, x2), Min(y1, y2))
    return hyp, join, meet, (k, x1, y1, x2, y2)


def counting_box_claim(X, S, cells, d, shape):
    """Theorem 1 in the finite-box form of the harness: for EVERY closed S in the box and EVERY
    monotone h with values in 0..2, the extension {(x, y) : x in S, y <= h(x_0)} is closed."""
    h = [z3.Int("h_%d" % a) for a in range(shape[0])]
    mono = z3.And([h[a] <= h[a + 1] for a in range(shape[0] - 1)] + [z3.And(h[a] >= -1, h[a] <= 2) for a in range(shape[0])])
    ext = lambda c, y: z3.And(S[c], y <= h[c[0]])
    cl = []
    ext_cells = [(c, y) for c in cells for y in range(3)]
    for (a, ya) in ext_cells:
        for (b, yb) in ext_cells:
            pre = z3.And(ext(a, ya), ext(b, yb))
            cl.append(z3.Implies(pre, z3.And(ext(PROVER.meet(a, b), min(ya, yb)), ext(PROVER.join(a, b), max(ya, yb)))))
    return z3.Implies(z3.And(PROVER.closed(S, cells), mono), z3.And(cl))


# concrete reference implementations for the fidelity guards ------------------------------------
def brute_closure_failures(cells):
    X = set(cells)
    m = j = 0
    for a, b in itertools.combinations(sorted(X), 2):
        m += tuple(map(min, a, b)) not in X
        j += tuple(map(max, a, b)) not in X
    return m, j


def guard_encoding(seed=5):
    """The Z3 predicates evaluated in Python must agree, cell by cell, with the concrete sets; and the
    counting-axis extension over random monotone bounds on random sublattices must be closed by the
    independent brute-force test, while a non-monotone bound must be caught."""
    rnd = random.Random(seed)
    ok = True
    # (1) region predicates vs. set membership, on every cell of a cap box
    inT = lambda a, b, c: abs(a - b) <= c <= a + b
    inC = lambda a, b, c: abs(a - b) <= c
    cap = 6
    T6 = {(a, b, c) for a in range(cap + 1) for b in range(cap + 1) for c in range(cap + 1) if inT(a, b, c)}
    coupling = load("coupling", PATHS["coupling"])
    ref = {(S, L, J) for (S, L, J) in coupling.triangle(cap)}          # its convention: (2S, 2L, 2J)
    T6_as_ref = {(b, a, c) for (a, b, c) in T6}                        # our (a, b) = (2L, 2S)
    same = T6_as_ref == ref
    m6, j6 = brute_closure_failures(T6)
    mref, jref = coupling.failures(coupling.triangle(cap))
    ok &= same and (m6, j6) == (mref, jref) == (2862, 0)
    print("  [%s] guard: triangle region at cap 6 equals the instrument's; failures %d meet / %d join (instrument %d / %d)"
          % ("ok" if same and (m6, j6) == (mref, jref) else "XX", m6, j6, mref, jref))
    C8 = {(a, b, c) for a in range(9) for b in range(9) for c in range(9) if inC(a, b, c)}
    m8, j8 = brute_closure_failures(C8)
    ok &= (m8, j8) == (12654, 0)
    print("  [%s] guard: |a−b| ≤ c at cap 8: %d meet / %d join failures by brute force" % ("ok" if (m8, j8) == (12654, 0) else "XX", m8, j8))
    for k in (0, 1, 2, 3):
        Bk = {(a, b) for a in range(8) for b in range(8) if abs(a - b) <= k}
        mk, jk = brute_closure_failures(Bk)
        ok &= (mk, jk) == (0, 0)
    print("  [%s] guard: B_k at cap 7, k = 0..3: closed by brute force" % ("ok" if ok else "XX"))
    inS = lambda k, x, y: abs(x - k) <= y <= x + k
    cst_ok = True
    cst_counts = {}
    for k in (1, 2, 3):
        Sk = {(x, y) for x in range(8) for y in range(11) if inS(k, x, y)}
        mk, jk = brute_closure_failures(Sk)
        cst_counts[k] = (mk, jk)
        cst_ok &= mk > 0 and jk == 0 and (0, k) in Sk and (k, 0) in Sk and (0, 0) not in Sk
    ok &= cst_ok
    print("  [%s] guard: the constant-side triangle {|x−k| ≤ y ≤ x+k} at cap 7, k = 1..3: join-closed and not meet-closed by brute force %s"
          % ("ok" if cst_ok else "XX", cst_counts))
    # (2) the Z3 predicates THEMSELVES, evaluated at concrete integers and compared, cell by cell and
    #     pair by pair, with the lambdas above: a wrong Abs, Max, Min or If would show here.
    dis = 0
    evals = 0
    hyp, join, meet, v = triangle_formulas()
    box6 = [(a, b, c) for a in range(7) for b in range(7) for c in range(7)]
    for u, w in [(u, u) for u in box6] + [(rnd.choice(box6), rnd.choice(box6)) for _ in range(400)]:
        sub = list(zip(v, u + w))
        dis += z3_eval(hyp, sub) != (inT(*u) and inT(*w))
        dis += z3_eval(join, sub) != inT(*map(max, u, w))
        dis += z3_eval(meet, sub) != inT(*map(min, u, w))
        evals += 3
    hyp, join, meet, v = cband_formulas()
    box8 = [(a, b, c) for a in range(9) for b in range(9) for c in range(9)]
    for u, w in [(u, u) for u in box8] + [(rnd.choice(box8), rnd.choice(box8)) for _ in range(300)]:
        sub = list(zip(v, u + w))
        dis += z3_eval(hyp, sub) != (inC(*u) and inC(*w))
        dis += z3_eval(join, sub) != inC(*map(max, u, w))
        dis += z3_eval(meet, sub) != inC(*map(min, u, w))
        evals += 3
    hyp, join, meet, v = band_formulas()
    box7 = [(a, b) for a in range(8) for b in range(8)]
    for k in (0, 1, 2, 3):
        inBk = lambda a, b: abs(a - b) <= k
        for u, w in [(u, u) for u in box7] + [(rnd.choice(box7), rnd.choice(box7)) for _ in range(100)]:
            sub = list(zip(v, (k,) + u + w))
            dis += z3_eval(hyp, sub) != (inBk(*u) and inBk(*w))
            dis += z3_eval(join, sub) != inBk(*map(max, u, w))
            dis += z3_eval(meet, sub) != inBk(*map(min, u, w))
            evals += 3
    hyp, join, meet, v = cst_formulas()
    box = [(x, y) for x in range(8) for y in range(11)]
    for k in (1, 2, 3):
        for u, w in [(u, u) for u in box] + [(rnd.choice(box), rnd.choice(box)) for _ in range(100)]:
            sub = list(zip(v, (k,) + u + w))
            dis += z3_eval(hyp, sub) != (inS(k, *u) and inS(k, *w))
            dis += z3_eval(join, sub) != inS(k, *map(max, u, w))
            dis += z3_eval(meet, sub) != inS(k, *map(min, u, w))
            evals += 3
    hyp, concl, v = counting_axis_formula()
    seen_true = 0
    for _ in range(600):
        vals = [rnd.randint(-2, 4) for _ in v]
        ph, pc = py_counting_axis(vals)
        sub = list(zip(v, vals))
        dis += z3_eval(hyp, sub) != ph
        dis += z3_eval(concl, sub) != pc
        seen_true += ph
        evals += 2
    print("  [%s] guard: the Z3 predicates (triangle, |a−b| ≤ c, B_k, the constant-side triangle, Theorem 1's hypothesis and conclusion) evaluated at concrete integers agree with the independent implementations: %d evaluations, %d disagreements; Theorem 1's hypothesis true at %d of 600 random points"
          % ("ok" if dis == 0 and seen_true > 0 else "XX", evals, dis, seen_true))
    ok &= dis == 0 and seen_true > 0
    # (3) the counting-axis extension on random generated sublattices with random monotone bounds,
    #     and Theorem 1's Z3 hypothesis and conclusion evaluated on cells of those extensions
    fails = 0
    trials = 0
    caught = 0
    tied = 0
    hypT, conclT, vT = counting_axis_formula()
    for _ in range(150):
        shape = rnd.choice([(3, 3), (4, 3), (3, 3, 3), (2, 4, 3)])
        cells = PROVER.cells_of(shape)
        Xs = set(rnd.sample(cells, rnd.randint(2, 6)))
        while True:                                                     # generated sublattice
            new = {PROVER.meet(a, b) for a in Xs for b in Xs} | {PROVER.join(a, b) for a in Xs for b in Xs}
            if new <= Xs:
                break
            Xs |= new
        p = rnd.randrange(len(shape))
        lo = sorted(rnd.randint(0, 2) for _ in range(shape[p]))
        hi = [l + rnd.randint(0, 3) for l in lo]
        hi = [max(hi[:i + 1]) for i in range(len(hi))]                  # monotone
        ext = {c + (y,) for c in Xs for y in range(lo[c[p]], hi[c[p]] + 1)}
        m, j = brute_closure_failures(ext)
        fails += m + j
        trials += 1
        ext_l = sorted(ext)
        for _ in range(3):                                              # the encoding on this instance's own cells
            c1, c2 = rnd.choice(ext_l), rnd.choice(ext_l)
            vals = (c1[p], c2[p], c1[p], c2[p], c1[-1], c2[-1], lo[c1[p]], lo[c2[p]], hi[c1[p]], hi[c2[p]])
            sub = list(zip(vT, vals))
            tied += z3_eval(hypT, sub) and z3_eval(conclT, sub)
        bad = list(hi)
        if len(bad) >= 2:
            bad[0], bad[-1] = bad[-1] + 2, bad[0]                       # a non-monotone control
            ext2 = {c + (y,) for c in Xs for y in range(0, bad[c[p]] + 1)}
            m2, j2 = brute_closure_failures(ext2)
            caught += (m2 + j2) > 0
    ok &= fails == 0 and caught > 0 and tied == 3 * trials
    print("  [%s] guard: counting-axis extensions closed on %d random sublattices (%d failures); non-monotone control caught %d times; Theorem 1's encoding true on %d of %d cell pairs drawn from them"
          % ("ok" if fails == 0 and caught > 0 and tied == 3 * trials else "XX", trials, fails, caught, tied, 3 * trials))
    return ok


def guard_vacuity():
    ok = True
    hyp, concl, v = counting_axis_formula()
    x1, x2, u1, u2, y1, y2, l1, l2, h1, h2 = v
    r, _ = z3_sat(z3.And(hyp, x1 < x2, u1 > u2, l1 < y1, y1 < h1, l2 < y2, y2 < h2, l1 < l2, h2 < h1))
    ok &= r == z3.sat
    print("  [%s] guard: counting-axis hypothesis satisfiable with y strictly inside both bounds, x1 < x2, u1 > u2 (the two parents moving oppositely), lo and hi both strictly monotone there" % ("ok" if r == z3.sat else "XX"))
    hyp, join, meet, v = triangle_formulas()
    a1, b1, c1, a2, b2, c2 = v
    r, _ = z3_sat(z3.And(hyp, a1 != a2, b1 != b2, c1 > 0, c2 > 0))
    ok &= r == z3.sat
    print("  [%s] guard: triangle hypothesis satisfiable with two distinct non-degenerate triples" % ("ok" if r == z3.sat else "XX"))
    hyp, join, meet, vb = band_formulas()
    k, a1, b1, a2, b2 = vb
    r, _ = z3_sat(z3.And(hyp, k >= 1, a1 != a2, b1 != b2))
    ok &= r == z3.sat
    hyp2, join2, meet2, vc = cband_formulas()
    a1, b1, c1, a2, b2, c2 = vc
    r2, _ = z3_sat(z3.And(hyp2, a1 != a2, b1 != b2, c1 > 0, c2 > 0))
    ok &= r2 == z3.sat
    hyp3, join3, meet3, vs = cst_formulas()
    k, x1, y1, x2, y2 = vs
    r3, _ = z3_sat(z3.And(hyp3, x1 != x2, y1 != y2))
    ok &= r3 == z3.sat
    print("  [%s] guard: band, |a−b| ≤ c and constant-side-triangle hypotheses satisfiable with two distinct non-degenerate members" % ("ok" if r == z3.sat and r2 == z3.sat and r3 == z3.sat else "XX"))
    # the finite-box obligation: a closed S strictly inside the box together with a non-constant h
    cells = PROVER.cells_of((3, 3))
    S = PROVER.subset_vars(cells, "s")
    h = [z3.Int("h_%d" % a) for a in range(3)]
    r, _ = z3_sat(z3.And(PROVER.closed(S, cells), z3.Or([z3.Not(S[c]) for c in cells]), z3.Or([S[c] for c in cells]),
                         h[0] <= h[1], h[1] <= h[2], h[0] < h[2], h[0] >= -1, h[2] <= 2))
    ok &= r == z3.sat
    print("  [%s] guard: finite-box hypothesis satisfiable with S strictly inside the box and h non-constant" % ("ok" if r == z3.sat else "XX"))
    return ok


def check_z3():
    section("§4  THE THEOREMS, MACHINE-CHECKED OVER THE INTEGERS (every cap at once)")
    print("  Z3 %s; guards first, obligations only if both pass" % z3.get_version_string())
    g1 = guard_vacuity()
    g2 = guard_encoding()
    DATA["guards"] = (g1, g2)
    if not (g1 and g2):
        ob("GUARD", "soundness guards", False, "obligations not reported")
        return
    ob("GUARD", "both guards passed (non-vacuity; encoding fidelity with a negative control)", True)
    hyp, concl, _ = counting_axis_formula()
    r = z3_prove(z3.Implies(hyp, concl))
    ob("MACHINE-CHECKED", "Theorem 1: an axis between monotone bounds of one parent is meet- and join-closed",
       r == z3.unsat, "integers, all caps: %s" % r)
    t0 = time.time()
    r = PROVER.prove("Theorem 1, finite-box form", (3, 3), counting_box_claim, quiet=True)
    ob("MACHINE-CHECKED", "Theorem 1, box form: every closed S ⊆ 3×3, every monotone h ∈ {−1..2}, extension closed",
       r, "2^9 subsets × all h, %.0fs" % (time.time() - t0))
    hyp, join, meet, v = triangle_formulas()
    ob("MACHINE-CHECKED", "Theorem 3: the triangle region |a−b| ≤ c ≤ a+b is join-closed", z3_prove(z3.Implies(hyp, join)) == z3.unsat,
       "integers, all caps")
    r, m = z3_sat(z3.And(hyp, z3.Not(meet)))
    ob("REFUTATION", "Theorem 3: the triangle region is not meet-closed (Z3 finds a witness)", r == z3.sat,
       "e.g. " + ", ".join("%s=%s" % (x, m.eval(x)) for x in v) if m is not None else "")
    inT = lambda a, b, c: abs(a - b) <= c <= a + b
    w1 = (0, 1, 1), (1, 0, 1)
    w2 = (4, 0, 4), (2, 2, 0)
    ok = all(inT(*p) and inT(*q) and not inT(*map(min, p, q)) for p, q in (w1, w2))
    ob("REFUTATION", "the two explicit meet witnesses: (0,1,1)∧(1,0,1) = (0,0,1) and (4,0,4)∧(2,2,0) = (2,0,0)", ok)
    hyp, join, meet, _ = band_formulas()
    ob("MACHINE-CHECKED", "Theorem 4(i): B_k = {|a−b| ≤ k} is a sublattice for every k ≥ 0",
       z3_prove(z3.Implies(hyp, z3.And(join, meet))) == z3.unsat, "integers, all k and all caps")
    hyp, join, meet, _ = cband_formulas()
    ob("MACHINE-CHECKED", "Theorem 4(ii): C = {|a−b| ≤ c} is join-closed", z3_prove(z3.Implies(hyp, join)) == z3.unsat, "integers")
    r, m = z3_sat(z3.And(hyp, z3.Not(meet)))
    inC = lambda a, b, c: abs(a - b) <= c
    ok = r == z3.sat and inC(2, 0, 2) and inC(2, 2, 0) and not inC(2, 0, 0)
    ob("REFUTATION", "Theorem 4(iii): C is not meet-closed; witness (2,0,2)∧(2,2,0) = (2,0,0)", ok)
    hyp, join, meet, v = cst_formulas()
    ob("MACHINE-CHECKED", "Theorem 5(iii): the constant-side triangle {|x−k| ≤ y ≤ x+k} is join-closed for every constant k ≥ 1",
       z3_prove(z3.Implies(hyp, join)) == z3.unsat, "integers, k free")
    r, m = z3_sat(z3.And(hyp, z3.Not(meet)))
    inS = lambda k, x, y: x >= 0 and y >= 0 and abs(x - k) <= y <= x + k
    wit = all(inS(k, 0, k) and inS(k, k, 0) and not inS(k, 0, 0) for k in range(1, 7))
    ob("REFUTATION", "Theorem 5(iii): it is not meet-closed; the solver's model, and (0,k)∧(k,0) = (0,0) verified for k = 1..6",
       r == z3.sat and wit, "e.g. " + ", ".join("%s=%s" % (x, m.eval(x)) for x in v) if m is not None else "")


# ----------------------------------------------------------------------------- the seed
def envelope_steps(X):
    d = len(X[0])
    alph = [sorted(set(c[i] for c in X)) for i in range(d)]
    st = []
    for i in range(d):
        for j in range(d):
            if i == j:
                continue
            prev = None
            for a in alph[j]:
                p = max(y[i] for y in X if y[j] <= a)
                if p != prev:
                    st.append((i, j, a, p))
                    prev = p
    return alph, st


def cover_signature(c, st):
    return frozenset(k for k, (i, j, a, p) in enumerate(st) if c[j] <= a and c[i] == p)


def min_cover(S, nel):
    """Exact minimum set cover by branch and bound over the family S (frozensets over range(nel))."""
    U = frozenset(range(nel))
    unc, ch = set(U), []
    while unc:
        s = max(S, key=lambda t: len(t & unc))
        ch.append(s)
        unc -= s
    best = [ch]
    bye = {e: [s for s in S if e in s] for e in U}

    def rec(unc, chosen):
        if not unc:
            if len(chosen) < len(best[0]):
                best[0] = list(chosen)
            return
        if len(chosen) + 1 >= len(best[0]):
            return
        mx = max(len(s & unc) for s in S)
        if len(chosen) + -(-len(unc) // mx) >= len(best[0]):
            return
        e = min(unc, key=lambda e: len(bye[e]))
        for s in sorted(bye[e], key=lambda t: -len(t & unc)):
            rec(unc - s, chosen + [s])
    rec(set(U), [])
    return best[0]


def slots_of(alph):
    return [(i, v) for i in range(len(alph)) for v in alph[i]]


def greedy_cover(S, nel):
    """Plain greedy set cover: an upper bound, and the algorithm behind the figures 7, 9, 9."""
    unc, ch = set(range(nel)), []
    while unc:
        s = max(S, key=lambda t: len(t & unc))
        ch.append(s)
        unc -= s
    return ch


def max_packing(nel, sigs):
    """The largest set of elements no signature contains two of, by exact branch and bound.
    Any cover needs one set per packed element, so the packing number bounds the cover below."""
    adj = [set() for _ in range(nel)]
    for s in sigs:
        for e in s:
            adj[e] |= s
    for e in range(nel):
        adj[e].discard(e)
    best = [[]]

    def rec(cand, chosen):
        if len(chosen) > len(best[0]):
            best[0] = list(chosen)
        cand = sorted(cand, key=lambda e: len(adj[e] & set(cand)))
        while cand:
            if len(chosen) + len(cand) <= len(best[0]):
                return
            e = cand[0]
            rec([x for x in cand[1:] if x not in adj[e]], chosen + [e])
            cand = cand[1:]
    rec(sorted(range(nel), key=lambda e: len(adj[e])), [])
    return best[0]


def reduce_instance(nel, dom):
    """Two exact reductions of a set-cover instance, each checked by its caller as a GUARD.
    Element dominance: if every set covering e also covers e', then covering e covers e', so e'
    may be dropped.  Set dominance (again, after the restriction): a set inside another may be
    replaced by the larger without growing the cover.  Returns (kept elements, reduced family)."""
    cov = {e: frozenset(m for m, s in enumerate(dom) if e in s) for e in range(nel)}
    keep = []
    for e in sorted(range(nel), key=lambda e: len(cov[e])):
        if not any(cov[k] <= cov[e] for k in keep):
            keep.append(e)
    K = set(keep)
    fam2 = list({frozenset(s & K) for s in dom})
    dom2 = [s for s in fam2 if s and not any(s < t for t in fam2)]
    return keep, cov, dom2


def check_seed():
    section("§9  THE SEED — a minimum cover of the envelope steps and alphabet slots")
    L = stages()
    want = {8: 7, 9: 8, 10: 9}            # exact, by branch and bound; the source's figures are 7, 9, 9
    greedy_figure = {8: 7, 9: 9, 10: 9}    # what plain greedy returns on steps + slots: the source's figures
    DATA["seed"] = {}
    for d in (8, 9, 10):
        X = L[d]
        alph, st = envelope_steps(X)
        slots = slots_of(alph)
        sig = {}
        for c in X:
            sig.setdefault(cover_signature(c, st), []).append(c)
        fam = list(sig)
        dom = [s for s in fam if not any(s < t for t in fam)]
        # (1) the relaxation — cover the STEPS only — solved exactly by branch and bound over the
        #     signatures maximal under inclusion.  Its optimum is a lower bound on the seed.
        t0 = time.time()
        best = min_cover(dom, len(st))
        tb = time.time() - t0
        G = [sig[s][0] for s in best]
        realised = all({c[i] for c in G} == set(alph[i]) for i in range(d))
        ob("EXHAUSTIVE", "minimum cover of the %d envelope steps of Λ_%d is %d, by branch and bound over %d maximal signatures"
           % (len(st), d, len(best), len(dom)), len(best) == want[d],
           "%d distinct signatures, %.0fs" % (len(fam), tb))
        # (2) the exhibited minimum cover also realises every alphabet value, so it is a seed:
        #     the relaxation is tight and seed(Λ_d) equals its optimum.
        ob("EXHAUSTIVE", "that cover realises every alphabet value of Λ_%d, so seed(Λ_%d) = %d exactly" % (d, d, want[d]),
           realised and len(best) == want[d], "%d slots, all realised: %s" % (len(slots), realised))
        # (3) the seed regenerates the stage under two independent staircases: the pure-Python one
        #     over the FIXED box of the stage, and the numpy sweep over the seed's OWN box.
        reg_fixed = stair_py(G, alph) == set(X)
        r_own, box_own = staircase_sweep(G)
        reg_own = r_own == len(X) and box_own == DATA["box"][d]
        ob("EXHAUSTIVE", "ℛ(seed) = Λ_%d under both independent staircases (fixed box; the seed's own box)" % d,
           reg_fixed and reg_own, "|ℛ(G)| = %d in a box of %d" % (r_own, box_own))
        # (4) plain greedy on steps + slots returns the source's figure — an upper bound only.
        full = [cover_signature(c, st) | frozenset(len(st) + k for k, (i, v) in enumerate(slots) if c[i] == v) for c in X]
        gr = greedy_cover(full, len(st) + len(slots))
        ob("EXHAUSTIVE", "greedy set cover of steps + slots at Λ_%d returns %d (an upper bound; exact %d)" % (d, greedy_figure[d], want[d]),
           len(gr) == greedy_figure[d] and len(gr) >= want[d], "%d" % len(gr))
        # (5) the packing lower bound: an explicit set of steps no cell witnesses two of, checked
        #     against every cell.  It is one short of the seed at every stage.
        P = max_packing(len(st), set(fam))
        pack_ok = all(sum(1 for e in P if e in s) <= 1 for s in fam)
        ob("EXHAUSTIVE", "a packing of %d steps of Λ_%d, no cell witnessing two (maximum, by exact search): seed ≥ %d" % (len(P), d, len(P)),
           pack_ok and len(P) == want[d] - 1, "steps " + " ".join("(%s≤%d→%s=%d)" % (COORDS[j], a, COORDS[i], p) for (i, j, a, p) in (st[e] for e in P)))
        # (6) minimality by Z3 on the dominance-reduced instance.  Two exact reductions, each
        #     checked here as a GUARD rather than assumed: every signature sits inside a maximal one
        #     (set dominance), and every dropped element is covered by every set that covers some
        #     kept element (element dominance).  Over the unreduced 442 maximal signatures of Λ_9 the
        #     same query is not decided in ten minutes; reduced, each stage takes seconds.
        domset = set(dom)
        red1 = all(any(t <= u for u in domset) for t in fam)
        keep, cov, dom2 = reduce_instance(len(st), dom)
        red2 = all(any(cov[k] <= cov[e] for k in keep) for e in range(len(st)))
        K = set(keep)
        red3 = all(any(frozenset(s & K) <= t for t in dom2) for s in dom)
        ob("GUARD", "every covering signature of Λ_%d sits inside a maximal one (%d of %d maximal)" % (d, len(dom), len(fam)), red1)
        ob("GUARD", "every one of the %d steps of Λ_%d is implied by one of %d kept steps; every restricted signature sits inside one of %d"
           % (len(st), d, len(keep), len(dom2)), red2 and red3)
        v = [z3.Bool("s%d" % k) for k in range(len(dom2))]
        clauses = [z3.Or([v[m] for m, t in enumerate(dom2) if e in t]) for e in keep]
        # GUARD, non-vacuity: the cover constraints are satisfiable with `want` signatures under this
        # very encoding, and the model the solver returns is a cover of the kept steps in Python.
        s0 = z3.Solver()
        s0.add(clauses)
        s0.add(z3.AtMost(*v, want[d]))
        r0 = s0.check()
        chosen0 = []
        if r0 == z3.sat:
            m0 = s0.model()
            chosen0 = [dom2[m] for m in range(len(dom2)) if z3.is_true(m0.eval(v[m], model_completion=True))]
        vac = r0 == z3.sat and len(chosen0) <= want[d] and all(any(e in t for t in chosen0) for e in keep)
        ob("GUARD", "non-vacuity at Λ_%d: the cover constraints are satisfiable with %d signatures, and the solver's model is a cover of the %d kept steps"
           % (d, want[d], len(keep)), vac, "%s, %d signatures chosen" % (r0, len(chosen0)))
        # GUARD, encoding fidelity: the clause set evaluated at concrete assignments says "covers"
        # exactly when the chosen signatures cover the kept steps in Python — on the exhibited cover
        # carried into the reduced instance, on that cover with each one member removed, and on
        # random subsets of the reduced family; and it says "does not cover" at least once.
        Kset = set(keep)
        carried = []
        for s_ in best:
            r_ = frozenset(s_ & Kset)
            if r_:
                carried.append(next(t for t in dom2 if r_ <= t))         # red3: such a t exists
        carried = list(dict.fromkeys(carried))
        def says(chosen):
            sub = [(v[m], z3.BoolVal(dom2[m] in chosen)) for m in range(len(dom2))]
            r_ = z3.simplify(z3.substitute(z3.And(clauses), *sub))
            return z3.is_true(r_) if (z3.is_true(r_) or z3.is_false(r_)) else None
        truth = lambda chosen: all(any(e in t for t in chosen) for e in keep)
        trials_f = [set(carried)] + [set(carried) - {t} for t in carried]
        rndf = random.Random(17 + d)
        trials_f += [set(rndf.sample(dom2, rndf.randint(1, len(dom2)))) for _ in range(40)]
        answers = [(says(c), truth(c)) for c in trials_f]
        fid = (all(a == b for a, b in answers) and answers[0] == (True, True)
               and any(a is False for a, b in answers[1:1 + len(carried)]))
        ob("GUARD", "encoding fidelity at Λ_%d: the clause set agrees with the concrete cover test on the carried minimum, on it minus each member, and on 40 random subsets; it says no of some deletion"
           % d, fid, "%d assignments, %d disagreements; carried cover of %d signatures says %s"
           % (len(answers), sum(a != b for a, b in answers), len(carried), answers[0][0]))
        s = z3.Solver()
        s.add(clauses)
        s.add(z3.AtMost(*v, want[d] - 1))
        t0 = time.time()
        r = s.check()
        ob("MACHINE-CHECKED", "no %d cells cover the steps of Λ_%d (every subset of the %d reduced signatures against %d kept steps)"
           % (want[d] - 1, d, len(dom2), len(keep)), r == z3.unsat and red1 and red2 and red3 and vac and fid,
           "%s, %.0fs; reported only with both guards and both reductions passed" % (r, time.time() - t0))
        DATA["seed"][d] = dict(steps=len(st), slots=len(slots), distinct=len(fam), dominant=len(dom), size=len(best), G=G,
                               greedy=len(gr), packing=len(P), kept=len(keep), reduced=len(dom2))
    ob("EXHAUSTIVE", "the seeds 7, 8, 9 rise by one at each stage; the greedy figures 7, 9, 9 do not (Λ_9 is where they part)",
       [DATA["seed"][d]["size"] for d in (8, 9, 10)] == [7, 8, 9] and [DATA["seed"][d]["greedy"] for d in (8, 9, 10)] == [7, 9, 9])
    comp = [round(len(L[d]) / DATA["seed"][d]["size"]) for d in (8, 9, 10)]
    DATA["compression"] = comp
    ob("EXHAUSTIVE", "compression |Λ|/seed = 139, 207, 282 at the three stages", comp == [139, 207, 282], str(comp))
    # the requirement count, stage by stage: envelope steps plus alphabet values
    req = {}
    for d in (8, 9, 10):
        a, st = envelope_steps(L[d])
        req[d] = (len(st), sum(len(x) for x in a))
    DATA["requirements"] = req
    ob("EXHAUSTIVE", "envelope steps and alphabet values per stage",
       req == {8: (77, 25), 9: (105, 29), 10: (138, 33)},
       "; ".join("Λ_%d: %d steps + %d values = %d" % (d, a, b, a + b) for d, (a, b) in sorted(req.items())))
    # fidelity guard for the cover reading, on Λ_8: covering all steps <=> ℛ(G) = X, and the
    # negative control: a seed less one cell fails both
    X = L[8]
    alph, st = envelope_steps(X)
    G = DATA["seed"][8]["G"]
    slots = slots_of(alph)
    rnd = random.Random(11)
    agree = agree_own = 0
    tot = 0
    for _ in range(40):
        H = set(rnd.sample(X, rnd.randint(3, 12))) | set(rnd.sample(G, rnd.randint(0, 7)))
        covered = all(any(c[j] <= a and c[i] == p for c in H) for (i, j, a, p) in st)
        realised = all(any(c[i] == v for c in H) for (i, v) in slots)
        regen = stair_py(H, alph) == set(X)                 # in the fixed box: steps alone decide it
        r_own, box_own = staircase_sweep(list(H))           # in H's own box: steps AND slots decide it
        regen_own = r_own == len(X) and box_own == DATA["box"][8]
        agree += covered == regen
        agree_own += (covered and realised) == regen_own
        tot += 1
    minus = G[1:]
    covered = all(any(c[j] <= a and c[i] == p for c in minus) for (i, j, a, p) in st)
    regen = stair_py(minus, alph) == set(X)
    ob("GUARD", "cover-of-steps ⇔ ℛ(G) = Λ_8 in the fixed box, and cover-of-steps-and-slots ⇔ ℛ(G) = Λ_8 in G's own box, on %d random subsets; seed minus one cell fails both" % tot,
       agree == tot and agree_own == tot and not covered and not regen, "%d/%d and %d/%d agree" % (agree, tot, agree_own, tot))


# ----------------------------------------------------------------------------- selftest
def selftest():
    print("SELFTEST — the guards, and false claims that must be refuted")
    g = guard_vacuity() and guard_encoding()
    ob("GUARD", "guards pass", g)
    # negative control 1: a wrong reference must be caught by the encoding guard's brute force.
    # The region with the upper bound only, {c <= a + b}, is NOT closed either — (2,0,2) ∧ (0,2,2)
    # = (0,0,2) leaves it — so what separates it from T is its failure count, 2254 against 2862.
    # (An earlier form of this control asserted the wrong region closed; that was a bug in the
    # control, not in the guard, and it is what the selftest exists to catch.)
    T6 = {(a, b, c) for a in range(7) for b in range(7) for c in range(7) if abs(a - b) <= c <= a + b}
    wrong = {(a, b, c) for a in range(7) for b in range(7) for c in range(7) if c <= a + b}     # drops the lower bound
    m, j = brute_closure_failures(wrong)
    ob("GUARD", "negative control: the upper-bound-only region's failure counts differ from T's, so the guard separates them",
       (m, j) == (2254, 0) and brute_closure_failures(T6) == (2862, 0) and (m, j) != (2862, 0),
       "wrong region %d / %d, T %d / %d" % ((m, j) + brute_closure_failures(T6)))
    # negative control 2: the false claim "the triangle is meet-closed" is refuted by Z3
    hyp, join, meet, _ = triangle_formulas()
    ob("REFUTATION", "negative control: 'the triangle region is meet-closed' is refuted", z3_prove(z3.Implies(hyp, meet)) == z3.sat)
    # negative control 3: the false claim "an axis under a NON-monotone bound is closed"
    x1, x2, y1, y2, h1, h2 = z3.Ints("x1 x2 y1 y2 h1 h2")
    hyp = z3.And(y1 <= h1, y2 <= h2, y1 >= 0, y2 >= 0)                # no monotonicity
    concl = Max(y1, y2) <= z3.If(x1 >= x2, h1, h2)
    ob("REFUTATION", "negative control: Theorem 1 without monotonicity is refuted", z3_prove(z3.Implies(hyp, concl)) == z3.sat)
    # negative control 3b: the false claim "the constant-side triangle is meet-closed" is refuted by Z3
    hyp, join, meet, _ = cst_formulas()
    ob("REFUTATION", "negative control: 'the triangle with one side constant is meet-closed' is refuted", z3_prove(z3.Implies(hyp, meet)) == z3.sat)
    # negative control 4: the exact-triangle stage is not closed
    L = stages()
    L12t = [c + (K,) for c in L[11] for K in range(0, c[10] + 2 * c[5] + 1) if abs(c[10] - 2 * c[5]) <= K and (K - c[10]) % 2 == 0]
    r, _ = staircase_sweep(L12t)
    ob("REFUTATION", "negative control: 'Λ_12 under the exact triangle is closed' is refuted", r != len(L12t), "E = %d" % (r - len(L12t)))
    # negative control 5: a wrong maximal-chain count (covers taken as any +1 in any coordinate, ignoring membership)
    ob("REFUTATION", "negative control: chains counted without membership give the box's count, not Λ_8's",
       count_box_chains() != 1113045672, "%d" % count_box_chains())


def count_box_chains():
    from math import factorial
    spans = [2, 1, 2, 3, 2, 1, 3, 3]
    n = factorial(sum(spans))
    for s in spans:
        n //= factorial(s)
    return n


def summary():
    print("\n" + "=" * 100)
    by = collections.Counter(s for s, n, ok, d in RESULTS)
    fails = [n for s, n, ok, d in RESULTS if not ok]
    print("obligations: " + ", ".join("%s %d" % (k, v) for k, v in sorted(by.items())) + "  — total %d" % len(RESULTS))
    print("failures: %d%s" % (len(fails), (" — " + "; ".join(fails)) if fails else ""))
    print("=" * 100)
    return 0 if not fails else 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args(argv)
    t0 = time.time()
    if a.selftest:
        selftest()
    else:
        check_stages()
        check_physics_bounds()
        check_envelope_gap()
        check_envelope_family()
        check_z3()
        check_graph()
        check_cylinder()
        check_rank_and_chains()
        check_brackets()
        check_seed()
    print("elapsed %.0fs" % (time.time() - t0))
    return summary()


if __name__ == "__main__":
    sys.exit(main())
