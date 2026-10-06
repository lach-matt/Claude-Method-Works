#!/usr/bin/env python3
"""entangle.py -- DOCKET 68, M-RULINGS item 100: "Consider that until refuted everything is entangled to everything,
however, the entanglements can range/differ in characterization."  What follows from it along the chain (chain.py,
item 96).  Deduced, computed and READ; not verified; not seated.  Write-up: ENTANGLE.md.

M's hypothesis, carried as given, never as a result:
  H-UNIVERSAL-ENTANGLEMENT  every system is entangled with every other, until a refutation; the entanglements differ in
                            character (in degree and in kind).

WHAT FOLLOWS THE WORK (item 82: lead with what passes)
  E1 NOT REFUTED; THE FIELD SUPPLIES IT, AND ITS CHARACTER FALLS WITH DISTANCE.  The vacuum of a free field is
     entangled between regions that cannot communicate, at every separation (vacuum.py, R1/R2 READ there: "arbitrarily
     far-apart regions", negativity >= exp(-(L/cT)^3)), and its strength falls faster than any power of L at a fixed
     window (vacuum.gauss_scaling, imported: N+_max/lambda^2 ~ (e/2pi) e^{-beta^2/2} beta^-4, beta = L/cT).  M's
     "everything ... entangled" holds for the field on vacuum.py's premises; M's "differ in characterization" is the
     fall with distance, computed.
  E2 THE PRIOR CONNECTION IS THE UNIVERSE'S, NOT THE DEVICE'S.  chain.py's WELL-POSED clause bars only a corridor made
     with no prior connection; under H-UNIVERSAL-ENTANGLEMENT every pair of places already has one (z3, below).  The
     setup item 99 read from answer 4 (R-ENTANGLED-SETUP) need not be built: it is already there, at every destination.
  E3 THE CORRIDOR FOR AN N-BIT README IS THE BRIDGE OF N EBITS.  Read with ER=EPR (Maldacena-Susskind, READ in
     geometry.py: entangled systems joined by Einstein-Rosen bridges) and the Ryu-Takayanagi area law (READ here:
     S_A = Area(gamma_A) / (4 G_N), eq. 1.5 p.1), a bridge carrying N ebits has minimal area
     A = N x 4 ln2 G hbar / c^3 = N x 2 h G ln2 / (pi c^3) = 7.24277891e-70 m^2 x N.  That is EXACTLY the neck chain.py
     found by a different route (Misner-Sharp at a throat with Bekenstein's bound): the corridor that holds the README
     is the bridge of the README's own size in entanglement.  M's "single channel that grows" (item 94) is a bridge that
     carries more ebits; M's found throats (item 86 answer 3, "common and regular occurrences") are the bridges of the
     entanglement already there.
  E4 WHAT WIDENING NEEDS (z3).  The ebits across the P1|P2 cut do not rise under local operations and classical
     communication (Vidal-Werner Prop. 3, READ in vacuum.py; Horodecki RMP: LOCC "cannot bring in entanglement for
     free", READ in chain item 99).  So: a corridor FOUND carrying >= N ebits holds the README with the device acting
     locally (consistent); WIDENING a bridge that carries < N by local action alone is inconsistent; widening with an
     operation that is not LOCC (a quantum carrier at <= c, or M's H-UNIDENTIFIED-CARRIER, item 90) is consistent.
  E5 THE TWO OPEN NEEDS LAND ON ONE HYPOTHESIS.  A non-traversable bridge carries no signal (MS fn.1; geometry.py's
     no-signal computation), so the README's presence at position 2 needs a carrier; widening a thin bridge needs a
     non-LOCC operation.  Both are what H-UNIDENTIFIED-CARRIER would have to do.  Recorded, not merged: whether one
     carrier does both is OPEN.

WHAT IS RULED OUT, AS THE BOUNDARY
  * Widening by the device's local action alone, from a bridge thinner than the README (LOCC monotonicity, z3).
  * If near-maximal pairs were needed (H-NEARMAX, vacuum.py) rather than entanglement entropy (RT), concentrating the
    weak vacuum entanglement needs at least one classical message, >= L/c (vacuum.window_free_floor, imported): for
    Proxima 1.340e8 s -- before the joining, so allowed as prior setup (H-PRIOR-SETUP), not a delay of the teleport.
    Under H-UNIVERSAL-ENTANGLEMENT no probe crosses (vacuum's H-PROBE-OPERATED is set aside: the matter at position 2
    is already entangled, H-POSITION-BUILDS).

NAMED HYPOTHESES
  M's: H-UNIVERSAL-ENTANGLEMENT (item 100); H-UNIDENTIFIED-CARRIER (90); H-COMMON-THROATS, H-MADE (86.3);
    H-SINGLE-CHANNEL-GROWS (94); H-POSITION-BUILDS (91); H-COST-IN-README (89).
  The board's: H-ER=EPR (MS's conjecture, "speculation" p.2, READ via geometry.py); H-RT-HERE (the Ryu-Takayanagi area
    law, proposed for AdS_{d+2}, applied to our corridor -- outside its stated setting); H-SI-RESTORE (S/k_B =
    A c^3 / (4 G hbar), the Bekenstein-Hawking form in SI, eq. 1.1's units restored); H-ENTROPY-COUNTS (the bridge's
    size counts entanglement entropy, not near-maximal pairs; its alternative H-NEARMAX is vacuum.py's); H-CUT (the
    ebits are counted across the cut the corridor joins, the regions the device triangulates, item 86.4); H-LOCC
    (linear QM: the device at P1 and the position at P2 act locally, with classical messages); and chain.py's
    H-NECK-HOLDS, H-STRONG-BOUND; vacuum.py's H-UDW, H-PERTURB, H-MINK-VAC, H-SPACELIKE (E1's scope).

USAGE
    python3 entangle.py              the report
    python3 entangle.py --selftest   checks, CONTROLS and CONTRASTS marked, STRUCTURAL printed and not counted
    python3 entangle.py --json
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
    "source": "Ryu & Takayanagi, 'Holographic Derivation of Entanglement Entropy from AdS/CFT', hep-th/0603001",
    "route": "arXiv PDF via Firecrawl (markdown, pages 1-3)",
    "eq_1_5": "S_A = Area of gamma_A / (4 G_N^(d+2)), p.1: 'we propose the following area law'; gamma_A the d "
              "dimensional static minimal surface in AdS_{d+2} whose boundary is the boundary of A",
    "eq_1_1": "S_BH = Area of horizon / (4 G_N), p.1 (the Bekenstein-Hawking formula the proposal is 'analogous to')",
    "p2": "'The minimal surface provides the severest entropy bound when we fix its boundary condition. In our case it "
          "saturates the bound.'",
    "scope": "AdS_{d+2} / CFT_{d+1}, a proposal shown for d = 1 and compared for general d (abstract); natural units",
}


# ============================================================================================ E3: the bridge of N ebits
def rt_area_per_ebit():
    """H-RT-HERE with H-SI-RESTORE: one ebit (S = k_B ln2) needs minimal area 4 ln2 G hbar / c^3 (M-COEFF: h, c exact,
    G measured).  Returns the exact form and value, and, as the control, the per-nat value (no ln2)."""
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
    per_nat = 4 * G * hbar / c ** 3
    return {"form": "A per ebit = 4 ln2 G hbar / c^3 = 2 h G ln2 / (pi c^3)", "exact": str(sp.nsimplify(per_ebit)),
            "value": float(sp.N(per_ebit, 20)), "per_nat": float(sp.N(per_nat, 20)),
            "chain_neck_area_per_bit": co["neck_area_m2_per_bit"]["value"], "u_r": co["neck_area_m2_per_bit"]["u_r"]}


# ============================================================================================ E2, E4: z3
CLAUSES = [
    ("UNIVERSAL", "UE -> E_exist > 0 & PriorConnection", "M's H-UNIVERSAL-ENTANGLEMENT (item 100)"),
    ("WELL-POSED", "Made & WellPosed & !PriorConnection -> False", "chain.py's clause (PriorSetup there; ungraded)"),
    ("HOLDS", "Holds <-> E_exist + E_added >= N", "H-ER=EPR + H-RT-HERE + H-NECK-HOLDS: the bridge holds the README "
                                                   "iff it carries N ebits (E3)"),
    ("LOCC-MONOTONE", "LocalOnly -> E_added <= 0", "Vidal-Werner Prop. 3 (READ, vacuum.py R7); Horodecki RMP sec. I "
                                                   "(READ, item 99): LOCC 'cannot bring in entanglement for free'"),
    ("CARRIER", "Carrier -> !LocalOnly", "definition: a non-LOCC operation (a quantum carrier at <= c, or "
                                         "H-UNIDENTIFIED-CARRIER) is not local action; nothing bounds what it adds"),
]

ROUTES = {
    "R-FIND: a bridge already carrying >= N ebits, device local": dict(UE=True, Made=False, ratio=1.0, LocalOnly=True),
    "R-MADE under UE (the universe's prior connection), bridge already >= N": dict(UE=True, Made=True, WellPosed=True,
                                                                               ratio=1.5, LocalOnly=True),
    "R-WIDEN-LOCAL: a thinner bridge (E_exist = N/2), widened by local action alone": dict(UE=True, Made=False,
                                                                                       ratio=0.5, LocalOnly=True),
    "R-WIDEN-CARRIER: a thinner bridge widened by a non-LOCC carrier": dict(UE=True, Made=False, ratio=0.5,
                                                                         LocalOnly=False, Carrier=True),
}


def z3_routes(routes=None, drop=None, ue=True):
    import z3
    B = {k: z3.Bool(k) for k in ("UE", "PriorConnection", "Made", "WellPosed", "Holds", "LocalOnly", "Carrier")}
    Ee, Ea, N = z3.Real("E_exist"), z3.Real("E_added"), z3.Real("N")
    cl = {
        "UNIVERSAL": z3.Implies(B["UE"], z3.And(Ee > 0, B["PriorConnection"])),
        "WELL-POSED": z3.Not(z3.And(B["Made"], B["WellPosed"], z3.Not(B["PriorConnection"]))),
        "HOLDS": B["Holds"] == (Ee + Ea >= N),
        "LOCC-MONOTONE": z3.Implies(B["LocalOnly"], Ea <= 0),
        "CARRIER": z3.Implies(B["Carrier"], z3.Not(B["LocalOnly"])),
    }
    out = {}
    for name, r in (routes or ROUTES).items():
        s = z3.Solver()
        for k, v in cl.items():
            if k != drop:
                s.add(v)
        s.add(N > 0, Ee >= 0, Ee == r["ratio"] * N, B["Holds"])
        s.add(B["UE"] == (r.get("UE", True) and ue))
        for k in ("Made", "WellPosed", "LocalOnly", "Carrier"):
            if k in r:
                s.add(B[k] == r[k])
        if not (r.get("UE", True) and ue):
            s.add(z3.Not(B["PriorConnection"]))
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
    snap = fa._measure()["grid_0p1A"]
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
                "widen_local_without_monotone": z3_routes({"w": ROUTES["R-WIDEN-LOCAL: a thinner bridge (E_exist = "
                                                                       "N/2), widened by local action alone"]},
                                                          drop="LOCC-MONOTONE")["w"],
                "made_without_ue": z3_routes({"m": ROUTES["R-MADE under UE (the universe's prior connection), bridge "
                                                          "already >= N"]}, ue=False)["m"],
            }
    finally:
        sys.path[:] = saved
    return {"rt": rt, "core_bits": core, "snap_bits": snap, "floor_core": fl_core,
            "bridge_area_core_m2": rt["value"] * core, "scaling": scaling, "proxima_L_m": L,
            "window_free_floor": wff, "z3": z, "controls": ctl, "rt_read": RT_READ}


def report(d):
    rt = d["rt"]
    print("entangle.py -- M-RULINGS item 100 (H-UNIVERSAL-ENTANGLEMENT), along chain.py (item 96)")
    print("E3 the bridge of N ebits (H-ER=EPR, H-RT-HERE, H-SI-RESTORE; RT eq. 1.5 p.1, READ):")
    print("   %s = %s = %.9e m^2 per ebit (u_r %.1e, from G)" % (rt["form"], rt["exact"], rt["value"], rt["u_r"]))
    print("   chain.py's neck per bit (Misner-Sharp + Bekenstein): %.9e m^2" % rt["chain_neck_area_per_bit"])
    print("   core README %.6e ebits: bridge area %.6e m^2; chain's bisected neck area %.6e m^2" % (
        d["core_bits"], d["bridge_area_core_m2"], 4 * math.pi * d["floor_core"]["r_m"] ** 2))
    print("E1 the field's entanglement by separation (vacuum.gauss_scaling, imported; per lambda^2, beta = L/cT):")
    for r in d["scaling"]:
        print("   beta %4.1f   N+_max %.4e   asymptote %.4e" % (r["beta=L/cT"], r["N+_max/lambda^2"],
                                                               r["asymptote (e/2pi)e^{-b^2/2}b^-4"]))
    print("E2/E4 z3 (clauses printed with their sources):")
    for n, cl, src in CLAUSES:
        print("   %-14s %-48s %s" % (n, cl, src))
    for k, v in d["z3"].items():
        print("   %-80s consistent=%s" % (k, v["consistent"]))
    m = d["window_free_floor"]["midpoint"]
    print("Boundary (H-NEARMAX only): one classical message after the window: L/c = %.4e s for Proxima (L = %.4e m), "
          "before the joining" % (m["light time L/c"], d["proxima_L_m"]))


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
    neck_area = 4 * math.pi * d["floor_core"]["r_m"] ** 2
    chk("E3: the Ryu-Takayanagi area for the core's ebits (%.9e m^2) equals chain.py's bisected neck from Misner-Sharp "
        "and Bekenstein (%.9e m^2)" % (d["bridge_area_core_m2"], neck_area),
        abs(d["bridge_area_core_m2"] / neck_area - 1) < 1e-9)
    chk("the area counted per nat instead of per bit misses the neck by ln2 (ratio %.9f)" % (
        rt["per_nat"] * d["core_bits"] / neck_area), abs(rt["per_nat"] * d["core_bits"] / neck_area - 1) > 0.1,
        ctl=True)
    rows = d["scaling"]
    vals = [r["N+_max/lambda^2"] for r in rows]
    chk("E1: the field's harvested entanglement falls with separation at every step of beta = %s (%.3e to %.3e)" % (
        [r["beta=L/cT"] for r in rows], vals[0], vals[-1]),
        all(a > b > 0 for a, b in zip(vals, vals[1:])))
    chk("E1: at beta = 14 it is within 2%% of the asymptote (e/2pi) e^{-beta^2/2} beta^-4 (ratio %.4f)" % (
        vals[-1] / rows[-1]["asymptote (e/2pi)e^{-b^2/2}b^-4"]),
        abs(vals[-1] / rows[-1]["asymptote (e/2pi)e^{-b^2/2}b^-4"] - 1) < 0.02)
    chk("E4: a found bridge already carrying the README's ebits holds it with the device acting locally (consistent)",
        z["R-FIND: a bridge already carrying >= N ebits, device local"]["consistent"])
    chk("E2: a made corridor under H-UNIVERSAL-ENTANGLEMENT clears WELL-POSED with no setup by the device (consistent)",
        z["R-MADE under UE (the universe's prior connection), bridge already >= N"]["consistent"])
    chk("E4: widening a bridge thinner than the README by local action alone is inconsistent (LOCC monotonicity)",
        not z["R-WIDEN-LOCAL: a thinner bridge (E_exist = N/2), widened by local action alone"]["consistent"],
        contrast=True)
    chk("E4: widening it with a non-LOCC carrier is consistent",
        z["R-WIDEN-CARRIER: a thinner bridge widened by a non-LOCC carrier"]["consistent"])
    chk("with LOCC monotonicity dropped, local widening becomes consistent (the clause is load-bearing)",
        c["widen_local_without_monotone"]["consistent"], ctl=True)
    chk("without H-UNIVERSAL-ENTANGLEMENT (and no setup), the made corridor is inconsistent (the hypothesis is "
        "load-bearing)", not c["made_without_ue"]["consistent"], ctl=True)
    m = d["window_free_floor"]["midpoint"]
    structural.append("boundary (H-NEARMAX): one classical message after a vanishing window, L/c = %.6e s for Proxima "
                      "(vacuum.window_free_floor, imported; it recomputes L/c, so not counted)" % m["light time L/c"])
    structural.append("the RT area per ebit and chain.py's neck per bit are the same closed form 2 h G ln2/(pi c^3) "
                      "(%.9e vs %.9e) -- algebra, first counted" % (rt["value"], rt["chain_neck_area_per_bit"]))
    structural.append("H-RT-HERE: RT is proposed for AdS_{d+2} (eq. 1.5 p.1); applying it to a corridor in our "
                      "universe is outside its stated setting")
    structural.append("H-ER=EPR: MS introduce it as speculation (p.2) and its bridges are non-traversable (fn.1), "
                      "READ via geometry.py -- E5: the README's crossing needs a carrier")
    structural.append("E1's scope is vacuum.py's: H-UDW, H-PERTURB, H-MINK-VAC, H-SPACELIKE; no READ upper bound over "
                      "all windows in 3+1 (vacuum.py OPEN)")
    structural.append("how many ebits the universe already holds across the Sun|Proxima cut is not computed: OPEN "
                      "(the found route's quantity)")
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
