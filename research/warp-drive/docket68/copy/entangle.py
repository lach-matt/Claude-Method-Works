#!/usr/bin/env python3
"""entangle.py -- DOCKET 68, M-RULINGS item 100: "Consider that until refuted everything is entangled to everything,
however, the entanglements can range/differ in characterization."  What follows from it along the chain (chain.py,
item 96).  Deduced, computed and READ; verified once (findings applied, History); SEATED (ledger.py section 8o).  Write-up: ENTANGLE.md.
First headed "...; not verified; not seated."

M's hypothesis, carried as given, never as a result:
  H-UNIVERSAL-ENTANGLEMENT  every system is entangled with every other, until a refutation; the entanglements
                            range/differ in characterization (the board's gloss: in degree and in kind).

WHAT FOLLOWS THE WORK (item 82: lead with what passes)
  E1 YOUR SECOND CLAUSE FOLLOWS FROM YOUR FIRST, AND BOTH HAVE READ SUPPORT.  Monogamy (Horodecki et al., READ: "no
     system can be EPR correlated with two systems at the same time", p.8; sec. XVI p.72) means that if everything is
     entangled with everything the entanglements cannot all be strong: they must range.  The kinds differ too (p.6:
     "free entanglement that can be distilled and the bound one"; "inequivalent types of multipartite entanglement").
     For field regions the vacuum is entangled at every separation (vacuum.py, R1/R2 READ there: "arbitrarily far-apart
     regions"); at a FIXED probe window its degree falls faster than any power of the distance (vacuum.gauss_scaling,
     imported), while with a window scaled to the distance it does not fall (vacuum.py: "a fixed negativity at any L
     needs a window T proportional to L").
  E2 THE PRIOR CONNECTION IS THE UNIVERSE'S, UNDER R-ENTANGLED-SETUP.  chain.py's WELL-POSED clause bars a corridor made
     with no prior connection; if pre-shared entanglement counts as one (item 99's R-ENTANGLED-SETUP, named here
     H-ENTANGLEMENT-IS-SETUP), every pair of places has one under item 100.  That is by the encoding (STRUCTURAL).  A
     made corridor is then consistent only where the entanglement already there reaches N (z3): with less, local making
     is inconsistent, so under item 100 "made" and "found" meet.
  E3 THE CORRIDOR'S NECK IS THE AREA OF N EBITS -- ONE FORMULA, NOT TWO ROUTES.  Ryu-Takayanagi's area law (READ: eq.
     1.5 p.1, "we propose the following 'area law'"; its normalization "is fixed from Eq. (1.1)", Bekenstein-Hawking,
     p.4; the two-sided case, "the AdS black hole can be dual to an entanglement of two different CFTs", p.4) gives
     N ebits a least area 4 ln2 G hbar N / c^3 = 2 h G ln2 N / (pi c^3) = 7.24277891e-70 m^2 x N.  chain.py's neck is
     the same number necessarily: Bekenstein's bound saturated at the Schwarzschild radius is the Bekenstein-Hawking
     area law.  Read with ER=EPR (Maldacena-Susskind, READ in geometry.py) and H-HOLD-IS-ENTANGLE, the neck that holds
     an N-bit README has the area of N ebits.
  E4 WHAT WIDENING NEEDS (z3, with the source's own qualifier).  Entanglement "can not be increased on average when
     systems are not in direct contact but distributed in spatially separated regions" (Horodecki, READ, p.4).  So:
     a corridor found with >= N ebits holds the README with the device acting locally; widening a thinner one
     DETERMINISTICALLY by local action is inconsistent; a HERALDED local widening succeeds with probability at most
     E_exist / N (z3: p = 1/2 consistent, p = 0.6 not, at E_exist = N/2).  Across the cut a quantum carrier adds at most
     what it carries (Horodecki sec. XV.J p.71, "How much can entanglement increase under communication of one qubit?";
     Chen-Yang quant-ph/0006051, title READ in the reference list: "at most" one ebit per qubit) -- so widening N/2
     needs N/2 qubits carried, comparable to the README itself.  M's H-UNIDENTIFIED-CARRIER is carried unbounded.
  E5 ONLY THE CROSSING NEEDS YOUR CARRIER.  Widening across the cut can be ordinary physics done BEFORE the joining
     (a quantum carrier at <= c, or swapping through the entanglement already everywhere), at a lead time >= L/c,
     consistent with H-PRIOR-SETUP and H-INSTANTANEOUS.  The README's crossing at trip time is what H-UNIDENTIFIED-CARRIER
     must do.  ER=EPR's bridges are non-traversable (MS fn.1); your corridor (H-IDENTIFY, "two places made one") is not
     claimed to be one of them -- the step from bridge to your corridor is wall 9, OPEN (candidate READ, not done:
     Gao-Jafferis-Wall 1608.05687, Maldacena-Stanford-Yang 1704.05333, bridges made traversable by a coupling).

WHAT IS RULED OUT, AS THE BOUNDARY
  * Deterministic local widening of a bridge thinner than the README; heralded local widening above E_exist / N.
  * Weak entanglement as classical geometry: pair bridges are "Planckian" and "probably" not classical (MS p.17), and
    geometry likely fails "before the entanglement is strictly zero" (Van Raamsdonk fn.1), both READ in geometry.py.
    Whether a found throat is classical is OPEN -- wall 3's quantity.
  * If near-maximal pairs were needed (H-NEARMAX) rather than entropy, concentration needs at least one classical message
    after the window, L/c = 1.340e8 s for Proxima (vacuum.window_free_floor) -- prior setup, not a delay of the teleport.

NAMED HYPOTHESES
  M's: H-UNIVERSAL-ENTANGLEMENT (100); H-UNIDENTIFIED-CARRIER (90); H-COMMON-THROATS, H-MADE (86.3);
    H-SINGLE-CHANNEL-GROWS (94); H-POSITION-BUILDS (91); H-IDENTIFY (95); H-INSTANTANEOUS (94).
  The board's: H-ER=EPR (MS's conjecture, "speculation" p.2); H-RT-HERE (the area law, proposed for AdS_{d+2}, applied
    here); H-SI-RESTORE (S/k_B = A c^3/(4 G hbar)); H-HOLD-IS-ENTANGLE (the bits a neck holds are counted as the ebits it
    carries -- entanglement "does not carry information itself", Horodecki p.4); H-ENTROPY-COUNTS (pure-state
    entanglement entropy is the measure; H-NEARMAX the alternative); H-ENTANGLEMENT-IS-SETUP (= R-ENTANGLED-SETUP);
    H-CUT; H-LOCC; H-POSITION-OPERATES (position 2 performs whatever quantum operations a protocol needs -- an extension
    of H-POSITION-BUILDS); H-SUBADD (the per-qubit bound, via Chen-Yang's title; the proof NOT READ); chain.py's
    H-NECK-HOLDS, H-STRONG-BOUND; vacuum.py's H-UDW, H-PERTURB, H-MINK-VAC, H-SPACELIKE (E1's field scope; rows with
    beta < 7 are "communication not excluded" there).

HISTORY (verifier, 2026-10-06; first-written claims kept)
  * E3 was counted as a check, "EXACTLY the neck chain.py found by a different route": the two are one formula (RT p.4
    fixes its normalization from Bekenstein-Hawking) -- now STRUCTURAL.  The per-nat "control" was ln2 by definition --
    STRUCTURAL.  E2's "clears WELL-POSED with no setup" was by the encoding and needed >= N already present -- STRUCTURAL,
    with the collapse of made into found shown.  The "without UE" control forced the negation of the escape: relabelled
    a control on PriorConnection (UE one source, H-PRIOR-SETUP another).
  * LOCC-MONOTONE was "LocalOnly -> E_added <= 0" (single run): the source says "on average"; now the expectation, with
    heralded widening.  CARRIER said "nothing bounds what it adds": a quantum carrier is bounded per qubit; M's carrier
    stays unbounded.  HOLDS was a biconditional: now one-way, under H-HOLD-IS-ENTANGLE.
  * E5 was "the two open needs land on one hypothesis": widening can be prior setup; only the crossing needs the carrier.
    "Found throats are the bridges of the entanglement already there" ignored MS p.17 / VR fn.1.  "Differ in
    characterization is the fall with distance" dropped vacuum.py's window qualifier and the kinds; monogamy omitted.
    The exact form printed "0" (nsimplify).
"""

import contextlib
import importlib.util
import io
import json
import math
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
_CACHE = {}


def _load(name, path, key):
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
    """Imported, never copied: chain.py (the chain and its M-COEFF table), vacuum.py (the field's entanglement)."""
    if not _CACHE:
        _CACHE["chain"] = _load("chain", os.path.join(HERE, "chain.py"), "copy_chain_entangle")
        _CACHE["vacuum"] = _load("vacuum", os.path.join(D68, "vacuum.py"), "d68_vacuum_entangle")
    return _CACHE


# ============================================================================================ READ here
RT_READ = {
    "source": "Ryu & Takayanagi, 'Holographic Derivation of Entanglement Entropy from AdS/CFT', hep-th/0603001v2",
    "route": "arXiv PDF via Firecrawl (pp.1-3) and alphaXiv (pp.1-5), 2026-10-06",
    "eq_1_5": "S_A = Area of gamma_A / (4 G_N^(d+2)), p.1: 'we propose the following area law'; gamma_A the d "
              "dimensional static minimal surface in AdS_{d+2} whose boundary is the boundary of A",
    "eq_1_1": "S_BH = Area of horizon / (4 G_N), p.1",
    "p2": "'The minimal surface provides the severest entropy bound when we fix its boundary condition. In our case it "
          "saturates the bound.'",
    "p4_norm": "'In a sense, the overall normalization in Eq. (1.5) is fixed from Eq. (1.1) once we consider the "
               "entanglement entropy at finite temperature.'",
    "p4_two_sided": "'the AdS black hole can be dual to an entanglement of two different CFTs at the two boundaries. ... "
                    "we may think the black hole entropy is the same as the entanglement entropy of the CFTs as the "
                    "minimal surface wrap the horizon.'",
    "scope": "AdS_{d+2} / CFT_{d+1}, a proposal shown for d = 1 and compared for general d (abstract); natural units",
}

HORODECKI_READ = {
    "source": "Horodecki x4, 'Quantum entanglement', quant-ph/0702225v2",
    "route": "arXiv PDF via Firecrawl and alphaXiv, 2026-10-06",
    "p4_average": "'it can not be increased on average when systems are not in direct contact but distributed in "
                  "spatially separated regions'",
    "p4_no_info": "entanglement is a resource 'which, though does not carry information itself, can help'",
    "p6_free": "'local operations and classical communication (LOCC), both of which cannot bring in entanglement for free'",
    "p6_kinds": "'there is free entanglement that can be distilled and the bound one'; 'inequivalent types of "
                "multipartite entanglement have been identified'",
    "p8_monogamy": "'no system can be EPR correlated with two systems at the same time'",
    "p71_heading": "sec. XV.J 'How much can entanglement increase under communication of one qubit?' (contents, p.2)",
    "chen_yang_title": "Chen & Yang, quant-ph/0006051, 'Transmitting one qubit can increase one ebit between two parties "
                       "at most' (reference list, p.98) -- title READ, proof NOT READ",
}


# ============================================================================================ E3: the area of N ebits
def rt_area_per_ebit():
    """H-RT-HERE with H-SI-RESTORE: one ebit (S = k_B ln2) has least area 4 ln2 G hbar / c^3 (M-COEFF: h, c exact,
    G measured).  The same closed form as chain.py's neck per bit (one formula)."""
    import sympy as sp
    co = owners()["chain"].coefficients()
    o = owners()["chain"].owners()
    seat = o["uses"].owners()[0]
    cosmo = o["cosmo"]
    h = sp.Rational("%.8e" % (cosmo._HBAR * 2 * math.pi))
    c = sp.Integer(int(seat.C))
    G = sp.Rational(repr(seat.G))
    hbar = h / (2 * sp.pi)
    per_ebit = 4 * sp.log(2) * G * hbar / c ** 3
    exact = str(sp.simplify(per_ebit))
    assert exact != "0"
    return {"form": "A per ebit = 4 ln2 G hbar / c^3 = 2 h G ln2 / (pi c^3)", "exact": exact,
            "value": float(sp.N(per_ebit, 20)), "chain_neck_area_per_bit": co["neck_area_m2_per_bit"]["value"],
            "u_r": co["neck_area_m2_per_bit"]["u_r"]}


# ============================================================================================ E2, E4: z3
CLAUSES = [
    ("UNIVERSAL", "UE -> E_exist > 0 & PriorConnection", "M's H-UNIVERSAL-ENTANGLEMENT with H-ENTANGLEMENT-IS-SETUP"),
    ("WELL-POSED", "Made & WellPosed & !PriorConnection -> False", "chain.py's clause (PriorSetup there; ungraded)"),
    ("HOLDS", "Holds -> E_success >= N", "H-HOLD-IS-ENTANGLE with H-ER=EPR, H-RT-HERE, H-NECK-HOLDS (one way: a floor)"),
    ("LOCC-AVERAGE", "LocalOnly -> p E_success + (1-p) E_fail <= E_exist",
     "Horodecki p.4 (READ): 'can not be increased on average'; measure H-ENTROPY-COUNTS"),
    ("QUANTUM-CARRIER", "QCarrier -> p E_success + (1-p) E_fail <= E_exist + qubits",
     "Chen-Yang (title READ): one qubit adds 'at most' one ebit (H-SUBADD)"),
    ("ONE-MODE", "exactly one of LocalOnly, QCarrier, UCarrier", "definition; UCarrier (M's) carries no bound"),
]


def _route(ratio, mode, p=1, qubits=0, made=False, ue=True, prior=None):
    return dict(ratio=ratio, mode=mode, p=p, qubits=qubits, made=made, ue=ue, prior=prior)


ROUTES = {
    "R-FIND: E_exist = N, device local": _route(1, "LocalOnly"),
    "R-WIDEN-LOCAL deterministic: E_exist = N/2, p = 1": _route(0.5, "LocalOnly"),
    "R-WIDEN-LOCAL heralded at the bound: E_exist = N/2, p = 1/2": _route(0.5, "LocalOnly", p=0.5),
    "R-WIDEN-LOCAL heralded above the bound: E_exist = N/2, p = 0.6": _route(0.5, "LocalOnly", p=0.6),
    "R-WIDEN-QUANTUM: E_exist = N/2, N/2 qubits carried": _route(0.5, "QCarrier", qubits=0.5),
    "R-WIDEN-QUANTUM short: E_exist = N/2, N/4 qubits carried": _route(0.5, "QCarrier", qubits=0.25),
    "R-WIDEN-UNIDENTIFIED: E_exist = N/2, M's carrier": _route(0.5, "UCarrier"),
    "R-MADE under UE, E_exist = N": _route(1, "LocalOnly", made=True),
    "R-MADE under UE, E_exist = N/2, local": _route(0.5, "LocalOnly", made=True),
}


def z3_routes(routes=None, drop=None):
    import z3
    B = {k: z3.Bool(k) for k in ("UE", "PriorConnection", "Made", "WellPosed", "Holds", "LocalOnly", "QCarrier",
                                 "UCarrier")}
    Ee, Es, Ef, N, p, q = (z3.Real(k) for k in ("E_exist", "E_success", "E_fail", "N", "p", "qubits"))
    cl = {
        "UNIVERSAL": z3.Implies(B["UE"], z3.And(Ee > 0, B["PriorConnection"])),
        "WELL-POSED": z3.Not(z3.And(B["Made"], B["WellPosed"], z3.Not(B["PriorConnection"]))),
        "HOLDS": z3.Implies(B["Holds"], Es >= N),
        "LOCC-AVERAGE": z3.Implies(B["LocalOnly"], p * Es + (1 - p) * Ef <= Ee),
        "QUANTUM-CARRIER": z3.Implies(B["QCarrier"], p * Es + (1 - p) * Ef <= Ee + q),
        "ONE-MODE": z3.PbEq([(B["LocalOnly"], 1), (B["QCarrier"], 1), (B["UCarrier"], 1)], 1),
    }
    out = {}
    for name, r in (routes or ROUTES).items():
        s = z3.Solver()
        for k, v in cl.items():
            if k != drop:
                s.add(v)
        s.add(N > 0, Ee == r["ratio"] * N, Ef >= 0, Es >= 0, p == r["p"], q == r["qubits"] * N, B["Holds"])
        s.add(B[r["mode"]], B["UE"] == r["ue"], B["Made"] == r["made"], B["WellPosed"])
        if r["prior"] is not None:
            s.add(B["PriorConnection"] == r["prior"])
        out[name] = {"consistent": s.check() == z3.sat}
    return out


# ============================================================================================ compute
def compute():
    o = owners()
    ch, vac = o["chain"], o["vacuum"]
    uses = ch.owners()["uses"]
    cm = ch.owners()["cmbframe"]
    seat, fa, ca = uses.owners()
    core = fa.identity_core()["total_bits"]
    rt = rt_area_per_ebit()
    fl_core = ch.corridor_floor(core)
    saved = list(sys.path)
    sys.path[:0] = [D68, WD]
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            scaling = vac.gauss_scaling((2, 4, 7, 10, 14))
            L = cm.geometry()["L_ly"] * cm.LY                           # the board's Proxima span (cmbframe)
            wff = vac.window_free_floor(L)
            z = z3_routes()
            ctl = {
                "deterministic_local_without_average": z3_routes(
                    {"w": ROUTES["R-WIDEN-LOCAL deterministic: E_exist = N/2, p = 1"]}, drop="LOCC-AVERAGE")["w"],
                "short_quantum_without_bound": z3_routes(
                    {"q": ROUTES["R-WIDEN-QUANTUM short: E_exist = N/2, N/4 qubits carried"]},
                    drop="QUANTUM-CARRIER")["q"],
                "made_no_prior_from_any_source": z3_routes(
                    {"m": _route(1, "LocalOnly", made=True, ue=False, prior=False)})["m"],
            }
    finally:
        sys.path[:] = saved
    return {"rt": rt, "core_bits": core, "floor_core": fl_core, "bridge_area_core_m2": rt["value"] * core,
            "scaling": scaling, "proxima_L_m": L, "window_free_floor": wff, "z3": z, "controls": ctl,
            "rt_read": RT_READ, "horodecki_read": HORODECKI_READ}


def report(d):
    rt = d["rt"]
    print("entangle.py -- M-RULINGS item 100 (H-UNIVERSAL-ENTANGLEMENT), along chain.py (item 96)")
    print("E3 the area of N ebits (one formula with chain.py's neck; RT eq. 1.5 p.1, normalization p.4, READ):")
    print("   %s = %s = %.9e m^2 per ebit (u_r %.1e, from G)" % (rt["form"], rt["exact"], rt["value"], rt["u_r"]))
    print("   core README %.6e bits, counted as ebits under H-HOLD-IS-ENTANGLE: area %.6e m^2" % (
        d["core_bits"], d["bridge_area_core_m2"]))
    print("E1 the field's entanglement by separation at a fixed window (vacuum.gauss_scaling; per lambda^2, beta = L/cT):")
    for r in d["scaling"]:
        tag = "" if r["beta=L/cT"] >= 7 else "   (communication not excluded, vacuum.py H-SPACELIKE)"
        print("   beta %4.1f   N+_max %.4e   asymptote %.4e%s" % (r["beta=L/cT"], r["N+_max/lambda^2"],
                                                                 r["asymptote (e/2pi)e^{-b^2/2}b^-4"], tag))
    print("E2/E4 z3 (clauses printed with their sources):")
    for n, cl, src in CLAUSES:
        print("   %-16s %-58s %s" % (n, cl, src))
    for k, v in d["z3"].items():
        print("   %-66s consistent=%s" % (k, v["consistent"]))
    m = d["window_free_floor"]["midpoint"]
    print("Boundary (H-NEARMAX only): one classical message after the window, L/c = %.4e s for Proxima, before the "
          "joining" % m["light time L/c"])


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

    rt, z, c = d["rt"], d["z3"], d["controls"]
    rows = [r for r in d["scaling"] if r["beta=L/cT"] >= 7]
    vals = [r["N+_max/lambda^2"] for r in rows]
    chk("E1: at a fixed window the field's entanglement falls at every spacelike step beta = %s (%.3e to %.3e)" % (
        [r["beta=L/cT"] for r in rows], vals[0], vals[-1]), all(a > b > 0 for a, b in zip(vals, vals[1:])))
    chk("E1: at beta = 14 it is within 2%% of the asymptote (e/2pi) e^{-beta^2/2} beta^-4 (ratio %.4f)" % (
        vals[-1] / rows[-1]["asymptote (e/2pi)e^{-b^2/2}b^-4"]),
        abs(vals[-1] / rows[-1]["asymptote (e/2pi)e^{-b^2/2}b^-4"] - 1) < 0.02)
    chk("E4: a bridge found with the README's ebits holds it with the device acting locally (consistent)",
        z["R-FIND: E_exist = N, device local"]["consistent"])
    chk("E4: deterministic local widening of a bridge half the README's size is inconsistent (on-average monotonicity)",
        not z["R-WIDEN-LOCAL deterministic: E_exist = N/2, p = 1"]["consistent"], contrast=True)
    chk("E4: heralded local widening succeeds at p = E_exist/N = 1/2 (consistent) and not at p = 0.6 (inconsistent)",
        z["R-WIDEN-LOCAL heralded at the bound: E_exist = N/2, p = 1/2"]["consistent"] and
        not z["R-WIDEN-LOCAL heralded above the bound: E_exist = N/2, p = 0.6"]["consistent"])
    chk("E4: a quantum carrier widens N/2 with N/2 qubits carried (consistent) and not with N/4 (inconsistent)",
        z["R-WIDEN-QUANTUM: E_exist = N/2, N/2 qubits carried"]["consistent"] and
        not z["R-WIDEN-QUANTUM short: E_exist = N/2, N/4 qubits carried"]["consistent"])
    chk("E4: M's unidentified carrier widens it (consistent; no bound is carried)",
        z["R-WIDEN-UNIDENTIFIED: E_exist = N/2, M's carrier"]["consistent"])
    chk("E2: under item 100 a made corridor is consistent where the entanglement already reaches N, and not with half "
        "of it by local action -- made and found meet",
        z["R-MADE under UE, E_exist = N"]["consistent"] and
        not z["R-MADE under UE, E_exist = N/2, local"]["consistent"])
    chk("with the on-average clause dropped, deterministic local widening becomes consistent (load-bearing)",
        c["deterministic_local_without_average"]["consistent"], ctl=True)
    chk("with the per-qubit bound dropped, the short quantum carrier becomes consistent (load-bearing)",
        c["short_quantum_without_bound"]["consistent"], ctl=True)
    chk("with no prior connection from any source, the made corridor is inconsistent (PriorConnection is load-bearing; "
        "UE is one source, H-PRIOR-SETUP another)", not c["made_no_prior_from_any_source"]["consistent"], ctl=True)
    structural.append("E3: the RT area per ebit and chain.py's neck per bit are one closed form, 2 h G ln2/(pi c^3) "
                      "(%.9e vs %.9e) -- RT fixes its normalization from Bekenstein-Hawking (p.4); first counted" % (
                          rt["value"], rt["chain_neck_area_per_bit"]))
    structural.append("the bit/nat factor is ln2 by definition (first counted as a control)")
    structural.append("E2: UE supplies PriorConnection by its encoding (H-ENTANGLEMENT-IS-SETUP); first counted")
    structural.append("H-RT-HERE: RT is proposed for AdS_{d+2}; applying it to a corridor in our universe is outside "
                      "its stated setting")
    structural.append("E1's field scope is vacuum.py's (H-UDW, H-PERTURB, H-MINK-VAC, H-SPACELIKE); with a window scaled "
                      "to L the degree does not fall (vacuum.py)")
    m = d["window_free_floor"]["midpoint"]
    structural.append("boundary (H-NEARMAX): one classical message after a vanishing window, L/c = %.6e s for Proxima "
                      "(vacuum.window_free_floor; it recomputes L/c, so not counted)" % m["light time L/c"])
    structural.append("how many ebits the universe already holds across the Sun|Proxima cut is not computed: OPEN")
    for s_ in structural:
        print("  STRUCTURAL: " + s_)
    print("entangle.py: %d/%d checks pass, %d of them controls and %d contrasts; %d STRUCTURAL printed, not counted" % (
        n_pass, n_pass + n_fail, n_ctl, n_con, len(structural)))
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
