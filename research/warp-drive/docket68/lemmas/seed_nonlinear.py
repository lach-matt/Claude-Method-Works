#!/usr/bin/env python3
"""seed_nonlinear.py -- item 527 (continued): the seed phase in the record's own exact vacuum equations, where the
escape is large enough to resolve, against the linear scattering computation -- the check of the second order's bound
(seed_types T7, seed_derive D6) in the exact equations rather than on model couplings.

M, 527: "it must be derived then proven"; 529: "Continue".  Labels: computed, deduced, estimate, M's.

  N0 (M's) 527 and 529, verbatim.
  N1 (computed) The configuration.  hf_core5's equations and scheme (hf_mirror5.evolve: T^2-mirror five-dimensional
     vacuum in compactified ingoing Bondi coordinates, nothing cut out, the inner boundary at the record's x = 1 on
     the seed), in the scheme's own regime: the seed mu0 = 1 (r_h0 = 1 in the code's units) at L = mu0/l5^2 = 102
     (copper's derived seed, seed_derive D3; the boundary y = (sqrt 72 mu0^2/L)^(-1/8) = 1.365, r_q = 0.54 r_h0), the
     reduced wavelength lam = 0.475 so that w r_h0 = 2.1 -- an escape of order 3e-2, which a grid resolves; at the
     derived point w r_h0 is 10.7 and the escape 1e-14, below any grid -- the envelope over 0.5 < v < 9.5 (three
     waves), Ny = 28, Nx = 16, cfl 2, to v = 12.  Two shells: A = 0.1 (0.0055 of the seed, strain lam A = 0.05 at the
     horizon) and A = 0.3 (0.049, strain 0.14): the first order's regime, with the second order's size changing nine
     times between them.  [A first configuration at mu0 = 0.04 (r_h0 = 0.2, lam = 0.095, the shell 0.4 and 10 times
     the seed, strain 0.3 and 1.5) was tried first: the scheme lost the horizon when the shell reached the hole
     (v = 1.25-1.5) at A = 0.2, 0.3 and 1.5, at Ny = 28 and 36 alike, and at A = 0.1 the mass at infinity scattered
     by 1.5e-3 after the shell, as large as the shell; a hole a fifth of the grid's design size is outside its reach.]
  N2 (computed) The measurement.  The escaped energy is the mass at infinity on the last cone less the hole's mass:
     (M_mean - r_AH^2)/(M_mean - mu0) at v = 12, r_AH the horizon bracket's midpoint; the ringdown's remainder is read
     from its change over the last half unit of v.
  N3 (computed) The linear prediction.  The pulse's energy spectrum (the rate of lam A env sin(v/lam); the carrier at
     w = 2.36, FWHM w r_h0 = 1.75-2.97) weights S(x) of the exact split at the hole's size as it grows: 3.08e-2
     (A = 0.1), 2.92e-2 (A = 0.3); at the seed's size 3.10e-2, monochromatic at the carrier 1.33e-2 -- the spectrum's
     width matters because S falls steeply (0.21 at x = 1.5, 1.3e-2 at 2.1, 3.1e-3 at 3).
  N4 (computed) The outcome: not resolved.  Both runs reach v = 12 with the angular residual at most 1.4e-3 (A = 0.1)
     and 1.2e-2 (A = 0.3), the v-residual at its worst sample 0.15 and 1.3, and the hole takes the shell -- but neither
     reading of the escaped energy reaches the predicted size.  (a) The mass at the compactified infinity, constant
     in the exact solution once the shell is in, swings by
     0.045 after the shell at A = 0.1 -- 8.3 times the whole shell (0.00547) -- and by 0.145 (3.0 shells) at A = 0.3:
     the reflected wave, of wavelength 3 in r, is compressed to nothing in y = r^(-1/2) as it runs out, and the
     expansion the mass aspect is read from breaks down; the "escape" it gives is -7.0 and -0.26 shells.  (b) The
     horizon, bracketed between the round spheres' first and last zeros of expansion, is still ringing at v = 12:
     0.995-1.009 (A = 0.1; mu +-0.028, 5.1 shells; its narrowest 0.0045 at v = 10.25, 1.6 shells) and 1.005-1.046
     (A = 0.3; 1.7 shells), lost outright at five samples while the l = 2 pulse deforms it; its reading of the
     escape is 0.27 and -0.03 shells.  The predicted escape, 1.7e-4 and 1.4e-3 in absolute mass, lies 100-260 times
     below these floors.
  N5 (deduced) The scheme's own regime cannot resolve the seed phase's escape with its present diagnostics (the mass
     aspect at the compactified infinity is made for ingoing data; the horizon finder for a round hole after the
     shell).  What would: a flux read through a worldtube at finite radius, a MOTS solved rather than bracketed, and
     a ringdown of some tens of r_h; and even then only the x = 2 regime, never the derived point's x = 10.7.  So the
     second order on the exact equations is not checked here; it stays an estimate on model couplings (seed_types T7,
     seed_derive D6), and the route that reaches the derived point is the second-order source derived symbolically
     from the record's own equations.
  Caveats.  The runs are the record's exact equations and are kept as record of what they show.  Ny = 28 on a
  Chebyshev grid is the resolution the step size allows in reasonable time.

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
LAM, M0, LSEED, NY, NX, VEND, V1, V2 = 0.475, 1.0, 102.0, 28, 16, 12.0, 0.5, 9.5
AMPS = (0.1, 0.3)
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
    return hashlib.md5((src + repr((LAM, M0, LSEED, NY, NX, VEND, V1, V2, AMPS, round(yex(), 9)))).encode()).hexdigest()


def _one(A):
    H.Data.__init__.__defaults__ = (V1, V2, 1.0)                 # the envelope over [V1, V2]
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
    """runs made by hf_mirror5.evolve with these arguments (run_<lam>_<A>_<Ny>_<Nx>_<m0>_<L>_<vend>_<v1>_<v2>.json)"""
    runs = {}
    files = {}
    for f in os.listdir(src):
        if f.startswith("run_") and f.endswith(".json"):
            try:
                files[tuple(float(x) for x in f[4:-5].split("_"))] = f
            except ValueError:
                pass
    for A in AMPS:
        runs[str(A)] = json.load(open(os.path.join(src, files[(LAM, A, float(NY), float(NX), M0, LSEED, VEND, V1, V2)])))
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
    late = [h for h in hist if h["v"] >= V2 + 0.25]
    Ms = [h["M_mean"] for h in late]; shell = h1["mu"] - M0
    rh = (h1["r_lo"] + h1["r_hi"])/2
    return dict(esc=e1, esc_prev=e0, drift=e1 - e0, shell=shell, mu_end=h1["mu"], M_end=h1["M_mean"], rh_end=rh,
                esc_h=(h1["mu"] - rh**2)/shell, width=h1["r_hi"] - h1["r_lo"], swing=max(Ms) - min(Ms),
                narrow=min((h["r_hi"] - h["r_lo"], h["v"]) for h in late if h["r_lo"] == h["r_lo"]),
                nans=sum(1 for h in hist if h["r_lo"] != h["r_lo"]), nz=max(h["nz"] for h in hist),
                resx=max(h["resx"] for h in hist), resv=max(h["resv"] for h in hist), spread=h1["M_max"] - h1["M_min"])


def _S():
    d = ST.data(); mS = SE._modes(d["rows"]); mT = SE._modes(SE.grid())
    S = np.zeros_like(SE.X)
    for k in range(1, ST.K + 1):
        S += d["pT"][k - 1]*SE._Rk(mT, k, SE.X) + d["pS"][k - 1]*SE._Rk(mS, k, SE.X)
    return lambda x: np.interp(x, SE.X, S)


def predict():
    """the linear escape for each shell: the pulse's energy spectrum weighting S at the hole's size as it grows"""
    Sx = _S()
    v = np.linspace(V1, V2, 600001); env = np.sin(np.pi*(v - V1)/(V2 - V1))**4
    dF = np.gradient(LAM*env*np.sin(v/LAM), v)
    w = np.linspace(0.02, 12, 6000)
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
        rr = rh[::2000]; sb = np.array([Sbar(r) for r in rr])
        out[str(A)] = dict(esc=float(np.trapezoid(np.interp(rh, rr, sb)*rate, v)/dmu[-1]), shell=float(dmu[-1]),
                           x0=float(rh[0]/LAM), xf=float(rh[-1]/LAM), S0=float(Sbar(rh[0])), Sf=float(Sbar(rh[-1])))
    return dict(runs=out, carrier=float(w[P.argmax()]), fwhm=(float(half[0]*np.sqrt(M0)), float(half[-1]*np.sqrt(M0))))


def compute():
    d = data(); pr = predict()
    ms = {A: measure(d["runs"][A]) for A in d["runs"]}
    resolved = all(max(2*ms[A]["width"], ms[A]["swing"]) < pr["runs"][A]["esc"]*ms[A]["shell"]/3 for A in ms)
    return dict(words=words(), yex=yex(), pr=pr, ms=ms, resolved=resolved)


def checks(o):
    ch = {}
    ch["N0 words of 527 and 529"] = o["words"]
    ch["N1 the inner boundary at x = 1 on the seed: y = 1.365 (r_q = 0.54 r_h0), inside the horizon y = 1"] = (
        abs(o["yex"] - 1.3646) < 0.002 and o["yex"] > M0**-0.25)
    p = o["pr"]
    ch["N3 the pulse: carrier w = 2.36 (1/lam 2.11), FWHM w r_h0 1.75-2.97; linear 3.08e-2 (A 0.1), 2.92e-2 (A 0.3)"] = (
        abs(p["carrier"] - 2.364) < 0.02 and abs(p["fwhm"][0] - 1.75) < 0.03 and abs(p["fwhm"][1] - 2.97) < 0.03
        and abs(p["runs"]["0.1"]["esc"]/3.08e-2 - 1) < 0.02 and abs(p["runs"]["0.3"]["esc"]/2.92e-2 - 1) < 0.02
        and abs(p["runs"]["0.3"]["xf"] - 2.156) < 0.005)
    m1, m3 = o["ms"]["0.1"], o["ms"]["0.3"]; p1, p3 = p["runs"]["0.1"], p["runs"]["0.3"]
    ch["N4 A = 0.1: the shell 0.00547; M at infinity swings 0.045 after it (8 shells); the bracket 0.014 at v = 12"] = (
        abs(m1["shell"] - 0.005469) < 2e-5 and abs(m1["swing"] - 0.0451) < 0.002 and abs(m1["width"] - 0.0139) < 0.001
        and abs(m1["esc"] + 7.04) < 0.3 and abs(m1["esc_h"] - 0.267) < 0.02 and m1["resx"] < 2e-3)
    ch["N4 A = 0.3: the shell 0.0492; the swing 0.145 (3 shells); the bracket 0.041; the horizon lost at 5 samples"] = (
        abs(m3["shell"] - 0.04922) < 1e-4 and abs(m3["swing"] - 0.1453) < 0.003 and abs(m3["width"] - 0.0409) < 0.002
        and m3["nans"] == 5 and abs(m3["esc_h"] + 0.029) < 0.01)
    ch["N4 unresolved: the floors (2 x bracket, the swing) exceed the predicted escape 100-260 times, both runs"] = (
        all(min(2*o["ms"][A]["width"], o["ms"][A]["swing"]) > 50*p["runs"][A]["esc"]*o["ms"][A]["shell"]
            for A in o["ms"]) and not o["resolved"])
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
            print("        shell %.5f; after it M at infinity swings %.4f (%.1f shells); r_AH at v = %g %.4f (bracket"
                  " %.4f, narrowest %.4f at v %.2f; lost at %d samples); 'escape' by M %.2f, by mu - r_AH^2 %.3f shells;"
                  " predicted %.2e abs; resx %.1e resv %.1e"
                  % (m["shell"], m["swing"], m["swing"]/m["shell"], VEND, m["rh_end"], m["width"], m["narrow"][0],
                     m["narrow"][1], m["nans"], m["esc"], m["esc_h"], q["esc"]*m["shell"], m["resx"], m["resv"]))
    print("  N4 resolved: %s" % o["resolved"])


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
