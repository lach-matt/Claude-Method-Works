#!/usr/bin/env python3
"""write_small.py -- item 260: the WRITE row's count at the family's small end.  The record's write (O3-WRITE W1-W5,
o3_write.py: T >= (9/2)(5 N ln2/Z)^(1/3) - 2 clocks of m/c, 199,702.19 at the example README) is a four-dimensional
derivation; M: "The write's clock count is still the record's 4D derivation. Redoing it at the small end belongs to the
WRITE row. - we need to address this first".  Here it is redone for the localized five-dimensional hole (C1, C2, C3;
items 251, 256), every hypothesis of O3-WRITE carried where it carries and named where it does not.  Worked in the
conversation (computed with sympy and mpmath, exact where marked; READ where marked; verified once -- item 264,
CONFIRMED with qualifications, all seated below in [Verifier, item 264] notes (205/206); not seated); 2026-10-11.
First headed "... not verified by a separate session ...".

  S0 (read) M's item-260 words, verbatim in the rulings file.
  S1 (STRUCTURAL) The small end's E is the five-dimensional black-hole energy of N bits: 2 pi^2 r_h^3/(4 l5^3) = N ln2
     with E = 3 pi c^4 r_h^2/(8 G5), by C2/C3's own construction -- not a finding.  Unlike the record's end it does not
     saturate Bekenstein's eq. (85): at R = r_h, 2 pi E R/(hbar c ln2) = 3N/2 bits, the hole holding 2/3 of the bound
     (computed).  So eq. (85) in place of the gas gives R >= (2/3) r_h -- no floor at all (T >= -1/3).
  S2 (computed from READ: Bekenstein-Schiffer, quant-ph/0311050, eqs. (86), (97), (112), (115), as o3_write W2 reads
     them) The rate bounds still take a fixed number of clocks: the five-dimensional hole has S = (4 pi/3) E r_h/(hbar
     c) (computed; the record's end has 2 pi E r_h), so N bits at a rate linear in E take N/(E r_h) clocks, a constant --
     (86) 2/3, (97) 26.5, (112) 8 pi^2/(3 ln2) = 37.97, (115) 37.97/log2(N_ch/ln2).  None decides the hold.
  S3 (computed from READ: 't Hooft, gr-qc/9310026, eqs. (2), (4), (5), (8), as o3_write W3 reads them; under named
     mappings) The gas bound.  The write is done when the README has crossed onto the hole's horizon at r = r_h
     (H-WRITE-IS-ARRIVAL, carried).  Moving at most at c, all of it then lay, when the write began, inside the ball of
     radius (1 + T) r_h, T the write's length in clocks of r_h/c (H-SMALL-CLOCK, replacing H-PULL-IS-COST: r_h/c =
     1/(c kappa), the hole's own clock, as C5 uses; seconds carry no clock convention) in advanced time (H-HOLD-FRAME,
     carried), the plane and the bulk flat there (H-FLAT-START, carried: R/ell and (r_h/R)^2 computed), carrying only
     the README's E (H-README-ALONE, carried).  The README is written in our plane's own fields (H-README-ON-PLANE,
     replacing H-NO-SHORTCUT: at the small end the bulk is where the hole lives, not a shortcut), so its gas lives in
     d = 3 on the plane; before it collapses its states at fixed E and V are at most the free gas's (H-FREE-GAS,
     carried); N bits need e^S >= 2^N (H-BITS-ARE-STATES, carried).  Exact, in the thermodynamic limit without
     self-gravity:
            T >= (3/2)(5 N ln2/Z)^(1/3) - 1 clocks of r_h/c          (d = 3, on the plane)
     -- at equal Z one third of the record's ball, (9/2)(5 N ln2/Z)^(1/3) in clocks of m/c, each end in its own clock.
     [Verifier, item 264: "one third" is a clock convention -- m/c = 1/(4 c kappa) there, r_h/c = 1/(c kappa) here; in
     horizon radii the ratio is 2/3, in units of 1/kappa 4/3 (computed, S5); physically the small end's ball is 1.9e7
     times the record's (7.5e-16 m against 4.0e-23 m) and its write as much longer in seconds (computed, S5).]
     Z is fixed by the gas's own temperature: at the bound 4E/(3S) = hbar c/(pi r_h), twice the hole's Hawking
     temperature, 5.6 TeV at the example README -- every Standard Model species is lighter, so Z >= 106.75 (the plane's
     species; at R << ell the graviton is five-dimensional, not a field of the plane, and enters V2).  At the example
     README: 66,980 clocks (Z = 106.75); the record's Z = 108.75 gives 66,567.06 = (199,702.19 + 2)/3 - 1, exactly.
     The count carries no ell: r_h/l5 is fixed by N (C3 F4).  In seconds at ell = 13.964 um (clock r_h/c = 3.74e-29 s):
     2.5e-24 s, and at every ell as ell^(1/3).  Self-gravity at the start: (r_h/R)^2 = 2.2e-10; R/ell = 5.4e-11.
     [Verifier, item 264: three of O3-WRITE's twelve hypotheses were left unnamed.  H-EXACT-ENERGY-AT-BOUND (G1) is
     replaced by C2's R1 count -- the count carries R1, which item 258 records as resting on convention-consistency:
     under R2 (one side) 1 + T halves and the head is 33,490 clocks (computed, S5).  H-WRITE-IN-STATIC-HOLD is carried
     by S4 only (the hole standing at its size through the write, M's 162-163).  R-VAIDYA-HOLDS is not carried:
     reading (ii) is not computed.]
     Variants (each fits the hold, S4):
       V2 H-README-ON-PLANE dropped: the plane's gas (d = 3, Z = 106.75) and the bulk graviton's (d = 4, 5 states, the
          4-ball on both sides of the plane, if the two sides are independent) at one temperature -- 1.251e4 clocks
          (computed, mpmath; the verifier's brute-force scan of the energy split peaks at the same split, 0.5% of E in
          the plane's gas); the graviton gas holds the most states per energy and sets the bound, the plane's lowering
          it by 0.2%.  [Verifier, item 264: "both sides as C2's R1 counts both" does not follow -- R1 and E are the same
          under the Z2 orbifold (covering-space normalisation) and under two independent sides, but the gas is not:
          under the orbifold only one side's graviton modes are independent -- V2 1.486e4, V3 1.490e4 (computed).]
       V3 the bulk graviton alone (d = 4, Z = 5): T >= 16 30^(3/4) pi (N ln2/Z)^(1/4)/(225 zeta(5)^(1/4)) - 1 =
          1.253e4 clocks; the power is 1/4, as the record's d = 4 variant.  Over one side of the plane only (the 4-ball
          halved, as Z/2: 1 + T scales as 2^(1/4), exact) 1.490e4 -- the critic's case, computed.  [Verifier, item
          264: V3's floor does not fall with the plane's Z, so with the same species in the evaporation (life as
          1/Z) it fails above Z = 6.8e12 (5.7e12 over one side) -- inside H-SPECIES-FINITE's ~1e14 (computed, S5).]
       V4 H-README-ALONE dropped ('t Hooft's eq. (8): energy up to the five-dimensional collapse 3 pi c^4 R^2/(8 G5) in
          the ball): 1 + T = ((3/2)(5 N ln2/Z)^(1/3))^(1/3), the head's ball to the power 1/3 -- 39.6 clocks, N^(1/9)
          (the record's eq. (8) variant goes as N^(1/6): the 4D collapse energy grows as R, the 5D as R^2).
       V5 prior entanglement (superdense coding, items 111, 137 (1)): 2^(-4/3) on 1 + T -- 26,580 clocks (Z = 106.75).
  S4 (computed; hold_small L3 imported) What it does to the hold at the small end, on reading (i) -- the hole standing
     at its size through the write (H-WRITE-IN-STATIC-HOLD; M's 162-163) [verifier, item 264].  The static bulk under the corridor
     is Tangherlini's exterior, regular with a smooth horizon (C1 H5, verified); it has no singular surface outside the
     horizon, so the record's tension -- the static eq. (17) bulk singular by ~18 clocks against a write of 2.0e5
     (O3-WRITE W4, the theorem's item-160 history: "the corridor must change while the README passes") -- does not
     arise.  The static hold lasts as long as the hole: 8.0e14 clocks at every ell (greybody 1; hold_small L4).  The
     write's floor sits inside it by 1.2e10 (greybody 1; 1.2e11 at greybody 0.1), and every variant fits at g* =
     106.75.  The energy the hole radiates over the write is t_w/(2 t_life) = 4.2e-11 of E: quasi-static through the
     write.  [Verifier, item 264: on reading (ii) (198, a guess: the README forms the hole) the bulk is not static
     through the write, as on the record, and the lifetime bounds only the completed hole.  Reading (i) carries an open
     energy question of its own: a hole of E(N) standing, and a README carrying E under H-README-ALONE, total 2E.
     With the same Z in the evaporation (life as 1/Z, floor as Z^(-1/3)) the head, V2, V4 and V5 fit at every Z --
     the head's floor reaches zero first (computed over Z to 3.2e16; V2, V4, V5 lie below the head) -- and V3 only for
     Z < 6.8e12 (S5).]
     [Item 338 (with item 340), seated after C8's verdict (its verifier loaded this file through hold_small): reading
     (ii) is computed -- arrival_small V1-V5: the README's own E forms the face, one E, so reading (i)'s 2E does not
     arise; this floor carries unchanged, its 66,980 clocks the README's approach in our exterior and the arrival onto
     the face compact, within 4.79 clocks. On 340's "for the math", with M's guess A, the math gives reading (ii),
     compact (arrival_small V11), the board's reading.]

What this does not show.
  - Whether the hole stands before the README arrives (items 162, 163: fixed size, one whole) or forms as it arrives
    (198, a guess): the floor counts only the README's states before arrival and holds on either reading; S4 holds on
    the first only [verifier, item 264].
  - The WRITE row's cypher at the small end (write_cypher.py with the localized hole's row re-read under item 251; item
    260 (b), in chain order).
  - The gas's self-gravity and greybody factors; species beyond the Standard Model (H-SPECIES-FINITE, carried).
    [First written "Z larger only shortens the floor, and the floor fits the hold at every Z >= 1" -- overstated
    (verifier, item 264): it held the evaporation's g* at 106.75 while Z varied; with the same Z in both, V3 fails
    above 6.8e12 (S4, S5).]
  - Linear survival over the write: the hole's linear stability is READ (Ishibashi-Kodama, via B4D-STAGE1.md and
    write_cypher W3), not computed here.

Imports o3_write.py (its gas and ball, and its t_min as the control), hold_small.py (the lifetime) and p2_gravity.py by
path.  Stdlib + sympy + mpmath.  python3 write_small.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
M260 = ("Not yet, One caveat. The write's clock count is still the record's 4D derivation. Redoing it at the small end "
        "belongs to the WRITE row. - we need to address this first")
N_EX = 2742570311524972
Z_PLANE = sp.Rational(10675, 100)          # the Standard Model's g* 106.75: the plane's species, all lighter (S3)
Z_RECORD = sp.Rational(10875, 100)         # the record's 106.75 + the four-dimensional graviton's 2 (control)
Z_GRAV5 = 5                                # a massless spin-2 field in five dimensions: D(D-3)/2 = 5 states
RECORD_FLOOR = 199702.19                   # the theorem's history: o3_write t_min(3) at the example README, Z = 108.75

N, Z, X, l5 = sp.symbols("N Z x l5", positive=True)


def _load(path, key):
    saved = list(sys.path)
    sys.path[:0] = [os.path.dirname(path), D68, WD]
    try:
        spec = importlib.util.spec_from_file_location(key, path)
        mod = importlib.util.module_from_spec(spec)
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
    finally:
        sys.path[:] = saved
    return mod


def _o3w():
    return _load(os.path.join(HERE, "o3_write.py"), "ws_o3w")


def hole(side="both"):
    """the small end in the bulk's Planck units (hbar = c = 1, G5 = l5^3): r_h, E, S (C2 R1, both sides; R2 one side)"""
    area = sp.pi ** 2 if (MUT.get("one_side") or side == "one") else 2 * sp.pi ** 2
    rho = (4 * N * sp.log(2) / area) ** sp.Rational(1, 3)
    rh = rho * l5
    E = 3 * sp.pi * rh ** 2 / (8 * l5 ** 3)
    S = sp.simplify(2 * sp.pi ** 2 * rh ** 3 / (4 * l5 ** 3))
    return dict(rh=rh, E=E, S=S)


def _offset():
    return 2 if MUT.get("record_offset") else 1          # the ball's radius (offset + T) r_h: the horizon is at r_h


def s1():
    h = hole()
    bek_bits = sp.simplify(2 * sp.pi * h["E"] * h["rh"] / sp.log(2))
    x_bek = sp.solve(sp.Eq(2 * sp.pi * h["E"] * X * h["rh"] / sp.log(2), N), X)[0]
    return dict(S=h["S"], bek_bits=bek_bits, x_bek=x_bek)


def s2():
    h = hole()
    rate = {"(86) bulk transport": 2 * sp.pi * h["E"] / sp.log(2),
            "(97) one channel, mean energy, self-heralding": sp.Rational(2279, 10000) * h["E"],
            "(112) one channel, energy ceiling": h["E"] / (2 * sp.pi)}
    clocks = {k: sp.nsimplify(sp.simplify(N / r / h["rh"])) for k, r in rate.items()}
    nch = sp.Symbol("N_ch", positive=True)
    clocks["(115) N_ch >> 1 channels"] = sp.simplify(N / (h["E"] / (2 * sp.pi) * sp.log(nch / sp.log(2), 2)) / h["rh"])
    smarr = sp.simplify(h["S"] / (h["E"] * h["rh"]))
    return dict(clocks=clocks, smarr=smarr)


def _bound(d, energy, bits=N, side="both"):
    """1 + T (offset + T under a mutant): the radius, in r_h, of the d-ball whose free gas at this energy holds 2^bits"""
    O = _o3w()
    _, _, a = O.gas(d)
    h = hole(side)
    zz = Z_GRAV5 if d == 4 else Z
    S = a * zz ** sp.Rational(1, d + 1) * O.ball(d, X * h["rh"]) ** sp.Rational(1, d + 1) * energy ** sp.Rational(d, d + 1)
    # both sides positive: raise to the power d + 1, so the equation is a monomial in x with one positive root
    sol = [r for r in sp.solve(sp.Eq(sp.expand_power_base(sp.simplify(S ** (d + 1)), force=True),
                                     (bits * sp.log(2)) ** (d + 1)), X) if r.is_positive]
    assert len(sol) == 1
    return sp.simplify(sol[0])


def s3():
    h = hole()
    x3 = _bound(3, h["E"])
    t3 = x3 - _offset()
    x4 = _bound(4, h["E"])                                         # V3: the bulk graviton alone, Z = 5
    x8 = _bound(3, 3 * sp.pi * (X * h["rh"]) ** 2 / (8 * l5 ** 3))
    xd = _bound(3, h["E"], bits=N / 2)
    tgas = sp.simplify(4 * h["E"] / (3 * h["S"]) * h["rh"])          # in units 1/r_h; Hawking is 1/(2 pi)
    x3_r2 = _bound(3, hole("one")["E"], side="one")                   # item 264: the count under C2's R2 (one side)
    return dict(x3=x3, t3=t3, x4=x4, x8=x8, xd=xd, tgas_rh=tgas, x3_r2=x3_r2)


def mixed(n=N_EX, zb=106.75, zg=Z_GRAV5, half=False):
    """V2: the plane's gas (d = 3, zb) and the bulk graviton's (d = 4, zg) in balls of radius x r_h, one temperature,
    energy E, entropy N ln2 (mpmath, 30 digits; units l5 = 1)"""
    mp.mp.dps = 30
    area = mp.pi ** 2 if MUT.get("one_side") else 2 * mp.pi ** 2
    rho = (4 * n * mp.log(2) / area) ** (mp.mpf(1) / 3)
    E = 3 * mp.pi * rho ** 2 / 8
    u3, u4 = mp.pi ** 2 / 30, 3 * mp.zeta(5) / mp.pi ** 2
    v3 = lambda R: 4 * mp.pi / 3 * R ** 3
    v4 = lambda R: mp.pi ** 2 / (4 if half else 2) * R ** 4       # half: the Z2 orbifold, one side's modes (item 264)

    def entropy(x):
        R = x * rho
        en = lambda tau: zb * u3 * v3(R) * tau ** 4 + zg * u4 * v4(R) * tau ** 5 - E
        lo_t, hi_t = mp.mpf("1e-40"), mp.mpf(10) * E          # the energy rises monotonically with temperature
        for _ in range(300):
            mid_t = mp.sqrt(lo_t * hi_t)
            lo_t, hi_t = (mid_t, hi_t) if en(mid_t) < 0 else (lo_t, mid_t)
        tau = mp.sqrt(lo_t * hi_t)
        return mp.mpf(4) / 3 * zb * u3 * v3(R) * tau ** 3 + mp.mpf(5) / 4 * zg * u4 * v4(R) * tau ** 4

    target = n * mp.log(2)
    lo, hi = mp.mpf(1), mp.mpf(10) ** 8
    for _ in range(200):
        mid = mp.sqrt(lo * hi)
        if entropy(mid) < target:
            lo = mid
        else:
            hi = mid
    return float(mp.sqrt(lo * hi))


def _num(expr, n=N_EX, z=None):
    return float(sp.N(expr.subs({N: n, Z: Z_PLANE if z is None else z}), 30))


def seconds():
    PG = _load(os.path.join(HERE, "p2_gravity.py"), "ws_pg")
    G, c, hbar = PG.G, PG.C, PG.HBAR
    out = {}
    for ell in (PG.ELL_MAX, 1e-9, 1e-20):
        G5 = G * ell
        lfive = (hbar * G5 / c ** 3) ** (1 / 3)
        rh = (2 * N_EX * math.log(2) / math.pi ** 2) ** (1 / 3) * lfive
        out[ell] = dict(rh=rh, clock=rh / c, ell=ell)
    kB = 1.380649e-23
    x = out[PG.ELL_MAX]
    tgas_K = hbar * c / (math.pi * kB * x["rh"])
    tgas_GeV = hbar * c / (math.pi * x["rh"]) / 1.602176634e-10
    return dict(rows=out, ell_max=PG.ELL_MAX, tgas_K=tgas_K, tgas_GeV=tgas_GeV)


def head_clocks():
    """the head floor at the example README, Z = 106.75 (hold_small imports this)"""
    return _num(s3()["t3"])


def s4(head):
    H = _load(os.path.join(HERE, "hold_small.py"), "ws_hold")
    L = H.lifetime()
    x = L["rows"][L["ell_max"]]
    life1, life01 = x["rows"][1.0]["clocks"], x["rows"][0.1]["clocks"]
    return dict(life1=life1, life01=life01, ratio1=life1 / head, ratio01=life01 / head, radiated=head / (2 * life1))


def compute():
    o = dict(s1=s1(), s2=s2(), s3=s3(), sec=seconds())
    t = o["s3"]
    o["ex"] = dict(head=_num(t["t3"]), record_z=_num(t["t3"], z=Z_RECORD), v3=_num(t["x4"]) - _offset(),
                   v4=_num(t["x8"]) - _offset(), v5=_num(t["xd"]) - _offset(), v2=mixed() - _offset(),
                   z1=_num(t["t3"], z=1))
    o["ex"]["v3_one_side"] = (_num(t["x4"]) * 2 ** 0.25) - _offset()
    x = _num(t["x3"])
    o["ex"]["self_grav"] = 1 / x ** 2
    row = o["sec"]["rows"][o["sec"]["ell_max"]]
    o["ex"]["R_over_ell"] = x * row["rh"] / row["ell"]
    o["ex"]["sec"] = {ell: o["ex"]["head"] * r["clock"] for ell, r in o["sec"]["rows"].items()}
    O = _o3w()
    o["record"] = float(O.t_min(3).subs({O.N: N_EX, O.Z: Z_RECORD}).evalf(30))
    o["s4"] = s4(o["ex"]["head"])
    o["s5"] = s5(o)
    return o


def s5(o):
    """item 264, the C6 verifier's qualifications, computed: R2's head; V2 over one side; the Z at which V3 outlasts
    the hole with the evaporation's species set to Z; the head against the life over Z; the balls compared with the
    record's, in convention and in metres"""
    t, e, s = o["s3"], o["ex"], o["s4"]
    life_z = lambda z: s["life1"] * 106.75 / z                        # P is linear in g*: the life falls as 1/Z
    head_z = lambda z: max(0.0, _num(t["t3"], z=sp.Float(z, 30)))
    zs = [10.0 ** k for k in range(0, 17)] + [3.2e16]
    head_fits = all(life_z(z) > head_z(z) for z in zs)
    zero_at = float(sp.Rational(27, 8) * 5 * N_EX * sp.log(2))          # the head's 1 + T reaches 1 here
    PG = _load(os.path.join(HERE, "p2_gravity.py"), "ws_pg5")
    m_rec = PG.G * PG.corridor(PG.G)["E1"] * math.sqrt(N_EX) / PG.C ** 4
    R_rec = (o["record"] + 2) * m_rec
    R_small = _num(t["x3"]) * o["sec"]["rows"][o["sec"]["ell_max"]]["rh"]
    rec_ball = sp.Rational(9, 2) * (5 * N * sp.log(2) / Z) ** sp.Rational(1, 3)   # in m; r0 = 2m, 1/kappa = 4m there
    return dict(head_r2=_num(t["x3_r2"]) - _offset(), v2_one=mixed(half=True) - _offset(),
                z_v3=s["life1"] * 106.75 / e["v3"], z_v3_one=s["life1"] * 106.75 / e["v3_one_side"],
                head_fits=head_fits, zero_at=zero_at, R_rec=R_rec, R_small=R_small, R_ratio=R_small / R_rec,
                in_radii=sp.simplify(t["x3"] / (rec_ball / 2)), in_kappa=sp.simplify(t["x3"] / (rec_ball / 4)))


def report(o):
    print("write_small.py -- the WRITE row's count at the family's small end (item 260)\n")
    print("S1 (STRUCTURAL) S = %s; Bekenstein eq. (85) at R = r_h: %s bits; eq. (85) in place of the gas: R >= %s r_h"
          % (o["s1"]["S"], o["s1"]["bek_bits"], o["s1"]["x_bek"]))
    print("S2 S/(E r_h) = %s (five-dimensional Smarr); the rate bounds in clocks of r_h/c:" % o["s2"]["smarr"])
    for k, c in o["s2"]["clocks"].items():
        print("     %-48s %s%s" % (k, c, "" if c.free_symbols else "  = %.2f" % float(c)))
    t = o["s3"]
    print("S3 the gas bound on the plane: T >= %s clocks of r_h/c" % t["t3"])
    print("   gas temperature at the bound x r_h = %s (Hawking 1/(2 pi)): %.3g K = %.3g GeV at the example"
          % (t["tgas_rh"], o["sec"]["tgas_K"], o["sec"]["tgas_GeV"]))
    e = o["ex"]
    print("   example README: %.2f clocks (Z = 106.75); %.2f (Z = 108.75; the record's %.2f -> (rec + 2)/3 - 1 = %.2f); "
          "Z = 1: %.4g" % (e["head"], e["record_z"], o["record"], (o["record"] + 2) / 3 - 1, e["z1"]))
    print("   self-gravity (r_h/R)^2 = %.2g; R/ell = %.2g; in seconds: %s" % (
        e["self_grav"], e["R_over_ell"], ", ".join("ell %.3g: %.3g s" % kv for kv in e["sec"].items())))
    print("   V2 plane + bulk graviton %.4g; V3 bulk graviton alone %.4g (one side %.4g); V4 eq. (8) %.4g; V5 superdense "
          "%.6g" % (e["v2"], e["v3"], e["v3_one_side"], e["v4"], e["v5"]))
    s = o["s4"]
    print("S4 the hold (the hole's lifetime) %.3g clocks (grey 1) / %.3g (grey 0.1); over the floor %.3g / %.3g; "
          "radiated over the write %.2g of E" % (s["life1"], s["life01"], s["ratio1"], s["ratio01"], s["radiated"]))
    v = o["s5"]
    print("S5 (item 264) under R2 the head %.2f; V2 over one side %.4g; V3 outlasts the life (species = Z) above Z = %.3g "
          "(%.3g one side); the head fits at every Z to %.3g: %s" % (v["head_r2"], v["v2_one"], v["z_v3"], v["z_v3_one"],
                                                                   v["zero_at"], v["head_fits"]))
    print("   the ball against the record's: %s in horizon radii, %s in 1/kappa; %.3g m against %.3g m (x %.3g)" % (
        v["in_radii"], v["in_kappa"], v["R_small"], v["R_rec"], v["R_ratio"]))


def checks(o):
    res = []
    add = lambda n, ok: res.append((n, bool(ok)))
    rul = " ".join(open(RULINGS, encoding="utf-8").read().split())
    add("S0 M's item-260 words verbatim in the rulings file", M260 in rul)
    s = o["s1"]
    add("S1 (STRUCTURAL) the hole holds N ln2; Bekenstein's eq. (85) at R = r_h gives 3N/2 bits (2/3 saturated); in "
        "place of the gas it gives R >= (2/3) r_h, no floor", sp.simplify(s["S"] - N * sp.log(2)) == 0
        and sp.simplify(s["bek_bits"] - sp.Rational(3, 2) * N) == 0 and s["x_bek"] == sp.Rational(2, 3))
    c = o["s2"]["clocks"]
    ok = sp.simplify(o["s2"]["smarr"] - 4 * sp.pi / 3) == 0 and c["(86) bulk transport"] == sp.Rational(2, 3)
    ok &= sp.simplify(c["(112) one channel, energy ceiling"] - 8 * sp.pi ** 2 / (3 * sp.log(2))) == 0
    ok &= abs(float(c["(97) one channel, mean energy, self-heralding"]) - 26.52) < 0.01
    add("S2 S = (4 pi/3) E r_h; the rate bounds take N-independent clocks: (86) 2/3, (97) 26.52, (112) 8 pi^2/(3 ln2)", ok)
    t = o["s3"]
    ok = sp.simplify(t["t3"] - (sp.Rational(3, 2) * (5 * N * sp.log(2) / Z) ** sp.Rational(1, 3) - 1)) == 0
    ok &= sp.simplify(t["tgas_rh"] - 1 / sp.pi) == 0
    add("S3a the gas bound is exactly T >= (3/2)(5 N ln2/Z)^(1/3) - 1 clocks of r_h/c; the gas at the bound is twice the "
        "hole's Hawking temperature", ok)
    e = o["ex"]
    ok = "%.0f" % e["head"] == "66980" and abs(e["record_z"] - ((o["record"] + 2) / 3 - 1)) < 1e-6
    ok &= "%.2f" % e["record_z"] == "66567.06" and "%.2f" % o["record"] == "199702.19"
    ok &= 5.5e3 < o["sec"]["tgas_GeV"] < 5.7e3 and e["self_grav"] < 3e-10 and e["R_over_ell"] < 1e-10
    ok &= "%.2g" % e["sec"][o["sec"]["ell_max"]] == "2.5e-24"
    add("S3b at the example README: 66,980 clocks (Z = 106.75); the record's Z gives 66,567.06 = (199,702.19 + 2)/3 - 1; "
        "gas at 5.6 TeV; (r_h/R)^2 < 3e-10; 2.5e-24 s at ell = 13.964 um", ok)
    ok = "%.4g" % e["v2"] == "1.251e+04" and "%.4g" % e["v3"] == "1.253e+04" and "%.3g" % e["v4"] == "39.6"
    ok &= "%.4g" % e["v5"] == "2.658e+04" and e["v2"] < e["v3"] < e["v3_one_side"] < e["head"]
    ok &= "%.3e" % e["v3_one_side"] == "1.490e+04"
    ok &= sp.simplify(t["x8"] - t["x3"] ** sp.Rational(1, 3)) == 0
    ok &= abs((e["v5"] + 1) / (e["head"] + 1) - 2 ** (-4 / 3)) < 1e-12
    add("S3c variants: plane + bulk graviton 1.251e4, the graviton alone 1.253e4, eq. (8) 39.6 (the head's ball to the "
        "1/3), superdense 2.658e4 (2^(-4/3) on 1 + T); the graviton over one side 1.490e4", ok)
    s = o["s4"]
    ok = "%.2g" % s["ratio1"] == "1.2e+10" and "%.2g" % s["ratio01"] == "1.2e+11" and "%.2g" % s["radiated"] == "4.2e-11"
    ok &= e["z1"] < s["life1"]
    add("S4 the static hold (the hole's life, 8.0e14 clocks) exceeds the floor by 1.2e10 (grey 1) / 1.2e11 (grey 0.1); "
        "4.2e-11 of E radiated over the write; fits at Z = 1 too", ok)
    v = o["s5"]
    ok = "%.0f" % v["head_r2"] == "33490" and "%.3e" % v["v2_one"] == "1.486e+04"
    ok &= "%.2g" % v["z_v3"] == "6.8e+12" and "%.2g" % v["z_v3_one"] == "5.7e+12" and v["head_fits"]
    ok &= "%.2g" % v["zero_at"] == "3.2e+16"
    ok &= v["in_radii"] == sp.Rational(2, 3) and v["in_kappa"] == sp.Rational(4, 3) and "%.2g" % v["R_ratio"] == "1.9e+07"
    ok &= "%.2g" % v["R_small"] == "7.5e-16" and "%.2g" % v["R_rec"] == "4e-23"
    add("S5 (item 264) R2's head 33,490; V2 over one side 1.486e4; V3 outlasts the life above Z = 6.8e12 (5.7e12 one "
        "side) while the head fits at every Z (to 3.2e16, where its floor is 0); the ball 2/3 of the record's in horizon "
        "radii, 4/3 in 1/kappa, 1.9e7 in metres", ok)
    return res


MUTANTS = {"one_side": "the hole's count over one side of the plane",
           "record_offset": "the ball's radius (2 + T) r_h, the record's 2m carried over",
           "graviton_on_plane": "the four-dimensional graviton's 2 counted in the plane's gas"}


def _compute_mut():
    if MUT.get("graviton_on_plane"):
        global Z_PLANE
        saved = Z_PLANE
        Z_PLANE = Z_RECORD
        try:
            return compute()
        finally:
            Z_PLANE = saved
    return compute()


def selftest():
    r_ = checks(compute())
    for n, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", n))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for kk, desc in MUTANTS.items():
        MUT.clear()
        MUT[kk] = True
        try:
            failed = [n.split()[0] for n, ok in checks(_compute_mut()) if not ok]
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-17s %-56s %s" % (kk, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
