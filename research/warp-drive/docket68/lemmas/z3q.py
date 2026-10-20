#!/usr/bin/env python3
"""z3q.py -- item 542, lemma Z3q: where the passage's negative sits on QB.  M, 542, to the weak rows: "strengthen the
existing lemmas, and ad more for support".  Z3bs and Z3b said the passage's negative is "confined to the quantum
region", which transition5 computed with a sharp region; since 537 the rows rest on QB, whose state departs from the
classical interior continuously (bounce_close C4).  This file locates the negative on QB.  Labels: computed (exact
unless marked numerical), READ, deduced, M's.

  Q0 (read) M's words, verbatim in the rulings file, 542.
  Q1 (computed, exact; bounce_close C2) Outside the horizon the geometry is Schwarzschild-AdS5 exactly (Birkhoff in five
     dimensions): every ray outside the horizon carries zero null energy.
  Q2 (computed, numerical) The tail.  On QB's symmetric state (bounce_close C3's parameters) the mass function m_eff
     against mu, at the curvature place x/x_b = (Y_min/<Y>)^2: |m_eff/mu - 1| <= 1.3 (x/x_b)^2 for x/x_b from 0.03 to
     0.25, and positive there -- the mass slightly above mu, not below it.
  Q3 (computed, numerical) The drop.  m_eff falls below mu only above x/x_b = 0.37, where the departure is of order one
     (to Y_min, about 3e-6 mu, at the bounce): the mass's drop, the negative, sits there.
  Q4 (computed, numerical; bounce_close C3) Net zero on every ray.  Every causal curve inside the horizon reaches the
     bounce (two horizons only, QB part 3), and m_eff returns to mu after it (in and out equal, the state
     time-symmetric): what the drop takes the far side gives back, 273 (c)'s pairing under 183.
  Q5 (computed) At the horizon the tail is (x_h/x_b)^2 of order: 2.6e-18 at the small end (x_h = 1.6e-9, QB), 1.4e-80
     at the large (x_h = 1.2e-40).
  Q6 (deduced) So on QB the rows' words hold, made exact: the passage's negative -- the mass's drop -- sits where QB
     departs at order one (x > 0.37 x_b); outside it QB's departure is a positive tail below 1.3 (x/x_b)^2; outside the
     horizon it is zero; and along every ray the net is zero.  Below the state's own width (the Gaussian in k, relative
     spread (s_k/k_c)^2 = 4.4e-5) the tail is not resolved and is not claimed.

Imports bounce_qm.py (the closed forms) and bounce_close.py (C2, C3) by path.  mpmath, numpy, sympy.
python3 z3q.py [--selftest | --mutants]
"""
import contextlib, importlib.util, io, os, sys
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
WORDS = ((542, "strengthen the existing lemmas, and ad more for support"),)
P = dict(kc=300.0, sk=2.0, Lc=0.0, sg=1e-7, xi0=1e6)           # bounce_close C3's symmetric state
X_H = {"small": 1.6e-9, "large": 1.2e-40}                        # QB's note (538): x_h at each end
_MOD = {}


def _load(name, alias):
    if alias not in _MOD:
        spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
        mod = importlib.util.module_from_spec(spec)
        sys.modules[alias] = mod
        with contextlib.redirect_stdout(io.StringIO()):
            spec.loader.exec_module(mod)
        _MOD[alias] = mod
    return _MOD[alias]


def words():
    txt = open(RULINGS, encoding="utf-8").read()
    return all(w in txt for _, w in WORDS)


def profile():
    """m_eff/mu - 1 against x/x_b along QB's symmetric state"""
    BQ = _load("bounce_qm.py", "z3q_bq")
    mp.mp.dps = 40
    kv = {a: BQ.kav(a, P) for a in (0.5, -1, -1.5)}
    mu = P["xi0"] * BQ.kav(2, P) / 9
    xf = lambda T: BQ.xicf(T, P, kv)
    yf = lambda T: BQ.Ycf(T, P, kv)

    def meff(T):
        Y_, Yd_ = yf(T), mp.diff(yf, T)
        m = Y_ * (1 + xf(T) * Y_ * Yd_ ** 2)
        return -m if MUT.get("sign") else m
    y0 = yf(mp.mpf(0))
    rows = []
    for s in (0.6, 0.8, 1.0, 1.2, 1.4, 1.6, 2, 3, 4, 6, 8, 12, 16):
        T = mp.mpf(s) / P["sg"]
        r = float((y0 / yf(T)) ** 2)
        rows.append((s, r, float(meff(T) / mu - 1)))
    return dict(rows=rows, m0=float(meff(mp.mpf(0)) / mu), mu=mu)


def crossing(rows):
    """the place where m_eff crosses mu, by linear interpolation in x/x_b"""
    for (s0, r0, d0), (s1, r1, d1) in zip(rows, rows[1:]):
        if d0 < 0 <= d1:
            return r0 + (r1 - r0) * (0 - d0) / (d1 - d0)
    return None


def compute():
    BC = _load("bounce_close.py", "z3q_bc")
    with contextlib.redirect_stdout(io.StringIO()):
        bk = BC.birkhoff()
        ms = BC.mass()
    pr = profile()
    tail = [(r, d) for s, r, d in pr["rows"] if 0.03 <= r <= 0.25]
    return dict(words=words(), birkhoff=bk, mass=ms, prof=pr, tail=tail, cross=crossing(pr["rows"]),
                horizon={k: v ** 2 for k, v in X_H.items()})


def checks(o):
    bk = o["birkhoff"]
    q1 = all(bool(v) for v in bk.values()) if isinstance(bk, dict) else bool(bk)
    tail = o["tail"]
    q2 = len(tail) >= 4 and all(0 < d <= 1.3 * r ** 2 for r, d in tail)
    q3 = o["cross"] is not None and 0.35 < o["cross"] < 0.38 and o["prof"]["m0"] < 1e-5
    ms = o["mass"]
    q4 = abs(float(ms["m_in"] - ms["m_out"]) / float(ms["mu"])) < 1e-9
    q5 = "%.2g" % o["horizon"]["small"] == "2.6e-18" and "%.2g" % o["horizon"]["large"] == "1.4e-80"
    return {"Q0": o["words"], "Q1": q1, "Q2": q2, "Q3": q3, "Q4": q4, "Q5": q5}


def report(o=None):
    o = o or compute(); ck = checks(o)
    print("Q0 M's words:", o["words"])
    print("Q1 outside the horizon Schwarzschild-AdS5 exactly (bounce_close C2):", ck["Q1"])
    for s, r, d in o["prof"]["rows"]:
        print("Q2 sigma T %5.2f  x/x_b %.4f  m_eff/mu - 1 %+.4e  /(x/x_b)^2 %+.3f" % (s, r, d, d / r ** 2))
    print("Q3 m_eff crosses mu at x/x_b = %.4f; at the bounce m_eff/mu = %.2e" % (o["cross"], o["prof"]["m0"]))
    ms = o["mass"]
    print("Q4 in and out equal: %.3e of mu" % abs(float(ms["m_in"] - ms["m_out"]) / float(ms["mu"])))
    print("Q5 (x_h/x_b)^2: small end %.2g, large end %.2g" % (o["horizon"]["small"], o["horizon"]["large"]))
    for k, v in ck.items():
        print("%s %s" % (k, v))
    return ck


def selftest(quiet=False):
    with contextlib.redirect_stdout(io.StringIO()) if quiet else contextlib.nullcontext():
        ck = report()
    ok = all(ck.values())
    if not quiet:
        print("selftest: %s" % ("PASS" if ok else "FAIL"))
    return ok


MUTANTS = {"sign": "the mass function's sign flipped, so the drop and the tail trade places (Q2, Q3)"}


def mutants():
    caught = 0
    for m, what in MUTANTS.items():
        MUT.clear(); MUT[m] = True
        try:
            ok = selftest(quiet=True)
        except Exception:
            ok = False
        caught += not ok
        print("mutant %-8s %s  (%s)" % (m, "caught" if not ok else "MISSED", what))
    MUT.clear()
    print("%d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
