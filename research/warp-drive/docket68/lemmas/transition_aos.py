#!/usr/bin/env python3
"""transition_aos.py -- item 478: 273's transition against the prior art that computes one (442: prior art first, then
computation).  Ashtekar, Olmedo and Singh's effective loop-quantum-gravity interior of a Schwarzschild hole
(arXiv 1806.02406v3, READ below) is reproduced and run at the record's sizes.  Labels: READ (verbatim, page), computed,
deduced, M's.  Worked in the conversation; not verified; not seated.

  T0 (READ, 1806.02406v3) p. 8, eqs. (2.19)-(2.25): "tan(delta_c c(T)/2) = -/+ (gamma L_o delta_c/8m) e^(-2T)",
     "p_c(T) = 4m^2 (e^(2T) + (gamma^2 L_o^2 delta_c^2/64m^2) e^(-2T))", "cos(delta_b b(T)) = b_o tanh((1/2)(b_o T +
     2 tanh^-1(1/b_o)))", "b_o = (1 + gamma^2 delta_b^2)^(1/2)"; p. 9: "p_c takes a minimum value p_c|min = m gamma L_o
     delta_c in every effective space-time"; p. 43, eq. (B7): "delta_b = (sqrt(Delta)/(sqrt(2 pi) gamma^2 m))^(1/3),
     L_o delta_c = (1/2)(gamma Delta^2/(4 pi^2 m))^(1/3)"; p. 23, eq. (4.20): "m_WH = m_BH (1 + O((l_Pl/m)^(2/3)
     ln(m/l_Pl)))"; abstract, p. 1: "All curvature scalars have uniform (i.e., mass independent) upper bounds".
  T1 (computed) The closed forms solve the effective equations (2.19)-(2.20), and m = sin(delta_c c) p_c/(gamma L_o
     delta_c) is constant along them, to 1e-25 at the record's sizes.
  T2 (computed, exact) p_c has one minimum, at e^(2T) = eps (eps = gamma L_o delta_c/8m), of value m gamma L_o delta_c:
     the transition surface, in place of the singularity.
  T3 (computed) To the future of the black hole's horizon the spheres shrink (trapped), past the transition surface they
     grow (anti-trapped): a black-hole interior followed by a white-hole interior.
  T4 (computed) The white hole's horizon (delta_b b = pi) has the black hole's mass: m_WH/m_BH - 1 at r0 = 20 ell, the
     Earth cap and 2.8e7 ell, below 1e-18, with (m_WH/m_BH - 1)/((l_P/m)^(2/3) ln(m/l_P)) bounded over m/l_P = 1e6..1e40,
     as (4.20).  273's construction (position 2's face the same N bits, by the Kruskal isometry) is what this gives.
  T5 (computed) Kretschmann's classical form at the transition surface, 48 m^2/p_c^3, is the same number at every mass,
     1.783e5 / l_P^4 (Planck curvature; the effective scalar is smaller, AOS section IV C); and the c-sector's correction to the classical p_c is (1/4)(K/K_T)^(2/3), a positive power of the
     curvature in Planck units vanishing where it is small -- quantum_onset's P2-Q2 form (415), in this theory.
  T6 (computed; a finding) The theory is four-dimensional, its scale l_P.  The record's large-end core is five-
     dimensional (core_face B1; core_large K6): x = l5^2 sqrt(K) reaches 1 where K = 1/l5^4, a factor (l_P/l5)^4 below
     the curvature at which this transition happens.  So T1-T5 realize 273 for a four-dimensional hole; they do not
     compute 273 in the record's five-dimensional core.

What this proves and does not: 273's transition (black-hole interior -> white-hole interior of equal mass, curvature
bounded, classical GR recovered wherever the curvature is small) is computed in effective loop quantum gravity, a
candidate quantum theory of gravity, not established physics; Penrose's theorem with the null energy condition excludes
it in classical GR, and the semiclassical route is closed (section 32).  The probability and time of the transition
(Haggard and Rovelli's m^2/l_P) are not computed here.  The five-dimensional core is not reached by this prior art.

python3 transition_aos.py [--selftest | --mutants]
"""
import os, sys, math, importlib.util
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
MUT = set()
mp.mp.dps = 80
GAMMA = mp.mpf("0.2375")                                 # Barbero-Immirzi parameter (as AOS)
DELTA = 4 * mp.sqrt(3) * mp.pi * GAMMA                   # LQG area gap, l_P = 1 (enters K_T's number only)


def _load(name, alias):
    spec = importlib.util.spec_from_file_location(alias, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod); return mod


def params(m):
    m = mp.mpf(m)
    db = (mp.sqrt(DELTA) / (mp.sqrt(2 * mp.pi) * GAMMA ** 2 * m)) ** (mp.mpf(1) / (2 if "db" in MUT else 3))
    Ldc = (GAMMA * DELTA ** 2 / (4 * mp.pi ** 2 * m)) ** (mp.mpf(1) / 3) / 2
    bo = mp.sqrt(1 + (-1 if "bo" in MUT else 1) * GAMMA ** 2 * db ** 2)
    return dict(m=m, db=db, Ldc=Ldc, bo=bo, eps=GAMMA * Ldc / (8 * m))


def sol(P, T):
    """AOS (2.21)-(2.25), the fiducial length L_o = 1 (results are L_o-independent)"""
    m, db, dc, bo, eps = P["m"], P["db"], P["Ldc"], P["bo"], P["eps"]
    c = 2 / dc * mp.atan(eps * mp.e ** (-2 * T))
    pc = 4 * m ** 2 * (mp.e ** (2 * T) + (0 if "classical" in MUT else eps ** 2 * mp.e ** (-2 * T)))
    cosb = bo * mp.tanh((bo * T + 2 * mp.atanh(1 / bo)) / 2)
    b = mp.acos(cosb) / db
    sb, sc = mp.sin(db * b), mp.sin(dc * c)
    pb = -2 * (sc / dc) * (sb / db) * pc / (sb ** 2 / db ** 2 + GAMMA ** 2)
    return dict(b=b, c=c, pb=pb, pc=pc)


def eom_residual(P, T):
    db, dc = P["db"], P["Ldc"]
    d = {k: mp.diff(lambda s: sol(P, s)[k], T) for k in ("b", "c", "pb", "pc")}
    s = sol(P, T); sb, cb = mp.sin(db * s["b"]), mp.cos(db * s["b"]); sc, cc = mp.sin(dc * s["c"]), mp.cos(dc * s["c"])
    rhs = dict(b=-(sb / db + GAMMA ** 2 * db / sb) / 2, c=-2 * sc / dc,
               pb=s["pb"] / 2 * cb * (1 - GAMMA ** 2 * db ** 2 / sb ** 2), pc=2 * s["pc"] * cc)
    rel = max(abs(d[k] - rhs[k]) / max(abs(rhs[k]), mp.mpf(10) ** -60) for k in d)
    mobs = sc * s["pc"] / (GAMMA * dc)
    return rel, abs(mobs / P["m"] - 1)


def surfaces(P):
    m, eps, bo = P["m"], P["eps"], P["bo"]
    TT = mp.log(eps) / 2                                  # p_c' = 0
    TWH = -4 * mp.atanh(1 / bo) / bo * (-1 if "wh" in MUT else 1)   # cos(delta_b b) = -1
    pmin = sol(P, TT)["pc"]
    mwh = mp.sqrt(sol(P, TWH)["pc"]) / 2
    return dict(TT=TT, TWH=TWH, pmin=pmin, mwh=mwh, KT=48 * m ** 2 / pmin ** 3)


def compute():
    QO = _load("quantum_onset.py", "ta_qo"); EC = _load("earth_cap.py", "ta_ec")
    o = QO.onset_4d(); lP, l5, ell = o["lP"], o["l5"], o["ell"]
    sizes = {"r0 = 20 ell": 20 * ell, "the Earth cap": EC.compute()["r0"], "r0 = 2.8e7 ell": 2.8e7 * ell}
    out = dict(rec={}, scan={})
    for k, r0 in sizes.items():
        P = params(r0 / 2 / lP); S = surfaces(P)
        res = [eom_residual(P, T) for T in (S["TT"] / 2, S["TT"] * mp.mpf("1.3"), (S["TT"] + S["TWH"]) / 2)]
        sides = (mp.diff(lambda s: sol(P, s)["pc"], S["TT"] / 2) > 0, mp.diff(lambda s: sol(P, s)["pc"], 1.5 * S["TT"]) < 0)
        out["rec"][k] = dict(P=P, S=S, eom=max(r[0] for r in res), mdrift=max(r[1] for r in res), sides=sides,
                             ratio=S["mwh"] / P["m"] - 1, pmin_ok=abs(S["pmin"] / (P["m"] * GAMMA * P["Ldc"]) - 1),
                             KT=S["KT"], K5onset=(lP / l5) ** 4)
    for e in range(6, 41, 2):
        P = params(mp.mpf(10) ** e); S = surfaces(P)
        out["scan"][e] = dict(ratio=S["mwh"] / P["m"] - 1, KT=S["KT"],
                              scaled=(S["mwh"] / P["m"] - 1) / (P["m"] ** (-mp.mpf(2) / 3) * mp.log(P["m"])))
    # T5: the c-sector correction against the classical p_c as a function of K/K_T
    P = params(mp.mpf(10) ** 30); S = surfaces(P)
    corr = []
    for f in (mp.mpf(10) ** -9, mp.mpf(10) ** -6, mp.mpf(10) ** -3):
        T = S["TT"] + mp.log(1 / f) / 3                   # K_cl/K_T = f at p_cl = p_min f^(-1/3) / ... (approx)
        pcl = 4 * P["m"] ** 2 * mp.e ** (2 * T); K = 48 * P["m"] ** 2 / pcl ** 3
        corr.append((sol(P, T)["pc"] / pcl - 1) / ((K / S["KT"]) ** (mp.mpf(2) / 3) / 4))
    out["corr"] = corr
    return out


def checks(o):
    R = o["rec"]
    t1 = all(v["eom"] < 1e-25 and v["mdrift"] < 1e-25 for v in R.values())
    t2 = all(v["pmin_ok"] < 1e-40 for v in R.values())
    t3 = all(all(v["sides"]) for v in R.values())
    sc = [abs(v["scaled"]) for v in o["scan"].values()]
    t4 = all(0 < abs(v["ratio"]) < 1e-18 for v in R.values()) and max(sc) < 10 and min(sc) > 1e-3
    KT = [v["KT"] for v in o["scan"].values()]
    t5 = (max(KT) / min(KT) - 1 < 1e-6 and 1e3 < KT[0] < 1e7
          and all(abs(c - 1) < 1e-2 for c in o["corr"]))
    t6 = all(v["K5onset"] < 1e-30 for v in R.values())
    return dict(T1=t1, T2=t2, T3=t3, T4=t4, T5=t5, T6=t6)


def report(o=None):
    o = o or compute(); ck = checks(o)
    for k, v in o["rec"].items():
        print("   %-15s m/l_P %.3e  eom resid %.1e  m drift %.1e  m_WH/m_BH - 1 = %.3e  K_T l_P^4 = %.4f  "
              "1/l5^4 against K_T: %.2e" % (k, float(v["P"]["m"]), float(v["eom"]), float(v["mdrift"]),
                                             float(v["ratio"]), float(v["KT"]), float(v["K5onset"] / v["KT"])))
    print("   scan m/l_P 1e6..1e40: (m_WH/m - 1)/((l_P/m)^(2/3) ln(m/l_P)) from %.3f to %.3f; K_T l_P^4 %.6f" % (
        float(min(abs(v["scaled"]) for v in o["scan"].values())),
        float(max(abs(v["scaled"]) for v in o["scan"].values())), float(o["scan"][6]["KT"])))
    print("   c-sector correction / ((K/K_T)^(2/3)/4) at K/K_T ~ 1e-9, 1e-6, 1e-3: %s" % (
        ", ".join("%.4f" % float(c) for c in o["corr"])))
    for k in ck:
        print("%s %s" % (k, ck[k]))
    return all(ck.values())


def selftest(quiet=False):
    o = compute(); ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


def mutants():
    caught = 0; names = ["bo", "classical", "db", "wh"]
    for mu in names:
        MUT.clear(); MUT.add(mu)
        try:
            res = selftest(quiet=True)
        except Exception:
            res = False
        caught += not res; print("mutant %-9s %s" % (mu, "caught" if not res else "SURVIVED"), flush=True)
    MUT.clear(); print("%d/%d caught" % (caught, len(names)))
    return caught == len(names)


if __name__ == "__main__":
    a = sys.argv[1:]
    if a and a[0] == "--selftest":
        sys.exit(0 if selftest() else 1)
    if a and a[0] == "--mutants":
        sys.exit(0 if mutants() else 1)
    report()
