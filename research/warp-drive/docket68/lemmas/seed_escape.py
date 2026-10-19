#!/usr/bin/env python3
"""seed_escape.py -- item 522 (SOURCE continued): how much of the shell's energy the seed hole sends back out, and the
least seed that delivers the record's energy to within half a bit at the anchored wavelength.

M, 522: "Two tasks: Continue SOURCE AND Prepare instructions for another session ...".  SOURCE (490, 509) asks the
shell to put E5(N) into the hole to within half a bit (emitter_process C1).  517-520 left the seed phase open: while
the hole is small against the wavelength it reflects part of what arrives, and the reflected part leaves.  This is
not N1* (521): it is linear scattering off the hole as it stands, at the anchored wavelength 10 l5.  Labels: computed
(exact unless marked), READ (verbatim at source, 2026-10-19), deduced, caveat, M's.

  E0 (M's) 522, verbatim.
  E1 (computed, exact; READ) The barrier.  A massless field Phi = r^(-3/2) psi(r*) Y_l on five-dimensional
     Tangherlini (f = 1 - mu/r^2) obeys psi'' + (w^2 - V) psi = 0 with V = f [((l+1)^2 - 1/4)/r^2 + 9 mu/(4 r^4)]
     (computed from box Phi = 0).  Kodama and Ishibashi, Prog. Theor. Phys. 110, 701 (2003), READ: the tensor
     harmonics have "k_T^2 = l(l + n - 1) - 2; l = 1, 2, ..., for K = 1" (5.2), and "box H_T + (n/r) Dr.DH_T
     - (k_T^2 + 2K)/r^2 H_T = 0" (5.3); at n = 3, K = 1, k_T^2 + 2K = l(l + 2), the massless scalar's eigenvalue, so
     (5.3) is the scalar's equation: the tensor-type wave meets exactly this barrier.  The top sits at w r_h near
     (l + 1)/2 (impact parameter 2 r_h).
  E2 (computed; cached under a hash of the solver's code) R_l(w r_h), the reflected share of a wave sent in from
     outside, for l = 2k, k = 0..45, from (k + 1/2) - 3 to (k + 1/2) + 6 in w r_h, step 1/4: 1681 integrations (DOP853,
     rtol 1e-11; ingoing at the horizon, matched to Hankel waves at r* = 150 r_h).  R + T = 1 to 1.2e-9; R is near 1/2
     at the top (0.50-0.56 for k >= 1); above the barrier R falls 1e3-6e3 per unit of w r_h; at l = 0 the far fall is
     e^(-2 pi w r_h), the law set by the potential's singularity at r = 0 (Im r* = pi r_h / 2).
  E3 (computed, exact quadrature) The angular power.  The torus-invariant harmonics with eigenvalue -l(l+2) are
     P_k(cos 2 theta), l = 2k.  The record's profiles on the two torus directions, c^2 h and s^2 h with h = sqrt(2/(1 +
     x^2)), x = cos 2 theta (hf_mirror5's data, kn_gauge K8's profiles), carry power p_k: p0 = 0.7768, p1 = 0.2129,
     sum 1 exactly, and successive ratios alternating about (1 + sqrt 2)^(-2) = 0.1716 and closing on it (the poles
     of h at x = +-i).
  E4 (computed; deduced) Escape and the least seed.  As the hole grows from r_h0 to r_hf by absorbing the shell
     (mu = r_h^2, so the energy taken in grows as d(r_h^2)), the share leaving is (2/(w r_hf)^2) int_(w r_h0) x S(x)
     dx with S = sum_k p_k R_2k (first order in S).  Half a bit of E5(N) is 1/(3N) of it (E5 ~ N^(2/3); equal to
     emitter_process's bit_r/(2 E5) to 1e-8).  At lam = 10 l5:
     - copper (emitter_process: N 1.282e21, r_hf 5.647e6 l5): the record's least seed (508, sqrt 72 l5^2, r_h 2.913 l5)
       lets 3.97e-15 out, 1.5e7 half bits; the least seed for half a bit is w r_h 11.28, r_h0 17.95 l5, mu0 322 l5^2;
     - the example README (hf_anchor5: N 2.743e15, r_hf 72762 l5): 2.39e-11, 2.0e5 half bits; w r_h 8.77, r_h0
       13.96 l5, mu0 195 l5^2;
     - hf_core5's computed seeds: mu0 = 1000 l5^2 passes both, mu0 = 100 fails both.
     The hole grows slowly on the record's shell: dr_h/dv <= 0.0110 (d mu/dv / sqrt mu <= 0.0219), computed.
  E5 (computed; deduced) Sensitivity, and what SOURCE now holds.  The harmonic labelling moved by one (each mode read
     off the grid at k - 1 or k + 1) moves the least seed to 16.29 / 19.60 l5 (copper), 12.25 / 15.67 l5 (example):
     the verdicts stand.  The least seed's own wavelength: the record's sqrt 72 l5^2 delivers within half a bit for
     lam <= 1.95 l5 (copper), 2.52 l5 (example).  So SOURCE at 10 l5 needs the seed to be a size (508) of at least
     mu0 = 322 l5^2 (copper), and the seed of hf_core5's runs at mu0 = 1000 meets it; 508's least size sqrt 72 l5^2 is
     the least hole, not the least seed for delivery.  (521's twenty wavelengths is the edge of the remainder
     estimate, not this requirement: here r_h0 >= 1.8 lam.)
  Caveats.  The angular content is carried on scalar harmonics; the tensor-type barrier is identical (E1, READ), the
  scalar-type the same at high l (eikonal), not computed here.  Linear adiabatic scattering is assumed (E4's growth
  rate).  Beyond the computed window R is extended by the e^(-2 pi) law from its last value above 1e-15 -- slower than
  the computed fall, so an over-estimate of escape.

Imports emitter_process.py and hf_anchor5.py by path.  numpy, scipy, sympy, mpmath.
python3 seed_escape.py [--selftest | --mutants | --build-grid]
"""
import contextlib
import hashlib
import importlib.util
import inspect
import io
import json
import os
import sys

import mpmath as mp
import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
GRID = os.path.join(HERE, "data", "seed_escape_R.json")
K = 45
LAM = 10.0
MUT = set()
MUTANTS = {"truncate": "modes above k = 5 dropped from the angular sum (E3-E4)",
           "half_1_over_N": "half a bit taken as 1/N of the energy in place of 1/(3N) (E4)",
           "barrier_shift": "every barrier moved out by half a unit of w r_h (E4)",
           "lam_1": "the wavelength taken as 1 l5 in place of 10 (E4)"}


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    s = open(RULINGS).read()
    return ('"Two tasks:' in s and "Continue SOURCE" in s
            and "522. **Continue SOURCE; hand N1* and the counterpart theorem" in s)


def potential():
    """V from box Phi = 0 on Tangherlini (r_h = 1 units below), and KI (5.3)'s coefficient at n = 3, K = 1"""
    t, r, mu, w, L = sp.symbols("t r mu omega ell", positive=True)
    f = 1 - mu/r**2
    psi = sp.Function("psi")(r)
    Phi = r**sp.Rational(-3, 2)*psi*sp.exp(-sp.I*w*t)
    box = -sp.diff(Phi, t, 2)/f + sp.diff(r**3*f*sp.diff(Phi, r), r)/r**3 - L*(L + 2)*Phi/r**2
    e = sp.simplify(box*f*r**sp.Rational(3, 2)*sp.exp(sp.I*w*t))
    V = sp.simplify(w**2 - (e - f*sp.diff(f*sp.diff(psi, r), r))/psi)
    form = f*(((L + 1)**2 - sp.Rational(1, 4))/r**2 + sp.Rational(9, 4)*mu/r**4)
    n, Kc = 3, 1
    kT2 = L*(L + n - 1) - 2
    return dict(V=V, exact=sp.simplify(V - form) == 0, ki=sp.expand(kT2 + 2*Kc - L*(L + 2)) == 0)


def V(u, L):
    r = 1 + u
    return (2*u + u*u)/(r*r)*(((L + 1)**2 - 0.25)/r**2 + 2.25/r**4)


def rstar(u):
    return 1 + u + 0.5*np.log(u/(2 + u))


def refl(L, w, u0=1e-15, rmax=150.0, rtol=1e-11):
    """|A_out/A_in|^2 and 1/|A_in|^2 for psi = e^(-i w r*) at the horizon, r = 1 + u in r_h units"""
    from scipy.integrate import solve_ivp
    from scipy.special import h1vp, h2vp, hankel1, hankel2
    s0 = rstar(u0)
    y0 = [np.cos(-w*s0), np.sin(-w*s0), w*np.sin(-w*s0), -w*np.cos(-w*s0), u0]

    def rhs(s, y):
        u = y[4]; q = V(u, L) - w*w
        return [y[2], y[3], q*y[0], q*y[1], (2*u + u*u)/(1 + u)**2]
    sol = solve_ivp(rhs, [s0, rmax], y0, method="DOP853", rtol=rtol, atol=1e-14)
    s = sol.t[-1]; y = sol.y[:, -1]
    psi = y[0] + 1j*y[1]; dpsi = y[2] + 1j*y[3]
    nu = L + 1; z = w*s; c = np.sqrt(np.pi*z/2)
    ho = c*hankel1(nu, z); hi = c*hankel2(nu, z)
    dho = w*(c*h1vp(nu, z) + hankel1(nu, z)*np.sqrt(np.pi/(8*z)))
    dhi = w*(c*h2vp(nu, z) + hankel2(nu, z)*np.sqrt(np.pi/(8*z)))
    Ain, Aout = np.linalg.solve(np.array([[hi, ho], [dhi, dho]]), [psi, dpsi])
    return abs(Aout/Ain)**2, 1/abs(Ain)**2


def _tasks():
    out = []
    for k in range(K + 1):
        xc = k + 0.5
        out += [(k, float(x)) for x in np.arange(max(0.25, xc - 3.0), xc + 6.01, 0.25)]
    return out


def _job(a):
    k, x = a
    R, T = refl(2*k, x)
    return [k, x, R, T]


def _hash():
    src = "".join(inspect.getsource(f) for f in (V, rstar, refl, _tasks, _job))
    return hashlib.md5(src.encode()).hexdigest()


def build_grid():
    """the 1681 integrations (about ten minutes on four processes), stored with the hash of the code that made them"""
    from multiprocessing import Pool
    with Pool(4) as p:
        rows = p.map(_job, _tasks(), chunksize=4)
    os.makedirs(os.path.dirname(GRID), exist_ok=True)
    json.dump(dict(hash=_hash(), rows=rows), open(GRID, "w"))
    return rows


def grid():
    d = json.load(open(GRID)) if os.path.exists(GRID) else {}
    return d["rows"] if d.get("hash") == _hash() else build_grid()


def power():
    mp.mp.dps = 30
    h = lambda x: mp.sqrt(2/(1 + x**2))                          # noqa: E731
    p = []
    for k in range(K + 1):
        ak = (2*k + 1)/mp.mpf(2)*mp.quad(lambda x: (1 + x)/2*h(x)*mp.legendre(k, x), [-1, 0, 1])
        bk = (2*k + 1)/mp.mpf(2)*mp.quad(lambda x: (1 - x)/2*h(x)*mp.legendre(k, x), [-1, 0, 1])
        p.append(float((ak**2 + bk**2)/(2*k + 1)))
    return np.array(p)


def _modes(rows):
    m = {}
    for k, x, R, T in rows:
        m.setdefault(k, []).append((x, R))
    return {k: np.array(sorted(v)).T for k, v in m.items()}


def _Rk(md, k, x, dx=0.0):
    xs, Rs = md[k]
    x = x - dx
    good = Rs >= 1e-15                                             # below this the matching radius sets the floor
    xl, Rl = xs[good][-1], Rs[good][-1]
    out = np.where(x < xs[0], 1.0, np.exp(np.interp(x, xs[good], np.log(Rs[good]))))
    return np.where(x > xl, Rl*np.exp(-2*np.pi*(x - xl)), out)  # beyond: the 2 pi law, slower than the computed fall


X = np.arange(0.25, 80.0, 0.005)


def _I(md, p, shift=0):
    dx = 0.5 if "barrier_shift" in MUT else 0.0
    kmax = 5 if "truncate" in MUT else K
    S = sum(p[k]*_Rk(md, min(max(k + shift, 0), K), X, dx) for k in range(kmax + 1)) + p[-1]/(1 - 0.2)
    xS = X*S
    return np.concatenate([np.cumsum((xS[1:] + xS[:-1])[::-1]/2*np.diff(X)[::-1])[::-1], [0.0]])


def cases():
    E = _load("emitter_process.py", "se_emitter").definition()
    A = _load("hf_anchor5.py", "se_anchor").a1()
    return {"copper": dict(N=E["N"], rhf=E["rh"]/A["l5"], half_em=E["bit_r"]/(2*E["E5"])),
            "example": dict(N=A["N"], rhf=A["rh_l5"], half_em=None)}


def escape(md, p, cs, lam=None, shift=0):
    lam = lam or (1.0 if "lam_1" in MUT else LAM)
    I = _I(md, p, shift)
    out = {}
    for name, c in cs.items():
        wr = 2*np.pi*c["rhf"]/lam
        half = 1/c["N"] if "half_1_over_N" in MUT else 1/(3*c["N"])
        need = half*wr**2/2
        x0 = 2*np.pi*72**0.25/lam
        esc0 = 2*np.interp(x0, X, I)/wr**2
        xs = X[I < need][0]
        rh = xs*lam/(2*np.pi)
        ok = {mu0: 2*np.interp(2*np.pi*np.sqrt(mu0)/lam, X, I)/wr**2 < half for mu0 in (100.0, 1000.0)}
        out[name] = dict(half=half, esc0=esc0, nhalf=esc0/half, x=xs, rh=rh, mu0=rh**2, ok=ok)
    return out


def lam_least(md, p, cs):
    """the longest wavelength at which the record's least seed (sqrt 72 l5^2) delivers within half a bit"""
    I = _I(md, p)
    out = {}
    for name, c in cs.items():
        lo, hi = 0.1, 10.0
        for _ in range(60):
            lam = 0.5*(lo + hi); wr = 2*np.pi*c["rhf"]/lam
            if 2*np.interp(2*np.pi*72**0.25/lam, X, I)/wr**2 < 1/(3*c["N"]):
                lo = lam
            else:
                hi = lam
        out[name] = lo
    return out


def growth():
    """dr_h/dv over the record's shell (kn_gauge K8's profile, r_hf and its time units)"""
    A = _load("hf_anchor5.py", "se_anchor2").a1()
    mu0 = A["seed"]/A["rh_l5"]**2; dmu = 1 - mu0
    s = np.linspace(0, 1, 200001); env = np.sin(np.pi*s)**4
    mup = dmu*env**2/((35/128)*A["D"])
    muv = mu0 + np.concatenate([[0], np.cumsum((mup[1:] + mup[:-1])/2*np.diff(s*A["D"]))])
    return float((mup/(2*np.sqrt(muv))).max())


def compute():
    rows = grid(); md = _modes(rows); p = power(); cs = cases()
    top = [dict((round(x, 3), R) for x, R in zip(*md[k]))[round(k + 0.5, 3)] for k in range(K + 1)]
    m = {k: dict((round(x, 3), R) for x, R in zip(*md[k])) for k in md}
    drop = [m[k][round(k + 2.5, 3)]/m[k][round(k + 3.5, 3)] for k in range(1, K + 1)]
    slope0 = -np.log(m[0][6.0]/m[0][5.0])
    return dict(words=words(), pot=potential(), flux=max(abs(R + T - 1) for k, x, R, T in rows), n=len(rows),
                top=top, drop=drop, slope0=slope0, p=p, cs=cs, esc=escape(md, p, cs),
                lo=escape(md, p, cs, shift=-1), hi=escape(md, p, cs, shift=1), lamleast=lam_least(md, p, cs),
                growth=growth())


def checks(o):
    ch = {}
    ch["E0 words of 522"] = o["words"]
    ch["E1 V = f[((l+1)^2 - 1/4)/r^2 + 9 mu/(4 r^4)] from box Phi = 0; KI (5.2)-(5.3) at n = 3: k_T^2 + 2K = l(l+2)"] = (
        o["pot"]["exact"] and o["pot"]["ki"])
    t = o["top"]
    ch["E2 grid: 1681 points, R + T = 1 to 2e-9; R at the top 0.50-0.56 (k >= 1), 1/2 at k = 45 to 0.005"] = (
        o["n"] == 1681 and o["flux"] < 2e-9 and min(t[1:]) >= 0.5 and max(t[1:]) < 0.56 and abs(t[-1] - 0.5) < 0.005)
    d = o["drop"]
    ch["E2 above the top R falls 1e3-1e4 per unit of w r_h, more steeply with l; l = 0 far slope 2 pi to 0.1"] = (
        1e3 < min(d) and max(d) < 1e4 and d[-1] > d[0] and abs(o["slope0"] - 2*np.pi) < 0.1)
    p = o["p"]; r = p[1:]/p[:-1]; q = (1 + np.sqrt(2))**-2
    ch["E3 power: sum 1 to 1e-12; p0 0.7768, p1 0.2129; ratios alternate about (1 + sqrt 2)^(-2), to 1% at k = 45"] = (
        abs(p.sum() - 1) < 1e-12 and abs(p[0] - 0.7768) < 5e-5 and abs(p[1] - 0.2129) < 5e-5
        and all(r[i] > q > r[i + 1] for i in range(2, K - 1, 2)) and abs(r[-1]/q - 1) < 0.01
        and abs(r[-1] - q) < abs(r[3] - q))
    e = o["esc"]; c, x = e["copper"], e["example"]
    ch["E4 half a bit = 1/(3N) = emitter_process's bit_r/(2 E5) (copper, to 1e-8)"] = (
        abs(c["half"]/o["cs"]["copper"]["half_em"] - 1) < 1e-8)
    ch["E4 copper: least seed lets 1.53e7 half bits out; least seed for half a bit r_h0 17.95 l5, mu0 322 l5^2"] = (
        abs(c["nhalf"]/1.53e7 - 1) < 0.01 and abs(c["rh"] - 17.95) < 0.01 and abs(c["mu0"] - 322) < 1)
    ch["E4 example README: 1.97e5 half bits; r_h0 13.96 l5, mu0 195 l5^2"] = (
        abs(x["nhalf"]/1.97e5 - 1) < 0.01 and abs(x["rh"] - 13.96) < 0.01 and abs(x["mu0"] - 195) < 1)
    ch["E4 hf_core5's seeds: mu0 = 1000 l5^2 passes both, mu0 = 100 fails both; dr_h/dv <= 0.0110 on the shell"] = (
        c["ok"][1000.0] and x["ok"][1000.0] and not c["ok"][100.0] and not x["ok"][100.0]
        and abs(o["growth"] - 0.0110) < 0.0001)
    lo, hi = o["lo"], o["hi"]
    ch["E5 labels moved by one: least seed 16.29-19.60 l5 (copper), 12.25-15.67 l5 (example); the verdicts stand"] = (
        abs(lo["copper"]["rh"] - 16.29) < 0.01 and abs(hi["copper"]["rh"] - 19.60) < 0.01
        and abs(lo["example"]["rh"] - 12.25) < 0.01 and abs(hi["example"]["rh"] - 15.67) < 0.01
        and all(q[n]["ok"][1000.0] and not q[n]["ok"][100.0] for q in (lo, hi) for n in q)
        and all(q[n]["nhalf"] > 1e4 for q in (lo, hi) for n in q))
    ll = o["lamleast"]
    ch["E5 the record's least seed delivers within half a bit only for lam <= 1.95 l5 (copper), 2.52 l5 (example)"] = (
        abs(ll["copper"] - 1.948) < 0.002 and abs(ll["example"] - 2.523) < 0.002)
    return ch


def report(o=None):
    o = o or compute()
    for k_, v_ in checks(o).items():
        print("%-118s %s" % (k_[:118], "PASS" if v_ else "FAIL"))
    print("  E1 V = %s" % sp.factor(o["pot"]["V"]))
    print("  E2 %d points, max |R + T - 1| %.2g; R at the top k = 0..5: %s; drop per unit %.3g-%.3g; l = 0 slope %.4f"
          % (o["n"], o["flux"], [round(float(v), 3) for v in o["top"][:6]], min(o["drop"]), max(o["drop"]),
             o["slope0"]))
    p = o["p"]
    print("  E3 p0..p3 %s; p45/p44 %.4f against %.4f" % ([round(float(v), 5) for v in p[:4]], p[-1]/p[-2],
                                                          (1 + 2**0.5)**-2))
    for tag, q in (("E4", o["esc"]), ("E5 k-1", o["lo"]), ("E5 k+1", o["hi"])):
        for n_, d in q.items():
            print("  %-6s %-8s half %.3g; least seed escapes %.3g = %.3g half bits; least seed for half a bit"
                  " w r_h %.2f, r_h0 %.2f l5, mu0 %.0f l5^2; mu0 100 %s, 1000 %s"
                  % (tag, n_, d["half"], d["esc0"], d["nhalf"], d["x"], d["rh"], d["mu0"], d["ok"][100.0],
                     d["ok"][1000.0]))
    print("  E5 the least seed delivers for lam <= %s l5; dr_h/dv <= %.4f" % (
        {k: round(v, 3) for k, v in o["lamleast"].items()}, o["growth"]))


def selftest():
    c = checks(compute())
    n = sum(c.values())
    for k_, v_ in c.items():
        print("%-118s %s" % (k_[:118], "PASS" if v_ else "FAIL"))
    print("seed_escape.py: %d/%d" % (n, len(c)))
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
    if "--build-grid" in sys.argv:
        print("%d points" % len(build_grid()))
        sys.exit(0)
    if "--selftest" in sys.argv:
        sys.exit(0 if selftest() else 1)
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    report()
