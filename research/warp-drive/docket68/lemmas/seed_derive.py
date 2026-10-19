#!/usr/bin/env python3
"""seed_derive.py -- item 527 (M-SEED-DERIVED): the seed's size and the emitter's wavelength derived from the math and
then proved, at both ends; the large end computed (526's item 2).

M, 527: "it must be derived then proven" (the seed's size, and with it the wavelength); "Continue with all SOURCE
work".  Labels: computed (exact unless marked), READ, deduced, criterion (an order-one physical criterion, not a
theorem), estimate, M's.

  D0 (M's) 527 and 529, verbatim.
  D1 (computed; criterion) The window's floor.  From the record's E5 = 3 pi hbar c r_h^2/(8 l5^3) (emitter_process),
     a quantum of the shell with energy 2 pi hbar c/lam has the horizon radius r_q^2 = (16/3) l5^3/lam.  It is not a
     hole of its own while its reduced wavelength exceeds r_q (the hoop criterion): lam > lam_P = (64 pi^2/3)^(1/3) l5
     = 5.949 l5.  source_spec U3's reading (each quantum below hbar c/l5) is 2 pi l5 = 1.056 lam_P.  The constant is a
     criterion: the derived floor is lam_P, with 2 pi l5 carried beside it.
  D2 (computed, exact in the law; checked on the grid) Monotone.  The energy let out while the hole grows from r_h0 is
     E_esc = (3/(16 pi)) (lam/l5)^2 I(2 pi r_h0/lam) E_P5, I(x0) = int_x0^inf x S(x) dx with S >= 0 (seed_escape E4
     generalized: E = (3 pi/8)(r_h/l5)^2 E_P5 while the hole is Tangherlini, E_P5 = hbar c/l5).  I is decreasing, so
     E_esc rises with lam at fixed r_h0 and falls with r_h0 at fixed lam: the least seed mu0(lam) is increasing, and
     the least seed over the window is at the floor.  Checked: mu0(lam) increases at 60 wavelengths from lam_P to
     46 l5 for all four anchors.
  D3 (computed) The derived seed.  Half a bit is (ln 2/(4 pi)) (l5/r_hf) E_P5 at the small end (the 5D first law,
     emitter_process C1) and (ln 2/(8 pi)) (l5/r0) E_P5 at the large end (the record's four-dimensional relation
     there, emitter_process C2: k T_H = hbar c^3/(8 pi G M), M = r0 c^2/(2 G); it equals E/(4 N) of earth_cap's own
     figures).  At lam_P: copper 102 l5^2 (r_h0 10.1 l5), the example README 61 l5^2, r0 = 20 ell 808 l5^2
     (28.4 l5), the Earth cap 917 l5^2 (30.3 l5); at 2 pi l5: 116, 69, 906, 1028.  At 10 l5 (522-525, a value in the
     window, now superseded as the wavelength): 324, 199, 2368, 2682.
  D4 (computed; deduced) The law.  x0* = 0.577 ln(r_hf/l5) + 1.75 at lam_P over the four anchors (residual 0.04):
     the slope is 1/ln((1 + sqrt 2)^2) = 0.567 to 2 %, because at large x the escape is set by the modes at their
     barrier tops, l near 2x, whose share of the record's power falls as (1 + sqrt 2)^(-2k) -- the poles of h(x) =
     sqrt(2/(1 + x^2)) at x = +-i (seed_types T3).  So the derived seed grows as (ln r_hf)^2: 102 to 917 l5^2 from a
     copper piece to the Earth cap, sixteen orders of magnitude in N.
  D5 (computed) The large end.  The derived seed is 28-30 l5 against ell = 9.07e19 l5: (r_h0/ell)^2 = 1e-37, so the
     seed phase is five-dimensional Tangherlini and the warp enters at that order; its shell (sigma_t = 113.9 GM/c^3,
     emitter_process C2; the same sin^8 profile, D = 9.444 sigma_t) reaches the seed phase at s = 3e-5 of its length.
  D6 (computed; estimate) The proof's second part at the derived point.  The strain at the horizon and the growth per
     crossing where escape is decided (r_h0 to 2 r_h0): copper 1.3e-4 and 3.8e-6; the example 8.5e-4 and 9.0e-5;
     r0 = 20 ell 9.3e-11 and 1.4e-17; the Earth cap 1.9e-11 and 7.0e-19.  The second order at 2w (seed_types T7,
     slope 3 from x = 3) lets out at most 1.2e-15 half bits (copper), 2.4e-13 (the example) and below 1e-35 at the
     large end.
  D7 (deduced) What is proved.  At (lam_P, mu0*) the shell delivers E5(N) within half a bit: to first order exactly,
     on the exact barriers (KI's V_T and V_S, READ), with the record's angular content split exactly; the second
     order estimated far below (model couplings; seed_types T7 and D6).  The floor's constant is a criterion.
  Caveats.  Linear scattering with the second order estimated, not the exact second-order equations.  The floor is
  an order-one criterion.  Beyond the computed window R follows the e^(-2 pi) law, an over-estimate of escape.

Imports seed_types.py (the exact split, its grids and its second order), seed_escape.py, source_spec.py and
earth_cap.py by path.  numpy, scipy, sympy, mpmath.
python3 seed_derive.py [--selftest | --mutants]
"""
import contextlib
import hashlib
import importlib.util
import inspect
import io
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
DATA = os.path.join(HERE, "data", "seed_derive.json")
MUT = set()
MUTANTS = {"floor_x2": "the floor doubled (D1, D3)",
           "large_5D_half": "the large end's half bit taken by the 5D first law (D3, D5)",
           "small_4D_half": "the small end's half bit taken by the 4D first law (D3)",
           "tail_x1e20": "the power above k = 45 inflated by 1e20 (D3, the large end)"}


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


ST = _load("seed_types.py", "sd_seed_types")
SE = ST.SE
SS = _load("source_spec.py", "sd_source_spec")
EC = _load("earth_cap.py", "sd_earth_cap")
LN2 = np.log(2)
LAMP = (64*np.pi**2/3)**(1/3)
ANCH = ("copper", "example", "r0 = 20 ell", "Earth cap")


def words():
    s = open(RULINGS).read()
    return ("it must be derived then proven" in s and "527. **Derive and prove the seed" in s
            and "529. **Continue (a direction, 2026-10-19)" in s)


def floor():
    lam = 2*LAMP if "floor_x2" in MUT else LAMP
    return dict(lamP=lam, u3=2*np.pi, ratio=2*np.pi/lam)


def anchors():
    """r_hf (or r0) in l5, the half bit h = E_half/E_P5, E_tot/E_P5 and the shell's D in l5, per anchor"""
    k = SS.consts(); l5, ell, lP = k["l5"], k["ell"], k["lP"]
    cs = SE.cases(); A5 = ST._load("hf_anchor5.py", "sd_anchor5").a1()
    ec = EC.compute()
    out = {}
    for n in ("copper", "example"):
        r = cs[n]["rhf"]
        h = (LN2/(8*np.pi) if "small_4D_half" in MUT else LN2/(4*np.pi))/r
        out[n] = dict(r=r, h=h, Etot=3*np.pi/8*r**2, D=A5["D"]*r, N=cs[n]["N"], end="small")
    for n, r0 in (("r0 = 20 ell", 20*ell), ("Earth cap", ec["r0"])):
        r = r0/l5
        h = (LN2/(4*np.pi) if "large_5D_half" in MUT else LN2/(8*np.pi))/r
        out[n] = dict(r=r, h=h, Etot=r*(l5/lP)**2/2, D=269.15/28.5*113.9*r/2, N=None, end="large")
    out["Earth cap"]["N"] = ec["N"]; out["Earth cap"]["E_J"] = ec["E"]
    out["_k"] = dict(l5=l5, ell=ell, lP=lP, EP5=k["hbar"]*k["c"]/l5)
    return out


def escape_I():
    d = ST.data(); mS = SE._modes(d["rows"]); mT = SE._modes(SE.grid())
    pS, pT = list(d["pS"]), list(d["pT"])
    if "tail_x1e20" in MUT:
        pS[-1] *= 1e20
    return ST._I(mS, mT, pS, pT)


def seed(I, lam, a):
    """the least r_h0 (l5) at wavelength lam (l5): (3/(16 pi)) lam^2 I(2 pi r_h0/lam) < h"""
    need = a["h"]*(16*np.pi/3)/lam**2
    ok = SE.X[I < need]
    if not len(ok):
        return dict(x=np.inf, rh=np.inf, mu0=np.inf)
    xs = ok[0]; rh = xs*lam/(2*np.pi)
    return dict(x=xs, rh=rh, mu0=rh**2)


def monotone(I, an):
    lams = np.linspace(floor()["lamP"], 46.0, 60)
    out = {}
    for n in ANCH:
        mus = np.array([seed(I, L_, an[n])["mu0"] for L_ in lams])
        out[n] = bool(np.all(np.diff(mus) > 0)) and np.isfinite(mus[-1])
    return out


def law(I, an):
    lamP = floor()["lamP"]
    xs = [seed(I, lamP, an[n])["x"] for n in ANCH]; lr = [np.log(an[n]["r"]) for n in ANCH]
    a, b = np.polyfit(lr, xs, 1)
    return dict(slope=a, icpt=b, resid=max(abs(np.polyval([a, b], lr) - np.array(xs))), q=1/np.log((1 + np.sqrt(2))**2))


def window(a, rh0, lam):
    """the strain at the horizon and the growth per crossing while the hole grows from rh0 to 2 rh0 (l5 units, c = 1):
    flux E_tot sin^8(pi s)/((35/128) D), mu = (8/(3 pi)) E/E_P5 (Tangherlini); h_H = sqrt2 lambar sqrt(mu') mu^-3/4"""
    s = np.logspace(-14, 0, 2000001)
    f = np.sin(np.pi*s)**8/((35/128)*a["D"])
    mu_eq = 8/(3*np.pi)*a["Etot"]
    cum = np.concatenate([[0], np.cumsum((f[1:] + f[:-1])/2*np.diff(s*a["D"]))])
    muv = rh0**2 + mu_eq*cum; mup = mu_eq*f
    win = (np.sqrt(muv) >= rh0) & (np.sqrt(muv) <= 2*rh0)
    if not win.any():
        win[0] = True
    hH = np.sqrt(2)*(lam/(2*np.pi))*np.sqrt(mup)*muv**-0.75
    eps = mup/np.sqrt(muv)
    return dict(hH=float(hH[win].max()), eps=float(eps[win].max()), s_lo=float(s[win].min()), s_hi=float(s[win].max()),
                cum_end=float(cum[-1]))


def _hash():
    src = "".join(inspect.getsource(f) for f in (ST.second_order, ST.VS, SE.V, SE.rstar))
    return hashlib.md5(src.encode()).hexdigest()


def s3():
    """the second order's largest outgoing-to-ingoing ratio at w r_h = 3 over l2 = 2, 4, both types, p = 3, 6
    (seed_types T7), computed once and cached under the hash of the code that gives it"""
    d = json.load(open(DATA)) if os.path.exists(DATA) else {}
    if d.get("hash") != _hash():
        vals = {"%s%d p%d" % (t, l2, p): ST.second_order(3.0, l2, p, V2)
                for t, V2 in (("T", SE.V), ("S", ST.VS)) for l2 in (2, 4) for p in (3, 6)}
        d = dict(hash=_hash(), s3=max(vals.values()), vals=vals)
        os.makedirs(os.path.dirname(DATA), exist_ok=True)
        json.dump(d, open(DATA, "w"), indent=1)
    return d["s3"]


def compute():
    an = anchors(); I = escape_I(); fl = floor()
    rows = {}
    for n in ANCH:
        a = an[n]
        rows[n] = {lam: seed(I, lam, a) for lam in (fl["lamP"], 2*np.pi, 10.0)}
    s3v = s3()
    win, so = {}, {}
    for n in ANCH:
        a = an[n]; d0 = rows[n][fl["lamP"]]
        w = window(a, d0["rh"], fl["lamP"]); win[n] = w
        sig = s3v*np.exp(-3.0*(d0["x"] - 3.0))
        frac = 4*w["hH"]**2*sig**2                                   # of the shell's energy
        so[n] = dict(sigma=sig, frac=frac, ratio=frac*a["Etot"]/a["h"])
    k = an["_k"]
    ec = an["Earth cap"]
    return dict(words=words(), fl=fl, an=an, rows=rows, mono=monotone(I, an), law=law(I, an), win=win, so=so,
                large=dict(ratio2=(rows["r0 = 20 ell"][fl["lamP"]]["rh"]/(k["ell"]/k["l5"]))**2,
                           first_law=ec["h"]*k["EP5"]/(ec["E_J"]/(4*ec["N"]))))


def checks(o):
    ch = {}
    ch["D0 words of 527 and 529"] = o["words"]
    fl = o["fl"]
    ch["D1 the floor lam_P = (64 pi^2/3)^(1/3) l5 = 5.949 l5 (hoop criterion); U3's 2 pi l5 is 1.056 lam_P"] = (
        abs(fl["lamP"] - 5.9491) < 1e-3 and abs(fl["ratio"] - 1.0562) < 1e-3)
    ch["D2 mu0(lam) increasing over the window at all four anchors: the least seed is at the floor"] = all(
        o["mono"].values())
    r = o["rows"]; P = fl["lamP"]
    ch["D3 small end at lam_P: copper 102 l5^2 (r_h0 10.1), the example README 61 l5^2; at 2 pi l5: 116, 69"] = (
        abs(r["copper"][P]["mu0"] - 102.4) < 1 and abs(r["copper"][P]["rh"] - 10.12) < 0.05
        and abs(r["example"][P]["mu0"] - 60.9) < 1 and abs(r["copper"][2*np.pi]["mu0"] - 115.9) < 1
        and abs(r["example"][2*np.pi]["mu0"] - 68.9) < 1)
    ch["D3 large end at lam_P: 20 ell 808 l5^2 (28.4), the Earth cap 917 l5^2 (30.3); at 2 pi: 906, 1028"] = (
        abs(r["r0 = 20 ell"][P]["mu0"] - 808.5) < 2 and abs(r["r0 = 20 ell"][P]["rh"] - 28.43) < 0.05
        and abs(r["Earth cap"][P]["mu0"] - 917.1) < 2 and abs(r["Earth cap"][P]["rh"] - 30.28) < 0.05
        and abs(r["r0 = 20 ell"][2*np.pi]["mu0"] - 906.0) < 2 and abs(r["Earth cap"][2*np.pi]["mu0"] - 1027.8) < 2)
    ch["D3 at 10 l5 (superseded as the wavelength): 324, 199 (522-525), 2368, 2682"] = (
        abs(r["copper"][10.0]["mu0"] - 323.7) < 1 and abs(r["example"][10.0]["mu0"] - 198.8) < 1
        and abs(r["r0 = 20 ell"][10.0]["mu0"] - 2368) < 3 and abs(r["Earth cap"][10.0]["mu0"] - 2682) < 3)
    lw = o["law"]
    ch["D4 x0* = 0.577 ln(r_hf/l5) + 1.75, residual < 0.05; the slope is 1/ln((1+sqrt2)^2) = 0.567 to 2 %"] = (
        abs(lw["slope"] - 0.5772) < 0.003 and abs(lw["icpt"] - 1.753) < 0.02 and lw["resid"] < 0.05
        and abs(lw["slope"]/lw["q"] - 1) < 0.02)
    lg = o["large"]
    ch["D5 large end: (r_h0/ell)^2 = 1e-37; the 4D half bit equals E/(4N) of earth_cap's figures to 1e-3"] = (
        1e-38 < lg["ratio2"] < 1e-36 and abs(lg["first_law"] - 1) < 1e-3)
    w = o["win"]
    ch["D6 strain/growth where escape is decided: 1.3e-4/3.8e-6 (copper), 8.5e-4/9e-5, 9.3e-11/1.4e-17, 2e-11/7e-19"] = (
        abs(w["copper"]["hH"]/1.34e-4 - 1) < 0.02 and abs(w["copper"]["eps"]/3.76e-6 - 1) < 0.02
        and abs(w["example"]["hH"]/8.50e-4 - 1) < 0.02 and abs(w["example"]["eps"]/8.97e-5 - 1) < 0.02
        and abs(w["r0 = 20 ell"]["hH"]/9.31e-11 - 1) < 0.02 and abs(w["r0 = 20 ell"]["eps"]/1.43e-17 - 1) < 0.02
        and abs(w["Earth cap"]["hH"]/1.93e-11 - 1) < 0.02 and abs(w["Earth cap"]["eps"]/6.95e-19 - 1) < 0.02)
    so = o["so"]
    ch["D6 the second order at the derived point: 1.2e-15 half bits (copper), 2.4e-13 (example), < 1e-35 (large)"] = (
        abs(so["copper"]["ratio"]/1.17e-15 - 1) < 0.05 and abs(so["example"]["ratio"]/2.36e-13 - 1) < 0.05
        and so["r0 = 20 ell"]["ratio"] < 1e-35 and so["Earth cap"]["ratio"] < 1e-35)
    return ch


def report(o=None):
    o = o or compute()
    for k_, v_ in checks(o).items():
        print("%-118s %s" % (k_[:118], "PASS" if v_ else "FAIL"))
    fl = o["fl"]
    print("  D1 lam_P %.4f l5; 2 pi l5 / lam_P = %.4f" % (fl["lamP"], fl["ratio"]))
    for n in ANCH:
        a = o["an"][n]
        print("  D3 %-12s r %.3e l5  h %.3e  " % (n, a["r"], a["h"]) + "  ".join(
            "lam %5.2f: x0 %5.2f r_h0 %6.2f mu0 %7.1f" % (lam, d["x"], d["rh"], d["mu0"])
            for lam, d in o["rows"][n].items()))
    lw = o["law"]
    print("  D4 x0* = %.4f ln(r/l5) + %.3f (resid %.3f); 1/ln((1+sqrt2)^2) = %.4f"
          % (lw["slope"], lw["icpt"], lw["resid"], lw["q"]))
    print("  D5 (r_h0/ell)^2 = %.1e; 4D half bit / (E/4N) = %.6f" % (o["large"]["ratio2"], o["large"]["first_law"]))
    for n in ANCH:
        w, s_ = o["win"][n], o["so"][n]
        print("  D6 %-12s h_H %.2e  growth/crossing %.2e  (s %.1e-%.1e); second order sigma(x*) %.2e, %.2e of the shell"
              " = %.2e half bits" % (n, w["hH"], w["eps"], w["s_lo"], w["s_hi"], s_["sigma"], s_["frac"], s_["ratio"]))


def selftest():
    c = checks(compute())
    n = sum(c.values())
    for k_, v_ in c.items():
        print("%-118s %s" % (k_[:118], "PASS" if v_ else "FAIL"))
    print("seed_derive.py: %d/%d" % (n, len(c)))
    return n == len(c)


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            c = checks(compute()); failed = [k[:44] for k, v in c.items() if not v]
        except Exception as ex:                                  # noqa: BLE001
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-14s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
