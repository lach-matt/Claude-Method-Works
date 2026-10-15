#!/usr/bin/env python3
"""source_capacity.py -- item 424 (2), the review of SOURCE: can the README's carrier bring N bits in compactly?

M, 424: "review all the other open items in the warp theorem map, and close them".  Every open row at the large end
rests on SOURCE (ARRIVAL, M1P2x, E1x, H2tx through one number, the arrival's width), and SOURCE's specification
(SOURCE-REQUIRED.md) asks two things of the carrier at once:
  item 5  exactly N bits, its carrier holding at least 2^N states (136 (5), H-BITS-ARE-STATES), at exactly the README's
          energy E(N) at the bound (item 4; G1, H1: the face holds exactly N bits at E(N));
  item 9  a compact arrival onto the face: within 4.79 clocks of r_h/c at the small end (arrival_small V2-V4), and at
          the large end within 4.31 to 8 clocks at our sigma (focusing_parts F5, item 419) -- or within the junction's
          period where position 2's sigma differs (1.57e-3 clocks at 2P, r0 = 10 ell; junction_own G7).
This instrument asks whether the two can hold together for a carrier made of the plane's fields.  Labels: computed
(exact unless marked), deduced, READ, estimate.  Worked in the conversation; not verified; not seated.

  S1 (computed, exact; standard thermodynamics, not READ here) At fixed energy E in a volume V, the most states a free
     massless carrier of Z degrees of freedom holds is e^S with S = (4/3) (pi^2 Z/30)^(1/4) (V/(hbar c)^3)^(1/4) E^(3/4)
     (the blackbody maximizes entropy at fixed E and V; any other state of the same fields holds fewer).  Everything the
     carrier brings through the face's capture cross-section sigma within a time tau lay, when it set out, in the volume
     sigma c tau swept toward it, so its count of states is at most e^S at V = sigma c tau (an upper bound: an isotropic
     gas there is more than can cross).  So N bits arrive within tau only if N ln2 <= S(E, sigma c tau).
  S2 (computed, exact) Hence the least arrival time for N bits at energy E: tau_min = (3 N ln2/4)^4 (hbar c)^3 /
     ((pi^2 Z/30) E^3 sigma c).  On the plane's four-dimensional hole at the bound (N ln2 = S_BH = pi r0^2/l_P^2, E = M
     c^2, sigma = 27 pi r0^2/4) it is exactly tau_min = (45/4) N ln2/Z clocks of r0/c -- no free number, independent of
     G, hbar and ell.  The README at the bound is the hole's own entropy, and bringing it in takes the time its Hawking
     emission takes to carry it out, up to order one (deduced; close_large L3's life, at least 2.417 N clocks of m/c).
  S3 (computed) The figures.  Small end (the example README, r_h = 1.12e-20 m, N = 2.74e15, E = 1.28098e9 J; the
     carrier on the plane, captured within b_c = 2 r_h, Tangherlini's photon sphere): tau_min = 5.3e15 clocks at Z = 2,
     1.0e14 at Z = 106.75, against the compact 4.79 (and the hole's life, 8.57e14).  Large end at r0 = 20 ell: 5.3e63
     and 9.7e61 clocks (Z = 2, 108.75); at the Earth cap (N* = 1.3651e66): 5.3e66 and 9.8e64 clocks, against the compact
     4.31-8 and the junction's 1.6e-3.
  S4 (computed) What a compact arrival would cost.  Holding N bits within w clocks needs E_c = (3 N ln2/4)^(4/3)
     (hbar c) (30/(pi^2 Z))^(1/3) / (sigma w r_h)^(1/3); against E(N) that is (tau_min/w)^(1/3): 2.8e4 (small end, Z =
     106.75, w = 4.79) and 2.3e21 (Earth cap, Z = 108.75, w = 8).  So a compact README is a README far above the bound:
     the face it forms holds (E_c/E(N))^(3/2) N bits (small end) or (E_c/E(N))^2 N (large), not N (136 (1), 162).
  S5 (deduced) So items 5 and 9 cannot hold together for any carrier of the plane's fields: at E(N) the arrival lasts
     at least tau_min, 13 to 66 orders beyond the compact widths (at the compact width the carrier has room for 4.7e-4
     of the bits at the small end, 1e-16 at the Earth cap); within those widths the energy is 3e4 to 9e21 times E(N).
     Something in the premise set gives: (a) the exact energy at the bound (G1, 133, 136 (1)); (b) the compact
     arrival -- the onset hidden behind the face (arrival_small V2-V4; focusing_parts F5, so O1b and O1c for the
     earliest parts) and, where a junction binds, the emergence within its period (item 10); (c) the carrier: a species
     count Z near Z tau_min/w, 2e15 to 1e66 (H-SPECIES-FINITE's replacement, readings Q27, bounds it far below).
     Which is M's.  RBITS (the bits arriving with the energy) is the reading S5 refutes for a compact arrival, as an
     estimate.

What this does not claim: the bound is free-field thermodynamics with Z species (an estimate in its idealizations: no
interactions, no gravity's own entropy before the face forms); the cross-section is geometric optics, which a carrier
of wavelength above r_h does not obey (S1's thermal README has its peak at 10.5 r0, S6, so the true capacity is lower
still); nothing here is about the read (399), only about the carrier's room.
  S6 (computed, exact) At fixed E and S an ultrarelativistic carrier has kT = (4/3) E/S whatever its volume; at the
     bound that is (8/3) of the hole's Hawking temperature, so its peak wavelength is 10.5 r0 at the large end, at
     every N.

python3 source_capacity.py [--selftest | --mutants]
"""
import os, sys, math, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
_C = {}


def _load(name, alias):
    if alias not in _C:
        spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); _C[alias] = m
    return _C[alias]


def consts():
    PG = _load("p2_gravity.py", "sc_pg")
    return dict(c=PG.C, G=PG.G, hbar=PG.HBAR, h=PG.H, ell=PG.ELL_MAX, ln2=math.log(2))


def s_max(E, V, Z, k):
    """S1: the largest entropy (nats) of a free massless carrier with Z degrees of freedom at energy E in volume V"""
    a = math.pi ** 2 * Z / 30 * (1.0 if "noZ" not in MUT else 30 / math.pi ** 2)
    return 4 / 3 * a ** 0.25 * (V / (k["hbar"] * k["c"]) ** 3) ** 0.25 * E ** 0.75


def tau_min(N, E, sigma, Z, k):
    """S2: the least time for N bits at energy E to cross sigma"""
    a = math.pi ** 2 * Z / 30
    p = 3 if "power3" in MUT else 4
    return (3 * N * k["ln2"] / 4) ** p * (k["hbar"] * k["c"]) ** 3 / (a * E ** 3 * sigma * k["c"])


def exact_4d():
    """S2: tau_min in clocks of r0/c on the plane's hole at the bound, in Planck units"""
    M, Z = sp.symbols("M Z", positive=True)
    S = 4 * sp.pi * M ** 2                       # S_BH = pi r0^2 / l_P^2 with r0 = 2M
    sigma = sp.Rational(27, 4) * sp.pi * (2 * M) ** 2
    a = sp.pi ** 2 * Z / 30
    tau = (3 * S / 4) ** 4 / (a * M ** 3 * sigma)
    return sp.simplify(tau / (2 * M) / (S / Z))  # tau_min / r0 per (N ln2 / Z)


def cases():
    k = consts(); c, G, hbar, ell = k["c"], k["G"], k["hbar"], k["ell"]
    out = {}
    # small end: the example README's five-dimensional hole (G5 = G ell), the carrier on the plane, b_c = 2 r_h
    G5 = G * ell; Es = 1.28098e9
    rh = math.sqrt(8 * G5 * Es / (3 * math.pi * c ** 4))
    l5c = G5 * hbar / c ** 3
    Ns = 2 * math.pi ** 2 * rh ** 3 / (4 * k["ln2"] * l5c)
    sig_s = math.pi * (2 * rh) ** 2
    out["small end"] = dict(N=Ns, E=Es, r=rh, sigma=sig_s, Zs=(2, 106.75), w=4.79)
    # large end: the plane's Schwarzschild hole at the bound, N ln2 = pi r0^2 / l_P^2
    lP2 = hbar * G / c ** 3
    EC = _load("earth_cap.py", "sc_ec").compute()
    for name, r0 in (("r0 = 20 ell", 20 * ell), ("the Earth cap", EC["r0"])):
        N = math.pi * r0 ** 2 / lP2 / k["ln2"]
        E = r0 * c ** 4 / (2 * G)
        out[name] = dict(N=N, E=E, r=r0, sigma=27 * math.pi * r0 ** 2 / 4, Zs=(2, 108.75), w=8.0)
    for name, d in out.items():
        d["tau"] = {Z: tau_min(d["N"], d["E"], d["sigma"], Z, k) * c / d["r"] for Z in d["Zs"]}
        d["Ec_ratio"] = {Z: (d["tau"][Z] / d["w"]) ** (1 / 3) for Z in d["Zs"]}
        d["S_room"] = s_max(d["E"], d["sigma"] * d["w"] * d["r"], d["Zs"][1], k) / (d["N"] * k["ln2"])
    out["the Earth cap"]["N_check"] = EC["N"]
    return out


def wavelength_4d():
    """S6: kT = (4/3) E/S at the bound against Hawking's, and the peak wavelength over r0 (Wien, x = 2.821)"""
    M = sp.symbols("M", positive=True)
    kT = sp.Rational(4, 3) * M / (4 * sp.pi * M ** 2)
    TH = 1 / (8 * sp.pi * M)
    ratio = sp.simplify(kT / TH)
    lam_over_r0 = float(2 * sp.pi / (2.821439372 * kT) / (2 * M))
    return ratio, lam_over_r0


def report():
    print("S2 exact, on the plane's hole at the bound: tau_min = %s x (N ln2 / Z) clocks of r0/c" % exact_4d())
    for name, d in cases().items():
        print("S3 %-14s N = %.4g, E = %.4g J, r = %.4g m: tau_min = %s clocks; compact w = %g; E_c/E(N) = %s; room at "
              "w for %.2g of the bits" % (name, d["N"], d["E"], d["r"],
                                         ", ".join("%.2g (Z = %g)" % (t, Z) for Z, t in d["tau"].items()), d["w"],
                                         ", ".join("%.2g" % v for v in d["Ec_ratio"].values()), d["S_room"]))
    r, lam = wavelength_4d()
    print("S6 the carrier's kT at the bound is %s of Hawking's; peak wavelength %.3g r0" % (r, lam))


def selftest(quiet=False):
    ok = []
    def say(m):
        if not quiet:
            print(m, flush=True)
    e = exact_4d()
    s2 = e == sp.Rational(45, 4)
    ok.append(s2); say("S2 tau_min = (45/4) N ln2 / Z clocks of r0/c, exact: %s (%s)" % (s2, e))
    cs = cases(); sm, tw, ec = cs["small end"], cs["r0 = 20 ell"], cs["the Earth cap"]
    k = consts()
    # the large end's numbers must equal S2's closed form
    closed = lambda d, Z: 45 / 4 * d["N"] * k["ln2"] / Z
    s3 = (abs(sm["r"] / 1.12008e-20 - 1) < 1e-4 and abs(sm["N"] / 2.742e15 - 1) < 2e-3
          and all(abs(d["tau"][Z] / closed(d, Z) - 1) < 1e-9 for d in (tw, ec) for Z in d["Zs"])
          and abs(ec["N"] / ec["N_check"] - 1) < 2e-3 and abs(sm["tau"][2] / 5.3e15 - 1) < 0.05
          and abs(ec["tau"][108.75] / 9.8e64 - 1) < 0.05)
    ok.append(s3); say("S3 the small end's r_h and N reproduced; the large end's tau_min equal to S2's closed form; "
                       "Earth cap N = N*; tau_min %.2g (small, Z = 2), %.2g (Earth cap, Z = 108.75): %s" % (
                           sm["tau"][2], ec["tau"][108.75], s3))
    s5 = (all(min(d["tau"].values()) > 1e12 * d["w"] and d["S_room"] < 1e-3 for d in cs.values() if "N" in d)
          and abs(sm["S_room"] / 4.7e-4 - 1) < 0.05)
    ok.append(s5); say("S5 every case: tau_min above 1e12 times the compact width, the room at that width under 1e-3 of "
                       "the bits: %s" % s5)
    r, lam = wavelength_4d()
    s6 = r == sp.Rational(8, 3) and abs(lam - 10.5) < 0.05
    ok.append(s6); say("S6 kT = (8/3) T_Hawking at the bound, peak wavelength %.2f r0: %s" % (lam, s6))
    return all(ok)


def mutants():
    caught = 0; names = ["noZ", "power3"]
    for m in names:
        MUT.clear(); MUT.add(m)
        try:
            r = selftest(quiet=True)
        except Exception:
            r = False
        caught += not r; print("mutant %-8s %s" % (m, "caught" if not r else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
