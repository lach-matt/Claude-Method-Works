#!/usr/bin/env python3
"""derived_go.py -- item 544: the N1* session's go/no-go at 10 l5 (n1star/growth5.py, N1STAR-PROOF.md section 10.2),
run at the record's own derived point: the window's floor lam_P = (64 pi^2/3)^(1/3) l5 = 5.949 l5 on the least seeds
seed_derive.py D3 gives there.  Labels: computed (exact unless marked), deduced, M's.

  D0 (M's) 544, verbatim: "Theorem P carried, and 10 l5 left with the N1* seesion - are now ready. The nonlinear
     settlings are still being worked".
  D1 (computed exact) The parameters, in growth5's units (the seed's mass mu0 = L l5^2 set to one).  The wavelength is
     lam/sqrt(mu0) = 5.949/sqrt(L); the core boundary x_K = 1 sits at r_K = (sqrt 72/L)^(1/4) sqrt(mu0) (hf_core5);
     the wave's metric amplitude there is a := (lam/sqrt(mu0)) A r_K^(-3/2) with A = 1.  growth5's two points are
     reproduced as the control (L = 100 at lam = 10 l5: 2.52; L = 1000: 1.89; the record's regime, lam/sqrt(mu0) =
     0.1 at L = 100: 0.25).  At lam_P: copper (L = 102.4) 1.50, the example README (60.9) 1.60, r0 = 20 ell (808.5)
     1.16, the Earth cap (917.2) 1.14.  hf_mirror5 X9 recorded the high-frequency regime as ending near a = 1.2.
  D2 (computed, numerical; pinned) The record's own scheme (hf_mirror5's, on hf_core5's domain: seed 1, A = 1, the
     record's envelope on [1/2, 7/2], the slices continued to x_K = 1) run by growth5.run at the derived point, with
     growth5's own breakdown criterion (a second zero of the round spheres' outgoing expansion persisting over 0.01 in
     v, or W >= 0 at the core boundary).  The shell peaks at v = 2.
     - Copper (L = 102.4, lam/sqrt(mu0) = 0.588): a second zero persists from v = 1.398 (Ny = 20; 1.403 at Ny = 28) to
       1.42; W >= 0 at the core boundary from 1.5625; the slice solve fails at 1.81-1.86.
     - The example README (60.9, 0.762): a second zero for one step at 1.45 (a transient the criterion excludes); W >= 0
       at the boundary from 1.5125; the solve fails at 1.725.
     - r0 = 20 ell (808.5, 0.209): a second zero persists from v = 1.833 to 2.02 (Ny = 20; 1.8326 at Ny = 28), again
       over 2.09-2.14; W < 0 at the boundary throughout, and the run reaches v = 4.5.  After the break its mass aspect
       at past null infinity, which the mass law fixes from the data alone (to second order 1 + (2/9) A^2 int (env^2 +
       lam^2 env'^2) = 1.202; the record's control run sits 0.005 from its own), swings by about 0.1 and differs
       between the grids (1.460 and 1.183 at v = 4.5): not a converged solution past the break.
  D3 (computed) Grids: copper at Ny = 20 and 28, the breakdown agreeing to 0.005; r0 = 20 ell at 20 and 28, to 0.0003.
  D4 (deduced) What it decides.  At the record's own derived point the record's scheme gives no approximant on D_T
     either: at the small end's two anchors it fails both clauses of its premise before the shell's peak; at the large
     end's anchor it fails the one-zero clause at the peak, the boundary staying outflow, and its run past the break
     does not converge.  So the N1* session's go/no-go at 10 l5 bears on SOURCE's own wavelength lam_P too, and the
     passage at the physical wavelength through the seed's interior is not computed by the record's scheme at any
     anchor.  The delivery within half a bit is computed outside the horizon (seed_escape, seed_types, seed_derive,
     seed_second) and does not use it.
  D5 (deduced; since 545) What the clauses are.  mots545 searched every slice for marginally trapped surfaces.  The
     one-zero clause fails on these slices only by the angular shift's term, and the outer horizon is the only
     marginally trapped surface of any shape wherever the boundary is outflow, so no inner one forms.  What stops the
     scheme at the small end is the causal clause (the boundary inflow from 1.5625 and 1.5125).  At the large end
     nothing stops it but the run's convergence past 1.833.

What this does not claim: anything about the event horizon or the exterior (growth5's measurement is of the round
spheres inside the seed's horizon, in the scheme's gauge); a theorem (a run of a scheme is not one); the large end's
two anchors beyond the one run (r0 = 20 ell stands for both, their amplitudes 1.16 and 1.14).

Usage: python3 derived_go.py --selftest | --mutants | --run NAME NY | --report
"""
import importlib.util, json, math, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
G5 = os.path.join(HERE, "..", "n1star", "growth5.py")
DATA = os.path.join(HERE, "data", "derived_go_runs.json")
LAM_P = (64*math.pi**2/3)**(1/3)
POINTS = {"copper": 102.4, "example": 60.9, "r0=20ell": 808.5, "earth": 917.2}   # seed_derive D3, at lam_P
MUT = {}


def words():
    return ("Theorem P carried, and 10 l5 left with the N1* seesion - are now ready. The nonlinear settlings are still "
            "being worked")


def g5():
    spec = importlib.util.spec_from_file_location("dg_growth5", G5)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, os.path.dirname(G5))
    spec.loader.exec_module(mod)
    return mod


def lam_hat(L, lam_l5=LAM_P):
    return lam_l5/(L if MUT.get("lam_in_l5") else math.sqrt(L))


def amplitude(L, lam_hat_):
    r_k = (math.sqrt(72)/L)**0.25
    return lam_hat_*r_k**(-1.0 if MUT.get("r_power") else -1.5)


def d1():
    ctl = {"L100 10l5": amplitude(100, lam_hat(100, 10.0)), "L1000 10l5": amplitude(1000, lam_hat(1000, 10.0)),
           "L100 regime": amplitude(100, 0.1)}
    pts = {k: amplitude(L, lam_hat(L)) for k, L in POINTS.items()}
    return ctl, pts


def key(name, Ny):
    return "%s_%dx16" % (name, Ny)


def trim(rec):
    return {"cfg": rec["cfg"], "end": rec["end"], "seconds": rec["seconds"],
            "steps": [s[:6] for s in rec["steps"]]}


def load():
    return json.load(open(DATA)) if os.path.exists(DATA) else {}


def breakdown(G, rec):
    return G.breakdown(rec, hold=0.0 if MUT.get("no_hold") else 0.01)


def int_kv(rec, vb):
    S = [s for s in rec["steps"] if vb is None or s[0] <= vb + 1e-9]
    return sum(0.5*(a[1] + b[1])*(b[0] - a[0]) for a, b in zip(S, S[1:]))


PINNED = {    # the runs of 2026-10-20 (data/derived_go_runs.json): breakdown, end, int K_v to the breakdown
    "copper_20x16": dict(v_break=1.398438, end="scheme failed at v = 1.8125: LinAlgError", int_Kv=0.3972),
    "copper_28x16": dict(v_break=1.403226, end="scheme failed at v = 1.8589: LinAlgError", int_Kv=0.4037),
    "example_20x16": dict(v_break=1.5125, end="scheme failed at v = 1.7250: LinAlgError", int_Kv=0.588),
    "r0=20ell_20x16": dict(v_break=1.832865, end="complete", int_Kv=1.0127),
    "r0=20ell_28x16": dict(v_break=1.832615, end="complete", int_Kv=1.0123),
}


def verdict(R, G):
    out = []
    for k in sorted(R):
        vb = breakdown(G, R[k])
        out.append((k, vb, R[k]["end"], int_kv(R[k], vb)))
    return out


def checks():
    ok = {}
    ok["D0 M's words, 544"] = words().startswith("Theorem P carried")
    ctl, pts = d1()
    ok["D1 growth5's points reproduced: 2.52 and 1.89 at 10 l5, 0.25 in the record's regime"] = (
        abs(ctl["L100 10l5"] - 2.52) < 0.01 and abs(ctl["L1000 10l5"] - 1.887) < 0.01
        and abs(ctl["L100 regime"] - 0.252) < 0.001)
    ok["D1 at lam_P: copper 1.50, the example 1.60, r0 = 20 ell 1.16, the Earth cap 1.14"] = (
        abs(lam_hat(1, 1) - 1) < 1e-12 and abs(LAM_P - 5.9491) < 1e-3
        and abs(pts["copper"] - 1.497) < 0.01 and abs(pts["example"] - 1.596) < 0.01
        and abs(pts["r0=20ell"] - 1.157) < 0.01 and abs(pts["earth"] - 1.138) < 0.01)
    R = load()
    if PINNED:
        G = g5()
        good = True
        for k, pin in PINNED.items():
            if k not in R:
                good = False
                continue
            vb = breakdown(G, R[k])
            good &= ((vb is None and pin["v_break"] is None) or
                     (vb is not None and pin["v_break"] is not None and abs(vb - pin["v_break"]) < 1e-6))
            good &= R[k]["end"] == pin["end"] and abs(int_kv(R[k], vb) - pin["int_Kv"]) < 1e-3
        ok["D2 the pinned runs read back: breakdown, end and int K_v as recorded"] = good
        if "copper_20x16" in PINNED and "copper_28x16" in PINNED:
            a, b = PINNED["copper_20x16"]["v_break"], PINNED["copper_28x16"]["v_break"]
            c, e = PINNED["r0=20ell_20x16"]["v_break"], PINNED["r0=20ell_28x16"]["v_break"]
            ok["D3 the breakdown agrees between Ny = 20 and 28: copper to 0.005, r0 = 20 ell to 0.0003"] = (
                a is not None and b is not None and abs(a - b) < 0.01 and abs(c - e) < 0.001)
    return ok


def selftest(quiet=False):
    ck = checks()
    for k, v in ck.items():
        if not quiet:
            print("[%s] %s" % ("ok" if v else "FAIL", k))
    good = all(ck.values())
    if not quiet:
        print("derived_go.py: %d/%d %s" % (sum(ck.values()), len(ck), "pass" if good else "FAIL"))
    return good


def mutants():
    caught = 0
    names = ("r_power", "lam_in_l5", "no_hold")
    for m in names:
        MUT.clear(); MUT[m] = True
        bad = not selftest(quiet=True)
        caught += bad
        print("mutant %-10s %s" % (m, "caught" if bad else "MISSED"))
    MUT.clear()
    print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


def report():
    ctl, pts = d1()
    print("D1 controls:", {k: round(v, 3) for k, v in ctl.items()})
    print("D1 at lam_P:", {k: round(v, 3) for k, v in pts.items()})
    R = load()
    if R:
        G = g5()
        for k, vb, end, iv in verdict(R, G):
            print("%-18s v_break %s  end: %s  int K_v %.3f  (%ds)" % (k, vb, end, iv, R[k]["seconds"]))


if __name__ == "__main__":
    if "--run" in sys.argv:
        i = sys.argv.index("--run")
        name, Ny = sys.argv[i + 1], int(sys.argv[i + 2])
        L = POINTS[name]
        G = g5()
        rec = G.run(L, lam_hat(L), Ny, 16)
        R = load()
        R[key(name, Ny)] = trim(rec)
        json.dump(R, open(DATA, "w"), separators=(",", ":"))
        print("wrote %s: end %s, breakdown %s, %ds" % (key(name, Ny), rec["end"], G.breakdown(rec), rec["seconds"]))
    elif "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    elif "--report" in sys.argv:
        report()
    else:
        sys.exit(0 if selftest() else 1)
