#!/usr/bin/env python3
"""passage_est.py -- item 486 (1): the README's bits carried by established physics, and the passage proved on it.
M, 486: "let's shift to the established physics and prove the passage is still true. If so, it supersedes 432(1)".
Labels: computed (exact unless marked), deduced, READ, estimate, M's.  Worked in the conversation; not verified; not
seated.

Held against the exclusions first (481, 484): every face below is the uncharged hole, Tangherlini at each instant, its
lapse with one root -- no inner horizon, no Cauchy horizon -- and the interior is transition5q's (no bounce changed).

The established physics used, and nothing else: information is carried by distinguishable states (quantum mechanics);
radiation's most states at fixed energy and volume (thermodynamics, source_spec U4); the first law of black holes and
energy conservation; Hawking emission and its ingoing negative flux (quantum fields in curved spacetime); unitary
propagation of a quantum field on a globally hyperbolic background.

  Q0 (read) M's words, verbatim in the rulings file: 486.
  Q1 (computed, source_spec U4) A delivery all at once holds 7.6e-4 of the README's bits at one face clock and none at
     width zero: so on established physics the bits cannot come in with the energy that opens the face.
  Q2 (computed, exact) The first law, dM = T dS, holds for the face at both ends (5D Tangherlini, 4D Schwarzschild);
     so the face's size holds exactly when its energy does, dA/dt proportional to dM/dt = P_in - P_H.
  Q3 (computed, exact) The face can hold its size while energy crosses it.  On Vaidya the face's one Einstein component
     is G_vv = 3 mu'/(2 r^3) with mu' set by the net flux; Hawking emission feeds the face a negative flux that carries
     exactly -P_H (energy conservation: an isolated face loses P_H), so an inflow absorbed at P_in = P_H gives mu' = 0
     and the face static (theta = 0, sigma = 0 for a round inflow).  settle_arrival A1's "nothing crosses after the
     opening" holds for the net null energy; its premise, null energy >= 0 on classical rays (183), is untouched.
  Q4 (computed) The write, at that balance.  The inflow carries the README at the face's own temperature (detailed
     balance fixes T_in = T_H for a round, full-capture inflow absorbed at P_H), with entropy (5/4) E/T in the bulk:
     tau_write = (4/5) N ln2 kT_H / P_H = (16/15) of the record's life (hold_small L5, exact), 48 N ln2/(g* gamma) face
     clocks -- 9.2e14 clocks, 3.4e-14 s, at the example README; 58 clocks for the copper block's 174 bits.  The inflow's
     energy is (8/15) E5(N), exactly; the face returns it to our side as its Hawking emission and holds E5(N) the whole
     time.  The thermal inflow saturates source_spec's room bound exactly (S = N ln2 in the volume it sweeps).  At the
     large end: tau_write = 3 N ln2/(32 pi alpha) clocks of GM/c^3 = 10.9 N (Z = 108.75), the inflow (3/8) E(N).
  Q5 (computed) The README's quanta cross to position 2, unitarily.  A massless field's modes e^(ikx) on the interior
     transition5q computes (ds^2 = -N^2 dT^2 + A^2 dx^2 + B^2 dOmega_3^2), evolved from our horizon to position 2's: the
     Klein-Gordon norm is kept to 6e-8 and |alpha|^2 - |beta|^2 = 1 to 6e-8 for every k -- the passage is a unitary map.
     Quanta near the face's own wavelength are squeezed by the transition (|beta|^2 from 0.7 to 7.7) by a known map that
     position 2 inverts exactly; once the adiabatic parameter falls below 0.1 they pass unmixed (|beta|^2 < 1e-9 at
     k r_h = 1e5), the threshold in k r_h growing as mu^(3/4).
  Q6 (computed; estimate in its quantum count) The face's size at balance fluctuates as the quanta cross: about
     sqrt(n) quanta's worth, 1.6e8 bits of 2.74e15 at the example README (5.7e-8), zero in the mean.
  Q7 (deduced) So the passage holds on established physics.  The face opens all at once with E5(N) (source_spec U2);
     the README streams in over tau_write, absorbed at the face's own emission so the face stands at its size (162,
     163's "one whole" at a fixed size, 158 (2) "exactly as long as the write needs", 426 M-LONG-WRITE -- and 426's open
     question, what balances the face while energy crosses, answered: its own Hawking emission); each quantum crosses
     the interior in 2 r_h/c (H9), unitarily (Q5), into position 2's white hole; one way (O1a).  The README's bits are
     the inflow's states: 432 (1) is not needed and is superseded as their carrier.  What it costs: the supply is E5(N)
     plus (8/15) E5(N), the face holding exactly E5(N) throughout; the passage's interior rests, as before, on 273's
     basis (transition5r: 415's shared onset), which is the one premise left beyond established physics.

python3 passage_est.py [--selftest | --mutants]
"""
import os, sys, math, re, io, contextlib, importlib.util
import numpy as np
import sympy as sp
import scipy.integrate as si
import scipy.optimize as so

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = set()
WORDS = ((486, "let's shift to the established physics and prove the passage is still true. If so, it supersedes 432(1)"),)
ZETA5, ZETA6, ZETA3, ZETA4 = 1.0369277551433699, 1.0173430619844491, 1.2020569031595942, math.pi ** 4 / 90


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


def _item(n):
    txt = open(RULINGS, encoding="utf-8").read()
    m = re.search(r"^%d\. .*?(?=^\d{3}\. |\Z)" % n, txt, re.M | re.S)
    return " ".join(m.group(0).split()) if m else ""


def words():
    return all(w in _item(n) for n, w in WORDS)


# ------------------------------------------------------------------ Q1
def all_at_once():
    SS = _load("source_spec.py", "pe_ss")
    k = SS.consts(); d = SS.energy_check(k); W = SS.window(k, d)
    R = SS.room(k, d, W)
    return dict(small=R[("small", 8)]["ratio"], cap=R[("the Earth cap", 8)]["ratio"], k=k, d=d)


# ------------------------------------------------------------------ Q2, Q3
def first_law():
    r, c, G, hb, kB, G5 = sp.symbols("r c G hbar k_B G5", positive=True)
    M5 = 3 * sp.pi * r ** 2 * c ** 4 / (8 * G5); S5 = kB * 2 * sp.pi ** 2 * r ** 3 * c ** 3 / (4 * G5 * hb)
    T5 = hb * c / (2 * sp.pi * kB * r)
    M4 = r * c ** 4 / (2 * G); S4 = kB * 4 * sp.pi * r ** 2 * c ** 3 / (4 * G * hb)
    T4 = hb * c / (4 * sp.pi * kB * r)
    ok5 = sp.simplify(sp.diff(M5, r) / sp.diff(S5, r) - T5) == 0
    ok4 = sp.simplify(sp.diff(M4, r) / sp.diff(S4, r) - T4) == 0
    # E/N at the face: (3/2) kT ln2 (5D), 2 kT ln2 (4D), with N ln2 = S/k_B
    e5 = sp.simplify(M5 / (S5 / kB * T5 * kB)); e4 = sp.simplify(M4 / (S4 / kB * T4 * kB))
    return dict(ok5=ok5, ok4=ok4, e5=e5, e4=e4)


def balance():
    """Vaidya with mu' set by the net flux: G_vv = 3 mu'/(2 r^3); P_in = P_H gives mu' = 0"""
    v, r = sp.symbols("v r", positive=True)
    Pin, PH, kap = sp.symbols("P_in P_H kappa", positive=True)
    mudot = kap * (Pin - PH) if "nohawking" not in MUT else kap * Pin
    Gvv = 3 * mudot / (2 * r ** 3)
    return dict(static=sp.simplify(Gvv.subs(Pin, PH)) == 0, grows=sp.simplify(Gvv.subs(PH, 0)) != 0)


# ------------------------------------------------------------------ Q4
def write_time(A):
    k, d = A["k"], A["d"]
    N, E5, rh = d["N"], d["E"], d["rh"]
    ln2 = math.log(2)
    gstar, gam = 106.75, 0.93                                        # hold_small L5: the record's species and greybody
    life = 45 * N * ln2 / (gstar * gam)                              # face clocks, hold_small L5
    kT = k["hbar"] * k["c"] / (2 * math.pi * rh)
    PH = E5 / (2 * life * rh / k["c"])                               # the record's power: life = E/(2P)
    ent = 1.25 if "entropy" not in MUT else 4 / 3                    # bulk inflow: S = (5/4) E/T
    tau = (1 / ent) * N * ln2 * kT / PH
    tau_cl = tau * k["c"] / rh
    E_in = PH * tau
    # the copper block's README, 174 bits
    L = _load("ledger.py", "pe_ledger")
    Ec, rhc, _ = L.e_small(174, 1.0)
    tau_cu = (1 / ent) * 174 * ln2 * (45 * 174 * ln2 / (gstar * gam)) * 2 * (k["hbar"] * k["c"] / (2 * math.pi * rhc)) / Ec
    # exact ratios
    n_, kT_, life_ = sp.symbols("N kT life", positive=True)
    E5s = sp.Rational(3, 2) * n_ * kT_ * sp.log(2)
    PHs = E5s / (2 * life_)
    taus = sp.Rational(4, 5) * n_ * sp.log(2) * kT_ / PHs
    ratio_life = sp.simplify(taus / life_); ratio_E = sp.simplify(PHs * taus / E5s)
    # the room bound, saturated: S_max(E_in, V swept) for a 5D thermal gas at T_H equals N ln2
    SS = _load("source_spec.py", "pe_ss2")
    a5 = SS.a5(8, k); u = a5 * kT ** 5
    V = E_in / u
    S_room = SS.s5(E_in, V, 8, k) / (N * ln2)
    # large end: P = alpha/M^2, T = 1/(8 pi M), life >= M^3/(3 alpha) (close_large L3), 4D inflow S = (4/3) E/T
    Z = 108.75; alpha = 27 * Z / (491520 * math.pi)
    per_N = 3 * ln2 / (32 * math.pi * alpha)                         # clocks of GM/c^3 per bit
    M_, al_ = sp.symbols("M alpha", positive=True)
    E4 = M_; PH4 = al_ / M_ ** 2; T4 = 1 / (8 * sp.pi * M_); N4ln2 = 4 * sp.pi * M_ ** 2
    tau4 = sp.Rational(3, 4) * N4ln2 * T4 / PH4
    ratio_E4 = sp.simplify(PH4 * tau4 / E4)
    return dict(life=life, tau=tau, tau_cl=tau_cl, tau_ratio=tau_cl / life, E_ratio=E_in / E5, tau_cu=tau_cu,
                ratio_life=ratio_life, ratio_E=ratio_E, S_room=S_room, per_N=per_N, ratio_E4=ratio_E4, kT=kT, PH=PH,
                E_in=E_in)


# ------------------------------------------------------------------ Q5
def _geo(mu):
    pmin = 72 ** 0.25 * math.sqrt(mu); dc = pmin / (3 * mu); kk = 1.5 * dc; TT = math.log(kk)
    db = so.brentq(lambda d: math.sqrt(1 + d * d) * TT + 2 * math.atanh(1 / math.sqrt(1 + d * d)), 1e-6, 2)
    bo = math.sqrt(1 + db * db); TWH = -4 * math.atanh(1 / bo) / bo
    def st(T):
        Pc = mu * (math.exp(T) + kk * kk * math.exp(-T))
        tt = math.tanh(bo * T / 2)
        sinb = math.sqrt(max(0.0, -db * db * tt * (2 * bo + tt * (1 + bo * bo)))) / abs(bo + tt)
        Pb = mu * sinb * db / (sinb ** 2 + db ** 2)
        B = math.sqrt(Pc); A = Pb / Pc; N = B * db / (2 * sinb)
        return N, A, B
    return st, TT, TWH


def modes(mu, kr, qtol=1e-4):
    """the mode e^(ikx) of a massless field: d/dT (A B^3/N df/dT) = -(N B^3/A) k^2 f; in and out modes WKB where the
    adiabatic parameter is below qtol, near each horizon"""
    st, TT, TWH = _geo(mu)
    kk = kr / math.sqrt(mu)
    def wz(T):
        N, A, B = st(T); return N * kk / A, A * B ** 3 / N
    def Q(T, h=1e-6):
        w1, z1 = wz(T - h); w2, z2 = wz(T + h); w, z = wz(T)
        return max(abs((w2 - w1) / (2 * h)) / w ** 2, abs((z2 - z1) / (2 * h)) / (z * w))
    grid = np.linspace(TWH + 1e-3, -1e-3, 4001)
    qs = np.array([Q(T) for T in grid])
    bad = np.where(qs > qtol)[0]
    T1, T0 = grid[max(bad[0] - 1, 0)], grid[min(bad[-1] + 1, len(grid) - 1)]
    damp = 1e-3 if "lossy" in MUT else 0.0
    def rhs(T, y):
        N, A, B = st(T)
        f = y[0] + 1j * y[1]; p = y[2] + 1j * y[3]
        df = N * p / (A * B ** 3); dp = -(N * B ** 3 / A) * kk * kk * f + damp * p
        return [df.real, df.imag, dp.real, dp.imag]
    om0, Z0 = wz(T0)
    f0 = (Z0 * om0) ** -0.5; p0 = Z0 * (1j * om0) * f0
    sol = si.solve_ivp(rhs, (T0, T1), [f0.real, f0.imag, p0.real, p0.imag], method="DOP853", rtol=1e-10, atol=1e-14)
    f = sol.y[0] + 1j * sol.y[1]; p = sol.y[2] + 1j * sol.y[3]
    W = np.imag(np.conj(f) * p)
    om1, Z1 = wz(T1); u = (Z1 * om1) ** -0.5
    a = (f[-1] / u + p[-1] / (1j * om1 * Z1 * u)) / 2; b = (f[-1] / u - p[-1] / (1j * om1 * Z1 * u)) / 2
    return dict(Wdrift=abs(W[-1] / W[0] - 1), unit=abs(abs(a) ** 2 - abs(b) ** 2 - 1), b2=abs(b) ** 2, qmax=qs.max())


# ------------------------------------------------------------------ Q6
def fluctuation(A, Wt):
    N, E5 = A["d"]["N"], A["d"]["E"]
    kT = Wt["kT"]
    e_in = 5 * ZETA6 / ZETA5 * kT                                    # mean quantum, 5D thermal inflow
    e_out = 3 * ZETA4 / ZETA3 * kT                                   # mean quantum, the plane's emission (4D)
    n_in = Wt["E_in"] / e_in; n_out = Wt["E_in"] / e_out
    dM = math.sqrt(n_in * e_in ** 2 + n_out * e_out ** 2)
    dbits = dM / (kT * math.log(2))
    return dict(dbits=dbits, rel=dbits / N)


def compute():
    o = dict(words=words(), A=all_at_once(), fl=first_law(), bal=balance())
    o["W"] = write_time(o["A"])
    o["modes"] = {(mu, kr): modes(mu, kr) for mu, kr in ((1e4, 0.3), (1e4, 1.0), (1e4, 10.0), (1e4, 100.0),
                                                          (1e4, 1e3), (1e4, 1e5), (1e6, 1.0), (1e6, 1e5))}
    o["fluct"] = fluctuation(o["A"], o["W"])
    return o


def checks(o):
    A, fl, b, W, Mo, F = o["A"], o["fl"], o["bal"], o["W"], o["modes"], o["fluct"]
    q0 = o["words"]
    q1 = A["small"] < 1e-2 and A["cap"] < 1e-10
    q2 = fl["ok5"] and fl["ok4"] and fl["e5"] == sp.Rational(3, 2) and fl["e4"] == 2
    q3 = b["static"] and b["grows"]
    q4 = (W["ratio_life"] == sp.Rational(16, 15) and W["ratio_E"] == sp.Rational(8, 15) and W["ratio_E4"] == sp.Rational(3, 8)
          and abs(W["tau_ratio"] - 16 / 15) < 1e-9 and abs(W["E_ratio"] - 8 / 15) < 1e-9 and abs(W["S_room"] - 1) < 1e-9
          and 9.0e14 < W["tau_cl"] < 9.3e14 and 50 < W["tau_cu"] < 70 and 10 < W["per_N"] < 12)
    unit = all(m["unit"] < 1e-5 and m["Wdrift"] < 1e-6 for m in Mo.values())
    mixed = all(Mo[(1e4, kr)]["b2"] > 0.1 for kr in (0.3, 1.0, 10.0)) and Mo[(1e6, 1.0)]["b2"] > 0.1
    clean = Mo[(1e4, 1e5)]["b2"] < 1e-8 and Mo[(1e6, 1e5)]["b2"] < 1e-8
    expo = math.log(Mo[(1e6, 1.0)]["qmax"] / Mo[(1e4, 1.0)]["qmax"]) / math.log(100)
    q5 = unit and mixed and clean and abs(expo - 0.75) < 0.05
    q6 = 1e-9 < F["rel"] < 1e-5
    return dict(Q0=q0, Q1=q1, Q2=q2, Q3=q3, Q4=q4, Q5=q5, Q6=q6)


def report(o=None):
    o = o or compute(); ck = checks(o); W = o["W"]; A = o["A"]
    print("Q0 M's words: %s" % o["words"])
    print("Q1 a delivery all at once holds %.2g of N (small end), %.2g (Earth cap) at one clock" % (A["small"], A["cap"]))
    print("Q2 first law dM = T dS: 5D %s, 4D %s; E/(N kT ln2) = %s (5D), %s (4D)" % (
        o["fl"]["ok5"], o["fl"]["ok4"], o["fl"]["e5"], o["fl"]["e4"]))
    print("Q3 the net flux sets mu': static at P_in = P_H %s; grows without the Hawking flux %s" % (
        o["bal"]["static"], o["bal"]["grows"]))
    print("Q4 small end: tau_write = %s of the life, the inflow %s of E5(N) (exact); %.3g face clocks = %.2g s at the "
          "example README (life %.3g clocks); %.3g clocks for 174 bits; the room saturated, S/(N ln2) = %.12f.  Large "
          "end: tau_write = %.3g N clocks of GM/c^3, the inflow %s of E(N)" % (
              W["ratio_life"], W["ratio_E"], W["tau_cl"], W["tau"], W["life"], W["tau_cu"], W["S_room"], W["per_N"],
              W["ratio_E4"]))
    for (mu, kr), m in o["modes"].items():
        print("Q5 mu/l5^2 %.0e, k r_h %-7g: KG norm drift %.1e, |alpha|^2 - |beta|^2 - 1 = %.1e, |beta|^2 %.3e, "
              "adiabatic Q max %.2e" % (mu, kr, m["Wdrift"], m["unit"], m["b2"], m["qmax"]))
    print("Q6 the face at balance fluctuates by %.2g bits of N (%.1e)" % (o["fluct"]["dbits"], o["fluct"]["rel"]))
    for kk, vv in ck.items():
        print("%s %s" % (kk, vv))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["nohawking", "entropy", "lossy"]
    for m_ in names:
        MUT.clear(); MUT.add(m_)
        try:
            r_ = selftest(quiet=True)
        except Exception:
            r_ = False
        caught += not r_; print("mutant %-10s %s" % (m_, "caught" if not r_ else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
