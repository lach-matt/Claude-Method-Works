#!/usr/bin/env python3
"""trajectories.py -- DOCKET 68, M-RULINGS item 113 (first of three): how much a destination's trajectories add to the
corridor.  Deduced and computed; not verified; not seated.  Write-up: TRAJECTORIES.md.

M's words (verbatim in the rulings file): item 101.6 "The 12 trajectories also contributed to the size of the corridor
depending on ranked dependency for each trajectory."; item 104(c) "They were proposed by Gemini in the taxonomy paper
... 12 was proposed by Gemini, however, there can certainly be more ... Consider that anything I can observe can be
used as a trajectory, for example my universe or rather my spacetime contains religious ideals and I may want to travel
to a universe where religion was never invented...."; item 23 "the math for the corridor is formed by the 12
trajectories of navigation ... entanglement at 12 criteria".  The twelve are the 12-vector settle.H12 carries
(multiverse_12_vector_taxonomy_v2.pdf): V = [M, R, K, T, CP, alpha_s, Z0, Lambda, G, G_F, G_theta, v].

THE BOARD'S READING (R-CHAIN-RULE, ungraded).  A trajectory adds the information it carries given the trajectories
ranked above it; the corridor's least area grows by 7.24277891e-70 m^2 per bit (chain.py, H-STRONG-BOUND,
H-HORIZON-HOLDS).  With n trajectory bits beside an N-bit README: area share n/(N + n), energy factor sqrt(1 + n/N).

WHAT FOLLOWS THE WORK (item 82)
  T1 RANKING SETS EACH TRAJECTORY'S SHARE, NOT THE TOTAL.  The chain rule H(X1..Xk) = sum H(Xi | X<i) gives the same
     total in every order (computed exactly on a toy joint distribution, H-TOY); only the attribution moves.  A
     trajectory ranked after the ones that fix it adds nothing; ranked first, it carries their information instead.
     So your "ranked dependency" decides who pays, not how much the corridor grows.
  T2 THREE OF THE TWELVE ADD NOTHING ONCE THEIR PARENTS ARE RANKED ABOVE THEM.  settle.H12 (imported) records M and R as
     readouts of alpha (M also of m_e and v) and G_F as 1/(sqrt2 v^2) at tree level; Z0 is alpha itself ("Z0 =
     2 alpha h/e^2").  With Z0 and v ranked above them, R and G_F add 0 bits and M adds only m_e's information
     (H-TREE-LEVEL for G_F).  K and T are material properties, per material -- trajectories of the object or the site,
     not of the universe.  Seven are universe-level and independent as the taxonomy records them: CP, alpha_s, Z0,
     Lambda, G, G_theta, v.
  T3 CONSTANTS AT MEASURABLE PRECISION ARE A NEGLIGIBLE SHARE.  The trajectory bits must reach N (2.74257e15 for the core
     README) before they double the area.  An illustration (H-ILLUSTRATIVE, not a measured figure): 12 x 64 bits gives
     an area share 2.8e-13 and an energy factor 1 + 1.4e-13.  What precision and range each needs is OPEN.
  T4 A WHOLE COUNTERFACTUAL UNIVERSE HAS A CEILING: THE HUBBLE HORIZON.  The most any specification of a universe like
     ours can carry is its horizon's Bekenstein-Hawking count, N_H = pi c^5 / (hbar G H0^2 ln2) = 3.272e122 bits
     (H0 = 67.36 km/s/Mpc, cosmo.py; u_r 1.6e-2).  A corridor sized for it has r_min = c/H0 = 1.3733e26 m and least
     energy c^5 / (2 G H0) = 8.3103e69 J -- a corridor the size of the observable universe (H-HOLOGRAPHIC-CEILING,
     Bousso's covariant bound read as the ceiling, H-STRONG-BOUND).  "A universe where religion was never invented" lies
     between T3 and T4: with your own universe ranked first (H-REFERENCE-UNIVERSE), it adds only what distinguishes the
     destination from yours -- how much is OPEN.

NAMED HYPOTHESES
  M's: H-TWELVE-TRAJECTORIES (101.6), H-TRAJECTORIES-OPEN (104c), H-12Q (item 24: the twelve quantum-correlated).
  The board's: R-CHAIN-RULE; H-TOY (the order-invariance shown on a toy distribution; the theorem is the chain rule);
    H-TREE-LEVEL; H-ILLUSTRATIVE; H-HOLOGRAPHIC-CEILING; H-REFERENCE-UNIVERSE; H-UNIFORM-RANGE (bits = log2(range /
    precision) for a value known to a precision within a range -- the per-trajectory figure, OPEN); chain.py's
    H-STRONG-BOUND, H-HORIZON-HOLDS.

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
    """The board's rule over settle.H12's own text: a readout or a Lagrangian-derived quantity is DEPENDENT; a material
    property is MATERIAL (object- or site-level); anything else is INDEPENDENT (universe-level)."""
    sym, what, klass, carrier = row[0], row[1], row[2], row[3]
    if "readout of" in carrier or klass.startswith("LAGRANGIAN-DERIVED"):
        return "DEPENDENT"
    if klass.startswith("MATERIAL PROPERTY"):
        return "MATERIAL"
    return "INDEPENDENT"


def twelve():
    rows = owners()["settle"].H12
    return [{"symbol": r[0], "what": r[1], "class": r[2], "carrier": r[3], "kind": classify(r)} for r in rows]


# ============================================================================================ T1: the chain rule
def H(p):
    return -sum(v * math.log2(v) for v in p.values() if v > 0)


def marginal(joint, idx):
    out = {}
    for k, v in joint.items():
        kk = tuple(k[i] for i in idx)
        out[kk] = out.get(kk, 0.0) + v
    return out


def chain_terms(joint, order):
    """H(X_order[0]), H(X_order[1] | X_order[0]), ... computed exactly from the joint."""
    terms, prev = [], 0.0
    for i in range(1, len(order) + 1):
        h = H(marginal(joint, order[:i]))
        terms.append(h - prev)
        prev = h
    return terms


def toy_joint(dependent=True):
    """H-TOY: Z0 (alpha) takes 4 values, v takes 3, R is a function of Z0 (a readout), G_F a function of v; with
    dependent=False R and G_F are drawn independently instead (the control)."""
    joint = {}
    pz = [0.4, 0.3, 0.2, 0.1]
    pv = [0.5, 0.3, 0.2]
    for z, v in itertools.product(range(4), range(3)):
        if dependent:
            joint[(z, v, z % 2, v)] = joint.get((z, v, z % 2, v), 0.0) + pz[z] * pv[v]
        else:
            for rr, gg in itertools.product(range(2), range(3)):
                joint[(z, v, rr, gg)] = pz[z] * pv[v] * 0.5 * pv[gg]
    return joint


# ============================================================================================ compute
def compute():
    o = owners()
    ch, cosmo = o["chain"], o["cosmo"]
    co = ch.coefficients()
    seat, fa = ch.owners()["uses"].owners()[0], ch.owners()["uses"].owners()[1]
    core = fa.identity_core()["total_bits"]
    a_bit = co["neck_area_m2_per_bit"]["value"]
    emin = co["E_min_J_per_sqrt_bit"]["value"]
    hbar, c, G, H0 = cosmo._HBAR, seat.C, seat.G, cosmo.H0()
    NH = math.pi * c ** 5 / (hbar * G * H0 ** 2 * math.log(2))
    n_ill = 12 * 64
    tw = twelve()
    jd, ji = toy_joint(True), toy_joint(False)
    orders = [(0, 1, 2, 3), (2, 3, 0, 1), (3, 0, 2, 1)]
    return {
        "twelve": tw,
        "counts": {k: sum(1 for r in tw if r["kind"] == k) for k in ("DEPENDENT", "MATERIAL", "INDEPENDENT")},
        "toy_dependent": {str(od): chain_terms(jd, od) for od in orders},
        "toy_independent": {str(od): chain_terms(ji, od) for od in orders},
        "core_bits": core, "area_per_bit_m2": a_bit, "E_min_per_sqrt_bit_J": emin,
        "illustrative_bits": n_ill, "illustrative_area_share": n_ill / (core + n_ill),
        "illustrative_energy_factor_minus_1": math.sqrt(1 + n_ill / core) - 1,
        "N_H_bits": NH, "r_at_NH_m": co["r_min_m_per_sqrt_bit"]["value"] * math.sqrt(NH), "c_over_H0_m": c / H0,
        "E_at_NH_J": emin * math.sqrt(NH), "hubble_energy_J": c ** 5 / (2 * G * H0),
        "H0_u_r": co["H0_per_s"]["u_r"],
    }


def report(d):
    print("trajectories.py -- item 113: the trajectories' share of the corridor")
    for r in d["twelve"]:
        print("   %-8s %-12s %s | %s" % (r["symbol"], r["kind"], r["class"][:52], r["carrier"][:40]))
    print("   counts: %s" % d["counts"])
    for k, v in d["toy_dependent"].items():
        print("   toy (R = f(Z0), G_F = g(v)) order %s: terms %s, total %.6f" % (k, ["%.4f" % t for t in v], sum(v)))
    print("   illustration %d bits beside the core: area share %.3e, energy factor 1 + %.3e" % (
        d["illustrative_bits"], d["illustrative_area_share"], d["illustrative_energy_factor_minus_1"]))
    print("   Hubble ceiling N_H = %.4e bits: r = %.4e m (c/H0 = %.4e m), E = %.4e J (c^5/2GH0 = %.4e J)" % (
        d["N_H_bits"], d["r_at_NH_m"], d["c_over_H0_m"], d["E_at_NH_J"], d["hubble_energy_J"]))


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
    totals = [sum(v) for v in tdep.values()]
    chk("T1: the chain-rule total is the same in every order (%s)" % ["%.12f" % t for t in totals],
        max(totals) - min(totals) < 1e-12)
    first = tdep[str((0, 1, 2, 3))]
    chk("T1: ranked after their parents, the readouts add nothing (terms %s: the last two are 0)" % (
        ["%.4f" % t for t in first]), abs(first[2]) < 1e-12 and abs(first[3]) < 1e-12)
    moved = tdep[str((2, 3, 0, 1))]
    chk("T1: ranked first, the readouts carry information and their parents pay less (terms %s)" % (
        ["%.4f" % t for t in moved]), moved[0] > 0.1 and moved[1] > 0.1 and moved[2] < tdep[str((0, 1, 2, 3))][0])
    ind = tind[str((0, 1, 2, 3))]
    chk("independent R and G_F add their own information even ranked last (terms %s)" % ["%.4f" % t for t in ind],
        ind[2] > 0.5 and ind[3] > 0.5, ctl=True)
    cts = d["counts"]
    chk("T2: settle.H12 by the board's rule -- %d dependent (M, R, G_F), %d material (K, T), %d independent" % (
        cts["DEPENDENT"], cts["MATERIAL"], cts["INDEPENDENT"]),
        cts == {"DEPENDENT": 3, "MATERIAL": 2, "INDEPENDENT": 7} and
        sorted(r["symbol"] for r in d["twelve"] if r["kind"] == "DEPENDENT") == ["G_F", "M", "R"])
    mutated = classify(("R", "x", "EMERGENT", "none", "", "", ""))
    chk("the rule reads the text: R with its 'readout of' carrier removed is no longer dependent (%s)" % mutated,
        mutated == "INDEPENDENT", ctl=True)
    structural.append("T3: %d illustrative bits beside the core's %.6e: area share %.3e, energy factor 1 + %.3e "
                      "(closed form n/(N+n), sqrt(1+n/N); H-ILLUSTRATIVE)" % (
                          d["illustrative_bits"], d["core_bits"], d["illustrative_area_share"],
                          d["illustrative_energy_factor_minus_1"]))
    structural.append("T4: at the Hubble ceiling N_H = pi c^5/(hbar G H0^2 ln2) = %.6e bits the floor's radius is "
                      "%.6e m against c/H0 = %.6e m and its energy %.6e J against c^5/(2 G H0) = %.6e J -- one formula "
                      "(u_r %.1e from H0)" % (d["N_H_bits"], d["r_at_NH_m"], d["c_over_H0_m"], d["E_at_NH_J"],
                                              d["hubble_energy_J"], 2 * d["H0_u_r"]))
    structural.append("the per-trajectory bits need a precision and a range for each value (H-UNIFORM-RANGE): OPEN")
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
