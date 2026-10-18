#!/usr/bin/env python3
"""face2_release.py -- item 491: what stands at position 2, from the math, and its face over its open period.

M, 491: "what does the physics say should stand at position 2?" ... "what does the math say it needs to be?"
489 (face2_open W2) took position 2's face to be open the whole write, the README emerging over it.  That premise is
against M's rulings.  432 (2): the passage is held whole through the write and released at the end (M-RELEASE-WHOLE).
163: the README is held as one whole, not bit by bit.  336 and 386: our energy stays; only information travels.  490
(face2_hold) reasoned from 489's premise and is withdrawn with it.  Here the math is asked directly.  Labels: computed
(exact unless marked), deduced, READ.

  V0 (read) M's words, verbatim in the rulings file: 163, 390, 432, 491.
  V1 (computed: transition5q, run here) What stands at position 2.  The interior our hole enters crosses one transition
     surface, trapped to anti-trapped, at T_T; its only other horizon is at T_WH = 2 T_T, position 2's white hole (H5).
     Its mass is our hole's, m_WH/m_BH = 1 to 1e-30, at every mass computed (H6).  The crossing takes 2 r_h/c, the two
     halves equal by the interior's symmetry about T_T (H9).  So the math puts a white hole of our hole's own mass at
     position 2.  That is 447's dictionary (M's): the five-dimensional corridor seen as a black hole at position 1 and a
     white hole at position 2.  Nothing at position 2 needs to change.
  V2 (computed, on 432 (2) and 390) Its open period.  Position 2's face opens because of the README and closes when
     nothing is contained within the corridor (390): it bounds the anti-trapped region the README crosses (junction_own
     G10).  Held whole through the write and released at the end (432 (2)), the README crosses that region once, whole.
     So the face is open for the release's crossing of the anti-trapped half, at most 1.000 r_h/c of the interior's 2.
     Even the whole interior, 2 r_h/c, bounds it.  At the large end that is 2 r_0/c = 4 clocks of GM/c^3.  The write
     (8.63e14 clocks) is on our side and is not position 2's open period.
  V3 (computed; the stress exact in the s-wave model, the crossing in Dray-'t Hooft-Redmount form: face2_open W4) It
     holds.  In position 2's vacuum the negative mass between the face's own flux and the emerging README grows as
     e^(kappa t) from one clock's flux.  Over T_open <= 2 clocks it reaches 2.2e-15 of the face's mass at the example;
     over 4 clocks of GM/c^3, one e-fold, 1.4e-67 at the Earth cap.  Position 2's vacuum ends a white hole only at
     t_q = 35.8 clocks (620 at the Earth cap), 17.9 (155) times the longest the face is open.
  V4 (computed: face2_open W3's rates; READ) No perturbation reaches it.  On Barcelo, Carballo-Rubio and Garay's
     criterion (JHEP 01 (2016) 157, READ: "black holes turn white fast", a short white phase is robust), a perturbation
     traps the face within T_open only if it carries 0.28 E e^(-kappa T_open): 4.9e7 J at the example, 5.5e40 J at the
     Earth cap, the order of the hole's own energy.  At the example the expected number of particles of any kind
     crossing the capture disc within T_open is 9.9e-16 inside a nucleus and 4.8e-51 in a 3 K bath.  At the Earth cap
     the hottest environment computed, a 1e10 K blackbody, delivers 5.6e19 J onto the disc within T_open.
  V5 (computed, exact) The README fits through the face whole.  Position 2's face has our face's area, since the mass
     is equal (V1), and the README's N ln2 is exactly A/(4 l5^3), the area law of (H) and G3.  So the release meets the
     covariant entropy bound (Bousso, JHEP 07 (1999) 004, READ) at equality, at any duration.  490's lower bound on the
     white phase (face2_hold K2) priced the README as free radiation carrying our energy out of position 2, which 336
     and 386 exclude: withdrawn.
  V6 (deduced) So the math says position 2 needs to be the white hole of our hole's mass that the transition computes.
     Its face opens with the README's release at the end of the write, is open at most 2 r_h/c (4 clocks of GM/c^3 at
     the large end), and closes as the README leaves (390).  Through that period established physics holds it (V3-V4),
     and the README passes it whole (V5).  FACE2s and FACE2 are proved under 441 (1): a computed solution
     (transition5q's interior, released on 432 (2)) meets the specification, consistent with established physics in
     the semiclassical region.  Barcelo et al.'s own conclusion, that a black hole turns white fast or stays black, is
     this case: fast.

python3 face2_release.py [--selftest | --mutants]
"""
import os, sys, math, re, io, contextlib, importlib.util
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((163, "All together, one whole"), (390, "it closes when there is nothing contained within the corridor"),
         (432, "M-RELEASE-WHOLE (the passage is held whole through the write and released at the end"),
         (491, "what does the math say it needs to be?"))


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


# ------------------------------------------------------------------ V1, V2
def transition():
    T5 = _load("transition5q.py", "f2r_t5")
    o = T5.compute()
    ck = T5.checks(o)
    res = o["res"]
    mp = T5.mp
    taus, halves, mwh = [], [], []
    for e, v in res.items():
        s = v["s"]
        taus.append(float(v["tau"]))
        # the anti-trapped half, T_T to T_WH: the lapse is symmetric about T_T (transition5q's symm, < 1e-20), so it
        # equals the trapped half, tau/2 (the integral to T_WH itself meets the horizon's coordinate singularity)
        halves.append(float(v["tau"]) / 2 if float(v["symm"]) < 1e-20 else float("inf"))
        mwh.append(abs(float(v["mwh"]) - 1))
    return dict(ck=ck, tau=max(taus), half=max(halves), mwh=max(mwh))


def open_period(tr):
    # 432 (2): released whole at the end -- the face open for the README's one crossing of the anti-trapped half;
    # the mutant restores 489's premise, the face open the whole write
    if "whole_write" in MUT:
        F2 = _load("face2_open.py", "f2r_f2w")
        return F2.write_and_open()["tau_w"], 4.0 * 1e60, "write"
    return 2.0, 4.0, "release"                                       # bounds: 2 r_h/c (H9) and 2 r_0/c = 4 GM/c^3 (G8)


# ------------------------------------------------------------------ V3, V4
def hold(T_s, T_l):
    F2 = _load("face2_open.py", "f2r_f2")
    w = F2.write_and_open(); tq = F2.t_quantum(w)
    E_over_eps = w["E"] / (w["P_tot"] * w["clock"])
    neg_s = math.exp(min(T_s, 700)) / (2 * E_over_eps)                        # mu_neg / E after T_open (W4: |eps| e^(kappa t))
    E_over_eps_L = w["E_L"] / (w["P_L"] * 4 * w["gm"])
    efolds_L = T_l / 4.0                                             # kappa = 1/(4M): one e-fold per 4 clocks
    neg_l = math.exp(min(efolds_L, 700)) / (2 * E_over_eps_L)
    trap_s = 0.28 * w["E"] * math.exp(-min(T_s, 700))                          # Barcelo's criterion (W3)
    trap_l = 0.28 * w["E_L"] * math.exp(-min(efolds_L, 700))
    # expected perturbing particles within T_open (W3's rates, scaled from the period it used)
    pt = F2.perturbations(w)
    scale_s = T_s / w["T_open"]
    scale_l = T_l / w["T_open_L"]
    cnt_s = {k: v * scale_s for k, v in pt["counts"].items()}
    cnt_l = {k: v * scale_l for k, v in pt["counts_L"].items()}
    # the large end by energy: the hottest environment computed (a 1e10 K blackbody) onto the capture disc within T_open
    sig = 5.670374419e-8
    disc_L = math.pi * (1.5 * math.sqrt(3) * w["r0"]) ** 2
    hot_l = sig * 1e10 ** 4 * disc_L * T_l * w["gm"]
    return dict(tq=tq, neg_s=neg_s, neg_l=neg_l, ratio_s=tq["t_q"] / T_s, ratio_l=tq["t_qL_clocks"] / T_l,
                trap_s=trap_s, trap_l=trap_l, cnt_s=cnt_s, cnt_l=cnt_l, hot_l=hot_l)


# ------------------------------------------------------------------ V5
def entropy():
    N, l5 = sp.symbols("N l5", positive=True)
    rh = (2 * N * sp.log(2) / sp.pi ** 2) ** sp.Rational(1, 3) * l5    # G3
    A = 2 * sp.pi ** 2 * rh ** 3                                      # the 3-sphere's area
    return sp.simplify(A / (4 * l5 ** 3) - N * sp.log(2)) == 0


def compute():
    tr = transition()
    T_s, T_l, kind = open_period(tr)
    return dict(words=words(), tr=tr, T_s=T_s, T_l=T_l, kind=kind, h=hold(T_s, T_l), ent=entropy())


def checks(o):
    tr, h = o["tr"], o["h"]
    nuc = [v for k, v in h["cnt_s"].items() if "nucleus" in k][0]
    bb3 = [v for k, v in h["cnt_s"].items() if "3 K" in k][0]
    return [("V0: M's 163, 390, 432 (2) and 491 verbatim in the rulings", o["words"]),
            ("V1: transition5q run here: one transition surface, position 2's white hole at T_WH = 2 T_T, its mass ours "
             "to 1e-30, the crossing 2 r_h/c, the anti-trapped half 1.000",
             tr["ck"]["H5"] and tr["ck"]["H6"] and tr["ck"]["H9"] and tr["mwh"] < 1e-30 and abs(tr["tau"] - 2) < 0.01
             and abs(tr["half"] - 1) < 0.005),
            ("V2-V3: position 2's face open for the release at most 2 r_h/c (4 clocks of GM/c^3); the vacuum's negative "
             "mass reaches 2.2e-15 of the face's at the example, 1.4e-67 at the Earth cap; t_q 17.9 and 155 times the "
             "open period", o["kind"] == "release" and "%.2g" % h["neg_s"] == "2.2e-15" and "%.2g" % h["neg_l"] == "1.4e-67"
             and "%.1f" % h["ratio_s"] == "17.9" and round(h["ratio_l"]) == 155),
            ("V4: a perturbation must carry 4.9e7 J (example), 5.5e40 J (Earth cap) to trap the face within T_open; "
             "expected particles within it 9.9e-16 inside a nucleus, 4.8e-51 in a 3 K bath (example); a 1e10 K "
             "blackbody delivers 5.6e19 J within it (Earth cap)",
             "%.2g" % h["trap_s"] == "4.9e+07" and "%.2g" % h["trap_l"] == "5.5e+40" and "%.2g" % nuc == "9.9e-16"
             and "%.2g" % bb3 == "4.8e-51" and "%.2g" % h["hot_l"] == "5.6e+19" and h["hot_l"] < 1e-20 * h["trap_l"]),
            ("V5: position 2's face (equal area) holds exactly N ln2 = A/(4 l5^3): the README passes whole at the "
             "covariant bound", o["ent"])]


def report(o=None):
    o = o or compute(); tr, h = o["tr"], o["h"]
    print("face2_release.py -- what stands at position 2, and its face over its open period (item 491)\n")
    print("V1 transition5q: H5 %s, H6 %s, H9 %s; m_WH/m_BH - 1 <= %.1e; crossing %.4f r_h/c, anti-trapped half %.4f"
          % (tr["ck"]["H5"], tr["ck"]["H6"], tr["ck"]["H9"], tr["mwh"], tr["tau"], tr["half"]))
    print("V2 open period (%s): <= %.3g clocks (small end), <= %.3g clocks of GM/c^3 (large end)" % (o["kind"], o["T_s"],
                                                                                                o["T_l"]))
    print("V3 negative mass / E after T_open: %.2g (example), %.2g (Earth cap); t_q / T_open %.1f and %.0f"
          % (h["neg_s"], h["neg_l"], h["ratio_s"], h["ratio_l"]))
    print("V4 energy to trap within T_open: %.2g J (example), %.2g J (Earth cap); expected particles (example): %s; "
          "1e10 K blackbody within T_open (Earth cap) %.2g J" % (h["trap_s"], h["trap_l"], ", ".join(
              "%s %.1e" % (k.split(" (")[0], v) for k, v in h["cnt_s"].items()), h["hot_l"]))
    print("V5 A/(4 l5^3) = N ln2 exactly: %s" % o["ent"])


MUTANTS = {"whole_write": "489's premise restored: position 2's face open the whole write (V2-V4)"}


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
        failed = [n_.split(":")[0] for n_, ok in checks(compute()) if not ok]
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
