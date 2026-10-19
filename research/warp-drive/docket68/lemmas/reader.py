#!/usr/bin/env python3
"""reader.py -- item 492: SOURCE's device that reads the object into the README, as the theorem's math requires it.

M, 492: "the device that reads the object into the README-definition of the device, how its start is initiated, what is
required of its function, and how that function is executed - as determined by what the theorem math requires".
Nothing here is designed beside the theorem.  Each requirement is read off a row or a ruling and computed from the
instrument that row rests on: encode_labels (ENCODE), read_index (the read's signal), encode_read (the bit's energy and
the write by size), ledger (E5(N)), passage_est (the write), r1_exact (R1), face2_release (the release).  Held to 386 and
491: only information travels; the object's matter does not.  Labels: computed (exact unless marked), deduced, READ,
estimate (standard values, not READ here), M's.

  A. DEFINITION
  A1 (computed: encode_labels) The device is the map R = encode o measure from the object's last state at position 1
     (438) to the README.  'measure' is one projective measurement of the object's labels: each site's Z, each site's
     occupancy, which site bonds to which, and the defects (M-GEOMETRY-AS-LABELS; no isotope, no motion: 438, 147).
     'encode' is ENCODE's canonical Elias-gamma code (encode_labels C1-C6): integers only, independent of the order the
     atoms are met, decoded exactly.  N = len(R(object)).  Water reads to 22 bits and ethanol to 79, against dimethyl
     ether's different 79.  A perfect cm^3 copper block reads to 174 bits, a 99.99 % piece to 1.3e21 (estimate).
  A2 (computed: ledger, scope C2) N is the trip's input (130: "your input to the device for each trip, read from the
     object being moved").  It fixes the corridor: r_h and E5(N) (G1, G3), and the theorem's domain N >= 7.12e9.  A
     molecule's README and a perfect crystal's lie below that domain; the real copper piece's lies inside: r_h = 8.7e-19 m,
     E5 = 7.7e12 J.  The device therefore reads to the README the corridor is built from: it is the theorem's first
     act, and its only input.
  B. HOW ITS START IS INITIATED
  B1 (computed) Before everything else.  E5 grows as N^(2/3) (dE/dN = (2/3) E/N > 0), so the opening's energy and the
     face's size are fixed only once N is.  One defect label more (151 bits) moves E5 of the real piece by 7.9e-20 of
     itself, an amount the face does not tolerate (162: it takes the size that holds the README upon opening).  The
     read completes before the opening.  The order is fixed: the user's choice of the object (130) starts the read;
     the read's completion (N) starts the opening, E5(N) all at once (source_spec U2), both faces at once (136 A, 136 (7));
     then the write; then the release whole at its end (432 (2)).
  B2 (deduced; estimate where marked) One instant.  The README holds the last state only (438), the labels at one
     instant (encode_labels C6 (b)).  So the read must finish before any label of the object changes:
     T_read < 1/Gamma, Gamma the object's rate of label changes.  In copper (vacancies hopping; standard values,
     not READ) Gamma is 464 per second per cm^3 at 300 K, so the read must finish within 2.2 ms; at 77 K Gamma is
     2.2e-94 per second -- the labels hold for longer than the universe's age.
  C. WHAT IS REQUIRED OF ITS FUNCTION
  C1 (computed, exact) Exact (R1, 146: no tolerance).  The device's record of a label must be a pointer state
     orthogonal to the record of every other value.  Helstrom's least error for two records of overlap s is
     (1 - sqrt(1 - s^2))/2, zero only at s = 0.  read_index's spectroscopic read (a finite window, a Gaussian line) errs
     at every finite window, so it cannot meet R1.  A projective read, every label's pointer states orthogonal, errs not
     at all, and quantum mechanics admits it for every label used: Z (a charge, superselected), occupancy and site (a
     partition of space into cells), bond (a pair of sites).
  C2 (computed: read_index; Mandelstam-Tamm and Margolus-Levitin, READ in encode_read E5) Fast enough.  An orthogonal
     record takes at least tau = pi hbar/(2 Delta E).  Committing the energy that separates a label from its neighbours,
     the K-shell gap D: 2.5e-17 s (H), 5.1e-18 s (O), 1.5e-18 s (Fe), 1.3e-18 s (Cu) per atom.  That is 6.7 times faster
     than read_index's conservative window at the copper's n, and exact.
  C3 (computed) Fine enough.  A site is fixed to within half a spacing only by a probe whose wavelength is at most the
     spacing (the Heisenberg microscope: dx >= lambda/(2 sin theta)).  In copper (nearest neighbours 2.556 A) that is a
     photon of 4.85 keV or more, or an electron of 23 eV or more.  Z is told by the K shell (read_index D3), so the probe
     reaches E_K, the index's K-shell scale: 11.4 keV for copper, above the 4.85 keV the spacing asks, so one hard
     X-ray probe at or above E_K meets both.  The probe must reach every atom the read keeps (S1C-O1), or the read takes atoms away one by one, each
     read as it goes (requirement 15; the destroying read, 136 (4)).
  C4 (computed) Complete and parallel.  Every atom is read (requirement 15, source_spec U7): 8.49e22 records for the
     cm^3 piece, at C2's 1.3e-18 s each 1.1e5 s in sequence.  Within B2's 2.2 ms that is 5.3e7 channels at least, at
     300 K; cold, it is any number.
  C5 (computed; exact where marked) Energy.  Each README bit carries Smarr's share of Landauer's at the face, (3/2) k T_H
     ln2 in five dimensions (encode_read E2, exact), so the README is E5(N) of information as energy (432 (1)).  The
     read's own least energy for N orthogonal records in T_read is pi hbar N/(2 T_read): 9.9e-11 J for the real piece in
     2.2 ms.  Resetting the device's memory for the next trip costs N k T ln2: 3.7 J at 300 K.  E5(N) is paid by the
     object's own rest energy when N <= N*(m) (the destroying read, 136 (4); encode_read E4).  The real piece's
     N* = 1.37e24 is above its 1.3e21, so it pays: E5 is 0.96 % of its m c^2.  Otherwise the device's input makes up the
     difference (130 (2)).
  D. HOW THAT FUNCTION IS EXECUTED
  D1 (computed) The read: on the user's choice, C1's projective read of every label, C3's probe, C4's channels, within
     B2's instant -- or the object cooled until B2 holds.
  D2 (computed: encode_labels) The encode: the labels to the canonical code, N its length, exact (decoded back to the
     same graph, checked).
  D3 (computed: ledger; source_spec U2) The hand-off: N fixes r_h and E5(N), and the opening shell delivers E5(N) all at
     once.  That shell is the bulk emitter's (486, proved: emitter.py), the third of SOURCE's needs and not the device's.
  D4 (computed: passage_est Q4, Q6) The write: the device emits the README as radiation into our face at T_H.
     - It is the plane's own radiation, so energy stays in our universe (336).  For the real piece, T_H = 4.2e14 K, a
       mean quantum of 98 GeV, wavelengths across the absorbed band of 1.8e-19 to 5.5e-17 m.
     - Each quantum carries 5.20 bits, the thermal entropy per quantum (4/3)(3 zeta(4)/zeta(3))/ln2 (exact).  So the
       README's N bits ride on 2.5e20 quanta, its state the code: R1 is met by r1_exact's exact inverse.
     - The inflow E5/2 is spread over tau_w = (1 + b) of the hole's life, 1.2e-6 s.  Its power must match the face's
       to 1/N (passage_est Q6), round in the mean.
  D5 (computed: face2_release, r1_exact) The release: the passage is held whole and released at the write's end (432
     (2)).  Position 2's face is open at most 2 r_h/c and holds, and position 2 inverts the interior's unitary map
     exactly.  The device does nothing after the write.

What this does not claim: a built device.  It claims the definition, the start, the function and the execution the
theorem's math requires, each computed, and consistent with quantum mechanics and general relativity.  Two parts of
SOURCE lie outside the device: the bulk emitter's process (D3), and the bulk read's reach (C3) where it is not a
destroying read.

python3 reader.py [--selftest | --mutants]
"""
import os, sys, math, re, io, contextlib, importlib.util, random
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
HBAR = 1.054571817e-34; H = 6.62607015e-34; C = 299792458.0; KB = 1.380649e-23; EV = 1.602176634e-19
ME = 9.1093837015e-31
ZETA3 = 1.2020569031595942; ZETA4 = math.pi ** 4 / 90
WORDS = ((130, "Is that amount your input to the device for each trip, read from the object being moved? - yes"),
         (146, "no tolerance at all"), (386, "only information can travel"),
         (492, "how its start is initiated, what is required of its function, and how that function is executed"))
CU_A = 3.615e-10                                                   # standard, not READ (encode_labels C3's value)
CU_MASS = 8.96e-3; CU_MOLAR = 63.546e-3; NA = 6.02214076e23        # 1 cm^3 of copper; standard, not READ
# copper vacancies (standard values, not READ): formation 1.28 eV, migration 0.70 eV, attempt frequency 1e13 Hz
E_F, E_MIG, NU0 = 1.28, 0.70, 1e13


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    ok = True
    for n, w in WORDS:
        m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
        ok = ok and bool(m) and w in " ".join(m.group(0).split())
    return ok


# ------------------------------------------------------------------ A
def definition():
    EL = _load("encode_labels.py", "rd_el")
    water = EL.encode_body([8, 1, 1], [(0, 1), (0, 2)])
    ethanol = EL.encode_body([6, 6, 8, 1, 1, 1, 1, 1, 1], [(0, 1), (1, 2), (0, 3), (0, 4), (0, 5), (1, 6), (1, 7),
                                                            (2, 8)])
    ether = EL.encode_body([6, 8, 6, 1, 1, 1, 1, 1, 1], [(0, 1), (1, 2), (0, 3), (0, 4), (0, 5), (2, 6), (2, 7),
                                                          (2, 8)])
    rng = random.Random(492)
    Zs, bonds = EL.relabel([6, 6, 8, 1, 1, 1, 1, 1, 1], [(0, 1), (1, 2), (0, 3), (0, 4), (0, 5), (1, 6), (1, 7), (2, 8)], rng)
    canon = EL.encode_body(Zs, bonds) == ethanol
    back = EL.decode_body(ethanol)
    exact = EL.encode_body(*back) == ethanol if isinstance(back, tuple) else False
    n_cu, cu = EL.copper_block()
    d, per, N_real, E_real, mc2 = EL.real_piece()
    ER = _load("encode_read.py", "rd_er")
    E5r, rhr = ER.e_small(N_real)
    return dict(water=len(water), ethanol=len(ethanol), ether=len(ether), differ=ethanol != ether, canon=canon,
                exact=exact, cu=len(cu), N_real=N_real, E5r=E5r, rhr=rhr, mc2=mc2, per=per, ER=ER,
                domain=7.12e9)


# ------------------------------------------------------------------ B
def start(df):
    N, E = sp.symbols("N E0", positive=True)
    E5 = E * N ** sp.Rational(2, 3)
    dEdN = sp.simplify(sp.diff(E5, N) / (E5 / N))                    # = 2/3
    one_label = float(dEdN) * df["per"] / df["N_real"]               # relative change of E5 for one defect label more
    # copper's label changes: equilibrium vacancies hopping (standard values, not READ)
    n_at = CU_MASS / CU_MOLAR * NA
    def gam(T):
        kT = KB * T / EV
        return n_at * math.exp(-E_F / kT) * NU0 * math.exp(-E_MIG / kT)
    g300, g77 = gam(300.0), gam(77.0)
    if "no_instant" in MUT:
        g300 = 0.0
    return dict(dEdN=dEdN, one_label=one_label, g300=g300, g77=g77, t300=(1 / g300 if g300 else float("inf")),
                n_at=n_at)


# ------------------------------------------------------------------ C
def function(df, st):
    s = sp.symbols("s", nonnegative=True)
    Pe = (1 - sp.sqrt(1 - s ** 2)) / 2
    zero_only = sp.solve(sp.Eq(Pe, 0), s) == [0]
    RI = _load("read_index.py", "rd_ri")
    tau = {}
    for Z, nm in ((1, "H"), (8, "O"), (26, "Fe"), (29, "Cu")):
        D = RI.gaps(Z)["min"]
        tau[nm] = math.pi * HBAR / (2 * D) * (1e3 if "slow_record" in MUT else 1.0)
    win_cu = RI.window(29, st["n_at"])                              # read_index's conservative window at the copper's n
    spect_err = RI.p_atom(29, win_cu * 10)                           # still > 0 at ten windows
    d_nn = CU_A / math.sqrt(2)
    E_ph = H * C / d_nn / EV
    E_el = (H / d_nn) ** 2 / (2 * ME) / EV
    E_K = RI.k_scale(29) / EV
    seq = st["n_at"] * tau["Cu"]
    channels = seq * st["g300"] if st["g300"] else 0.0
    T_read = st["t300"]
    e_ml = math.pi * HBAR * df["N_real"] / (2 * T_read) if math.isfinite(T_read) else 0.0
    e_reset = df["N_real"] * KB * 300.0 * math.log(2)
    nstar = df["ER"].n_star(CU_MASS)
    # E2: E5(N)/N = (3/2) k T_H ln2, kT_H = hbar c/(2 pi r_h), exact
    kTH = HBAR * C / (2 * math.pi * df["rhr"])
    smarr = df["E5r"] / (df["N_real"] * kTH * math.log(2))
    return dict(zero_only=zero_only, tau=tau, ratio=win_cu / tau["Cu"], spect_err=spect_err, E_ph=E_ph, E_el=E_el,
                E_K=E_K, seq=seq, channels=channels, e_ml=e_ml, e_reset=e_reset, nstar=nstar, smarr=smarr,
                frac=df["E5r"] / df["mc2"], kTH=kTH)


# ------------------------------------------------------------------ D
def execution(df):
    HS = _load("hold_small.py", "rd_hs")
    dof = sum(n_ for n_, _ in HS.GREY_SPIN.values())
    gam = sum(n_ * g for n_, g in HS.GREY_SPIN.values()) / dof
    b = HS.GRAV_BULK_DOF / (gam * dof)
    N, rh, E5 = df["N_real"], df["rhr"], df["E5r"]
    life = 45 * N * math.log(2) / (dof * gam * (1 + b))               # face clocks (hold_small L5)
    clock = rh / C
    tau_w = (1 + b) * life * clock
    kTH = HBAR * C / (2 * math.pi * rh)
    q_mean = 3 * ZETA4 / ZETA3 * kTH
    bpq = sp.nsimplify(sp.Rational(4, 3)) * 3 * sp.zeta(4) / sp.zeta(3) / sp.log(2)
    bpq_f = float(bpq) * (0.5 if "half_bits" in MUT else 1.0)
    n_q = N / bpq_f
    E_in = E5 / 2
    lam = (2 * math.pi * rh / 30.0, 2 * math.pi * rh / 0.1)
    return dict(TH=kTH / KB, q_TeV=q_mean / EV / 1e12, bpq=bpq_f, n_q=n_q, tau_w=tau_w, P=E_in / tau_w, match=1 / N,
                lam=lam, E_in=E_in, bits_check=abs((4 / 3) * E_in / kTH / math.log(2) / N - 1))


def compute():
    df = definition(); st = start(df)
    return dict(words=words(), df=df, st=st, fn=function(df, st), ex=execution(df),
                r1=_load("r1_exact.py", "rd_r1").selftest(quiet=True),
                f2=None)


def checks(o):
    df, st, fn, ex = o["df"], o["st"], o["fn"], o["ex"]
    return [("A0: M's 130, 146, 386 and 492 verbatim in the rulings", o["words"]),
            ("A1: the device R = encode o measure, ENCODE's canonical code: water 22 bits, ethanol 79 and dimethyl ether a "
             "different 79, independent of order, decoded exactly; the perfect copper block 174 bits",
             df["water"] == 22 and df["ethanol"] == 79 and df["ether"] == 79 and df["differ"] and df["canon"]
             and df["exact"] and df["cu"] == 174),
            ("A2: N is the trip's input and fixes the corridor; the real copper piece (1.3e21 bits) inside the domain "
             "N >= 7.12e9 at r_h 8.7e-19 m, E5 7.7e12 J; a molecule and the perfect crystal below it",
             "%.2g" % df["N_real"] == "1.3e+21" and df["N_real"] >= df["domain"] and df["cu"] < df["domain"]
             and "%.2g" % df["rhr"] == "8.7e-19" and "%.2g" % df["E5r"] == "7.7e+12"),
            ("B1-B2: dE5/dN = (2/3) E5/N, one defect label more moves E5 by 7.9e-20 of itself, so the read completes "
             "before the opening; one instant: 464 label changes per second per cm^3 of copper at 300 K (the read "
             "within 2.2 ms), 2.2e-94 at 77 K",
             st["dEdN"] == sp.Rational(2, 3) and "%.2g" % st["one_label"] == "7.9e-20" and round(st["g300"]) == 464
             and "%.2g" % st["t300"] == "0.0022" and "%.2g" % st["g77"] == "2.2e-94"),
            ("C1: Helstrom's error vanishes only for orthogonal records; the spectroscopic read still errs at ten windows",
             fn["zero_only"] and fn["spect_err"] > 0),
            ("C2: an orthogonal record within pi hbar/(2D): 2.5e-17 s (H), 5.1e-18 (O), 1.5e-18 (Fe), 1.3e-18 (Cu), 6.7 "
             "times faster than read_index's window at the copper's n",
             ["%.2g" % fn["tau"][k] for k in ("H", "O", "Fe", "Cu")] == ["2.5e-17", "5.1e-18", "1.5e-18", "1.3e-18"]
             and "%.2g" % fn["ratio"] == "6.7"),
            ("C3: site within half a spacing: a photon >= 4.85 keV or an electron >= 23 eV in copper; Z by the K shell, "
             "E_K 11.4 keV, above it", "%.3g" % (fn["E_ph"] / 1e3) == "4.85" and round(fn["E_el"]) == 23
             and "%.3g" % (fn["E_K"] / 1e3) == "11.4" and fn["E_K"] > fn["E_ph"]),
            ("C4-C5: 1.1e5 s in sequence, 5.3e7 channels within 2.2 ms; least read energy 9.9e-11 J, reset 3.7 J at "
             "300 K; each bit (3/2) k T_H ln2 at the face; N* 1.37e24 above the piece's N, E5 0.96 % of its m c^2",
             "%.2g" % fn["seq"] == "1.1e+05" and "%.2g" % fn["channels"] == "5.3e+07" and "%.2g" % fn["e_ml"] == "9.9e-11"
             and "%.2g" % fn["e_reset"] == "3.7" and abs(fn["smarr"] - 1.5) < 1e-9 and "%.3g" % fn["nstar"] == "1.37e+24"
             and fn["nstar"] > df["N_real"] and "%.2g" % (100 * fn["frac"]) == "0.96"),
            ("D4: the write at T_H 4.2e14 K, mean quantum 98 GeV, 5.20 bits per quantum (exact), 2.5e20 quanta over "
             "tau_w 1.2e-6 s, the bits saturating (4/3) E_in/(k T_H ln2) = N, power matched to 1/N",
             "%.2g" % ex["TH"] == "4.2e+14" and round(ex["q_TeV"] * 1e3) == 98 and "%.3g" % ex["bpq"] == "5.2"
             and "%.2g" % ex["n_q"] == "2.5e+20" and "%.2g" % ex["tau_w"] == "1.2e-06" and ex["bits_check"] < 1e-9),
            ("D5: R1 met by the exact inverse (r1_exact selftest)", o["r1"])]


def report(o=None):
    o = o or compute(); df, st, fn, ex = o["df"], o["st"], o["fn"], o["ex"]
    print("reader.py -- SOURCE's device that reads the object into the README (item 492)\n")
    print("A  README lengths: water %d, ethanol %d, dimethyl ether %d (differ %s), canonical %s, exact %s; copper block "
          "%d bits; real piece N %.3g, r_h %.3g m, E5 %.3g J" % (df["water"], df["ethanol"], df["ether"], df["differ"],
                                                                 df["canon"], df["exact"], df["cu"], df["N_real"],
                                                                 df["rhr"], df["E5r"]))
    print("B  dE5/dN = %s E5/N; one label: %.2g; label changes: %.3g /s (300 K) -> read within %.3g s; %.2g /s (77 K)"
          % (st["dEdN"], st["one_label"], st["g300"], st["t300"], st["g77"]))
    print("C  exact iff orthogonal: %s; tau_min %s; %.2gx faster than the spectroscopic window; probe >= %.3g keV photon "
          "or %.0f eV electron, E_K %.3g keV; %.2g s in sequence, %.2g channels; read energy %.2g J, reset %.2g J; "
          "bit energy / (k T_H ln2) = %.4f; N* %.3g; E5/mc^2 %.3g"
          % (fn["zero_only"], ", ".join("%s %.2g s" % kv for kv in fn["tau"].items()), fn["ratio"], fn["E_ph"] / 1e3,
             fn["E_el"], fn["E_K"] / 1e3, fn["seq"], fn["channels"], fn["e_ml"], fn["e_reset"], fn["smarr"], fn["nstar"],
             fn["frac"]))
    print("D  write: T_H %.3g K, quantum %.3g TeV, %.4f bits/quantum, %.3g quanta, tau_w %.3g s, P %.3g W, match %.2g, "
          "band %.2g-%.2g m; R1 inverse %s" % (ex["TH"], ex["q_TeV"], ex["bpq"], ex["n_q"], ex["tau_w"], ex["P"],
                                               ex["match"], ex["lam"][0], ex["lam"][1], o["r1"]))


MUTANTS = {"no_instant": "the last state read without its instant: no bound on the read's duration (B2)",
           "slow_record": "the record taken a thousand times slower than the gap allows (C2)",
           "half_bits": "half the thermal entropy per quantum (D4)"}


def selftest(quiet=False):
    r_ = checks(compute())
    if not quiet:
        for n_, ok in r_:
            print("  [%s] %s" % ("ok" if ok else "FAIL", n_))
    k = sum(ok for _, ok in r_)
    if not quiet:
        print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            failed = [n_.split(":")[0] for n_, ok in checks(compute()) if not ok]
        except Exception as e:
            failed = ["raised %s" % type(e).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  [%s] %s -> %s" % ("caught" if failed else "MISSED", desc, ", ".join(failed) or "nothing"))
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
