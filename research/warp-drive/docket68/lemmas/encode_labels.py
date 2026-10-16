#!/usr/bin/env python3
"""encode_labels.py -- item 439: ENCODE settled -- a geometric object into binary information, in one fixed exact
encoding that reads the same at every point of the 26-lattice.

M, 439: ENCODE "need[s] to be addressed, proved, and settled".  M's rulings it stands on: 131 (the README "in its most
simplistically exact  binary code form"); 136 (5) (one fixed exact encoding); 146 ("no tolerance at all"; written in what
every universe shares); 147 (no motion; labels and values); 148 and 437 (position 2's matter rearranges to the README,
then its laws, its 26, govern: M-RECON-ALWAYS); 438 (M-GEOMETRY-AS-LABELS, M-ISOTOPE-OUT, M-LAST-STATE, M-POTENTIAL-IN);
399 (the read is part of SOURCE, M-SOURCE-READ).  Labels: computed (exact unless marked), deduced, READ, estimate,
standard (not READ here), M's.  Worked in the conversation; not verified; not seated.

  C0 (read) M's words, verbatim in the rulings file (131, 146, 147, 437, 438, 439).
  C1 (computed) The integers.  Every label is a non-negative integer written in Elias's gamma code, self-delimiting, so
     a README is one bit string with no separators; decoding is exact (checked for 0..4095).
  C2 (computed) A body of atoms: its last state's labels are each atom's element Z and which atom bonds to which -- a
     labelled graph (M-GEOMETRY-AS-LABELS; no isotope, M-ISOTOPE-OUT; no motion, 147).  The code is canonical: the
     least code over every ordering an individualization-refinement search admits, so it does not depend on the order
     the atoms are listed (checked under random relabellings), and decoding returns the same graph exactly (checked).
     It separates structures with the same formula -- ethanol and dimethyl ether, C2H6O, read differently.
  C3 (computed; standard values, not READ) A crystal: its Bravais lattice (one of 14), its basis (Z and the site as
     integer fractions), its size as whole numbers of cells, and its defects as (cell, site, new Z or a vacancy).  One
     cubic centimetre of copper, a perfect fcc block of 27,662,517 cells a side (a = 3.615 A), is 174 bits; its energy at
     the small end 2.0 J (ledger.e_small).  Its spacing is not in it: the count of cells is.
  C4 (computed; estimate where marked) A real piece.  At 99.99 % purity the block holds 8.49e18 foreign atoms, each a
     defect label of about 151 bits: N ~ 1.3e21 bits (estimate), E5 ~ 7.7e12 J, 1 % of the copper's own m c^2 and far
     under its crossover N* = 1.37e24 (encode_read E4) -- the object can pay for its own README.
  C5 (computed; deduced) Invariance across the 26-lattice.  The README holds integers only (checked: no real number
     enters).  Moving the electron's mass coordinate halves every atomic length in Planck units (encode_read E1); the
     README is unchanged, and the copy built under position 2's 26 is the same count of cells of position 2's own
     spacing (437, M-RECON-ALWAYS).  So the encoding reads the same at every point of the lattice (146), and what
     differs is the copy's size, which is position 2's.
  C6 (deduced) What the three remaining words of the rulings ask.  (a) "Most simplistically exact" (131): N is the
     length in the one fixed encoding (136 (5)); a shortest code over all encodings is uncomputable (Kolmogorov
     complexity, standard), so 131's N is this encoding's -- C3's 174 bits, against the record's estimate of about 300.
     (b) "The last state" (M-LAST-STATE): the labels at one instant, the read's, no history and no motion.
     (c) "Potential to be other states is carried" (M-POTENTIAL-IN), read so: a label carries every state its laws
     allow it -- Z carries each isotope of the element and each excitation of its electrons -- and which one the copy
     takes is position 2's (437); it costs no bit.  The board's reading of (c), put to M at 438, restated.
  C7 (deduced; READ) The read itself.  The encoding needs, from the object, each atom's Z and its place in the structure
     to within half a spacing -- discrete labels, measurable exactly in principle, and no-cloning does not bind a
     classical README (FAITHFUL 7).  The device that reads them is SOURCE's (399, M-SOURCE-READ; deferred,
     M-SOURCE-LAST).
     The nearest demonstration at source: atomic electron tomography located and classified 23,804 atoms of an FePt
     nanoparticle -- "3D coordinates (+-22 pm precision) and chemical species (99% accuracy)" (Zhou, Yang, Ercius and
     Miao's review, READ) -- the place within half a spacing already, the species not yet without error, at 1e4 atoms
     against a body's 1e23.  Requirement 14 (exact, read errors dissolved) stays SOURCE's.
  So ENCODE, as a row of the theorem -- how a geometric object becomes binary information, one fixed exact encoding
  reading the same at every point of the lattice -- is DERIVED from M's rulings and computed results; the device that
  performs the read is SOURCE's, as M placed it at 399.

python3 encode_labels.py [--selftest | --mutants]
"""
import importlib.util, math, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((131, "in its most simplistically exact binary code form"), (146, "1 - no tolerance at all"),
         (147, "is the copy's motion part of the README? - No"),
         (437, "Any information is reconstructed to obey the 26 of any position 2"),
         (438, "The README only contains the last state of the object at position 1"),
         (438, "potential to be other states is carried as part of the README"),
         (439, "that need to be addressed, proved, and settled"))
BRAVAIS = ("aP", "mP", "mS", "oP", "oS", "oI", "oF", "tP", "tI", "hR", "hP", "cP", "cI", "cF")
CU_A, CU_SIDE, CU_M, CU_MOLAR, NA = 3.615e-10, 1e-2, 8.96e-3, 63.546e-3, 6.02214076e23   # standard, not READ
C_LIGHT = 299792458.0


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


# ------------------------------------------------------------------ C1 the integers
def gamma(n):
    """Elias gamma of n >= 0 (codes n + 1)"""
    if "float_coord" in MUT and not isinstance(n, int):
        return format(int(n * 1000) + 1, "b")                       # the mutant lets a real number in
    assert isinstance(n, int) and n >= 0, n
    b = format(n + 1, "b")
    return "0" * (len(b) - 1) + b


def ungamma(bits, i):
    z = 0
    while bits[i + z] == "0":
        z += 1
    v = int(bits[i + z:i + 2 * z + 1], 2)
    return v - 1, i + 2 * z + 1


# ------------------------------------------------------------------ C2 a body of atoms
def _refine(Z, adj, colours):
    n = len(Z)
    while True:
        sig = [(colours[v], tuple(sorted(colours[u] for u in adj[v]))) for v in range(n)]
        ranks = {s: k for k, s in enumerate(sorted(set(sig)))}
        new = [ranks[sig[v]] for v in range(n)]
        if len(set(new)) == len(set(colours)):
            return new
        colours = new


def _leaves(Z, adj, colours):
    colours = _refine(Z, adj, colours)
    n = len(Z)
    if len(set(colours)) == n:
        yield colours
        return
    cells = {}
    for v in range(n):
        cells.setdefault(colours[v], []).append(v)
    target = min((c for c in cells if len(cells[c]) > 1), key=lambda c: (len(cells[c]), c))
    for v in cells[target]:
        indiv = [2 * c + (0 if (u == v) else 1) if c == target else 2 * c + 1 for u, c in enumerate(colours)]
        yield from _leaves(Z, adj, indiv)


def _code_for(Z, adj, order):
    pos = {v: k for k, v in enumerate(order)}
    n = len(Z)
    bits = "0" + gamma(n) + "".join(gamma(0 if "drop_z" in MUT else Z[v]) for v in order)
    tri = ["1" if order[j] in adj[order[i]] else "0" for i in range(n) for j in range(i + 1, n)]
    return bits + "".join(tri)


def encode_body(Z, bonds):
    n = len(Z)
    adj = [set() for _ in range(n)]
    for a, b in bonds:
        adj[a].add(b); adj[b].add(a)
    if "no_canon" in MUT:
        return _code_for(Z, adj, list(range(n)))
    best = None
    for leaf in _leaves(Z, adj, list(Z)):
        order = sorted(range(n), key=lambda v: leaf[v])
        c = _code_for(Z, adj, order)
        if best is None or c < best:
            best = c
    return best


def decode_body(bits):
    assert bits[0] == "0"
    n, i = ungamma(bits, 1)
    Z = []
    for _ in range(n):
        z, i = ungamma(bits, i)
        Z.append(z)
    bonds = []
    for a in range(n):
        for b in range(a + 1, n):
            if bits[i] == "1":
                bonds.append((a, b))
            i += 1
    return Z, bonds


MOLECULES = {
    "water": ([8, 1, 1], [(0, 1), (0, 2)]),
    "methane": ([6, 1, 1, 1, 1], [(0, 1), (0, 2), (0, 3), (0, 4)]),
    "ethanol": ([6, 6, 8, 1, 1, 1, 1, 1, 1], [(0, 1), (1, 2), (0, 3), (0, 4), (0, 5), (1, 6), (1, 7), (2, 8)]),
    "dimethyl ether": ([6, 8, 6, 1, 1, 1, 1, 1, 1], [(0, 1), (1, 2), (0, 3), (0, 4), (0, 5), (2, 6), (2, 7), (2, 8)]),
    "benzene": ([6] * 6 + [1] * 6, [(k, (k + 1) % 6) for k in range(6)] + [(k, k + 6) for k in range(6)]),
    "hydrogen sulphide": ([16, 1, 1], [(0, 1), (0, 2)]),
}


def relabel(Z, bonds, rng):
    n = len(Z)
    p = list(range(n)); rng.shuffle(p)
    Zp = [0] * n
    for v in range(n):
        Zp[p[v]] = Z[v]
    return Zp, [(p[a], p[b]) for a, b in bonds]


# ------------------------------------------------------------------ C3 a crystal
def encode_crystal(bravais, q, basis, counts, defects):
    """bravais: label; q: common denominator; basis: [(Z, (p1, p2, p3))]; counts: (n1, n2, n3); defects:
    [(i, j, k, site, Z_new)] with Z_new = 0 a vacancy"""
    bits = "1" + gamma(BRAVAIS.index(bravais)) + gamma(q) + gamma(len(basis))
    for Z, ps in basis:
        bits += gamma(Z) + "".join(gamma(p) for p in ps)
    bits += "".join(gamma(c) for c in counts) + gamma(len(defects))
    for d in sorted(defects):
        bits += "".join(gamma(x) for x in d)
    if "iso_in" in MUT:
        bits += gamma(34)                                           # the mutant writes a neutron number
    return bits


def decode_crystal(bits):
    assert bits[0] == "1"
    b, i = ungamma(bits, 1)
    q, i = ungamma(bits, i)
    nb, i = ungamma(bits, i)
    basis = []
    for _ in range(nb):
        Z, i = ungamma(bits, i)
        ps = []
        for _ in range(3):
            p, i = ungamma(bits, i); ps.append(p)
        basis.append((Z, tuple(ps)))
    counts = []
    for _ in range(3):
        c, i = ungamma(bits, i); counts.append(c)
    nd, i = ungamma(bits, i)
    defects = []
    for _ in range(nd):
        d = []
        for _ in range(5):
            x, i = ungamma(bits, i); d.append(x)
        defects.append(tuple(d))
    return BRAVAIS[b], q, basis, tuple(counts), defects, i == len(bits)


def copper_block(a=CU_A, defects=()):
    n = round(CU_SIDE / a)
    return n, encode_crystal("cF", 1, [(29, (0, 0, 0))], (n, n, n), list(defects))


def e_small(N):
    spec = importlib.util.spec_from_file_location("el_ledger", os.path.join(HERE, "ledger.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.e_small(N, 1.0)[0]


def real_piece():
    """C4 (estimate): 99.99 % copper -- foreign atoms as defect labels of the block"""
    n, _ = copper_block()
    atoms = CU_M / CU_MOLAR * NA
    d = 1e-4 * atoms
    per = 3 * len(gamma(n // 2)) + len(gamma(0)) + len(gamma(30))
    N = d * per
    return d, per, N, e_small(N), CU_M * C_LIGHT ** 2


def report():
    print("C0 M's words:", words())
    for name, (Z, b) in MOLECULES.items():
        c = encode_body(Z, b)
        print("C2 %-18s %3d bits  %s" % (name, len(c), c))
    n, c = copper_block()
    print("C3 1 cm^3 copper, fcc, %d cells a side: %d bits; E5 = %.3g J" % (n, len(c), e_small(len(c))))
    d, per, N, E, mc2 = real_piece()
    print("C4 99.99 %% copper: %.3g defects x %d bits = %.3g bits; E5 = %.3g J = %.3g of m c^2" % (d, per, N, E,
                                                                                                 E / mc2))
    n2, c2 = copper_block(a=CU_A / 2)
    print("C5 the same block read where atomic lengths are halved in Planck units: the README is the count, %d cells; "
          "the copy at position 2 is %d of its own cells (437)" % (n, n))


def selftest(quiet=False):
    ok = []

    def say(s):
        if not quiet:
            print(s, flush=True)
    w = words(); ok.append(w); say("C0 M's words verbatim inside their items: %s" % w)
    c1 = all(ungamma(gamma(k), 0) == (k, len(gamma(k))) for k in range(4096))
    ok.append(c1); say("C1 gamma code exact on 0..4095: %s" % c1)
    rng = random.Random(439)
    canon = all(encode_body(*relabel(Z, b, rng)) == encode_body(Z, b) for Z, b in MOLECULES.values() for _ in range(6))
    trip = all(encode_body(*decode_body(encode_body(Z, b))) == encode_body(Z, b) for Z, b in MOLECULES.values())
    codes = [encode_body(Z, b) for Z, b in MOLECULES.values()]
    distinct = len(set(codes)) == len(codes)
    c2 = canon and trip and distinct
    ok.append(c2); say("C2 canonical under relabelling, exact round trip, ethanol, dimethyl ether, water and H2S all "
                       "distinct: %s" % c2)
    n, c = copper_block()
    dec = decode_crystal(c)
    c3 = (n == 27662517 and len(c) == 174 and dec[0] == "cF" and dec[3] == (n, n, n) and dec[5]
          and dec[2] == [(29, (0, 0, 0))] and abs(e_small(len(c)) - 2.04) < 0.01)
    ok.append(c3); say("C3 1 cm^3 copper: %d cells a side, %d bits, decoded exactly: %s" % (n, len(c), c3))
    d, per, N, E, mc2 = real_piece()
    c4 = 1.2e21 < N < 1.6e21 and 0.005 < E / mc2 < 0.02 and N < 1.37e24
    ok.append(c4); say("C4 99.99 %% copper: N = %.2g bits, E5 = %.2g of m c^2, under N*: %s" % (N, E / mc2, c4))
    ints = all(ch in "01" for ch in c)
    # C5: one real coordinate must not survive the encoder
    try:
        encode_crystal("cF", 1, [(29, (0, 0, 0.5))], (2, 2, 2), [])
        reals_refused = "float_coord" not in MUT and False
    except AssertionError:
        reals_refused = True
    c5 = ints and reals_refused
    ok.append(c5); say("C5 the README holds integers only; a real coordinate is refused by the encoder: %s" % c5)
    return all(ok)


def mutants():
    names = ["no_canon", "float_coord", "drop_z", "iso_in"]
    caught = 0
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-12s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
