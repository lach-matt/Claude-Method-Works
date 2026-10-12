#!/usr/bin/env python3
"""o3_hold.py -- Warp Theorem lemma O3: the hold's window in the corridor's clocks, and that the corridor survives any hold in it.

[Auditing agent, item 281 (the reverse passage, 270/276): O3c bounds stability S5b's power-law blueshift, carried by
side-2 rays along the white-hole surface -- inflow from position 2 (W3), which the one-way object excludes (i_oneway
I3); excluding it strengthens O3c rather than weakens it.  Kept as written.]

[Item 331 (M-UPDATE-STALE-NOW): O3b's window and O3c's figures (v/4, (1 + v/8)^2) are read off eq. (17) at r0 = 2m,
whose horizon is extremal (stability S1); the corridor's is not (item 251; rows_small O2s; item 271's verifier: O2 false
at both ends).  O3a-O3d stand as statements about eq. (17) and are kept as written; O3b's "2.0e5 at the example
README" is the record's four-dimensional write (o3_write), 66,980 clocks at the small end (write_small S3, C6 verified).
The corridor's hold and its survival are O3e, the current statement.]

READ (through bulk/crossing.py, P-ML): Margolus & Levitin, quant-ph/9710043v2 -- at least h/(4E) to reach one orthogonal
state (eq. 4, p.4); energies of non-interacting subsystems add, and so do their rates (p.8); the bound is on orthogonal
states, NOT bits (p.2).

  O3a  THE HOLD'S LOWER BOUNDS (READ + computed).  Margolus-Levitin's eq. 4 applied to the whole register -- the README
       written onto the throat and horizons (H1, H2) as one system holding the one exact energy E (items 111 (b), 133)
       -- gives hold >= h/(4E) = (2 pi^2/ln2)/N clocks.  Bremermann's bound as Bekenstein states it (quant-ph/0311049,
       eq. (26), p.10: I-dot < 8 pi xi E/hbar log2 e, with xi fixed "at some large value (we shall take xi = 10 for
       illustration)"; READ) gives, for the N bits with the same E, hold >= 1/(2 xi) clocks -- 0.05 clocks at xi = 10
       (computed: E^2 is proportional to N, so the clocks are the same for every N).  Applying a channel-rate bound to
       the register write is the board's mapping.  The tighter is 1/(2 xi); neither is an exact value
  O3a' THE PER-BIT FIGURE, WITHDRAWN.  First derived here: each of N holders flipped to an orthogonal state on its own
       share E/N (H-ONE-STEP-PER-BIT), eq. 4 per holder, hold >= hN/(4E) = 2 pi^2/ln2 = 28.4777 clocks for every N, and
       the hold equal to it (H-HOLD-AT-BOUND).  b4_static.py shows the static bulk carried through that hold reaches
       K = 2.3e4 in its cone and its curvature singularity above the throat.  What the bulk refutes is a conjunction --
       the per-bit write, eq. (17) held exactly and statically, the flat limit, the board's locally analytic class,
       Padé continuation -- and the board withdraws its own reading of the write, H-ONE-STEP-PER-BIT.  H-HOLD-AT-BOUND is
       not refuted by itself: kept against the bounds that remain it would set the hold at about 1/(2 xi) clocks; it is
       withdrawn by choice.  The figure is kept as a control (computed exactly, refuted)
  O3b  THE HOLD'S WINDOW (computed bounds; a requirement on the write).  From below max(h/(4E), 1/(2 xi)); from above
       the bulk -- b4_static.py finds every hold shorter than about 11.3 clocks keeps its computed double cone in
       regular, Padé-stable static bulk.  So the theorem now REQUIRES the hold to lie in the window (H-HOLD-IN-WINDOW,
       the board's): no write mechanism achieving it is shown.  At the example README the top is ~7.5e-36 s.  M's
       136 E, "instantaneous or near instantaneous", is consistent with the window and does not choose it.
       Since item 158 the hold is the write, and o3_write.py puts the write at >= (3645 ln2 N/(8 Z))^(1/3) - 2 clocks
       (2.0e5 at the example README): past this window if the write sits in the static hold, a floor on the opening
       if it is the opening.  O3 is OPEN, waiting on B4d; this window is what the static bulk carries
  O3c  the corridor survives any hold in the window, in linear theory (PROVED for every hold in it): at the window's top,
       v ~ 11.3 m of the horizon's advanced time, stability.py S4's exact rate changes the second derivative by v/(4m)
       times its natural size, and S5b's power-law blueshift is at most (1 + v/(8m))^2 for rays starting within m of the
       surface.  Control: the non-extremal r0 = 1.8m member's exponential over the same v, e^(kappa v)
  O3d  the window's top still exceeds GLOBALBULK G1's local span (1.3-3.2 clocks): the hold is decided by the bulk
       beyond the local data, which is what b4_static.py computes
  O3e  (item 331) the corridor's hold, on the corridor's own geometry.  Since item 158 the hold is the write: at the
       small end at least C6's floor, 66,980 clocks of r_h/c at the example README (write_small S3; C6 verified, item
       264), within the hole's life, 8.57e14 clocks, 1.28e10 times the floor (hold_small, C5 U4; C5 verified, item
       318).  O3b's static window is eq. (17)'s and does not bound it.  Survival in linear theory (bulk/stability.py
       S6, computed):
         our face (the black-hole side, where the hold is): every transverse derivative is damped at kappa = 1/r_h, one
         e-fold per clock, so over any hold -- the floor or the life -- it is bounded by its initial size plus 3/2 of
         the tangential derivative's bound (deduced from S6's identity, the ODE solved exactly); no Aretakis growth.
         That the tangential derivative stays bounded is READ for the scalar wave: Schlue, arXiv:1012.5963v1, Theorem
         1 (eq. (1.9), n >= 3 spatial dimensions) and Proposition 5.2 (the nondegenerate energy uniformly bounded,
         through the redshift effect), quoted in stability S6.  So, for the scalar model Wall E treats and at flat
         order (the bulk Tangherlini, C1 H1), our face survives any hold in linear theory -- the floor and the life
         alike (READ + computed).  Gravitational perturbations: Ishibashi-Kodama's mode stability only (rows_small
         O2s), not a bound -- OPEN for them.
         position 2's face (the white-hole side): the transverse derivative grows as e^(kappa u), Eardley's blueshift,
         bounded by the face's open period, at most 33.6 clocks (c_junction J1): e^33.6 = 3.9e14 (J5; c7_oneway V12
         (Q1), verified).  A blackbody bath of position 2 over that period lands 27 to 65 orders below Barcelo's 0.28 E
         (V12 (Q1)); position 2's other ambient fields are its variances (240), not claimed.
       At the large end (four-dimensional Schwarzschild, kappa = 1/(4M), S6) the same identity holds, damping one
       e-fold per four clocks of m/c on our face, and Schlue's n = 3 covers it; the write there is the record's
       199,702.19 clocks (o3_write), and the large end's open period on position 2's face is not computed -- OPEN with
       M1 there.
       [Item 334: "the hold is the write", read as the face standing through the write, is M's (M-HOLD-IS-THE-FACE,
       confirmed): O3e rests on no reading of the board's; its scope is Wall E's scalar wave, as stated.]
Imports copy/exactE.py, bulk/stability.py, lemmas/b4_static.py and lemmas/hold_small.py by path.  Stdlib + sympy.
python3 o3_hold.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
WD = os.path.dirname(D68)
EXAMPLE_N = 2742570311524972
MUT = {}


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


def hold_in_clocks():
    h, c, G, N = sp.symbols("h c G N", positive=True)
    E = sp.sqrt(N * h * c**5 * sp.log(2) / (8 * sp.pi**2 * G))       # G1, the one exact energy (exactE.py's form)
    clock = (G * E / c**4) / c                                       # m/c
    parallel = sp.simplify((h * N / (4 * E)) / clock)
    sequential = sp.simplify((h * N / (2 * E)) / clock)
    return parallel, sequential


def compute():
    par, seq = hold_in_clocks()
    v_bit = float(par)                                               # the per-bit figure, in units of m
    b4 = _load(os.path.join(HERE, "b4_static.py"), "o3_b4static").compute(live=False)
    v = round(b4["cone"]["t_cert"], 2)                               # the window's top, ~11.3
    st = _load(os.path.join(D68, "bulk", "stability.py"), "o3_stability")
    m = sp.Symbol("m", positive=True)
    c1, _ = st.D_derivatives(sp.Rational(9, 5) * m, 2 * m)            # control member's D'
    kappa_ctl = float((c1 / 2).subs(m, 1))
    ex = _load(os.path.join(D68, "copy", "exactE.py"), "o3_exactE")
    E_ex = ex.e_per_sqrt_bit() * math.sqrt(EXAMPLE_N)
    G, C = 6.67430e-11, 299792458.0
    clock_s = G * E_ex / C**5
    h_, c_, G_, N_, xi = sp.symbols("h c G N xi", positive=True)
    E = sp.sqrt(N_ * h_ * c_**5 * sp.log(2) / (8 * sp.pi**2 * G_))
    clock = G_ * E / c_**5
    whole = sp.simplify((h_ / (4 * E)) / clock)
    transfer = sp.simplify((N_ * sp.log(2) * h_ / (2 * sp.pi) / (8 * sp.pi * xi * E)) / clock)   # N bits at eq. (26)
    transfer_xi10 = float(transfer.subs(xi, 10))
    return {"parallel": par, "sequential": seq, "v_bit": v_bit, "v": v, "whole": whole, "transfer": transfer,
            "t_fail_2": b4["cone"]["t_fail_2"], "Kmax_bit": b4["Kmax_o3"], "clock_s": clock_s, "transfer_xi10": transfer_xi10,
            "hold_top_s": v * clock_s, "whole_example": float(whole.subs(N_, EXAMPLE_N)),
            "s4_growth": v / 4, "s5b_blueshift": (1 + v / 8) ** 2, "control_exp": math.exp(kappa_ctl * v),
            "kappa_ctl": kappa_ctl, "g1_span": (1.29, 3.16), "o3e": o3e(st)}


def o3e(st):
    """O3e (item 331): the hold on the corridor's own horizon (stability S6), its floor and its life"""
    if MUT.get("extremal_kept"):
        st.MUT["extremal_reading"] = True                            # the mutant: eq. (17)'s extremal horizon kept
    if MUT.get("open_through_write"):
        st.MUT["open_through_write"] = True                          # the mutant: face open through the write
    try:
        x = st.nonextremal()
    finally:
        st.MUT.clear()
    H = _load(os.path.join(HERE, "hold_small.py"), "o3_hold_small")
    life = H.l5_checks()["life_clocks"]
    small = x["ends"]["small"]
    return dict(damp=x["bh"]["damp"], grow=x["wh"]["damp"], kap=x["bh"]["syms"][0], sup_ratio=small["sup_ratio"],
                floor=x["floor"], life=life, over=life / x["floor"], open_clocks=x["open_clocks"],
                log10_blue=x["log10_blue"], kappa_large=x["ends"]["large"]["kappa"])


def report(d):
    print("o3_hold.py -- Warp Theorem lemma O3: the hold\n")
    print("O3a whole register: hold >= h/(4E) = %s clocks (%.3g at the example README); transfer (eq. (26)): >= %s"
          % (d["whole"], d["whole_example"], d["transfer"]))
    print("O3a' the per-bit figure h N/(4E) = %s = %.4f clocks: withdrawn as the hold -- its cone reaches K = %.3g "
          "(b4_static.py)" % (d["parallel"], d["v_bit"], d["Kmax_bit"]))
    print("O3b the window: from the READ bounds up to %.2f clocks (= %.2e s at the example README); curved layer from "
          "%.2f" % (d["v"], d["hold_top_s"], d["t_fail_2"]))
    print("O3c at the window's top: S4 change %.2f x natural size; S5b blueshift <= %.2f; control e^(kappa v) = %.1f"
          % (d["s4_growth"], d["s5b_blueshift"], d["control_exp"]))
    print("O3d the window's top (%.1f clocks) exceeds G1's local span (%.2f-%.2f): the bulk decides it"
          % ((d["v"],) + d["g1_span"]))
    e = d["o3e"]
    print("\nO3e (item 331) the corridor's hold: floor %.0f clocks, life %.3g clocks (%.3g x floor); our face d/dv H = "
          "(%s) H + ..., forced part <= %s sup|dpsi/dv|; position 2's face grows at (%s), open %.2f clocks: <= 10^%.2f; "
          "large end kappa = %s" % (e["floor"], e["life"], e["over"], e["damp"], e["sup_ratio"], e["grow"],
                                    e["open_clocks"], e["log10_blue"], e["kappa_large"]))


def checks(d):
    out = []

    def chk(name, cond):
        out.append((name, bool(cond)))

    N_, xi = sp.symbols("N xi", positive=True)
    chk("O3a: whole register, hold >= h/(4E) = (2 pi^2/ln2)/N clocks; transfer bound (eq. (26)) >= 1/(2 xi) clocks",
        sp.simplify(d["whole"] - 2 * sp.pi**2 / sp.log(2) / N_) == 0 and sp.simplify(d["transfer"] - 1 / (2 * xi)) == 0)
    chk("O3a' control: the per-bit figure is h N/(4E) = 2 pi^2/ln2 = 28.48 clocks exactly (sequential: twice)",
        sp.simplify(d["parallel"] - 2 * sp.pi**2 / sp.log(2)) == 0 and sp.simplify(d["sequential"] - 2 * d["parallel"]) == 0)
    chk("O3a': the bulk refutes the per-bit hold -- its cone reaches K > 2e4 (b4_static.py)", d["Kmax_bit"] > 2e4)
    chk("O3b: the window is not empty -- its bottom max(h/(4E), 1/(2 xi)) is 0.05 clocks at xi = 10, its top the bulk's "
        "~11.3 clocks (~7.5e-36 s at the example README), below the curved layer", d["whole_example"] < 1e-10
        and abs(d["transfer_xi10"] - 0.05) < 1e-12 and 10.5 < d["v"] < 12 and 1e-36 < d["hold_top_s"] < 1e-34
        and d["v"] < d["t_fail_2"])
    chk("O3c: at the window's top S4 changes the second derivative by v/4 natural sizes; S5b at most (1 + v/8)^2",
        abs(d["s4_growth"] - d["v"] / 4) < 1e-9 and abs(d["s5b_blueshift"] - (1 + d["v"] / 8) ** 2) < 1e-9
        and d["s5b_blueshift"] < 6.5)
    chk("O3c control: the non-extremal member's exponential over the same v exceeds the corridor's power law",
        d["control_exp"] > d["s5b_blueshift"])
    chk("O3d (STRUCTURAL): the window's top exceeds the local bulk's span, so the global bulk bears on it",
        d["v"] > d["g1_span"][1])
    e = d["o3e"]
    chk("O3e (item 331): the corridor's hold is the write -- C6's floor 66,980 clocks, within the life 8.57e14 clocks "
        "(1.28e10 x); our face damps every transverse derivative at kappa (stability S6), bounded by 3/2 of the "
        "tangential bound; position 2's face's blueshift at most e^33.6 = 3.9e14 over its open period",
        round(e["floor"]) == 66980 and "%.3g" % e["life"] == "8.57e+14" and "%.3g" % e["over"] == "1.28e+10"
        and sp.simplify(e["damp"] + e["kap"]) == 0 and sp.simplify(e["grow"] - e["kap"]) == 0
        and e["sup_ratio"] == sp.Rational(3, 2) and "%.1f" % e["open_clocks"] == "33.6"
        and "%.2g" % 10 ** e["log10_blue"] == "3.9e+14")
    return out


MUTANTS = {"extremal_kept": "the corridor's horizon read as eq. (17)'s, extremal (O3e; item 251)",
           "open_through_write": "position 2's face held open through the write's floor (O3e; item 271 (3))"}


def selftest():
    r_ = checks(compute())
    for name, ok in r_:
        print("  [%s] %s" % ("ok" if ok else "FAIL", name))
    k = sum(ok for _, ok in r_)
    print("selftest: %d/%d" % (k, len(r_)))
    return k == len(r_)


def mutants():
    caught = 0
    for k, desc in MUTANTS.items():
        MUT.clear()
        MUT[k] = True
        try:
            failed = sorted({nm.split(":")[0].split()[0] for nm, ok in checks(compute()) if not ok})
        except Exception as ex_:
            failed = ["raised %s" % type(ex_).__name__]
        MUT.clear()
        caught += bool(failed)
        print("  mutant %-20s %-72s %s" % (k, desc, "caught by " + ", ".join(failed) if failed else "NOT CAUGHT"))
    print("mutants: %d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)




if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report(compute())
