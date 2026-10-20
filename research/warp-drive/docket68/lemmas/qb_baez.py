#!/usr/bin/env python3
"""qb_baez.py -- item 539: the Planckian curvature QB operates at, measured under varying values of Baez's constants,
as p2_matter measured copper under the laws of other positions (M: the copper study "was built and models and measured
under different constant conditions of varying universes").  Every value is computed under our constants and under
each varied set with one instrument, and the difference is the finding.  Worked in the conversation (computed, stdlib
with sympy and mpmath; READ where marked; deduced where marked; not verified by a separate session); 2026-10-20.

  B0 (read) M's words, verbatim in the rulings file, 539: "measure the planckian curvature under varying Baez constants
     values, like the copper study".
  B1 (proved; computed exactly) What in QB carries a constant.  QB's equations (BOUNCE-PROOF L1-L5) are the vacuum
     Einstein equations with the bulk's Lambda5 = -6/ell^2: no field of the plane enters the interior, so no Baez
     constant enters them except through ell.  In units of l5 every QB quantity is a function of N, Lambda5 l5^2 and
     the place x_b alone, with Lambda5 l5^2 = -6 (l5/ell)^2 = -6 (l_P/ell)^(4/3).  Exactly:
     - the Kretschmann scalar of Schwarzschild-AdS5 is 72 mu^2/r^8 + 10 Lambda5^2/9 = 72 mu^2/r^8 + 40/ell^4, so at the
       Planckian place the bulk constant adds 40 (l5/ell)^4 of l5^-4;
     - xi = mu - Y + Lambda5 Y^2/6, so at the least sphere, Y_min^2 = sqrt(72) mu l5^2/x_b, the constant's share of xi is
       sqrt(2) Lambda5 l5^2/x_b, whatever the mass;
     - the horizon's place x_h = sqrt(72) (l5/r_h)^2 = sqrt(72) (pi^2/(2 N ln2))^(2/3) at the small end (H1's count) is
       N's alone, the same in every universe: the identity core 1.6e-9; copper's README 1.8e-14 at 7.6e22 bits, and 0.70
       at 300 bits on its bare count, 0.083 on its least seed (102 l5^2), where the place theorem's x_b >> x_h is
       weakest.
  B2 (computed) Where the 26 enter: ell, and so l5 = (l_P^2 ell)^(1/3) and the Planckian curvature K_P = l5^-4.  The
     record holds three readings of ell:
     - (H) the Higgs tie (ell_higgs H5-H7): E5 = hbar c/l5 at the running quartic's zero E_I (p2_offset's three-loop
       run), so K_P = (E_I/hbar c)^4.  It moves with m_t, m_H, alpha_s and m_W, four of the 26 at the run's precision
       (the bottom and tau Yukawas left out, as in p2_offset; the light masses, the mixings and the neutrino masses do
       not enter the run).  Ours: E_I 3.637e10 GeV, interpolated in ln mu and unchanged at 4 and 16 times the steps;
       the record's 3.68e10 is the run's first step past the zero, 1.3 % high, so ell_H is 0.611 nm, not 0.588 nm (a
       precision finding on ell_higgs H3, recorded here, not repaired there); l5 5.43e-27 m, K_P 1.15e105 m^-4;
     - (D) the dark-energy tie (ell_de D3, a postulate in the theorem's bulk, 379 D2):
       ell = lam_C (hbar c/rho_L c^2)^(1/4)
       with Casimir's lam_C = 0.08432: ell_D 7.43 um, K_P 4.13e99 m^-4.  It moves with the cosmological constant, the
       26th, as rho_L^(1/3);
     - (F) a fixed ell: the window's top, 13.964 um (a measurement: E5 1.28e9 GeV, K_P 1.78e99 m^-4), or 12.28 l_P
       (Einstein's coupling, ell_fix X4, excluded by ell_higgs H5: K_P 5.17e137 m^-4): it moves with none of the 26.
  B3 (computed) The table, ours against each variation.  Under (H), across m_t's 1 sigma (172.28-172.86 GeV) K_P runs
     over a factor 2.9e3, across alpha_s's 1 sigma 7.8e3, across m_H's 39, across m_W's 1.6 %; across the metastable
     window, m_t from 171.0 to 177.68 GeV, by 4.2e33.  At m_t <= 170.88 GeV, or at m_H 130 GeV, the quartic has no zero:
     the vacuum is stable, the tie fixes nothing, and the Planckian curvature is the window's (F).  m_H and alpha_s
     raise E_I where m_t lowers it.  Under (D), Lambda x 1e3 raises K_P by 10 and x 1e-3 lowers it by 10.
  B4 (computed) QB rerun in each universe.  bounce_proof P6's state at x_b = 1 (mu = 1e10 l5^2) with Lambda5 l5^2 set
     to 0, -1e-12, -2e-12 and -4e-12: both horizons and the symmetry stay; the curvature maximum moves linearly, by
     1.2392 Lambda5 l5^2 (the slope constant to 1e-11); the crossing by -1.33 (r_h/ell)^2, the constant's share at the
     horizon, not at the bounce.  At each universe's own value the bounce moves by at most 6.7e-15 in the scan (at
     m_t 171.0 GeV, where ell_H is least) and by 5.9e-34 in ours.  The crossing of copper's largest README moves by
     5.1e-20 in ours; it moves by 0.58 only at m_t 171.0 GeV, where that README's hole is 0.66 ell, at the crossover,
     and the large end's form takes over, as in the record.  Einstein's coupling, Lambda5 l5^2 = -0.21, would move the
     bounce, and there the semiclassical small end barely exists (2.9 l5 < r_h < 5.3 l5): a reading the record excludes.
  B5 (computed) The copper study's own universes.  2a (the exception law, min and mirror) touches only the d shells of
     the exception elements: no vacuum quantity, so K_P x 1 under every reading.  2b (G x 2, ell x 1/sqrt 2) and 2c
     (2a + 2b): K_P x 2^(-2/3) = 0.63 on their own ell, x 2^(-4/3) = 0.40 on the window's top held in SI, x 1 on the
     Higgs tie (the 26 unchanged).  2P (G x 2, ell x sqrt 2): x 1/4 on its own ell, which is ours in Planck units
     (K_P l_P^4 x 1), as p2_planck Q2 found for every geometric clause.
  B6 (computed; READ) Against what is tested.  The highest collision energy reached is 13.6 TeV (CERN, Run 3; READ).
     Under (H) our E5 is 2.7e6 times it, 6.43 orders.  The tie meets the window's top at m_t 173.84 GeV: beyond it ell_H
     exceeds the measured 13.964 um, so wherever the window holds, E5 >= 1.28e9 GeV, 4.97 orders above.  Across the whole
     metastable window, the window's top set aside, the gap never falls below 2.79 orders (at 177.68 GeV, where ell_H is
     52 m).  E5 would reach 13.6 TeV only at m_t 195.7 GeV or m_H 99.3 GeV (estimates: Buttazzo's matching is linear
     about 173.34 and 125.15 GeV, extrapolated), where our vacuum would be unstable.  Under (D) the gap is 5.07 orders.
  B7 (deduced) What the measurement says.  QB's outcome is universal: the same equations and the same dimensionless
     numbers in every universe of Baez's list the scan reaches, the bounce always at that universe's own
     five-dimensional Planck curvature.  The 26 move that curvature's size, and only through ell: under the Higgs tie by
     dozens of orders across the metastable window, under the dark-energy tie by Lambda^(1/3), under a fixed ell not at
     all.  In every universe with a metastable vacuum it lies at least 2.8 orders of energy above the highest energy
     tested, and at least 5.0 where the measured window holds, so the step QB postulates -- quantum mechanics there --
     is untested in all of them.  The status stays COMPUTED-THEORIZED; the measurement shows the theorem does not depend
     on which universe's constants hold.

Imports p2_offset.py (the run) and bounce_qm.py (the closed forms and the curvature) by path.
python3 qb_baez.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import math
import os
import sys

import mpmath as mp
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
D68 = os.path.dirname(HERE)
RULINGS = os.path.join(D68, "M-RULINGS-2026-10-03.md")
MUT = {}
mp.mp.dps = 30
WORDS = ((539, "measure the planckian curvature under varying Baez constants values, like the copper study"),)
LHC_READ = ("The LHC will now run for close to four years at the record collision energy of 13.6 trillion electronvolts "
            "(TeV)",                                                                     # home.cern Run 3 media kit
            "colliding proton beams at a world-record-breaking energy of 13.6 tera electron volts (TeV)")  # ATLAS
E_LHC = 13.6e3                                    # GeV
HBARC = 1.973269804e-16                           # GeV m
C, HBAR, G = 299792458.0, 6.62607015e-34 / (2 * math.pi), 6.67430e-11
L_P = math.sqrt(HBAR * G / C ** 3)                # the theorem's l_P, no 8 pi (384)
OFFSET = 5.25e-10                                 # J/m^3, rho_Lambda c^2 (201)
LAM_C = (3 * 1.0369277551433699 / (2 * math.pi) ** 6) ** 0.25        # Casimir's lam (ell_de D3): zeta(5)
ELL_TOP = 13.964e-6                               # the window's top (ell_fix X2)
ELL_EIN = math.sqrt(48 * math.pi) * L_P           # Einstein's coupling (ell_fix X4)
OURS = dict(mh=125.09, mt=172.57, a3=0.1180, mw=80.384)               # p2_offset READ; start()'s m_W
SIG = dict(mh=0.24, mt=0.29, a3=0.0009, mw=0.0133)                    # p2_offset READ; PDG 2024 m_W
N_CU = (300.0, 7.6e22)                            # copper's README (SOURCE-REQUIRED 399)
N_CORE = 2.7426e15                                # the identity core (ell_map)
MU_SEED_CU = 102.0                                # copper's least seed, l5^2 (seed_derive; WARPTHEOREM)
KR = 0.7424                                       # K_max/K_cl(Y_min) at the place (bounce_proof P6)
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


# ---------------------------------------------------------------- B1
def kretschmann_sads():
    """K of -f dt^2 + dr^2/f + r^2 dOmega_3^2, f = 1 - mu/r^2 - Lambda r^2/6, exactly"""
    BQ = _load("bounce_qm.py", "qbz_bq")
    t, r, c, th, ph, mu, L = sp.symbols("t r chi theta phi mu Lambda", real=True)
    f = 1 - mu / r ** 2 - L * r ** 2 / 6
    X = (t, r, c, th, ph)
    g = sp.diag(-f, 1 / f, r ** 2, r ** 2 * sp.sin(c) ** 2, r ** 2 * sp.sin(c) ** 2 * sp.sin(th) ** 2)
    gi, _, riem = BQ._curv(g, X)
    K = 0
    for a in range(5):
        for b in range(5):
            for cc in range(5):
                for d in range(cc + 1, 5):
                    q = sp.simplify(riem(a, b, cc, d))
                    if q != 0:
                        K += 2 * g[a, a] * gi[b, b] * gi[cc, cc] * gi[d, d] * q ** 2
    K = sp.simplify(K)
    want = 72 * mu ** 2 / r ** 8 + sp.Rational(10, 9) * L ** 2
    if MUT.get("lambda_coeff"):
        want = 72 * mu ** 2 / r ** 8 + sp.Rational(5, 9) * L ** 2
    ell = sp.symbols("ell", positive=True)
    return dict(exact=sp.simplify(K - want) == 0, ell_form=sp.simplify(want.subs(L, -6 / ell ** 2)
                                                                       - (72 * mu ** 2 / r ** 8 + 40 / ell ** 4)) == 0)


def xi_share():
    """xi's Lambda term at Y_min^2 = sqrt(72) mu/x_b (l5 = 1), relative to mu: sqrt(2) Lambda/x_b"""
    mu, L, xb = sp.symbols("mu Lambda x_b", positive=True)
    Y2 = sp.sqrt(72) * mu / xb
    return sp.simplify((L * Y2 / 6) / mu - sp.sqrt(2) * L / xb) == 0


def x_h(N):
    return math.sqrt(72) * (math.pi ** 2 / (2 * N * math.log(2))) ** (2 / 3)


# ---------------------------------------------------------------- B2-B3
def e_i(mh, mt, a3, mw=OURS["mw"]):
    """the running quartic's zero, interpolated in ln mu; None if it stays positive to M_Pl"""
    PO = _load("p2_offset.py", "qbz_po")
    st = PO.start
    PO.start = lambda a, b, c, mw_=mw: st(a, b, c, mw=mw_)
    try:
        _, path = PO.run(mh, mt, a3)
    finally:
        PO.start = st
    for (m0, l0), (m1, l1) in zip(path, path[1:]):
        if l0 > 0 >= l1:
            return math.exp(math.log(m0) + (math.log(m1) - math.log(m0)) * l0 / (l0 - l1))
    return None


def universe(ell):
    l5 = (L_P ** 2 * ell) ** (1 / 3)
    if MUT.get("l5_power"):
        kp = l5 ** -2
    else:
        kp = l5 ** -4
    e5 = HBARC / l5
    return dict(ell=ell, l5=l5, E5=e5, KP=kp, Kmax=KR * kp, lam=-6 * (l5 / ell) ** 2, gap=math.log10(e5 / E_LHC))


def ell_h(E):
    l5 = HBARC / E
    if MUT.get("reduced"):
        l5 *= math.sqrt(8 * math.pi)
    return l5 ** 3 / L_P ** 2


def ell_d(rho_factor=1.0):
    return LAM_C * (HBAR * C / (OFFSET * rho_factor)) ** 0.25


def higgs_rows():
    rows = []
    def add(name, **kw):
        p = dict(OURS, **kw)
        E = e_i(p["mh"], p["mt"], p["a3"], p["mw"])
        rows.append(dict(name=name, p=p, EI=E, u=universe(ell_h(E)) if E else None))
    add("ours")
    for k, n in (("mt", 1), ("mt", 3), ("mh", 1), ("mh", 3), ("a3", 1), ("a3", 3), ("mw", 1)):
        for s in (-1, 1):
            add("%s %+d sigma" % (k, s * n), **{k: OURS[k] + s * n * SIG[k]})
    for mt in (170.0, 170.88, 171.0, 175.0, 177.68, 180.0, 190.0):
        add("m_t %.2f" % mt, mt=mt)
    for mh in (120.0, 130.0):
        add("m_H %.0f" % mh, mh=mh)
    return rows


def solve_for(key, lo, hi, target=E_LHC):
    """the value of one input at which E_I = target (E_I decreasing in m_t, increasing in m_H)"""
    for _ in range(40):
        mid = (lo + hi) / 2
        E = e_i(**dict(OURS, **{key: mid}))
        up = (E is None or E > target)
        if key == "mt":
            lo, hi = (mid, hi) if up else (lo, mid)
        else:
            lo, hi = (lo, mid) if up else (mid, hi)
    return (lo + hi) / 2


# ---------------------------------------------------------------- B4
def qb_at(lam, xb=1.0, xi0=1e6):
    """bounce_proof P6's state at one place, with the bulk constant Lambda5 l5^2 = lam (l5 = 1)"""
    BQ = _load("bounce_qm.py", "qbz_bq")
    if MUT.get("drop_lambda"):
        lam = 0.0
    base = dict(kc=300.0, sk=0.5, Lc=lam, xi0=xi0)
    kv = {a: BQ.kav(a, base) for a in (0.5, -1, -1.5)}
    mu = base["xi0"] * BQ.kav(2, base) / 9
    Ymin = (math.sqrt(72) * mu / xb) ** 0.5
    sg = (2.0 / 3) * float(kv[0.5]) ** 2 * math.gamma(0.75) ** 2 / (math.pi * Ymin ** 2)
    p = dict(base, sg=sg)
    xf = lambda T: BQ.xicf(T, p, kv)
    yf = lambda T: BQ.Ycf(T, p, kv)
    Y0 = yf(0)
    Th = mp.findroot(xf, 3 * mu ** 2 / (2 * p["kc"]))
    zeros = (xf(0) > 0) and (xf(2 * Th) < 0) and (xf(-2 * Th) < 0)
    Kf = _MOD.get("Kf") or BQ.kretschmann_eff()
    _MOD["Kf"] = Kf
    d = [mp.diff(xf, 0, n) for n in (0, 1, 2)] + [mp.diff(yf, 0, n) for n in (0, 1, 2)]
    Kr = abs(Kf(*d)) / (72 * mu ** 2 / Y0 ** 4)
    tau = 2 * mp.quad(lambda T: 1 / (2 * mp.sqrt(xf(T)) * yf(T)), [0, Th / 1e6, Th / 1e3, Th / 8, Th / 2, Th])
    return dict(mu=mu, Kr=Kr, tau=tau / (2 * mp.sqrt(mu)), zeros=zeros, sym=abs(xf(Th / 2) - xf(-Th / 2)) == 0)


def qb_scan():
    lams = (0.0, -1e-12, -2e-12, -4e-12)
    rows = [qb_at(l) for l in lams]
    sK = [(r["Kr"] - rows[0]["Kr"]) / l for r, l in zip(rows[1:], lams[1:])]
    sT = [(r["tau"] - rows[0]["tau"]) / l for r, l in zip(rows[1:], lams[1:])]
    cT = -6 * sT[0] / rows[0]["mu"]                       # d(tau/2r_h) per (r_h/ell)^2: the horizon's share
    return dict(lams=lams, rows=rows, sK=sK, sT=sT, cT=cT)


def shifts(o):
    """the induced changes in each universe: the bounce's by sK Lambda5 l5^2, the crossing's by cT (r_h/ell)^2 for
    copper's largest README at the small end"""
    q = o["qb"]
    rh = (2 * N_CU[1] * math.log(2) / math.pi ** 2) ** (1 / 3)               # in l5
    us = [r["u"] for r in o["H"] if r["u"]] + list(o["D"].values()) + [o["F"]["top"]]
    return dict(bounce=max(abs(float(q["sK"][0]) * u["lam"]) for u in us),
                crossing=max(abs(float(q["cT"])) * (rh * u["l5"] / u["ell"]) ** 2 for u in us), rh=rh)


# ---------------------------------------------------------------- B5
def positions():
    """K_P against ours under each ell reading: 2a; 2b (G x2, ell x 1/sqrt2); 2c = 2a + 2b; 2P (G x2, ell x sqrt2)"""
    out = {}
    for name, gf, ef in (("2a", 1.0, 1.0), ("2b", 2.0, 2 ** -0.5), ("2c", 2.0, 2 ** -0.5), ("2P", 2.0, 2 ** 0.5)):
        lp2 = L_P ** 2 * gf                                       # l_P^2 = hbar G/c^3
        own = ((L_P ** 2 * ELL_TOP) / (lp2 * ELL_TOP * ef)) ** (4 / 3)       # ell scaled as the position defines it
        top = ((L_P ** 2 * ELL_TOP) / (lp2 * ELL_TOP)) ** (4 / 3)            # ell held in SI
        out[name] = dict(own=own, top=top, higgs=1.0, planck_own=own * gf ** 2)
    return out


# ---------------------------------------------------------------- the whole
def compute():
    H = higgs_rows()
    o = dict(words=words(), K=kretschmann_sads(), xi=xi_share(),
             xh=dict(cu=[x_h(n) for n in N_CU], seed=math.sqrt(72) / MU_SEED_CU, core=x_h(N_CORE),
                     rh_core=(2 * N_CORE * math.log(2) / math.pi ** 2) ** (1 / 3)),
             H=H, D={f: universe(ell_d(f)) for f in (1e-3, 1.0, 1e3)},
             F=dict(top=universe(ELL_TOP), ein=universe(ELL_EIN)),
             mt_star=solve_for("mt", 180.0, 215.0), mh_star=solve_for("mh", 80.0, 125.0),
             mt_top=solve_for("mt", 172.0, 180.0, target=universe(ELL_TOP)["E5"]),
             qb=qb_scan(), pos=positions())
    o["shift"] = shifts(o)
    return o


def checks(o):
    ck = {}
    ck["B0"] = o["words"]
    xh = o["xh"]
    ck["B1"] = (o["K"]["exact"] and o["K"]["ell_form"] and o["xi"] and "%.2g" % xh["cu"][0] == "0.7"
                and "%.2g" % xh["cu"][1] == "1.8e-14" and "%.2g" % xh["seed"] == "0.083"
                and "%.2g" % xh["core"] == "1.6e-09" and abs(xh["rh_core"] - 72762.24) < 1)
    H = {r["name"]: r for r in o["H"]}
    u0 = H["ours"]["u"]
    D, F = o["D"], o["F"]
    ck["B2"] = ("%.4g" % H["ours"]["EI"] == "3.637e+10" and "%.3g" % (u0["ell"] * 1e9) == "0.611"
                and "%.3g" % u0["l5"] == "5.43e-27" and "%.3g" % u0["KP"] == "1.15e+105"
                and "%.3g" % (D[1.0]["ell"] * 1e6) == "7.43" and "%.3g" % D[1.0]["KP"] == "4.13e+99"
                and "%.3g" % F["top"]["KP"] == "1.78e+99" and "%.3g" % F["top"]["E5"] == "1.28e+09"
                and abs(F["ein"]["ell"] / L_P - 12.28) < 0.01 and abs(F["ein"]["lam"] + 0.2118) < 1e-3)
    f1 = H["mt -1 sigma"]["u"]["KP"] / H["mt +1 sigma"]["u"]["KP"]
    fw = H["m_t 171.00"]["u"]["KP"] / H["m_t 177.68"]["u"]["KP"]
    mono = all(H[a]["EI"] > H[b]["EI"] for a, b in (("m_t 171.00", "mt -3 sigma"), ("mt -3 sigma", "ours"),
                                                     ("ours", "mt +3 sigma"), ("mt +3 sigma", "m_t 175.00"),
                                                     ("m_t 175.00", "m_t 177.68"), ("m_t 177.68", "m_t 180.00")))
    ck["B3"] = ("%.2g" % f1 == "2.9e+03" and "%.2g" % fw == "4.2e+33" and mono
                and H["m_t 170.00"]["EI"] is None and H["m_t 170.88"]["EI"] is None and H["m_H 130"]["EI"] is None
                and H["mh +1 sigma"]["EI"] > H["ours"]["EI"] and H["a3 +1 sigma"]["EI"] > H["ours"]["EI"]
                and abs(H["mw +1 sigma"]["EI"] / H["ours"]["EI"] - 1) < 0.005
                and abs(D[1e3]["KP"] / D[1.0]["KP"] - 10) < 1e-9 and abs(D[1e-3]["KP"] / D[1.0]["KP"] - 0.1) < 1e-9)
    q, sh = o["qb"], o["shift"]
    ck["B4"] = (all(r["zeros"] and r["sym"] for r in q["rows"]) and abs(q["rows"][0]["Kr"] - KR) < 3e-3
                and abs(q["sK"][2] / q["sK"][0] - 1) < 1e-6 and abs(q["sT"][2] / q["sT"][0] - 1) < 0.02
                and 1 < q["sK"][0] < 1.5 and -2 < q["cT"] < -1
                and sh["bounce"] < 1e-14 and abs(float(q["sK"][0]) * u0["lam"]) < 1e-33)
    P = o["pos"]
    ck["B5"] = (P["2a"]["own"] == 1.0 and abs(P["2b"]["own"] - 2 ** (-2 / 3)) < 1e-12
                and abs(P["2b"]["top"] - 2 ** (-4 / 3)) < 1e-12 and abs(P["2P"]["own"] - 0.25) < 1e-12
                and abs(P["2P"]["planck_own"] - 1.0) < 1e-12 and P["2c"] == P["2b"])
    gaps = [r["u"]["gap"] for r in o["H"] if r["u"] and 171.0 <= r["p"]["mt"] <= 177.68 and r["p"]["mh"] <= 125.81]
    ck["B6"] = ("%.2g" % (u0["E5"] / E_LHC) == "2.7e+06" and "%.2f" % min(gaps) == "2.79"
                and 195 < o["mt_star"] < 196.5 and 98.5 < o["mh_star"] < 100 and 173.5 < o["mt_top"] < 174.2
                and "%.2f" % F["top"]["gap"] == "4.97" and "%.2f" % D[1.0]["gap"] == "5.07")
    return ck


def report(o=None):
    o = o or compute()
    ck = checks(o)
    print("B0 M's words (539) verbatim: %s" % ck["B0"])
    xh = o["xh"]
    print("B1 K(SAdS5) = 72 mu^2/r^8 + 10 Lambda^2/9 = ... + 40/ell^4 exactly: %s; xi's share at Y_min "
          "sqrt(2) Lambda/x_b: %s; x_h copper %.2g (bare 300 bits) / %.2g (on its least seed) / %.2g (7.6e22 bits), "
          "core %.2g (r_h/l5 %.2f): %s" % (o["K"]["exact"] and o["K"]["ell_form"], o["xi"], xh["cu"][0], xh["seed"],
                                           xh["cu"][1], xh["core"], xh["rh_core"], ck["B1"]))
    print("   %-14s %7s %7s %7s %10s %10s %10s %10s %6s" % ("universe", "m_t", "m_H", "alpha_s", "E_I GeV", "ell_H m",
                                                           "l5 m", "K_P m^-4", "gap"))
    for r in o["H"]:
        u = r["u"]
        print("   %-14s %7.2f %7.2f %7.4f %10s %10s %10s %10s %6s" % (
            r["name"], r["p"]["mt"], r["p"]["mh"], r["p"]["a3"], "%.3e" % r["EI"] if r["EI"] else "no zero",
            "%.3e" % u["ell"] if u else "--", "%.3e" % u["l5"] if u else "--", "%.3e" % u["KP"] if u else "--",
            "%.2f" % u["gap"] if u else "--"))
    for f, u in o["D"].items():
        print("   (D) Lambda x %-6g ell %.3e m, l5 %.3e m, K_P %.3e m^-4, Lambda5 l5^2 %.2e, gap %.2f"
              % (f, u["ell"], u["l5"], u["KP"], u["lam"], u["gap"]))
    for k, u in o["F"].items():
        print("   (F) %-4s ell %.3e m, l5 %.3e m, E5 %.3e GeV, K_P %.3e m^-4, Lambda5 l5^2 %.2e, gap %.2f"
              % (k, u["ell"], u["l5"], u["E5"], u["KP"], u["lam"], u["gap"]))
    print("B2 the readings: %s; B3 the table: %s" % (ck["B2"], ck["B3"]))
    q, sh = o["qb"], o["shift"]
    for l, r in zip(q["lams"], q["rows"]):
        print("   Lambda5 l5^2 %8.1e: K_max/K_cl %.12f, tau/2r_h %.10f, two horizons %s, symmetric %s"
              % (l, float(r["Kr"]), float(r["tau"]), r["zeros"], r["sym"]))
    print("B4 dK/dLambda %s; dtau/dLambda %s at mu %.3g, so d(tau/2r_h) = %.3f (r_h/ell)^2; induced in the scan: the "
          "bounce at most %.1e (ours %.1e), the crossing of copper's largest README at most %.2f (ours %.1e): %s"
          % (", ".join("%.6g" % float(s) for s in q["sK"]), ", ".join("%.4g" % float(s) for s in q["sT"]),
             q["rows"][0]["mu"], float(q["cT"]), sh["bounce"],
             abs(float(q["sK"][0]) * o["H"][0]["u"]["lam"]), sh["crossing"],
             abs(float(q["cT"])) * (sh["rh"] * o["H"][0]["u"]["l5"] / o["H"][0]["u"]["ell"]) ** 2, ck["B4"]))
    print("B5 positions, K_P factor (own ell / window top in SI / Higgs tie): %s: %s"
          % ("; ".join("%s %.4g/%.4g/%.4g" % (k, v["own"], v["top"], v["higgs"]) for k, v in o["pos"].items()),
             ck["B5"]))
    print("B6 E5/13.6 TeV ours %.2g; the tie meets the window's top at m_t %.2f GeV; E5 = 13.6 TeV at m_t %.1f GeV "
          "or m_H %.1f GeV (estimates): %s" % (o["H"][0]["u"]["E5"] / E_LHC, o["mt_top"], o["mt_star"], o["mh_star"],
                                        ck["B6"]))
    return ck


def selftest(quiet=False):
    o = compute()
    ck = checks(o)
    if not quiet:
        report(o)
    return all(ck.values())


MUTANTS = {"l5_power": "the Planckian curvature taken as l5^-2, not l5^-4 (B2-B6)",
           "reduced": "E5 with the reduced Planck length (384 excludes it) (B2)",
           "lambda_coeff": "Schwarzschild-AdS5's constant term taken as 5 Lambda^2/9 (B1)",
           "drop_lambda": "QB rerun with the bulk constant dropped (B4)"}


def mutants():
    caught = 0
    for m, why in MUTANTS.items():
        MUT.clear()
        MUT[m] = True
        _MOD.pop("Kf", None)
        try:
            ok = selftest(quiet=True)
        except Exception:
            ok = False
        caught += not ok
        print("mutant %-13s %s  (%s)" % (m, "caught" if not ok else "MISSED", why))
    MUT.clear()
    print("%d/%d caught" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    if "--selftest" in sys.argv:
        r = selftest()
        print("selftest:", "PASS" if r else "FAIL")
        sys.exit(0 if r else 1)
    report()
