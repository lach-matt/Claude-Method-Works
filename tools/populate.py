#!/usr/bin/env python3
"""tools/populate.py -- populate an element on every axis of every index.

Give it a ground-state atomic number and it returns that element, and every
ion of it, on every coordinate the books define: the observed ground
configuration, the per-subshell quantum axes, the three periodic-table indexes,
the Rydberg channels of the spectra index, the Pauli bound, the quantum defect
under the method equation, and the Lambda_8 transition cells of its ionisation
ladder with the caps each one needs.

    python3 tools/populate.py --element K
    python3 tools/populate.py --z 19 --charge 1
    python3 tools/populate.py --element Fe --json
    python3 tools/populate.py --axes
    python3 tools/populate.py --equation
    python3 tools/populate.py --check-B
    python3 tools/populate.py --selftest

THE TWO HALVES. Register 1206 names the architecture: "the two halves of the
method equation meet for the first time on this index" -- R PLACES cells and
the channel equation VALUES them. This runs both. R is imported from
tools/cypher.py, where it is the PINNED order operator of section 32.4.1; the
channel equation is register 1205's final form.

PROVENANCE, AND WHY NOTHING HERE IS COPIED. The observed ground configurations
are LW1-ground.py, a seated bundle member (register 1306, NIST ASD 5.12, read
not computed), and the tower is tower-2.py. Both are imported BY PATH and
never transcribed, per CLAUDE.md section 5. The spectra index is
COORDINATES-2.13 in the Drive mirror, read with the csv module because its
source column contains commas.

STATUS, CARRIED NOT FLATTENED. Every axis this tool populates says where it
comes from, in cypher.py's vocabulary:

    READ           a measurement, taken from a member or the mirror
    PINNED         the corpus defines it at the precision a program needs
    DERIVED        arithmetic on a READ or PINNED quantity, nothing added
    RECONSTRUCTED  the corpus states the object and its behaviour but not the
                   form a program needs. Reconstructed here, measured against
                   the corpus's own numbers, and kept as RECONSTRUCTED so a
                   later ruling can move it.

Three things it refuses to do:

  1. It never prints a value without its status. A RECONSTRUCTED defect and a
     READ one are different objects and the report never merges them.

  2. It never silently places an element outside the caps. Lambda at section
     7.4's caps (n,e <= 3, l,f <= 1, k <= 3) admits almost no real element;
     rather than truncate, the report says OUTSIDE CAPS and names the caps at
     which the cell would be admitted.

  3. It never repairs a disagreement. Where the recomputed value differs from
     the recorded one the report carries both, per G0c: when a reconstruction
     disagrees with the record, the finding is about the reconstruction.
"""

from __future__ import annotations

import argparse
import bisect
import collections
import itertools
import csv
import importlib.util
import json
import math
import os
import sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEMBERS = os.path.join(REPO, "method", "members")
DEFAULT_SPECTRA = os.path.join(REPO, "drive", "The Method Materials",
                               "COORDINATES-2_13.csv")

READ, PINNED, DERIVED, RECON = "READ", "PINNED", "DERIVED", "RECONSTRUCTED"
# RECOVERED — not stated in any member, but recovered by measurement from the
# index's own computed column and consistent with what the registers say about
# it qualitatively. Stronger than RECONSTRUCTED, weaker than PINNED.
RECOVERED = "RECOVERED"
# PREDICTED — beyond the evidentiary boundary. Section VIII of the Loewdin
# solution: "Because ground configurations are experimentally established only
# through Z = 108, this work enforces a strict evidentiary boundary there. The
# 107 elements up to it constitute the derivation, scored against nature. The
# twelve elements beyond it are published as predictions — explicitly labeled,
# unfitted, and falsifiable the day their spectra can be measured."
PREDICTED = "PREDICTED"


def _load(name, filename):
    """Import a seated member by path. CLAUDE.md section 5: never by copying."""
    path = os.path.join(MEMBERS, filename)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


LW1 = _load("lw1_ground", "LW1-ground.py")
TOWER = _load("tower_2", "tower-2.py")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cypher  # noqa: E402  -- R, the PINNED order operator of section 32.4.1

LSYM = "spdfgh"
# Spectroscopic term letters. J is skipped, which is why "4K11/2" is L = 7.
TERM_L = "SPDFGHIKLMNOQRTUV"
SYMBOL_TO_Z = {sym: z for z, (sym, _c, _l) in LW1.GROUND.items()}

# ---------------------------------------------------------------------------
# The periodic table, laid out as chapter 6 lays it out
# ---------------------------------------------------------------------------

# Section 6: "main-table cells (lanthanides and actinides set aside) = 90".
PERIOD_END = [2, 10, 18, 36, 54, 86, 118, 168]
LANTHANIDES = range(58, 72)      # Ce to Lu
ACTINIDES = range(90, 104)       # Th to Lr


def period_of(Z):
    return bisect.bisect_left(PERIOD_END, Z) + 1


def set_aside(Z):
    """The f-block rows chapter 6 sets aside from the main table."""
    return Z in LANTHANIDES or Z in ACTINIDES


def group_of(Z):
    """Group in the drawn eighteen-column layout, or None if set aside.

    Reproduces chapter 6's ninety main-table cells exactly: period 1 holds
    groups 1 and 18, periods 2 and 3 hold 1, 2 and 13 to 18, and periods 4 to 7
    hold all eighteen. That is 2 + 8 + 8 + 18*4 = 90, and the self-test asserts
    it against section 6's own figure."""
    if set_aside(Z):
        return None
    p = period_of(Z)
    start = 1 if p == 1 else PERIOD_END[p - 2] + 1
    i = Z - start                       # 0-based position within the period
    if p == 1:
        return 1 if Z == 1 else 18
    if p in (2, 3):
        return (1, 2, 13, 14, 15, 16, 17, 18)[i]
    if p in (6, 7):
        # 3 before the f-block, then 15 after it
        return i + 1 if i <= 2 else i + 1 - 14
    if p == 8:
        # Only 119 and 120 are predicted; the g-block below them is not.
        return i + 1 if i <= 1 else None
    return i + 1


def block_of(Z):
    """The block, from the DIFFERENTIATING electron -- the subshell that
    distinguishes Z from Z-1. This is the Loewdin construction's own object,
    and it is why the block is a fact about filling rather than about the
    drawn layout."""
    if Z == 1:
        return 0
    a, b = config_of(Z), config_of(Z - 1)
    if a is None or b is None:
        return None
    now = {(n, l): o for n, l, o in a}
    before = {(n, l): o for n, l, o in b}
    gained = [(n, l) for (n, l), o in now.items() if o > before.get((n, l), 0)]
    if not gained:
        return None
    return sorted(gained)[-1][1]


def janet_cell(Z):
    """Janet's coordinate IS n+l (register 1188), so its blocks ARE the
    collapse boundaries. The cell is (n+l, l) of the differentiating electron."""
    if Z == 1:
        return (1, 0)
    a, b = config_of(Z), config_of(Z - 1)
    if a is None or b is None:
        return None
    now = {(n, l): o for n, l, o in a}
    before = {(n, l): o for n, l, o in b}
    gained = [(n, l) for (n, l), o in now.items() if o > before.get((n, l), 0)]
    if not gained:
        return None
    n, l = sorted(gained)[-1]
    return (n + l, l)


# ---------------------------------------------------------------------------
# The Pauli bound -- register 1141, PINNED
# ---------------------------------------------------------------------------

# The corpus's own prediction, stated as a rule rather than a table: "the
# entrant is 6d from Z = 109 through 112, 7p from 113 through 118, and 8s at
# 119 and 120, with stated margins between 0.058 and 0.264 hartree, every one
# clearing the spin-orbit worst case" (Loewdin solution, section VIII).
# The configurations below are DERIVED from that rule and from Hs at Z = 108,
# which is READ. They are never merged with the observed table.
PREDICTED_ENTRANT = (((109, 112), (6, 2)),      # 6d
                     ((113, 118), (7, 1)),      # 7p
                     ((119, 120), (8, 0)))      # 8s
PREDICTED_MAX = 120
EVIDENTIARY_BOUNDARY = 108

# Conventional IUPAC symbols, a convenience for reading the report only. The
# store names none of these; 119 and 120 have only systematic names.
BEYOND_SYMBOL = {109: "Mt", 110: "Ds", 111: "Rg", 112: "Cn", 113: "Nh",
                 114: "Fl", 115: "Mc", 116: "Lv", 117: "Ts", 118: "Og",
                 119: "Uue", 120: "Ubn"}


def entrant_of(Z):
    for (lo, hi), nl in PREDICTED_ENTRANT:
        if lo <= Z <= hi:
            return nl
    return None


def predicted_config(Z):
    """The ground configuration at Z = 109 to 120, built from Hs plus the
    corpus's stated entrant sequence. One electron per element, into the
    subshell section VIII names."""
    if not (EVIDENTIARY_BOUNDARY < Z <= PREDICTED_MAX):
        return None
    occ = {(n, l): o for n, l, o in LW1.expand(EVIDENTIARY_BOUNDARY)}
    for z in range(EVIDENTIARY_BOUNDARY + 1, Z + 1):
        nl = entrant_of(z)
        if nl is None:
            return None
        occ[nl] = occ.get(nl, 0) + 1
        if occ[nl] > 2 * (2 * nl[1] + 1):
            return None
    return [(n, l, o) for (n, l), o in
            sorted(occ.items(), key=lambda kv: (kv[0][0] + kv[0][1], kv[0][0]))
            if o > 0]


def ground_of(Z, table="observed"):
    """The ground configuration and where it comes from.

    Below the evidentiary boundary this is measurement; above it, the corpus's
    published prediction. The status is carried so the two are never merged --
    which is the boundary section VIII enforces, kept in the program."""
    if Z in LW1.GROUND:
        sym, shells, level = LW1.GROUND[Z]
        cfg = config_of(Z, table)
        return {"config": cfg, "symbol": sym, "shells": shells,
                "level": level, "status": READ if table == "observed" else DERIVED,
                "basis": ("NIST ASD 5.12 via LW1-ground.py (register 1306)"
                          if table == "observed"
                          else "aufbau, the table register 1306 withdrew")}
    cfg = predicted_config(Z)
    if cfg is None:
        return None
    return {"config": cfg, "symbol": BEYOND_SYMBOL.get(Z, "Z%d" % Z),
            "shells": " ".join("%d%s%d" % (n, LSYM[l], o) for n, l, o in cfg),
            "level": None, "status": PREDICTED,
            "basis": "Loewdin solution section VIII: the entrant is 6d from "
                     "Z = 109 to 112, 7p from 113 to 118, 8s at 119 and 120"}


MADELUNG = sorted(((n, l) for n in range(1, 9) for l in range(0, min(n, 5))),
                  key=lambda t: (t[0] + t[1], t[0]))


def aufbau_config(Ne):
    """The configuration Madelung order predicts. Register 1306 WITHDREW this
    table as the store's ground configurations -- "that table was wrong at Pd
    ... and at Lr" -- but COORDINATES-2.13 was built on it, so reproducing the
    index as it stands requires it. It is never the default."""
    out, left = [], Ne
    for n, l in MADELUNG:
        if left <= 0:
            break
        take = min(2 * (2 * l + 1), left)
        out.append((n, l, take))
        left -= take
    return out


CONFIG_TABLES = {
    "observed": lambda Ne: (LW1.expand(Ne) if Ne in LW1.GROUND else None),
    "aufbau": aufbau_config,
}


def config_of(Ne, table="observed"):
    """The configuration of a neutral species with Ne electrons.

    Above the evidentiary boundary the observed table has nothing, so the
    corpus's published prediction is used and the caller is expected to carry
    the PREDICTED status with it."""
    if Ne < 1:
        return None
    if table == "observed" and Ne not in LW1.GROUND:
        return predicted_config(Ne)
    return CONFIG_TABLES[table](Ne)


def core_p(core_Ne, l, table="observed"):
    """p, the core's orbital count at this l, from the OBSERVED ground
    configuration of the core (register 1306)."""
    cfg = config_of(core_Ne, table)
    if cfg is None:
        return None
    return sum(1 for _n, ll, o in cfg if ll == l and o > 0)


def n0_of(core_Ne, l, table="observed"):
    """n0, the first Pauli-allowed n.

    RECONSTRUCTED. Register 1141 states the bound and names its two terms; it
    does not say whether a PARTIALLY filled subshell counts as allowed. Both
    readings were measured against COORDINATES-2.13's own B column: "first n
    with room" matches 87.0% of 102,871 rows, "first ENTIRELY UNOCCUPIED n"
    matches 97.7%. He I ns settles it -- the core is 1s(1), the CSV gives B = 1,
    and only the second reading returns 1."""
    cfg = config_of(core_Ne, table)
    if cfg is None:
        return None
    occ = {(n, ll): o for n, ll, o in cfg}
    n = l + 1
    while occ.get((n, l), 0) > 0:
        n += 1
    return n


def pauli_bound(Z, charge, l, config=None):
    """B = min(p, n0 - l - 1). Register 1141, Pauli 1925, Janet 1929."""
    core = Z - charge
    if core < 1:
        return 0
    if config is not None:
        occ = {(n, ll): o for n, ll, o in config}
        p = sum(1 for n, ll, o in config if ll == l and o > 0)
        n = l + 1
        while occ.get((n, l), 0) > 0:
            n += 1
    else:
        p = core_p(core, l)
        n = n0_of(core, l)
        if p is None or n is None:
            return None
    return max(0, min(p, n - l - 1))


# ---------------------------------------------------------------------------
# The channel equation, final form -- register 1205
# ---------------------------------------------------------------------------

A_COEFF = 0.3772
E0, E1 = 0.8297, 0.0900
K_COEFF = 0.4942
H_COEFF = 0.5415

# The Janet block opening for each l: the Z at which the n+l block containing
# that subshell opens. Register 1188 gives two of them exactly -- "the n+l = 5
# block opens at Z = 21 (Sc) and 3d collapses at 21. The n+l = 7 block opens at
# 57 (La) and 4f collapses at 57" -- and l = 1 falls out of the same rule at
# boron, where the 2p block opens.
COLLAPSE_Z = {1: 5, 2: 21, 3: 57}
COLLAPSE_WIDTH = 8.0


def collapse_C(Z, l):
    """C(Z), the collapse coordinate across the Janet boundary.

        C(Z, l) = clamp( 0.5 + (Z - Z0(l)) / 8, 0, 1 )

    RECOVERED, not reconstructed. No member states the form: register 1190 says
    only that it is "read off the periodic table, not fitted -- one lookup".
    But COORDINATES-2.13's own computed column is generated by this equation,
    so C can be INVERTED out of it, and it comes back exact:

        l = 2:  C = 0.125, 0.250, 0.375, 0.500, 0.625, 0.750, 0.875, 1.000
                at Z =  18,   19,    20,    21,    22,    23,    24,    25
        l = 3:  the same eight values at Z = 54 to 61
        l = 1:  the same eight values at Z =  2 to  9

    A linear ramp eight wide, reaching exactly 0.5 at the Janet boundary and
    saturating four beyond it. That is register 1189 in closed form -- "the
    collapse is a rapid transition, NOT A STEP" -- and it is why Ca I nd is
    0.908 at Z = 20, below the threshold: C(20, 2) = 0.375, already a third of
    the way up the ramp. An indicator would have made it zero.

    Above l = 3 there is no collapse and C is zero, which the index agrees
    with: every l >= 4 channel inverts to C = 0 exactly."""
    z0 = COLLAPSE_Z.get(l)
    if z0 is None:
        return 0.0
    return min(1.0, max(0.0, 0.5 + (Z - z0) / COLLAPSE_WIDTH))


def channel_delta(Z, charge, l, table="observed"):
    """delta for a Rydberg channel, register 1205's standing form.

        delta = a p^e(Ne) Ne^k ln(c+1)/c                  where p > 0
        delta = h C(Z) ((Ne-1)/Ne) Ne^k ln(c+1)/c         where p = 0

    Ne is the electron count of the ION and c its spectroscopic charge, so a
    neutral atom is c = 1 and the core it presents is singly charged.

    Register 5193 records that at Ne = 1 the (Ne-1)/Ne factor vanishes
    identically for every charge and every C(Z), which is what makes a
    one-electron ion return exactly zero -- the hydrogenic case, and not a
    fitted one."""
    Ne = Z - charge + 1
    c = charge
    if Ne < 1 or c < 1:
        return None
    core = Ne - 1
    p = core_p(core, l, table) if core >= 1 else 0
    if p is None:
        return None
    charge_factor = math.log(c + 1) / c
    if p > 0:
        e = E0 - E1 * math.log(Ne)
        return A_COEFF * (p ** e) * (Ne ** K_COEFF) * charge_factor
    return (H_COEFF * collapse_C(Z, l) * ((Ne - 1) / Ne)
            * (Ne ** K_COEFF) * charge_factor)


# ---------------------------------------------------------------------------
# Terms, seniority, and the coupling chain -- Lambda_9 to Lambda_13
# ---------------------------------------------------------------------------

_TERMS = {}


def terms(l, k):
    """The multiset of LS terms (2S, L) of the configuration l^k.

    PINNED. Section 12.11.1 defines it and this is that definition, executed:
    "list every way of placing k electrons in the 2(2l+1) spin-orbitals,
    accumulate (2M_L, 2M_S), and strip complete (2S, 2L) blocks from the
    largest M_L down until the list is empty."

    The section calls it "the standard construction and the origin Chapter 7
    already cites for 2S <= k", so nothing here is new; what matters is that
    the tower's bounds are computed from it rather than asserted."""
    key = (l, k)
    if key in _TERMS:
        return _TERMS[key]
    if k < 0 or k > 2 * (2 * l + 1):
        _TERMS[key] = []
        return []
    orb = [(ml, ms2) for ml in range(l, -l - 1, -1) for ms2 in (1, -1)]
    cnt = collections.Counter()
    for c in itertools.combinations(orb, k):
        cnt[(sum(o[0] for o in c), sum(o[1] for o in c))] += 1
    out = []
    while cnt:
        ML = max(m for (m, _s) in cnt)
        MS2 = max(s for (m, s) in cnt if m == ML)
        out.append((MS2, ML))
        for ml in range(-ML, ML + 1):
            for ms2 in range(-MS2, MS2 + 1, 2):
                cnt[(ml, ms2)] -= 1
                if cnt[(ml, ms2)] <= 0:
                    del cnt[(ml, ms2)]
    out.sort()
    _TERMS[key] = out
    return out


def j2_values(S2, L):
    """2J for a term, |L-S| <= J <= L+S in integer steps."""
    lo, hi = abs(2 * L - S2), 2 * L + S2
    return list(range(lo, hi + 1, 2))


def hund_ground_term(l, k):
    """Hund: maximum S, then maximum L, then J = |L-S| below half filling and
    L+S at or above it. Returns (2S, L, 2J) or None for an empty shell."""
    ts = terms(l, k)
    if not ts:
        return None
    S2 = max(t[0] for t in ts)
    L = max(t[1] for t in ts if t[0] == S2)
    js = j2_values(S2, L)
    half = 2 * l + 1
    return (S2, L, js[0] if k <= half else js[-1])


def seniority(l, k, S2, L):
    """v, the seniority of a term: the smallest k' of the same parity in which
    the term first appears. Lambda_10's coordinate, bounded 2S' <= v <= g."""
    for kp in range(k % 2, k + 1, 2):
        if (S2, L) in terms(l, kp):
            return kp
    return None


def phi_hat(k, lmax=None):
    """phi-hat(k), section 12.11.1: "the monotone envelope of k -> max 2J over
    the parent shells admitted by the caps".

    COMPUTED, not copied. At section 7.4's caps (l <= 1) this returns
    {1: 3, 2: 4, 3: 5}, which is exactly tower-2.py's hardcoded PHI -- and
    that agreement is a self-test fixture, because it is the one place the
    microstate enumeration above can be checked against a seated instrument.

    Note the section's warning: this is NOT section 6.1's phi-hat_ij, R's
    pairwise envelope. Both are monotone envelopes and that is the whole of
    the resemblance."""
    if lmax is None:
        lmax = CAPS["l"]
    best = 0
    for l in range(0, lmax + 1):
        for S2, L in terms(l, k):
            best = max(best, 2 * L + S2)
    return best


LEVEL_LS = None


def parse_level(text):
    """A NIST ground level into its quantum numbers.

    The store carries three forms: LS terms like "4I*15/2", the jj-coupled
    "(1/2,1/2)0" that Pb takes, and a bare J for Sg, Bh and Hs where only that
    is known. The star is odd parity."""
    import re
    t = (text or "").strip()
    m = re.fullmatch(r"(\d+)([A-Z])(\*?)(\d+(?:/2)?)", t)
    if m:
        mult, letter, star, j = m.groups()
        if letter in TERM_L:
            return {"form": "LS", "mult": int(mult), "S2": int(mult) - 1,
                    "L": TERM_L.index(letter), "parity": "odd" if star else "even",
                    "J2": int(j[:-2]) if j.endswith("/2") else 2 * int(j),
                    "J": j}
    m = re.fullmatch(r"\((.*?)\)(\*?)(\d+(?:/2)?)", t)
    if m:
        inner, star, j = m.groups()
        return {"form": "jj", "mult": None, "S2": None, "L": None,
                "parity": "odd" if star else "even",
                "J2": int(j[:-2]) if j.endswith("/2") else 2 * int(j),
                "J": j, "pair": inner}
    m = re.fullmatch(r"(\d+(?:/2)?)", t)
    if m:
        j = m.group(1)
        return {"form": "J only", "mult": None, "S2": None, "L": None,
                "parity": None,
                "J2": int(j[:-2]) if j.endswith("/2") else 2 * int(j), "J": j}
    return {"form": "unparsed", "mult": None, "S2": None, "L": None,
            "parity": None, "J2": None, "J": None}


def open_shells(cfg):
    return [(n, l, o) for n, l, o in cfg if 0 < o < 2 * (2 * l + 1)]


def core_term(cfg):
    """The core's ground term (2S, L, 2J), and how it was got.

    A closed shell is 1S0 exactly. One open subshell is Hund on that subshell,
    which is DERIVED and exact for a single shell. More than one open subshell
    needs a coupling between them that Hund does not fix, so it is reported
    UNDETERMINED rather than guessed."""
    if cfg is None:
        return None
    op = open_shells(cfg)
    if not op:
        return {"S2": 0, "L": 0, "J2": 0, "shell": None,
                "basis": "closed shell: 1S0 exactly", "status": DERIVED}
    if len(op) == 1:
        n, l, k = op[0]
        g = hund_ground_term(l, k)
        return {"S2": g[0], "L": g[1], "J2": g[2],
                "shell": "%d%s%d" % (n, LSYM[l], k),
                "basis": "Hund on the one open subshell", "status": DERIVED}
    return {"S2": None, "L": None, "J2": None,
            "shell": ", ".join("%d%s%d" % (n, LSYM[l], k) for n, l, k in op),
            "basis": "more than one open subshell; Hund does not fix the "
                     "coupling between them", "status": "UNDETERMINED"}


def tower_for_channel(Z, charge, l_out, table="observed"):
    """The Lambda_9 to Lambda_13 coordinates of one Rydberg channel.

    A tower cell extends a Lambda_8 transition by the target's multiplicity,
    its seniority, and the J_c-K coupling chain. A Rydberg channel IS that
    object: a core with fine structure 2J_c, and one electron placed in a
    subshell of l. Section 12.11.1 says as much of the three coupling axes --
    "the core's fine structure", "core-orbit orientation", "the outer
    electron's spin bit" -- and |2J - 2K| <= 1 is J = K +/- 1/2 written out.

    So g = 1 and q = 1: one electron moved. Every bound below is tower-2.py's,
    and every physical value is the coupling the core and that electron
    actually admit."""
    Ne = Z - charge + 1
    core = Ne - 1
    cfg = config_of(core, table) if core >= 1 else []
    if cfg is None:
        return None
    ct = core_term(cfg)
    op = open_shells(cfg)
    if op:
        _n, l_src, k = op[-1]
    elif cfg:
        _n, l_src, k = cfg[-1]
    else:
        l_src, k = 0, 0

    g = 1                      # one electron placed in the outer subshell
    S2 = ct["S2"]              # Lambda_8's 2S, the source multiplicity
    J2c = ct["J2"]             # Lambda_11's 2J_c, the core's fine structure

    out = {
        "core_Ne": core, "l_out": l_out, "k": k, "l_source": l_src,
        "core_term": ct,
        "L8_2S": {"value": S2, "bound": "2S <= k = %d" % k,
                  "admitted": list(range(0, k + 1)), "status": ct["status"]},
        "L9_2Sprime": {"value": 1, "bound": "2S' <= g = 1",
                       "admitted": [0, 1],
                       "status": DERIVED,
                       "note": "one electron carries spin 1/2, so 2S' = 1"},
        "L10_v": {"value": seniority(l_out, 1, 1, l_out),
                  "bound": "2S' <= v <= g = 1", "admitted": [1],
                  "status": PINNED,
                  "note": "seniority of a one-electron shell"},
        "L11_2Jc": {"value": J2c,
                    "bound": "2J_c <= phi-hat(k) = %d" % phi_hat(k, lmax=max(l_src, CAPS["l"])),
                    "admitted": list(range(0, phi_hat(k, lmax=max(l_src, CAPS["l"])) + 1)),
                    "status": ct["status"]},
    }
    if J2c is None:
        out["L12_2K"] = {"value": None, "admitted": None, "status": "UNDETERMINED",
                         "bound": "2K <= 2J_c + 2f_max"}
        out["L13_2J"] = {"value": None, "admitted": None, "status": "UNDETERMINED",
                         "bound": "|2J - 2K| <= 1"}
        return out

    # K is the vector coupling of J_c with the outer electron's orbital l.
    K2 = list(range(abs(J2c - 2 * l_out), J2c + 2 * l_out + 1, 2))
    out["L12_2K"] = {
        "value": K2, "admitted": K2, "status": DERIVED,
        "bound": "index: 2K <= 2J_c + 2f_max = %d; physical: |2J_c - 2l| <= 2K"
                 " <= 2J_c + 2l" % (J2c + 2 * CAPS["f"]),
        "within_index_bound": all(x <= J2c + 2 * CAPS["f"] for x in K2),
    }
    # J is K coupled with the outer electron's spin: J = K +/- 1/2.
    J2 = sorted({j for x in K2 for j in (x - 1, x + 1) if j >= 0})
    out["L13_2J"] = {"value": J2, "admitted": J2, "status": DERIVED,
                     "bound": "|2J - 2K| <= 1, which is J = K +/- 1/2"}
    return out


# ---------------------------------------------------------------------------
# The spectra index
# ---------------------------------------------------------------------------

class Spectra:
    """COORDINATES-2.13, the spectra index: (Z, charge, l, mult) -> a channel."""

    def __init__(self, path):
        self.path = path
        self.rows = []
        self.by_z = {}
        if not path or not os.path.exists(path):
            return
        with open(path, encoding="utf-8-sig", newline="") as fh:
            for r in csv.DictReader(fh):
                self.rows.append(r)
                self.by_z.setdefault(int(r["Z"]), []).append(r)

    @property
    def present(self):
        return bool(self.rows)

    def channels(self, Z, charge=None):
        out = [r for r in self.by_z.get(Z, [])
               if charge is None or int(r["charge"]) == charge]
        return sorted(out, key=lambda r: (int(r["charge"]), int(r["l"]),
                                          int(r["mult"])))


def csv_bound(r):
    """The CSV's B column, as the Pauli bound -- or None.

    The column is OVERLOADED. In 104,807 rows it carries the integer Pauli
    bound; in 25 measured rows from the 2026-08-14 NIST fetch it carries a
    float, a dispersion of the median defect rather than a bound. Reading it as
    a bound in those 25 rows is wrong, so this returns None and the report says
    so rather than comparing an integer against a spread."""
    v = r.get("B", "")
    return int(v) if v.lstrip("-").isdigit() else None


# ---------------------------------------------------------------------------
# Lambda_8 and the tower
# ---------------------------------------------------------------------------

CAPS = dict(n=3, e=3, l=1, f=1, k=3)     # section 7.4's standing caps

LAMBDA_COORDS = ["n", "l", "k", "q", "e", "f", "g", "2S"]
LAMBDA_MEANING = {
    "n": "source shell", "l": "source subshell", "k": "source occupancy",
    "q": "electrons removed", "e": "target shell", "f": "target subshell",
    "g": "target occupancy", "2S": "multiplicity",
}


def lambda_constraints(cell):
    """Section 7.1's seven constraints, four origins. PINNED."""
    n, l, k, q, e, f, g, S2 = cell
    return [
        ("l <= n-1", l <= n - 1, "hydrogenic radial solution"),
        ("k <= 2(2l+1)", k <= 2 * (2 * l + 1), "Pauli exclusion"),
        ("q <= k", q <= k, "counting"),
        ("f <= e-1", f <= e - 1, "hydrogenic radial solution"),
        ("g <= 2(2f+1)", g <= 2 * (2 * f + 1), "Pauli exclusion"),
        ("g <= q", g <= q, "counting"),
        ("2S <= k", S2 <= k, "vector coupling (an envelope)"),
    ]


def caps_needed(cell):
    n, l, k, q, e, f, g, _S2 = cell
    return dict(n=n, e=e, l=l, f=f, k=k)


def within_caps(cell, caps=CAPS):
    need = caps_needed(cell)
    return {ax: need[ax] <= caps[ax] for ax in caps}


def _sym(Ne):
    if Ne in LW1.GROUND:
        return LW1.GROUND[Ne][0]
    return BEYOND_SYMBOL.get(Ne, "Z%d" % Ne)


def ionisation_cells(Z):
    """The ionisation ladder as Lambda_8 transition cells.

    RECONSTRUCTED, and the reconstruction is stated rather than assumed.
    Chapter 7 makes a Lambda_8 cell a TRANSITION -- a source configuration, a
    target configuration and the electron count moved between them -- so an
    element is not a cell and a mapping has to be chosen. The one chosen here
    is the element's own ionisation ladder, read off the observed
    configurations: at each step, the electrons the ion loses relative to the
    neutral atom leave a source subshell, and the subshell that differs
    identifies the target. Nothing else in the store fixes this mapping, so it
    is marked RECONSTRUCTED and a later ruling can move it.

    2S is the ion's own ground multiplicity where the term is known, else the
    envelope 2S <= k leaves it undetermined and it is reported as None."""
    out = []
    for charge in range(2, Z + 2):
        Ne = Z - charge + 1
        pcfg, ccfg = config_of(Ne + 1), config_of(Ne)
        if Ne < 1 or pcfg is None or ccfg is None:
            continue
        parent = {(n, l): o for n, l, o in pcfg}
        child = {(n, l): o for n, l, o in ccfg}
        lost = [(nl, parent[nl] - child.get(nl, 0)) for nl in parent
                if parent[nl] > child.get(nl, 0)]
        gained = [(nl, child[nl] - parent.get(nl, 0)) for nl in child
                  if child[nl] > parent.get(nl, 0)]
        if not lost:
            continue
        (sn, sl), q = sorted(lost)[-1]
        k = parent[(sn, sl)]
        if gained:
            (tn, tl), g = sorted(gained)[-1]
        else:
            tn, tl, g = sn, sl, 0
        out.append({
            "charge": charge, "Ne": Ne,
            "from": _sym(Ne + 1), "to": _sym(Ne),
            "cell": (sn, sl, k, q, tn, tl, g, None),
        })
    return out


# ---------------------------------------------------------------------------
# The report
# ---------------------------------------------------------------------------

AXES = [
    ("Z", READ, "the ground-state atomic number, the input"),
    ("symbol", READ, "NIST ASD 5.12 via LW1-ground.py (register 1306)"),
    ("configuration", READ, "observed ground shells, cores expanded"),
    ("level", READ, "observed ground level"),
    ("n", DERIVED, "principal quantum number, per occupied subshell"),
    ("l", DERIVED, "azimuthal quantum number, per occupied subshell"),
    ("occupancy", DERIVED, "electrons in the subshell"),
    ("capacity", PINNED, "2(2l+1), Pauli exclusion (section 7.1)"),
    ("n+l", DERIVED, "the Madelung/Janet coordinate (register 1188)"),
    ("period", DERIVED, "the drawn eighteen-column layout (section 6)"),
    ("group", DERIVED, "the same layout; None where set aside"),
    ("block", DERIVED, "l of the differentiating electron"),
    ("janet cell", DERIVED, "(n+l, l) of the differentiating electron; E = 0"),
    ("charge", READ, "spectroscopic stage; 1 is neutral"),
    ("Ne", DERIVED, "electron count of the ion, Z - charge + 1"),
    ("p", PINNED, "the core's orbital count at this l (register 1141)"),
    ("n0", RECON, "first entirely unoccupied n at this l; see n0_of"),
    ("B", PINNED, "min(p, n0-l-1), the Pauli bound (register 1141)"),
    ("delta measured", READ, "COORDINATES-2.13, grade measured/exact"),
    ("delta equation", PINNED, "the channel equation, final form (register 1205)"),
    ("C(Z)", RECON, "the collapse coordinate (registers 1188-1190)"),
    ("witness", READ, "COORDINATES-2.13"),
    ("bound", READ, "COORDINATES-2.13"),
    ("2S", DERIVED, "Lambda_8: source multiplicity, from terms(l^k) and Hund"),
    ("2S'", DERIVED, "Lambda_9: the target's multiplicity, 2S' <= g"),
    ("v", PINNED, "Lambda_10: seniority, 2S' <= v <= g (section 12.11.1)"),
    ("2J_c", DERIVED, "Lambda_11: the core's fine structure, 2J_c <= phi-hat(k)"),
    ("2K", DERIVED, "Lambda_12: core-orbit orientation, 2K <= 2J_c + 2f_max"),
    ("2J", DERIVED, "Lambda_13: the outer electron's spin bit, |2J - 2K| <= 1"),
    ("terms(l^k)", PINNED, "microstate enumeration, defined at section 12.11.1"),
    ("phi-hat(k)", PINNED, "computed from terms; equals tower-2.py's PHI at the caps"),
    ("Lambda_8 cell", RECON, "the ionisation ladder as transitions; see ionisation_cells"),
    ("caps", PINNED, "section 7.4's (n,e,l,k,f) = (3,3,1,3,1)"),
]


_R_CACHE = {}


def layout_closure():
    """The structural half: R over the drawn layout. Section 6 -- 90 cells
    held, 126 admitted, E = 36, and the thirty-six are the gaps in the short
    periods. Computed once and cached; R is cypher.py's PINNED order operator,
    imported rather than reimplemented."""
    if "periodic" not in _R_CACHE:
        main = [Z for Z in range(1, 119) if not set_aside(Z)]
        held = {(period_of(Z), group_of(Z)) for Z in main}
        ix = cypher.Index("periodic table (period x group)",
                          ["period", "group"], sorted(held))
        admitted, _note = cypher.op_order(ix, {})
        # cypher.Index recodes every coordinate value to an ordinal, because R
        # is order-dependent (section 20.3). Decode before comparing to the
        # layout, or the cells come back as ranks and read as the wrong groups.
        admitted = {tuple(ix.decode[i][v] for i, v in enumerate(cell))
                    for cell in admitted}
        _R_CACHE["periodic"] = (held, admitted)
    return _R_CACHE["periodic"]


def populate(Z, spectra, charge=None, table="observed"):
    g = ground_of(Z, table)
    if g is None:
        raise KeyError("Z = %d has no configuration: measurement stops at %d "
                       "and the corpus's predictions stop at %d"
                       % (Z, EVIDENTIARY_BOUNDARY, PREDICTED_MAX))
    sym, shells, level = g["symbol"], g["shells"], g["level"]
    cfg = g["config"]
    n_e = sum(o for _n, _l, o in cfg)
    out = {
        "Z": Z, "symbol": sym, "shells_as_printed": shells, "level": level,
        "config_status": g["status"], "config_basis": g["basis"],
        "electron_count": n_e,
        "electron_count_ok": n_e == Z,
        "configuration": [{"n": n, "l": l, "subshell": "%d%s" % (n, LSYM[l]),
                           "occupancy": o, "capacity": 2 * (2 * l + 1),
                           "full": o == 2 * (2 * l + 1), "n+l": n + l}
                          for n, l, o in cfg],
        "period": period_of(Z), "group": group_of(Z), "block": block_of(Z),
        "block_letter": (LSYM[block_of(Z)] if block_of(Z) is not None else None),
        "set_aside": set_aside(Z), "janet_cell": janet_cell(Z),
        "outer": LW1.outer(Z),
        "level_decoded": parse_level(level) if level else
        {"form": "not predicted", "mult": None, "S2": None, "L": None,
         "parity": None, "J2": None, "J": None},
    }
    held, admitted = layout_closure()
    out["closure"] = {
        "held": len(held), "admitted": len(admitted),
        "E": len(admitted) - len(held),
        "cell_held": (out["period"], out["group"]) in held,
        "denied_in_this_period": sorted(
            g for (p, g) in (admitted - held) if p == out["period"]),
    }

    chans = []
    stages = range(1, Z + 1) if charge is None else [charge]
    seen_csv = {}
    if spectra.present:
        for r in spectra.channels(Z, charge):
            seen_csv[(int(r["charge"]), int(r["l"]), int(r["mult"]))] = r
    ls = sorted({l for (_c, l, _m) in seen_csv} | {0, 1, 2, 3})
    for c in stages:
        Ne = Z - c + 1
        if Ne < 1:
            continue
        core = Ne - 1
        for l in ls:
            rows = [r for (cc, ll, _m), r in seen_csv.items()
                    if cc == c and ll == l]
            eq = channel_delta(Z, c, l, table)
            B = pauli_bound(Z, c, l, config=config_of(core, table))
            ch = {
                "charge": c, "Ne": Ne, "l": l, "subshell_letter": LSYM[l]
                if l < len(LSYM) else str(l),
                "core_Ne": core,
                "core_symbol": LW1.GROUND[core][0] if core in LW1.GROUND else None,
                "p": core_p(core, l, table) if core >= 1 else 0,
                "n0": n0_of(core, l, table) if core >= 1 else None,
                "B_computed": B,
                "C_of_Z": collapse_C(Z, l),
                "delta_equation": eq,
                "tower": tower_for_channel(Z, c, l, table),
                "measured": [],
            }
            for r in sorted(rows, key=lambda r: int(r["mult"])):
                cb = csv_bound(r)
                ch["measured"].append({
                    "mult": int(r["mult"]), "delta": float(r["delta"]),
                    "grade": r["grade"], "witness": r["witness"],
                    "source": r["source"], "bound_note": r["bound"],
                    "B_csv": cb,
                    "B_agrees": (None if cb is None or B is None else cb == B),
                    "B_csv_is_not_a_bound": cb is None and r.get("B", "") != "",
                    "floor_le_B": (None if B is None
                                   else math.floor(float(r["delta"])) <= B),
                    "residual": (None if eq is None
                                 else float(r["delta"]) - eq),
                })
            chans.append(ch)
    out["config_table"] = table
    out["channels"] = chans
    out["lambda8"] = []
    for step in ionisation_cells(Z):
        cell = step["cell"]
        probe = tuple(0 if v is None else v for v in cell)
        out["lambda8"].append({
            **step,
            "coords": dict(zip(LAMBDA_COORDS, cell)),
            "constraints": [{"rule": r, "holds": h, "origin": o}
                            for r, h, o in lambda_constraints(probe)],
            "within_caps": within_caps(probe),
            "caps_needed": caps_needed(probe),
        })
    return out


def _halves(two_j):
    """2J as a J: 3 -> 3/2, 4 -> 2."""
    return str(two_j // 2) if two_j % 2 == 0 else "%d/2" % two_j


def _fmt(v, nd=4):
    return "-" if v is None else ("%.*f" % (nd, v) if isinstance(v, float)
                                  else str(v))


def report(rep, show_channels=True, max_charge=None):
    print("=" * 78)
    print("  Z = %-4d %-3s   %s" % (rep["Z"], rep["symbol"],
                                    rep["shells_as_printed"]))
    print("  ground level %s   electrons %d %s"
          % (rep["level"] or "not predicted", rep["electron_count"],
             "OK" if rep["electron_count_ok"] else "MISMATCH"))
    print("  configuration  [%s]  %s" % (rep["config_status"],
                                         rep["config_basis"]))
    if rep["config_status"] == PREDICTED:
        print("  *** BEYOND THE EVIDENTIARY BOUNDARY at Z = %d. Section VIII "
              "publishes Z = 109" % EVIDENTIARY_BOUNDARY)
        print("      to 120 as PREDICTIONS -- unfitted and falsifiable, never "
              "scored against nature.")
        print("      Nothing below is a measurement, and none of it may be "
              "quoted as one.")
    print("=" * 78)
    print()
    print("  THE LAYOUT INDEXES                                        [DERIVED]")
    print("    periodic table 2-D   (period, group)  = (%s, %s)%s"
          % (rep["period"], rep["group"],
             "   SET ASIDE from the main table (f-block)"
             if rep["set_aside"] else ""))
    print("    periodic table 3-D   (period, group, block) = (%s, %s, %s)"
          % (rep["period"], rep["group"], rep["block_letter"]))
    print("    Janet                (n+l, l) = %s     [E = 0, register 1188]"
          % (rep["janet_cell"],))
    cl = rep["closure"]
    print()
    print("  THE STRUCTURAL HALF -- R over the drawn layout          [PINNED]")
    print("    the table holds %d cells; R admits %d; E = %d   [section 6]"
          % (cl["held"], cl["admitted"], cl["E"]))
    print("    this element's cell is %s"
          % ("held" if cl["cell_held"]
             else "NOT a main-table cell (set aside)"))
    if cl["denied_in_this_period"]:
        print("    in period %s, R admits and the table denies groups %s"
              % (rep["period"],
                 ", ".join(str(g) for g in cl["denied_in_this_period"])))
    print("    differentiating electron: %s-block"
          % (rep["block_letter"] or "?"))
    print()
    d = rep["level_decoded"]
    print("  THE GROUND LEVEL, DECODED                                     [READ]")
    if d["form"] == "not predicted":
        print("    the entrant is predicted; the LEVEL is not. 2S, L and J "
              "are undetermined here.")
    elif d["form"] == "LS":
        print("    %-12s form LS   multiplicity %d (2S = %d)   L = %s (%d)   "
              "parity %s   J = %s (2J = %d)"
              % (rep["level"], d["mult"], d["S2"], TERM_L[d["L"]], d["L"],
                 d["parity"], d["J"], d["J2"]))
    elif d["form"] == "jj":
        print("    %-12s form jj (%s)   J = %s (2J = %d)   -- no LS term, so "
              "2S and L are not defined here"
              % (rep["level"], d.get("pair"), d["J"], d["J2"]))
    elif d["form"] == "J only":
        print("    %-12s only J is known: J = %s (2J = %d)"
              % (rep["level"], d["J"], d["J2"]))
    else:
        print("    %-12s not parsed" % rep["level"])
    print()
    print("  THE GROUND CONFIGURATION, PER SUBSHELL                        [READ]")
    print("    %-8s %-3s %-3s %-6s %-9s %-5s" %
          ("subshell", "n", "l", "occ", "capacity", "n+l"))
    for s in rep["configuration"]:
        print("    %-8s %-3d %-3d %-6d %-9d %-5d %s"
              % (s["subshell"], s["n"], s["l"], s["occupancy"],
                 s["capacity"], s["n+l"], "full" if s["full"] else ""))
    print()

    if show_channels and rep["channels"]:
        print("  THE RYDBERG CHANNELS -- the spectra index and the equation")
        print("    delta_eq is register 1205's channel equation [PINNED];")
        print("    delta is COORDINATES-2.13 [READ]; B is the Pauli bound [PINNED].")
        print()
        print("    %-4s %-4s %-3s %-5s %-4s %-4s %-4s %-9s %-9s %-9s %s"
              % ("chg", "Ne", "l", "mult", "p", "n0", "B", "delta_eq", "delta",
                 "resid", "grade"))
        shown = 0
        for ch in rep["channels"]:
            if max_charge is not None and ch["charge"] > max_charge:
                continue
            if ch["measured"]:
                for m in ch["measured"]:
                    flag = ""
                    if m["B_agrees"] is False:
                        flag += "  B_csv=%s DIFFERS" % m["B_csv"]
                    if m["B_csv_is_not_a_bound"]:
                        flag += "  B column is not a bound here"
                    if m["floor_le_B"] is False:
                        flag += "  PAULI BOUND VIOLATED"
                    print("    %-4d %-4d %-3d %-5d %-4s %-4s %-4s %-9s %-9s "
                          "%-9s %s%s"
                          % (ch["charge"], ch["Ne"], ch["l"], m["mult"],
                             _fmt(ch["p"]), _fmt(ch["n0"]),
                             _fmt(ch["B_computed"]),
                             _fmt(ch["delta_equation"]), _fmt(m["delta"]),
                             _fmt(m["residual"]), m["grade"], flag))
                    shown += 1
            else:
                print("    %-4d %-4d %-3d %-5s %-4s %-4s %-4s %-9s %-9s %-9s %s"
                      % (ch["charge"], ch["Ne"], ch["l"], "-", _fmt(ch["p"]),
                         _fmt(ch["n0"]), _fmt(ch["B_computed"]),
                         _fmt(ch["delta_equation"]), "-", "-",
                         "not in the index"))
                shown += 1
            if shown > 400:
                print("    ... truncated; use --charge or --json")
                break
        print()

    if show_channels and rep["channels"]:
        print("  THE TOWER -- Lambda_9 to Lambda_13, per Rydberg channel")
        print("    A tower cell extends a Lambda_8 transition by the target's")
        print("    multiplicity, its seniority and the J_c-K coupling chain")
        print("    (section 12.11.1). A Rydberg channel is that object: a core with")
        print("    fine structure 2J_c and one electron placed in l, so g = q = 1.")
        print("    Bounds are tower-2.py's; values are the coupling the core admits.")
        print()
        print("    %-4s %-3s %-7s %-4s %-5s %-5s %-4s %-6s %-9s %s"
              % ("chg", "l", "core", "k", "2S", "2S'", "v", "2J_c", "2K",
                 "2J   (levels)"))
        n = 0
        for ch in rep["channels"]:
            if max_charge is not None and ch["charge"] > max_charge:
                continue
            t = ch["tower"]
            if not t:
                continue
            ct = t["core_term"]
            k2 = t["L12_2K"]["value"]
            j2 = t["L13_2J"]["value"]
            levels = ("" if not j2 else
                      "  J = " + ", ".join(_halves(x) for x in j2))
            cap = ("" if t["L12_2K"].get("within_index_bound", True)
                   else "   2K OUTSIDE 7.4: f_max = %d bounds 2K <= %d"
                        % (CAPS["f"], (t["L11_2Jc"]["value"] or 0)
                           + 2 * CAPS["f"]))
            print("    %-4d %-3d %-7s %-4d %-5s %-5s %-4s %-6s %-9s %s%s%s"
                  % (ch["charge"], ch["l"],
                     LW1.GROUND[t["core_Ne"]][0]
                     if t["core_Ne"] in LW1.GROUND else "-",
                     t["k"], _fmt(t["L8_2S"]["value"]),
                     _fmt(t["L9_2Sprime"]["value"]),
                     _fmt(t["L10_v"]["value"]), _fmt(t["L11_2Jc"]["value"]),
                     ",".join(str(x) for x in k2) if k2 else "-",
                     ",".join(str(x) for x in j2) if j2 else "-", levels, cap))
            if ct["status"] == "UNDETERMINED":
                print("         core term UNDETERMINED: %s" % ct["basis"])
            n += 1
            if n >= 40:
                print("    ... truncated; use --charge or --json")
                break
        print()

    if rep["lambda8"]:
        print("  THE IONISATION LADDER AS LAMBDA_8 CELLS         [RECONSTRUCTED]")
        print("    A Lambda_8 cell is a transition (section 7). The mapping from an")
        print("    element to cells is not fixed by the store; this one is the")
        print("    ionisation ladder, and its status is carried, not flattened.")
        print()
        print("    %-10s %-26s %-8s %s"
              % ("step", "(n,l,k,q,e,f,g,2S)", "7 rules", "caps"))
        for row in rep["lambda8"][:24]:
            cell = row["cell"]
            held = sum(1 for c in row["constraints"] if c["holds"])
            over = [ax for ax, ok in row["within_caps"].items() if not ok]
            caps = ("within 7.4" if not over
                    else "OUTSIDE: needs " + ", ".join(
                        "%s>=%d" % (ax, row["caps_needed"][ax]) for ax in over))
            print("    %-10s %-26s %-8s %s"
                  % ("%s->%s" % (row["from"], row["to"]),
                     str(tuple("-" if v is None else v for v in cell)),
                     "%d/7" % held, caps))
        if len(rep["lambda8"]) > 24:
            print("    ... %d more; --json for all" % (len(rep["lambda8"]) - 24))
        print()


def report_axes():
    print("Every axis this tool populates, with where it comes from.")
    print()
    for name, status, note in AXES:
        print("  %-16s %-14s %s" % (name, status, note))
    print()
    print("  READ           a measurement, from a member or the mirror")
    print("  PINNED         the corpus defines it at the precision a program needs")
    print("  DERIVED        arithmetic on a READ or PINNED quantity")
    print("  RECONSTRUCTED  stated by the corpus but not in the form a program")
    print("                 needs; reconstructed, measured, and kept as such")
    return 0


# ---------------------------------------------------------------------------
# The equation, measured against the index
# ---------------------------------------------------------------------------

def equation_report(spectra, grades=("measured",), table="observed"):
    if not spectra.present:
        print("the spectra index is not in the tree: %s" % spectra.path)
        return 2
    rows = [r for r in spectra.rows if r["grade"] in grades]
    res, skipped = [], 0
    for r in rows:
        Z, c, l = int(r["Z"]), int(r["charge"]), int(r["l"])
        if (Z - c) >= 1 and (Z - c) not in LW1.GROUND:
            skipped += 1
            continue
        eq = channel_delta(Z, c, l, table)
        if eq is None:
            skipped += 1
            continue
        res.append((float(r["delta"]) - eq, float(r["delta"]), eq, l, r))
    if not res:
        print("no comparable channels")
        return 2
    n = len(res)
    rms = math.sqrt(sum(d * d for d, *_ in res) / n)
    mean = sum(v for _d, v, *_ in res) / n
    ss_tot = sum((v - mean) ** 2 for _d, v, *_ in res)
    ss_res = sum(d * d for d, *_ in res)
    r2 = 1 - ss_res / ss_tot if ss_tot else float("nan")
    med = sorted(abs(d) for d, *_ in res)[n // 2]
    print("the channel equation, final form (register 1205), against "
          "COORDINATES-2.13")
    print("  grades: %s   configurations: %s" % (", ".join(grades), table))
    print("  channels compared: %d   skipped (core outside the table): %d"
          % (n, skipped))
    print("  rms %.4f   R2 %.4f   median |error| %.4f" % (rms, r2, med))
    print()
    print("  by l:")
    for l in sorted({x[3] for x in res}):
        sub = [d for d, _v, _e, ll, _r in res if ll == l]
        print("    l = %d   n = %-5d rms %.4f"
              % (l, len(sub), math.sqrt(sum(d * d for d in sub) / len(sub))))
    print()
    print("  RECORDED at register 1205, on a different sample: 284 channels,")
    print("  Z = 2 to 90, charge 1 to 10, rms 0.1610, R2 0.9741, l >= 4 rms 0.0150.")
    print("  COORDINATES-2.13 now holds %d measured channels, so the samples are"
          % len([r for r in spectra.rows if r["grade"] == "measured"]))
    print("  not the same and the numbers are not expected to match exactly.")
    print("  G0c: where they disagree the finding is about the reconstruction.")
    return 0


def check_B(spectra):
    """The B column against both configuration tables. This is the finding."""
    if not spectra.present:
        print("the spectra index is not in the tree: %s" % spectra.path)
        return 2

    order = sorted(((n, l) for n in range(1, 9) for l in range(0, min(n, 5))),
                   key=lambda t: (t[0] + t[1], t[0]))

    def aufbau(Ne):
        out, left = [], Ne
        for n, l in order:
            if left <= 0:
                break
            take = min(2 * (2 * l + 1), left)
            out.append((n, l, take))
            left -= take
        return out

    obs = auf = n = 0
    both_wrong = []
    cores = {}
    for r in spectra.rows:
        b = csv_bound(r)
        if b is None:
            continue
        Z, c, l = int(r["Z"]), int(r["charge"]), int(r["l"])
        core = Z - c
        if not (1 <= core <= 108):
            continue
        n += 1
        o = pauli_bound(Z, c, l)
        a = pauli_bound(Z, c, l, config=aufbau(core))
        obs += (o == b)
        auf += (a == b)
        if o != b and a == b:
            cores[core] = cores.get(core, 0) + 1
        elif o != b and a != b:
            both_wrong.append((Z, c, l, o, a, b))

    print("COORDINATES-2.13's B column, against the two configuration tables")
    print()
    print("  rows with an integer B and a core inside the table: %d" % n)
    print("  B from the OBSERVED configurations (register 1306):  %6d  %.2f%%"
          % (obs, 100.0 * obs / n))
    print("  B from AUFBAU configurations:                        %6d  %.2f%%"
          % (auf, 100.0 * auf / n))
    print()
    print("  The B column was built on AUFBAU, and register 1306 withdrew that")
    print("  table: 'Every previous version built configurations by aufbau and")
    print("  patched exceptions by hand; that table was wrong at Pd ... and at Lr.'")
    print("  The spectra index has not been rebuilt on the observed table.")
    print()
    print("  cores where aufbau matches the column and observation does not:")
    for core, cnt in sorted(cores.items(), key=lambda kv: -kv[1])[:14]:
        sym, sh, _lv = LW1.GROUND[core]
        print("    Ne=%-4d %-3s %5d rows   observed %s" % (core, sym, cnt, sh))
    print()
    print("  rows neither table reproduces: %d" % len(both_wrong))
    for x in both_wrong[:5]:
        print("    Z=%d charge=%d l=%d  observed %s  aufbau %s  column %s" % x)
    floats = sum(1 for r in spectra.rows if csv_bound(r) is None)
    print()
    print("  and %d rows carry a NON-INTEGER B -- a dispersion, not a bound."
          % floats)
    print("  The column is overloaded; those rows are not compared.")
    return 0


# ---------------------------------------------------------------------------
# Self-test
# ---------------------------------------------------------------------------

def selftest(spectra):
    fails, checked = [], 0

    def check(cond, msg):
        nonlocal checked
        checked += 1
        if not cond:
            fails.append(msg)

    # --- the seated members, as imported -----------------------------------
    check(len(LW1.GROUND) == 108,
          "LW1-ground.py holds %d elements, register 1306 says 108"
          % len(LW1.GROUND))
    bad = [Z for Z in LW1.GROUND if LW1.occ_count(Z) != Z]
    check(not bad, "electron counts fail at %s; register 1306 says 108 of 108"
          % bad[:5])
    check(len(TOWER.L8()) == 976,
          "tower-2.py gives |L8| = %d at section 7.4's caps, expected 976"
          % len(TOWER.L8()))
    for d, want in ((9, 1654), (10, 2535), (11, 13585), (12, 70905),
                    (13, 199130)):
        got = len(TOWER.STAGES[d]())
        check(got == want, "|L%d| = %d, section 12.11.0.10 says %d"
              % (d, got, want))

    # --- the layout: chapter 6's ninety ------------------------------------
    main = [Z for Z in range(1, 119) if not set_aside(Z)]
    check(len(main) == 90,
          "the main table holds %d cells, section 6 says 90" % len(main))
    check(len({(period_of(Z), group_of(Z)) for Z in main}) == 90,
          "the ninety cells are not distinct in (period, group)")
    check(len([Z for Z in range(1, 119) if set_aside(Z)]) == 28,
          "the f-block rows set aside are not 28")
    for Z, want in ((1, (1, 1)), (2, (1, 18)), (3, (2, 1)), (10, (2, 18)),
                    (19, (4, 1)), (20, (4, 2)), (21, (4, 3)), (26, (4, 8)),
                    (36, (4, 18)), (57, (6, 3)), (72, (6, 4)), (86, (6, 18)),
                    (89, (7, 3)), (104, (7, 4)), (118, (7, 18))):
        got = (period_of(Z), group_of(Z))
        check(got == want, "Z=%d lands at %s, the layout puts it at %s"
              % (Z, got, want))
    check(group_of(58) is None and group_of(92) is None,
          "a lanthanide or actinide was given a main-table group")

    # --- blocks and the Janet coordinate -----------------------------------
    for Z, want in ((19, 0), (21, 2), (31, 1), (58, 3)):
        check(block_of(Z) == want,
              "Z=%d differentiates into block %s, expected %s"
              % (Z, block_of(Z), want))
    # Register 1188: the n+l = 5 block opens at Sc, 7 at La, 8 at Ac.
    for Z, want in ((21, 5), (57, 7), (89, 8)):
        cell = janet_cell(Z)
        check(cell is not None and cell[0] == want,
              "Z=%d sits in Janet block %s, register 1188 says n+l = %d"
              % (Z, cell, want))

    # --- the collapse thresholds, register 1188 ----------------------------
    # The ramp reaches exactly 0.5 at the Janet boundary, 0 four below it and
    # 1 four above -- inverted out of COORDINATES-2.13's computed column.
    for l, z0 in COLLAPSE_Z.items():
        check(collapse_C(z0, l) == 0.5,
              "C at the l=%d Janet boundary Z=%d is %s, not 0.5"
              % (l, z0, collapse_C(z0, l)))
        check(collapse_C(z0 - 4, l) == 0.0 and collapse_C(z0 + 4, l) == 1.0,
              "the l=%d ramp is not eight wide about Z=%d" % (l, z0))
    for Z, want in ((18, 0.125), (19, 0.25), (20, 0.375), (21, 0.5),
                    (25, 1.0), (17, 0.0)):
        check(abs(collapse_C(Z, 2) - want) < 1e-12,
              "C(%d, 2) = %s, the index inverts to %s"
              % (Z, collapse_C(Z, 2), want))
    check(collapse_C(50, 4) == 0.0 and collapse_C(50, 7) == 0.0,
          "C is non-zero above l = 3, where the index inverts to exactly 0")

    # --- the channel equation ----------------------------------------------
    # Register 5193: at Ne = 1 the (Ne-1)/Ne factor vanishes identically, for
    # every charge and every C(Z). The hydrogenic output is exactly zero and
    # no parameter can move it.
    for Z in (1, 20, 50, 92):
        for l in (0, 2, 3):
            d = channel_delta(Z, Z, l)          # charge = Z is one electron
            check(d == 0.0,
                  "hydrogenic channel Z=%d l=%d returns %r, register 1205 "
                  "says exactly zero" % (Z, l, d))
    check(channel_delta(19, 1, 0) > channel_delta(19, 1, 3),
          "the equation does not fall with l for K I")

    # --- the Pauli bound, and its reconstruction ---------------------------
    # He I ns: the core is 1s(1), so p = 1 and the first ENTIRELY unoccupied
    # ns is n = 2, giving B = 1. The other reading of n0 gives 0.
    check(pauli_bound(2, 1, 0) == 1,
          "He I ns has B = %s, COORDINATES-2.13 gives 1" % pauli_bound(2, 1, 0))
    check(pauli_bound(4, 1, 0) == 2, "Be I ns has B = %s, expected 2"
          % pauli_bound(4, 1, 0))

    # --- Lambda_8's seven constraints, on a known cell ---------------------
    inside = TOWER.L8()[0]
    check(all(h for _r, h, _o in lambda_constraints(inside)),
          "a cell of L8 fails one of section 7.1's seven constraints")
    check(len(lambda_constraints(inside)) == 7,
          "section 7.1 states seven constraints")
    bad_cell = (1, 1, 1, 1, 1, 0, 1, 1)          # l <= n-1 fails
    check(not lambda_constraints(bad_cell)[0][1],
          "the l <= n-1 constraint does not fire on a cell that breaks it")

    # --- R, imported rather than reimplemented -----------------------------
    _held_st, admitted = layout_closure()
    check(admitted is not None, "cypher.op_order returned no admitted set")
    if admitted is not None:
        E = len(admitted) - 90
        check(E == 36, "R admits %d cells over the ninety, so E = %d; "
                       "section 6 says 36" % (len(admitted), E))
        # Section 6 names the thirty-six exactly: (p1,g2)..(p1,g17),
        # (p2,g3)..(p2,g12) and (p3,g3)..(p3,g12).
        held = {(period_of(Z), group_of(Z)) for Z in main}
        denied = admitted - held
        want = ({(1, g) for g in range(2, 18)}
                | {(2, g) for g in range(3, 13)}
                | {(3, g) for g in range(3, 13)})
        check(denied == want,
              "the cells R admits and the table denies are not section 6's "
              "thirty-six; %d differ" % len(denied ^ want))

    # --- the evidentiary boundary at Z = 108 --------------------------------
    check(ground_of(108)["status"] == READ,
          "Hs at Z = 108 is not READ; it is the last measured element")
    check(ground_of(109)["status"] == PREDICTED,
          "Z = 109 is not PREDICTED; section VIII puts the boundary at 108")
    for Z, nl in ((110, (6, 2)), (112, (6, 2)), (113, (7, 1)),
                  (118, (7, 1)), (119, (8, 0)), (120, (8, 0))):
        check(entrant_of(Z) == nl,
              "the entrant at Z = %d is %s; section VIII says %s"
              % (Z, entrant_of(Z), nl))
    for Z in range(109, 121):
        g = ground_of(Z)
        check(g is not None, "no predicted configuration at Z = %d" % Z)
        if g:
            check(sum(o for _n, _l, o in g["config"]) == Z,
                  "the predicted configuration at Z = %d holds %d electrons"
                  % (Z, sum(o for _n, _l, o in g["config"])))
            check(g["level"] is None,
                  "a ground LEVEL is claimed at Z = %d; section VIII predicts "
                  "the entrant only" % Z)
    check(ground_of(121) is None,
          "a configuration is offered at Z = 121; the predictions stop at 120")
    # Og closes the 7p shell; 119 and 120 open 8s.
    og = {(n, l): o for n, l, o in ground_of(118)["config"]}
    check(og.get((7, 1)) == 6, "Og does not close 7p")
    check(og.get((8, 0)) is None, "Og has an 8s electron")
    check({(n, l): o for n, l, o in ground_of(120)["config"]}.get((8, 0)) == 2,
          "Z = 120 does not close 8s")

    # --- terms, phi-hat and the coupling chain ------------------------------
    for l, k, want in ((1, 2, {(0, 0), (0, 2), (2, 1)}),        # 1S 1D 3P
                       (1, 3, {(1, 1), (1, 2), (3, 0)}),        # 2P 2D 4S
                       (1, 1, {(1, 1)}),                        # 2P
                       (0, 2, {(0, 0)}),                        # 1S
                       (2, 2, {(0, 0), (0, 2), (0, 4),
                               (2, 1), (2, 3)})):               # 1S 1D 1G 3P 3F
        got = set(terms(l, k))
        check(got == want, "terms(l=%d, k=%d) = %s, the standard construction "
                           "gives %s" % (l, k, sorted(got), sorted(want)))
    check(terms(1, 6) == [(0, 0)], "a closed p shell is not 1S alone")

    # THE decisive fixture for the whole coupling chain: phi-hat computed from
    # the microstate enumeration must equal tower-2.py's hardcoded PHI.
    computed_phi = {k: phi_hat(k, lmax=CAPS["l"]) for k in TOWER.PHI}
    check(computed_phi == TOWER.PHI,
          "phi-hat computed from terms is %s; tower-2.py hardcodes %s"
          % (computed_phi, TOWER.PHI))

    # Seniority: a term first appearing at k' has v = k'.
    check(seniority(1, 1, 1, 1) == 1, "v of a one-electron shell is not 1")
    check(seniority(1, 2, 0, 0) == 0, "v of 1S in p^2 is not 0")
    check(seniority(1, 2, 2, 1) == 2, "v of 3P in p^2 is not 2")

    # Ground levels, in all three forms the store carries.
    for text, form, J2 in (("2S1/2", "LS", 1), ("1S0", "LS", 0),
                           ("4I*15/2", "LS", 15), ("(1/2,1/2)0", "jj", 0),
                           ("4", "J only", 8), ("5/2", "J only", 5)):
        d = parse_level(text)
        check(d["form"] == form and d["J2"] == J2,
              "level %r parsed as %s with 2J = %s, expected %s and %d"
              % (text, d["form"], d["J2"], form, J2))
    d = parse_level("4I*15/2")
    check(d["S2"] == 3 and d["L"] == 6 and d["parity"] == "odd",
          "4I*15/2 decodes to 2S=%s L=%s %s, expected 3, 6, odd"
          % (d["S2"], d["L"], d["parity"]))

    # K I: the alkali doublet, derived rather than looked up. An Ar core is
    # closed, so 2J_c = 0; the np channel couples to K = 1 and J = 1/2, 3/2 --
    # potassium's D lines -- and the ns channel to J = 1/2, which is exactly
    # the ground level LW1-ground.py reads, 2S1/2.
    t = tower_for_channel(19, 1, 1)
    check(t["L11_2Jc"]["value"] == 0, "K I's Ar core is not J = 0")
    check(t["L13_2J"]["value"] == [1, 3],
          "K I np gives 2J = %s, the D-doublet is 1 and 3"
          % t["L13_2J"]["value"])
    t0 = tower_for_channel(19, 1, 0)
    check(t0["L13_2J"]["value"] == [1],
          "K I ns gives 2J = %s, expected 1" % t0["L13_2J"]["value"])
    check(parse_level(LW1.GROUND[19][2])["J2"] == 1,
          "K's ground level is not J = 1/2")
    # At section 7.4's caps f_max = 1, so 2K <= 2J_c + 2 and only s and p
    # channels fit. The d channel must be reported outside, not truncated.
    check(tower_for_channel(19, 1, 1)["L12_2K"]["within_index_bound"],
          "K I np should sit inside the capped 2K bound")
    check(not tower_for_channel(19, 1, 2)["L12_2K"]["within_index_bound"],
          "K I nd should be reported OUTSIDE the capped 2K bound")

    # The whole coupling chain, against measurement. Where a configuration has
    # a closed or single open subshell, Hund on terms(l^k) must reproduce the
    # ground level NIST recorded -- 2S, L and J, all three. It does, 92 times
    # out of 92, which is the evidence that terms(), hund_ground_term() and
    # parse_level() agree with the physics and not merely with each other.
    hok = hbad = 0
    for Zi, (_sym, _sh, lvl) in LW1.GROUND.items():
        ct = core_term(LW1.expand(Zi))
        d = parse_level(lvl)
        if ct["status"] != DERIVED or d["form"] != "LS":
            continue
        if (ct["S2"], ct["L"], ct["J2"]) == (d["S2"], d["L"], d["J2"]):
            hok += 1
        else:
            hbad += 1
    check(hok + hbad >= 90, "only %d elements were available to test Hund "
                            "against the observed levels" % (hok + hbad))
    check(hbad == 0, "Hund on terms(l^k) misses the observed ground level for "
                     "%d of %d elements" % (hbad, hok + hbad))

    # --- the equation against the index it generated ------------------------
    # The p > 0 branch is register 1205's, coefficient for coefficient; the
    # p = 0 branch carries the RECOVERED ramp. Together they reproduce the
    # computed column of COORDINATES-2.13 -- which is the evidence that the
    # recovery is right, since nothing was fitted to it.
    if spectra.present:
        comp = [r for r in spectra.rows if r["grade"] == "computed"]
        for table, floor in (("aufbau", 0.980), ("observed", 0.970)):
            ok = tot = 0
            for r in comp:
                Z, c, l = int(r["Z"]), int(r["charge"]), int(r["l"])
                if not (1 <= Z - c <= 108):
                    continue
                got = channel_delta(Z, c, l, table)
                if got is None:
                    continue
                tot += 1
                ok += abs(got - float(r["delta"])) < 5e-4
            check(tot > 100000, "only %d computed rows compared" % tot)
            check(ok / tot >= floor,
                  "the equation reproduces %.3f%% of the computed column under "
                  "%s configurations, expected at least %.1f%%"
                  % (100.0 * ok / tot, table, 100 * floor))

    # --- the spectra index --------------------------------------------------
    if spectra.present:
        check(len(spectra.rows) == 104832,
              "COORDINATES-2.13 holds %d rows, coords.py's gate reads 104,832"
              % len(spectra.rows))
        wit = sum(1 for r in spectra.rows if r["witness"] == "witnessed")
        check(wit == 358, "witnessed rows: %d, expected 358" % wit)
        k1 = [r for r in spectra.channels(19, 1)]
        check(bool(k1), "no K I channels in the spectra index")
        # The B column is overloaded; exactly the 2026-08-14 NIST fetch rows
        # carry a float where a bound belongs.
        floats = [r for r in spectra.rows if csv_bound(r) is None]
        check(len(floats) == 25,
              "%d rows carry a non-integer B, expected 25" % len(floats))
        check(all(r["grade"] == "measured" for r in floats),
              "a non-measured row carries a non-integer B")
    else:
        print("  note: the spectra index is not in the tree; its fixtures are "
              "skipped")

    print("fixtures checked: %d  failed: %d" % (checked, len(fails)))
    for f in fails:
        print("  FAIL " + f)
    print()
    print("SELFTEST OK" if not fails else "SELFTEST FAILED")
    return 0 if not fails else 1


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Populate an element on every axis of every index.")
    ap.add_argument("--z", type=int)
    ap.add_argument("--element")
    ap.add_argument("--charge", type=int,
                    help="restrict to one spectroscopic stage; 1 is neutral")
    ap.add_argument("--spectra", default=DEFAULT_SPECTRA)
    ap.add_argument("--config", choices=sorted(CONFIG_TABLES),
                    default="observed",
                    help="which configuration table the derived quantities use: "
                         "'observed' is register 1306's, the store's; 'aufbau' "
                         "is the withdrawn one COORDINATES-2.13 was built on, "
                         "and reproduces the index as it stands")
    ap.add_argument("--max-charge", type=int, default=6,
                    help="stages to print in the channel table (default 6)")
    ap.add_argument("--no-channels", action="store_true")
    ap.add_argument("--axes", action="store_true")
    ap.add_argument("--equation", action="store_true")
    ap.add_argument("--check-B", dest="check_b", action="store_true")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)

    if args.axes:
        return report_axes()

    spectra = Spectra(args.spectra)

    if args.selftest:
        return selftest(spectra)
    if args.equation:
        return equation_report(spectra, table=args.config)
    if args.check_b:
        return check_B(spectra)

    Z = args.z
    if Z is None and args.element:
        Z = SYMBOL_TO_Z.get(args.element)
        if Z is None:
            ap.error("unknown element %r" % args.element)
    if Z is None:
        ap.error("name an element with --element or --z")

    try:
        rep = populate(Z, spectra, args.charge, args.config)
    except KeyError as exc:
        print(exc.args[0], file=sys.stderr)
        return 2

    if args.json:
        json.dump(rep, sys.stdout, indent=2, default=str)
        print()
        return 0
    report(rep, show_channels=not args.no_channels,
           max_charge=args.charge or args.max_charge)
    return 0


if __name__ == "__main__":
    sys.exit(main())
