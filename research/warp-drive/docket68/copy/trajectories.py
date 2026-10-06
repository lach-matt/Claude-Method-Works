#!/usr/bin/env python3
"""trajectories.py -- DOCKET 68, M-RULINGS item 113 (first of three): how much a destination's trajectories add to the
corridor.  Deduced and computed; verified once (findings applied, History); not seated.  Write-up: TRAJECTORIES.md.
First headed "...; not verified; not seated."

M'S WORDS (verbatim in the rulings file)
  101.6 "The 12 trajectories also contributed to the size of the corridor depending on ranked dependency for each
  trajectory."  104(c) "They were proposed by Gemini in the taxonomy paper in the warp folder of Google drive. They are
  based on quantum physics forces that help define the geometric shape iof any object. 12 was proposed by Gemini,
  however, there can certainly be more ... Consider that anything I can observe can be used as a trajectory, for example
  my universe or rather my spacetime contains religious ideals and I may want to travel to a universe where religion was
  never invented...."  23 "the math for the corridor is formed by the 12 trajectories of navigation. Each one is a
  physics condition that governs an aspect of the reconstruction at seating. These 12 allow for the predetermination of
  seat compatibility based on the starting state - entanglement at 12 criteria."  24 "The 12 conditions only need to
  supply enough for the object to reconstruct in the new environment".  25 "this is where the magnitude of
  probabilities (negative and positive), and complex binary come into play. The stronger negative magnitudes will
  automatically triangulate the stronger positive magnitudes which rank the probability of seating".  The twelve are
  settle.H12's 12-vector (multiverse_12_vector_taxonomy_v2.pdf): V = [M, R, K, T, CP, alpha_s, Z0, Lambda, G, G_F,
  G_theta, v]; only H12's first column is the taxonomy's, the class and carrier columns are the board's.

THE BOARD'S READING (R-CHAIN-RULE, ungraded, under H-CLASSICAL-SHANNON) AND ITS TENSION WITH YOUR SENTENCE
  A trajectory adds the information it carries given those ranked above it.  With n trajectory bits held with the README
  (H-TRAJECTORIES-IN-README) the corridor's least area grows by 2 h G ln2/(pi c^3) = 4 hbar G ln2/c^3 = 7.24277891e-70
  m^2 per bit and its least energy is sqrt(hbar c^5 ln2 / (4 pi G)) x sqrt(N + n) = 4.59404002e8 J x sqrt(N + n)
  (chain.py; H-STRONG-BOUND, H-HORIZON-HOLDS): area share n/(N + n), energy share ~ n/(2N) for n << N.  Under this
  reading the TOTAL does not depend on the ranking -- your sentence says the size does.  Two readings of yours would make
  it depend: ranking by signed or complex magnitudes (item 25, H-SEATRANK), or a stopping rule, taking trajectories in
  rank order "only ... enough" (item 24, H-STOP-WHEN-ENOUGH).  Asked.

WHAT FOLLOWS THE WORK (item 82)
  T1 CLASSICALLY, RANKING MOVES WHO CARRIES THE INFORMATION.  On a toy joint (H-TOY): readouts ranked after their parents
     add 0; ranked first, they carry information and their parents carry less (computed); the total is the same in every
     order (an identity of H(joint), STRUCTURAL).  Control: independent readouts add their own information ranked last.
  T1q QUANTUM-CORRELATED TRAJECTORIES CAN SUBTRACT (YOUR ITEM 24, H-12Q).  If the twelve are literally quantum-
     correlated, each term is a von Neumann conditional entropy, which can be negative: for a maximally entangled pair,
     S(B|A) = -1 bit (computed); a trajectory ranked after its entangled partner LOWERS the count.  Control: a product
     state gives S(B|A) = S(B) >= 0.  A candidate meaning of your "negative magnitudes" (item 25) -- the board's reading.
  T2 TWO OF THE TWELVE ADD NOTHING ONCE THEIR PARENTS RANK ABOVE THEM; ONE ADDS AT MOST A LITTLE.  By H12's carrier text
     (the board's rule, tuned to the twelve rows -- Z0's "DERIVED:" escapes it, rightly, since Z0 is alpha): R (a readout
     of alpha, via Z0) adds 0; G_F (1/(sqrt2 v^2), H-TREE-LEVEL) adds 0; M (a readout of alpha and m_e, inheriting alpha
     and v) adds at most H(m_e | alpha, v), and m_e is not one of the twelve -- how much is OPEN.  K and T are material
     properties: trajectories of the object or the site, which is what you say the trajectories are ("help define the
     geometric shape of any object"); their bits per object and site are OPEN.  Seven have no dependence recorded in H12
     (H-NO-RECORDED-DEPENDENCE): CP, alpha_s, Z0, Lambda, G, G_theta, v -- not shown independent; H12 ties CP to the
     Higgs-Yukawa sector (v's field), and under your H-UNIVERSAL-ENTANGLEMENT their mutual information is presumed
     non-zero until refuted.
  T3 BELOW A COMPUTED THRESHOLD THE TRAJECTORIES ARE A NEGLIGIBLE SHARE.  The area share stays below 1e-6 while
     n < 1e-6 N: 2.742570e9 bits for the core README.  Illustration (H-ILLUSTRATIVE): the nine trajectories T2 does not set
     to zero, at 64 bits each, give an area share 2.1e-13 and an energy share 1.05e-13.
  T4 A BOUNDARY, NOT A CORRIDOR: THE HUBBLE-RADIUS COUNT.  The Bekenstein-Hawking count of the Hubble sphere,
     N_H = pi c^5 / (hbar G H0^2 ln2) = 3.272224e122 bits (u_r 1.6e-2), sized by the asymptotically flat floor, gives
     r = c/H0 = 1.373312e26 m and E = c^5/(2 G H0) = 8.310292e69 J (each u_r 8.0e-3) -- exactly the critical-density
     mass-energy of the Hubble sphere, (4 pi/3)(c/H0)^3 (3 H0^2 / 8 pi G) c^2 (computed).  But (i) c/H0 is the apparent
     horizon only in flat FRW (H-FLAT-FRW-APPARENT-HORIZON); (ii) with Lambda > 0 the asymptotic de Sitter count is larger,
     N_H / Omega_Lambda = 4.779e122 bits (Omega_Lambda = 0.6847, Planck 2018, NOT READ); (iii) the board grades Bousso's
     covariant bound NARROWED -- a conjecture, outside NEC-violating matter (VERIFIED-GRADES.tsv), and the corridor reads
     NEC-violating (H-BOUSSO-CONJECTURE); (iv) with our Lambda no black-hole horizon exceeds 1/sqrt(Lambda) = 0.698 c/H0
     (Schwarzschild-de Sitter, computed, the Nariai source NOT READ), so a corridor of horizon radius c/H0 cannot exist
     here (H-ASYMPTOTICALLY-FLAT breaks); (v) a counterfactual universe has its own H0 and Lambda (H-SAME-H0); and
     H-PLANCK-H0 (SH0ES's larger H0, NOT READ, would move N_H by about 15%).  "A universe where religion was never
     invented" lies between T3 and T4: with your own universe as the starting state (item 23, H-REFERENCE-UNIVERSE), it
     adds what distinguishes the destination from yours -- OPEN.
  T5 THE TRAJECTORIES RIDE THE README.  Under H-TRAJECTORIES-IN-README they cross with it through your three holds (item
     106), and the trip is one E_min(N + n) delivered into position 2's build (items 110, 111).  Monogamy (ENTANGLE.md,
     Horodecki p.8) under H-12Q and H-HOLD-IS-ENTANGLE: degrees of freedom maximally entangled as the README's bridge
     cannot also carry the twelve criteria's correlations, so n adds to N rather than sharing it.

NAMED HYPOTHESES
  M's: H-TWELVE-TRAJECTORIES (101.6), H-TRAJECTORIES-OPEN (104c), H-12Q (24), H-SEATRANK (25), H-UNIVERSAL-ENTANGLEMENT
    (100), H-REFERENCE-UNIVERSE (23, "based on the starting state").
  The board's: R-CHAIN-RULE, H-CLASSICAL-SHANNON, H-STOP-WHEN-ENOUGH (a reading of 24); H-TOY; H-TREE-LEVEL;
    H-NO-RECORDED-DEPENDENCE; H-ILLUSTRATIVE; H-TRAJECTORIES-IN-README; H-FLAT-FRW-APPARENT-HORIZON; H-BOUSSO-CONJECTURE;
    H-ASYMPTOTICALLY-FLAT; H-SAME-H0; H-PLANCK-H0; H-UNIFORM-RANGE; chain.py's H-STRONG-BOUND, H-HORIZON-HOLDS.

HISTORY (verifier, 2026-10-06; first-written claims kept in TRAJECTORIES.md)
  The order-invariance check was an identity (now STRUCTURAL); the mutated-row control used a hand-made row (now the
  real H12 row, mutated); "three of the twelve add nothing" contradicted "M adds only m_e's information" (two add
  nothing; M at most H(m_e | alpha, v)); "independent as the taxonomy records them" over-read H12 and bent item 100;
  R-CHAIN-RULE's ranking-independence was stated as yours without flagging your sentence; the quantum case, K and T as
  trajectories, the ceiling's scope (apparent horizon, de Sitter, Bousso NARROWED, Schwarzschild-de Sitter), the
  per-quantity u_r, the closed forms, the threshold, the README's three holds and monogamy were missing; "the size of
  the observable universe" was the Hubble radius; the illustration counted the zero trajectories.

USAGE
    python3 trajectories.py | --selftest | --json
"""

import contextlib
import importlib.util
import io
import itertools
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
_CACHE = {}
OMEGA_LAMBDA_NOT_READ = 0.6847      # Planck 2018 (NOT READ here): used only for the de Sitter boundary line


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


def owners():
    """Imported, never copied: chain.py (the floor, its constants), settle.py (H12), cosmo.py (H0)."""
    if not _CACHE:
        _CACHE["chain"] = _load(os.path.join(HERE, "chain.py"), "copy_chain_traj")
        _CACHE["settle"] = _load(os.path.join(D68, "settle.py"), "d68_settle_traj")
        _CACHE["cosmo"] = _load(os.path.join(WD, "cosmo.py"), "wd_cosmo_traj")
    return _CACHE


# ============================================================================================ T2: the twelve
def classify(row):
    """The board's rule over settle.H12's carrier and class text (tuned to its twelve rows): a readout or a
    Lagrangian-derived quantity is DEPENDENT; a material property is MATERIAL (object- or site-level); otherwise
    NO-RECORDED-DEPENDENCE."""
    klass, carrier = row[2], row[3]
    if "readout of" in carrier or klass.startswith("LAGRANGIAN-DERIVED"):
        return "DEPENDENT"
    if klass.startswith("MATERIAL PROPERTY"):
        return "MATERIAL"
    return "NO-RECORDED-DEPENDENCE"


def twelve(rows=None):
    rows = owners()["settle"].H12 if rows is None else rows
    return [{"symbol": r[0], "what": r[1], "class": r[2], "carrier": r[3], "kind": classify(r)} for r in rows]


def counts(tw):
    return {k: sum(1 for r in tw if r["kind"] == k) for k in ("DEPENDENT", "MATERIAL", "NO-RECORDED-DEPENDENCE")}


# ============================================================================================ T1: classical
def H(p):
    return -sum(v * math.log2(v) for v in p.values() if v > 0)


def marginal(joint, idx):
    out = {}
    for k, v in joint.items():
        kk = tuple(k[i] for i in idx)
        out[kk] = out.get(kk, 0.0) + v
    return out


def chain_terms(joint, order):
    terms, prev = [], 0.0
    for i in range(1, len(order) + 1):
        h = H(marginal(joint, order[:i]))
        terms.append(h - prev)
        prev = h
    return terms


def toy_joint(dependent=True):
    """H-TOY: Z0 (alpha) 4 values, v 3 values; R = Z0 mod 2 (a lossy readout), G_F a function of v; independent=False
    draws R and G_F independently (the control)."""
    joint = {}
    pz, pv = [0.4, 0.3, 0.2, 0.1], [0.5, 0.3, 0.2]
    for z, v in itertools.product(range(4), range(3)):
        if dependent:
            joint[(z, v, z % 2, v)] = joint.get((z, v, z % 2, v), 0.0) + pz[z] * pv[v]
        else:
            for rr, gg in itertools.product(range(2), range(3)):
                joint[(z, v, rr, gg)] = pz[z] * pv[v] * 0.5 * pv[gg]
    return joint


# ============================================================================================ T1q: quantum
def vn_bits(rho):
    import numpy as np
    w = np.linalg.eigvalsh(rho)
    w = w[w > 1e-15]
    return float(-np.sum(w * np.log2(w)))


def conditional_entropy(psi):
    """S(B|A) = S(AB) - S(A) for a two-qubit state vector."""
    import numpy as np
    rho = np.outer(psi, psi.conj())
    rA = np.einsum("ijkj->ik", rho.reshape(2, 2, 2, 2))
    return vn_bits(rho) - vn_bits(rA)


def quantum_cases():
    import numpy as np
    bell = np.array([1, 0, 0, 1], dtype=complex) / math.sqrt(2)
    plus = np.array([1, 1], dtype=complex) / math.sqrt(2)
    zero = np.array([1, 0], dtype=complex)
    product = np.kron(zero, plus)
    return {"bell_S_B_given_A": conditional_entropy(bell), "product_S_B_given_A": conditional_entropy(product)}


# ============================================================================================ compute
def compute():
    o = owners()
    ch, cosmo = o["chain"], o["cosmo"]
    co = ch.coefficients()
    seat, fa = ch.owners()["uses"].owners()[0], ch.owners()["uses"].owners()[1]
    core = fa.identity_core()["total_bits"]
    hbar, c, G, H0 = cosmo._HBAR, seat.C, seat.G, cosmo.H0()
    NH = math.pi * c ** 5 / (hbar * G * H0 ** 2 * math.log(2))
    lam = 3 * OMEGA_LAMBDA_NOT_READ * H0 ** 2 / c ** 2
    n_ill = 9 * 64
    tw = twelve()
    rows = [list(r) for r in owners()["settle"].H12]
    for r in rows:
        if r[0] == "R":
            r[3] = "none"                                    # strip R's recorded "readout of alpha"
    jd, ji = toy_joint(True), toy_joint(False)
    orders = [(0, 1, 2, 3), (2, 3, 0, 1), (3, 0, 2, 1)]
    hub_mass_energy = (4 * math.pi / 3) * (c / H0) ** 3 * (3 * H0 ** 2 / (8 * math.pi * G)) * c ** 2
    return {
        "twelve": tw, "counts": counts(tw), "counts_R_stripped": counts(twelve(rows)),
        "toy_dependent": {str(od): chain_terms(jd, od) for od in orders},
        "toy_independent": {str(od): chain_terms(ji, od) for od in orders},
        "quantum": quantum_cases(),
        "core_bits": core, "area_per_bit_m2": co["neck_area_m2_per_bit"]["value"],
        "E_min_per_sqrt_bit_J": co["E_min_J_per_sqrt_bit"]["value"],
        "threshold_bits_1e-6": 1e-6 * core,
        "illustrative_bits": n_ill, "illustrative_area_share": n_ill / (core + n_ill),
        "illustrative_energy_share": math.sqrt(1 + n_ill / core) - 1, "illustrative_energy_share_approx": n_ill / (2 * core),
        "N_H_bits": NH, "c_over_H0_m": c / H0, "E_at_NH_J": co["E_min_J_per_sqrt_bit"]["value"] * math.sqrt(NH),
        "hubble_energy_J": c ** 5 / (2 * G * H0), "hubble_critical_mass_energy_J": hub_mass_energy,
        "de_sitter_bits_NOT_READ": NH / OMEGA_LAMBDA_NOT_READ,
        "max_bh_horizon_over_c_over_H0": (1 / math.sqrt(lam)) / (c / H0),
        "H0_u_r": co["H0_per_s"]["u_r"],
    }


def report(d):
    print("trajectories.py -- item 113: the trajectories' share of the corridor")
    for r in d["twelve"]:
        print("   %-8s %-24s %s | %s" % (r["symbol"], r["kind"], r["class"][:46], r["carrier"][:36]))
    print("   counts: %s" % d["counts"])
    for k, v in d["toy_dependent"].items():
        print("   toy order %s: terms %s, total %.6f" % (k, ["%.4f" % t for t in v], sum(v)))
    q = d["quantum"]
    print("   quantum: S(B|A) Bell pair %.4f bit; product state %.4f bit" % (q["bell_S_B_given_A"],
                                                                         q["product_S_B_given_A"]))
    print("   threshold for a 1e-6 area share: %.6e bits; illustration %d bits: area %.3e, energy %.3e" % (
        d["threshold_bits_1e-6"], d["illustrative_bits"], d["illustrative_area_share"], d["illustrative_energy_share"]))
    print("   boundary: N_H %.6e bits, r = c/H0 %.6e m, E %.6e J (critical mass-energy %.6e J); de Sitter %.4e bits "
          "(Omega_L NOT READ); largest SdS horizon %.3f c/H0" % (
              d["N_H_bits"], d["c_over_H0_m"], d["E_at_NH_J"], d["hubble_critical_mass_energy_J"],
              d["de_sitter_bits_NOT_READ"], d["max_bh_horizon_over_c_over_H0"]))


def selftest(d):
    n_pass = n_fail = n_ctl = n_con = 0
    structural = []

    def chk(label, ok, ctl=False, contrast=False):
        nonlocal n_pass, n_fail, n_ctl, n_con
        tag = "CONTROL: " if ctl else ("CONTRAST: " if contrast else "")
        print("  %s %s%s" % ("ok  " if ok else "FAIL", tag, label))
        n_pass += bool(ok)
        n_fail += not ok
        n_ctl += bool(ctl)
        n_con += bool(contrast)

    tdep, tind = d["toy_dependent"], d["toy_independent"]
    first, moved = tdep[str((0, 1, 2, 3))], tdep[str((2, 3, 0, 1))]
    chk("T1: ranked after their parents, the readouts add nothing (terms %s)" % ["%.4f" % t for t in first],
        abs(first[2]) < 1e-12 and abs(first[3]) < 1e-12)
    chk("T1: ranked first, the readouts carry information and their parents carry less (terms %s)" % (
        ["%.4f" % t for t in moved]), moved[0] > 0.1 and moved[1] > 0.1 and moved[2] < first[0])
    ind = tind[str((0, 1, 2, 3))]
    chk("independent readouts add their own information even ranked last (terms %s)" % ["%.4f" % t for t in ind],
        ind[2] > 0.5 and ind[3] > 0.5, ctl=True)
    q = d["quantum"]
    chk("T1q: under H-12Q a trajectory ranked after its entangled partner subtracts: S(B|A) = %.6f bit for a Bell pair" %
        q["bell_S_B_given_A"], abs(q["bell_S_B_given_A"] + 1) < 1e-9)
    chk("a product state gives S(B|A) = S(B) = %.6f >= 0" % q["product_S_B_given_A"],
        q["product_S_B_given_A"] > -1e-12, ctl=True)
    cts, cs = d["counts"], d["counts_R_stripped"]
    chk("T2: settle.H12 by the board's rule -- %d dependent (M, R, G_F), %d material (K, T), %d with no recorded "
        "dependence" % (cts["DEPENDENT"], cts["MATERIAL"], cts["NO-RECORDED-DEPENDENCE"]),
        cts == {"DEPENDENT": 3, "MATERIAL": 2, "NO-RECORDED-DEPENDENCE": 7} and
        sorted(r["symbol"] for r in d["twelve"] if r["kind"] == "DEPENDENT") == ["G_F", "M", "R"])
    chk("the real H12 row for R with its 'readout of alpha' stripped moves R out of the dependent set (%s)" % cs,
        cs["DEPENDENT"] == 2 and cs["NO-RECORDED-DEPENDENCE"] == 8, ctl=True)
    structural.append("T4: c^5/(2 G H0) = %.9e J equals the Hubble sphere's critical-density mass-energy %.9e J -- an "
                      "algebraic identity" % (d["hubble_energy_J"], d["hubble_critical_mass_energy_J"]))
    chk("T4 boundary: with our Lambda no black-hole horizon reaches c/H0 (largest %.4f c/H0; Schwarzschild-de Sitter, "
        "Omega_Lambda NOT READ)" % d["max_bh_horizon_over_c_over_H0"], d["max_bh_horizon_over_c_over_H0"] < 1)
    tot = [sum(v) for v in tdep.values()]
    structural.append("T1: the chain-rule total is %s in every order -- an identity of H(joint) (first counted)" % (
        ["%.12f" % t for t in tot]))
    structural.append("T3: area share < 1e-6 while n < %.6e bits; the illustration (%d bits) gives area %.4e, energy "
                      "%.4e (~ n/2N = %.4e)" % (d["threshold_bits_1e-6"], d["illustrative_bits"],
                                                d["illustrative_area_share"], d["illustrative_energy_share"],
                                                d["illustrative_energy_share_approx"]))
    structural.append("T4: N_H = %.6e bits (u_r %.1e), r = c/H0 = %.6e m and E = %.6e J (u_r %.1e each) -- the floor's "
                      "formula at N_H (one formula); de Sitter count %.4e bits (Omega_Lambda NOT READ)" % (
                          d["N_H_bits"], 2 * d["H0_u_r"], d["c_over_H0_m"], d["E_at_NH_J"], d["H0_u_r"],
                          d["de_sitter_bits_NOT_READ"]))
    structural.append("closed forms: area per bit 2 h G ln2/(pi c^3) = %.9e m^2; E_min per sqrt(bit) sqrt(hbar c^5 ln2/"
                      "(4 pi G)) = %.9e J" % (d["area_per_bit_m2"], d["E_min_per_sqrt_bit_J"]))
    structural.append("the per-trajectory bits need a precision and a range each (H-UNIFORM-RANGE): OPEN")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("trajectories.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted"
          % (n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
    return n_fail == 0


def main(argv):
    d = compute()
    if "--json" in argv:
        print(json.dumps(d, indent=1, default=str))
        return 0
    if "--selftest" in argv:
        return 0 if selftest(d) else 1
    report(d)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
