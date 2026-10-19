#!/usr/bin/env python3
"""read_index.py -- item 486 (3): the read's error calculated from M's own indexes, on water, an alcohol and steel, to a
formula for any number of atoms.  M, 486: "use my indexes and calculate it yourself instead of relying on outside
numbers. Use a simple molecule like and alcohol molecule, or water, or steel so the calculation establishes a formula for
calculating larger amounts of atoms".  Labels: computed (exact unless marked), deduced, READ (through the indexes),
DERIVED (arithmetic on an index value), M's.  Worked in the conversation; not verified; not seated.

The indexes used, imported by path and never copied: the element index (tools/populate.py: each element's observed
ground configuration, LW1-ground.py, READ; the Pauli capacities 2(2l+1), PINNED; R_inf, alpha and m_e as it carries
them) and the isotope index (tools/isotopes.py: AME2020 Table I, READ).  No device figure enters.

  D0 (read) M's words, verbatim in the rulings file: 486.
  D1 (DERIVED from the element index) Each atom's label and what it binds.  Z is the configuration's electron count
     (checked for every element used); the bonds an atom makes are its outer s-p shell's electrons or vacancies,
     whichever is fewer (min(e, 8 - e); min(e, 2 - e) for the first shell): H 1, C 4, O 2.
  D2 (computed) The structure labels a molecule needs.  Every bond graph the valences of D1 admit, kept once by
     ENCODE's canonical code (encode_labels C2): water admits one (its structure follows from its labels, 0 bits to
     read); C2H6O admits two, ethanol and dimethyl ether (one bit to read, which atom the oxygen binds).
  D3 (DERIVED from both indexes) The signal that tells an element from its neighbours.  The K-shell scale E_K = Z^2 R_M
     h c, R_M the Rydberg reduced by the element's nuclear mass (AME2020's lightest beta-stable nuclide; populate's
     reduced_rydberg); the gaps to Z - 1 and Z + 1 are (2Z -+ 1) R_M h c to 1e-4, 41 eV (H) to 776 eV (Cu) -- the
     index's own Dirac term changes them by at most 2.3 % (Cu), and they never close.
  D4 (computed) The error of one atom's read.  An energy read over a window t resolves sigma = hbar/(2t) (the Fourier
     limit, quantum mechanics); a neighbour at gap D is taken for the atom's own label with probability Q(D t/hbar), Q the
     Gaussian tail; a thermal mimic needs D of energy, e^(-D/kT) = e^(-1578) at 300 K for hydrogen.  So p(t) = Q(D- t/hbar)
     + Q(D+ t/hbar): it falls as e^(-(D t/hbar)^2/2), exponentially in the window.  (A projective read of the charge, an
     eigenvalue, has no intrinsic error at all; this is the conservative read.)
  D5 (computed) The formula.  A read of n atoms exact with probability 1 - eps needs every atom's error below eps/n:
          rho(n) = Q^-1(eps/(2n)) ~ sqrt(2 ln(2n/eps)),   t_i = rho(n) hbar/D_i,   T(n) = rho(n) hbar sum_i 1/D_i,
     each site's presence read with q >= ln(n/eps) quanta, and each structure label with d/sigma_x >= 2 rho(n_s).  The
     window per atom grows only as the square root of the logarithm of the number of atoms.
  D6 (computed) The examples (eps = 1e-2):
          water, one molecule (n = 3): rho = 2.94, t = 4.7e-17 s (H), 9.5e-18 s (O); structure 0 bits
          ethanol, one molecule (n = 9): rho = 3.26, t = 5.3e-17 s (H) and less; structure 1 bit, d/sigma_x >= 5.2
          steel (Fe, 1 atom-% C), one mole: rho = 10.65, t = 1.0e-17 s per Fe atom, T = 6.3e6 s for the mole in sequence
          stainless steel (Fe 72, Cr 18, Ni 8, Mn 2 atom-%), one mole: rho = 10.65; Mn sits 667 and 694 eV from Cr, Fe
          1 cm^3 of copper (8.49e22 atoms): per-atom error 1.2e-25, rho = 10.47, t = 8.9e-18 s per atom
     A per-atom error of 1e-2 needs rho = 2.58: the 1.2e-25 the copper needs is the same read for 4.1 times as long.
  D7 (DERIVED from the isotope index) A read by mass would be harder: the elements of steel share beta-stable isobars
     (54Cr and 54Fe, 58Fe and 58Ni, 64Ni and 64Zn), apart by 1.3e-5 of their mass at least (computed from AME2020), against
     the K-shell signal's 8 % between Mn and Fe.  So the read's label is electronic, as M-ISOTOPE-OUT makes it.

python3 read_index.py [--selftest | --mutants]
"""
import os, sys, math, re, itertools, importlib.util
from statistics import NormalDist

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
REPO = os.path.abspath(os.path.join(D68, "..", "..", ".."))
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((486, "use my indexes and calculate it yourself instead of relying on outside numbers"),)
HBAR = 1.054571817e-34; H = 6.62607015e-34; C = 299792458.0; EV = 1.602176634e-19; KB = 1.380649e-23
NA = 6.02214076e23
_N = NormalDist()
Qinv = lambda x: -_N.inv_cdf(x)                                             # the Gaussian tail's inverse
Q = lambda x: 0.5 * math.erfc(x / math.sqrt(2))                             # the Gaussian tail


def _load(path, alias):
    spec = importlib.util.spec_from_file_location(alias, path)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


_IDX = {}


def indexes():
    if not _IDX:
        sys.path.insert(0, os.path.join(REPO, "tools"))
        _IDX["P"] = _load(os.path.join(REPO, "tools", "populate.py"), "ri_populate")
        _IDX["I"] = _load(os.path.join(REPO, "tools", "isotopes.py"), "ri_isotopes")
        _IDX["rows"] = _IDX["I"].read()
        _IDX["EL"] = _load(os.path.join(HERE, "encode_labels.py"), "ri_el")
    return _IDX


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


# ------------------------------------------------------------------ D1
def label(Z):
    P = indexes()["P"]
    cfg = P.config_of(Z)
    e = sum(o for _, _, o in cfg)
    nmax = max(n for n, _, _ in cfg)
    outer = sum(o for n, l, o in cfg if n == nmax and l <= 1)
    cap = 2 if nmax == 1 else 8
    v = min(outer, cap - outer) if Z <= 20 else None                          # s-p valence: light atoms
    if "valence" in MUT and Z == 8:
        v = 3
    return dict(Z=Z, electrons=e, valence=v)


# ------------------------------------------------------------------ D2
def bond_graphs(Zs):
    """every connected simple bond graph (bond orders 1-3 between heavy atoms, single bonds to H) whose degrees are the
    valences of D1, kept once by ENCODE's canonical code"""
    EL = indexes()["EL"]
    val = {Z: label(Z)["valence"] for Z in set(Zs)}
    heavy = [i for i, Z in enumerate(Zs) if Z != 1]
    hyd = [i for i, Z in enumerate(Zs) if Z == 1]
    pairs = list(itertools.combinations(heavy, 2))
    seen = set()
    for orders in itertools.product(range(4), repeat=len(pairs)):
        deg = {i: 0 for i in heavy}
        edges = []
        for (a, b), k in zip(pairs, orders):
            if k:
                deg[a] += k; deg[b] += k; edges.append((a, b))
        free = {i: val[Zs[i]] - deg[i] for i in heavy}
        if any(v < 0 for v in free.values()) or sum(free.values()) != len(hyd):
            continue
        # connected heavy skeleton
        comp, stack = {heavy[0]}, [heavy[0]]
        while stack:
            x = stack.pop()
            for a, b in edges:
                for u, w in ((a, b), (b, a)):
                    if u == x and w not in comp:
                        comp.add(w); stack.append(w)
        if len(comp) != len(heavy):
            continue
        bonds = list(edges); hs = list(hyd)
        for i in heavy:
            for _ in range(free[i]):
                bonds.append((i, hs.pop()))
        code = EL.encode_body(list(Zs), bonds)
        seen.add(code)
    return seen


# ------------------------------------------------------------------ D3
def beta_stable(rows):
    """(Z, A) with mass below both isobaric neighbours (single-beta stable), from AME2020's mass excesses"""
    ex = {(r[0], r[2]): r[4] for r in rows}
    out = set()
    for (Z, A), d in ex.items():
        lo = ex.get((Z - 1, A)); hi = ex.get((Z + 1, A))
        if (lo is None or d < lo) and (hi is None or d < hi):
            out.add((Z, A))
    return out


def r_m(Z):
    """R_M (cm^-1) by the element's lightest beta-stable nuclide's mass, AME2020; populate's R_inf and m_e"""
    I = indexes(); P = I["P"]; rows = I["rows"]
    stab = sorted(A for (z, A) in beta_stable(rows) if z == Z)
    A = stab[0]
    dm = next(r[4] for r in rows if r[0] == Z and r[2] == A)                  # keV, atomic mass excess
    M_u = A + dm / 931494.10242
    M_nuc = M_u - Z * P.M_E_U
    return P.R_INF / (1 + P.M_E_U / M_nuc)


def k_scale(Z):
    """E_K = Z^2 R_M h c in J"""
    return Z * Z * r_m(Z) * 100 * H * C


def gaps(Z):
    lo = k_scale(Z) - k_scale(Z - 1) if Z > 1 else None
    hi = k_scale(Z + 1) - k_scale(Z)
    if "nogap" in MUT:
        hi = hi * 1e-6
        lo = lo * 1e-6 if lo else lo
    P = indexes()["P"]
    dirac = Z ** 4 * P.ALPHA_FS ** 2 / 4 * r_m(Z) * 100 * H * C           # the index's Sommerfeld-Dirac term
    dirac_hi = (Z + 1) ** 4 * P.ALPHA_FS ** 2 / 4 * r_m(Z + 1) * 100 * H * C
    return dict(lo=lo, hi=hi, min=min(x for x in (lo, hi) if x), dirac_shift=abs(dirac_hi - dirac) / hi)


# ------------------------------------------------------------------ D4-D5
def p_atom(Z, t, T=300.0):
    g = gaps(Z)
    p = sum(Q(D * t / HBAR) for D in (g["lo"], g["hi"]) if D)
    p += sum(math.exp(-min(D / (KB * T), 700)) for D in (g["lo"], g["hi"]) if D)
    return p


def rho(n, eps=1e-2):
    return Qinv(eps / 2) if "per_object" in MUT else Qinv(eps / (2 * n))


def window(Z, n, eps=1e-2):
    return rho(n, eps) * HBAR / gaps(Z)["min"]


def body(comp, n, eps=1e-2):
    """comp: {Z: fraction}; the read of n atoms: rho, the window per species, the time in sequence"""
    r = rho(n, eps)
    t = {Z: r * HBAR / gaps(Z)["min"] for Z in comp}
    T = n * sum(f * t[Z] for Z, f in comp.items())
    # check: at that window every atom's error is at most eps/n
    worst = max(p_atom(Z, t[Z]) for Z in comp)
    return dict(n=n, rho=r, t=t, T=T, worst=worst, target=eps / n, q=math.log(n / eps))


# ------------------------------------------------------------------ D7
def isobars(Zs):
    rows = indexes()["rows"]
    st = beta_stable(rows)
    ex = {(r[0], r[2]): r[4] for r in rows}
    out = []
    for Z in Zs:
        for (z, A) in st:
            if z != Z:
                continue
            for (z2, A2) in st:
                if A2 == A and z2 != Z:
                    out.append((A, Z, z2, abs(ex[(Z, A)] - ex[(z2, A)]) / (A * 931494.10242)))
    return sorted(set(out), key=lambda x: x[3])


def compute():
    o = dict(words=words())
    o["labels"] = {Z: label(Z) for Z in (1, 6, 8, 24, 25, 26, 28, 29)}
    o["water_graphs"] = len(bond_graphs([8, 1, 1]))
    o["ethanol_graphs"] = len(bond_graphs([6, 6, 8, 1, 1, 1, 1, 1, 1]))
    o["gaps"] = {Z: gaps(Z) for Z in (1, 6, 8, 24, 25, 26, 28, 29)}
    o["water"] = body({8: 1 / 3, 1: 2 / 3}, 3)
    o["ethanol"] = body({6: 2 / 9, 8: 1 / 9, 1: 6 / 9}, 9)
    o["steel"] = body({26: 0.99, 6: 0.01}, NA)
    o["stainless"] = body({26: 0.72, 24: 0.18, 28: 0.08, 25: 0.02}, NA)
    EL = indexes()["EL"]
    n_cu = EL.CU_M / EL.CU_MOLAR * EL.NA
    o["copper"] = body({29: 1.0}, n_cu)
    o["ethanol_struct"] = 2 * rho(1, 1e-2)
    o["scale"] = [(n, rho(n)) for n in (3, 9, 1e3, 1e6, 1e12, NA, 1e27, 1e40)]
    o["ratio_1e2"] = rho(1, 1e-2 / 2 * 2)                                     # one atom at error 1e-2
    o["isobars"] = isobars([24, 25, 26, 28])
    o["mn_fe"] = gaps(25)["hi"] / k_scale(25)
    return o


def checks(o):
    labs = o["labels"]
    d1 = all(v["electrons"] == Z for Z, v in labs.items()) and (labs[1]["valence"], labs[6]["valence"], labs[8]["valence"]) == (1, 4, 2)
    d2 = o["water_graphs"] == 1 and o["ethanol_graphs"] == 2
    G = o["gaps"]
    d3 = (all(abs(G[Z]["hi"] / ((2 * Z + 1) * r_m(Z) * 100 * H * C) - 1) < 1e-3 for Z in G)
          and 38 < G[1]["min"] / EV < 44 and 700 < G[29]["min"] / EV < 800 and max(g["dirac_shift"] for g in G.values()) < 0.03)
    d4 = all(r["worst"] <= r["target"] * 1.0000001 for r in (o["water"], o["ethanol"], o["steel"], o["stainless"], o["copper"]))
    sc = dict(o["scale"])
    d5 = (all(abs(r / math.sqrt(2 * math.log(2 * n / 1e-2)) - 1) < 0.15 for n, r in o["scale"] if n >= 1e6)
          and sc[1e40] < 2 * sc[1e12])
    cu = o["copper"]
    d6 = (abs(cu["target"] - 1.18e-25) < 0.01e-25 and 10.3 < cu["rho"] < 10.5 and 2.5 < o["ratio_1e2"] < 2.7
          and 1e5 < o["steel"]["T"] < 1e7)
    d7 = o["isobars"] and o["isobars"][0][3] < 2e-5 and o["mn_fe"] > 0.03
    return dict(D0=o["words"], D1=d1, D2=d2, D3=d3, D4=d4, D5=d5, D6=d6, D7=d7)


def report(o=None):
    o = o or compute(); ck = checks(o)
    print("D0 M's words: %s" % o["words"])
    print("D1 labels: %s" % ", ".join("Z %d: %d electrons, valence %s" % (Z, v["electrons"], v["valence"])
                                      for Z, v in o["labels"].items()))
    print("D2 bond graphs the valences admit: water %d, C2H6O %d" % (o["water_graphs"], o["ethanol_graphs"]))
    for Z, g in o["gaps"].items():
        print("D3 Z %2d: R_M %.4f cm^-1; gap to Z-1 %s, to Z+1 %.1f eV; the Dirac term moves it %.2g" % (
            Z, r_m(Z), ("%.1f eV" % (g["lo"] / EV)) if g["lo"] else "none (a vacancy)", g["hi"] / EV, g["dirac_shift"]))
    for nm in ("water", "ethanol", "steel", "stainless", "copper"):
        r = o[nm]
        print("D6 %-9s n %.3g: rho %.2f; window %s; in sequence %.2g s; worst atom's error %.2g against %.2g; presence "
              "%.1f quanta a site" % (nm, r["n"], r["rho"], ", ".join("Z%d %.2g s" % (Z, t) for Z, t in r["t"].items()),
                                       r["T"], r["worst"], r["target"], r["q"]))
    print("D5 rho(n): %s" % ", ".join("%.3g: %.2f" % (n, r) for n, r in o["scale"]))
    print("   ethanol's structure bit: d/sigma_x >= %.2f; one atom at error 1e-2: rho %.2f" % (o["ethanol_struct"],
                                                                                           o["ratio_1e2"]))
    print("D7 beta-stable isobars across elements (AME2020): %s; Mn to Fe by K-shell %.3f" % (
        ", ".join("A=%d Z%d/Z%d %.2g" % x for x in o["isobars"][:4]), o["mn_fe"]))
    for kk, vv in ck.items():
        print("%s %s" % (kk, vv))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["nogap", "valence", "per_object"]
    for m_ in names:
        MUT.clear(); MUT.add(m_)
        try:
            r_ = selftest(quiet=True)
        except Exception:
            r_ = False
        caught += not r_; print("mutant %-8s %s" % (m_, "caught" if not r_ else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
