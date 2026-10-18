#!/usr/bin/env python3
"""face2_hold.py -- item 490: work on FACE2s / FACE2 (opened at 489), position 2's face holding through its open period.

face2_open (489) showed that in position 2's vacuum the face lasts t_q = 35.8 clocks against an open period of 8.63e14,
and that one state would hold it: the time reverse of our face's state.  It did not claim that no other state or
mechanism holds the face.  This instrument asks that question: could a shorter white phase, a bath at position 2, or a
correlated incoming state hold the face?  Labels: computed (exact unless marked), deduced, READ.

  K0 (read) M's words, verbatim in the rulings file: 490.
  K1 (READ, prior art first, 442) A white-hole face is unstable classically to matter coming in from its own side
     (Eardley, PRL 33, 442 (1974)) and quantum mechanically: the first-order stress diverges along its horizon
     (Zel'dovich, Novikov and Starobinsky, JETP 39, 933 (1974)), with an infinite flux at future null infinity where the
     horizon ends (Wald and Ramaswamy, PRD 21, 2736 (1980)).  So a white-hole phase must be short (Barcelo, Carballo-Rubio
     and Garay, JHEP 01 (2016) 157).  It is stable only to perturbations of its future data, never of its past data,
     and only a Planck-size face escapes this, by loop quantum gravity's area gap (Rovelli and Vidotto, arXiv:1805.03872;
     Bianchi et al., arXiv:1802.04264), which is not established physics.
  K2 (computed, exact) The white phase cannot be made short.  Through the face's area A, in time t, radiation of energy E
     carries at most S = (4/3) (a A t)^(1/4) E^(3/4) (the thermal maximum).  So at fixed S = N ln2 the least time scales
     as E^-3: t_min = tau_w (E_in / E_out)^3.  The face can give out no more than it holds, E_out <= E_in + E, so
     t_min >= tau_w / 27 = 3.2e13 clocks at the example and (3/11)^3 tau_w = 3.0e65 clocks of GM/c^3 at the Earth cap.
     Both are against t_q = 35.8 clocks and 620 clocks.  The bulk channel is slower (passage_est Q4), and the coding
     fraction F only lengthens the write (Q5).
  K3 (computed, exact in the s-wave model) The hold condition.  A bath at temperature T coming in from position 2 sets
     the net ingoing stress at the face to T_vv = (pi/12) (T^2 - T_H^2).  This is zero only at T = T_H, where it vanishes
     as f^2 (regular).  With T = T_H (1 + delta), the face lasts t_q(delta) = t_q + ln(1/|2 delta + delta^2|), where
     vacuum is delta = -1.  So holding it through the open period needs |2 delta + delta^2| <= e^(-(T_open - t_q)):
     10^(-3.75e14) at the example.  A bath too hot traps the face (Eardley's black hole, the crossing's f_fut < 0); one
     too cold leaves the negative mass of face2_open W4.  A cosmic background like ours, 2.725 K, against the Earth-cap
     face's T_H of 0.0205 K, ends it after 145 e-folds.
  K4 (computed) The face's own fluctuation floors the mismatch for any bath that is not correlated with the face.  Its
     mass moves by whole quanta, mean 2.701 k T_H each, which by the first law is 3.90 bits.  T_H goes as N^(-1/3) (5D)
     or N^(-1/2) (4D), so one quantum moves T_H by 4.7e-16 at the example and 1.4e-66 at the Earth cap.  The face then
     lasts 70.4 clocks at the example and 306 e-folds (1224 clocks) at the Earth cap.  Over the write it drifts by
     1.3e8 bits (passage_est Q6), which gives 53.1 clocks.  No bath at fixed T reaches T_open.
  K5 (computed, exact) The correlated state is excluded by monogamy.  To track the face, the incoming radiation must be
     the time reverse of our face's Hawking radiation.  It must therefore purify the partner modes that position 2's
     face emits (b_bounce Q1's isometry carries our face's infalling partners there), with mutual information 2 g(n)
     per mode: 0.0272 nats at k r_h = 1, 2.96 at k r_h = 0.1.  Those partners are in a pure two-mode state with our
     Hawking radiation (Hawking's state; M's 336 keeps them in the core), so their mutual information with any third
     system is exactly 0.  The covariance matrices are computed: I(A:C) = 0 for every coupling of C.  No channel brings
     our Hawking radiation to position 2's past null infinity either: the corridor is one way (O1a) and emerges at the
     face.
  K6 (deduced) So FACE2s and FACE2 as posed -- a semiclassical white-hole face at position 2 held through the write --
     are not merely unproved: established physics refutes them.  No state of position 2's fields holds the face over
     T_open (K3-K5), and the white phase cannot be cut to fit t_q (K2).  More computation of the same object cannot
     prove the rows; what stands at position 2 must change, and that is M's to decide (414).  Two candidates are left by
     established physics: (a) position 2's face a black hole, stable to its past data, with the README emerging in its
     radiation, which changes 447's dictionary (a white hole at position 2); (b) a horizonless mouth at position 2,
     whose throat must be held open as in 445 (2).  A Planck-size white hole (K1) rests on physics beyond the
     established, so 441 (1) cannot prove it.

What this does not claim: anything beyond the s-wave model for the stress, or about either candidate beyond naming it.

python3 face2_hold.py [--selftest | --mutants]
"""
import os, sys, math, re, io, contextlib, importlib.util
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORD = (490, "Start the work on the new open objects of the warp theorem")
Q_MEAN = 3 * 1.0823232337111382 / 1.2020569031595942                 # mean quantum / kT, 4D thermal radiation: 2.701
T_CMB = 2.725


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % WORD[0], txt, re.M | re.S)
    return bool(m) and WORD[1] in " ".join(m.group(0).split())


# ------------------------------------------------------------------ K2
def short_phase(w):
    a, A, t, E, S = sp.symbols("a A t E S", positive=True)
    Smax = sp.Rational(4, 3) * (a * A * t) ** sp.Rational(1, 4) * E ** sp.Rational(3, 4)
    tsol = sp.solve(sp.Eq(Smax, S), t)[0]
    E1, E2 = sp.symbols("E1 E2", positive=True)
    ratio = sp.simplify(tsol.subs(E, E2) / tsol.subs(E, E1))           # t(E2)/t(E1) at fixed S, A
    e_out = 1.0 if "all_out" in MUT else None                        # mutant: the face gives out only the README
    f_s = float(ratio.subs({E1: 0.5, E2: e_out if e_out else 1.5}))
    f_l = float(ratio.subs({E1: sp.Rational(3, 8), E2: (sp.Rational(3, 8) if e_out else sp.Rational(11, 8))}))
    return dict(ratio=ratio, f_s=f_s, f_l=f_l, tmin_s=w["tau_w"] * f_s, tmin_l=w["tau_L"] * f_l)


# ------------------------------------------------------------------ K3
def hold_condition(w, tq):
    r, M, T = sp.symbols("r M T", positive=True)
    f = 1 - 2 * M / r
    Tvv_B = -M * (2 * r - 3 * M) / (48 * sp.pi * r ** 4)              # face2_open W4 (Boulware, s-wave)
    TH = 1 / (8 * sp.pi * M)
    Tvv = sp.pi * T ** 2 / 12 + Tvv_B                                 # a thermal bath at T coming in, plus the vacuum's
    at_face = sp.simplify(Tvv.subs(r, 2 * M))
    form = sp.simplify(at_face - sp.pi / 12 * (T ** 2 - TH ** 2)) == 0
    regular = sp.simplify(sp.limit(Tvv.subs(T, TH) / f ** 2, r, 2 * M)) != sp.oo and \
        sp.simplify(Tvv.subs(T, TH).subs(r, 2 * M)) == 0
    tq0 = tq["t_q"]
    t_of = lambda d: tq0 + math.log(1 / abs(2 * d + d * d))
    need_log10 = -(w["T_open"] - tq0) / math.log(10)
    THL = 1.0 / (8 * math.pi) * w["k"]["hbar"] * w["k"]["c"] ** 3 / (w["k"]["G"] * w["M"] * 1.380649e-23)
    dL = T_CMB / THL - 1
    tL_cmb = tq["t_qL_efolds"] + math.log(1 / abs(2 * dL + dL * dL))
    # a bath too hot: ingoing e > 0 meets the README Delta at r_h + delta (DTR, face2_open W4's algebra, 5D)
    mu, D, e, dl, rh = sp.symbols("mu Delta e delta r_h", positive=True)
    R = rh + dl
    fx = lambda m: 1 - m / R ** 2
    f_fut = fx(mu - D) * fx(mu + e) / fx(mu)
    hot = float(f_fut.subs({mu: 1, rh: 1, dl: 1e-3, D: 1e-2, e: 3e-3}))  # e above 2 delta r_h: f_fut < 0, trapped
    return dict(form=form, regular=regular, t_of=t_of, vac=t_of(-1.0), need_log10=need_log10, THL=THL,
                tL_cmb=tL_cmb, hot_traps=hot < 0)


# ------------------------------------------------------------------ K4
def fluctuation_floor(w, tq):
    PE = _load("passage_est.py", "fh_pe")
    A = PE.all_at_once(); Wt = PE.write_time(A); fl = PE.fluctuation(A, Wt)
    dN_q = Q_MEAN / math.log(2)                                       # bits per quantum: dS = dM / T, S = N ln2
    p5, p4 = (1.0 if "no_power" in MUT else 1 / 3), 0.5
    dT_s = p5 * dN_q / w["N"]
    dT_l = p4 * dN_q / 1.3651e66
    t_s = tq["t_q"] + math.log(1 / (2 * dT_s))
    t_l = tq["t_qL_efolds"] + math.log(1 / (2 * dT_l))
    dT_w = p5 * fl["rel"]
    t_w = tq["t_q"] + math.log(1 / (2 * dT_w))
    return dict(dN_q=dN_q, dT_s=dT_s, dT_l=dT_l, t_s=t_s, t_l=t_l, t_lc=4 * t_l, dT_w=dT_w, t_w=t_w,
                rel=fl["rel"])


# ------------------------------------------------------------------ K5
def _S(V):
    """von Neumann entropy (nats) of a Gaussian state from its covariance matrix (vacuum = identity/2)"""
    n = V.shape[0] // 2
    Om = np.kron(np.eye(n), np.array([[0, 1], [-1, 0]]))
    nu = np.sort(np.abs(np.linalg.eigvals(1j * Om @ V)))[::2]
    return sum((x + 0.5) * math.log(x + 0.5) - (x - 0.5) * math.log(x - 0.5) if x > 0.5 + 1e-12 else 0.0 for x in nu)


def _sub(V, idx):
    ii = [2 * i + j for i in idx for j in (0, 1)]
    return V[np.ix_(ii, ii)]


def monogamy():
    out = {}
    for kr in (0.1, 1.0):
        nbar = 1 / math.expm1(2 * math.pi * kr)
        rr = math.asinh(math.sqrt(nbar))
        ch, sh = math.cosh(2 * rr) / 2, math.sinh(2 * rr) / 2
        Z = np.diag([1, -1])
        Vab = np.block([[ch * np.eye(2), sh * Z], [sh * Z, ch * np.eye(2)]])   # A partner, B our Hawking mode: pure
        I_AB = _S(_sub(Vab, [0])) + _S(_sub(Vab, [1])) - _S(Vab)
        worst = 0.0
        for g in (0.0, 0.3, 1.0, 3.0):                                # C, position 2's incoming mode, any state
            Vc = (0.5 + g) * np.eye(2)
            V = np.zeros((6, 6)); V[:4, :4] = Vab; V[4:, 4:] = Vc
            if "leak" in MUT:                                         # mutant: C correlated with A while AB stays pure
                V[0, 4] = V[4, 0] = V[1, 5] = V[5, 1] = 0.05
            I_AC = _S(_sub(V, [0])) + _S(_sub(V, [2])) - _S(_sub(V, [0, 2]))
            worst = max(worst, abs(I_AC))
        g_n = (nbar + 1) * math.log(nbar + 1) - nbar * math.log(nbar)
        out[kr] = dict(nbar=nbar, need=2 * g_n, I_AB=I_AB, I_AC=worst, pure=abs(_S(Vab)) < 1e-9)
    return out


def compute():
    F2 = _load("face2_open.py", "fh_f2")
    w = F2.write_and_open(); tq = F2.t_quantum(w)
    return dict(words=words(), w=w, tq=tq, sp_=short_phase(w), hc=hold_condition(w, tq), ff=fluctuation_floor(w, tq),
                mg=monogamy())


def checks(o):
    w, tq, s, h, ff, mg = o["w"], o["tq"], o["sp_"], o["hc"], o["ff"], o["mg"]
    E1, E2 = sp.symbols("E1 E2", positive=True)
    return [("K0: M's 490 verbatim in the rulings", o["words"]),
            ("K2: at fixed entropy through the face t_min goes as E^-3; t_min = tau_w/27 = 3.2e13 clocks at the example, "
             "(3/11)^3 tau_w = 3.0e65 at the Earth cap, against t_q 35.8 and 620",
             sp.simplify(s["ratio"] - (E1 / E2) ** 3) == 0 and "%.2g" % s["tmin_s"] == "3.2e+13"
             and "%.2g" % s["tmin_l"] == "3e+65" and s["tmin_s"] > 1e11 * tq["t_q"]),
            ("K3: a bath at T gives T_vv(face) = (pi/12)(T^2 - T_H^2), regular as f^2 at T_H; t_q(delta) = t_q + ln "
             "1/|2 delta + delta^2| (vacuum 35.8); holding needs 10^(-3.75e14); a 2.725 K background on the Earth-cap "
             "face (T_H 0.0205 K) ends it at 145 e-folds; too hot traps it",
             h["form"] and h["regular"] and "%.1f" % h["vac"] == "35.8" and "%.3g" % h["need_log10"] == "-3.75e+14"
             and "%.3g" % h["THL"] == "0.0205" and round(h["tL_cmb"]) == 145 and h["hot_traps"]),
            ("K4: one quantum (3.90 bits) moves T_H by 4.7e-16 at the example, 1.4e-66 at the Earth cap: the face lasts "
             "70.4 clocks and 306 e-folds; the write's drift (4.6e-8 of N) gives 53.1 clocks",
             "%.2f" % ff["dN_q"] == "3.90" and "%.2g" % ff["dT_s"] == "4.7e-16" and "%.2g" % ff["dT_l"] == "1.4e-66"
             and "%.1f" % ff["t_s"] == "70.4" and round(ff["t_l"]) == 306 and "%.1f" % ff["t_w"] == "53.1"),
            ("K5: the time reverse needs I(partner : incoming) = 2 g(n) per mode, 0.0272 nats at k r_h = 1 and 2.96 at "
             "0.1; the partner is pure with our Hawking mode, so I(partner : any third) = 0",
             all(m["pure"] and m["I_AC"] < 1e-9 and abs(m["I_AB"] - m["need"]) < 1e-9 for m in mg.values())
             and "%.3g" % mg[1.0]["need"] == "0.0272" and "%.3g" % mg[0.1]["need"] == "2.96")]


def report(o=None):
    o = o or compute(); w, tq, s, h, ff, mg = o["w"], o["tq"], o["sp_"], o["hc"], o["ff"], o["mg"]
    print("face2_hold.py -- can anything hold position 2's face through its open period? (item 490)\n")
    print("K2 t_min/tau_w = %s; t_min %.2g clocks (example), %.2g clocks of GM/c^3 (Earth cap); t_q %.1f, %.0f"
          % (s["ratio"], s["tmin_s"], s["tmin_l"], tq["t_q"], tq["t_qL_clocks"]))
    print("K3 T_vv at the face for a bath at T: (pi/12)(T^2 - T_H^2) [%s]; regular at T_H: %s; t_q(vacuum) %.1f; hold "
          "needs |2d + d^2| <= 10^(%.3g); Earth-cap T_H %.3g K, a 2.725 K background ends it at %.0f e-folds"
          % (h["form"], h["regular"], h["vac"], h["need_log10"], h["THL"], h["tL_cmb"]))
    print("K4 one quantum %.2f bits: dT/T %.2g (example) -> %.1f clocks; %.2g (Earth cap) -> %.0f e-folds; the write's "
          "drift %.2g of N -> %.1f clocks" % (ff["dN_q"], ff["dT_s"], ff["t_s"], ff["dT_l"], ff["t_l"], ff["rel"],
                                               ff["t_w"]))
    for kr, m in mg.items():
        print("K5 k r_h %g: n %.3g, needed I 2g(n) %.4g nats, I(partner:Hawking) %.4g, I(partner:third) %.1e"
              % (kr, m["nbar"], m["need"], m["I_AB"], m["I_AC"]))


MUTANTS = {"all_out": "the face's own mass withheld from the white phase (K2)",
           "no_power": "T_H taken as moving one-for-one with N (K4)",
           "leak": "position 2's incoming mode correlated with the partner while partner and Hawking mode stay pure (K5)"}


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
        except Exception as e:                                       # an unphysical state is caught too
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
