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
SYMBOL_TO_Z = {sym: z for z, (sym, _c, _l) in LW1.GROUND.items()}

# ---------------------------------------------------------------------------
# The periodic table, laid out as chapter 6 lays it out
# ---------------------------------------------------------------------------

# Section 6: "main-table cells (lanthanides and actinides set aside) = 90".
PERIOD_END = [2, 10, 18, 36, 54, 86, 118]
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
    return i + 1


def block_of(Z):
    """The block, from the DIFFERENTIATING electron -- the subshell that
    distinguishes Z from Z-1. This is the Loewdin construction's own object,
    and it is why the block is a fact about filling rather than about the
    drawn layout."""
    if Z == 1:
        return 0
    if Z not in LW1.GROUND or Z - 1 not in LW1.GROUND:
        return None
    now = {(n, l): o for n, l, o in LW1.expand(Z)}
    before = {(n, l): o for n, l, o in LW1.expand(Z - 1)}
    gained = [(n, l) for (n, l), o in now.items() if o > before.get((n, l), 0)]
    if not gained:
        return None
    return sorted(gained)[-1][1]


def janet_cell(Z):
    """Janet's coordinate IS n+l (register 1188), so its blocks ARE the
    collapse boundaries. The cell is (n+l, l) of the differentiating electron."""
    if Z == 1:
        return (1, 0)
    now = {(n, l): o for n, l, o in LW1.expand(Z)}
    before = {(n, l): o for n, l, o in LW1.expand(Z - 1)}
    gained = [(n, l) for (n, l), o in now.items() if o > before.get((n, l), 0)]
    if not gained:
        return None
    n, l = sorted(gained)[-1]
    return (n + l, l)


# ---------------------------------------------------------------------------
# The Pauli bound -- register 1141, PINNED
# ---------------------------------------------------------------------------

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
    if Ne < 1:
        return None
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
    for charge in range(2, min(Z, 108) + 2):
        Ne = Z - charge + 1
        if Ne < 1 or Ne not in LW1.GROUND or (Ne + 1) not in LW1.GROUND:
            continue
        parent = {(n, l): o for n, l, o in LW1.expand(Ne + 1)}
        child = {(n, l): o for n, l, o in LW1.expand(Ne)}
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
            "from": LW1.GROUND[Ne + 1][0], "to": LW1.GROUND[Ne][0],
            "cell": (sn, sl, k, q, tn, tl, g, None),
        })
    return out


# ---------------------------------------------------------------------------
# The report
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# THE SERIES LIMIT -- the twenty-sixth axis
# ---------------------------------------------------------------------------
# "The ionisation limit. Writing it as a formula is the single most damaging
# thing that can be done to a channel" -- and register 3249 is what happens
# when it is: Li III's limit was recorded as the bare Coulomb Z^2 R and the
# whole channel set moved when it was fitted from the series instead. So the
# limit is READ or FITTED, NEVER computed, and a species with neither is not
# given one. Register 2469's ruling stands: a defect is meaningless without a
# limit, so an absent limit means levels-only, not a guess.
#
# Keyed by (Z, charge) with charge the spectroscopic stage, 1 = neutral.
# (value cm^-1, sigma or None, status, provenance)
LIMITS = {
    (3, 3):  (987662.29,   0.36,  "FITTED",
              "P.converge over 81 levels; register 3249"),
    (5, 4):  (2091995.451, None,  "READ",
              "printed under the B IV table; register 3313"),
    (5, 5):  (2744111.38,  1.95,  "FITTED",
              "not in the capture, fitted; register 3313"),
    (15, 4): (415551.8,    350.0, "FITTED",
              "four-member 3s.ns 3S run; register 3401"),
}

# Deficits against the REDUCED-MASS Coulomb baseline Z^2 R_M, as banked in
# register 3357. Be IV's limit is not quoted anywhere as a limit, only as this
# deficit, so it is carried here and its limit is DERIVED rather than FITTED --
# the one place this file reconstructs a limit, and it is labelled.
DEFICITS_RM = {(3, 3): 103.94, (4, 4): 329.80, (5, 5): 816.68}

# Register 3353: the deficit IS the Sommerfeld-Dirac relativistic term less the
# 1s Lamb shift, and the ratio is constant to under one per cent.
DIRAC_RATIO = 0.8849
DIRAC_RATIO_SD = 0.0069

R_INF = 109737.31568          # cm^-1, CODATA
ALPHA_FS = 7.2973525693e-3
M_E_U = 5.48579909065e-4
# Masses of the nuclides the fits used, in u. READ, not computed.
NUCLIDE_U = {3: 7.0160034366, 4: 9.0121830700, 5: 11.0093054000,
             15: 30.97376199842, 56: 137.9052470}


def reduced_rydberg(Z):
    """R_M for this element's nuclide. Register 3357 needed the reduced mass
    TWICE -- once in the defect formula and once in the baseline a limit is
    compared against -- and a baseline missing it produced an apparent Z^6.4."""
    if Z not in NUCLIDE_U:
        return None
    return R_INF / (1.0 + M_E_U / NUCLIDE_U[Z])


def dirac_term(Z):
    """The Sommerfeld-Dirac 1s relativistic term, Z^4 alpha^2 R_M / 4."""
    rm = reduced_rydberg(Z)
    return None if rm is None else rm * Z ** 4 * ALPHA_FS ** 2 / 4.0


def series_limit(Z, charge):
    """(value, sigma, status, provenance) for this stage, or None.

    None is the honest answer and the common one: four stages are banked out of
    every stage of every element. Register 2469 withdrew ten channels built on
    an invented limit, so nothing is invented here.
    """
    if (Z, charge) in LIMITS:
        return LIMITS[(Z, charge)]
    if (Z, charge) in DEFICITS_RM:
        rm = reduced_rydberg(Z)
        if rm is not None:
            return (Z * Z * rm + DEFICITS_RM[(Z, charge)], None, "DERIVED",
                    "reconstructed from register 3357's banked deficit")
    return None


def limit_deficit(Z, charge):
    """The QED-and-relativistic deficit against Z^2 R_M, and what it is made of.

    Returns (deficit, dirac, ratio) or None. This is the one place exotic matter
    is measurably present on the periodic index: the deficit is the relativistic
    term less the 1s Lamb shift, of which vacuum polarisation is a part.
    """
    if (Z, charge) in DEFICITS_RM:
        d = DEFICITS_RM[(Z, charge)]
    else:
        lim = series_limit(Z, charge)
        rm = reduced_rydberg(Z)
        if lim is None or rm is None or lim[2] == "DERIVED":
            return None
        d = lim[0] - Z * Z * rm
    dt = dirac_term(Z)
    return None if dt is None else (d, dt, d / dt)


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
    ("Lambda_8 cell", RECON, "the ionisation ladder as transitions; see ionisation_cells"),
    ("caps", PINNED, "section 7.4's (n,e,l,k,f) = (3,3,1,3,1)"),
    ("series limit", READ, "the measured ionisation limit; READ or FITTED per "
                           "registers 3249/3313/3401, never computed. The "
                           "defect's own denominator, and where the QED sits "
                           "(register 3253). None where unbanked."),
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
    if Z not in LW1.GROUND:
        raise KeyError("Z = %d is outside LW1-ground.py's table (1 to 108)" % Z)
    sym, shells, level = LW1.GROUND[Z]
    cfg = LW1.expand(Z)
    out = {
        "Z": Z, "symbol": sym, "shells_as_printed": shells, "level": level,
        "electron_count": LW1.occ_count(Z),
        "electron_count_ok": LW1.occ_count(Z) == Z,
        "configuration": [{"n": n, "l": l, "subshell": "%d%s" % (n, LSYM[l]),
                           "occupancy": o, "capacity": 2 * (2 * l + 1),
                           "full": o == 2 * (2 * l + 1), "n+l": n + l}
                          for n, l, o in cfg],
        "period": period_of(Z), "group": group_of(Z), "block": block_of(Z),
        "block_letter": (LSYM[block_of(Z)] if block_of(Z) is not None else None),
        "set_aside": set_aside(Z), "janet_cell": janet_cell(Z),
        "outer": LW1.outer(Z),
    }
    stage = charge if charge is not None else 1
    lim = series_limit(Z, stage)
    out["series_limit"] = None if lim is None else {
        "value": lim[0], "sigma": lim[1], "status": lim[2], "source": lim[3]}
    dfc = limit_deficit(Z, stage)
    out["limit_deficit"] = None if dfc is None else {
        "deficit": dfc[0], "dirac": dfc[1], "ratio": dfc[2],
        "baseline": "Z^2 R_M (reduced mass), register 3357"}

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


def _fmt(v, nd=4):
    return "-" if v is None else ("%.*f" % (nd, v) if isinstance(v, float)
                                  else str(v))


def report(rep, show_channels=True, max_charge=None):
    print("=" * 78)
    print("  Z = %-4d %-3s   %s" % (rep["Z"], rep["symbol"],
                                    rep["shells_as_printed"]))
    print("  ground level %s   electrons %d %s"
          % (rep["level"], rep["electron_count"],
             "OK" if rep["electron_count_ok"] else "MISMATCH"))
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
    sl = rep.get("series_limit")
    print()
    print("  THE SERIES LIMIT -- the 26th axis")
    if sl is None:
        print("    NOT BANKED for this stage. Register 2469: a defect is")
        print("    meaningless without a limit, so this is levels-only, not a")
        print("    guess. Four stages are banked in the whole table.")
    else:
        print("    limit = %.3f%s cm^-1   [%s]"
              % (sl["value"],
                 "" if sl["sigma"] is None else " +/- %.2f" % sl["sigma"],
                 sl["status"]))
        print("    %s" % sl["source"])
        df = rep.get("limit_deficit")
        if df is not None:
            print("    deficit against Z^2 R_M = %+.2f cm^-1" % df["deficit"])
            print("    Sommerfeld-Dirac term   = %+.2f cm^-1" % df["dirac"])
            print("    ratio = %.4f   [register 3353: 0.8849 +/- 0.0069 over Z=3,4,5]"
                  % df["ratio"])
            print("    THE DEFICIT IS THE RELATIVISTIC TERM LESS THE 1s LAMB SHIFT.")
            print("    That is where QED -- and so vacuum polarisation -- sits on")
            print("    this index: in the LIMIT, not in the levels (register 3253).")

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

    # --- the twenty-sixth axis: the series limit ---------------------------
    check(any(a[0] == "series limit" for a in AXES),
          "the series limit is an axis")
    check(len(AXES) == 26, "twenty-six axes")

    # Every banked limit is READ or FITTED. Nothing is computed, which is the
    # whole point of the axis -- register 3249's fault was a computed limit.
    for key, (val, sig, st, src) in LIMITS.items():
        check(st in ("READ", "FITTED"), "banked limit %r is READ or FITTED" % (key,))
        check(val > 0 and src, "banked limit %r carries a value and a source" % (key,))
    check(series_limit(3, 3)[0] == 987662.29, "Li III's fitted limit, register 3249")
    check(series_limit(5, 5)[0] == 2744111.38, "B V's fitted limit, register 3313")
    check(series_limit(5, 4)[2] == "READ", "B IV's limit was printed, not fitted")

    # An unbanked stage returns None rather than a guess. Register 2469
    # withdrew ten channels built on an invented limit.
    check(series_limit(6, 1) is None, "an unbanked stage returns None, not a guess")
    check(series_limit(56, 4) is None, "Ba IV is not banked here either")

    # Register 3249: the deficit against the BARE Coulomb baseline is 26.45.
    check(abs((987662.29 - 9 * R_INF) - 26.45) < 0.01,
          "the bare-Coulomb deficit is register 3249's 26.45")

    # Register 3357: against the REDUCED-MASS baseline the deficits are
    # 103.94, 329.80, 816.68 and the Z^4 law holds. Two independent checks.
    for (Z, ch), want in DEFICITS_RM.items():
        lim = series_limit(Z, ch)
        if lim is not None and lim[2] != "DERIVED":
            got = lim[0] - Z * Z * reduced_rydberg(Z)
            check(abs(got - want) < 2.0,
                  "Z=%d deficit reproduces register 3357's %.2f" % (Z, want))

    # Register 3353: deficit = Sommerfeld-Dirac term LESS the 1s Lamb shift,
    # ratio constant to under one per cent across Z = 3, 4, 5.
    ratios = [DEFICITS_RM[k] / dirac_term(k[0]) for k in sorted(DEFICITS_RM)]
    check(all(abs(r - DIRAC_RATIO) < 0.02 for r in ratios),
          "every ratio is within 0.02 of register 3353's 0.8849")
    mean = sum(ratios) / len(ratios)
    check(abs(mean - DIRAC_RATIO) < 0.001,
          "and their mean IS 0.8849 (register 3353)")
    check(abs(dirac_term(3) - 118.32) < 0.05, "Li III's Dirac term, register 3353")
    check(abs(dirac_term(4) - 373.97) < 0.05, "Be IV's Dirac term, register 3353")
    check(abs(dirac_term(5) - 913.03) < 0.05, "B V's Dirac term, register 3353")

    # The baseline matters: register 3357 records that missing the reduced mass
    # produced an apparent Z^6.4 against a leading Dirac Z^4. Pin the fault so
    # the wrong baseline cannot creep back.
    bare = [(987662.29 - 9 * R_INF), None, (2744111.38 - 25 * R_INF)]
    check(abs(bare[0] - 26.45) < 0.01 and abs(bare[2] - 678.49) < 1.0,
          "the bare-baseline deficits are 26.45 and 678.49")
    import math as _m
    bad = _m.log(bare[2] / bare[0]) / _m.log(5.0 / 3.0)
    good = _m.log(DEFICITS_RM[(5, 5)] / DEFICITS_RM[(3, 3)]) / _m.log(5.0 / 3.0)
    check(bad > 6.0, "the wrong baseline really does imply about Z^6.4")
    check(abs(good - 4.0) < 0.1, "and the right one recovers the Z^4 law")

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
