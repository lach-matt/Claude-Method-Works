#!/usr/bin/env python3
"""source_spec.py -- item 485 (M's item 1): SOURCEs and SOURCE, so the completed theorem names what each must supply,
and the read (399).  Labels: computed (exact unless marked), deduced, READ (at source, 2026-10-17), estimate, M's.
Worked in the conversation; not verified; not seated.

Held against the exclusions first (481, 484): the delivery below forms an uncharged hole whose lapse has one root --
no inner horizon, no Cauchy horizon -- and no bounce enters SOURCE.

  U0 (read) M's words, verbatim in the rulings file: 485, "do 3 first, then 1"; 344-345 (M-SOURCE-LAST: the completed
     theorem tells SOURCE what is required); 386, "matter cannot travel, only information can travel"; 399, "Converting
     a geometric object into an information README"; 432 (1), "Information is energy in the form of a binary
     interaction"; 438, "What does the math require?".
  U1 (computed by their owners) The rows that say what SOURCE must supply pass their own checks: settle_arrival A0-A7
     (the delivery), encode_labels C0-C7 (the encoding), encode_read E0-E6 (the read and the write by size),
     source_capacity S1-S7 (the carrier's room).
  U2 (computed, exact) The delivery exists in general relativity.  On 5D Vaidya the in-going null vector k = -dv has
     g^vv = 0, so the shell is null dust with T trace zero (no rest mass, 386); G_vv = 3 mu'/(2 r^3) >= 0 (no partner);
     the lapse 1 - mu/r^2 has one positive root (no inner horizon, no Cauchy horizon); the step mu = r_h^2 theta(v)
     carries the ADM energy 3 pi c^4 r_h^2/(8 G5), the record's E5(N) at the example README to 1e-12.  The large end is
     settle_arrival A4's warped Vaidya, reading on the plane as the 4D step.
  U3 (READ; computed) Its carrier is the bulk's own radiation.  "all high-frequency limits are isometric to solutions
     to the Einstein-null dust system; and conversely, all solutions to the Einstein-null dust system also arise locally
     as high-frequency limits of vacuum spacetimes" (Huneau and Luk, arXiv 2009.08968, READ; 3+1, carried to 5D as the
     board's reading; Isaacson 1968, Burnett 1989): the shell can be gravitational waves of the bulk alone, energy and
     no matter (386).  The window is wide: r_h = 7.3e4 l5 at the example README, so waves of 10 l5 are 1.0e10 quanta,
     each below the 5D Planck energy; at the large end r0/l5 is 1.8e21 (r0 = 20 ell) to 5.8e22 (the Earth cap).
  U4 (computed) What a delivery all at once can carry.  The most states massless radiation holds at energy E in volume V
     is e^S, S = (5/4)(a5 V)^(1/5) E^(4/5) in five dimensions (a5 = Z 2 pi^2 Gamma(5) zeta(5)/(2 pi hbar c)^4); what crosses
     the face within w lay in V = A c w (Liouville: an isotropic gas there is the most), A = 2 pi^2 r_h^3 at the small
     end, and at the large end the black string's area with Tolman's weighting to its cap, V = 4 pi r0^2 c w (r0 - ell)
     (computed).  So S/(N ln2) grows only as w^(1/5) and falls as (r_h/l5)^(-3/5): at one face clock it is 7.6e-4 at
     the small end (Z = 8, the bulk graviton and U(1); 7.0e-4 with the graviton alone), 1.4e-13 at r0 = 20 ell and
     3.7e-14 at the Earth cap; at w -> 0 it is zero.  The README's N bits fit only over w_min = 3.9e15 face clocks
     (small end) -- the record's own 4D figure, 1.0e14 at Z = 106.75 (source_capacity S2), as Z^(-1) makes it.
  U5 (computed) What closes that gap, each way computed.  (a) A delivery of width w_min: its face (r^2 = mu(v)) is at
     1.6e-8 of r_h one face clock after the onset, and full size only at w_min -- 162 and settle_arrival A1 refuse it.
     (b) More species: Z = 8 (N ln2/S)^5 = 3.1e16 at one clock (small end), 1.2e68 at the Earth cap.  (c) The README's bits
     not carried as the delivery's states: M's 432 (1), "a binary interaction", and 136 (7), synchronization.  General
     relativity and quantum mechanics bound the delivery's information by U4; (c) is the one that holds with 162, and
     it is M's, not established physics -- the second premise of the theorem beyond established physics, named.
  U6 (READ) The read's devices at source.  Atom probe tomography: "the detection efficiency is from 37% upto 80%"; atoms
     not detected are removed unread (S1C-O1).  The quantum gas microscope: "a very conservative lower limit of the
     fidelity of 98% in identifying atoms at a given lattice site" (Bakr et al. 2009) -- atoms first placed in an
     optical lattice, not an object's.  Atomic electron tomography: "6,569 iron atoms and 16,627 platinum atoms, with
     each atom's coordinates precisely plotted" (Berkeley Lab, 2017), species to 99 % (encode_labels C7).  State
     tomography needs many copies; one object is one.
  U7 (computed; estimate where marked) What the read must do, per object.  It reads every atom (the labels are of the
     last state, and a crystal's 174 bits assert that no atom differs), each with error below eps/n: 1e-25 for 1 cm^3 of
     copper (8.49e22 atoms, eps = 1e-2), against the demonstrated 1e-2 -- 23 orders.  N, E5(N) and whether the object
     pays its own README (encode_read E4) for a molecule, the copper block and a real piece.
  U8 (deduced) The two rows as the completed theorem names them: what each must supply, item by item, with each item's
     standing (computed / READ / M's / open).  Computed: the delivery, its carrier, the read's encoding, the energy.
     Open and allowed: the emitter in the bulk (A3: not our plane's matter), the exact read of a body.  M's, beyond
     established physics: the README's bits on a delivery all at once (U5 (c)).

python3 source_spec.py [--selftest | --mutants]
"""
import os, sys, math, io, re, contextlib, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((485, "do 3 first, then 1"), (386, "How can it be a gas if matter cannot travel, only information can travel?"),
         (399, "Converting a geometric object into an information README"),
         (432, "Information is energy in the form of a binary interaction"), (438, "What does the math require?"))


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


def owners():
    out = {}
    for f in ("settle_arrival.py", "encode_labels.py", "encode_read.py", "source_capacity.py"):
        mod = _load(f, "ss_" + f[:-3])
        with contextlib.redirect_stdout(io.StringIO()):
            out[f] = bool(mod.selftest(quiet=True))
    return out


def consts():
    PG = _load("p2_gravity.py", "ss_pg")
    G5 = PG.G * PG.ELL_MAX
    return dict(c=PG.C, G=PG.G, hbar=PG.HBAR, ell=PG.ELL_MAX, G5=G5, l5=(PG.HBAR * G5 / PG.C ** 3) ** (1 / 3),
                lP=(PG.HBAR * PG.G / PG.C ** 3) ** 0.5, ln2=math.log(2))


# ------------------------------------------------------------------ U2 the delivery in general relativity
def vaidya():
    v, r, c, th, ph = sp.symbols("v r chi theta phi", real=True)
    mu = sp.Function("mu")(v)
    X = (v, r, c, th, ph)
    f = 1 - mu / r ** 2
    g = sp.zeros(5, 5)
    g[0, 0] = -f; g[0, 1] = g[1, 0] = 1
    g[2, 2] = r ** 2; g[3, 3] = r ** 2 * sp.sin(c) ** 2; g[4, 4] = r ** 2 * sp.sin(c) ** 2 * sp.sin(th) ** 2
    gi = sp.simplify(g.inv())
    k = sp.Matrix([-1, 0, 0, 0, 0])                                  # k_a = -d_a v, in-going
    msq = sp.Symbol("m2") if "massive" in MUT else 0
    norm = sp.simplify((k.T * gi * k)[0] + msq)                      # g^ab k_a k_b
    # Einstein tensor
    Gm = [[[sum(gi[a, d] * (sp.diff(g[d, b], X[cc]) + sp.diff(g[d, cc], X[b]) - sp.diff(g[b, cc], X[d])) for d in range(5)) / 2
            for cc in range(5)] for b in range(5)] for a in range(5)]
    def ric(b, d):
        return sp.simplify(sum(sp.diff(Gm[a][b][d], X[a]) - sp.diff(Gm[a][b][a], X[d])
                               + sum(Gm[a][a][e] * Gm[e][b][d] - Gm[a][d][e] * Gm[e][b][a] for e in range(5))
                               for a in range(5)))
    R = sp.Matrix(5, 5, lambda i, j: ric(i, j))
    Rs = sp.simplify(sum(gi[i, j] * R[i, j] for i in range(5) for j in range(5)))
    Gt = sp.simplify(R - Rs * g / 2)
    only_vv = all(sp.simplify(Gt[i, j]) == 0 for i in range(5) for j in range(5) if (i, j) != (0, 0))
    Gvv = sp.simplify(Gt[0, 0])
    roots = sp.solve(sp.Eq(1 - sp.Symbol("mu0", positive=True) / r ** 2, 0), r)
    pos_roots = [x for x in roots if x.is_positive]
    return dict(null=norm == 0, Gvv=Gvv, Gvv_ok=sp.simplify(Gvv - 3 * sp.diff(mu, v) / (2 * r ** 3)) == 0,
                only_vv=only_vv, one_root=len(pos_roots) == 1)


def energy_check(k):
    L = _load("ledger.py", "ss_ledger")
    E, rh, _ = L.e_small(L.EXAMPLE_N, 1.0)
    E_adm = 3 * math.pi * k["c"] ** 4 * rh ** 2 / (8 * k["G5"])
    return dict(N=L.EXAMPLE_N, E=E, rh=rh, rel=abs(E_adm / E - 1))


# ------------------------------------------------------------------ U3 the carrier's window
def window(k, d):
    rh = d["rh"]; l5 = k["l5"]
    lam = 10 * l5
    n_quanta = d["E"] * lam / (2 * math.pi * k["hbar"] * k["c"])
    per_quantum = 2 * math.pi * k["hbar"] * k["c"] / lam
    E5P = k["hbar"] * k["c"] / l5                                  # the 5D Planck energy, hbar c / l5
    EC = _load("earth_cap.py", "ss_ec").compute()
    big = {"r0 = 20 ell": 20 * k["ell"], "the Earth cap": EC["r0"]}
    return dict(rh_l5=rh / l5, n_quanta=n_quanta, below_planck=per_quantum < E5P,
                large={nm: r0 / l5 for nm, r0 in big.items()}, big=big, EC=EC)


# ------------------------------------------------------------------ U4 the room of a delivery all at once
def a5(Z, k):
    return Z * 2 * math.pi ** 2 * math.gamma(5) * 1.0369277551433699 / (2 * math.pi * k["hbar"] * k["c"]) ** 4


def s5(E, V, Z, k):
    s = 1.25 * (a5(Z, k) * V) ** 0.2 * E ** 0.8
    return s * (1e6 if "room" in MUT else 1.0)


def tolman():
    """the large end's warped volume: T = T0 e^(y/ell), dV = 4 pi r0^2 c w e^(-3y/ell) dy, Killing energy u e^(-y/ell);
    E and S share one factor, so S = (5/4)(a5 V_eff)^(1/5) E^(4/5) with V_eff = 4 pi r0^2 c w ell (e^(Y/ell) - 1)"""
    y, Y, ell, T0, A, w, a = sp.symbols("y Y ell T0 A w a", positive=True)
    dV = A * w * sp.exp(-3 * y / ell)
    E = sp.integrate(a * (T0 * sp.exp(y / ell)) ** 5 * sp.exp(-y / ell) * dV, (y, 0, Y))
    S = sp.integrate(sp.Rational(5, 4) * a * (T0 * sp.exp(y / ell)) ** 4 * dV, (y, 0, Y))
    Veff = A * w * ell * (sp.exp(Y / ell) - 1)
    return sp.simplify(S - sp.Rational(5, 4) * (a * Veff) ** sp.Rational(1, 5) * E ** sp.Rational(4, 5)) == 0


def room(k, d, W):
    out = {}
    c, l5 = k["c"], k["l5"]
    rh, E, N = d["rh"], d["E"], d["N"]
    A = 2 * math.pi ** 2 * rh ** 3
    for Z in (5, 8):
        clock = rh / c
        S1 = s5(E, A * c * clock, Z, k)
        wmin = (N * k["ln2"] / (1.25 * E ** 0.8)) ** 5 / (a5(Z, k) * A * c) / clock
        out[("small", Z)] = dict(ratio=S1 / (N * k["ln2"]), wmin=wmin,
                                 tiny=s5(E, A * c * clock * 1e-10, Z, k) / S1)
    for nm, r0 in W["big"].items():
        Nl = math.pi * r0 ** 2 / k["lP"] ** 2 / k["ln2"]
        El = r0 * c ** 4 / (2 * k["G"])
        clock = r0 / c
        V = 4 * math.pi * r0 ** 2 * c * clock * (r0 - k["ell"])
        S1 = s5(El, V, 8, k)
        out[(nm, 8)] = dict(ratio=S1 / (Nl * k["ln2"]), N=Nl, E=El)
    SC = _load("source_capacity.py", "ss_sc")
    with contextlib.redirect_stdout(io.StringIO()):
        cs = SC.cases()
    out["record_4d_small"] = cs["small end"]["tau"][106.75]
    return out


def gap(R, d):
    """U5: (a) a delivery of width w_min, its face one clock after the onset; (b) the species it would need"""
    wmin = R[("small", 8)]["wmin"]
    rAH_one = math.sqrt(1 / wmin)                                   # r^2 = mu(v) = r_h^2 v/w_min on a linear ramp
    if "thick" in MUT:
        rAH_one = 1.0
    Z_need_small = 8 * (1 / R[("small", 8)]["ratio"]) ** 5
    Z_need_cap = 8 * (1 / R[("the Earth cap", 8)]["ratio"]) ** 5
    return dict(rAH_one=rAH_one, Z_small=Z_need_small, Z_cap=Z_need_cap)


# ------------------------------------------------------------------ U6-U7 the read
READ_DEVICES = {  # READ at source, 2026-10-17
    "atom probe tomography": dict(detected=(0.37, 0.80), what="detection efficiency; undetected atoms removed unread",
                                  src="ScienceDirect Topics, 'Atom Probe': 'the detection efficiency is from 37% upto 80%'"),
    "quantum gas microscope": dict(fidelity=0.98, what="atoms first placed in an optical lattice",
                                   src="Bakr et al. 2009 (arXiv 0908.0174): 'a very conservative lower limit of the "
                                       "fidelity of 98%'"),
    "atomic electron tomography": dict(atoms=6569 + 16627, species_error=1e-2,
                                       src="Berkeley Lab 2017: '6,569 iron atoms and 16,627 platinum atoms'; species "
                                           "to 99 % (encode_labels C7)"),
}


def read_needs(k):
    EL = _load("encode_labels.py", "ss_el"); ER = _load("encode_read.py", "ss_er")
    eps = 1e-2
    rows = {}
    for nm in ("water", "benzene"):
        Z, b = EL.MOLECULES[nm]
        N = len(EL.encode_body(Z, b)); E, rh = ER.e_small(N)
        rows[nm] = dict(N=N, E=E, atoms=len(Z), p_need=eps / len(Z))
    n, code = EL.copper_block()
    atoms = EL.CU_M / EL.CU_MOLAR * EL.NA
    E, rh = ER.e_small(len(code))
    mc2 = EL.CU_M * k["c"] ** 2
    rows["1 cm^3 copper, perfect"] = dict(N=len(code), E=E, atoms=atoms, p_need=eps / atoms, pays=E < mc2)
    d_, per, Nr, Er, mc2r = EL.real_piece()
    rows["1 cm^3 copper, 99.99 % (estimate)"] = dict(N=Nr, E=Er, atoms=atoms, p_need=eps / atoms, pays=Er < mc2r)
    demonstrated = READ_DEVICES["atomic electron tomography"]["species_error"]
    if "read99" in MUT:
        rows["1 cm^3 copper, perfect"]["p_need"] = 1e-2
    return rows, demonstrated


# ------------------------------------------------------------------ U8 the two rows named
SPEC = {
    "SOURCEs (the small end)": [
        ("the README's labels, read from the object's last state in ENCODE's one fixed encoding: N bits", "computed",
         "encode_labels C1-C6; M-LAST-STATE, M-GEOMETRY-AS-LABELS, M-ISOTOPE-OUT (438)"),
        ("energy exactly E5(N) = 3 pi hbar c r_h^2/(8 l5^3), no rest mass, nothing besides", "computed",
         "U2; ledger.e_small; 136 (1), 386"),
        ("delivered as a round null shell in the bulk crossing the face's whole 3-sphere at once", "computed",
         "U2; settle_arrival A1, A2"),
        ("carried by the bulk's own radiation, gravitational waves in the high-frequency limit (or the bulk U(1))",
         "READ", "U3; Huneau and Luk 2009.08968; u1_bulk (446)"),
        ("emitted from the bulk, from every direction about the hole: not from our plane's matter", "open",
         "settle_arrival A3; 180"),
        ("the object's own rest energy pays when N <= N*(m), the device's input otherwise", "computed",
         "encode_read E4; U7"),
        ("the read: every atom of the object, each label without error (per-atom error below eps/n)", "open",
         "U6, U7; S1C-O1; 399, M-SOURCE-READ"),
        ("the README's N bits reach the face with a delivery all at once", "M's",
         "U4, U5: established physics bounds such a delivery to S << N bits; 432 (1), 136 (7)"),
    ],
    "SOURCE (the large end)": [
        ("the README's labels in the one fixed encoding: N bits (every laboratory object lies at the small end, "
         "N < N_L = 5.31e60)", "computed", "encode_labels; encode_read E3"),
        ("energy exactly E(N) = m c^2, 4 pi r0^2 = 4 N l_P^2 ln2, no rest mass", "computed", "U2; exactE"),
        ("delivered as the warped Vaidya shell in the bulk conforming to the large hole, e^(2y/ell)-weighted near the "
         "plane, reading on the plane as the 4D step with no matter there", "computed", "settle_arrival A4, A7"),
        ("carried by the bulk's own radiation in the high-frequency limit", "READ", "U3"),
        ("emitted from the bulk at every depth to the hole's cap: not from our plane's matter", "open",
         "settle_arrival A4, A5; 180"),
        ("the read, as at the small end", "open", "U6, U7"),
        ("the README's N bits reach the face with a delivery all at once", "M's", "U4, U5 (3.7e-14 of N at the Earth cap)"),
    ],
}


def compute():
    k = consts()
    o = dict(words=words(), owners=owners(), vaidya=vaidya(), tolman=tolman())
    d = energy_check(k); o["energy"] = d
    W = window(k, d); o["window"] = W
    R = room(k, d, W); o["room"] = R
    o["gap"] = gap(R, d)
    o["read"], o["demonstrated"] = read_needs(k)
    return o


def checks(o):
    v = o["vaidya"]; W = o["window"]; R = o["room"]; g = o["gap"]; rd = o["read"]
    u0 = o["words"]
    u1 = all(o["owners"].values())
    u2 = v["null"] and v["Gvv_ok"] and v["only_vv"] and v["one_root"] and o["energy"]["rel"] < 1e-12
    u3 = W["rh_l5"] > 1e4 and W["n_quanta"] > 1e9 and W["below_planck"] and all(x > 1e20 for x in W["large"].values())
    u4 = (o["tolman"] and all(R[("small", Z)]["ratio"] < 1e-2 for Z in (5, 8)) and R[("r0 = 20 ell", 8)]["ratio"] < 1e-10
          and R[("the Earth cap", 8)]["ratio"] < 1e-10 and abs(R[("small", 8)]["tiny"] - 1e-2) < 1e-6
          and 0.01 < R[("small", 8)]["wmin"] / R["record_4d_small"] < 100)
    u5 = g["rAH_one"] < 1e-6 and g["Z_small"] > 1e10 and g["Z_cap"] > 1e60
    cu = rd["1 cm^3 copper, perfect"]
    u7 = cu["N"] == 174 and cu["p_need"] < 1e-20 and o["demonstrated"] > 1e6 * cu["p_need"] and cu["pays"]
    labels = {lab for rows in SPEC.values() for _, lab, _ in rows}
    u8 = labels <= {"computed", "READ", "M's", "open"} and all(any(lab == "M's" for _, lab, _ in rows) for rows in SPEC.values())
    return dict(U0=u0, U1=u1, U2=u2, U3=u3, U4=u4, U5=u5, U7=u7, U8=u8)


def report(o=None):
    o = o or compute(); ck = checks(o); R = o["room"]; W = o["window"]; g = o["gap"]
    print("U0 M's words: %s" % o["words"])
    print("U1 owners: %s" % ", ".join("%s %s" % (f, r) for f, r in o["owners"].items()))
    v = o["vaidya"]
    print("U2 5D Vaidya: k null %s; G_vv = 3 mu'/(2 r^3) %s, the only component %s; one root %s; ADM energy = E5(N) at "
          "the example README (N = %d, E = %.5e J) to %.1e" % (v["null"], v["Gvv_ok"], v["only_vv"], v["one_root"],
                                                               o["energy"]["N"], o["energy"]["E"], o["energy"]["rel"]))
    print("U3 r_h/l5 %.3g; waves of 10 l5: %.3g quanta, each below the 5D Planck energy %s; large end r0/l5: %s" % (
        W["rh_l5"], W["n_quanta"], W["below_planck"], ", ".join("%.2g (%s)" % (x, nm) for nm, x in W["large"].items())))
    print("U4 Tolman's warped volume: %s.  S/(N ln2) at one face clock: small end %.2g (Z = 5), %.2g (Z = 8); r0 = 20 "
          "ell %.2g; Earth cap %.2g; at 1e-10 of a clock x %.3g; w_min %.2g face clocks (record's 4D: %.2g)" % (
              o["tolman"], R[("small", 5)]["ratio"], R[("small", 8)]["ratio"], R[("r0 = 20 ell", 8)]["ratio"],
              R[("the Earth cap", 8)]["ratio"], R[("small", 8)]["tiny"], R[("small", 8)]["wmin"], R["record_4d_small"]))
    print("U5 (a) a delivery of width w_min: its face at %.2g of r_h one clock after the onset; (b) species needed: %.2g "
          "(small end), %.2g (Earth cap); (c) M's 432 (1)" % (g["rAH_one"], g["Z_small"], g["Z_cap"]))
    for nm, dv in READ_DEVICES.items():
        print("U6 %s: %s" % (nm, dv["src"]))
    for nm, r in o["read"].items():
        print("U7 %-34s N %-10.4g E5 %.3g J  atoms %.3g  per-atom error needed < %.1e%s" % (
            nm, r["N"], r["E"], r["atoms"], r["p_need"], ("  object pays: %s" % r["pays"]) if "pays" in r else ""))
    print("   demonstrated per-atom species error %.0e (atomic electron tomography)" % o["demonstrated"])
    for row, items in SPEC.items():
        print("U8 %s" % row)
        for what, lab, src in items:
            print("   [%s] %s  (%s)" % (lab, what, src))
    for kk, vv in ck.items():
        print("%s %s" % (kk, vv))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["massive", "room", "thick", "read99"]
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
