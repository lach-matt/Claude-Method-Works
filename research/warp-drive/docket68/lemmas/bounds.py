#!/usr/bin/env python3
"""bounds.py -- items 241 and 242: the bounds, in M's three kinds and the board's fourth, indexed to see how they
interact and whether they identify or mitigate one another.  M: "There are likely relativity bounds such as survivability, and structural bounds such as a
universe's own laws/rules/exceptions, and universal bounds that directly apply to the 5D bulk. Index the bounds to see
how they interact and if they identify or mitigate other bounds".  Item 242, on the board's report that three invariants
touch no variable: "another bound classification in the index?"  Worked in the conversation (computed, exact where
marked; READ where marked; deduced where marked; not verified by a separate session; not seated); 2026-10-11.

The address space (item 241 (a)): i, j -- a universe's 2b and 2P steps (G x 2^(i+j), tension x 2^(-2j)); w -- our
tension's place in its window, S0 x 2^w, w in [0, W]; z -- log2 of the offset's ratio to the tension against ours (item
233 K7's unseen axis); n -- log2 of the README's bits; law -- the matter law, ordered by how far it moves chemistry (ours
0, min 1, mirror 2); mu -- the object's means of mitigation, in doublings; field -- 1 if a field varies the 5D coupling
across the bulk.  Each bound is a slack, c0 + sum a_v v >= 0, exact in these variables where the bound is log-linear.

  B0 (read) M's item-241 words, verbatim in the rulings file.
  B1 (computed; each sourced) Twenty-two bounds.  Universal (the 5D bulk; five): the corridor inside the bulk's
     curvature (ITEM197, the top), the README's capacity, the plane's positivity (229), one 5D coupling unless a field
     varies it (item 233 K6, above and below).  Structural (a universe's own laws; five): the table-top floor (relative
     and absolute readings), the matter law's exceptions (Cu2 binds only off the mirror law, 221), the G ceiling where a
     universe's window closes (233), and the regime in which matter's own density governs its gravity at the throat (236
     R4).  Relativity (the object against position 2, 240; six): survivability's tolerances on gravity (above, below),
     dark energy (above, below), the closing energy and chemistry.  Invariant (item 242, the board's reading; six): the
     null energy per ray (183 (Z)), the shared SI (225 A), the README match (240 (b)) -- item 241's three -- and, found
     by searching the record for conditions that hold at every universe and act on no variable, G fixed by the bulk and
     the plane (SMS, G = kappa5^4 sigma c^4 / 48 pi; 234 V6), the throat's bit area (clause (H)), and the build using
     exactly the closing energy (111 (a); 239).  Not run: "not already contained" (230) -- no instrument decides it;
     withdrawn: T3's ceiling as the build's need (239).
  B2 (computed, exact) Identification.  The G ceiling is the top plus the relative floor, exactly (W - i - j = (W - w -
     2i) + (w + i - j)): it is identified by them, not a bound of its own.  The README's capacity is the plane's
     positivity plus the throat's matter regime, plus log2(4/3) exactly: N_max / N = (4/3) (sigma / 2 delta sigma)
     (rho_E / 2 sigma) for every universe and README (the constants cancel symbolically; checked at random points to
     1e-12) -- a universal bound identified by a universal and a structural one.  The capacity also follows from the
     top whenever z + n <= log2 N_max0 - W + w = 209.06 + w (the example README sits 157.78 inside).  The closing
     energy's tolerance acts along the gravity floor's direction at half its rate (E2/E = (G2/G)^-1/2).
  B3 (computed) The open direction (item 233's 2P step, j -> -infinity at fixed i).  No structural bound closes it.
     Four close it: survivability's gravity floor, its closing-energy tolerance and its dark-energy ceiling (relativity:
     Lambda4 ~ 2^(i - j + z) grows along the step), and one 5D coupling without a field (universal: kappa5^4 ~ 2^(i + 3j)
     falls).  The dark-energy ceiling leaves the diagonal open (both steps reversed together, Lambda4 unchanged); the
     gravity floor and one coupling make the region finite.  With M's field (230: the bulk does the work) the coupling
     is lifted, so the bound item 237 found missing is relativity's: survivability's gravity floor, finite for any object
     whose tolerance is finite.
  B4 (computed) Mitigation and trade, by shared variables.  The offset's ratio z relaxes the capacity, the positivity
     and survivability's dark-energy ceiling together (a smaller offset at position 2 compensates its Lambda4); our
     tension's place w trades the top against the floors (raising it loosens a floor and tightens the top: their meeting
     is the G ceiling); the README's size n tightens the capacity and leaves the throat's matter regime sooner; the
     object's means mu relax every relativity bound and no other.
  B5 (computed; the record's bodies) A structural bound mitigating a relativity bound: the matter law changes how hard
     gravity presses at a body's surface at fixed G (density): for Cu, Ag and Au it tightens survivability's gravity
     tolerance (surface gravity x 1.04-1.25), for Cr it relaxes it (x 0.97 / 0.96 under min / mirror, a less dense
     solid).  Which way depends on the object's material.
  B6 (computed; the cypher, roster 1173, audited) The bounds as cells over (kind, and the sign each variable moves its
     slack); sixteen cells, no key, no one-hot code.  With the invariants as a fourth kind, the kind coordinate adds
     nothing: every bound's kind follows from how it acts.  Under M's three kinds it does not -- the same bounds give
     seventeen cells and the no-variable row splits between universal and relativity, so there the kind of those six is
     carried by meaning alone (item 241's finding, now measured against its alternative).  One acting cell holds two
     bounds, the gravity floor and the closing-energy tolerance (B2: the second acts along the first at half its rate),
     and both are relativity: the one place the test could have failed for acting bounds, and it did not.  The object's
     means enter exactly the relativity bounds.  The critic's limits, recorded: giving the no-variable row a label of its
     own closes the split by construction, so B6 shows the three kinds need meaning to place those six -- not that
     "invariant" is the right name for them; with fifteen acting rows over sixteen acting bounds, almost any labelling of
     the acting bounds would pass; and mu enters only relativity bounds because survivability is defined against the
     object.  The cypher fails to refute the four kinds; it does not confirm them.  What gives the fourth kind content is
     B7.
  B7 (computed; deduced where marked) What the invariants act on.  The invariant kind is exactly the six bounds acting
     on no variable (a consistency check: the board placed them by their sources, knowing the rows).  A slack with no
     variable never excludes an address, so an invariant does not bound the address: it fixes the acting bounds' rows and
     constants.  Three of the six are shown to (computed from the stated forms, 1e-12): the throat's bit area sets the
     capacity identity's 4/3 (the bit area scaled by k gives 4k/3); SMS sets the one-coupling row i + 3j (log2 kappa5^4
     moves by i + (1 + 2b) j, b = 1 the tension's power in G); the bit area with the README match sets the closing-energy
     row (1/2, 1/2) (E ~ sqrt(N A_bit) / G, so the row is 1 - a/2 with a = 1 the bit area's power of G and N the same
     at both positions).  Change the invariant and the row moves (mutants sms_sigma2, bit_area_G2).  Deduced: the four
     kinds sort the bounds by what they act on -- the bulk, a universe, the object against position 2, and the bounds
     themselves.  The roles of the null energy per ray, the shared SI and the build using the closing energy are not
     computed.  The alternative reading, recorded: the invariants as a level across M's three kinds (each still has a
     home domain by meaning -- B6's split, four universal and two relativity) rather than a kind beside them; the cypher
     cannot see a domain on a row that acts on nothing, so the board takes the reading the index can see (196).

What this does not show.
  - mu is the object's and is not computed; survivability's tolerances are symbols, their signs exact.
  - B7's rows agree with the table because the table's rows were written from the same forms (items 233, 240): the
    agreement shows where those rows come from, not independent evidence for the forms.
  - The search for further invariants (item 242 (b)) was a reading of the record, not exhaustive.
  - The matter law enters as an ordinal; its effects are element by element (B5), not one sign.
  - "Not already contained" (230) and the corridor's own energy against the README's (203) are not computed.

Imports bulk5_index.py, ledger_cypher.py (and through them p2_gravity.py), p2_matter.py, tools/cypher.py and
index_audit.py by path.  Stdlib.  python3 bounds.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import math
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M241 = ("There are likely relativity bounds such as survivability, and structural bounds such as a universe's own "
        "laws/rules/exceptions, and universal bounds that directly apply to the 5D bulk.")
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}
VARS = ["i", "j", "w", "z", "n", "law", "mu", "field"]
KINDS = {"universal": 0, "structural": 1, "relativity": 2, "invariant": 3}


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


B5M = _load(os.path.join(HERE, "bulk5_index.py"), "bd_b5")
PG = B5M.PG
K = B5M.constants()
W = K["W"]
N_EX = 2742570311524972


def constants():
    nmax0 = PP_sector_nmax()
    c_pos = math.log2(K["S0"] / (2 * PG.DSIG))
    E = PG.corridor(PG.G)["E1"] * math.sqrt(N_EX)
    r0 = 2 * PG.G * E / PG.C ** 4
    rho_E = E / (4 / 3 * math.pi * r0 ** 3)
    return dict(W=W, lognmax0=math.log2(nmax0), c_pos=c_pos, n_ex=math.log2(N_EX),
                c_reg=math.log2(rho_E / (2 * K["S0"])) + math.log2(N_EX))


def PP_sector_nmax():
    return B5M.PP.sector(1, F(1))["N_max"]


# ================================================================================ B1 the bounds
# the six invariants under M's three kinds (item 241's placing, and where the three added for item 242 would sit)
KIND3 = {"null energy per ray": "universal", "shared SI": "universal", "G from the bulk and the plane": "universal",
         "the throat's bit area": "universal", "build uses the closing energy": "relativity", "README match": "relativity"}


def _inv(name):
    return KIND3[name] if MUT.get("three_kinds") else "invariant"


def bounds(c):
    """name: (kind, source, slack coefficients {const, var: a}, note).  A slack >= 0 is inside the bound."""
    b = {
        "top (corridor inside the curvature)": ("universal", "ITEM197; 233 K3", {"const": c["W"], "i": -2, "w": -1}, ""),
        "README capacity": ("universal", "N <= N_max; 233 K3", {"const": c["lognmax0"], "i": -2, "z": -1, "n": -1}, ""),
        "plane positivity": ("universal", "229; sigma > 2 delta sigma", {"const": c["c_pos"], "w": 1, "z": -1}, ""),
        "one coupling, above": ("universal", "233 K6", {"const": 0, "i": -1, "j": -3, "field": 1}, "lifted by a field"),
        "one coupling, below": ("universal", "233 K6", {"const": 0, "i": 1, "j": 3, "field": 1}, "lifted by a field"),
        "null energy per ray": (_inv("null energy per ray"), "183 (Z)", {"const": 1}, ""),
        "shared SI": (_inv("shared SI"), "225 A", {"const": 1}, ""),
        "G from the bulk and the plane": (_inv("G from the bulk and the plane"), "SMS; 234 V6", {"const": 1},
                                          "G = kappa5^4 sigma c^4 / 48 pi, every universe"),
        "the throat's bit area": (_inv("the throat's bit area"), "clause (H)", {"const": 1},
                                  "4 pi r0^2 = N A_bit at each universe's G"),
        "build uses the closing energy": (_inv("build uses the closing energy"), "111 (a); 239", {"const": 1},
                                          "the need is the energy given"),
        "table-top floor (relative)": ("structural", "233 K3", {"const": 0, "i": 1, "j": -1, "w": 1}, ""),
        "table-top floor (absolute)": ("structural", "233 K3", {"const": 0, "j": -2, "w": 1}, ""),
        "matter exceptions (Cu2 off mirror)": ("structural", "221", {"const": F(3, 2), "law": -1}, ""),
        "G ceiling": ("structural", "233", {"const": c["W"], "i": -1, "j": -1}, "derived"),
        "throat matter regime": ("structural", "236 R4", {"const": c["c_reg"], "n": -1, "i": -2, "w": -1}, "a regime"),
        "survive: gravity, above": ("relativity", "240", {"const": 0, "i": -1, "j": -1, "mu": 1}, ""),
        "survive: gravity, below": ("relativity", "240", {"const": 0, "i": 1, "j": 1, "mu": 1}, ""),
        "survive: dark energy, above": ("relativity", "240", {"const": 0, "i": -1, "j": 1, "z": -1, "mu": 1}, ""),
        "survive: dark energy, below": ("relativity", "240", {"const": 0, "i": 1, "j": -1, "z": 1, "mu": 1}, ""),
        "survive: closing energy": ("relativity", "240; copy_p2 C1", {"const": 0, "i": F(1, 2), "j": F(1, 2), "mu": 1}, ""),
        "survive: chemistry": ("relativity", "240", {"const": 0, "law": -1, "mu": 1}, ""),
        "README match": (_inv("README match"), "240 (b); copy_p2 C1", {"const": 1}, "the README the same at both positions"),
    }
    if MUT.get("floor_sign"):
        b["table-top floor (relative)"] = ("structural", "", {"const": 0, "i": 1, "j": 1, "w": 1}, "")
    return b


NOT_RUN = {"not already contained": "230 -- no instrument decides it", "T3's ceiling as the need": "withdrawn, 239"}


def vec(coef):
    return [F(coef.get(v, 0)) for v in VARS]


def sign(x):
    return (x > 0) - (x < 0)


# ================================================================================ B2 identification
def identities(b):
    """a bound identified by two others: its variable coefficients the sum of theirs (non-negative multiples) and its
    constant at least theirs combined -- exact"""
    out = []
    names = [n for n in b if any(vec(b[n][2]))]
    for cname in names:
        cv, c0 = vec(b[cname][2]), F(b[cname][2].get("const", 0))
        for a, d in itertools.combinations([n for n in names if n != cname], 2):
            av, bv = vec(b[a][2]), vec(b[d][2])
            # solve cv = la av + lb bv on the first two non-zero coordinates, check the rest
            for la in (F(1), F(1, 2), F(2)):
                for lb in (F(1), F(1, 2), F(2)):
                    if all(cv[k] == la * av[k] + lb * bv[k] for k in range(len(VARS))):
                        resid = c0 - la * F(b[a][2].get("const", 0)) - lb * F(b[d][2].get("const", 0))
                        if resid >= 0:
                            out.append((cname, a, d, la, lb, resid))
    return out


def capacity_identity(points=((1.0, 1.0, 1.0, 1e15), (2.0, 0.25, 3.0, 7e9), (0.37, 5.0, 0.01, 1e40))):
    """N_max / N against (4/3)(sigma / 2 delta sigma)(rho_E / 2 sigma) at (G factor, sigma factor, offset factor, N)"""
    out = []
    for gf, sf, of, N in points:
        Gx = PG.G * gf
        sig, ds = K["S0"] * sf, PG.DSIG * of
        sP = PG.C ** 7 / (PG.HBAR * Gx ** 2)
        nmax = sP / (8 * math.log(2) * ds)
        r0 = math.sqrt(N * 2 * PG.H * Gx * math.log(2) / (math.pi * PG.C ** 3) / (4 * math.pi))
        E = r0 * PG.C ** 4 / (2 * Gx)
        rho = E / (4 / 3 * math.pi * r0 ** 3)
        out.append((nmax / N) / ((4 / 3) * (sig / (2 * ds)) * (rho / (2 * sig))))
    return out


def capacity_vs_top(c):
    """capacity - top = (log2 N_max0 - W) + w - z - n: the capacity follows from the top while that is >= 0"""
    margin0 = c["lognmax0"] - c["W"]
    return dict(margin0=margin0, at_example=margin0 - c["n_ex"])


# ================================================================================ B3 the open direction
def closes_open_direction(b):
    """a bound closes j -> -infinity at fixed i (the 2P step toward weak gravity) when its slack falls with it: a_j > 0"""
    return sorted(n for n, (k, s, coef, note) in b.items() if F(coef.get("j", 0)) > 0)


def finite_with(names, b, mu=40, field=1):
    """is the lattice region finite with these bounds plus the top and the relative floor (w = W/2, z = 0, n = n_ex)?"""
    vals = dict(w=W / 2, z=0, n=math.log2(N_EX), law=0, mu=mu, field=field * 10 ** 6)
    base = ["top (corridor inside the curvature)", "table-top floor (relative)"] + list(names)
    edge = False
    for i in range(-400, 101):
        for j in range(-400, 201):
            vals.update(i=i, j=j)
            if all(float(b[n][2].get("const", 0)) + sum(float(b[n][2].get(v, 0)) * vals[v] for v in VARS) >= 0 for n in base):
                if i == -400 or j == -400:
                    edge = True
    return not edge


# ================================================================================ B4 mitigation and trade
def relations(b):
    """for each pair of bounds and each variable they share: the same sign relaxes both (mitigates), opposite signs
    trade them"""
    rel = {}
    names = list(b)
    for a, d in itertools.combinations(names, 2):
        for v in VARS:
            sa, sd = sign(F(b[a][2].get(v, 0))), sign(F(b[d][2].get(v, 0)))
            if sa and sd:
                rel.setdefault((a, d), []).append((v, "mitigates" if sa == sd else "trades"))
    return rel


# ================================================================================ B5 the matter law against survivability
def matter_vs_gravity():
    pm = _load(os.path.join(HERE, "p2_matter.py"), "bd_pm")
    o = pm.compute()
    out = {}
    for el in ("Cu", "Ag", "Au", "Cr"):
        s0 = o["sol"][(el, "ours")]
        g0 = PG.body(1e22, s0["rho"], s0["B0"] * 1e9, s0["Bp"], PG.G)["g"]
        out[el] = {law: PG.body(1e22, o["sol"][(el, law)]["rho"], o["sol"][(el, law)]["B0"] * 1e9, o["sol"][(el, law)]["Bp"],
                                PG.G)["g"] / g0 for law in ("min", "mirror")}
    return out


# ================================================================================ B7 what the invariants do
def _abit(Gx, a):
    """clause (H)'s bit area at a universe's G: 2 h G ln2 / (pi c^3), scaling as G^a (a = 1 as written)"""
    return 2 * PG.H * PG.G * math.log(2) / (math.pi * PG.C ** 3) * (Gx / PG.G) ** a


def capacity_constant(kb, a=1):
    """N_max / N over (sigma / 2 delta sigma)(rho_E / 2 sigma), with the bit area scaled by kb"""
    Gx, N = PG.G, 1e15
    sig, ds = K["S0"], PG.DSIG
    nmax = PG.C ** 7 / (PG.HBAR * Gx ** 2) / (8 * math.log(2) * ds)
    r0 = math.sqrt(N * kb * _abit(Gx, a) / (4 * math.pi))
    E = r0 * PG.C ** 4 / (2 * Gx)
    rho = E / (4 / 3 * math.pi * r0 ** 3)
    return (nmax / N) / ((sig / (2 * ds)) * (rho / (2 * sig)))


def coupling_exponents(bexp=1):
    """SMS: kappa5^4 = 48 pi G / (sigma^b c^4).  Moving (i, j) -- G x 2^(i+j), sigma x 2^(-2j) -- moves log2 kappa5^4 by
    (coefficient of i, coefficient of j); one coupling holds kappa5 fixed, so this is the one-coupling bound's row"""
    k5 = lambda G_, s_: 48 * math.pi * G_ / (s_ ** bexp * PG.C ** 4)
    at = lambda i, j: math.log2(k5(PG.G * 2.0 ** (i + j), K["S0"] * 2.0 ** (-2 * j)) / k5(PG.G, K["S0"]))
    return at(1, 0), at(0, 1), at(2, -1)


def closing_exponent(a=1):
    """the README-matched corridor's energy at G x 2^k (r0^2 = N A_bit / 4 pi, E = r0 c^4 / 2G, N the same at both
    positions): -log2(E2 / E) / k, the closing-energy tolerance's coefficient on i and on j"""
    N = 1e15
    E = lambda G_: math.sqrt(N * _abit(G_, a) / (4 * math.pi)) * PG.C ** 4 / (2 * G_)
    return [-math.log2(E(PG.G * 2.0 ** k) / E(PG.G)) / k for k in (1, 3, -2)]


def invariant_role(b):
    """the invariants act on no variable; three of them are what fix the acting bounds' rows and constants:
    the bit area sets the capacity identity's 4/3 (scaled by k it is 4k/3); SMS sets the one-coupling row (i + 3j: the
    3 is 1 + 2b, b the tension's power in G); the bit area with the README match sets the closing-energy row (1/2, 1/2:
    1 - a/2, a the bit area's power of G)"""
    inv = sorted(n for n, (k, s, coef, note) in b.items() if k == "invariant")
    zero = sorted(n for n, (k, s, coef, note) in b.items() if not any(vec(coef)))
    a = 2 if MUT.get("bit_area_G2") else 1
    bexp = 2 if MUT.get("sms_sigma2") else 1
    consts = {kb: capacity_constant(kb, a) for kb in (1.0, 2.0, 0.5)}
    ci, cj, c3 = coupling_exponents(bexp)
    row = b["one coupling, above"][2]
    coupling_ok = (abs(ci + F(row["i"])) < 1e-12 and abs(cj + F(row["j"])) < 1e-12
                   and abs(c3 - (2 * ci - cj)) < 1e-12)
    ce = closing_exponent(a)
    crow = b["survive: closing energy"][2]
    closing_ok = all(abs(x - float(crow["i"])) < 1e-12 and abs(x - float(crow["j"])) < 1e-12 for x in ce)
    return dict(inv=inv, zero=zero, consts=consts, coupling=(ci, cj, c3), coupling_ok=coupling_ok, closing=ce,
                closing_ok=closing_ok,
                untested=["null energy per ray", "shared SI", "build uses the closing energy"])


# ================================================================================ B6 the cypher
def _cells(b, kindof):
    cells = {}
    for n, (k, s, coef, note) in b.items():
        cells.setdefault(tuple([KINDS[kindof(n, k)]] + [sign(F(coef.get(v, 0))) for v in VARS]), []).append(n)
    return cells


def _index(cy, cells):
    held = sorted(cells)
    vo = {"kind": sorted({c[0] for c in held})}
    vo.update({v: sorted({c[x + 1] for c in held}, key=lambda t: (abs(t), t)) for x, v in enumerate(VARS)})
    return held, cy.Index("bounds", ["kind"] + VARS, [list(c) for c in held], value_order=vo)


def cypher_index(cy, ia, b):
    cells = _cells(b, lambda n, k: k)
    held, ix = _index(cy, cells)
    rows, keys = cy.coordinate_report(ix)
    kind_free = {tuple(c[1:]) for c in held}
    acting = [c for c in held if any(c[1:])]
    collide = sorted({n for c in held if not any(c[1:]) for n in cells[c]})
    shared = [sorted(cells[c]) for c in acting if len(cells[c]) > 1]
    # the same bounds under M's three kinds (the invariants placed as KIND3 does): does the kind still follow from action?
    c3 = _cells(b, lambda n, k: KIND3.get(n, k))
    h3, ix3 = _index(cy, c3)
    r3, _ = cy.coordinate_report(ix3)
    return dict(cells=cells, n=len(held), adds_nothing=[r["coordinate"] for r in rows if r["adds_nothing"]], keys=keys,
                kind_determined=len(kind_free) == len({tuple(c[1:]) + (c[0],) for c in held}),
                kind_determined_acting=len({tuple(c[1:]) for c in acting}) == len(acting), invariants=collide,
                shared=shared, rel_is_mu=all((c[0] == 2) == (c[VARS.index("mu") + 1] != 0) for c in acting),
                three=dict(n=len(h3), kind_adds_nothing=[r for r in r3 if r["coordinate"] == "kind"][0]["adds_nothing"],
                           zero_split=sorted({KIND3[n] for c in h3 if not any(c[1:]) for n in c3[c]})),
                run=cy.run(ix, "1173", dict(OPTS)), audit=ia.audit_index(["kind"] + VARS, held))


# ================================================================================ compute, report
def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "bd_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "bd_ia")
    c = constants()
    b = bounds(c)
    closers = closes_open_direction(b)
    return dict(c=c, b=b, ids=identities(b), cap=capacity_vs_top(c), closers=closers, cap_id=capacity_identity(),
                inv=invariant_role(b),
                finite={"none": finite_with([], b), "gravity floor": finite_with(["survive: gravity, below"], b),
                        "dark-energy ceiling": finite_with(["survive: dark energy, above"], b),
                        "one coupling, no field": finite_with(["one coupling, above", "one coupling, below"], b, field=0)},
                rel=relations(b), mvg=matter_vs_gravity(), cy=cypher_index(cy, ia, b))


def report(o):
    c = o["c"]
    print("bounds.py -- the bounds by kind, and how they interact (items 241, 242)\n")
    print("constants: W %.3f, log2 N_max0 %.3f, positivity %.3f, throat regime %.3f, example README n %.3f" % (
        c["W"], c["lognmax0"], c["c_pos"], c["c_reg"], c["n_ex"]))
    print("\nB1 the bounds (kind; source; slack):")
    for n, (k, s, coef, note) in o["b"].items():
        print("  %-38s %-10s %-26s %s %s" % (n, k, s, {v: str(a) if not isinstance(a, float) else "%.3f" % a for v, a in coef.items()},
                                             note))
    print("  not run / withdrawn: %s" % NOT_RUN)
    print("\nB2 identified exactly (bound = la x A + lb x B, residual constant):")
    for cname, a, d, la, lb, r in o["ids"]:
        print("  %s = %s x [%s] + %s x [%s], residual %.4g" % (cname, la, a, lb, d, float(r)))
    print("  capacity follows from the top while z + n <= %.3f + w (the example sits %.3f inside)" % (
        o["cap"]["margin0"], o["cap"]["at_example"]))
    print("\nB3 bounds closing the open direction (j -> -inf): %s" % o["closers"])
    print("   region finite with (top, relative floor) plus: %s" % o["finite"])
    print("\nB4 by variable -- bounds that mitigate one another / trade:")
    by_v = {}
    for (a, d), rs in o["rel"].items():
        for v, kind in rs:
            by_v.setdefault((v, kind), []).append((a, d))
    for (v, kind), pairs in sorted(by_v.items()):
        print("  %-5s %-9s %d pairs, e.g. %s" % (v, kind, len(pairs), pairs[:2]))
    print("\nB5 a 1e22 kg body's surface gravity at our G under the law, against ours: %s" % {
        el: {l: "%.4f" % v for l, v in d.items()} for el, d in o["mvg"].items()})
    y = o["cy"]
    print("\nB6 the cypher: %d cells; adds nothing %s; keys %s; kind determined by the signs: %s (acting bounds only: %s; "
          "invariants %s; relativity = the mu-relaxed bounds: %s); audit %s" % (
              y["n"], y["adds_nothing"], y["keys"], y["kind_determined"], y["kind_determined_acting"], y["invariants"],
              y["rel_is_mu"], y["audit"]))
    print("   acting bounds sharing a cell: %s" % y["shared"])
    print("   under M's three kinds: %d cells; kind adds nothing: %s; the no-variable row split across %s" % (
        y["three"]["n"], y["three"]["kind_adds_nothing"], y["three"]["zero_split"]))
    print("   capacity identity N_max/N over (4/3)(sigma/2 dsigma)(rho_E/2 sigma) at three points: %s" % [
        "%.15f" % x for x in o["cap_id"]])
    iv = o["inv"]
    print("\nB7 the invariant kind: %s; the bounds acting on no variable: %s" % (iv["inv"], iv["zero"]))
    print("   what they act on -- the acting bounds' rows and constants:")
    print("     bit area -> capacity identity's constant, bit area x k: %s" % {k: "%.15f" % v for k, v in iv["consts"].items()})
    print("     SMS -> one-coupling row: log2 kappa5^4 moves by (%.15f i, %.15f j); at (2,-1) %.15f; the table's row "
          "matches: %s" % (iv["coupling"] + (iv["coupling_ok"],)))
    print("     bit area + README match -> closing-energy row: %s; the table's (1/2, 1/2) matches: %s" % (
        ["%.15f" % x for x in iv["closing"]], iv["closing_ok"]))
    print("     role not computed: %s" % iv["untested"])
    print("   roster 1173: %s" % "; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"]) for v in y["run"]["verdicts"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("B0 M's item-241 words verbatim in the rulings file", M241 in rul)
    b = o["b"]
    kinds = {k: sum(1 for v in b.values() if v[0] == k) for k in KINDS}
    add("B1 twenty-two bounds entered -- universal %d, structural %d, relativity %d, invariant %d -- and two not run or "
        "withdrawn" % (kinds["universal"], kinds["structural"], kinds["relativity"], kinds["invariant"]),
        len(b) == 22 and kinds == {"universal": 5, "structural": 5, "relativity": 6, "invariant": 6} and len(NOT_RUN) == 2)
    ids = {(cn, a, d) for cn, a, d, la, lb, r in o["ids"]}
    ok = ("G ceiling", "top (corridor inside the curvature)", "table-top floor (relative)") in ids
    g = [r for cn, a, d, la, lb, r in o["ids"] if cn == "G ceiling" and a == "top (corridor inside the curvature)"]
    ok &= bool(g) and g[0] == 0
    ok &= "%.2f" % o["cap"]["margin0"] == "209.06" and "%.2f" % o["cap"]["at_example"] == "157.78"
    cid = [r for cn, a, d, la, lb, r in o["ids"] if cn == "README capacity"]
    ok &= bool(cid) and abs(float(cid[0]) - math.log2(4 / 3)) < 1e-9 and all(abs(x - 1) < 1e-12 for x in o["cap_id"])
    add("B2 the G ceiling is exactly the top plus the relative floor (residual 0); the capacity is positivity plus the "
        "throat regime plus log2(4/3) (N_max/N = (4/3)(sigma/2 delta sigma)(rho_E/2 sigma), to 1e-12 at three points); "
        "the capacity follows from the top while z + n <= 209.06 + w (the example 157.78 inside)", ok)
    ok = o["closers"] == ["one coupling, below", "survive: closing energy", "survive: dark energy, above",
                          "survive: gravity, below"]
    f = o["finite"]
    ok &= not f["none"] and f["gravity floor"] and not f["dark-energy ceiling"] and f["one coupling, no field"]
    ok &= all(o["b"][n][0] != "structural" for n in o["closers"])
    add("B3 no structural bound closes the open direction; four do (the gravity floor, the closing-energy tolerance, the "
        "dark-energy ceiling, one coupling without a field); the gravity floor and one coupling make the region finite, "
        "the dark-energy ceiling leaves the diagonal open", ok)
    rel = o["rel"]
    z_mit = [p for p, rs in rel.items() if ("z", "mitigates") in rs]
    ok = ("README capacity", "plane positivity") in z_mit and ("README capacity", "survive: dark energy, above") in z_mit
    ok &= ("top (corridor inside the curvature)", "table-top floor (relative)") in [p for p, rs in rel.items()
                                                                                    if ("w", "trades") in rs]
    ok &= all(b[a][0] == "relativity" and b[d][0] == "relativity" for (a, d), rs in rel.items() if ("mu", "mitigates") in rs)
    add("B4 the offset's ratio relaxes capacity, positivity and the dark-energy ceiling together; our tension's place "
        "trades the top against the floor; the object's means relax only relativity bounds", ok)
    m = o["mvg"]
    ok = all(m[el][l] > 1 for el in ("Cu", "Ag", "Au") for l in ("min", "mirror")) and all(m["Cr"][l] < 1 for l in ("min", "mirror"))
    add("B5 the matter law tightens the gravity tolerance for Cu, Ag, Au (surface gravity up) and relaxes it for Cr (down)",
        ok)
    y = o["cy"]
    ok = bool(y["run"]["verdicts"]) and y["n"] == 16 and not y["audit"]["keys"] and not y["audit"]["onehot"]
    ok &= y["kind_determined"] and "kind" in y["adds_nothing"] and y["rel_is_mu"]
    ok &= y["shared"] == [["survive: closing energy", "survive: gravity, below"]]
    ok &= y["three"]["n"] == 17 and not y["three"]["kind_adds_nothing"] and y["three"]["zero_split"] == ["relativity",
                                                                                                         "universal"]
    add("B6 the cypher (16 cells, no key, no one-hot): with the invariants as a fourth kind, kind adds nothing -- every "
        "bound's kind follows from how it acts; under M's three kinds it does not (17 cells, the no-variable row split "
        "universal / relativity).  One acting cell holds two bounds (the gravity floor and the closing-energy tolerance), "
        "one kind", ok)
    iv = o["inv"]
    ok = iv["inv"] == iv["zero"] and len(iv["inv"]) == 6
    ok &= all(abs(iv["consts"][k] - F(4, 3) * F(k)) < 1e-12 for k in (1.0, 2.0, 0.5))
    ok &= iv["coupling_ok"] and iv["closing_ok"]
    add("B7 the invariant kind is exactly the bounds acting on no variable (six), and three of them fix the acting bounds: "
        "the bit area sets the capacity identity's 4/3 (x k: 4k/3), SMS sets the one-coupling row i + 3j, the bit area "
        "with the README match sets the closing-energy row (1/2, 1/2)", ok)
    return res


MUTANTS = {"floor_sign": "the relative floor's j-sign reversed",
           "three_kinds": "the invariants left in the three kinds (item 241's table)",
           "sms_sigma2": "SMS with G ~ sigma^2 (the invariant changed)",
           "bit_area_G2": "the bit area ~ G^2 (the invariant changed)"}


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
        print("  mutant %-12s %-50s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
