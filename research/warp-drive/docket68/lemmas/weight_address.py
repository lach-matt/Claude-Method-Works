#!/usr/bin/env python3
"""weight_address.py -- item 235: which weighting the bulk's ensemble carries, and what each weighting makes of position
2's address, against plausibility.  M: "Ask the cypher which weighting the ensemble carries. ... Each weighting likely
governs a aspect of position 2's address, each individually bearing on what position 2 can actually be compared to
plausibility."  Worked in the conversation (computed, exact where marked; deduced where marked; not verified by a
separate session; not seated); 2026-10-11.

Position 2's address is its place in item 233's bulk index: i steps of 2b and j of 2P, so G x 2^(i+j), tension x
2^(-2j), the 5D coupling x 2^(i+3j), the curvature in 5D Planck units x 2^(-2i/3) (sigma/sigma_P x 2^(2i)), and the
matter law.

  A0 (read) M's item-235 words, verbatim in the rulings file.
  A1 (computed, exact) Every normalisable weighting of item 234 is G^x sigma^-z: its lattice exponents are a = x,
     b = x + 2z.  The record's weightings lie on three rays -- G's (z = 0: G, the corridor's mass, alpha_G, the bit
     area), the coupling's (z = x: kappa5^4 = 48 pi G/(sigma c^4), G5, l5) and the tension's (x = 0: 1/sigma, relative
     floor only) -- and the three are two directions: the coupling is G over the tension.  In the family each
     multiplier is conjugate to one coordinate of the address (x to log G, z to -log sigma): the mean address moves
     with them through the ensemble's covariance, positive definite.
  A2 (computed; sums exact, the j-tails in closed form) Each of the record's weightings, under each floor reading, as
     an ensemble over the plausible bulk (weight x item 233's window share).  Every one puts position 2 within a few
     doublings of the G ceiling where its own tension window closes -- G <= ours x 2^W (relative, W = 196.885) or x
     2^(W/2) (absolute): mean log2 G 193.9 / 95.6 for G's weight.  2a-2P (item 229's destination: the addresses of 2a,
     2b, 2c and 2P) weighs 2.6e-59 under G's weight (relative) and 1.3e-174 under the coupling's; position 1 less still.
  A3 (computed) M's guess H-WEIGHT-GOVERNS-ADDRESS, tested.  G's weights fix position 2's G (spread 2-4 doublings) and
     leave its tension, its coupling and its 5D curvature spread along the whole top edge (57 doublings): one aspect
     each, as M guessed.  The coupling's and the tension's weights fix two -- G and the 5D curvature, the latter at ours
     (the 2P direction: position 2 a 2P-like universe of very high coupling).  No weighting the record computes touches
     the matter law (each law 1/3) or the offset (item 233 K7).
  A4 (computed; the statistics language's maximum-entropy principle, register 1174, with the destination's mean address
     as the constraint) The destination itself picks the weighting in the family: x = 0.014879, z = -0.000112 (relative)
     or x = 0.029579, z = -0.000045 (absolute) -- G's ray, the tension's multiplier zero to within 1 % of G's.  It is a
     G-weighting of exponent about 1/67 (1/34), a number the record does not compute.  The control: other addresses near
     ours fitted the same way give |z|/x from 5 % to 67 % -- (5, -3), (-10, 10), (20, 0), (0, 20), (-30, -30), (40, 40)
     in (i, j) -- so landing on G's ray is the destination's own, not nearness to ours.  Under it position 2's address is
     centred on 2a-2P but spread: log2 G over 139 (69) doublings; the destination family weighs 8.4e-5 (1.7e-4).
  A4b (computed) The trade along each ray, scanned in strength x: as x grows, position 2's G rises to the ceiling, its
     spread falls (about 2/x doublings on G's ray) and the destination's weight falls (about 2^(-x W) once the mean has
     passed it): 7.6e-5, 8.0e-6, 3.6e-8, 1.8e-13, 2.1e-30, 2.6e-59 at x = 0.02, 0.05, 0.1, 0.2, 0.5, 1 (G's ray,
     relative).  Fixing position 2's G and carrying the destination trade against each other: to give 2a-2P a weight
     of 1e-3, G must be left spread over tens of doublings (one scanned strength, G's ray at x = 0.2 absolute, does both
     at the stated margins: a spread of 10 doublings and a weight of 7e-8).
  A5 (computed; the cypher, roster 1173, audited) The weightings -- the record's, A4b's scanned strengths, the
     destination-fitted one, the unweighted count -- as cells over (governs G, governs the 5D curvature, carries the
     destination, a quantity the record computes, normalisable).  The target -- a normalisable weighting the record
     computes that carries the destination -- is held by none: the record's weightings never carry it, and those that do
     are strengths the record does not compute.  The audit finds no key and no one-hot code (7 cells).  Order, algebra
     and information admit target cells -- such a weighting is admissible from the cells' structure, held by none --
     and geometry and statistics refuse them: the cypher does not decide whether some weighting the record could compute
     would carry the destination.  The record's actual weightings do not (A2).
  A6 (deduced) So the ensemble carries a G-weighting: the record's own G-weights and the destination agree on the ray
     and disagree on its strength.  At the record's strengths (G, G^1/2) position 2 is pressed against the G ceiling
     and 2a-2P is all but excluded; at the destination's (G^0.015) 2a-2P is the centre and position 2 is spread over
     the window.  Which strength is the open number: one exponent, governing the G aspect of position 2's address.

What this does not show.
  - A4b's "about 2/x" and "2^(-x W)" are read off the scan, not derived; the scan's values are exact sums.
  - The weightings are the record's quantities and their powers (item 234 V1); a weighting peaked at a universe needs a
    width the record does not give.
  - A4 constrains the means only (order 1), the analogue of the statistics language's order-k tables on an infinite
    lattice; the destination's mean is over its four named positions (2a, 2b, 2c, 2P); over its six universes the
    exponents differ by 4.9e-6 (relative) and 1.0e-5 (absolute).
  - "Governs" is a spread below 20 doublings in log2 G and 30 in the curvature exponent; the data separate at 9.1 / 19.3
    against 56.9, so any threshold between gives the same table.

Imports bulk5_index.py (and through it p2_planck.py), tools/cypher.py and index_audit.py by path.  Stdlib.
python3 weight_address.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M235 = ("Ask the cypher which weighting the ensemble carries. Which weighting is not fixed. Several weights that rise with "
        "G work, and the record doesn't choose among them. Each weighting likely governs a aspect of position 2's address, "
        "each individually bearing on what position 2 can actually be compared to plausibility.")
LANGS = ("order", "algebra", "geometry", "information", "statistics")
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
DEST = ((0, 0), (1, 0), (1, 0), (0, 1))        # 2a, 2b, 2c, 2P as (i, j) addresses
DEST_UNIVERSES = ((0, 0), (0, 0), (1, 0), (1, 0), (1, 0), (0, 1))
GOVERN_G, GOVERN_C1, CARRY = 20.0, 30.0, 1e-8


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


B5 = _load(os.path.join(HERE, "bulk5_index.py"), "wa_b5")
K = B5.constants()
W = K["W"]
# the record's normalisable weightings (item 234 V1) as G^x sigma^-z, and their lattice exponents (a, b) = (x, x + 2z)
RECORD = {"G": (1.0, 0.0), "m1": (0.5, 0.0), "kappa5^4": (1.0, 1.0), "G5": (0.5, 0.5), "l5": (1 / 6, 1 / 6),
          "1/sigma": (0.0, 1.0)}


def ab(x, z):
    return (x, x + 2 * z) if not MUT.get("b_wrong") else (x, x + z)


def normalisable(a, b, floor):
    return (b > 0 and a + b > 0) if floor == "rel" else (b > 0 and a > 0)


# ================================================================================ A2 the ensemble, exact sums
def moments(a, b, floor, tail=60.0):
    """the ensemble 2^(a i + b j) x window share over item 233's plausible lattice: normaliser-free moments of (i, j), the
    destination's and position 1's weights.  For each i the j-tail below the floor's threshold is summed in closed form
    (geometric series with linear and quadratic terms); the finite rest term by term; i is cut where the weight has
    fallen by 2^-tail"""
    q = 2.0 ** (-b)
    imax = int(W // 2)
    rate = a if floor == "abs" else a + b
    imin = -int(tail / rate) - int(W) - 2
    top = lambda i: (W - abs(i)) if floor == "rel" else (W - 2 * max(i, 0)) / 2
    R = max(a * i + b * top(i) for i in range(imin, imax + 1))
    S = [0.0] * 6
    for i in range(imin, imax + 1):
        hi = min(W, W - 2 * i)
        if hi < 0:
            continue
        j0 = i if floor == "rel" else 0
        if MUT.get("floor_threshold"):
            j0 = 0 if floor == "rel" else i
        c = hi / W
        e0 = a * i + b * j0 - R
        base = 2.0 ** e0 if e0 > -1000 else 0.0
        s0 = base / (1 - q)
        s1 = base * (j0 / (1 - q) - q / (1 - q) ** 2)
        s2 = base * (j0 * j0 / (1 - q) - 2 * j0 * q / (1 - q) ** 2 + q * (1 + q) / (1 - q) ** 3)
        S[0] += c * s0
        S[1] += c * i * s0
        S[2] += c * s1
        S[3] += c * i * i * s0
        S[4] += c * s2
        S[5] += c * i * s1
        j = j0 + 1
        while True:
            lo = (j - i) if floor == "rel" else 2 * j
            if lo > hi:
                break
            wt = (hi - lo) / W * 2.0 ** (a * i + b * j - R)
            S[0] += wt
            S[1] += i * wt
            S[2] += j * wt
            S[3] += i * i * wt
            S[4] += j * j * wt
            S[5] += i * j * wt
            j += 1
    Z = S[0]
    Ei, Ej = S[1] / Z, S[2] / Z
    Vi, Vj, Cij = S[3] / Z - Ei ** 2, S[4] / Z - Ej ** 2, S[5] / Z - Ei * Ej
    cell = lambda i, j: B5.weight(i, j, K, floor) * 2.0 ** (a * i + b * j - R) / Z
    return dict(Ei=Ei, Ej=Ej, Vi=Vi, Vj=Vj, Cij=Cij, dest=sum(cell(i, j) for i, j in set(DEST)), ours=cell(0, 0))


def address(m):
    """the address coordinates' means and spreads: log2 G = i + j, log2 sigma = -2j, the curvature exponent c1 = 2i
    (sigma/sigma_P), the coupling's c2 = i + 3j"""
    lin = {"log2G": (1, 1), "log2sigma": (0, -2), "c1": (2, 0), "c2": (1, 3)}
    out = {}
    for n, (p, r) in lin.items():
        mean = p * m["Ei"] + r * m["Ej"]
        var = p * p * m["Vi"] + r * r * m["Vj"] + 2 * p * r * m["Cij"]
        out[n] = (mean, math.sqrt(max(var, 0.0)))
    return out


def a2():
    rows = {}
    for name, (x, z) in RECORD.items():
        for floor in ("rel", "abs"):
            a, b = ab(x, z)
            if not normalisable(a, b, floor):
                continue
            m = moments(a, b, floor)
            rows[(name, floor)] = dict(x=x, z=z, m=m, ad=address(m), ceiling=W if floor == "rel" else W / 2)
    return rows


# ================================================================================ A4 the destination's weighting
def solve(target, floor, a=0.02, b=0.02):
    """the family member whose mean address equals target (Newton; the Jacobian is ln 2 times the covariance)"""
    m = None
    for it in range(80):
        m = moments(a, b, floor)
        r = (m["Ei"] - target[0], m["Ej"] - target[1])
        if abs(r[0]) < 1e-10 and abs(r[1]) < 1e-10:
            break
        J = [[math.log(2) * m["Vi"], math.log(2) * m["Cij"]], [math.log(2) * m["Cij"], math.log(2) * m["Vj"]]]
        det = J[0][0] * J[1][1] - J[0][1] * J[1][0]
        da = (J[1][1] * r[0] - J[0][1] * r[1]) / det
        db = (-J[1][0] * r[0] + J[0][0] * r[1]) / det
        lam = 1.0
        while a - lam * da <= 0 or b - lam * db <= 0:
            lam /= 2
        a, b = a - lam * da, b - lam * db
    return dict(a=a, b=b, x=a, z=(b - a) / 2, m=m, ad=address(m), cov_pd=m["Vi"] > 0 and m["Vi"] * m["Vj"] > m["Cij"] ** 2)


def a4():
    mean = lambda pts: (sum(p[0] for p in pts) / len(pts), sum(p[1] for p in pts) / len(pts))
    tgt = mean(DEST)
    if MUT.get("dest_shift"):
        tgt = (tgt[0] + 40, tgt[1])
    return {floor: dict(named=solve(tgt, floor), universes=solve(mean(DEST_UNIVERSES), floor), target=tgt)
            for floor in ("rel", "abs")}


# ================================================================================ A4b the strength scan
SCAN = (0.02, 0.05, 0.1, 0.2, 0.5, 1.0)
RAYS = {"G": lambda x: (x, 0.0), "coupling": lambda x: (x, x)}


def a4b(r4):
    out = {}
    for ray, f in RAYS.items():
        for floor in ("rel", "abs"):
            xs = sorted(set(SCAN) | {r4[floor]["named"]["x"]})
            for x in xs:
                a, b = ab(*f(x))
                m = moments(a, b, floor)
                out[(ray, floor, x)] = dict(m=m, ad=address(m), fitted=(x == r4[floor]["named"]["x"]),
                                           record=(ray == "G" and x in (0.5, 1.0)) or (ray == "coupling" and x in (0.5, 1.0)))
    return out


# ================================================================================ A5 the cypher
def a5(cy, ia, r2, r4, r4b=None):
    cells = {}
    for (ray, floor, x), r in (r4b or {}).items():
        if r["record"] or r["fitted"]:
            continue                                           # the record's strengths are r2's; the fitted one is below
        cell = (int(r["ad"]["log2G"][1] <= GOVERN_G), int(r["ad"]["c1"][1] <= GOVERN_C1), int(r["m"]["dest"] >= CARRY), 0, 1)
        cells.setdefault(cell, []).append("%s x %.3g/%s" % (ray, x, floor))
    for (name, floor), r in r2.items():
        cell = (int(r["ad"]["log2G"][1] <= GOVERN_G), int(r["ad"]["c1"][1] <= GOVERN_C1), int(r["m"]["dest"] >= CARRY), 1, 1)
        cells.setdefault(cell, []).append("%s/%s" % (name, floor))
    for floor, d in r4.items():
        r = d["named"]
        cell = (int(r["ad"]["log2G"][1] <= GOVERN_G), int(r["ad"]["c1"][1] <= GOVERN_C1), int(r["m"]["dest"] >= CARRY), 0, 1)
        cells.setdefault(cell, []).append("destination-fitted/%s" % floor)
    # the unweighted count and the window share alone: not normalisable, and in the limit they carry nothing (item 234 V2)
    cells.setdefault((0, 0, 0, 1, 0), []).extend(["unweighted", "window share"])
    coords = ["governs_G", "governs_curvature", "carries_destination", "from_record", "normalisable"]
    held = sorted(cells)
    ix = cy.Index("weight_address", coords, [list(c) for c in held])
    targets = [c for c in held if c[2] == 1 and c[3] == 1 and c[4] == 1]
    adm = {}
    for lg in LANGS:
        a, _ = cy.ADMISSION[lg][0](ix, dict(OPTS))
        adm[lg] = None if a is None else sorted(tuple(ix.decode[x][c[x]] for x in range(5)) for c in a
                                                 if ix.decode[2][c[2]] == 1 and ix.decode[3][c[3]] == 1
                                                 and ix.decode[4][c[4]] == 1)
    return dict(cells=cells, targets=targets, admitted_targets=adm, run=cy.run(ix, "1173", dict(OPTS)),
                audit=ia.audit_index(coords, held))


# ================================================================================ compute, report
def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "wa_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "wa_ia")
    r2 = a2()
    r4 = a4()
    r4b = a4b(r4)
    # A1: the conjugacy -- moving x raises mean log G, moving z raises mean -log sigma (finite differences at G's ray)
    base = moments(*ab(1.0, 0.0), "rel")
    dx = moments(*ab(1.01, 0.0), "rel")
    dz = moments(*ab(1.0, 0.01), "rel")
    conj = dict(dlogG_dx=address(dx)["log2G"][0] - address(base)["log2G"][0],
                dmlogs_dz=-(address(dz)["log2sigma"][0] - address(base)["log2sigma"][0]))
    return dict(r2=r2, r4=r4, r4b=r4b, conj=conj, cy=a5(cy, ia, r2, r4, r4b))


def report(o):
    print("weight_address.py -- which weighting the ensemble carries; position 2's address under each (item 235)\n")
    print("A1 conjugacy at G's ray: d<log2 G>/dx = %.3f (per 0.01), d<-log2 sigma>/dz = %.3f (per 0.01)" % (
        o["conj"]["dlogG_dx"], o["conj"]["dmlogs_dz"]))
    print("\nA2/A3 the record's weightings (x, z) and position 2's address (mean +- spread, doublings of ours):")
    for (n, f), r in o["r2"].items():
        ad = r["ad"]
        print("  %-9s %s  x %.3f z %.3f | log2 G %7.2f +- %5.2f (ceiling %.3f) | log2 sigma %8.2f +- %5.2f | c1 %7.2f +- "
              "%5.2f | c2 %7.2f +- %5.2f | 2a-2P %.2e  ours %.2e" % (
                  n, f, r["x"], r["z"], ad["log2G"][0], ad["log2G"][1], r["ceiling"], ad["log2sigma"][0],
                  ad["log2sigma"][1], ad["c1"][0], ad["c1"][1], ad["c2"][0], ad["c2"][1], r["m"]["dest"], r["m"]["ours"]))
    print("\nA4 the destination's own weighting (mean address = 2a, 2b, 2c, 2P's):")
    for f, d in o["r4"].items():
        for lbl in ("named", "universes"):
            r = d[lbl]
            print("  %s %-9s x %.6f z %.6f | log2 G %.2f +- %.1f | log2 sigma %.2f +- %.1f | c1 +- %.1f | 2a-2P %.3e ours %.3e"
                  % (f, lbl, r["x"], r["z"], r["ad"]["log2G"][0], r["ad"]["log2G"][1], r["ad"]["log2sigma"][0],
                     r["ad"]["log2sigma"][1], r["ad"]["c1"][1], r["m"]["dest"], r["m"]["ours"]))
    print("\nA4b the strength scan (ray, floor, x): mean log2 G +- spread, curvature spread, 2a-2P's weight")
    for (ray, fl, x), r in sorted(o["r4b"].items()):
        print("  %-8s %s x %.4f%s  log2 G %6.1f +- %5.1f  c1 +- %5.1f  2a-2P %.2e" % (
            ray, fl, x, " (fitted)" if r["fitted"] else (" (record)" if r["record"] else ""), r["ad"]["log2G"][0],
            r["ad"]["log2G"][1], r["ad"]["c1"][1], r["m"]["dest"]))
    c = o["cy"]
    print("\nA5 the cypher: cells %s" % {str(k): v for k, v in c["cells"].items()})
    print("   target cells held: %s; target cells admitted per language: %s" % (c["targets"], c["admitted_targets"]))
    print("   roster 1173: %s; audit %s" % ("; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"])
                                                    for v in c["run"]["verdicts"]), c["audit"]))


# ================================================================================ checks
def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("A0 M's item-235 words verbatim in the rulings file", M235 in rul)
    ok = o["conj"]["dlogG_dx"] > 0 and o["conj"]["dmlogs_dz"] > 0
    ok &= ab(1.0, 1.0) == (1.0, 3.0) and ab(0.5, 0.5) == (0.5, 1.5) and ab(0.0, 1.0) == (0.0, 2.0)
    add("A1 the family G^x sigma^-z: the record's weightings on three rays, two directions (kappa5^4 = (1, 3) = G (1, 1) "
        "+ 1/sigma (0, 2)); x moves mean log G, z moves mean -log sigma", ok)
    r2 = o["r2"]
    ok = len(r2) == 11 and ("1/sigma", "abs") not in r2
    ok &= all(r["ceiling"] - r["ad"]["log2G"][0] < 12 for r in r2.values())
    g = r2[("G", "rel")]
    ok &= "%.2f" % g["ad"]["log2G"][0] == "193.94" and "%.2f" % r2[("G", "abs")]["ad"]["log2G"][0] == "95.62"
    ok &= "%.2e" % g["m"]["dest"] == "2.62e-59" and "%.2e" % r2[("kappa5^4", "rel")]["m"]["dest"] == "1.29e-174"
    ok &= all(r["m"]["dest"] < 1e-14 and r["m"]["ours"] < r["m"]["dest"] for r in r2.values())
    add("A2 every record weighting puts position 2's G within 12 doublings of its ceiling (2^W relative, 2^(W/2) "
        "absolute): G's weight 193.94 / 95.62; 2a-2P weighs 2.62e-59 (G) to 1.29e-174 (kappa5^4) and below 1e-14 in all", ok)
    gov = {k: (r["ad"]["log2G"][1] <= GOVERN_G, r["ad"]["c1"][1] <= GOVERN_C1) for k, r in r2.items()}
    ok = all(gov[(n, f)] == (True, False) for n in ("G", "m1") for f in ("rel", "abs"))
    ok &= all(gov[(n, f)] == (True, True) for n in ("kappa5^4", "G5", "l5") for f in ("rel", "abs"))
    ok &= gov[("1/sigma", "rel")] == (True, True)
    ok &= all(r2[(n, f)]["ad"]["c1"][1] > 56 and r2[(n, f)]["ad"]["log2sigma"][1] > 56 for n in ("G", "m1") for f in ("rel", "abs"))
    ok &= max(r["ad"]["log2G"][1] for r in r2.values()) < 9.2 and max(r2[(n, f)]["ad"]["c1"][1] for n in ("kappa5^4", "G5", "l5")
                                                                    for f in ("rel", "abs")) < 19.4
    ok &= all(abs(r2[(n, "rel")]["ad"]["c1"][0]) < 5 for n in ("kappa5^4", "G5", "l5", "1/sigma"))
    add("A3 H-WEIGHT-GOVERNS-ADDRESS: G's weights fix G alone (tension and curvature spread > 56 doublings); the coupling's "
        "and the tension's fix G and the 5D curvature, the latter at ours (|c1| < 5, the 2P direction); the separation "
        "9.1 / 19.3 against 56.9 makes the thresholds immaterial", ok)
    r4 = o["r4"]
    rel, abs_ = r4["rel"]["named"], r4["abs"]["named"]
    ok = "%.6f" % rel["x"] == "0.014879" and "%.6f" % abs_["x"] == "0.029579"
    ok &= abs(rel["z"]) < 0.01 * rel["x"] and abs(abs_["z"]) < 0.01 * abs_["x"] and rel["cov_pd"] and abs_["cov_pd"]
    ok &= abs(r4["rel"]["universes"]["x"] - rel["x"]) < 5e-6 and abs(r4["abs"]["universes"]["x"] - abs_["x"]) < 1.1e-5
    ok &= "%.1e" % rel["m"]["dest"] == "8.4e-05" and "%.1e" % abs_["m"]["dest"] == "1.7e-04"
    ok &= rel["ad"]["log2G"][1] > 100 and abs_["ad"]["log2G"][1] > 60
    ctrl = [abs(solve(t, "rel")["z"]) / solve(t, "rel")["x"] for t in ((5, -3), (-10, 10), (20, 0), (0, 20))]
    ok &= abs(rel["z"]) / rel["x"] < 0.01 and min(ctrl) > 0.05
    add("A4 the destination's mean address picks G's ray (|z| < 1 % of x): x = 0.014879 relative, 0.029579 absolute (the "
        "six universes within 4.9e-6 / 1.0e-5); 2a-2P then weighs 8.4e-5 / 1.7e-4 and log G spreads over > 100 / 60 doublings; "
        "control: other addresses near ours give |z|/x > 5 %", ok)
    sc = o["r4b"]
    ok = True
    for ray in RAYS:
        for fl in ("rel", "abs"):
            xs = [x for (r_, f_, x) in sorted(sc) if r_ == ray and f_ == fl and x >= o["r4"][fl]["named"]["x"]]
            seq = [sc[(ray, fl, x)] for x in xs]
            ok &= all(p["ad"]["log2G"][0] < q["ad"]["log2G"][0] and p["ad"]["log2G"][1] > q["ad"]["log2G"][1]
                      and p["m"]["dest"] > q["m"]["dest"] for p, q in zip(seq, seq[1:]))
    gr = [sc[("G", "rel", x)] for x in SCAN]
    ok &= ["%.1e" % r["m"]["dest"] for r in gr] == ["7.6e-05", "8.0e-06", "3.6e-08", "1.8e-13", "2.1e-30", "2.6e-59"]
    ok &= all(abs(r["ad"]["log2G"][1] * x / 2.04 - 1) < 0.02 for r, x in zip(gr, SCAN) if x >= 0.1)
    add("A4b the trade, on both rays and both floors: from the fitted strength up, mean log G rises, its spread falls and "
        "2a-2P's weight falls; on G's ray (relative) 7.6e-5 ... 2.6e-59 at x = 0.02 ... 1, the spread 2.04/x to 2 %", ok)
    c = o["cy"]
    ok = c["targets"] == [] and bool(c["run"]["verdicts"])
    ok &= any(any("destination-fitted" in n for n in v) for k, v in c["cells"].items() if k[2] == 1)
    ok &= all(k[3] == 0 for k in c["cells"] if k[2] == 1)
    adm = c["admitted_targets"]
    ok &= all(adm[lg] for lg in ("order", "algebra", "information")) and not adm["geometry"] and not adm["statistics"]
    ok &= not c["audit"]["keys"] and not c["audit"]["onehot"]
    add("A5 the cypher (run and audited): no held weighting is normalisable, from the record and carrying the destination; "
        "every one that carries it is a strength the record does not compute; order, algebra, information admit target "
        "cells, geometry and statistics refuse them -- not decided; no key, no one-hot", ok)
    return res


MUTANTS = {"b_wrong": "the lattice exponent b taken as x + z instead of x + 2z",
           "floor_threshold": "the closed-form tail started at the other floor's threshold",
           "dest_shift": "the destination's mean address shifted by 40 doublings of 2b"}


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
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-16s %-62s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
