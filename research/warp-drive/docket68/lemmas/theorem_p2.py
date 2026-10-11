#!/usr/bin/env python3
"""theorem_p2.py -- item 225: back to the warp theorem with the data of positions 2a, 2b and 2c.  M: "Continue. Keep
all the work here please" (on the board's plan: item 201's units first, then sigma, position 2's G and m, and the bulk's
reading of position 2's plane).  Worked in the conversation, with no workflows; 2026-10-11.

The plan, from the report of item 224: item 201's units first, then sigma, position 2's G and m, and the bulk's reading
of position 2's plane.  Computed, deduced and READ; one question put to M and answered (item 226); checked in the
conversation by three lenses; not verified by a separate session; not seated beyond what the history records.

  TA (READ; computed; cypher) Item 201's units.
     - READ: the SI's seven defining constants are the Cs-133 hyperfine frequency, c, h, e, k, N_A and K_cd (SI
       Brochure 9th ed., section 2.2).  None is G, and caesium is not one of NIST's twenty exception elements, so the
       SI is realised identically in ours and in 2a, 2b and 2c.  Planck units carry G, and are not.
     - Eight readings, as cells: SI or Planck units, with neither, either or both of the coupling and the matter law
       as further coordinates.  For each, the six universes' cells were computed.
     - The target (fits 201 as stated in J/m^3; a standard all six share; every universe its own cell) is held by one
       reading: sigma and the offset in SI, with the coupling and the matter law as further coordinates.
     - SI with the coupling alone leaves 2a with ours, and SI with the matter law alone leaves 2b with ours.  Planck
       alone gives exactly SI-with-the-coupling's two cells: Planck units carry the coupling but not the matter law.
     - Every language also admits the target with one further coordinate, which no reading holds: a join, not a
       reading.  The audit finds no key; stated/shared and d2c/all_distinct are equal columns.
  TB (structural; computed; deduced) sigma in the theorem.
     - WARPTHEOREM.md's head table had not been regenerated since item 206.  It still showed 34 lemmas, with B6' as
       "nature", against warptheorem.py's 51 rows (45 lemmas, 6 inputs; 17 proved, 18 derived, 4 definitions, 6 OPEN;
       then 21 green strict, 25 counting definitions; 22 and 26 since item 229 derived B5px; 32 and 36 since item 231
       derived M1, an input counting green by its own status), where B6' is a
       DEFINITION on item 201.  The history had carried the
       true count since item 206.  The head is now generated from the instrument, and checked against it here.
     - B6' (201) defines our universe among those with our laws.  Under one coupling (H-ONE-G5) sigma fixes G and ell.
       Across couplings, sigma and the offset fix only G ell^2 = 3c^4/(4 pi (sigma - 2 delta sigma)): 1.301444e-20 in
       ours and in 2b.
     - The theorem reads sigma only through ell/m in corridor units, (ell/m)^2 = (3/ln2)(sigma_P/sigma)/N, that is
       through sigma/sigma_P (M1's ring at ell/m = 8.5415; the bulk's depth and far boundary).  The offset enters one
       row, B5px, as delta sigma_2 against sigma: a ratio, the same in any units.  I2's capacity is Planck-unit
       (A_bit = 4 ln2 l_P^2) and uses neither.  So 2b at sigma is, for every clause that depends on ell, ours at 4 sigma: ell/m agrees
       exactly at N = 1, 676 and 1e6.
     - The window's top (ITEM197's ell > 8.5415 m1) is 0.0593236 sigma_P in both universes: 2.7484e112 J/m^3 in ours,
       6.8711e111 in 2b.  Item 201 defines sigma in SI; the theorem reads it in Planck units.
  TC (computed; deduced) Position 2's G and m between universes, per candidate (one E, 203).
     - 2a and item 218's identical universe: m2 = m, capacity N.  2b and 2c: m2 = 2m, capacity 2N, the per-sheet value
       reached by a law.  139 (1)'s plane: 2m and 2N on the per-sheet count.
     - B5px's normal half at the pin, (summed tension) + delta sigma_2 + rho1 + rho2 >= 0: met by every positive
       candidate (summed tension +2 sigma, offset ours, matter ordinary); undecided for 139's plane, offset unstated.
  TD (computed; M's answer, item 226) Position 2's plane.
     - Seven theorem rows rest on 139 (1)'s negative plane (found in the instrument's own text): H2tx, O3, B4d, B5px,
       B6, M1P2x, FAR.  O3's and B4d's are plane-carried stage readings, set aside for M's configuration by item 179.
     - Put to M; M chose "Its own values" (item 226).  A position 2 carries its own universe's values, so 2a, 2b and 2c
       are positive planes.
     - B6, recomputed with Israel's tau = 3[A']/kappa^2 (standard, not READ, as b6_once.py labels it) in b6_once.py's
       convention (control: the quarter gives k_R = k_L/2).  In each position's own view (214, 215), k2/k1 = 1 (2a) and sqrt 2 (2b, 2c), matching item 223's
       k x sqrt 2.  In b6_once's slab, a plane at +sigma gives k_R = 3 k_L.  A negative plane cannot close its own
       bulk.
     - FAR, recomputed on far_bridge.py's own junction forms: 20000 points per arm, sampled in mu in [0.05, 3],
       ell_s in [0.2, 3], ell_2 in [0.2, 6] and R in (1.01, 6) r_h; the counts belong to that box.  With position 2's plane on the
       decaying outer side (k = 1), 18741 meet the surface WEC, which with F1 keeps (Z) at the plane.  The growing side
       (k = 1) and both sides at k = 0 meet it nowhere.  FAR is narrowed, not met: the k = 0 failure never depended on
       the plane's sign.
     - H2tx and M1P2x: position 2's G2 is its law's, so m2 = (G2/G) m: m for 2a, 2m for 2b and 2c.

What this does not show.
  - No status in warptheorem.py moves on this instrument alone.  The history records what was seated.
  - The own-view reading of B6 rests on items 214 and 215 (each bulk closing on its own mirror).  The slab is the
    reading of item 200 (1).
  - FAR's positive arm is the board's scan of model C's family; a far model is still to be chosen.

Reads p2_gravity.py, p2_matter.py's bank (load only), tools/cypher.py and index_audit.py by path, and the rulings file
(read-only).  Stdlib.  python3 theorem_p2.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import itertools
import os
import sys
from fractions import Fraction as F

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D68)))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M225 = "Continue. Keep all the work here please"


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


PG = _load(os.path.join(HERE, "p2_gravity.py"), "tp2_pg")
G, Q4 = PG.G, PG.Q4
UNIVERSES = {"ours": ("ours", 1), "2a-min": ("min", 1), "2a-mirror": ("mirror", 1), "2b": ("ours", Q4),
             "2c-min": ("min", Q4), "2c-mirror": ("mirror", Q4)}
LANGS = ("order", "algebra", "geometry", "information", "statistics")
OPTS = {"statistics_order": 2, "algebra_budget": 10 ** 6}

# ------------------------------------------------------------------------------------------- A: item 201's units
# READ, the SI Brochure, 9th edition, section 2.2 (BIPM, retrieved 2026-10-11): the SI is the system in which seven
# constants take fixed values.  What each depends on, of the two laws positions 2a-2c change: the d-shell law acts on
# atoms of NIST's twenty exception elements only (item 221); the coupling acts on G only (item 223)
SI_READ = ("the unperturbed ground state hyperfine transition frequency of the caesium 133 atom ... the Planck constant "
           "... the elementary charge ... the Boltzmann constant ... the Avogadro constant ... the luminous efficacy",
           "https://www.bipm.org/documents/20126/41483022/SI-Brochure-9-EN.pdf")
SI_DEFINING = {"Cs-133 hyperfine frequency": {"element": "Cs", "G": False}, "c": {"element": None, "G": False},
               "h": {"element": None, "G": False}, "e": {"element": None, "G": False}, "k": {"element": None, "G": False},
               "N_A": {"element": None, "G": False}, "K_cd": {"element": None, "G": False}}
PLANCK_DEFINING = {"l_P = sqrt(hbar G / c^3)": {"element": None, "G": True}}


def unit_shared(defining, exceptions):
    """is a unit system realised identically in all six universes?  Only if none of its defining constants depends on
    G (changed in 2b, 2c) or on an exception element's atom (changed in 2a, 2c)"""
    if MUT.get("cs_is_exception"):
        exceptions = set(exceptions) | {"Cs"}
    return all(not d["G"] and d["element"] not in exceptions for d in defining.values())


def coordinates(units, extras):
    """each universe's coordinates under a reading of item 201: sigma and the offset in SI or in its own Planck units,
    with or without the coupling and the matter law as further coordinates"""
    out = {}
    for u, (law, q) in UNIVERSES.items():
        if units == "SI":
            c = ("%.12g" % PG.SIGMA_WINDOW[0], "%.12g" % PG.DSIG)
        else:
            p = PG.planck_content(G * q)
            c = ("%.12g" % p["sigma"], "%.12g" % p["offset"])
        if "kappa5" in extras:
            c += (q,)
        if "matter" in extras:
            c += (law,)
        out[u] = c
    return out


def readings(exceptions):
    """every reading: units x the further coordinates; for each, the six universes' cells and what the reading does"""
    out = {}
    for units in ("SI", "Planck"):
        for k in range(3):
            for extras in itertools.combinations(("kappa5", "matter"), k):
                co = coordinates(units, extras)
                cells = {}
                for u, c in co.items():
                    cells.setdefault(c, []).append(u)
                same = lambda a, b: co[a] == co[b]
                out[(units, extras)] = dict(
                    cells=sorted(sorted(v) for v in cells.values()),
                    stated=(units == "SI") != bool(MUT.get("stated_planck")),  # 201 states delta sigma in J/m^3
                    shared=unit_shared(SI_DEFINING if units == "SI" else PLANCK_DEFINING, exceptions),
                    d2a=not same("2a-min", "ours"), d2b=not same("2b", "ours"),
                    d2c=not same("2c-min", "2a-min") and not same("2c-min", "2b"),
                    all_distinct=len(cells) == len(UNIVERSES), n_extra=len(extras))
    return out


A_COORDS = ["stated", "shared", "d2a", "d2b", "d2c", "all_distinct", "n_extra"]
A_TARGET = (1, 1, 1, 1, 1, 1)          # fits 201 as stated, a standard all six share, every universe its own cell


def question_a(cy, ia, exceptions):
    rd = readings(exceptions)
    rows = {k: tuple(int(v[c]) for c in A_COORDS) for k, v in rd.items()}
    ix = cy.Index("tp2_units", A_COORDS, [list(r) for r in sorted(set(rows.values()))],
                  value_order={c: ([0, 1, 2] if c == "n_extra" else [0, 1]) for c in A_COORDS})
    runs = {r: cy.run(ix, r, OPTS) for r in ("1173", "33.1", "20.2")}
    held = sorted(k for k, r in rows.items() if r[:6] == A_TARGET)
    best = min((rows[k][6] for k in held), default=None)
    admits = {}
    for lang in LANGS:
        adm, _ = cy.ADMISSION[lang][0](ix, OPTS)
        admits[lang] = None if adm is None else sorted(
            n for n in range(3) if tuple(ix.code[i][v] for i, v in enumerate(A_TARGET + (n,))) in adm)
    crow, keys = cy.coordinate_report(ix)
    return dict(readings=rd, rows=rows, held=held, simplest=[k for k in held if rows[k][6] == best], admits=admits,
                runs=runs, audit=ia.audit_index(A_COORDS, sorted(set(rows.values()))),
                adds_nothing=[r["coordinate"] for r in crow if r["adds_nothing"]],
                si_shared=unit_shared(SI_DEFINING, exceptions), planck_shared=unit_shared(PLANCK_DEFINING, exceptions))


# ------------------------------------------------------------------------------------------- B: sigma in the theorem
WT = os.path.join(D68, "warptheorem.py")
WTMD = os.path.join(D68, "WARPTHEOREM.md")
ELL_MIN_OVER_M1 = 8.5415                        # sigma_cypher W1: ITEM197's positivity, ell > 8.5415 m1 (1-bit README)


def _wt_rows():
    """warptheorem.py's lemma list, read as data (ast), without running the instrument"""
    import ast
    mods = {n.targets[0].id: n.value for n in ast.parse(open(WT, encoding="utf-8").read()).body
            if isinstance(n, ast.Assign) and hasattr(n.targets[0], "id")}
    return ast.literal_eval(mods["LEMMAS"]), ast.literal_eval(mods["RESTS_ON"])


def head_table():
    """does WARPTHEOREM.md's head table carry warptheorem.py's rows and statuses, and its count?"""
    import re
    L, R = _wt_rows()
    md = open(WTMD, encoding="utf-8").read()
    head = md[md.index("## Its lemmas"):md.index("## The energy ledger")]
    st = {"proved": "PROVED", "derived": "DERIVED", "definition": "DEFINITION", "**OPEN**": "OPEN"}
    rows = {}
    for line in head.splitlines():
        p = [x.strip() for x in line.split("|")]
        if len(p) > 4 and p[1] in "GHOZBIERN" and len(p[1]) == 1:
            rows[p[2].split()[0]] = st.get(p[3], p[3])
    inst = {n.split()[0]: s for _, n, s, _ in L}
    lem = [(c, n.split()[0], s) for c, n, s, w in L if c != "N"]
    gin = {n.split()[0] for c, n, s, w in L if c == "N" and s in ("PROVED", "DERIVED")}   # inputs green by own status
    strict = sum(1 for c, k, s in lem if s in ("PROVED", "DERIVED") and all(i in gin for i in R.get(k, "").split()))
    count = "%d rows, %d lemmas and %d inputs" % (len(L), len(lem), len(L) - len(lem))
    return dict(agree=rows == inst, n_md=len(rows), n_inst=len(inst), count=count, count_in_md=count in head,
                green=strict, green_in_md="**%d green**" % strict in head, b6=inst.get("B6'"))


def ell_over_m(Gx, sigma, N):
    """the corridor's ell in units of its README mass: (ell/m)^2 = (3/ln2)(sigma_P/sigma)/N, from the two definitions"""
    ell = (3 * PG.C ** 4 / (4 * PG.math.pi * Gx * (sigma - 2 * PG.DSIG))) ** 0.5
    return ell / (PG.corridor(Gx)["m1"] * N ** 0.5)


def question_b():
    s0 = PG.SIGMA_WINDOW[0]
    pairs = {}
    for N in (1, 676, 10 ** 6):
        pairs[N] = dict(ours=ell_over_m(G, s0, N), p2b=ell_over_m(Q4 * G, s0, N), ours4=ell_over_m(G, Q4 ** 2 * s0, N))
    # the window's edges in each universe's SI: the floor at the table-top ell (relative reading, item 223) and the
    # top at ell = 8.5415 m1 (ITEM197); in Planck units both edges are the same in ours and 2b
    win = {}
    for u, Gx in (("ours", G), ("2b", Q4 * G)):
        m1 = PG.corridor(Gx)["m1"]
        kap = 3 * PG.C ** 4 / (4 * PG.math.pi * Gx)
        top = kap / (ELL_MIN_OVER_M1 * m1) ** 2
        sP = PG.corridor(Gx)["sigma_P"]
        win[u] = dict(top=top, top_planck=top / sP, floor_rel=kap / PG.ELL_MAX ** 2 + 2 * PG.DSIG)
    gl2 = {u: Gx * (3 * PG.C ** 4 / (4 * PG.math.pi * Gx * (s0 - 2 * PG.DSIG))) for u, Gx in (("ours", G), ("2b", Q4 * G))}
    return dict(head=head_table(), pairs=pairs, win=win, gl2=gl2)


# ------------------------------------------------------------------------------------------- C: position 2's G and m
# candidates for the theorem's position 2: the three of items 219-224 (our sigma and offset, by 223 (b)), item 218's
# identical universe, and item 139 (1)'s plane (-sigma/4; its offset unstated, item 223's record read)
CANDIDATES = {"2a": dict(G2=1, sigma2=1, offset2="ours", matter="d-shell law"),
              "2b": dict(G2=Q4, sigma2=1, offset2="ours", matter="ours"),
              "2c": dict(G2=Q4, sigma2=1, offset2="ours", matter="d-shell law"),
              "identical (218)": dict(G2=1, sigma2=1, offset2="ours", matter="ours"),
              "139 (1) plane": dict(G2=Q4, sigma2=-0.25, offset2=None, matter=None)}


def question_c():
    """M1P2x / H2tx under one E (203): m2/m = G2/G and capacity (G2/G) N; B5px's normal half at the pin, (sum of the
    two planes' tensions) + delta sigma_2 + rho1 + rho2 >= 0, with every candidate's own tension and offset"""
    out = {}
    for name, c in CANDIDATES.items():
        tr = PG.trip(G, G * c["G2"])
        summed = 1 + c["sigma2"]                                   # in units of our sigma, at coincidence (127)
        if c["offset2"] is None:
            normal = None                                          # "which no ruling gives" (B5px, item 211)
        else:
            normal = summed > 0                                    # offset ours (> 0) and matter rho >= 0
        out[name] = dict(m_ratio=tr["m_ratio"], capacity=tr["capacity_ratio"], summed=summed, b5px_normal=normal,
                         positive_plane=c["sigma2"] > 0)
    return out


# ------------------------------------------------------------------------------------------- D: position 2's plane
# which theorem rows rest on item 139 (1)'s negative plane (computed from the instrument's own text), and what each
# reading of position 2's plane does to them (DEDUCED; the board's, for M to decide between)
P139 = r"139 \(1\)|139's negative|negative-tension|per-sheet|3/4\) sigma|negative-P2|plane counts once"
CONSEQ = {
    "B6": ("stands: k_R = k_L/2 from the per-sheet count",
           "per destination: own view k2/k1 = 1 (2a), sqrt 2 (2b, 2c); b6_once's slab with tau2 = +sigma gives 3"),
    "H2tx": ("stands: m2 = 2m, capacity 2N on the per-sheet count", "by the law: m2 = m, N (2a); 2m, 2N (2b, 2c)"),
    "M1P2x": ("stands: the per-sheet reading", "the per-sheet reading replaced by the law's G2"),
    "B5px": ("undecided: position 2's offset unstated", "normal half met: offset ours, matter ordinary, plane +sigma"),
    "FAR": ("fails as computed: sigma_2 |n.k| < 0 on every ray meeting the plane",
            "narrowed: k = 1 with the plane on the decaying side meets the surface WEC; k = 0 fails either side"),
    "O3": ("a plane-carried stage reading, set aside for M's configuration by item 179", "the same"),
    "B4d": ("a plane-carried stage reading, set aside for M's configuration by item 179", "the same"),
}


def b6_recompute():
    """B6's ratio under item 226, from Israel's junction tau = 3[A']/kappa^2 in b6_once.py O1's convention (its control
    reproduced first: the quarter, counted once, gives k_R = k_L/2).  Two geometries: b6_once's slab (position 2's plane
    joins the slab, k_L, to its own bulk beyond, k_R; one coupling) and each position's own view (214, 215: a plane
    closing its own bulk on both sides, tau = 6k/kappa^2, with its own coupling)"""
    from fractions import Fraction as Fr
    slab = lambda q: 1 + 2 * Fr(q)                  # tau2/tau1 = (k_R - k_L)/(2 k_L) = q  =>  k_R/k_L = 1 + 2q
    control = slab(Fr(-1, 4))
    out = {"control_quarter": control, "slab_2a": slab(Fr(-1, 4) if MUT.get("b6_quarter_kept") else 1)}
    # own view: k = kappa^2 sigma / 6 per universe; kappa^2 ratio = sqrt(kappa^4 ratio)
    for name, q4 in (("2a", 1), ("2b", Q4), ("2c", Q4)):
        out["own_" + name] = (q4 ** 0.5) * 1.0       # sigma2/sigma1 = 1 (226: our sigma)
    out["own_139"] = None                             # a negative plane cannot close its own bulk with k > 0
    return out


def far_recompute(n=20000, seed=226):
    """FAR's model C under item 226: far_bridge.py's own junction forms (imported), scanned on both outer sides for a
    plane meeting the surface WEC (rho > 0, rho + p >= 0) -- with F1, the condition for (Z) at the plane"""
    import math
    import random
    fb = _load(os.path.join(HERE, "far_bridge.py"), "tp2_fb")
    import sympy as sp
    f1, f = fb.f1(), fb.f23()
    R, mu, ls, l2 = sp.symbols("R mu ell_s ell_2", positive=True)
    res = {}
    for (k, eps), v in f["forms"].items():
        sgn = eps if not MUT.get("far_side_swapped") else -eps
        rho = sp.lambdify((R, mu, ls, l2), 3 * (sp.sqrt(v["fs"]) + sgn * sp.sqrt(v["fo"])) / R)
        B = sp.lambdify((R, mu, ls, l2), v["B"])
        rnd = random.Random(seed)
        good = tot = 0
        for _ in range(n):
            m_, a, b = rnd.uniform(0.05, 3), rnd.uniform(0.2, 3), rnd.uniform(0.2, 6)
            rh = math.sqrt((-k * a * a + math.sqrt(k * k * a ** 4 + 4 * a * a * m_)) / 2)
            Rv = rh * rnd.uniform(1.01, 6)
            r_, b_ = rho(Rv, m_, a, b), B(Rv, m_, a, b)
            if isinstance(r_, complex) or isinstance(b_, complex):
                continue
            tot += 1
            good += r_ > 0 and b_ >= 0
        res[(k, "decaying" if eps == 1 else "growing")] = (good, tot)
    return dict(tension_share=f1["tension"], scan=res)


def question_d():
    import re
    L, _ = _wt_rows()
    rows = {}
    for c, n, st, w in L:
        hits = sorted(set(re.findall(P139, n + " " + w)))
        if hits:
            rows[n.split()[0]] = dict(status=st, hits=hits)
    return dict(rows=rows, conseq={k: CONSEQ.get(k) for k in rows}, b6=b6_recompute(), far=far_recompute())


def compute():
    cy = _load(os.path.join(ROOT, "tools", "cypher.py"), "tp2_cy")
    ia = _load(os.path.join(HERE, "index_audit.py"), "tp2_ia")
    pm = _load(os.path.join(HERE, "p2_matter.py"), "tp2_pm")
    exceptions = set(pm.load()["nist"])
    return dict(exceptions=exceptions, A=question_a(cy, ia, exceptions), B=question_b(),
                C=question_c(), D=question_d())


def report(o):
    print("theorem_p2.py -- back to the warp theorem with positions 2a, 2b, 2c (item 225)\n")
    A = o["A"]
    print("A. item 201's units.  NIST's exception elements (%d): %s" % (len(o["exceptions"]), " ".join(sorted(o["exceptions"]))))
    print("   the SI's seven defining constants shared by all six universes: %s; Planck units: %s" % (
        A["si_shared"], A["planck_shared"]))
    for k, r in A["readings"].items():
        print("   %-6s + %-18s cells %d %s  %s" % (k[0], ",".join(k[1]) or "-", len(r["cells"]), r["cells"],
                                                 "".join(map(str, A["rows"][k]))))
    print("   coordinates %s; target %s (any n_extra)" % (A_COORDS, A_TARGET))
    for rn, res in A["runs"].items():
        print("   roster %s: %s" % (rn, "; ".join("%s %s E=%s" % (v["language"], v["state"], v["E"]) for v in res["verdicts"])))
    print("   held by %s; the fewest further coordinates: %s; admitted (n_extra values) per language %s" % (
        A["held"], A["simplest"], A["admits"]))
    print("   audit %s; adds nothing %s" % (A["audit"], A["adds_nothing"]))


    B = o["B"]
    h = B["head"]
    print("\nB. sigma in the theorem.  WARPTHEOREM.md's head table agrees with warptheorem.py: %s (%d rows against %d); "
          "count '%s' in it: %s; %d green in it: %s; B6' is %s" % (h["agree"], h["n_md"], h["n_inst"], h["count"],
                                                                h["count_in_md"], h["green"], h["green_in_md"], h["b6"]))
    print("   G ell^2 = %.6e (ours), %.6e (2b) m^5 kg^-1 s^-2: sigma and the offset fix it whatever kappa5" % (
        B["gl2"]["ours"], B["gl2"]["2b"]))
    for N, r in B["pairs"].items():
        print("   N = %-8d ell/m: ours at sigma %.6e; 2b at sigma %.6e; ours at 4 sigma %.6e" % (N, r["ours"], r["p2b"], r["ours4"]))
    for u, w in B["win"].items():
        print("   %-4s window top (ell = 8.5415 m1) %.4e J/m^3 = %.6e sigma_P; floor (table-top, relative) %.4e" % (
            u, w["top"], w["top_planck"], w["floor_rel"]))


    print("\nC. position 2's G and m between universes, per candidate for the theorem's position 2 (one E, 203):")
    for n, c in o["C"].items():
        print("   %-16s m2/m %g, capacity %g N; summed tension at the pin %+.2f sigma; B5px normal half: %s; its plane "
              "positive: %s" % (n, c["m_ratio"], c["capacity"], c["summed"],
                                {None: "undecided (offset unstated)", True: "met", False: "fails"}[c["b5px_normal"]],
                                c["positive_plane"]))


    print("\nD. theorem rows resting on item 139 (1)'s negative plane (from warptheorem.py's text), and each reading:")
    for k, r in o["D"]["rows"].items():
        c = o["D"]["conseq"][k] or ("?", "?")
        print("   %-6s %-10s %s\n          if every position 2 has 139's plane: %s\n          if position 2 carries its own "
              "universe's values (2a-2c: +sigma): %s" % (k, r["status"], r["hits"], c[0], c[1]))


    b6, far = o["D"]["b6"], o["D"]["far"]
    print("   B6 recomputed: control (quarter, counted once) k_R/k_L = %s; slab with tau2 = +sigma (2a) %s; own view (214) "
          "k2/k1 = %.6f (2a), %.6f (2b), %.6f (2c); 139's plane in its own view: %s" % (
              b6["control_quarter"], b6["slab_2a"], b6["own_2a"], b6["own_2b"], b6["own_2c"], b6["own_139"]))
    print("   FAR recomputed (far_bridge's forms; a pure tension's share sigma |n.k|: %s): %s" % (
        far["tension_share"], {"k=%d %s" % k: "%d/%d meet the surface WEC" % v for k, v in far["scan"].items()}))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("T0 M's item-225 words and item 226's choice verbatim in the rulings file",
        M225 in rul and 'M chose: "Its own values"' in rul)
    A = o["A"]
    ncell = {k: len(v["cells"]) for k, v in A["readings"].items()}
    ok = A["si_shared"] and not A["planck_shared"] and A["held"] == [("SI", ("kappa5", "matter"))]
    ok &= ncell == {("SI", ()): 1, ("SI", ("kappa5",)): 2, ("SI", ("matter",)): 3, ("SI", ("kappa5", "matter")): 6,
                    ("Planck", ()): 2, ("Planck", ("kappa5",)): 2, ("Planck", ("matter",)): 6,
                    ("Planck", ("kappa5", "matter")): 6}
    ok &= A["readings"][("Planck", ())]["cells"] == A["readings"][("SI", ("kappa5",))]["cells"]
    ok &= all(A["admits"][l] == [1, 2] for l in LANGS) and A["audit"]["keys"] == []
    ok &= sorted(A["audit"]["onehot"]) == [("d2c", "all_distinct"), ("stated", "shared")]
    add("TA the SI shared by all six universes, Planck units not; the target held by SI + coupling + matter law alone; "
        "the cells per reading as computed; Planck alone = SI + coupling; one-coordinate admission a join; no key", ok)
    B = o["B"]
    h = B["head"]
    ok = h["agree"] and h["count_in_md"] and h["green_in_md"] and h["count"] == "51 rows, 45 lemmas and 6 inputs"
    ok &= h["green"] == 32 and h["b6"] == "DEFINITION"     # 21 until item 229 (B5px), 22 until item 231 (M1)
    ok &= all(abs(r["p2b"] / r["ours4"] - 1) < 1e-12 and abs(r["ours"] / r["p2b"] - 2) < 1e-12 for r in B["pairs"].values())
    ok &= "%.6e" % B["gl2"]["ours"] == "1.301444e-20" and abs(B["gl2"]["2b"] / B["gl2"]["ours"] - 1) < 1e-12
    ok &= ["%.6e" % B["win"][u]["top_planck"] for u in ("ours", "2b")] == ["5.932360e-02"] * 2
    ok &= ("%.4e" % B["win"]["ours"]["top"], "%.4e" % B["win"]["2b"]["top"]) == ("2.7484e+112", "6.8711e+111")
    add("TB WARPTHEOREM.md's head agrees with warptheorem.py (51 rows, 32 green since item 231, B6' a DEFINITION); G ell^2 1.301444e-20 "
        "in ours and 2b; 2b at sigma has ours-at-4-sigma's ell/m at every N; the window's top 0.0593236 sigma_P in both", ok)
    C = o["C"]
    ok = [(C[n]["m_ratio"], C[n]["capacity"], C[n]["b5px_normal"]) for n in CANDIDATES] == [
        (1, 1, True), (2, 2, True), (2, 2, True), (1, 1, True), (2, 2, None)]
    add("TC per candidate: m2/m and capacity 1, 2, 2, 1, 2 (2a, 2b, 2c, 218, 139's plane); B5px's normal half met by every "
        "positive plane, undecided for 139's", ok)
    D = o["D"]
    ok = sorted(D["rows"]) == sorted(["H2tx", "O3", "B4d", "B5px", "B6", "M1P2x", "FAR"])
    b6 = D["b6"]
    ok &= b6["control_quarter"] == F(1, 2) and b6["slab_2a"] == 3 and b6["own_2a"] == 1.0
    ok &= abs(b6["own_2b"] - 2 ** 0.5) < 1e-12 and b6["own_139"] is None
    sc = D["far"]["scan"]
    ok &= D["far"]["tension_share"] and sc[(1, "decaying")] == (18741, 20000)
    ok &= all(sc[k][0] == 0 for k in ((1, "growing"), (0, "growing"), (0, "decaying")))
    add("TD seven rows rest on 139 (1) (H2tx, O3, B4d, B5px, B6, M1P2x, FAR); B6: the control k_L/2 reproduced, own view "
        "1 / sqrt 2, slab +sigma 3; FAR: 18741/20000 decaying k = 1 points meet the surface WEC, none elsewhere", ok)
    return res


MUTANTS = {"cs_is_exception": "caesium counted among the exception elements (the SI no longer shared)",
           "stated_planck": "item 201 read as stated in Planck units",
           "b6_quarter_kept": "B6's slab recomputed with 139's quarter kept for a positive destination",
           "far_side_swapped": "FAR's outer sides swapped (decaying read as growing)"}


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
        print("  mutant %-17s %-80s %s" % (k, desc, "caught by " + ", ".join(sorted(set(failed))) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
