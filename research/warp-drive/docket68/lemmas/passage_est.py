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
  Q4 (computed; corrected at 489, F2 of the 488 verification) The write, at that balance, by one channel at a time.
     First written mixing two: the bulk's entropy, (5/4) E/T, against the plane's power -- giving 16/15 and 8/15, wrong.
     The plane's channel: the README as the plane's own radiation at T_H (detailed balance for a round inflow absorbed
     at the plane's share of the power), entropy (4/3) E/T; with N ln2 k T_H = (2/3) E5 (first law) the inflow is
     E5(N)/2 exactly, and tau_write = E_in / P_plane = (1 + b) of the life (hold_small L5, which counts every channel;
     b = 0.0062 the bulk gravitons' share): 8.63e14 face clocks, 3.2e-14 s, at the example README.  The bulk's
     channel, done on its own: 5D radiation absorbed on the capture ball of radius 2 r_h holds the face only at
     T_in = 1.98 T_H, tau = 2.12 lives, the inflow 1.06 E5(N).  The plane's channel is the faster, and the one the
     theorem uses; its thermal inflow saturates the 4D room bound exactly (S = (4/3) E_in / T = N ln2).  At the large
     end (one channel, the plane's): tau_write = 3 N ln2/(32 pi alpha) clocks of GM/c^3 = 10.9 N (Z = 108.75), the
     inflow (3/8) E(N).  [The copper block's 174 bits, quoted here first, lie outside the computed domain, N >= 7.12e9
     (scope.py C2): withdrawn.]
  [Item 491, M: R1's "model and premise are both wrong".  Q5's 489 reading -- each mode alone at position 2, its
  partner kept in the core, an amplifier channel, "error below any epsilon, not exactly" -- is against 418 (whatever
  falls in is the README), 163 (held as one whole), 432 (2) (released whole at the end) and 386, and is withdrawn.  The
  mixing Q5 computes, a' = alpha a + beta b^+, is a unitary on the README's own modes, inverted exactly at position 2
  (r1_exact.py).  Q5's numbers stand as computed; F is the withdrawn premise's figure.  In Q7, "each quantum crosses
  ... toward position 2's white hole" reads: the README, held whole, crosses whole at the write's end.]
  Q5 (computed; corrected at 489, F3) The README's quanta cross the computed interior unitarily: the Klein-Gordon norm
     kept to 6e-8 and |alpha|^2 - |beta|^2 = 1 to 6e-8 for every k computed.  Quanta in the inflow's band (k r_h 0.1 to 30 at
     mu/l5^2 = 1e6) are mixed by the transition, |beta|^2 from 0.16 to 20, with the partner modes -k: the interior
     partners of our face's Hawking quanta, entangled with our Hawking radiation.  First written: "a known map that
     position 2 inverts exactly" -- that needs the partners at position 2, and the theorem keeps them in the core (B4ds
     D7, D15; M's 336, E1x: only the README crosses).  So position 2 holds each README mode alone: an amplifier channel
     of gain 1 + |beta|^2 with the partner's thermal noise.  No finite k inverts exactly (|beta|^2 > 0 at every k, below
     1e-9 only past the adiabatic threshold, k r_h > 5.1e7 at the example); by channel coding (Shannon; the Gaussian
     capacity of phase-insensitive channels, Giovannetti et al., Nat. Photon. 8, 796 (2014), READ) the README is
     recovered with error below any epsilon > 0, not zero, at a rate the channel's capacity bounds: of the thermal
     inflow's entropy, position 2 alone can recover the fraction F computed here (0.30 at mu/l5^2 = 1e4, 0.27 at 1e6,
     falling as the mixing grows with mu), so the write lasts at least tau_write / F.
  Q6 (computed; estimate in its quantum count; worded at 489, F8) The face's size at balance holds in the mean, not at
     every instant: it fluctuates by about sqrt(n) quanta's worth, 1.3e8 bits of 2.74e15 at the example README (4.6e-8),
     and the inflow must match P_H to 1/N (3.6e-16) for the drift over the write to stay below one bit.
     [Item 542, D5: the balance is an unstable equilibrium -- P_H goes as 1/M in five dimensions, so a departure grows
     at P/M, one e-fold per two lives.  Over the write, (1 + b) lives, x = (1 + b)/2 = 0.503: a constant mismatch drifts
     (e^x - 1)/x = 1.30 times what the count above gives, and the random walk's spread sqrt((e^2x - 1)/(2x)) = 1.31
     times -- 1.7e8 bits of 2.74e15, the match 1/(1.30 N).  No verdict moves (computed below).]
  Q7 (deduced) So the passage holds on established physics, with Q5's and Q6's qualifications.  The face opens all at
     once with E5(N) (source_spec U2); the README streams in over tau_write / F, absorbed at the face's own emission so
     the face stands at its size in the mean (162, 163's "one whole" at a fixed size, 426 M-LONG-WRITE); each quantum
     crosses the interior in 2 r_h/c (H9), unitarily (Q5), toward position 2's white hole -- whose holding through the
     write is face2_open's, OPEN (489, F1); one way (O1a).  The README's bits are the inflow's states, recovered at
     position 2 with error below any epsilon, not exactly: 432 (1) is not needed and is superseded as their carrier.
     What it costs: the supply is E5(N) plus E5(N)/2 per tau_write, the face holding E5(N) in the mean throughout; the
     passage's interior rests, as before, on 273's basis (transition5r: 415's shared onset).
     [Item 542, D4: kept as written.  "Whose holding through the write is face2_open's, OPEN" and "with error below any
     epsilon, not exactly" were withdrawn at 491: position 2's face holds through the release (face2_release), and the
     README is recovered exactly by the inverse of the interior's unitary map (r1_exact).  The interior's basis is QB
     since 538.]

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
    """Q4 (corrected at 489): the plane's channel and the bulk's, each consistent; the plane's the theorem's"""
    k, d = A["k"], A["d"]
    N, E5, rh = d["N"], d["E"], d["rh"]
    ln2 = math.log(2)
    HS = _load("hold_small.py", "pe_hs")
    dof = sum(n_ for n_, _ in HS.GREY_SPIN.values())
    gam = sum(n_ * g for n_, g in HS.GREY_SPIN.values()) / dof
    b = HS.GRAV_BULK_DOF / (gam * dof)
    life = 45 * N * ln2 / (dof * gam * (1 + b))                      # face clocks, hold_small L5, every channel
    clock = rh / k["c"]
    kT = k["hbar"] * k["c"] / (2 * math.pi * rh)
    P_tot = E5 / (2 * life * clock)                                  # life = E/(2P) at the small end
    P_pl = P_tot / (1 + b)
    if "entropy" in MUT:                                             # the first version's mix: bulk entropy, plane's power
        ent, P_in = 1.25, P_pl
    else:
        ent, P_in = 4 / 3, P_pl
    E_in = N * ln2 * kT / ent
    tau = E_in / P_in
    tau_cl = tau / clock
    # the bulk's own channel: 5D thermal radiation (Z = 8) on the capture ball radius 2 r_h, at T_in holding the face
    a5 = 8 * 2 * math.pi ** 2 * 24 * ZETA5 / (2 * math.pi * k["hbar"] * k["c"]) ** 4
    vol = 4 / 3 * math.pi * (2 * rh) ** 3
    P_bulk = lambda kTx: k["c"] * a5 * kTx ** 5 * vol
    Tin = (P_tot / P_bulk(kT)) ** 0.2
    tau_bk = 0.8 * N * ln2 * kT * Tin / P_tot / clock
    # exact ratios on the plane's channel
    n_, kT_, life_, bb = sp.symbols("N kT life b", positive=True)
    E5s = sp.Rational(3, 2) * n_ * kT_ * sp.log(2)
    Ptot_s = E5s / (2 * life_)
    taus = sp.Rational(3, 4) * n_ * sp.log(2) * kT_ / (Ptot_s / (1 + bb))
    ratio_life = sp.simplify(taus / life_); ratio_E = sp.simplify(sp.Rational(3, 4) * n_ * sp.log(2) * kT_ / E5s)
    S_room4 = (4 / 3) * E_in / kT / (N * ln2)                        # the 4D thermal inflow's entropy against N ln2
    # large end: P = alpha/M^2, T = 1/(8 pi M), 4D inflow S = (4/3) E/T
    Z = 108.75; alpha = 27 * Z / (491520 * math.pi)
    per_N = 3 * ln2 / (32 * math.pi * alpha)                         # clocks of GM/c^3 per bit
    M_, al_ = sp.symbols("M alpha", positive=True)
    E4 = M_; PH4 = al_ / M_ ** 2; T4 = 1 / (8 * sp.pi * M_); N4ln2 = 4 * sp.pi * M_ ** 2
    tau4 = sp.Rational(3, 4) * N4ln2 * T4 / PH4
    ratio_E4 = sp.simplify(PH4 * tau4 / E4)
    return dict(life=life, tau=tau, tau_cl=tau_cl, tau_ratio=tau_cl / life, E_ratio=E_in / E5, b=b,
                ratio_life=ratio_life, ratio_E=ratio_E, S_room4=S_room4, per_N=per_N, ratio_E4=ratio_E4, kT=kT,
                PH=P_tot, E_in=E_in, Tin_bulk=Tin, tau_bulk=tau_bk / life, Ein_bulk=P_tot * tau_bk * clock / E5)


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


def _g(x):
    return (x + 1) * math.log(x + 1) - (x * math.log(x) if x > 0 else 0.0)


def capacity(mu, krs=(0.1, 0.3, 1.0, 3.0, 10.0, 30.0)):
    """Q5 (489, F3): position 2 holds each README mode alone -- a' = alpha a + beta b^+, the partner b thermal at T_H and
    kept in the core.  Per mode the Gaussian classical capacity at the inflow's own occupation n = 1/(e^(2 pi k r_h) - 1):
    C = g(G n + (G - 1)(n + 1)) - g((G - 1)(n + 1)), G = 1 + |beta|^2; F = int k^2 C dk / int k^2 g(n) dk"""
    rows = []
    for kr in krs:
        b2 = 0.0 if "partners_cross" in MUT else modes(mu, kr)["b2"]
        G = 1 + b2
        n = 1 / math.expm1(2 * math.pi * kr)
        noise = (G - 1) * (n + 1)
        C = _g(G * n + noise) - _g(noise)
        rows.append((kr, b2, n, C, _g(n)))
    # trapezoid in ln k with weight k^3 (k^2 dk = k^3 d ln k)
    lk = [math.log(r[0]) for r in rows]
    num = sum((lk[i + 1] - lk[i]) * (rows[i][0] ** 3 * rows[i][3] + rows[i + 1][0] ** 3 * rows[i + 1][3]) / 2
              for i in range(len(rows) - 1))
    den = sum((lk[i + 1] - lk[i]) * (rows[i][0] ** 3 * rows[i][4] + rows[i + 1][0] ** 3 * rows[i + 1][4]) / 2
              for i in range(len(rows) - 1))
    return dict(rows=rows, F=num / den)


# ------------------------------------------------------------------ Q6
def fluctuation(A, Wt):
    N, E5 = A["d"]["N"], A["d"]["E"]
    kT = Wt["kT"]
    e_in = 3 * ZETA4 / ZETA3 * kT                                    # mean quantum, the plane's thermal inflow (4D)
    e_out = 3 * ZETA4 / ZETA3 * kT                                   # mean quantum, the plane's emission (4D)
    n_in = Wt["E_in"] / e_in; n_out = Wt["E_in"] / e_out
    dM = math.sqrt(n_in * e_in ** 2 + n_out * e_out ** 2)
    dbits = dM / (kT * math.log(2))
    x = (1 + Wt["b"]) / 2                                            # [542, D5] the write in units of 2 lives
    g_drift = (math.exp(x) - 1) / x                                  # a constant mismatch, against linear drift
    g_walk = math.sqrt((math.exp(2 * x) - 1) / (2 * x))              # the random walk's spread, against linear
    return dict(dbits=dbits, rel=dbits / N, match=1 / N, x=x, g_drift=g_drift, g_walk=g_walk,
                dbits_u=dbits * g_walk, match_u=1 / (N * g_drift))


def compute():
    o = dict(words=words(), A=all_at_once(), fl=first_law(), bal=balance())
    o["W"] = write_time(o["A"])
    o["modes"] = {(mu, kr): modes(mu, kr) for mu, kr in ((1e4, 0.3), (1e4, 1.0), (1e4, 10.0), (1e4, 100.0),
                                                          (1e4, 1e3), (1e4, 1e5), (1e6, 1.0), (1e6, 1e5))}
    o["fluct"] = fluctuation(o["A"], o["W"])
    o["cap"] = {mu: capacity(mu) for mu in (1e4, 1e6)}
    return o


def checks(o):
    A, fl, b, W, Mo, F = o["A"], o["fl"], o["bal"], o["W"], o["modes"], o["fluct"]
    q0 = o["words"]
    q1 = A["small"] < 1e-2 and A["cap"] < 1e-10
    q2 = fl["ok5"] and fl["ok4"] and fl["e5"] == sp.Rational(3, 2) and fl["e4"] == 2
    q3 = b["static"] and b["grows"]
    bb = sp.Symbol("b", positive=True)
    q4 = (sp.simplify(W["ratio_life"] - (1 + bb)) == 0 and W["ratio_E"] == sp.Rational(1, 2)
          and W["ratio_E4"] == sp.Rational(3, 8) and abs(W["tau_ratio"] - (1 + W["b"])) < 1e-9
          and abs(W["E_ratio"] - 0.5) < 1e-9 and abs(W["S_room4"] - 1) < 1e-9 and "%.3g" % W["tau_cl"] == "8.63e+14"
          and "%.2f" % W["Tin_bulk"] == "1.98" and "%.2f" % W["tau_bulk"] == "2.12"
          and "%.2f" % W["Ein_bulk"] == "1.06" and 10 < W["per_N"] < 12)
    unit = all(m["unit"] < 1e-5 and m["Wdrift"] < 1e-6 for m in Mo.values())
    mixed = all(Mo[(1e4, kr)]["b2"] > 0.1 for kr in (0.3, 1.0, 10.0)) and Mo[(1e6, 1.0)]["b2"] > 0.1
    clean = Mo[(1e4, 1e5)]["b2"] < 1e-8 and Mo[(1e6, 1e5)]["b2"] < 1e-8
    expo = math.log(Mo[(1e6, 1.0)]["qmax"] / Mo[(1e4, 1.0)]["qmax"]) / math.log(100)
    q5 = unit and mixed and clean and abs(expo - 0.75) < 0.05
    Cp = o["cap"]
    q5 = q5 and all(0 < c["F"] < 1 for c in Cp.values()) and Cp[1e6]["F"] < Cp[1e4]["F"] \
        and all(r[1] > 0 for c in Cp.values() for r in c["rows"])
    q6 = 1e-9 < F["rel"] < 1e-5 and F["match"] < 1e-15 \
        and "%.3f" % F["g_drift"] == "1.300" and "%.3f" % F["g_walk"] == "1.313"      # [542, D5]
    return dict(Q0=q0, Q1=q1, Q2=q2, Q3=q3, Q4=q4, Q5=q5, Q6=q6)


def report(o=None):
    o = o or compute(); ck = checks(o); W = o["W"]; A = o["A"]
    print("Q0 M's words: %s" % o["words"])
    print("Q1 a delivery all at once holds %.2g of N (small end), %.2g (Earth cap) at one clock" % (A["small"], A["cap"]))
    print("Q2 first law dM = T dS: 5D %s, 4D %s; E/(N kT ln2) = %s (5D), %s (4D)" % (
        o["fl"]["ok5"], o["fl"]["ok4"], o["fl"]["e5"], o["fl"]["e4"]))
    print("Q3 the net flux sets mu': static at P_in = P_H %s; grows without the Hawking flux %s" % (
        o["bal"]["static"], o["bal"]["grows"]))
    print("Q4 small end, the plane's channel: tau_write = %s of the life (b = %.4f), the inflow %s of E5(N) (exact); "
          "%.3g face clocks = %.2g s at the example README (life %.3g clocks); the 4D room saturated, S/(N ln2) = %.12f."
          "  The bulk's channel: T_in = %.2f T_H, tau = %.2f lives, inflow %.2f E5(N).  Large end: tau_write = %.3g N "
          "clocks of GM/c^3, the inflow %s of E(N)" % (
              W["ratio_life"], W["b"], W["ratio_E"], W["tau_cl"], W["tau"], W["life"], W["S_room4"],
              W["Tin_bulk"], W["tau_bulk"], W["Ein_bulk"], W["per_N"], W["ratio_E4"]))
    for (mu, kr), m in o["modes"].items():
        print("Q5 mu/l5^2 %.0e, k r_h %-7g: KG norm drift %.1e, |alpha|^2 - |beta|^2 - 1 = %.1e, |beta|^2 %.3e, "
              "adiabatic Q max %.2e" % (mu, kr, m["Wdrift"], m["unit"], m["b2"], m["qmax"]))
    for mu, c in o["cap"].items():
        print("Q5 position 2 alone, mu/l5^2 %.0e: " % mu + "; ".join("k r_h %g |beta|^2 %.3g C %.3g of %.3g nats" % (
            r[0], r[1], r[3], r[4]) for r in c["rows"]) + "; recoverable fraction F = %.3f" % c["F"])
    print("Q6 the face at balance holds in the mean: fluctuates by %.2g bits of N (%.1e); P_in must match P_H to %.1e" % (
        o["fluct"]["dbits"], o["fluct"]["rel"], o["fluct"]["match"]))
    print("   [542, D5] the balance unstable, one e-fold per two lives: over the write (x = %.4f) the drift x %.3f, the "
          "spread x %.3f -- %.2g bits, the match %.2e" % (o["fluct"]["x"], o["fluct"]["g_drift"], o["fluct"]["g_walk"],
                                                          o["fluct"]["dbits_u"], o["fluct"]["match_u"]))
    for kk, vv in ck.items():
        print("%s %s" % (kk, vv))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["nohawking", "entropy", "lossy", "partners_cross"]
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
