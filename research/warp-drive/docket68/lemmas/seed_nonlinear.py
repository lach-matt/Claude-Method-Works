#!/usr/bin/env python3
"""seed_nonlinear.py -- item 527 (continued): the seed phase in the record's own exact vacuum equations, where the
escape is large enough to resolve, against the linear scattering computation -- the check of the second order's bound
(seed_types T7, seed_derive D6) in the exact equations rather than on model couplings.

M, 527: "it must be derived then proven"; 529: "Continue".  Labels: computed, deduced, estimate, M's.

  N0 (M's) 527 and 529, verbatim.
  N1 (computed) The configuration.  hf_core5's equations and scheme (hf_mirror5.evolve: T^2-mirror five-dimensional
     vacuum in compactified ingoing Bondi coordinates, nothing cut out, the inner boundary at the record's x = 1 on
     the seed), with the seed mu0 = 0.04 (r_h0 = 0.2 in the code's units) at L = mu0/l5^2 = 116 (copper's seed at
     2 pi l5, seed_derive D3; the boundary y = (sqrt 72 mu0^2/L)^(-1/8) = 3.10, r_q = 0.52 r_h0), the reduced wavelength
     lam = 0.095 so that w r_h0 = 2.1 -- an escape of order 1e-2, which a grid resolves; at the derived point w r_h0 is
     10.7 and the escape 1e-14, below any grid -- Ny = 28, Nx = 12, cfl 2, to v = 5 (the shell over 0.5 < v < 3.5).
     Two shells: A = 0.3 (0.016, 0.41 of the seed: the linear regime) and A = 1.5 (0.41, ten times the seed: the hole
     grows from w r_h = 2.1 to 7.1, as it does through the seed phase of the delivery).
  N2 (computed) The measurement.  The escaped energy is the mass at infinity on the last cone less the hole's mass:
     (M_mean - r_AH^2)/(M_mean - mu0) at v = 5, r_AH the horizon bracket's midpoint; the ringdown's remainder is read
     from its change over the last half unit of v.
  N3 (computed) The linear prediction.  The pulse's energy spectrum (the rate of lam A env sin(v/lam); the carrier at
     w = 11.0, FWHM w r_h0 = 1.8-2.6) weights S(x) of the exact split at the hole's size as it grows:
     1.29e-2 (A = 0.3), 1.08e-3 (A = 1.5).  Monochromatic at the carrier, growth-weighted: 9.4e-3 and 8.5e-4; the
     spectrum's width matters because S falls steeply (0.21 at x = 1.5, 1.3e-2 at 2.1, 3.1e-3 at 3).
  N4 (computed) The comparison: filled from the runs (--build, about an hour on two processes, or --import of runs made
     by the same code with the same arguments).
  N5 (deduced) What it says of the second order.
  Caveats.  One wavelength and one seed size, in the resolvable regime; the delivery's own regime (w r_h0 = 10.7) is
  reached by the exponential law the linear computation proves, not by the grid.  Ny = 28 on a Chebyshev grid is the
  resolution the step size allows in reasonable time; the runs' own residuals are reported.

Imports hf_core5.py (and through it hf_mirror5.py) and seed_types.py by path.  numpy, scipy, sympy, mpmath.
python3 seed_nonlinear.py [--selftest | --mutants | --build | --import DIR]
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
DATA = os.path.join(HERE, "data", "seed_nonlinear.json")
LAM, M0, LSEED, NY, NX, VEND = 0.095, 0.04, 116.0, 28, 12, 5.0
AMPS = (0.3, 1.5)
MUT = set()
MUTANTS = {"no_spectrum": "the prediction monochromatic at the carrier (N3)",
           "fixed_hole": "the prediction at the seed's size, the growth ignored (N3)",
           "vaidya_mass": "the hole's mass taken as the Vaidya mu in place of the horizon's (N2)"}


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


C5 = _load("hf_core5.py", "sn_hf_core5")
H = C5.H
ST = _load("seed_types.py", "sn_seed_types")
SE = ST.SE


def words():
    s = open(RULINGS).read()
    return "it must be derived then proven" in s and "529. **Continue (a direction, 2026-10-19)" in s


def yex():
    """the record's x = 1 on the seed: r_q^4 = sqrt72 mu0 l5^2 with l5^2 = mu0/L (hf_core5.y_core has mu0 = 1)"""
    return (np.sqrt(72)*M0**2/LSEED)**-0.125


def _hash():
    src = "".join(inspect.getsource(f) for f in (H.evolve, H.rhs, H.diag, H.horizon, H.Data, H.Grid))
    return hashlib.md5((src + repr((LAM, M0, LSEED, NY, NX, VEND, AMPS, round(yex(), 9)))).encode()).hexdigest()


def _one(A):
    return H.evolve(LAM, A, NY, NX, m0=M0, yex=yex(), cfl=2.0, v_end=VEND, every=0.25)


def build():
    """the two evolutions (about an hour each; run on two processes), stored with the hash of the code and arguments"""
    from multiprocessing import Pool
    with Pool(2) as p:
        hs = p.map(_one, AMPS)
    d = dict(hash=_hash(), runs={str(A): h for A, h in zip(AMPS, hs)})
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    json.dump(d, open(DATA, "w"))
    return d


def import_runs(src):
    """runs made by hf_mirror5.evolve with these arguments (run_<lam>_<A>_<Ny>_<Nx>_<m0>_<L>_<vend>.json), seated"""
    runs = {}
    for A in AMPS:
        name = "run_%s.json" % "_".join("%g" % x for x in (LAM, A, NY, NX, M0, LSEED, VEND))
        runs[str(A)] = json.load(open(os.path.join(src, name)))
    d = dict(hash=_hash(), runs=runs)
    os.makedirs(os.path.dirname(DATA), exist_ok=True)
    json.dump(d, open(DATA, "w"))
    return d


def data():
    d = json.load(open(DATA)) if os.path.exists(DATA) else {}
    return d if d.get("hash") == _hash() else build()


def measure(hist):
    """escaped share at the end and half a unit of v before; the horizon's width; the residuals"""
    def at(v):
        h = min(hist, key=lambda h: abs(h["v"] - v))
        hole = h["mu"] if "vaidya_mass" in MUT else ((h["r_lo"] + h["r_hi"])/2)**2
        return (h["M_mean"] - hole)/(h["M_mean"] - M0), h
    e1, h1 = at(VEND); e0, h0 = at(VEND - 0.5)
    return dict(esc=e1, esc_prev=e0, drift=e1 - e0, shell=h1["M_mean"] - M0, mu_end=h1["mu"], M_end=h1["M_mean"],
                rh_end=(h1["r_lo"] + h1["r_hi"])/2, width=h1["r_hi"] - h1["r_lo"], nz=max(h["nz"] for h in hist),
                resx=max(h["resx"] for h in hist), resv=max(h["resv"] for h in hist),
                spread=h1["M_max"] - h1["M_min"])


def _S():
    d = ST.data(); mS = SE._modes(d["rows"]); mT = SE._modes(SE.grid())
    S = np.zeros_like(SE.X)
    for k in range(1, ST.K + 1):
        S += d["pT"][k - 1]*SE._Rk(mT, k, SE.X) + d["pS"][k - 1]*SE._Rk(mS, k, SE.X)
    return lambda x: np.interp(x, SE.X, S)


def predict():
    """the linear escape for each shell: the pulse's energy spectrum weighting S at the hole's size as it grows"""
    Sx = _S()
    v = np.linspace(0.5, 3.5, 300001); env = np.sin(np.pi*(v - 0.5)/3)**4
    dF = np.gradient(LAM*env*np.sin(v/LAM), v)
    w = np.linspace(0.1, 40, 8000)
    P = abs(np.array([np.trapezoid(dF*np.exp(-1j*om*v), v) for om in w]))**2; P /= np.trapezoid(P, w)
    half = w[P > P.max()/2]
    if "no_spectrum" in MUT:
        Sbar = lambda rh: Sx(rh/LAM)                              # noqa: E731
    else:
        Sbar = lambda rh: np.trapezoid(P*Sx(w*rh), w)             # noqa: E731
    out = {}
    for A in AMPS:
        dmu = (2/9)*A**2*np.cumsum(np.concatenate([[0], (env[1:]**2 + env[:-1]**2)/2*np.diff(v)]))
        rh = np.sqrt(M0 + dmu); rate = np.gradient(dmu, v)
        if "fixed_hole" in MUT:
            rh = np.full_like(rh, rh[0])
        rr = rh[::1000]; sb = np.array([Sbar(r) for r in rr])
        out[str(A)] = dict(esc=float(np.trapezoid(np.interp(rh, rr, sb)*rate, v)/dmu[-1]), shell=float(dmu[-1]),
                           x0=float(rh[0]/LAM), xf=float(rh[-1]/LAM), S0=float(Sbar(rh[0])), Sf=float(Sbar(rh[-1])))
    return dict(runs=out, carrier=float(w[P.argmax()]), fwhm=(float(half[0]*np.sqrt(M0)), float(half[-1]*np.sqrt(M0))))


def compute():
    d = data(); pr = predict()
    ms = {A: measure(d["runs"][A]) for A in d["runs"]}
    return dict(words=words(), yex=yex(), pr=pr, ms=ms,
                ratio={A: ms[A]["esc"]/pr["runs"][A]["esc"] for A in ms})


def checks(o):
    ch = {}
    ch["N0 words of 527 and 529"] = o["words"]
    ch["N1 the inner boundary at x = 1 on the seed: y = 3.10 (r_q = 0.52 r_h0), inside the horizon y = 2.24"] = (
        abs(o["yex"] - 3.098) < 0.01 and o["yex"] > M0**-0.25)
    p = o["pr"]
    ch["N3 the pulse: carrier w = 11.0 (1/lam 10.5), FWHM w r_h0 1.8-2.6; linear 1.29e-2 (A 0.3), 1.08e-3 (A 1.5)"] = (
        abs(p["carrier"] - 11.03) < 0.1 and abs(p["fwhm"][0] - 1.82) < 0.05 and abs(p["fwhm"][1] - 2.58) < 0.05
        and abs(p["runs"]["0.3"]["esc"]/1.29e-2 - 1) < 0.02 and abs(p["runs"]["1.5"]["esc"]/1.08e-3 - 1) < 0.02
        and abs(p["runs"]["1.5"]["xf"] - 7.06) < 0.02)
    return ch


def report(o=None):
    o = o or compute()
    for k_, v_ in checks(o).items():
        print("%-118s %s" % (k_[:118], "PASS" if v_ else "FAIL"))
    p = o["pr"]
    print("  N1 yex %.4f; N3 carrier %.2f, FWHM x %.2f-%.2f" % (o["yex"], p["carrier"], *p["fwhm"]))
    for A in p["runs"]:
        q = p["runs"][A]; m = o["ms"].get(A)
        print("  A %-4s shell %.4f (x %.2f -> %.2f): linear %.4e (Sbar %.3e -> %.3e)" % (A, q["shell"], q["x0"], q["xf"],
                                                                                    q["esc"], q["S0"], q["Sf"]))
        if m:
            print("        measured %.4e (at v - 1/2: %.4e, drift %.1e); shell %.4f, M_end %.6f, mu_end %.6f, r_AH %.5f "
                  "(width %.1e), nz %d, resx %.1e, resv %.1e, spread %.1e; measured/linear %.3f"
                  % (m["esc"], m["esc_prev"], m["drift"], m["shell"], m["M_end"], m["mu_end"], m["rh_end"], m["width"],
                     m["nz"], m["resx"], m["resv"], m["spread"], o["ratio"][A]))


def selftest():
    c = checks(compute())
    n = sum(c.values())
    for k_, v_ in c.items():
        print("%-118s %s" % (k_[:118], "PASS" if v_ else "FAIL"))
    print("seed_nonlinear.py: %d/%d" % (n, len(c)))
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
        print("mutant %-12s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--build" in sys.argv:
        print("built: %s" % list(build()["runs"]))
        sys.exit(0)
    if "--import" in sys.argv:
        print("imported: %s" % list(import_runs(sys.argv[sys.argv.index("--import") + 1])["runs"]))
        sys.exit(0)
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
