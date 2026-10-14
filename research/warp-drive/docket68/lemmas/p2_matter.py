#!/usr/bin/env python3
"""p2_matter.py -- item 221: matter in position 2.  M: "assume all the other laws are the as ours and start building
molecules and measuring mass, density, gravity, etc, and notice how those value differ because of the madel exception
change".  Every value below is computed twice with one instrument -- once under our law, once under position 2's law --
and the difference is the finding.  Worked in the conversation, the runs banked in data/p2_matter_rows.json; 2026-10-11.

  X0 (read) M's words (item 221, verbatim in the rulings file; the quotation above omits M's opening "Yes. That is the
     first step.").  NIST ASD 5.12's gaps for the twenty configuration exceptions (fifteen measured; Pa U Np Cm Lr not),
     McDonough 2003's bulk-Earth tables, IUPAC 2013 weights and Huber-Herzberg's Cu2/Ag2 constants, banked with sources.
  X1 (RECONSTRUCTED law; computed calibration) item 221 reading (b) states the smallest shell-energy term on the d (or
     f) shell that makes the aufbau configuration the free atom's ground state (its premise from item 220 is narrowed by
     item 222; the operational law rests on M's own words).  The board adds the counting (the Lowdin population of the
     atom's d orbitals), the gauge, and a second, mirror, target.  As computed here, on Cu, Ag, Au and Cr: each d
     electron carries an extra energy delta, E' = E + delta (N_d - N_obs); every other law is ours.  delta is set in each
     method so the free atom's aufbau configuration lies 0.05 eV (min, reading (b)'s) or the NIST gap (mirror, the
     board's: the order reversed by its own amount) below the observed one.  Recomputed from the banked descents --
     PBE0/def2-TZVP: Cu 1.9732 / 3.3125, Ag 4.0428 / 7.7422, Au 1.9244 / 3.0106 eV; PBE/GTH: Cu 1.3971 / 2.7366, Ag
     4.1904 / 7.9023, Au 1.4813 / 2.5722, Cr 2.0476 / 2.9609 -- the PBE/GTH Cu, Ag, Au min values first-order
     extrapolations past the point where the aufbau state collapsed, PBE0 Au's interpolated between mixed rows.  The rows
     were run at values within 1 meV of these: Cu molecules at 1.9737 / 3.3131 (atom gaps 0.0505 / 1.3896 eV; where
     1.9737/3.3131 came from is an earlier secant, not banked), solids at Cu 1.3972 / 2.7365, Ag 4.1902 / 7.9023, Au
     1.4812 / 2.5722, Cr 2.0476 / 2.9609.  On clean rows the gap moves with slope -1.000 +- 0.003 per eV -- the shift
     lowers the aufbau state rigidly against the observed one, which says the counts stay integral there.  Where the
     aufbau state mixes, a banked state already lies 0.05 eV below the observed one at a smaller delta (the law is linear
     in delta at fixed density, so this is exact per row): PBE/GTH Cu 1.2887, Ag 4.1232, Au 1.4709, PBE0 Au 1.8986 eV.
     Those min laws are upper bounds on the smallest, by 0.01-0.11 eV per d electron, and the free atom under them is
     taken at the lowest banked state.  Deduced from the law's form, for the four computed: delta_min is the
     exception's whole cost in the method (1.35-4.14 eV per d electron) plus 0.05 eV, acting on every d electron of the
     element in every compound -- the smallest law is not a small change for these four (for Nb and Pt, whose NIST gaps
     are 0.14 and 0.10 eV, it could be).  The mirror target is the lowest-J level of the aufbau configuration while both
     methods are scalar-relativistic (no spin-orbit), so the mirror deltas are biased low by part of the multiplet
     spread, most for Au; its size is not banked
  X2 (computed) molecules, UKS PBE0/def2-TZVP, a 7-point coarse and 7-point fine curve each, quartic fit; r_e (A),
     omega_e (cm^-1), D_e (eV), ours -> min -> mirror:
         CuH   1.4850 1861 2.532 -> 1.4373 2008 2.793 -> 1.4350 1852 1.877
         AgH   1.6175 1780 2.251 -> 1.4921 2151 3.043 -> 1.5774 1777 1.853 (a triplet; its singlet 0.07 eV above)
         AuH   1.5399 2249 2.942 -> 1.4917 2474 3.501 -> 1.4729 2577 2.952
         Cu2   2.2846  246 1.762 -> 2.2690  254 1.708 -> no bound minimum found
         Ag2   2.5765  182 1.528 -> 2.5255  202 1.860 -> no minimum resolved
         Au2   2.5242  175 1.987 -> 2.4748  187 2.187 -> 2.4334  197 0.737
         CuF   1.7648  593 3.853 -> 1.7218  640 3.975 -> 1.7207  638 3.298 (followed branch)
     Under min every bond shortens (-0.7 % Cu2 to -7.7 % AgH), stiffens (+3 to +21 % omega_e) and all but Cu2 bind more
     (+3 to +35 %; Cu2 -3 %).  Under mirror the resolved bonds shorten (-2.5 to -4.4 %) and binding falls in four of five
     -- CuH -26 %, AgH -18 %, CuF -14 %, Au2 -63 %; AuH +0.4 % -- against a free atom the law has lowered by the whole
     NIST gap.  Cu2 under mirror holds no bound minimum the runs found: its one minimum (2.29 A, triplet) lies 0.38 eV
     above two free atoms and every branch followed out to 5 A stays above them.  Ag2 under mirror has no minimum
     resolved out to 3.68 A: its followed singlet is still falling there, 0.086 eV below twice the banked free atom, so
     a shallow well beyond is not excluded (and see below on the atom).  Au2, whose free atoms are d9s2 under the same
     law, binds by 0.737 eV.  The d count at r_e (interpolated) falls in every resolved molecule.  Our law against
     Huber-Herzberg (read): Cu2 r_e 2.2846 vs 2.2197 A, omega_e 246.1 vs 264.55; Ag2 omega_e 182.1 vs 192.4
  X3 (computed) solids, PBE, GTH pseudopotential and GTH-DZVP basis, 4x4x4 k (irreducible wedge), Fermi smearing 0.01
     Ha, cutoff 160 Ha on a fixed FFT mesh per metal, third-order Birch-Murnaghan through the five points about each
     minimum; a0 (A), density (kg/m^3), B0 (GPa), E_coh (eV), ours -> min -> mirror:
         Cu (fcc)  3.6596  8612  137 3.233 -> 3.5833  9174  168 3.450 -> 3.5119  9745  212 2.709
         Ag (fcc)  4.1613  9943   94 2.300 -> 3.8833 12235  192 3.130 -> 3.7134 13992  347 1.636
         Au (fcc)  4.2124 17503  147 2.639 -> 4.1980 17684  139 3.396 -> 4.1666 18086  156 3.044
         Cr (bcc)  2.8312  7609  279 3.901 -> 2.8748  7268  247 3.930 -> 2.8892  7160  250 3.241
     Copper is 6.5 % / 13.2 % denser and 23 % / 55 % stiffer; silver 23 % / 41 % denser and twice / 3.7 times as stiff;
     gold 1.0 % / 3.3 % denser; chromium (nonmagnetic) expands, 4.5 % / 5.9 % less dense.  Why (deduced, and checked):
     to first order the law adds delta N_d(a) to E(a), so a0 moves by -delta N_d'(a0)/E''(a0); read off our law's own
     scans this has the computed sign in all eight cases and its size within a factor 2.6 -- the d count falls on
     compression in Cu, Ag and Au and rises in Cr.  The projector, tested in three Cu cases (Mulliken's d count, equal to
     Lowdin's on a free atom, the same delta): every sign held -- CuH shortens 3.4 % (min) / 5.8 % (mirror) against
     3.2 / 3.4, binds 13.7 % more / 17.4 % less against 10.3 / 25.9, Cu metal contracts 3.0 % (min) against 2.1 % --
     and the sizes moved by 33-72 %.  Ag, Au, Cr, the bands and the chemistry were not tested against the projector
  X4 (computed from read data; magnitude and sign are gauge choices) the gauge constant -delta N_obs is free, so an
     atom's rest-mass shift is not fixed by the law: keeping the observed configuration's energy (G0, the board's) gives
     -target/(m c^2) (Cu -8.4e-13 min, -2.35e-11 mirror), keeping the aufbau one's (G1) +dE/(m c^2); between these two
     the largest is 3.73e-11 (Ag, mirror), of the fifteen exceptions with a measured gap; the law read without a constant
     gives up to 7.3e-10 (Ag, mirror).  The binding a body adds or loses (X2, X3) is gauge-free
  X5 (computed from read data) the Earth's free-atom mass part: dg/g = -4.906e-15 (min, G0), -9.475e-14 (mirror, G0),
     +9.475e-14 (G1), 98 % of it Cr; U (0.015 ppm, no measured gap) is not counted.  Binding changes of the same order
     are left out (Cr-metal-like bonding would scale the Cr term by about 0.3 to 1.6).  Mean atomic mass 26.02 u, Cr atom
     fraction 0.00235 (McDonough's Table 3)
  X6 (computed; the Earth's structural part an ESTIMATE) bodies of the same atoms: pure Cu denser by 6.52 % / 13.15 %,
     surface gravity +4.30 % / +8.59 %; Ag +23.1 % / +40.7 % and +14.8 % / +25.6 %; Au +1.04 % / +3.33 %.  The Earth,
     if its Cr atoms swell as pure Cr does and nothing else moves: dV/V +1.1e-4 / +1.5e-4, dg/g -7.4e-5 / -9.8e-5,
     1.5e10 / 1.0e9 times the free-atom mass part.  In matter the exception change acts through structure, not mass
  X7 (deduced from the law's form; checked on the banked runs, structurally) the law touches only exception elements,
     and an atom it does not touch is the same atom in both universes: water, air and carbon chemistry are ours exactly,
     and silicate rock is ours but for its trace exception elements (Cr, Cu, the light rare earths, Th, U and the rest)
  X8 (computed; the reading inferred) one gas-phase reaction: 2 CuF -> Cu + CuF2 costs +0.294 eV under our law (PBE0)
     and pays -0.175 eV under min and -1.046 eV under mirror; the second Cu-F bond strengthens 3.559 -> 4.150 -> 4.345
     eV while the first weakens under mirror (3.853 -> 3.298).  The banked d counts put most of the reaction's d-count
     fall on its free Cu atom, which the law makes d9s2 (85 % mirror, 71 % min), not on Cu(II): CuF2's count is only
     0.40 / 0.27 / 0.07 below CuF's.  That copper's +2 state would win in condensed matter is inferred, not computed
  X9 (computed; the colour inferred) the d band on an 8x8x8 k mesh at each law's a0: the upper edge of the occupied d
     band against E_F, taken (the board's rule) as the energy below which 95 % of the occupied d weight lies -- ours ->
     min -> mirror: Cu -1.240 -> -1.379 -> -1.307 eV; Au -1.524 -> (not run) -> -1.356; Ag -2.609 -> (not run) ->
     -1.379.  Under the mirror law silver's edge rises 1.23 eV (0.63-1.25 eV for 90-98 % rules; above 98 % the s-d tail
     at E_F takes over and every edge is meaningless), to where copper's and gold's sit under ours in the same method
     for every rule in that range (between gold's and copper's): silver's absorption onset moves into the band that colours copper and gold, so
     position 2's silver, under the mirror law, would not be white (inferred; PBE places every onset too low, the
     comparison is within the method, and min was not run for Ag or Au).  Copper's onset moves 0.05-0.15 eV to the blue
     and gold's 0.08-0.18 eV to the red (mirror) over the same rules -- small.  band.py's own d_top field (states above E_F with d weight > 0.5)
     is not a band edge and is not used

What this does not show.  The law is the board's reconstruction (X1), not M's or nature's: its form (a d-shell energy
counted by a projector), its gauge and its mirror target are choices, and a projector is not an observable -- the sizes
above carry it (X3).  Two density functionals carry their own errors (PBE0 for molecules, PBE for solids); our-law
values sit near measurement where read (X2), and the laws' differences, not the absolute values, are the finding.  Only
Cu, Ag and Au, and Cr as a solid, were computed of the twenty elements; Cr is modelled nonmagnetic (real Cr is an
antiferromagnet).  A molecule's curve is the lowest state over the guesses tried; CuF, Cu2 and Ag2 under the mirror law
needed branch-following, and a lower branch elsewhere is not excluded.  Every free Cu, Ag and Au atom was searched as a
doublet only; under the mirror law (delta = 7.7 eV per d electron for Ag) a higher-spin state with N_d below 9 was not
searched, and one would lower every Ag mirror D_e and E_coh.  Ag2's long-range 0.086 eV says either that, or that the
Lowdin count shifts with overlap alone by enough to move energies about 0.1 eV at 3.7 A.  The solids use a 4x4x4 k mesh
with 0.27 eV smearing (the d band was read on 8x8x8); the Earth's structural part assumes its Cr atoms swell as pure Cr
does and is an estimate, not a computation of the Earth's phases.  No mass, density or gravity of any body here enters
the corridor (deduced from M's "all the other laws are the as ours"): none of sigma, the offset, G, l or m moves.

Reads data/p2_matter_rows.json, data/p2_atoms_nist.json and the rulings file (read-only).  The runs that made the rows
(PySCF 2.14, a scratch environment, minutes to hours each) are not re-run here; their scripts' sha256 are banked.
Stdlib.  python3 p2_matter.py [--selftest | --mutants]
"""
import copy
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, "data", "p2_matter_rows.json")
NIST = os.path.join(HERE, "data", "p2_atoms_nist.json")
RULINGS = os.path.join(os.path.dirname(HERE), "M-RULINGS-2026-10-03.md")
MUT = {}
M221 = ("Now assume all the other laws are the as ours and start building molecules and measuring mass, density, "
        "gravity, etc, and notice how those value differ because of the madel exception change")

HA = 27.211386245988          # eV per hartree (CODATA 2018)
BOHR = 0.529177210903         # angstrom per bohr
AMU_ME = 1822.888486209       # electron masses per dalton
HA_CM = 219474.6313632        # cm^-1 per hartree
EV_CM = 8065.543937           # cm^-1 per eV
U_EV = 931494102.42           # eV per dalton (c^2 u)
U_KG = 1.66053906660e-27      # kg per dalton
GPA = 29421.02648438959       # GPa per hartree/bohr^3
G0 = 9.80665                  # m s^-2, standard gravity
LAWS = ("ours", "min", "mirror")
METALS = ("Cu", "Ag", "Au")
ISO = {"H": 1.00782503207, "F": 18.99840316, "Cu": 62.9295989, "Ag": 106.905091, "Au": 196.966552}   # most abundant isotope (u)


# ---------------------------------------------------------------------------------------------- stdlib fits
def _solve(A, b):
    n = len(b)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = max(range(c, n), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for k in range(c, n + 1):
                M[r][k] -= f * M[c][k]
    x = [0.0] * n
    for r in range(n - 1, -1, -1):
        x[r] = (M[r][n] - sum(M[r][k] * x[k] for k in range(r + 1, n))) / M[r][r]
    return x


def polyfit(xs, ys, deg):
    """least squares, centred and scaled: returns (x0, s, c) with y ~ sum c_k ((x - x0)/s)^k"""
    x0 = sum(xs) / len(xs)
    s = max(abs(x - x0) for x in xs) or 1.0
    t = [(x - x0) / s for x in xs]
    A = [[sum(ti ** (i + j) for ti in t) for j in range(deg + 1)] for i in range(deg + 1)]
    b = [sum(yi * ti ** i for ti, yi in zip(t, ys)) for i in range(deg + 1)]
    return x0, s, _solve(A, b)


def peval(f, x, der=0):
    x0, s, c = f
    t = (x - x0) / s
    v = 0.0
    for k in range(der, len(c)):
        m = 1.0
        for j in range(der):
            m *= (k - j)
        v += c[k] * m * t ** (k - der)
    return v / s ** der


def diatomic(pts, mA, mB):
    """pts [(r in A, E in Ha)]: quartic through every point; r_e is the stationary point nearest the lowest point
    (Newton); omega_e from k = E''(r_e), Ha/A^2 converted to Ha/bohr^2.  Returns r_e, E_min, omega_e (cm^-1), worst
    residual (meV)."""
    rs = [p[0] for p in pts]
    es = [p[1] for p in pts]
    f = polyfit(rs, es, min(4, len(pts) - 1))
    r = rs[es.index(min(es))]
    for _ in range(60):
        r -= peval(f, r, 1) / peval(f, r, 2)
    k = peval(f, r, 2) * (1.0 if MUT.get("omega_no_bohr") else BOHR ** 2)
    mu = mA * mB / (mA + mB) * AMU_ME
    we = (k / mu) ** 0.5 * HA_CM
    resid = max(abs(e - peval(f, x)) for x, e in zip(rs, es)) * HA * 1000
    return r, peval(f, r), we, resid


def birch(vs, es):
    """third-order Birch-Murnaghan, which is a cubic in x = V^(-2/3): V0 (bohr^3), E0 (Ha), B0 (Ha/bohr^3), B0', worst
    residual (meV)"""
    xs = [v ** (-2.0 / 3.0) for v in vs]
    f = polyfit(xs, es, 3)
    x = xs[es.index(min(es))]
    for _ in range(60):
        x -= peval(f, x, 1) / peval(f, x, 2)
    V0 = x ** -1.5
    dxdv = -2.0 / 3.0 * V0 ** (-5.0 / 3.0)
    d2xdv2 = 10.0 / 9.0 * V0 ** (-8.0 / 3.0)
    B0 = V0 * peval(f, x, 2) * dxdv ** 2
    # B' = -1 - V E'''(V) / E''(V) at V0
    E2 = peval(f, x, 2) * dxdv ** 2 + peval(f, x, 1) * d2xdv2
    d3xdv3 = -80.0 / 27.0 * V0 ** (-11.0 / 3.0)
    E3 = peval(f, x, 3) * dxdv ** 3 + 3 * peval(f, x, 2) * dxdv * d2xdv2 + peval(f, x, 1) * d3xdv3
    Bp = -1.0 - V0 * E3 / E2
    resid = max(abs(e - peval(f, xx)) for xx, e in zip(xs, es)) * HA * 1000
    return V0, peval(f, x), B0, Bp, resid


# ---------------------------------------------------------------------------------------------- data
def load():
    d = json.load(open(DATA, encoding="utf-8"))
    n = json.load(open(NIST, encoding="utf-8"))
    d["nist"] = {r["el"]: r for r in n["rows"]}
    if MUT.get("gauge_dropped"):          # the solid's energies without the gauge constant -delta N_obs
        d = copy.deepcopy(d)
        for s in d["solids"]:
            for r in s["rows"]:
                r["E"] = r["E_raw"]
    return d


def target(d, el, law):
    if law == "ours":
        return None
    if law == "min":
        return d["nist"][el]["dE_eV"] if MUT.get("min_is_mirror") else 0.05
    return d["nist"][el]["dE_eV"]


def law_delta(d, method, el, law):
    return None if law == "ours" else d["calibration"][method][el]["laws"][law]


def envelope(d, method, el, delta):
    """the lowest energy (eV, against the observed state) that any banked descent row's density reaches at delta: the law
    is linear in delta at fixed density, E'(delta) = gap_row + (delta - delta_row)(N_row - N_obs), so this is exact for
    each row and a variational upper bound on the free atom's lowest state at that delta"""
    c = d["calibration"][method][el]
    nobs = c.get("N_obs0", 10.0)
    return min(g + (delta - dr) * (n - nobs) for dr, g, n, no, ok in c["table"])


def atom_ground(d, el, law, method="pbe0_def2", used=None, run=None):
    """free-atom ground energy (Ha) under a law, gauge E' = E + delta (N - N_obs): the lowest of the states the SCF found
    at the delta the run used, the calibrated aufbau state (which lies `target` below the observed one by construction
    of delta) and the descent envelope at that delta (which can lie lower where the aufbau state mixes)"""
    if method == "pbe0_def2":
        if el == "H":
            return min(s[0] for s in d["atoms_pbe0"]["H"]["0"])
        if el not in METALS:                # a light atom the law never touches: the run's own free-atom energy
            return run["E_atoms_run"][el]
        key = "%g" % (0.0 if law == "ours" else used)
        found = min(s[0] for s in d["atoms_pbe0"][el][key])
    else:
        found = d["calibration"][method][el]["E_obs0"]
    if law == "ours" or d.get("no_calibrated_atom"):
        return found
    if MUT.get("mixed_atom") and (el, law, method) == ("Au", "min", "pbe0_def2"):
        return found                        # the mutant: the SCF's mixed Au state, 0.013 eV below the observed one
    e0 = d["calibration"][method][el]["E_obs0"]
    cal = e0 - target(d, el, law) / HA
    env = e0 + envelope(d, method, el, used) / HA
    return min(found, cal, env)


# ---------------------------------------------------------------------------------------------- compute
def compute():
    d = load()
    out = {"cal": {}, "mol": {}, "sol": {}, "mass": {}, "earth": {}, "body": {}}
    # 1. calibration: delta per element per law per method, recomputed from the banked descent table -- where gap(delta)
    #    crosses -target between two rows, by linear interpolation; where the aufbau state collapsed before the crossing,
    #    first order from the last two rows with an unmixed shell count -- and the gap's slope in delta
    for method in ("pbe0_def2", "pbe_gth"):
        for el, c in d["calibration"][method].items():
            t = c["table"]
            nauf = {"Cr": 4.0}.get(el, 9.0)
            clean = [r for r in t if abs(r[2] - nauf) < 0.01]
            got = {}
            for name, tg in (("switch", 0.0), ("min", target(d, el, "min")), ("mirror", target(d, el, "mirror"))):
                hit = None
                for r1, r2 in zip(t, t[1:]):
                    if (r1[1] + tg) * (r2[1] + tg) <= 0:
                        hit = r1[0] + (r2[0] - r1[0]) * (-tg - r1[1]) / (r2[1] - r1[1])
                        break
                if hit is None and len(clean) >= 2 and not MUT.get("no_extrapolation"):
                    r1, r2 = clean[-2], clean[-1]
                    hit = r2[0] + (r2[0] - r1[0]) * (-tg - r2[1]) / (r2[1] - r1[1])
                got[name] = hit
            slope = (clean[-1][1] - clean[0][1]) / (clean[-1][0] - clean[0][0]) if len(clean) > 1 else None
            lo, hi = 0.0, got["min"]                            # the smallest delta at which any banked state lies
            for _ in range(60):                                 # 0.05 eV below the observed one (bisection on the envelope)
                mid = 0.5 * (lo + hi)
                lo, hi = (lo, mid) if envelope(d, method, el, mid) <= -target(d, el, "min") else (mid, hi)
            out["cal"][(method, el)] = dict(got, banked=c["laws"], slope=slope, E_obs0=c["E_obs0"], min_env=hi,
                                            how={k: c["laws"].get(k + "_how") for k in ("switch", "min", "mirror")})
    # 2. molecules
    for m in d["molecules"]:
        A, B = (m["mol"][:2], m["mol"][2:]) if m["mol"][1].islower() else (m["mol"][0], m["mol"][1:])
        pts = [(p[0], p[1]) for p in m["fine"]]
        re, emin, we, resid = diatomic(pts, ISO[A], ISO[B])
        Ea = sum(atom_ground(d, X, m["law"], used=m["delta_eV"].get(X), run=m) for X in (A, B))
        De = (Ea - emin) * HA
        fr = sorted(m["fine"], key=lambda p: p[0])
        nd_mid = next(([p1[3][0] + (p2[3][0] - p1[3][0]) * (re - p1[0]) / (p2[0] - p1[0])] for p1, p2 in zip(fr, fr[1:])
                       if p1[0] <= re <= p2[0]), fr[len(fr) // 2][3])      # Lowdin N_d of atom 0, linear to r_e
        tag = {"AgAg": "Ag2", "CuCu": "Cu2", "AuAu": "Au2"}.get(m["mol"], m["mol"]) + "_" + m["law"]
        br = {k[len(tag) + 2:]: v for k, v in d.get("branches", {}).items() if k.startswith(tag + "_s")}
        cand = [((Ea - r["E"]) * HA, r["r"], int(sp)) for sp, rows in br.items() for r in rows if r["E"] is not None]
        cand += [((Ea - p[1]) * HA, p[0], p[2]) for p in m["coarse"] + m["fine"]]
        fw = {k[len(tag) + 2:]: sorted((r["r"], r["E"]) for r in rows if r["E"] is not None and r.get("conv", True))
              for k, rows in d.get("follows", {}).items() if k.startswith(tag + "_s")}
        cand += [((Ea - e) * HA, r, int(sp)) for sp, rows in fw.items() for r, e in rows]
        best = max(cand)                    # the most bound point any run found (all spins, guesses, followed branches)
        follow = {}
        for sp, rows in fw.items():         # a followed branch with an interior minimum: quartic through the 5 points about it
            if len(rows) < 5:
                continue
            i = min(range(len(rows)), key=lambda j: rows[j][1])
            if 2 <= i <= len(rows) - 3:
                r5, e5, w5, res5 = diatomic(rows[i - 2:i + 3], ISO[A], ISO[B])
                follow[int(sp)] = dict(re=r5, we=w5, De=(Ea - e5) * HA, resid=res5, Emin=e5)
        out["mol"][(m["mol"], m["law"])] = dict(re=re, we=we, De=De, Emin=emin, D0=De - we / 2 / EV_CM, resid=resid,
                                                unresolved=resid > 1.0, branch_best=best, follow=follow,
                                                branch_min={sp: min((r["E"], r["r"]) for r in rows if r["E"] is not None) for sp, rows in br.items()
                                                            if any(r["E"] is not None for r in rows)},
                                                spin=min(m["fine"], key=lambda p: p[1])[2], Nd=nd_mid[0],
                                                De_run=m["De_eV"], dmass=-De / ((ISO[A] + ISO[B]) * U_EV))
    # 3. solids
    for s in d["solids"]:
        rows = sorted(s["rows"], key=lambda r: r["a"])
        if len(rows) < 4:
            continue
        lo = min(range(len(rows)), key=lambda i: rows[i]["E"])
        sel = rows[max(0, min(lo - 2, len(rows) - 5)):][:5]
        V0, E0, B0, Bp, resid = birch([r["V_bohr3"] for r in sel], [r["E"] for r in sel])
        per = 4.0 if s.get("struct", "fcc") == "fcc" else 2.0
        a0 = (per * V0) ** (1.0 / 3.0) * BOHR
        mX = d["weights"][s["el"]]
        rho = mX * U_KG / (V0 * (BOHR * 1e-10) ** 3)                 # kg m^-3
        Ecoh = (atom_ground(d, s["el"], s["law"], "pbe_gth", used=s["delta_eV"]) - E0) * HA
        # N_d and the d-band centre at a0, linear between the bracketing rows
        def at(key):
            for r1, r2 in zip(rows, rows[1:]):
                if r1["a"] <= a0 <= r2["a"]:
                    return r1[key] + (r2[key] - r1[key]) * (a0 - r1["a"]) / (r2["a"] - r1["a"])
            return None
        out["sol"][(s["el"], s["law"])] = dict(a0=a0, V0=V0, B0=B0 * GPA, Bp=Bp, rho=rho, Ecoh=Ecoh, resid=resid,
                                               Nd=at("Nd"), epsd=at("eps_d_minus_EF_eV"), n=len(rows), edge=lo in (0, len(rows) - 1),
                                               vsound=(B0 * GPA * 1e9 / rho) ** 0.5)
    # 3a. why the lattice moves: to first order the law adds delta * N_d(a) to E(a), so a0 shifts by -delta N_d'(a0) / E''(a0),
    #     with N_d(a) and E(a) both read off our law's own scan
    for s in d["solids"]:
        if s["law"] != "ours" or (s["el"], "ours") not in out["sol"]:
            continue
        rows = s["rows"]
        a = [r["a"] for r in rows]
        fN, fE = polyfit(a, [r["Nd"] for r in rows], 1), polyfit(a, [r["E"] for r in rows], 4)
        a0 = out["sol"][(s["el"], "ours")]["a0"]
        dN, E2 = peval(fN, a0, 1), peval(fE, a0, 2) * HA
        for law in ("min", "mirror"):
            if (s["el"], law) in out["sol"]:
                dl = d["calibration"]["pbe_gth"][s["el"]]["laws"][law]
                out.setdefault("first_order", {})[(s["el"], law)] = dict(dNd_da=dN, E2=E2, pred=-dl * dN / E2,
                                                                         actual=out["sol"][(s["el"], law)]["a0"] - a0)
    # 3b. the d band at each law's a0 on a dense k mesh (band.py): occupied d-band centre and upper edge (the energy below
    #     which 95 % of the occupied d weight lies), both against E_F; the edge sets the interband absorption onset
    for b in d.get("bands", []):
        law = next(l for l in LAWS if (l == "ours") == (b["delta_eV"] == 0.0) and (l == "ours" or abs(b["delta_eV"] - d["calibration"]["pbe_gth"][b["el"]]["laws"][l]) < 2e-3))
        occ = sorted((e, w * wd) for w, e, wd in b["bands"] if e < 0)
        tot = sum(v for _, v in occ)
        edges = {}
        for p in (0.90, 0.95, 0.97, 0.98):                      # the edge rule is the board's: report its spread
            acc = 0.0
            for e, v in occ:
                acc += v
                if acc >= p * tot:
                    edges[p] = e
                    break
        out.setdefault("band", {})[(b["el"], law)] = dict(centre=sum(e * v for e, v in occ) / tot, edge=edges[0.95],
                                                         edges=edges, Nd_occ=2 * tot, a=b["a"], nk=b["nk"])
    # 3c. robustness of the law's projector: Mulliken's d count in place of Lowdin's (equal on a free atom, so the same delta)
    rb = d.get("robust", {})
    for mm in rb.get("molecules", []):
        A, B = mm["mol"][:2], mm["mol"][2:]
        r, e, w, res = diatomic([(p[0], p[1]) for p in mm["fine"]], ISO[A], ISO[B])
        out.setdefault("robust", {})[(mm["mol"], mm["law"])] = dict(re=r, we=w, De=(sum(mm["E_atoms"].values()) - e) * HA)
    for key, rows in rb.get("solids", {}).items():
        el, law = key.split("_")[:2]
        if len(rows) >= 5:
            lo = min(range(len(rows)), key=lambda i: rows[i]["E"])
            sel = rows[max(0, min(lo - 2, len(rows) - 5)):][:5]
            V0, E0, B0, Bp, res = birch([x["V_bohr3"] for x in sel], [x["E"] for x in sel])
            out.setdefault("robust", {})[(el, law, "solid")] = dict(a0=(4.0 * V0) ** (1.0 / 3.0) * BOHR, B0=B0 * GPA,
                                                                    edge=lo in (0, len(rows) - 1))
    # 4. masses: per atom, two gauges; G0 keeps the observed configuration's energy (the board's law), G1 the aufbau's
    for el, r in d["nist"].items():
        if r.get("dE_eV") is None or el not in d["weights"]:
            continue
        mc2 = d["weights"][el] * U_EV
        out["mass"][el] = dict(G0_min=-target(d, el, "min") / mc2, G0_mirror=-r["dE_eV"] / mc2, G1=r["dE_eV"] / mc2)
    # 5. the Earth (mass part) and a pure-metal body
    w = d["earth"]["bulk_ppm"]
    for g in ("G0_min", "G0_mirror", "G1"):
        out["earth"][g] = sum(w[el] * 1e-6 * out["mass"][el][g] for el in w if el in out["mass"])
    # the Earth, structural part (an ESTIMATE, not a computation of the Earth's phases): Cr's atoms take the volume change
    # pure bcc Cr shows under the law, at the mean atomic volume, everything else unchanged
    maj, W = d["earth"]["majors_ppm"], d["weights"]
    moles = {el: w / W[el] for el, w in maj.items()}
    xcr = moles["Cr"] / sum(moles.values())
    out["earth"]["mean_atomic_mass"] = sum(maj.values()) / sum(moles.values())
    out["earth"]["x_Cr"] = xcr
    oc = out["sol"].get(("Cr", "ours"))
    for law in ("min", "mirror"):
        pc = out["sol"].get(("Cr", law))
        if oc and pc:
            dv = xcr * ((pc["a0"] / oc["a0"]) ** 3 - 1.0)
            out["earth"]["struct_" + law] = dict(dV_over_V=dv, dg_over_g=(1.0 + dv) ** (-2.0 / 3.0) - 1.0)
    # chemistry: copper's +1 and +2 states (CuF, linear CuF2), gas phase, PBE0
    for law in LAWS:
        cuf = out["mol"].get(("CuF", law))
        x2 = next((x for x in d.get("mx2", []) if x["law"] == law), None)
        if cuf and x2:
            eF = x2["E_F_atom"]
            used = None if law == "ours" else x2["delta_eV"]
            eCu = atom_ground(d, "Cu", law, used=used)
            eCuF = cuf["Emin"] if not cuf["unresolved"] else min(f["Emin"] for f in cuf["follow"].values())
            out.setdefault("chem", {})[law] = dict(D_CuF=(eCu + eF - eCuF) * HA, D_FCuF=(eCuF + eF - x2["Emin"]) * HA,
                                                   dispro=(eCu + x2["Emin"] - 2 * eCuF) * HA, re_CuF2=x2["re"])
    for el in METALS:
        o = out["sol"].get((el, "ours"))
        for law in ("min", "mirror"):
            p = out["sol"].get((el, law))
            if not (o and p):
                continue
            dm = out["mass"][el]["G0_" + law]
            da = p["a0"] / o["a0"] - 1.0
            out["body"][(el, law)] = dict(da=da, drho=(1 + dm) / (1 + da) ** 3 - 1, dg_same_atoms=(1 + dm) / (1 + da) ** 2 - 1,
                                          dg_same_radius=(1 + dm) / (1 + da) ** 3 - 1)
    return out


# ---------------------------------------------------------------------------------------------- report
def report(o):
    print("p2_matter.py -- matter in position 2 (item 221): our law vs position 2's law, one instrument\n")
    print("law's shift delta (eV per d electron), set so the free atom's aufbau configuration lies 0.05 eV (min) or the NIST")
    print("gap (mirror) below the observed one:")
    for (method, el), c in sorted(o["cal"].items()):
        print("  %-9s %-2s  switch %-8s min %-8s mirror %-8s  slope %-8s  smallest by the envelope %.4f%s" % (
            method, el, *(None if c[k] is None else round(c[k], 4) for k in ("switch", "min", "mirror")),
            None if c["slope"] is None else round(c["slope"], 4), c["min_env"], "  (min EXTRAPOLATED)" if (c["how"]["min"] or "").startswith("EXTRA") else ""))
    print("\nmolecules (UKS PBE0/def2-TZVP): r_e (A), omega_e (cm^-1), D_e, D_0 (eV), Lowdin N_d at r_e")
    for (mol, law), m in sorted(o["mol"].items(), key=lambda kv: (kv[0][0], LAWS.index(kv[0][1]))):
        if m["unresolved"]:
            print("  %-5s %-6s NO RESOLVED MINIMUM on the lowest-state curve (quartic misfit %.1f meV); most bound point found %.3f eV at %.2f A (2S = %d)" % (
                mol, law, m["resid"], *m["branch_best"]))
            for sp, f in sorted(m["follow"].items()):
                print("  %-5s %-6s   followed branch 2S = %d: r_e %.4f  w_e %7.1f  D_e %.4f  fit %.3f meV" % (mol, law, sp, f["re"], f["we"], f["De"], f["resid"]))
            continue
        print("  %-5s %-6s r_e %.4f  w_e %7.1f  D_e %.4f  D_0 %.4f  spin %d  N_d %.4f  fit %.3f meV" % (
            mol, law, m["re"], m["we"], m["De"], m["D0"], m["spin"], m["Nd"], m["resid"]))
    print("\nsolids (PBE, GTH-DZVP, k-symmetry): a0 (A), rho (kg/m^3), B0 (GPa), E_coh (eV), Lowdin N_d at a0, bulk sound speed")
    print("  (the 4x4x4 scans' d-band centre is not printed: their Fermi level jumps by up to 1.4 eV between neighbouring a; see the")
    print("   8x8x8 d band below)")
    for (el, law), s in sorted(o["sol"].items(), key=lambda kv: (kv[0][0], LAWS.index(kv[0][1]))):
        print("  %-2s %-6s a0 %.4f  rho %8.1f  B0 %6.1f  B' %.2f  E_coh %.3f  N_d %s  v %.0f m/s%s" % (
            el, law, s["a0"], s["rho"], s["B0"], s["Bp"], s["Ecoh"], s["Nd"] and round(s["Nd"], 4),
            s["vsound"], "  (minimum at grid edge)" if s["edge"] else ""))
    if o.get("robust"):
        print("\nthe projector tested: Mulliken's d count in place of Lowdin's (same delta)")
        for k, v in sorted(o["robust"].items()):
            print("  %s: %s" % ("/".join(k), {x: round(y, 4) if isinstance(y, float) else y for x, y in v.items()}))
    print("\nwhy the lattice moves: first order, da = -delta N_d'(a0) / E''(a0), from our law's own scan")
    for (el, law), f in sorted(o.get("first_order", {}).items()):
        print("  %-2s %-6s N_d' %+.4f /A  E'' %.3f eV/A^2  predicted %+.4f A  computed %+.4f A" % (el, law, f["dNd_da"], f["E2"], f["pred"], f["actual"]))
    print("\nthe d band at a0 (PBE, 8x8x8 k mesh): occupied centre and upper edge (95 % of the occupied d weight) against E_F (eV)")
    for (el, law), b in sorted(o.get("band", {}).items(), key=lambda kv: (kv[0][0], LAWS.index(kv[0][1]))):
        print("  %-2s %-6s centre %+.3f  edge %+.3f  (90/97/98 %%: %+.3f / %+.3f / %+.3f; occupied d weight %.3f)" % (
            el, law, b["centre"], b["edge"], b["edges"][0.90], b["edges"][0.97], b["edges"][0.98], b["Nd_occ"]))
    print("\natomic mass shift dm/m: G0 (observed configuration's energy kept) / G1 (aufbau configuration's kept)")
    for el, m in o["mass"].items():
        print("  %-2s  G0 min %+.3e  G0 mirror %+.3e  G1 %+.3e" % (el, m["G0_min"], m["G0_mirror"], m["G1"]))
    print("\nthe Earth, mass part of dg/g (bulk composition): %s" % {k: "%+.3e" % o["earth"][k] for k in ("G0_min", "G0_mirror", "G1")})
    for k in ("struct_min", "struct_mirror"):
        if k in o["earth"]:
            print("  structural estimate %s (Cr as pure bcc Cr; x_Cr %.5f): dV/V %+.2e  dg/g %+.2e" % (k[7:], o["earth"]["x_Cr"], o["earth"][k]["dV_over_V"], o["earth"][k]["dg_over_g"]))
    for law, c in o.get("chem", {}).items():
        print("  chemistry %-6s D(Cu-F) %.3f  D(FCu-F) %.3f  2CuF -> Cu + CuF2 %+.3f eV  r(CuF2) %.4f" % (law, c["D_CuF"], c["D_FCuF"], c["dispro"], c["re_CuF2"]))
    for (el, law), b in sorted(o["body"].items()):
        print("  pure %s body, %s: da/a %+.4f  drho/rho %+.4f  dg/g same atoms %+.4f  same radius %+.4f" % (
            el, law, b["da"], b["drho"], b["dg_same_atoms"], b["dg_same_radius"]))

# ---------------------------------------------------------------------------------------------- checks
NIST_FIX = {"Cu": 1.388948, "Ag": 3.7495671196, "Au": 1.1358412, "Cr": 0.96097009}
MOL_FIX = {("CuH", "ours"): (1.4850, 1861.2, 2.5317), ("CuH", "min"): (1.4373, 2008.3, 2.7933),
           ("CuH", "mirror"): (1.4350, 1851.9, 1.8770), ("AgH", "ours"): (1.6175, 1780.3, 2.2510),
           ("AgH", "min"): (1.4921, 2151.1, 3.0432), ("AgH", "mirror"): (1.5774, 1776.6, 1.8525),
           ("AuH", "ours"): (1.5399, 2248.8, 2.9417), ("AuH", "min"): (1.4917, 2474.0, 3.5008),
           ("AuH", "mirror"): (1.4729, 2576.5, 2.9522), ("CuCu", "ours"): (2.2846, 246.1, 1.7615),
           ("CuCu", "min"): (2.2690, 253.9, 1.7076), ("AgAg", "ours"): (2.5765, 182.1, 1.5284),
           ("AgAg", "min"): (2.5255, 201.6, 1.8596), ("AuAu", "ours"): (2.5242, 175.0, 1.9869),
           ("AuAu", "min"): (2.4748, 186.9, 2.1873), ("AuAu", "mirror"): (2.4334, 196.6, 0.7366)}
SOL_FIX = {("Cu", "ours"): (3.6596, 8612.1, 136.6, 3.233), ("Cu", "min"): (3.5833, 9174.0, 168.0, 3.450),
           ("Cu", "mirror"): (3.5119, 9744.6, 211.8, 2.709), ("Ag", "ours"): (4.1613, 9942.9, 93.9, 2.300),
           ("Ag", "min"): (3.8833, 12235.2, 191.7, 3.130), ("Ag", "mirror"): (3.7134, 13991.7, 346.9, 1.636),
           ("Au", "ours"): (4.2124, 17502.8, 146.8, 2.639), ("Au", "min"): (4.1980, 17684.2, 139.3, 3.396),
           ("Au", "mirror"): (4.1666, 18086.1, 156.5, 3.044), ("Cr", "ours"): (2.8312, 7609.4, 278.6, 3.901),
           ("Cr", "min"): (2.8748, 7268.2, 246.7, 3.931), ("Cr", "mirror"): (2.8892, 7159.7, 249.8, 3.241)}
MASS_FIX = {"Cr": -1.984e-11, "Cu": -2.346e-11, "Ag": -3.732e-11, "Au": -6.191e-12, "Pd": -3.139e-11}


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    d = load()
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("X0 M's item-221 words verbatim in the rulings file; NIST gaps (Cu, Ag, Au, Cr), McDonough's bulk-Earth Cr and Cu "
        "and the IUPAC weights as banked",
        M221 in rul and all(abs(d["nist"][el]["dE_eV"] - v) < 1e-12 for el, v in NIST_FIX.items())
        and d["earth"]["bulk_ppm"]["Cr"] == 4700 and d["earth"]["bulk_ppm"]["Cu"] == 60 and d["weights"]["Cu"] == 63.546)
    cal = o["cal"]
    ok1 = all(c[k] is not None and abs(c[k] - c["banked"][k]) < 5e-4 for c in cal.values() for k in ("switch", "min", "mirror"))
    ok1 = ok1 and all(abs(c["slope"] + 1.0) < 0.003 for c in cal.values())
    ok1 = ok1 and all(0.045 < c["min"] - c["switch"] < 0.055 for c in cal.values())
    ok1 = ok1 and min(c["switch"] for c in cal.values()) > 1.3
    runs = [(X, mm["law"], v, "pbe0_def2") for mm in d["molecules"] for X, v in mm["delta_eV"].items()]
    runs += [(sd["el"], sd["law"], sd["delta_eV"], "pbe_gth") for sd in d["solids"] if sd["law"] != "ours"]
    ok1 = ok1 and all(abs(v - cal[(mt, X)][law]) < 1e-3 for X, law, v, mt in runs)
    env = {k: (c["min"] - c["min_env"]) for k, c in cal.items()}
    ok1 = ok1 and all(0.06 < env[("pbe_gth", el)] for el in ("Cu", "Ag")) and env[("pbe0_def2", "Au")] > 0.02
    ok1 = ok1 and all(abs(env[k]) < 1e-3 for k in (("pbe0_def2", "Cu"), ("pbe0_def2", "Ag"), ("pbe_gth", "Cr")))
    add("X1 the law's delta recomputed from every banked descent equals the banked value (5e-4 eV); the gap moves with "
        "slope -1.000 +- 0.003 per eV (the aufbau state shifts rigidly); min - switch = 0.05 eV "
        "(+-0.005 where the bracketing rows are mixed); every switch exceeds 1.3 eV "
        "(for the four computed); every run's delta (read from its row) is the calibration's within 1 meV; and where the "
        "aufbau state mixes (PBE/GTH Cu, Ag; PBE0 Au) a banked state reaches 0.05 eV below the observed one at a smaller "
        "delta -- those min laws are upper bounds on the smallest", ok1)
    m = o["mol"]
    ok2 = all(k in m and abs(m[k]["re"] - a) < 1e-4 and abs(m[k]["we"] - b) < 0.1 and abs(m[k]["De"] - c) < 1e-4
              for k, (a, b, c) in MOL_FIX.items())
    base = [n for n in ("CuH", "AgH", "AuH", "CuCu", "AgAg", "AuAu")]
    ok2 &= all(m[(n, "min")]["re"] < m[(n, "ours")]["re"] for n in base)
    ok2 &= all(m[(n, "min")]["De"] > m[(n, "ours")]["De"] for n in base if n != "CuCu") and m[("CuCu", "min")]["De"] < m[("CuCu", "ours")]["De"]
    ok2 &= all(m[(n, law)]["Nd"] < m[(n, "ours")]["Nd"] for n in base for law in ("min", "mirror") if not m[(n, law)]["unresolved"])
    agh = m[("AgH", "mirror")]
    ok2 &= agh["spin"] == 2 and (agh["Emin"] - agh["branch_min"]["0"][0]) * HA < -0.05
    ok2 &= m[("AgAg", "mirror")]["unresolved"] and m[("AgAg", "mirror")]["branch_best"][0] < 0.1
    ok2 &= m[("CuCu", "mirror")]["De"] < 0 and m[("CuCu", "mirror")]["branch_best"][0] < 0.01
    add("X2 molecules: r_e, omega_e, D_e of 16 resolved curves as fixed; under the min law every bond shortens and every "
        "one but Cu2 strengthens; every resolved N_d falls; AgH under the mirror law is a triplet, its singlet branch "
        "above by more than 0.05 eV; Cu2 under the mirror law holds no bound minimum the runs found and Ag2 none resolved (best "
        "binding below 0.1 eV and 0.01 eV; Cu2's 2.29 A triplet minimum sits above two free atoms; Ag2's is a minimum not "
        "resolved, not a proof of none)", ok2)
    so = o["sol"]
    ok3 = all(k in so and abs(so[k]["a0"] - a) < 2e-4 and abs(so[k]["rho"] - r) < 1.0 and abs(so[k]["B0"] - b) < 0.2
              and abs(so[k]["Ecoh"] - c) < 1e-3 for k, (a, r, b, c) in SOL_FIX.items())
    ok3 = ok3 and all(not s["edge"] and s["resid"] < 0.1 for s in so.values())
    ok3 = ok3 and all(so[(el, "ours")]["a0"] > so[(el, "min")]["a0"] > so[(el, "mirror")]["a0"] for el in METALS)
    ok3 = ok3 and so[("Cr", "ours")]["a0"] < so[("Cr", "min")]["a0"] < so[("Cr", "mirror")]["a0"]
    ok3 = ok3 and all(so[(el, law)]["Nd"] < so[(el, "ours")]["Nd"] for el in METALS + ("Cr",) for law in ("min", "mirror"))
    fo = o.get("first_order", {})
    ok3 = ok3 and len(fo) == 8 and all(f["pred"] * f["actual"] > 0 and 1 / 2.6 < f["pred"] / f["actual"] < 2.6 for f in fo.values())
    ok3 = ok3 and all(fo[(el, "min")]["dNd_da"] > 0 for el in METALS) and fo[("Cr", "min")]["dNd_da"] < 0
    add("X3 solids (fcc Cu, Ag, Au; nonmagnetic bcc Cr): a0, density, B0, E_coh of twelve Birch-Murnaghan fits as fixed, "
        "each minimum inside its grid, every fit within 0.1 meV; Cu, Ag and Au contract under both laws, mirror more than "
        "min, while Cr expands; the d count falls in every one; and the first-order response -delta N_d'(a0)/E''(a0), read off "
        "our law's own scan, has the computed shift's sign in all eight cases and its size within a factor 2.6: the d count "
        "falls on compression in Cu, Ag and Au and rises in Cr, and the law pays for d electrons", ok3)
    mass = o["mass"]
    ok4 = all(abs(mass[el]["G0_mirror"] / v - 1) < 2e-3 for el, v in MASS_FIX.items())
    ok4 &= max(abs(x) for r in mass.values() for x in r.values()) < 3.8e-11
    ok4 &= all(abs(r["G1"] + r["G0_mirror"]) < 1e-20 for r in mass.values())
    lit = (d["nist"]["Ag"]["dE_eV"] + o["cal"][("pbe0_def2", "Ag")]["mirror"] * d["nist"]["Ag"]["N_auf"]) / (d["weights"]["Ag"] * U_EV)
    ok4 &= 7.2e-10 < lit < 7.4e-10
    add("X4 the gauge constant is free, so an atom's mass shift is a gauge choice in size and sign: between G0 (observed "
        "configuration keeps its energy, -target/mc^2) and G1 (aufbau keeps its, +dE/mc^2) the largest is 3.73e-11 (Ag, "
        "mirror), of the fifteen with a measured gap; the law with no constant gives 7.3e-10 (Ag, mirror)", ok4)
    e = o["earth"]
    cr_share = d["earth"]["bulk_ppm"]["Cr"] * 1e-6 * mass["Cr"]["G0_mirror"] / e["G0_mirror"]
    add("X5 the Earth's free-atom mass part: dg/g = -4.906e-15 (min, G0), -9.475e-14 (mirror, G0), +9.475e-14 (G1); Cr carries "
        "%.1f%% of it; bulk-Earth mean atomic mass 26.02 u, Cr atom fraction 0.00235" % (100 * cr_share),
        abs(e["G0_min"] / -4.906e-15 - 1) < 1e-3 and abs(e["G0_mirror"] / -9.475e-14 - 1) < 1e-3 and cr_share > 0.97
        and abs(e["mean_atomic_mass"] - 26.02) < 0.01 and abs(e["x_Cr"] - 0.00235) < 1e-5)
    bd = o["body"]
    add("X6 bodies: a pure Cu body of the same atoms is denser by 6.52 % (min) / 13.15 % (mirror) and pulls 4.30 % / 8.59 % "
        "harder at its surface; Ag 23.06 % / 40.72 % and 14.83 % / 25.58 %; Au 1.04 % / 3.33 %; the Earth's structural "
        "estimate (Cr's atoms swelling as pure Cr does) dg/g = -7.35e-05 / -9.84e-05, 1.5e10 / 1.0e9 times the mass part",
        abs(bd[("Cu", "min")]["drho"] - 0.0652) < 1e-4 and abs(bd[("Cu", "mirror")]["drho"] - 0.1315) < 1e-4
        and abs(bd[("Cu", "min")]["dg_same_atoms"] - 0.0430) < 1e-4 and abs(bd[("Cu", "mirror")]["dg_same_atoms"] - 0.0859) < 1e-4
        and abs(bd[("Ag", "min")]["drho"] - 0.2306) < 1e-4 and abs(bd[("Ag", "mirror")]["drho"] - 0.4072) < 1e-4
        and abs(bd[("Ag", "min")]["dg_same_atoms"] - 0.1483) < 1e-4 and abs(bd[("Ag", "mirror")]["dg_same_atoms"] - 0.2558) < 1e-4
        and abs(bd[("Au", "min")]["drho"] - 0.0104) < 1e-4 and abs(bd[("Au", "mirror")]["drho"] - 0.0333) < 1e-4
        and abs(e["struct_min"]["dg_over_g"] / -7.35e-05 - 1) < 2e-3 and abs(e["struct_mirror"]["dg_over_g"] / -9.84e-05 - 1) < 2e-3
        and abs(e["struct_min"]["dg_over_g"] / e["G0_min"]) > 1e10 and abs(e["struct_mirror"]["dg_over_g"] / e["G0_mirror"]) > 1e9)
    ch = o.get("chem", {})
    ok8 = set(ch) == set(LAWS) and abs(ch["ours"]["dispro"] - 0.294) < 1e-3 and abs(ch["min"]["dispro"] + 0.175) < 1e-3
    ok8 = ok8 and abs(ch["mirror"]["dispro"] + 1.046) < 1e-3 and ch["ours"]["D_FCuF"] < ch["min"]["D_FCuF"] < ch["mirror"]["D_FCuF"]
    rb = o.get("robust", {})
    ok8 = ok8 and all(rb[(n, law)]["re"] < m[(n, "ours")]["re"] for n, law in (("CuH", "min"), ("CuH", "mirror")))
    ok8 = ok8 and rb[("CuH", "min")]["De"] > m[("CuH", "ours")]["De"] > rb[("CuH", "mirror")]["De"]
    ok8 = ok8 and so[("Cu", "ours")]["a0"] > rb[("Cu", "min", "solid")]["a0"] and not rb[("Cu", "min", "solid")]["edge"]
    add("X8 chemistry and the projector: 2 CuF -> Cu + CuF2 costs +0.294 eV under our law and pays -0.175 (min) / -1.046 eV "
        "(mirror) -- copper's +2 state wins; with Mulliken's d count in place of Lowdin's (equal on a free atom) every sign "
        "holds: CuH shortens under both laws, binds more under min and less under mirror, and Cu metal contracts", ok8)
    bnd = o.get("band", {})
    ok9 = all(k in bnd for k in (("Cu", "ours"), ("Cu", "min"), ("Cu", "mirror"), ("Au", "ours"), ("Au", "mirror")))
    ok9 = ok9 and bnd[("Cu", "min")]["edge"] < bnd[("Cu", "ours")]["edge"] and bnd[("Cu", "mirror")]["edge"] < bnd[("Cu", "ours")]["edge"]
    ok9 = ok9 and bnd[("Au", "mirror")]["edge"] > bnd[("Au", "ours")]["edge"]
    ok9 = ok9 and abs(bnd[("Cu", "ours")]["edge"] + 1.240) < 2e-3 and abs(bnd[("Au", "mirror")]["edge"] + 1.356) < 2e-3
    ok9 = ok9 and ("Ag", "mirror") in bnd and bnd[("Ag", "mirror")]["edge"] - bnd[("Ag", "ours")]["edge"] > 1.0
    ok9 = ok9 and all(bnd[("Au", "ours")]["edges"][p] < bnd[("Ag", "mirror")]["edges"][p] < bnd[("Cu", "ours")]["edges"][p]
                      and bnd[("Ag", "mirror")]["edges"][p] - bnd[("Ag", "ours")]["edges"][p] > 0.6 for p in (0.90, 0.95, 0.97, 0.98))
    add("X9 the d band (8x8x8 k): the upper edge of copper's occupied d band falls 0.14 / 0.07 eV further below E_F (its "
        "absorption onset moves to the blue), gold's rises 0.17 eV (mirror; to the red); silver's rises 1.23 eV (mirror; more than 0.6 eV "
        "for every 90-98 % rule), between gold's and copper's edges under our law for every rule", ok9)
    touched = {el for mm in d["molecules"] for el in mm["delta_eV"]} | {s["el"] for s in d["solids"] if s["law"] != "ours"}
    fl = [mm["E_atoms_run"]["F"] for mm in d["molecules"] if "F" in mm.get("E_atoms_run", {})]
    add("X7 (structural) the law touches only exception elements (every element given a delta is one of NIST's twenty), "
        "and an atom it does not touch is the same atom in both universes (H banked once; F identical across the laws' runs)",
        touched <= set(d["nist"]) and len(d["atoms_pbe0"]["H"]) == 1 and (max(fl) - min(fl) < 1e-9 if fl else True))
    return res


MUTANTS = {"omega_no_bohr": "omega_e from E'' in Ha/A^2 (the bohr^2 conversion dropped, as the board's first fit did)",
           "mixed_atom": "the PBE0 Au atom under min left in the SCF's mixed state (0.013 eV below), not the lowest known",
           "min_is_mirror": "the min law's target taken as the full NIST gap",
           "gauge_dropped": "the solids' energies without the gauge constant -delta N_obs",
           "no_extrapolation": "the calibration refuses to extrapolate where the aufbau state collapsed"}


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
        print("  mutant %-16s %-75s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
