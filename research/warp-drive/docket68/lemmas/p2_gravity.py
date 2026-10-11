#!/usr/bin/env python3
"""p2_gravity.py -- item 223: a second position 2 (position 2b), separate from item 221's.  M: "build another separate
position 2 that separates our universe by one law other than the madelung exceptions ... Perhaps the law you choose to
change could give us more insights into σ, the offset, G, ℓ and m".  Worked in the conversation; 2026-10-11.

What changes: the bulk's gravitational coupling, kappa5^4 = 2 x ours (H-G5-PER-UNIVERSE for position 2b only).  sigma,
the offset and every matter law are ours.  Position 2a (items 219/221) changes matter at fixed gravity; position 2b
changes gravity at fixed matter.  So the two differ from ours, and from each other, in independent ways.

  Y0 (read) M's words (item 223, verbatim in the rulings file).  The relations are the theorem's own:
     - SMS (19), G = kappa5^4 sigma / (48 pi), and SMS (18) in b1_matter.py's form, Lambda4 = (Lambda5 + kappa^4
       lambda^2/6)/2;
     - ell^2 = 3c^4 / (4 pi G (sigma - 2 delta sigma)), with item 201's delta sigma = rho_Lambda c^2;
     - the corridor, E = sqrt(N h c^5 ln2 / (8 pi^2 G)), m = GE/c^4, A_bit = 2hG ln2/(pi c^3);
     - MK (41), V ~ GM/r (1 + 2 ell^2/(3 r^2)), and Adelberger's |beta_3| <= 1.3e-4, as B6P-SCALE reads them (the
       table-top floor ell <= 13.964 um);
     - for stars, Eddington's radiative L ~ G^4 M^3 and the Chandrasekhar mass ~ (hbar c / G)^(3/2) (READ, Wikipedia,
       retrieved 2026-10-11; CHANDRA_READ, ML_READ below);
     - the record's three values for position 2's G, from g2_between.py: +2 per sheet, +6 on the doubled count, -1/4 on
       the one-plane law.
  Y1 (computed; cypher) The choice.
     - Stage 1: seven candidate laws, each on its own grid (the parameter at 1/2, 1 and 2 x ours; N = 1, 2, 4, 8), in
       exact rationals with pi and ln2 factored out.  The moves over (sigma, offset, G, ell, m) are: identity 00000,
       kappa5 00111, sigma-setter 10111, offset 01010, bit-area 00001, h 00001, c 00011.  All five operator-bearing
       languages give the same binary on every row, and no index has a key.
     - The offset moves ell only through 2 delta sigma / sigma, at most 7.08e-63 across the window.  A pipeline at 12
       significant figures reads the offset's row as 01000 (mutant float_compare): exact values are needed (209).
     - Stage 2: one index over the candidates, with P2a as a control.  Its six coordinates are the five moves and
       "leaves matter ours" (h and c move alpha, item 222).  It has 8 cells, no two candidates share one, the audit is
       clean, and moves_offset and moves_G add nothing.  E: order 6, algebra 6, geometry 3, information 4, statistics
       3; analysis is NOT-RUN and documentary SILENT, never silently dropped.
     - The rule: sigma and the offset kept (item 201's values), matter ours, and the most of the five moved.  It picks
       kappa5 alone, which moves 3 of the five (G, ell, m).  The target "sigma, offset kept; G, ell, m moved; matter
       ours" is held by kappa5 and admitted by all five languages.
     - "All five moved, matter ours" and "the offset moved with G, matter ours" are held by no candidate.  Geometry
       and statistics refuse both; order, algebra and information admit them by joining rows, not as a held law.
       With the record's 139 (1) plane added (per sheet, 11111), the index has 9 cells and the plane holds both, every
       language admitting.  So no single law in the record moves the offset with G; only the plane, a change of
       values, moves all five.
     - Held at Lambda4 instead of rho_Lambda (mutant lambda4_held), the offset would move with kappa5 and the rule
       would pick bit-area.  The choice rests on 201's delta sigma = rho_Lambda c^2.
  Y2 (deduced; computed at the window's floor; every ratio is independent of sigma) Position 2b's gravitational sector.
     - G x 2; ell x 1/sqrt 2 (0.707107); k = 1/ell x sqrt 2.
     - Lambda4 = 8 pi G delta sigma / c^4 x 2.  Lambda5 = -6/ell^2 x 2 in b1_matter.py's geometric form; the bulk's
       vacuum energy density, SMS's own Lambda = Lambda5 / kappa5^2, x sqrt 2.
     - The short-range term relative to Newton's, 2 ell^2/(3 r^2), x 1/2.  But the absolute term 2 G M ell^2 / (3 r^3)
       is x 1: G ell^2 = 3c^4 / (4 pi (sigma - 2 delta sigma)) depends on sigma and the offset alone.
     - Read in position 2b against its own G, the same relative bound admits sigma down to 7.41e52 J/m^3, half our
       floor of 1.48e53 (DEDUCED, on the same relative sensitivity).
  Y3 (computed) The corridor at fixed N under position 2b's own G.
     - E1: 4.594040e8 -> 3.248477e8 J (x 1/sqrt 2).
     - m1: 3.795926e-36 -> 5.368249e-36 m (x sqrt 2).
     - A_bit: 7.242779e-70 -> 1.448556e-69 m^2 (x 2).
     - sigma_P = c^7/(hbar G^2): 4.6329e113 -> 1.1582e113 J/m^3 (x 1/4).
     - N_max = sigma_P / (8 ln2 delta sigma), the Schwarzschild-de Sitter (Nariai) cap and a third of the de Sitter
       horizon's bits (checked): 1.5918e122 -> 3.9795e121 (x 1/4).
     - (ell/m)^2 = (3/ln2)(sigma_P/sigma)/N falls by 4 at fixed sigma and N, so ell/m x 1/2.
     - The README the assembly ceiling (1.1947e10 J) can write: 676.3 -> 1352.6 bits.  Energy buys twice the bits.
     - A trip from ours to position 2b under 203's one E gives m2/m = 2 and a capacity of 2N (g2_between G3).  These
       are the per-sheet values, realised here by a law rather than by a count.  J5's m2 = m holds for glued bulks only
       (item 215).
  Y4 (computed) Matter is ours.  No atomic, molecular or solid value moves, and every equation of state is item 221's
     under our law.  Gravity's share of hydrogen's binding, G m_e m_p / (e^2/(4 pi eps0)), is 4.408e-40 -> 8.816e-40.
  Y5 (computed) Bodies: 1e22 kg of one metal, cold and hydrostatic, on item 221's BM3 fits, integrated by RK4.
     - Position 2b against ours, for Cu / Ag / Au: g x 2.016 / 2.026 / 2.035; R -0.40 / -0.64 / -0.85 %; mean density
       +1.2 / +2.0 / +2.6 %; central pressure x 2.06 / 2.09 / 2.11.
     - Gravity's change acts through G, with the body's extra compression second; the softer the metal, the larger
       that term.  Position 2a's change acts through the metal's density: g +4.2 / +14.3 / +0.8 % (min) and +8.4 /
       +24.6 / +2.2 % (mirror), with G unchanged.
     - Every central pressure lies inside the pressures its banked rows reach (Ag 2b at 91 %, Au 2b at 94 %).  An
       Earth-mass body is out of reach; no row approaches 360 GPa.
     - These bodies are compressible.  Item 221's 4.3 / 8.6 % (Cu) and 15 / 26 % (Ag) were uniform bodies at zero
       pressure.
  Y6 (deduced from READ scalings; ESTIMATE as stars) A star of fixed mass, with matter ours.
     - L x 16; main-sequence lifetime (~M/L) x 1/16, so a 10 Gyr star lasts 0.625 Gyr.
     - Chandrasekhar mass x 2^-1.5 = 0.3536.
     - At 1 AU: year x 0.7071, insolation x 16, equilibrium temperature x 2; equal insolation at 4 AU.
     - L ~ G^4 is the radiative, constant-opacity scaling; convective envelopes and ignition thresholds are not
       modelled.
  Y7 (not computed) Cosmology.  With rho_Lambda held, Lambda4 doubles and the de Sitter radius shrinks by 1/sqrt 2.
     H^2 = 8 pi G rho / 3 doubles at the same densities.  The expansion history, BBN and structure formation are not
     computed.
  Y8 (deduced; computed) What the three universes say about sigma, the offset, G, ell and m.
     - In SI, neither position 2 moves sigma or the offset, so item 201's two coordinates make ONE cell of ours, 2a and
       2b (mutant sigma_moves makes two).
     - In each universe's own Planck units, position 2b has sigma/sigma_P and delta sigma/sigma_P x 4, ell/l_P x 1/2
       and alpha_G = G m_p^2/(hbar c) x 2.  Ours has sigma/delta sigma, E1/E_P = m1/l_P = sqrt(ln2/(4 pi)) and every
       matter ratio, and so do both positions 2.
     - So 201's coordinates in Planck units make two cells: 2b apart, 2a still with ours.  Whether 201's defining
       numbers are SI values or Planck-unit values decides whether a kappa5 universe is a different cell.  That is
       recorded for the board, not decided.
     - sigma is read by the absolute short-range term whatever kappa5 is; kappa5 trades G against ell along G ell^2 =
       constant.
     - The offset enters ell at 7e-63, but in Planck units it sets the bit budget: N_max ~ sigma_P / delta sigma.
     - The corridor is the same object in every universe's own Planck units.  G sets only its SI scale.
  Y9 (recorded, not resolved) Tensions in the record.
     - Which universe's G sets E on a trip is undecided; Y3 gives both.
     - The record holds three values for position 2's G (+2, +6, -1/4) against G2 = G in items 218-221.  Position 2b
       takes +2, by a law.
     - H-ONE-G5 is set aside for position 2b only (223 (c)).
     - J5's m2 = m stands for glued bulks; item 215 withdraws it for M's configuration.
     - The offset is held at rho_Lambda, not at Lambda4 (Y1).
     - 201's coordinates are unit-dependent (Y8).

What this does not show.
  - No bulk solution for position 2b is computed.  The ratios are the theorem's relations at fixed sigma and offset.
  - Stars are READ scalings, not models.  Friedmann histories and BBN are not computed.
  - Bodies above about 30 GPa of central pressure are out of the banked equations of state.
  - Whether kappa5 can differ between cells of one bulk index is the board's reading (H-G5-PER-UNIVERSE), not a result.

Reads data/p2_matter_rows.json through p2_matter.py; tools/cypher.py, sigma_cypher.py and index_audit.py by path; and
the rulings file, b6p_scale.py and g2_between.py as text (all read-only).  Stdlib.
python3 p2_gravity.py [--selftest | --mutants]
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
MUT = {}
M223 = ("The next step is to build another separate position 2 that separates our universe by one law other than the "
        "madelung exceptions. 2 position 2s that are different from our universe and each other will give as a lot more "
        "to measure. Perhaps the law you choose to change could give us more insights into σ, the offset, G, ℓ and m")
# READ (Wikipedia, retrieved 2026-10-11 through the web connectors)
CHANDRA_READ = ("M_limit = (omega3^0 sqrt(3 pi) / 2) (hbar c / G)^(3/2) / (mu_e m_H)^2; about 1.44 M_sun for mu_e near 2",
                "https://en.wikipedia.org/wiki/Chandrasekhar_limit")
ML_READ = ("L ~ (1/15) (2 pi^3 / (9 5^5)) G^4 m_e^2 m_n^5 / (alpha^2 hbar^5) M^3 (Eddington's radiative derivation)",
           "https://en.wikipedia.org/wiki/Mass%E2%80%93luminosity_relation")

# SI: c, h exact; G CODATA 2018 as exactE.py carries it; rho_Lambda the record's (sigma_defines.py, Planck via cosmo.py)
C = 299792458.0
H = 6.62607015e-34
HBAR = H / (2 * math.pi)
G = 6.67430e-11
RHO_L = 5.84e-27                                   # kg/m^3
DSIG = RHO_L * C ** 2                              # the offset, item 201: delta sigma = rho_Lambda c^2 (J/m^3)
SIGMA_WINDOW = (1.482e53, 2.748e112)               # sigma_cypher.py W1 (J/m^3)
LN2 = math.log(2.0)
Q4 = 2                                             # position 2b: kappa5^4 = 2 x ours, so G2b = 2 G (the per-sheet value)
ASSEMBLY_MAX_J = 1.1947e10                         # warptheorem.py (LOOSE.md L1): the matter-side assembly ceiling


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


# ------------------------------------------------------------------------------------------- the choice, via the cypher
# Exact squares with pi and ln2 factored out, so every coordinate is an exact rational and monotone in the physical value
# (the cypher reader's recipe): 48 pi G = K s (K = kappa5^4, s = sigma); ell^2 = 36 c^4 / (K s (s - 2 ds)) from
# ell^2 = 3c^4 / (4 pi G (sigma - 2 delta sigma)); m^2 (8 pi^2 c^3 / ln2) = f N h G, i.e. m2' = f N h K s / c^3.
OURS = dict(K=F(7), s=F(1482, 1) * 10 ** 50, ds=F(5249, 10 ** 13), h=F(662607015, 10 ** 17), c=F(299792458), f=F(1))
LAWS = {"identity": None, "kappa5": "K", "sigma-setter": "s", "offset": "ds", "bit-area": "f", "h": "h", "c": "c"}
STAGE1_COORDS = ["law", "N", "sigma", "offset", "G48pi", "ell2", "m2"]


def warp_values(p, N):
    if MUT.get("lambda4_held"):              # hold Lambda4 = 8 pi G ds / c^4 instead of the offset ds (the pilot's flip)
        ds = OURS["ds"] * (OURS["K"] * OURS["s"]) / (p["K"] * p["s"]) * (p["c"] / OURS["c"]) ** 4
    else:
        ds = p["ds"]
    Gq = p["K"] * p["s"]
    ell2 = 36 * p["c"] ** 4 / (p["K"] * p["s"] * (p["s"] - 2 * ds))
    m2 = p["f"] * N * p["h"] * p["K"] * p["s"] / p["c"] ** 3
    row = [p["s"], ds, Gq, ell2, m2]
    if MUT.get("float_compare"):             # a tolerance pipeline: values rounded to 12 significant figures
        row = [F(float("%.12g" % float(v))) for v in row]
    return row


def stage1(cy, sc, ia):
    """one universe grid per law (parameter at 1/2, 1, 2 of ours; N = 1, 2, 4, 8): the move binaries measured"""
    out = {}
    for name, key in LAWS.items():
        cells = []
        for i, mu in enumerate((F(1, 2), F(1), F(2))):
            p = dict(OURS)
            if key:
                p[key] = OURS[key] * mu
            for N in (1, 2, 4, 8):
                cells.append([i, N] + warp_values(p, N))
        vo = {c: sorted({row[j] for row in cells}) for j, c in enumerate(STAGE1_COORDS)}
        ix = cy.Index(name, STAGE1_COORDS, cells, value_order=vo)
        moves = {X: not sc.fixed_by(cy, ix, X, ["N"]) for X in STAGE1_COORDS[2:]}
        per_lang = {}
        for lang in ("order", "algebra", "geometry", "information", "statistics"):
            adm, _ = cy.ADMISSION[lang][0](ix, {"algebra_budget": 10 ** 6, "statistics_order": 2})
            if adm is None:
                per_lang[lang] = None
                continue
            bits = ""
            for j in range(2, len(STAGE1_COORDS)):
                seen = {}
                for cl in adm:
                    seen.setdefault(cl[1], set()).add(cl[j])
                bits += str(int(any(len(v) > 1 for v in seen.values())))
            per_lang[lang] = bits
        audit = ia.audit_index(STAGE1_COORDS, [tuple(c) for c in cells])
        out[name] = dict(moves="".join(str(int(moves[X])) for X in STAGE1_COORDS[2:]), per_lang=per_lang,
                         cells=len(ix.cells), box=ix.box, keys=audit["keys"])
    return out


STAGE2_COORDS = ["moves_sigma", "moves_offset", "moves_G", "moves_ell", "moves_m", "leaves_matter"]
# the board's reading beside the measured move binaries: which candidates leave matter ours (h and c move alpha, and
# P2a is the Madelung change itself); item 201 makes sigma and the offset defining VALUES, so a candidate that moves
# either is a change of value, not of law (202), and the rule below excludes it
MATTER = {"identity": 1, "kappa5": 1, "sigma-setter": 1, "offset": 1, "bit-area": 1, "h": 0, "c": 0}
RECORD_ROWS = {"P2a (control)": ("00000", 0),                         # no_madelung N7: none of the five moves
               # 139 (1): sigma -> -sigma/4; COUNT-CYPHER per sheet: G -> 2G; B6: k_R = k_L/2, so ell -> 2 ell;
               # g2_between G3: m -> 2m.  The record states no offset for position 2's plane, so both codings are run
               "139 (1) plane, per sheet, offset moved (unstated)": ("11111", 1),
               "139 (1) plane, per sheet, offset held (unstated)": ("10111", 1)}
PLANES = [k for k in RECORD_ROWS if k.startswith("139")]
TARGETS = {"the rule: sigma, offset kept; G, ell, m moved; matter ours": ((0, 0, 1, 1, 1, 1),),
           "all five moved, matter ours": ((1, 1, 1, 1, 1, 1),),
           "the offset moved with G, matter ours": tuple((a, 1, 1, b, c, 1) for a in (0, 1) for b in (0, 1) for c in (0, 1))}


def _index_readout(cy, ia, rows, name):
    cells = sorted(set(rows.values()))
    ix = cy.Index(name, STAGE2_COORDS, [list(c) for c in cells], value_order={c: [0, 1] for c in STAGE2_COORDS})
    runs = {r: cy.run(ix, r, {"statistics_order": 2, "algebra_budget": 10 ** 6}) for r in ("1173", "33.1", "20.2")}
    admits = {}
    for tname, codes in TARGETS.items():
        a = {}
        for lang in ("order", "algebra", "geometry", "information", "statistics"):
            adm, _ = cy.ADMISSION[lang][0](ix, {"statistics_order": 2, "algebra_budget": 10 ** 6})
            a[lang] = None if adm is None else any(tuple(ix.code[i][v] for i, v in enumerate(cd)) in adm for cd in codes)
        a["held_by"] = sorted(n for n, r in rows.items() if r in codes)
        admits[tname] = a
    crow, keys = cy.coordinate_report(ix)
    return dict(cells=cells, shared={c: sorted(n for n, r in rows.items() if r == c) for c in cells},
                audit=ia.audit_index(STAGE2_COORDS, cells), runs=runs, admits=admits,
                adds_nothing=[r["coordinate"] for r in crow if r["adds_nothing"]], keys=keys)


def stage2(cy, ia, s1):
    """one index over the candidate laws (+ P2a as control), then the same with the record's 139 (1) plane added"""
    laws = {n: tuple(int(b) for b in s1[n]["moves"]) + (MATTER[n],) for n in LAWS}
    laws["P2a (control)"] = tuple(int(b) for b in RECORD_ROWS["P2a (control)"][0]) + (RECORD_ROWS["P2a (control)"][1],)
    planes = {}
    for pk in PLANES:
        with_plane = dict(laws)
        mv, mat = RECORD_ROWS[pk]
        with_plane[pk] = tuple(int(b) for b in mv) + (mat,)
        planes[pk] = _index_readout(cy, ia, with_plane, "p2b_laws_and_plane")
    rule = [n for n, r in laws.items() if n in LAWS and r[0] == 0 and r[1] == 0 and r[5] == 1]
    best = max(sum(laws[n][:5]) for n in rule)
    chosen = sorted(n for n in rule if sum(laws[n][:5]) == best)
    return dict(rows=laws, laws=_index_readout(cy, ia, laws, "p2b_laws"), planes=planes, chosen=chosen, best=best)


# ------------------------------------------------------------------------------------------- position 2b's sectors
ELL_MAX = 13.964e-6                                # B6P-SCALE: the table-top floor, ell <= 13.964 um (MK (41), |beta_3| <= 1.3e-4)
M_P = 1.67262192369e-27


def gravity_sector(q4=Q4, sigma=SIGMA_WINDOW[0]):
    """the theorem's relations evaluated in ours and position 2b at one sigma (every ratio is independent of which)"""
    u = {}
    for name, Gx in (("ours", G), ("2b", q4 * G)):
        ell2 = 3 * C ** 4 / (4 * math.pi * Gx * (sigma - 2 * DSIG))
        kap4 = 48 * math.pi * Gx / (sigma * C ** 4)          # SMS (19) with the c's carried, so kap4 sigma^2/6 is 1/m^2
        L4 = 8 * math.pi * Gx * DSIG / C ** 4
        L5 = 2 * L4 - kap4 * sigma ** 2 / 6                    # b1_matter.py's form of SMS (18); equals -6/ell^2
        u[name] = dict(G=Gx, ell=ell2 ** 0.5, k=ell2 ** -0.5, L4=L4, L5=L5, L5_density=L5 / kap4 ** 0.5,
                       beta3_rel=2 * ell2 / 3 / 1e-6, short_abs=Gx * ell2,
                       sigma_floor=3 * C ** 4 / (4 * math.pi * Gx * ELL_MAX ** 2) + 2 * DSIG)
    r = {k: u["2b"][k] / u["ours"][k] for k in u["ours"]}
    return dict(u=u, ratio=r, offset_in_ell=2 * DSIG / sigma, offset_in_ell_top=2 * DSIG / SIGMA_WINDOW[1])


def planck_content(Gx, sigma=SIGMA_WINDOW[0]):
    """a universe's numbers in its own Planck units: what a kappa5 change does dimensionlessly"""
    sP, lP, EP = C ** 7 / (HBAR * Gx ** 2), (HBAR * Gx / C ** 3) ** 0.5, (HBAR * C ** 5 / Gx) ** 0.5
    co = corridor(Gx)
    ell = (3 * C ** 4 / (4 * math.pi * Gx * (sigma - 2 * DSIG))) ** 0.5
    return dict(sigma=sigma / sP, offset=DSIG / sP, ell=ell / lP, E1=co["E1"] / EP, m1=co["m1"] / lP,
                alpha_G=Gx * M_P ** 2 / (HBAR * C), sigma_over_offset=sigma / DSIG)


def corridor(Gx):
    """the theorem's corridor at N = 1 under gravitational constant Gx (clause G, H): E1, m1, A_bit; sigma_P; N_max"""
    E1 = math.sqrt(H * C ** 5 * LN2 / (8 * math.pi ** 2 * Gx))
    m1 = Gx * E1 / C ** 4
    A_bit = 2 * H * Gx * LN2 / (math.pi * C ** 3)
    sigma_P = C ** 7 / ((H if MUT.get("h_for_hbar") else HBAR) * Gx ** 2)
    N_max = sigma_P / (8 * LN2 * DSIG)             # the Schwarzschild-de Sitter cap (corridor reader: 1.59e122 for ours)
    ell_over_m_sq_N = 3 / LN2 * sigma_P            # (ell/m)^2 = (3/ln2)(sigma_P/sigma)/N: times 1/(sigma N)
    L4 = 8 * math.pi * Gx * DSIG / C ** 4
    dS_bits = 4 * math.pi * (3 / L4) / A_bit        # the de Sitter horizon's area in bits; Nariai's is a third of it
    return dict(E1=E1, m1=m1, A_bit=A_bit, sigma_P=sigma_P, N_max=N_max, lm2=ell_over_m_sq_N, dS_bits=dS_bits)


def trip(G_origin, G_dest):
    """a corridor from a universe of G_origin to one of G_dest under 203's one E (g2_between G3): m2/m = G2/G, capacity
    N2/N = G2/G; and within one universe the assembly ceiling's README size N* = (ceiling/E1)^2"""
    return dict(m_ratio=G_dest / G_origin, capacity_ratio=G_dest / G_origin)


def universe_cells():
    """item 201's two coordinates (sigma, offset) for ours, position 2a and position 2b: how many cells do they make, in
    SI and in each universe's own Planck units?"""
    si = {"ours": (SIGMA_WINDOW[0], DSIG), "2a": (SIGMA_WINDOW[0], DSIG), "2b": (SIGMA_WINDOW[0], DSIG)}
    if MUT.get("sigma_moves"):              # a position 2b that changed sigma (a value, not a law) would be its own cell
        si["2b"] = (2 * SIGMA_WINDOW[0], DSIG)
    pl = {}
    for u, Gx in (("ours", G), ("2a", G), ("2b", Q4 * G)):
        p = planck_content(Gx)
        pl[u] = ("%.12g" % p["sigma"], "%.12g" % p["offset"])
    return dict(si=len(set(si.values())), planck=len(set(pl.values())),
                planck_cells={c: sorted(u for u, v in pl.items() if v == c) for c in set(pl.values())})


def matter_shift(Gx):
    """gravity's share of the hydrogen atom's binding: G m_e m_p / (e^2/(4 pi eps0)), unchanged laws otherwise"""
    me, mp, e, eps0 = 9.1093837015e-31, 1.67262192369e-27, 1.602176634e-19, 8.8541878128e-12
    return Gx * me * mp / (e ** 2 / (4 * math.pi * eps0))


# ------------------------------------------------------------------------------------------- bodies
def _bm3(x, B0, Bp):
    y = x ** (-2.0 / 3.0)
    return 1.5 * B0 * (y ** 3.5 - y ** 2.5) * (1.0 + 0.75 * (Bp - 4.0) * (y - 1.0))


def _x_of_P(P, B0, Bp, x0=1.0):
    if P <= 0:
        return 1.0
    x = x0
    for _ in range(60):
        f = _bm3(x, B0, Bp) - P
        d = (_bm3(x + 1e-7, B0, Bp) - _bm3(x - 1e-7, B0, Bp)) / 2e-7
        x2 = min(1.0, max(0.15, x - f / d))
        if abs(x2 - x) < 1e-14:
            return x2
        x = x2
    return x


def _sphere(Pc, rho0, B0, Bp, Gx, n=600):
    if MUT.get("no_compression"):                   # uniform density: G cancels in every ratio but g
        R = (3 * Pc / (2 * math.pi * Gx * rho0 ** 2)) ** 0.5
        return R, 4 / 3 * math.pi * R ** 3 * rho0
    xc = _x_of_P(Pc, B0, Bp)
    rc = rho0 / xc
    dr = (3 * Pc / (2 * math.pi * Gx * rc ** 2)) ** 0.5 / n
    st = {"x": xc}

    def f(r, P, m):
        st["x"] = _x_of_P(P, B0, Bp, st["x"])
        rho = rho0 / st["x"]
        return -Gx * m * rho / r ** 2, 4 * math.pi * r ** 2 * rho
    r, P, m = dr, Pc, 4.0 / 3.0 * math.pi * dr ** 3 * rc
    while True:
        k1 = f(r, P, m)
        k2 = f(r + dr / 2, P + dr / 2 * k1[0], m + dr / 2 * k1[1])
        k3 = f(r + dr / 2, P + dr / 2 * k2[0], m + dr / 2 * k2[1])
        k4 = f(r + dr, P + dr * k3[0], m + dr * k3[1])
        dP = dr / 6 * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0])
        dm = dr / 6 * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1])
        if P + dP <= 0:
            t = P / -dP
            return r + t * dr, m + t * dm
        r, P, m = r + dr, P + dP, m + dm


def body(M, rho0, B0, Bp, Gx):
    """a cold self-gravitating sphere of one metal, mass M, in hydrostatic equilibrium on its BM3 equation of state"""
    lo, hi = math.log(1e5), math.log(5e13)
    for _ in range(45):
        mid = 0.5 * (lo + hi)
        R, m = _sphere(math.exp(mid), rho0, B0, Bp, Gx)
        lo, hi = (lo, mid) if m > M else (mid, hi)
    Pc = math.exp(0.5 * (lo + hi))
    R, m = _sphere(Pc, rho0, B0, Bp, Gx)
    return dict(Pc=Pc, R=R, M=m, rho_mean=m / (4 / 3 * math.pi * R ** 3), g=Gx * m / R ** 2)


def bodies(pm):
    """copper, silver and gold spheres of 1e22 kg in ours, position 2a (min, mirror) and position 2b"""
    o = pm.compute()
    d = pm.load()
    out, support = {}, {}
    for el in ("Cu", "Ag", "Au"):
        for law in ("ours", "min", "mirror"):
            s = o["sol"][(el, law)]
            rows = [r for r in d["solids"] if r["el"] == el and r["law"] == law][0]["rows"]
            xmin = min(r["V_bohr3"] for r in rows) / s["V0"]
            support[(el, law)] = _bm3(xmin, s["B0"] * 1e9, s["Bp"])        # the highest pressure a scanned row reaches
            universes = [(law if law != "ours" else "ours", G)] + ([("2b", Q4 * G)] if law == "ours" else [])
            for name, Gx in universes:
                out[(el, name if name != "ours" else "ours")] = dict(body(1e22, s["rho"], s["B0"] * 1e9, s["Bp"], Gx),
                                                                     law=law, Gx=Gx)
    return out, support


def stars(q4=Q4):
    """READ scalings, DEDUCED numbers: L ~ G^4 M^3 (radiative), lifetime ~ M/L, M_Ch ~ G^-3/2"""
    lum = 3 if MUT.get("luminosity_G3") else 4
    L = q4 ** lum
    return dict(L_ratio=L, life_ratio=1 / L, Mch_ratio=q4 ** -1.5, year_ratio=q4 ** -0.5, insolation_ratio=L,
                Teq_ratio=L ** 0.25, hab_dist_ratio=L ** 0.5, sun_life_Gyr=10.0 / L)


def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "p2g_cy")
    sc = _load(os.path.join(HERE, "sigma_cypher.py"), "p2g_sc")
    ia = _load(os.path.join(HERE, "index_audit.py"), "p2g_ia")
    pm = _load(os.path.join(HERE, "p2_matter.py"), "p2g_pm")
    s1 = stage1(cy, sc, ia)
    s2 = stage2(cy, ia, s1)
    gs = gravity_sector()
    cor = {"ours": corridor(G), "2b": corridor(Q4 * G)}
    bd, support = bodies(pm)
    nstar = {u: (ASSEMBLY_MAX_J / c["E1"]) ** 2 for u, c in cor.items()}
    return dict(s1=s1, s2=s2, gs=gs, cor=cor, bodies=bd, support=support, stars=stars(), nstar=nstar,
                trip=trip(G, Q4 * G), cells201=universe_cells(),
                planck={"ours": planck_content(G), "2b": planck_content(Q4 * G)},
                matter={"ours": matter_shift(G), "2b": matter_shift(Q4 * G)})


def report(o):
    print("p2_gravity.py -- position 2b: the bulk's gravitational coupling kappa5^4 = 2 x ours (item 223)\n")
    print("stage 1 (the cypher): which of (sigma, offset, G, ell, m) each candidate law moves, measured on its own grid")
    for n, r in o["s1"].items():
        print("  %-13s moves %s  per language %s  keys %s" % (n, r["moves"], r["per_lang"], r["keys"]))
    s2 = o["s2"]
    print("\nstage 2: one index over the candidates (%s); the rule keeps sigma and the offset (201's values)" % ", ".join(STAGE2_COORDS))
    for n, r in s2["rows"].items():
        print("  %-36s %s" % (n, "".join(map(str, r))))
    for pk in PLANES:
        print("  %-36s %s" % (pk, "".join(RECORD_ROWS[pk][0]) + str(RECORD_ROWS[pk][1])))
    for lab, rd in [("laws (+ P2a)", s2["laws"])] + [("laws + " + pk, s2["planes"][pk]) for pk in PLANES]:
        print("  [%s] cells %d, shared %s, audit %s, adds nothing %s, keys %s" % (
            lab, len(rd["cells"]), {"".join(map(str, c)): v for c, v in rd["shared"].items() if len(v) > 1}, rd["audit"],
            rd["adds_nothing"], rd["keys"]))
        for rn, res in rd["runs"].items():
            print("    roster %s: %s" % (rn, "; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"]) for v in res["verdicts"])))
        for t, a in rd["admits"].items():
            print("    target '%s': %s" % (t, a))
    print("  the rule (sigma, offset kept, matter ours, the most of the five): %s (moves %d of five)" % (s2["chosen"], s2["best"]))
    gs, r = o["gs"], o["gs"]["ratio"]
    print("\nposition 2b's gravitational sector (sigma, offset held): G x%g, ell x%.6f, k x%.6f, Lambda4 x%g, Lambda5 x%g"
          " (geometric) / x%.6f (SMS's energy density)" % (r["G"], r["ell"], r["k"], r["L4"], r["L5"], r["L5_density"]))
    print("  short-range term: relative 2 ell^2/(3 r^2) x%.3f, absolute 2 G M ell^2/(3 r^3) x%.12g; sigma's table-top floor"
          " %.4e (ours) / %.4e (2b, same relative bound)" % (r["beta3_rel"], r["short_abs"], gs["u"]["ours"]["sigma_floor"],
                                                             gs["u"]["2b"]["sigma_floor"]))
    print("  the offset enters ell as 2 delta sigma / sigma: %.3e at the window's floor, %.3e at its top" % (
        gs["offset_in_ell"], gs["offset_in_ell_top"]))
    for u, c in o["cor"].items():
        print("  corridor %-4s E1 %.6e J  m1 %.6e m  A_bit %.6e m^2  sigma_P %.4e J/m^3  N_max %.4e" % (
            u, c["E1"], c["m1"], c["A_bit"], c["sigma_P"], c["N_max"]))
    print("  README size at the assembly ceiling, N* = (ceiling/E1)^2: %.1f bits (ours) / %.1f (2b)" % (o["nstar"]["ours"], o["nstar"]["2b"]))
    print("  a trip from ours to 2b under one E (203): m2/m %g, capacity %g N" % (o["trip"]["m_ratio"], o["trip"]["capacity_ratio"]))
    print("  N_max / de Sitter horizon bits: %.12f (ours) / %.12f (2b)" % tuple(c["N_max"] / c["dS_bits"] for c in o["cor"].values()))
    c2 = o["cells201"]
    print("  item 201's coordinates (sigma, offset) make %d cell(s) of ours, 2a and 2b in SI, %d in each one's Planck units %s"
          % (c2["si"], c2["planck"], sorted(c2["planck_cells"].values())))
    po, pb = o["planck"]["ours"], o["planck"]["2b"]
    print("  in Planck units (2b / ours): " + ", ".join("%s x%.6g" % (k, pb[k] / po[k]) for k in po))
    print("  matter: gravity's share of hydrogen's binding %.3e (ours) / %.3e (2b)" % (o["matter"]["ours"], o["matter"]["2b"]))
    print("\nbodies (1e22 kg, cold, hydrostatic on item 221's BM3 fits): R (km), mean density, g (m/s^2), Pc (GPa)")
    for (el, u), b in sorted(o["bodies"].items()):
        print("  %-2s %-6s R %8.2f  rho %8.1f  g %.4f  Pc %6.2f  (EOS rows reach %.1f GPa)" % (
            el, u, b["R"] / 1e3, b["rho_mean"], b["g"], b["Pc"] / 1e9, o["support"][(el, b["law"])] / 1e9))
    st = o["stars"]
    print("\nstars (READ scalings): L x%g, lifetime x%g (the Sun %.3f Gyr), M_Ch x%.4f; at 1 AU: year x%.4f, insolation x%g,"
          " T_eq x%.3f, habitable distance x%g" % (st["L_ratio"], st["life_ratio"], st["sun_life_Gyr"], st["Mch_ratio"],
                                                    st["year_ratio"], st["insolation_ratio"], st["Teq_ratio"], st["hab_dist_ratio"]))


MOVES_FIX = {"identity": "00000", "kappa5": "00111", "sigma-setter": "10111", "offset": "01010", "bit-area": "00001",
             "h": "00001", "c": "00011"}
E_FIX = {"order": 6, "algebra": 6, "geometry": 3, "information": 4, "statistics": 3}
# (element, universe): R km, mean density kg/m^3, g m/s^2, Pc GPa
BODY_FIX = {("Cu", "ours"): (649.30, 8721.3, 1.5831, 4.54), ("Cu", "min"): (636.06, 9277.1, 1.6497, 4.92),
            ("Cu", "mirror"): (623.72, 9838.9, 1.7157, 5.31), ("Cu", "2b"): (646.70, 8826.8, 3.1918, 9.33),
            ("Ag", "ours"): (617.11, 10158.3, 1.7526, 5.61), ("Ag", "min"): (577.28, 12409.3, 2.0028, 7.27),
            ("Ag", "mirror"): (552.90, 14124.8, 2.1833, 8.60), ("Ag", "2b"): (613.15, 10356.5, 3.5506, 11.70),
            ("Au", "ours"): (509.82, 18016.0, 2.5679, 12.12), ("Au", "min"): (507.68, 18244.4, 2.5895, 12.35),
            ("Au", "mirror"): (504.40, 18603.2, 2.6234, 12.64), ("Au", "2b"): (505.48, 18484.5, 5.2244, 25.63)}


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    mk = open(os.path.join(HERE, "b6p_scale.py"), encoding="utf-8").read()
    g2 = open(os.path.join(HERE, "g2_between.py"), encoding="utf-8").read()
    add("Y0 M's item-223 words verbatim in the rulings file; MK (41) and the record's three values for position 2's G "
        "(+2, +6, -1/4) as the record states them; the star scalings carry their sources",
        M223 in rul and "V(r) ~ GM/r (1 + 2 ell^2/(3 r^2))" in mk and "G2 = -G/4" in g2 and "G2/G1 = +2" in g2
        and "gave +6" in g2 and CHANDRA_READ[1].startswith("https://") and ML_READ[1].startswith("https://"))
    s1, s2 = o["s1"], o["s2"]
    ok1 = all(s1[n]["moves"] == m and set(s1[n]["per_lang"].values()) == {m} and s1[n]["keys"] == []
              for n, m in MOVES_FIX.items())
    ok1 &= 7.0e-63 < o["gs"]["offset_in_ell"] < 7.1e-63
    L = s2["laws"]
    ok1 &= len(L["cells"]) == 8 and all(len(v) == 1 for v in L["shared"].values()) and L["audit"]["keys"] == []
    ok1 &= L["audit"]["onehot"] == [] and L["adds_nothing"] == ["moves_offset", "moves_G"]
    v1173 = {v["language"]: v for v in L["runs"]["1173"]["verdicts"]}
    ok1 &= all(v1173[k]["E"] == e and v1173[k]["state"] == "SPEAKS" for k, e in E_FIX.items())
    ok1 &= v1173["analysis"]["state"] == "NOT-RUN" and v1173["documentary"]["state"] == "SILENT"
    langs = list(E_FIX)
    t_rule, t_all, t_off = list(TARGETS)
    ok1 &= L["admits"][t_rule]["held_by"] == ["kappa5"] and all(L["admits"][t_rule][k] for k in langs)
    for t in (t_all, t_off):
        a = L["admits"][t]
        ok1 &= a["held_by"] == [] and not a["geometry"] and not a["statistics"]
        ok1 &= a["order"] and a["algebra"] and a["information"]
    pm, ph = PLANES
    P = s2["planes"][pm]
    ok1 &= len(P["cells"]) == 9 and all(P["admits"][t]["held_by"] == [pm] and all(P["admits"][t][k] for k in langs)
                                        for t in (t_all, t_off))
    Q = s2["planes"][ph]
    ok1 &= len(Q["cells"]) == 8 and Q["shared"][(1, 0, 1, 1, 1, 1)] == sorted([ph, "sigma-setter"])
    ok1 &= all(Q["admits"][t]["held_by"] == [] and not Q["admits"][t]["geometry"] and not Q["admits"][t]["statistics"]
               for t in (t_all, t_off))
    ok1 &= s2["chosen"] == ["kappa5"] and s2["best"] == 3
    add("Y1 the choice through the cypher: stage 1's move binaries as fixed, every language agreeing, no keys; the offset "
        "reaches ell at 7.08e-63; stage 2's laws index 8 cells, unshared, audit clean, moves_offset and moves_G adding "
        "nothing, E as fixed with analysis NOT-RUN and documentary SILENT; the rule's target held by kappa5 and admitted "
        "by all five; 'all five' and 'offset with G' held by none, refused by geometry and statistics, admitted by the "
        "other three; with the record's plane coded offset-moved both are held by it and admitted by all, coded "
        "offset-held it shares the sigma-setter's cell and neither is held; the rule picks kappa5, 3 of five", ok1)
    gs, r = o["gs"], o["gs"]["ratio"]
    ok2 = r["G"] == 2 and abs(r["ell"] - 2 ** -0.5) < 1e-12 and abs(r["k"] - 2 ** 0.5) < 1e-12
    ok2 &= abs(r["L4"] - 2) < 1e-12 and abs(r["L5"] - 2) < 1e-12 and abs(r["L5_density"] - 2 ** 0.5) < 1e-12
    ok2 &= abs(r["beta3_rel"] - 0.5) < 1e-12 and abs(r["short_abs"] - 1) < 1e-12
    ok2 &= all(abs(u["L5"] * u["ell"] ** 2 + 6) < 1e-9 for u in gs["u"].values())
    ok2 &= abs(gs["u"]["ours"]["sigma_floor"] / 1.4817e53 - 1) < 1e-4 and abs(gs["u"]["2b"]["sigma_floor"] / 7.4086e52 - 1) < 1e-4
    ok2 &= abs(gs["u"]["ours"]["beta3_rel"] / 1.3e-4 - 1) < 0.01
    ok2 &= o["cells201"]["si"] == 1
    add("Y2 position 2b's sector: G x2, ell x1/sqrt2, k xsqrt2, Lambda4 x2, Lambda5 x2 (geometric, = -6/ell^2) and xsqrt2 "
        "(energy density), the relative short-range term x1/2 and the absolute one x1; sigma's table-top floor 1.4817e53 "
        "(ours, where beta_3 = 1.3e-4) and 7.4086e52 (2b); item 201's coordinates make one SI cell of the three", ok2)
    co, cb = o["cor"]["ours"], o["cor"]["2b"]
    fx = lambda v, w, t=1e-6: abs(v / w - 1) < t
    ok3 = fx(co["E1"], 4.594040e8) and fx(cb["E1"], 3.248477e8) and fx(co["m1"], 3.795926e-36) and fx(cb["m1"], 5.368249e-36)
    ok3 &= fx(co["A_bit"], 7.242779e-70) and fx(cb["A_bit"], 1.448556e-69)
    ok3 &= fx(co["sigma_P"], 4.6329e113, 1e-4) and fx(cb["sigma_P"], 1.1582e113, 1e-4)
    ok3 &= fx(co["N_max"], 1.5918e122, 1e-4) and fx(cb["N_max"], 3.9795e121, 1e-4)
    ok3 &= all(abs(c["N_max"] / c["dS_bits"] - 1 / 3) < 1e-12 for c in (co, cb)) and fx(cb["lm2"] / co["lm2"], 0.25, 1e-12)
    ok3 &= abs(o["nstar"]["ours"] - 676.3) < 0.05 and abs(o["nstar"]["2b"] - 1352.6) < 0.05
    ok3 &= o["trip"]["m_ratio"] == 2 and o["trip"]["capacity_ratio"] == 2
    add("Y3 the corridor: E1, m1, A_bit, sigma_P, N_max as fixed in both universes (x1/sqrt2, xsqrt2, x2, x1/4, x1/4); "
        "N_max a third of the de Sitter horizon's bits in both; (ell/m)^2 x1/4; the ceiling's README 676.3 -> 1352.6 bits; "
        "a trip under one E m2/m = 2, capacity 2N", ok3)
    add("Y4 matter ours: gravity's share of hydrogen's binding 4.408e-40 -> 8.816e-40, exactly x2",
        fx(o["matter"]["ours"], 4.408e-40, 1e-3) and fx(o["matter"]["2b"], 8.816e-40, 1e-3)
        and abs(o["matter"]["2b"] / o["matter"]["ours"] - 2) < 1e-12)
    bd, sup = o["bodies"], o["support"]
    ok5 = all(abs(bd[k]["R"] / 1e3 - R) < 0.01 and abs(bd[k]["rho_mean"] - rho) < 0.1 and abs(bd[k]["g"] - g) < 1e-4
              and abs(bd[k]["Pc"] / 1e9 - Pc) < 0.01 for k, (R, rho, g, Pc) in BODY_FIX.items())
    ok5 &= all(b["Pc"] < sup[(el, b["law"])] for (el, u), b in bd.items())
    ok5 &= all(2.0 < bd[(el, "2b")]["g"] / bd[(el, "ours")]["g"] < 2.05 and bd[(el, "2b")]["R"] < bd[(el, "ours")]["R"]
               for el in ("Cu", "Ag", "Au"))
    add("Y5 bodies of 1e22 kg: R, mean density, g and central pressure of all twelve as fixed; every central pressure inside "
        "its rows' reach; in 2b g rises by 2.0-2.05x and every body shrinks", ok5)
    st = o["stars"]
    add("Y6 stars from the READ scalings: L x16, lifetime x1/16 (0.625 Gyr), M_Ch x2^-1.5, year x2^-1/2, insolation x16, "
        "T_eq x2, equal insolation at 4 AU",
        st["L_ratio"] == 16 and st["life_ratio"] == 1 / 16 and abs(st["sun_life_Gyr"] - 0.625) < 1e-12
        and abs(st["Mch_ratio"] - 2 ** -1.5) < 1e-12 and abs(st["year_ratio"] - 2 ** -0.5) < 1e-12
        and st["insolation_ratio"] == 16 and abs(st["Teq_ratio"] - 2) < 1e-12 and abs(st["hab_dist_ratio"] - 4) < 1e-12)
    po, pb = o["planck"]["ours"], o["planck"]["2b"]
    rr = {k: pb[k] / po[k] for k in po}
    ok8 = all(abs(rr[k] - v) < 1e-9 for k, v in (("sigma", 4), ("offset", 4), ("ell", 0.5), ("E1", 1), ("m1", 1),
                                                     ("alpha_G", 2), ("sigma_over_offset", 1)))
    ok8 &= abs(po["E1"] - (LN2 / (4 * math.pi)) ** 0.5) < 1e-12 and abs(po["m1"] - po["E1"]) < 1e-12
    ok8 &= o["cells201"]["planck"] == 2 and sorted(o["cells201"]["planck_cells"].values()) == [["2a", "ours"], ["2b"]]
    add("Y8 in each universe's own Planck units 2b has sigma and the offset x4, ell x1/2, alpha_G x2, and the corridor's "
        "E1/E_P = m1/l_P = sqrt(ln2/4pi) and sigma/offset unchanged; 201's coordinates make two Planck-unit cells (2b "
        "apart, 2a with ours) against one SI cell", ok8)
    return res


MUTANTS = {"float_compare": "the cypher grids rounded to 12 significant figures (the offset's 7e-63 in ell lost)",
           "lambda4_held": "the offset held at Lambda4 = 8 pi G delta sigma / c^4 instead of rho_Lambda (201)",
           "no_compression": "the bodies at uniform density (no equation of state)",
           "luminosity_G3": "stellar luminosity taken as G^3 M^3 instead of Eddington's G^4 M^3",
           "sigma_moves": "position 2b given a different sigma (a value change, not the law)",
           "h_for_hbar": "the Planck tension c^7/(h G^2) with h in place of hbar"}


def selftest():
    r = checks(compute())
    for n, ok in r:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r)
    print("selftest: %d/%d" % (k, len(r)))
    return k == len(r)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = [n.split()[0] for n, ok in checks(compute()) if not ok]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-15s %-80s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
