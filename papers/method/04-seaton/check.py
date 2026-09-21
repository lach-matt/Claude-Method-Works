#!/usr/bin/env python3
"""check.py -- the machine checks behind papers/method/04-seaton/PAPER.md.

Every number the paper prints is produced here, or is CITED.  Exact arithmetic
(fractions.Fraction, decimal at 40 digits for the one square root) throughout;
Z3 for the two real-arithmetic obligations; stdlib otherwise.

    python3 check.py              every obligation, one line each, a summary; exit 1 on failure
    python3 check.py --selftest   the same, plus three negative controls that must be REFUTED

Instruments are imported by path and never copied:
  recovered/ritz.py            the level data of the thirteen series (read with ast, since the
                               file's own imports need scipy, which is absent here)
  tools/populate.py            core_p -- the core's orbital count at l, from the observed
                               ground configurations of LW1-ground.py (register 1306)
  research/warp-drive/prover.py   require_z3 (no lattice obligation arises in this paper)

Statuses, as PAPER-SPEC.md defines them:
  PROVED           a written derivation, verified exactly on a grid above its degree
  EXHAUSTIVE       a decision procedure over a stated finite family (size printed)
  MACHINE-CHECKED  Z3 unsat on the negation, box named, both guards passed
  SOURCE           a figure the source states, compared with what is recomputed here
"""
import ast
import importlib.util
import itertools
import math
import os
import random
import statistics
import sys
from decimal import Decimal, getcontext
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RITZ = os.path.join(REPO, "recovered", "ritz.py")
POPULATE = os.path.join(REPO, "tools", "populate.py")
PROVER = os.path.join(REPO, "research", "warp-drive", "prover.py")
RAW = os.path.join(REPO, "extracted", "archives", "restore-point-2-13", "spectra_raw")
CAPTURE = {"Cd I": os.path.join(RAW, "CdI.tsv"), "Rb I": os.path.join(RAW, "RbI.tsv"),
           "Sr II": os.path.join(RAW, "SrII.tsv"),
           "In I": os.path.join(REPO, "extracted", "archives", "spectra-levels-store", "deliver", "queue2", "InI.tsv")}

getcontext().prec = 40

RESULTS = []          # (status, name, ok, detail)
FIGURES = {}          # every number the paper prints, by key


def report(status, name, ok, detail=""):
    RESULTS.append((status, name, ok, detail))
    print("  [%s] %-16s %-58s %s" % ("ok" if ok else "XX", status, name, detail))
    return ok


# ---------------------------------------------------------------- imports by path

def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_series():
    """The thirteen series, read from recovered/ritz.py by AST.  The file executes
    scipy on import, so its data are read as literals rather than by exec; nothing
    is transcribed."""
    tree = ast.parse(open(RITZ, encoding="utf-8").read())
    got = {}
    for node in tree.body:
        if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
            nm = node.targets[0].id
            if nm in ("S", "LM", "Rinf", "mp"):
                got[nm] = ast.literal_eval(node.value)
    S, LM = got["S"], got["LM"]
    Rinf, mp = got["Rinf"], got["mp"]
    out = []
    for nm, (c, A, lim, levels) in S.items():
        sp, lc = nm.rsplit(" ", 1)
        out.append(dict(name=nm, species=sp, lsym=lc, l=LM[lc], c=c, A=A, lim=lim,
                        levels={int(k): v for k, v in levels.items()}))
    return out, Rinf, mp


# ------------------------------------------------------------- hydrogenic <r^-4>

def laguerre(k, alpha):
    """Generalised Laguerre L_k^{(alpha)}(x) as exact rational coefficients in x."""
    co = []
    for j in range(k + 1):
        co.append(F((-1) ** j * math.comb(k + alpha, k - j), math.factorial(j)))
    return co


def radial_poly(n, l):
    """P(r) with R_nl(r) = N P(r) e^{-r/n}: r^l L_{n-l-1}^{(2l+1)}(2r/n), Z = 1, a.u."""
    L = laguerre(n - l - 1, 2 * l + 1)
    co = {}
    for j, cj in enumerate(L):
        co[l + j] = cj * F(2, n) ** j
    return co


def poly_mul(a, b):
    out = {}
    for i, x in a.items():
        for j, y in b.items():
            out[i + j] = out.get(i + j, 0) + x * y
    return out


def expect_power(n, l, s):
    """<r^s> for the hydrogenic state (n, l), Z = 1, exactly.  Uses
    int_0^inf r^k e^{-2r/n} dr = k! (n/2)^{k+1}, valid for integer k >= 0."""
    P2 = poly_mul(radial_poly(n, l), radial_poly(n, l))
    def integ(shift):
        tot = F(0)
        for k, ck in P2.items():
            kk = k + shift
            if kk < 0:
                raise ValueError("divergent")
            tot += ck * math.factorial(kk) * F(n, 2) ** (kk + 1)
        return tot
    return integ(2 + s) / integ(2)


def r4_formula(n, l):
    """Bethe-Salpeter closed form: [3n^2 - l(l+1)] / [2 n^5 (l+3/2)(l+1)(l+1/2) l (l-1/2)]."""
    D = (F(l) + F(3, 2)) * (l + 1) * (F(l) + F(1, 2)) * l * (F(l) - F(1, 2))
    return F(3 * n * n - l * (l + 1)) / (2 * n ** 5 * D)


def K(l):
    return l * (l + 1) * (2 * l - 1) * (2 * l + 1) * (2 * l + 3)


def ob_r4(nmax=30, wrong=False):
    fam = 0
    bad = 0
    for n in range(2, nmax + 1):
        for l in range(1, n):
            fam += 1
            lhs = expect_power(n, l, -4)
            rhs = r4_formula(n, l)
            if wrong:
                rhs = F(3 * n * n + l * (l + 1)) / (2 * n ** 5) / ((F(l) + F(3, 2)) * (l + 1) * (F(l) + F(1, 2)) * l * (F(l) - F(1, 2)))
            if lhs != rhs:
                bad += 1
    FIGURES["r4_family"] = fam
    FIGURES["r4_nmax"] = nmax
    return fam, bad


def ob_r2_sanity(nmax=30):
    """<r^-2> = 1 / (n^3 (l + 1/2)) -- a second closed form checked the same way, so the
    integration itself is tested against something the <r^-4> formula does not share."""
    fam = bad = 0
    for n in range(2, nmax + 1):
        for l in range(1, n):
            fam += 1
            if expect_power(n, l, -2) != 1 / (n ** 3 * (F(l) + F(1, 2))):
                bad += 1
    return fam, bad


# --------------------------------------------------------- the algebraic identities

def grid(n, start=2):
    out, k = [], start
    while len(out) < n:
        out.append(F(k, k + 1) + k)
        k += 1
    return out


def ob_energy_expansion():
    """-z^2/(2(n-d)^2) + z^2/(2n^2)  ==  -z^2 d (2n - d) / (2 n^2 (n - d)^2), as a polynomial
    identity after clearing 2 n^2 (n-d)^2: degree 2 in n, 2 in d, 2 in z -> grid 4 x 4 x 4."""
    pts = 0
    for n in grid(4):
        for d in grid(4, 7):
            for z in grid(4, 11):
                lhs = (-z * z / (2 * (n - d) ** 2) + z * z / (2 * n * n)) * 2 * n * n * (n - d) ** 2
                rhs = -z * z * d * (2 * n - d)
                if lhs != rhs:
                    return pts, False
                pts += 1
    return pts, True


def ob_ritz_vs_n2():
    """d2/(n-d0)^2 - d2/n^2  ==  d2 d0 (2n - d0) / (n^2 (n-d0)^2): the Ritz denominator differs
    from 1/n^2 by a term of order d0 d2, second order in the polarisability (Lemma 3).
    Cleared of n^2 (n-d0)^2 it is polynomial: degree 2 in n, 3 in d0, 1 in d2 -> grid 4 x 5 x 3."""
    pts = 0
    for n in grid(4):
        for d0 in grid(5, 7):
            for d2 in grid(3, 13):
                lhs = (d2 / (n - d0) ** 2 - d2 / (n * n)) * n * n * (n - d0) ** 2
                rhs = d2 * d0 * (2 * n - d0)
                if lhs != rhs:
                    return pts, False
                pts += 1
    return pts, True


def seaton_coeffs(alpha, z, l):
    """First-order polarisation defect delta(n) = c0 + c2 / n^2 with
    c0 = 6 alpha z^2 / K(l),  c2 = -2 alpha z^2 l(l+1) / K(l).  (Theorem 1.)"""
    c0 = 6 * alpha * z * z / F(K(l))
    c2 = -2 * alpha * z * z * l * (l + 1) / F(K(l))
    return c0, c2


def ob_ratio_identity():
    """delta(n) = (alpha/2) z^2 n^3 <r^-4>_n  ==  c0 + c2/n^2 with c2/c0 = -l(l+1)/3, for every
    (n, l) in the exhausted family, on a grid of alpha and z above the degree (1 and 2)."""
    fam = 0
    for n in range(2, 21):
        for l in range(1, n):
            r4 = r4_formula(n, l)
            for alpha in grid(3):
                for z in grid(4, 9):
                    c0, c2 = seaton_coeffs(alpha, z, l)
                    lhs = alpha / 2 * z * z * n ** 3 * r4
                    if lhs != c0 + c2 / (n * n):
                        return fam, False
                    if 3 * c2 != -l * (l + 1) * c0:
                        return fam, False
                    fam += 1
    return fam, True


# ------------------------------------------------------------------ Z3 obligations

def ob_z3(lmax=8, wrong=False):
    """For each l in {1..8}: for ALL real alpha, z:  3 c2 = -l(l+1) c0;  and
    alpha > 0, z != 0  =>  c0 > 0 and c2 < 0.  Negation asserted, unsat expected.
    Guards: non-vacuity (the hypothesis alpha > 0, z != 0 is satisfiable) and encoding
    fidelity (the Z3 terms, evaluated at 200 random rationals, equal seaton_coeffs)."""
    prover = _load("prover", PROVER)
    prover.require_z3()
    import z3
    a, z = z3.Reals("alpha z")
    results = []
    for l in range(1, lmax + 1):
        Kl = K(l)
        c0 = 6 * a * z * z / Kl
        c2 = -2 * a * z * z * l * (l + 1) / Kl
        target = -l * (l + 1) if not wrong else -l * (l + 1) * 2
        claim = z3.And(3 * c2 == target * c0, z3.Implies(z3.And(a > 0, z != 0), z3.And(c0 > 0, c2 < 0)))
        s = z3.Solver()
        s.add(z3.Not(claim))
        r = s.check()
        results.append(r == z3.unsat)
    # guard 1: non-vacuity
    s = z3.Solver(); s.add(z3.And(a > 0, z != 0))
    nonvac = s.check() == z3.sat
    # guard 2: encoding fidelity against the Fraction implementation
    rnd = random.Random(5)
    compared = disagree = 0
    for _ in range(200):
        l = rnd.randint(1, lmax)
        av = F(rnd.randint(-50, 50), rnd.randint(1, 9))
        zv = F(rnd.randint(-6, 6), rnd.randint(1, 3))
        Kl = K(l)
        e0 = z3.simplify(z3.substitute(6 * a * z * z / Kl, (a, z3.RealVal(str(av))), (z, z3.RealVal(str(zv)))))
        e2 = z3.simplify(z3.substitute(-2 * a * z * z * l * (l + 1) / Kl, (a, z3.RealVal(str(av))), (z, z3.RealVal(str(zv)))))
        f0, f2 = seaton_coeffs(av, zv, l)
        compared += 1
        if F(e0.as_fraction()) != f0 or F(e2.as_fraction()) != f2:
            disagree += 1
    return all(results), nonvac, compared, disagree


def ob_prefactor():
    """The prefactor identity behind Theorem 1's displayed constant:
        6 / K(l)  ==  (3/4) / [ (l-1/2) l (l+1/2) (l+1) (l+3/2) ],
    and its large-l limit l^5 * 6/K(l) -> 3/4 from below.  Exact, every l in 1..200."""
    fam = 0
    ok = True
    for l in range(1, 201):
        lhs = F(6, K(l))
        rhs = F(3, 4) / ((F(l) - F(1, 2)) * l * (F(l) + F(1, 2)) * (l + 1) * (F(l) + F(3, 2)))
        if lhs != rhs:
            ok = False
        fam += 1
    tail = [F(l) ** 5 * F(6, K(l)) for l in (10, 50, 200)]
    mono = all(a < b for a, b in zip(tail, tail[1:])) and all(t < F(3, 4) for t in tail)
    return fam, ok and mono, float(tail[-1])


def ob_limit_sensitivity():
    """A shift dI in the ionisation limit moves the defect by about n*^3 dI / (2 z^2 R_M).
    Checked against the exact recomputation on every level of every series, at dI = 0.01 cm^-1:
    the predicted and the recomputed shift agree to better than 1 part in 10^4."""
    series, Rinf, mp = load_series()
    worst = 0.0
    tot = 0
    for ser in series:
        RM = Decimal(repr(Rinf)) / (1 + 1 / (Decimal(repr(ser["A"])) * Decimal(repr(mp))))
        for n in sorted(ser["levels"]):
            E = Decimal(repr(ser["levels"][n]))
            I = Decimal(repr(ser["lim"]))
            dI = Decimal("0.01")
            ns0 = Decimal(ser["c"]) * dec_sqrt(RM / (I - E))
            ns1 = Decimal(ser["c"]) * dec_sqrt(RM / (I + dI - E))
            actual = (Decimal(n) - ns1) - (Decimal(n) - ns0)          # change in delta
            pred = ns0 ** 3 * dI / (2 * Decimal(ser["c"]) ** 2 * RM)
            worst = max(worst, abs(float((actual - pred) / pred)))
            tot += 1
    return tot, worst


def ob_separating_cores():
    """The sample cannot separate "p = 0" from "l >= 3", but cores that do separate them exist:
    an argon-like core (18 electrons) holds no d orbital, so p = 0 at l = 2, where the
    krypton-like core of this sample has p = 1; and a core with a filled f subshell has
    p = 1 at l = 3.  Read from the same observed ground configurations as D3."""
    pop = _load("populate", POPULATE)
    ar_d = pop.core_p(18, 2)           # Ca II nd converges on Ca2+, argon-like
    kr_d = pop.core_p(36, 2)           # Sr II nd converges on Sr2+, krypton-like
    f_core = [ne for ne in range(60, 80) if pop.core_p(ne, 3) == 1]
    return ar_d, kr_d, len(f_core)


# -------------------------------------------------------------- the classification

def ob_p_table():
    pop = _load("populate", POPULATE)
    cores = {"Cd I": 47, "In I": 48, "Rb I": 36, "Sr II": 36}   # Z - charge
    table = {}
    for sp, ne in cores.items():
        table[sp] = {l: pop.core_p(ne, l) for l in range(0, 4)}
    expect = {"Cd I": {0: 5, 1: 3, 2: 2, 3: 0}, "In I": {0: 5, 1: 3, 2: 2, 3: 0},
              "Rb I": {0: 4, 1: 3, 2: 1, 3: 0}, "Sr II": {0: 4, 1: 3, 2: 1, 3: 0}}
    ok = table == expect
    FIGURES["p_table"] = table
    # on these four cores p = 0 iff l >= 3 (the sample cannot separate p from l)
    same = all((table[sp][l] == 0) == (l >= 3) for sp in cores for l in range(4))
    FIGURES["p_iff_l3"] = same
    return ok, same, table


# ------------------------------------------------------------- the quantum defects

def dec_sqrt(x):
    return Decimal(x).sqrt()


def defects(ser, Rinf, mp):
    """delta_n = n - c sqrt(R_M / (I - E_n)),  R_M = R_inf / (1 + 1/(A m_p)).  Exact
    rationals except the one square root, taken to 40 significant digits."""
    RM = Decimal(repr(Rinf)) / (1 + 1 / (Decimal(repr(ser["A"])) * Decimal(repr(mp))))
    out = []
    for n in sorted(ser["levels"]):
        E = Decimal(repr(ser["levels"][n]))
        I = Decimal(repr(ser["lim"]))
        nstar = ser["c"] * dec_sqrt(RM / (I - E))
        out.append((n, F(n) - F(nstar)))
    return out, RM


def profile_fit(pts, ritz=True):
    """Least squares for delta(n) = d0 + d2 / (n - d0)^2  (ritz=True) or d0 + d2 / n^2.
    For fixed d0 the model is linear in d2, so d2*(d0) is exact and S(d0) is a rational
    function; the minimiser is located by an exact scan, then a ternary search in exact
    rationals, and certified: S at the minimiser is below S at every scanned point and at
    both ends of the final bracket."""
    ns = [F(n) for n, _ in pts]
    ds = [d for _, d in pts]

    def S_and_d2(d0):
        w = [1 / (n - d0) ** 2 if ritz else 1 / (n * n) for n in ns]
        r = [d - d0 for d in ds]
        d2 = sum(ri * wi for ri, wi in zip(r, w)) / sum(wi * wi for wi in w)
        S = sum((ri - d2 * wi) ** 2 for ri, wi in zip(r, w))
        return S, d2

    lo, hi = min(ds) - 1, max(ds) + 1
    if hi >= min(ns) - F(1, 2):
        hi = min(ns) - F(1, 2)
    steps = 400
    best = None
    scanned = []
    for i in range(steps + 1):
        d0 = lo + (hi - lo) * i / steps
        S, _ = S_and_d2(d0)
        scanned.append((d0, S))
        if best is None or S < best[1]:
            best = (d0, S)
    h = (hi - lo) / steps
    a, b = best[0] - h, best[0] + h
    # ternary search, exact
    for _ in range(90):
        m1 = a + (b - a) / 3
        m2 = b - (b - a) / 3
        if S_and_d2(m1)[0] <= S_and_d2(m2)[0]:
            b = m2
        else:
            a = m1
    d0 = (a + b) / 2
    S, d2 = S_and_d2(d0)
    certified = all(S <= s for _, s in scanned) and S <= S_and_d2(a)[0] and S <= S_and_d2(b)[0]
    # count the local minima on the scan, so a second basin would be reported
    basins = 0
    for i in range(1, len(scanned) - 1):
        if scanned[i][1] < scanned[i - 1][1] and scanned[i][1] < scanned[i + 1][1]:
            basins += 1
    return d0, d2, S, certified, basins, float(b - a)


def capture_levels(species):
    """Every (n, l-symbol, energy) the species' NIST ASD capture file holds, as strings."""
    out = set()
    for line in open(CAPTURE[species], encoding="utf-8"):
        if line.startswith("#") or not line.strip():
            continue
        f = line.rstrip("\n").split("\t")
        cfg = f[0].split(".")[-1]
        import re
        m = re.match(r"(\d+)([spdfgh])$", cfg)
        if not m:
            continue
        val = f[3].strip("[]")
        try:
            out.add((int(m.group(1)), m.group(2), float(val)))
        except ValueError:
            pass
    return out


def ob_captures(rows):
    """Each level the instrument tabulates occurs, at the same n and l, in the species'
    capture file -- a second copy of the same NIST retrieval held in the tree."""
    tot = 0
    missing = []
    for r in rows:
        cap = capture_levels(r["species"])
        for n, E in r["levels"].items():
            tot += 1
            if (n, r["lsym"], E) not in cap:
                missing.append((r["name"], n, E))
    return tot, missing


# the source's own printed fit, (d0, d2), four decimals, as the instrument printed it
SOURCE_FIT = {
    "Cd I f": (0.0393, -0.1808), "In I f": (0.0416, -0.1838), "Sr II f": (0.0648, -0.4054),
    "Rb I d": (1.3504, -0.7418), "Sr II d": (1.4514, 0.5152), "Cd I d": (2.0837, 0.1403),
    "In I d": (2.3009, -1.0075), "Cd I p": (3.0522, -0.0082), "Rb I p": (2.6540, 0.3258),
    "Rb I s": (3.1308, 0.1980), "Sr II s": (2.7055, 0.3394), "Cd I s": (3.6551, 0.3354),
    "In I s": (3.7193, 0.3168),
}
SOURCE_STAT = {"p0_median": 1.150, "p0_sd": 0.206, "p1_median": -0.015, "p1_sd": 0.177,
               "p0_series": 3, "p1_series": 10}
# the channel table's Cd I rows (species, series, n-range, members, median delta, spread, limit)
SOURCE_CDI = {"d": ("nd 3D J=1", (5, 11), 7, 2.0898, 0.0049), "f": ("nf 3F* J=3", (4, 10), 7, 0.0346, 0.0034),
              "s": ("ns 3S J=1", (6, 16), 11, 3.6677, 0.0188), "p": ("np 1P* J=1", (6, 12), 7, 3.0515, 0.0005)}


def r3(x):
    return round(float(x), 3)


def r4(x):
    return round(float(x), 4)


def pstdev(xs):
    m = sum(xs) / len(xs)
    return math.sqrt(float(sum((x - m) ** 2 for x in xs) / len(xs)))


def sstdev(xs):
    m = sum(xs) / len(xs)
    return math.sqrt(float(sum((x - m) ** 2 for x in xs) / (len(xs) - 1)))


def run_fits(perturb=None):
    series, Rinf, mp = load_series()
    pop = _load("populate", POPULATE)
    cores = {"Cd I": 47, "In I": 48, "Rb I": 36, "Sr II": 36}
    rows = []
    for ser in series:
        if perturb and ser["name"] == perturb[0]:
            ser = dict(ser, levels=dict(ser["levels"]))
            ser["levels"][perturb[1]] += perturb[2]
        pts, RM = defects(ser, Rinf, mp)
        if len(pts) < 4:
            continue
        d0, d2, S, cert, basins, width = profile_fit(pts)
        d0n, d2n, Sn, certn, _, _ = profile_fit(pts, ritz=False)
        l = ser["l"]
        p = pop.core_p(cores[ser["species"]], l)
        seat = F(-l * (l + 1), 3)
        rho = (d2 / d0) / seat if seat != 0 else None
        rho_n2 = (d2n / d0n) / seat if seat != 0 else None
        rows.append(dict(name=ser["name"], species=ser["species"], l=l, lsym=ser["lsym"], p=p, c=ser["c"],
                         A=ser["A"], lim=ser["lim"], RM=RM, n_lo=pts[0][0], n_hi=pts[-1][0], members=len(pts),
                         pts=pts, d0=d0, d2=d2, rms=math.sqrt(float(S) / len(pts)), certified=cert,
                         basins=basins, width=width, seat=seat, rho=rho, d0_n2=d0n, d2_n2=d2n, rho_n2=rho_n2,
                         levels=ser["levels"]))
    return rows


def stats(rows):
    p0 = [r for r in rows if r["p"] == 0]
    p1 = [r for r in rows if r["p"] >= 1]
    p0r = [r["rho"] for r in p0 if r["rho"] is not None]
    p1r = [r["rho"] for r in p1 if r["rho"] is not None]
    out = dict(p0_series=len(p0), p1_series=len(p1), p0_defined=len(p0r), p1_defined=len(p1r),
               p0_median=statistics.median(p0r), p0_sd=pstdev(p0r), p0_mean=sum(p0r) / len(p0r), p0_ssd=sstdev(p0r),
               p1_median=statistics.median(p1r), p1_sd=pstdev(p1r), p1_mean=sum(p1r) / len(p1r), p1_ssd=sstdev(p1r),
               p0_min=min(p0r), p0_max=max(p0r), p1_min=min(p1r), p1_max=max(p1r),
               p0_rho=p0r, p1_rho=p1r)
    p1n = [r["rho_n2"] for r in p1 if r["rho_n2"] is not None]
    p0n = [r["rho_n2"] for r in p0 if r["rho_n2"] is not None]
    out.update(p0_median_n2=statistics.median(p0n), p0_sd_n2=pstdev(p0n),
               p1_median_n2=statistics.median(p1n), p1_sd_n2=pstdev(p1n))
    # leave-one-out on the p = 0 class
    loo = []
    for i in range(len(p0r)):
        rest = p0r[:i] + p0r[i + 1:]
        loo.append(statistics.median(rest))
    out["p0_loo"] = loo
    # sign rule
    sign = {}
    for r in rows:
        sign.setdefault(r["p"], [0, 0])
        sign[r["p"]][0 if r["d2"] > 0 else 1] += 1
    out["sign"] = sign
    return out


# ------------------------------------------------------------------------- main

def main(selftest=False):
    print("papers/method/04-seaton -- check.py")
    print()
    allok = True

    # 1  <r^-4>
    fam, bad = ob_r4()
    allok &= report("EXHAUSTIVE", "Lemma 1: <r^-4> closed form", bad == 0,
                    "%d states (n <= %d, 1 <= l <= n-1), %d disagree" % (fam, FIGURES["r4_nmax"], bad))
    fam2, bad2 = ob_r2_sanity()
    allok &= report("EXHAUSTIVE", "control: <r^-2> = 1/(n^3 (l+1/2))", bad2 == 0, "%d states, %d disagree" % (fam2, bad2))

    # 2  energy expansion
    pts, ok = ob_energy_expansion()
    allok &= report("PROVED", "Lemma 2: exact energy-defect identity", ok, "grid 4x4x4 above degree (2,2,2), %d points" % pts)

    pts3, ok3b = ob_ritz_vs_n2()
    allok &= report("PROVED", "Lemma 3: Ritz denominator vs 1/n^2, exact identity", ok3b, "grid 4x5x3 above degree (2,3,1), %d points" % pts3)

    famp, okp, tail = ob_prefactor()
    allok &= report("EXHAUSTIVE", "Theorem 1's prefactor 6/K(l) = (3/4)/[(l-1/2)l(l+1/2)(l+1)(l+3/2)]", okp,
                    "%d values of l, exact; l^5 6/K(l) rises to %.6f < 3/4 at l = 200" % (famp, tail))

    # 3  ratio identity
    fam3, ok3 = ob_ratio_identity()
    allok &= report("PROVED", "Theorem 1: c2/c0 = -l(l+1)/3", ok3, "%d (n,l,alpha,z) grid points, exact" % fam3)
    FIGURES["ratio_grid"] = fam3

    # 4  Z3
    z3ok, nonvac, compared, disagree = ob_z3()
    allok &= report("MACHINE-CHECKED", "Theorem 1 over l in {1..8}, alpha, z real", z3ok and nonvac and disagree == 0,
                    "8 obligations unsat; non-vacuity %s; encoding %d compared, %d disagree"
                    % ("ok" if nonvac else "FAIL", compared, disagree))

    # 5  p table
    okp, same, table = ob_p_table()
    allok &= report("EXHAUSTIVE", "D3: p for the four cores from the ground configurations", okp,
                    "; ".join("%s %s" % (sp, [table[sp][l] for l in range(4)]) for sp in table))
    allok &= report("EXHAUSTIVE", "on these cores p = 0 iff l >= 3, over l in {0,1,2,3}", same, "16 (core, l) cells")
    ar_d, kr_d, nf = ob_separating_cores()
    allok &= report("EXHAUSTIVE", "cores that WOULD separate p = 0 from l >= 3 exist, and none is here",
                    ar_d == 0 and kr_d == 1 and nf > 0,
                    "argon-like core (18 e): p = %d at l = 2, against %d for the krypton-like core here; "
                    "%d cores in 60-79 e have p = 1 at l = 3" % (ar_d, kr_d, nf))

    # 6  the fits
    rows = run_fits()
    FIGURES["rows"] = rows
    allok &= report("EXHAUSTIVE", "thirteen series loaded", len(rows) == 13, "%d series, %d levels" % (len(rows), sum(r["members"] for r in rows)))
    FIGURES["levels_total"] = sum(r["members"] for r in rows)
    _, Rinf_v, mp_v = load_series()
    pop_c = _load("populate", POPULATE)
    print()
    print("      Table 1 -- R_inf = %s cm^-1, m_p/m_e = %s; R_M = R_inf / (1 + 1/(A m_p/m_e))" % (Rinf_v, mp_v))
    print("      %-9s %-22s %2s %2s %2s %6s %3s %12s %8s %12s" %
          ("series", "core ground config", "l", "p", "z", "n", "N", "I (cm^-1)", "A", "R_M (cm^-1)"))
    cfgmap = {"Cd I": 47, "In I": 48, "Rb I": 36, "Sr II": 36}
    cfgtxt = {}
    for sp, ne in cfgmap.items():
        cfg = pop_c.config_of(ne, "observed")
        cfgtxt[sp] = " ".join("%d%s%d" % (n, "spdfg"[l], o) for n, l, o in cfg)
    short = {sp: (t.replace("1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6", "[Kr]")) for sp, t in cfgtxt.items()}
    for r in sorted(rows, key=lambda r: (r["p"], r["l"], r["name"])):
        print("      %-9s %-22s %2d %2d %2d %2d-%-3d %3d %12.3f %8s %12.3f" %
              (r["name"], short[r["species"]], r["l"], r["p"], r["c"], r["n_lo"], r["n_hi"], r["members"],
               r["lim"], r["A"], r["RM"]))
    print("      core ground configurations in full:")
    for sp in sorted(cfgtxt):
        print("        %-6s (%d electrons)  %s" % (sp, cfgmap[sp], cfgtxt[sp]))
    certs = all(r["certified"] for r in rows)
    basins = max(r["basins"] for r in rows)
    allok &= report("EXHAUSTIVE", "each least-squares minimiser certified", certs,
                    "401-point exact scan + 90 ternary steps; bracket width <= %.1e; max local minima on scan %d"
                    % (max(r["width"] for r in rows), basins))
    print()
    print("      %-9s %2s %2s %5s %3s %10s %10s %10s %9s %9s %10s" % ("series", "l", "p", "n", "N", "d0", "d2", "d2/d0", "Seaton", "rho", "rms"))
    for r in sorted(rows, key=lambda r: (r["p"], r["l"], r["name"])):
        print("      %-9s %2d %2d %2d-%-2d %3d %10.4f %10.4f %10.4f %9.3f %9s %10.5f"
              % (r["name"], r["l"], r["p"], r["n_lo"], r["n_hi"], r["members"], r["d0"], r["d2"], r["d2"] / r["d0"],
                 float(r["seat"]), ("%.3f" % r["rho"]) if r["rho"] is not None else "undef", r["rms"]))
    print()
    nsrc = 0
    for r in rows:
        s0, s2 = SOURCE_FIT[r["name"]]
        if abs(r4(r["d0"]) - s0) <= 0.00011 and abs(r4(r["d2"]) - s2) <= 0.00011:
            nsrc += 1
    allok &= report("SOURCE", "fits agree with the source's printed (d0, d2) to 4 dp", nsrc == 13, "%d of 13" % nsrc)

    # 7  the statistics
    st = stats(rows)
    FIGURES["stats"] = st
    allok &= report("EXHAUSTIVE", "class sizes", st["p0_series"] == 3 and st["p1_series"] == 10,
                    "p = 0: %d series; p >= 1: %d series" % (st["p0_series"], st["p1_series"]))
    allok &= report("EXHAUSTIVE", "ratios defined", st["p0_defined"] == 3 and st["p1_defined"] == 6,
                    "p = 0: %d; p >= 1: %d (the four l = 0 series have Seaton's ratio 0, rho undefined)"
                    % (st["p0_defined"], st["p1_defined"]))
    line = "p = 0: median %.3f, sd %.3f (mean %.3f, sample sd %.3f); p >= 1: median %.3f, sd %.3f (mean %.3f, sample sd %.3f)" % (
        st["p0_median"], st["p0_sd"], st["p0_mean"], st["p0_ssd"], st["p1_median"], st["p1_sd"], st["p1_mean"], st["p1_ssd"])
    okst = (r3(st["p0_median"]) == SOURCE_STAT["p0_median"] and r3(st["p0_sd"]) == SOURCE_STAT["p0_sd"]
            and r3(st["p1_median"]) == SOURCE_STAT["p1_median"] and r3(st["p1_sd"]) == SOURCE_STAT["p1_sd"])
    allok &= report("SOURCE", "the four statistics reproduce (median, population sd)", okst, line)
    print("        p = 0 ratios: %s" % ", ".join("%.3f" % x for x in st["p0_rho"]))
    print("        p >= 1 ratios: %s" % ", ".join("%.3f" % x for x in st["p1_rho"]))
    print("        leave-one-out medians, p = 0: %s" % ", ".join("%.3f" % x for x in st["p0_loo"]))
    print("        with a 1/n^2 denominator instead of 1/(n-d0)^2: p = 0 median %.3f sd %.3f; p >= 1 median %.3f sd %.3f"
          % (st["p0_median_n2"], st["p0_sd_n2"], st["p1_median_n2"], st["p1_sd_n2"]))
    sign = st["sign"]
    print("        sign of d2 by p: %s" % "; ".join("p=%d %d+ %d-" % (p, sign[p][0], sign[p][1]) for p in sorted(sign)))
    signok = sign[0] == [0, 3] and sign[5] == [2, 0] and sign[4] == [2, 0] and all(sign[p] == [1, 1] for p in (1, 2, 3))
    allok &= report("EXHAUSTIVE", "sign rule: 0 of 3 positive at p = 0; 2 of 2 at p = 4 and 5; 1 of 2 at p = 1, 2, 3", signok)
    fr = [sign[p][0] / sum(sign[p]) for p in sorted(sign)]
    allok &= report("EXHAUSTIVE", "positive fraction non-decreasing in p", all(a <= b for a, b in zip(fr, fr[1:])),
                    " ".join("%.2f" % f for f in fr))

    ind = [r for r in rows if r["name"] == "In I d"][0]
    ind_ds = [float(d) for _, d in ind["pts"]]
    rising = all(a < b for a, b in zip(ind_ds, ind_ds[1:]))
    allok &= report("EXHAUSTIVE", "In I d: the one series whose residual is an order above the rest", rising,
                    "rms %.5f against %.5f next largest; defect rises monotonically %.2f (n=%d) to %.2f (n=%d)"
                    % (ind["rms"], max(r["rms"] for r in rows if r["name"] != "In I d"),
                       ind_ds[0], ind["n_lo"], ind_ds[-1], ind["n_hi"]))
    nl, worst = ob_limit_sensitivity()
    allok &= report("EXHAUSTIVE", "limit sensitivity: d(delta) = n*^3 dI / (2 z^2 R_M)", worst < 1e-4,
                    "%d levels, dI = 0.01 cm^-1, worst relative error %.2e" % (nl, worst))

    # 8  the levels against the capture files, and Cd I against the channel table
    print()
    tot, missing = ob_captures(rows)
    # the one level the captures do not hold: Cd I 5p (5s5p 1P*1, 43692.384), below the
    # Cd I capture's first row, which starts at 6s.  Expected, and recorded in SOURCES.md.
    expected_missing = [("Cd I p", 5, 43692.384)]
    allok &= report("EXHAUSTIVE", "levels occur in the species' NIST capture files", missing == expected_missing,
                    "%d levels, %d found; not held: %s" % (tot, tot - len(missing), ", ".join("%s n=%d %.3f" % m for m in missing)))
    FIGURES["capture_found"] = tot - len(missing)
    for r in rows:
        if r["species"] != "Cd I":
            continue
        row = SOURCE_CDI[r["lsym"]]
        ds = [float(d) for _, d in r["pts"]]
        med, mean = statistics.median(ds), sum(ds) / len(ds)
        same_range = (r["n_lo"], r["n_hi"]) == row[1] and r["members"] == row[2]
        note = "n %d-%d, %d members: median %.4f, mean %.4f; channel table %s n %d-%d, %d members, %.4f%s" % (
            r["n_lo"], r["n_hi"], r["members"], med, mean, row[0], row[1][0], row[1][1], row[2], row[3],
            "" if same_range else " (different n-range)")
        if same_range:
            okmean = abs(round(mean, 4) - row[3]) <= 0.00011
            okmed = abs(round(med, 4) - row[3]) <= 0.00011
            allok &= report("SOURCE", "Cd I %s: the channel table's delta is the MEAN of these members" % r["lsym"],
                            okmean, note + "; median %s, mean %s" % ("agrees" if okmed else "differs", "agrees" if okmean else "differs"))
        else:
            print("        Cd I %s: %s" % (r["lsym"], note))

    # -- selftest: negative controls
    if selftest:
        print()
        print("  negative controls (each must be REFUTED):")
        fam, bad = ob_r4(nmax=8, wrong=True)
        allok &= report("REFUTED", "control: wrong <r^-4> (3n^2 + l(l+1)) fails the family", bad > 0, "%d of %d disagree" % (bad, fam))
        z3ok, nonvac, _, _ = ob_z3(lmax=3, wrong=True)
        allok &= report("REFUTED", "control: Z3 finds a model against c2/c0 = -2l(l+1)/3", not z3ok, "sat, as it must be")
        rows_p = run_fits(perturb=("Cd I f", 4, 5.0))
        stp = stats(rows_p)
        moved = r3(stp["p0_median"]) != SOURCE_STAT["p0_median"] or r3(stp["p0_sd"]) != SOURCE_STAT["p0_sd"]
        allok &= report("REFUTED", "control: Cd I 4f raised by 5 cm^-1 moves the p = 0 statistic", moved,
                        "median %.3f sd %.3f" % (stp["p0_median"], stp["p0_sd"]))

    print()
    n = len(RESULTS)
    nok = sum(1 for r in RESULTS if r[2])
    print("%d of %d obligations discharged%s" % (nok, n, "" if allok else " -- FAILURES ABOVE"))
    return 0 if allok else 1


if __name__ == "__main__":
    sys.exit(main("--selftest" in sys.argv))
