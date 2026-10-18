#!/usr/bin/env python3
"""hf_anchor5.py -- item 514: THM-HF5's remaining estimate, anchored in our universe's values, its coefficients
evaluated.

M, 514: "Prove the remaining estimate please. Anchor you work with real value from our universe so you can calculate
what you need to evaluate the coefficients that are preventing a precise answer instead of an estimate".  The estimate
(L-UNIF', hf_theorem5 F7) says the vacuum solution stays within C lam of its approximant; what kept it an estimate was
C (and the order beyond it) left unevaluated, and lam left abstract.  Here both are made definite.  Labels: computed
(exact unless marked), READ (the record's values, by path), deduced, M's.

  A0 (M's) 514, verbatim.
  A1 (READ, by path) Our universe's values, as the record holds them: l5 = 1.54e-25 m and the example README's face,
     N = 2.74e15 bits, E5 = 1.28e9 J, r_h = 1.12e-20 m = 72,762 l5 (source_spec consts, energy_check); the record's
     least-spread shell, the sin^8 flux over D = 269.15 r_h (src_hole D_REC; sigma_t = 28.5 r_h, emitter_process C2);
     the least seed sqrt(72) l5^2 (src_hole S4, 508); the emitter's wavelength window, from 10 l5 (source_spec U3) to
     the r_h/10 the emitter names (emitter_process C4).
  A2 (computed, exact; checked against the sequence) The first-order coefficient.  The departure the runs measure, P,
     is the largest |F|, |G| -- the waves' amplitude rescaled by r^(3/2), which at leading order is carried unchanged
     along each ingoing cone (amplitude ~ area^(-1/2) = r^(-3/2) in five dimensions).  So P = sqrt(2) lam A max(env)
     (1 + O(lam)), the sqrt(2) being h(0).  The runs give P/lam = 1.406, 1.449 at lam = 0.025, 0.0125 (mu0/l5^2 =
     100) and 1.406 at 0.025 (1000): within 3 % of sqrt(2) = 1.414.  The strain on the metric itself is at most
     (2/3) lam A env r^(-3/2) (at the axes x = +-1, where h = 1).
  A3 (computed, exact; checked against the sequence) The second-order coefficient.  The scri flux with the data's
     exact rates, averaged over the phase, is (A^2/6)(env^2 + lam^2 env'^2) at every x (symbolic): the mass gained
     exceeds Vaidya's by (2/9) A^2 lam^2 int env'^2, exactly.  For env = sin^4 over T = 3 that is
     c2 = 5 pi^2/(36 T) = 0.45693.  The runs' mean-mass offset over lam^2: 0.4608, 0.4590, 0.4568 (100) and 0.459,
     0.4589 (1000, x = 20) -- converging on c2 to 0.01 %.  What is left after it is below 0.1 lam^3 at every
     lam <= 0.05 (0.074, 0.088, 0.005; 0.045, 0.077 in units of lam^3).
  A4 (computed) Anchored.  With A1's values (lengths in l5): the shell brings Delta mu = r_h^2 = 5.29e9 l5^2, so
     A = (16.457 Delta mu / D)^(1/2) = 66.7 l5^(1/2).  Then for waves of wavelength w (lam = w/2 pi):
     - the relative second-order mass offset is 0.5714 (w/D)^2: 1.5e-13 at w = 10 l5, 7.9e-8 at w = r_h/10;
     - the strain at the face's horizon at the end is (2/3) lam A r_h^(-3/2): 3.6e-6 at 10 l5, 2.6e-3 at r_h/10;
     - at the record's quantum boundary x = 1 (r_q = (sqrt72 mu l5^2)^(1/4) = 460 l5 at the end), 7.2e-3 at 10 l5 and
       5.2 at r_h/10;
     - the high-frequency condition is a wavelength below a tenth of the local curvature radius K^(-1/4) =
       r^2/(72^(1/4) sqrt(mu)); at x = 1 that radius is l5 for every hole (the definition of x), so no wave of a
       physical length is high-frequency there.  10 l5 waves are high-frequency from infinity down to r = 4,604 l5
       (x = 1e-4) and are a small perturbation (strain below a tenth) all the way to x = 1, for all of the shell's
       energy; they are high-frequency at the horizon for all but 1.6e-5 of it;
     - r_h/10 waves are neither: high-frequency only beyond r = 124,186 l5, outside the horizon (which needs
       w < r_h/(10 x 72^(1/4)) = 2,498 l5), and not small at x = 1 (strain 5.2).  The r_h/10 emitter_process C4 names
       is outside both.
     [Item 515 corrects the first version of A4, which took r_q in place of the curvature radius at x = 1 and so
     reported a band of 10-46 l5 reaching x = 1 at high frequency; at x = 1 the curvature radius is l5.]
  A5 (deduced) What this settles of L-UNIF'.  The coefficients the estimate left open are evaluated: the first order
     exactly (sqrt(2) A), the second order exactly (5 pi^2/(36 T) per A^2), both confirmed by the nonlinear runs, the
     remainder after them measured below 0.1 lam^3; and lam is our universe's, bounded below by the Planck scale (the
     window starts at 10 l5), so lam -> 0 is never needed: at w = 10 l5 the third-order term is ~1e-15 of the shell.
     It is not an analytic inequality for every lam: that the series stays asymptotic below the computed wavelengths
     is what the runs show at four of them, not a proof for all.

Imports source_spec.py, src_hole.py and hf_core5.py by path.  numpy, sympy, mpmath.
python3 hf_anchor5.py [--selftest | --mutants]
"""
import contextlib
import importlib.util
import io
import os
import sys

import numpy as np
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
RULINGS = os.path.join(HERE, "..", "M-RULINGS-2026-10-03.md")
MUT = set()


def _load(name, key):
    spec = importlib.util.spec_from_file_location(key, os.path.join(HERE, name))
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        spec.loader.exec_module(mod)
    return mod


def words():
    return ("Anchor you work with real value from our universe so you can calculate what you need to evaluate the "
            "coefficients" in open(RULINGS).read())


def a1():
    S = _load("source_spec.py", "an_source_spec")
    H = _load("src_hole.py", "an_src_hole")
    k = S.consts(); d = S.energy_check(k)
    return dict(l5=k["l5"], N=d["N"], E=d["E"], rh=d["rh"], rh_l5=d["rh"]/k["l5"], D=H.D_REC, seed=np.sqrt(72))


def a2_a3():
    """the first- and second-order coefficients, exact, and the runs' measured ones"""
    x, A, lam, ph, e, ep = sp.symbols("x A lambda phi e ep", real=True)
    c2_, s2_ = (1 + x)/2, (1 - x)/2
    h = sp.sqrt(2/(1 + x**2))
    eps_term = 0 if "no_lam2" in MUT else lam*A*ep*h
    Fv = eps_term*sp.sin(ph) + A*e*h*sp.cos(ph)
    Gv = eps_term*sp.cos(ph) - A*e*h*sp.sin(ph)
    q1, q2 = (2*c2_*Gv - s2_*Fv)/3, (2*s2_*Fv - c2_*Gv)/3
    avg = sp.factor(sp.simplify(sp.integrate(sp.expand(q1**2 + q1*q2 + q2**2), (ph, 0, 2*sp.pi))/(2*sp.pi)))
    exact_avg = sp.simplify(avg - A**2*(e**2 + lam**2*ep**2)/6) == 0
    # int env'^2 for env = sin^4(pi (v - v1)/T): 16 (pi/T)^2 T int_0^1 sin^6 cos^2 = (5 pi^2/8)/T
    u = sp.Symbol("u")
    I62 = sp.integrate(sp.sin(sp.pi*u)**6*sp.cos(sp.pi*u)**2, (u, 0, 1))
    T = sp.Integer(3)
    c2 = sp.nsimplify(sp.Rational(2, 9)*16*sp.pi**2/T*I62)
    hmax = sp.sqrt(2) if "unit_h" not in MUT else sp.Integer(1)
    C = _load("hf_core5.py", "an_hf_core5")
    st = C.stats()
    rows = {}
    for cfg in C.RUNLIST:
        kk = C.key(cfg)
        if kk in st and cfg[2] == 1.0:
            rows[(cfg[0], cfg[1], cfg[3], cfg[4])] = st[kk]
    seqs = {100: [(0.1, 20, 16), (0.05, 24, 16), (0.025, 28, 16), (0.0125, 32, 16)],
            1000: [(0.05, 28, 20), (0.025, 36, 20)]}
    meas = {}
    for L, s in seqs.items():
        meas[L] = [(lam_, rows[(L, lam_, ny, nx)]["P"]/lam_, rows[(L, lam_, ny, nx)]["offset"]/lam_**2,
                    abs(rows[(L, lam_, ny, nx)]["offset"] - float(c2)*lam_**2)/lam_**3)
                   for lam_, ny, nx in s if (L, lam_, ny, nx) in rows]
    return dict(avg=avg, exact_avg=exact_avg, c2=c2, c2f=float(c2), c1=float(hmax), meas=meas)


def a4(R, c2f):
    """our universe's shell: amplitude; strains at the horizon and at x = 1; where the waves are high-frequency (shorter
    than a tenth of the local curvature radius K^(-1/4) = r^2/(72^(1/4) sqrt(mu)), which is l5 at x = 1 for every hole)
    and where they are a small perturbation (strain below a tenth)"""
    rh, D_rh, seed = R["rh_l5"], R["D"], R["seed"]
    D = D_rh*rh                                              # duration in l5
    dmu = rh**2 - seed
    S8 = 35/128
    A = np.sqrt(9*dmu/(2*D*S8))
    v = np.linspace(0, D, 400001)
    env = np.sin(np.pi*v/D)**4
    flux = (2/9)*A**2*env**2
    mu = seed + np.concatenate([[0], np.cumsum((flux[1:] + flux[:-1])/2*np.diff(v))])
    c4 = 72**0.25
    rq_end = (np.sqrt(72)*rh**2)**0.25
    curv_q = rq_end**2/(c4*rh)                               # K^(-1/4) at x = 1: l5, by the definition of x
    share = lambda m: float(np.sum(flux[:-1][m[:-1]]*np.diff(v)[m[:-1]])/np.sum(flux[:-1]*np.diff(v))) if m.any() else 0.0
    out = dict(A=A, D=D, dmu=dmu, mu_end=mu[-1], curv_q=curv_q, w_max_h=0.1*rh/c4)
    for name, w in (("10 l5", 10.0), ("r_h/10", rh/10)):
        lam = w/(2*np.pi)
        rq = (np.sqrt(72)*mu)**0.25
        s_h = (2/3)*lam*A*env*mu**-0.75
        s_q = (2/3)*lam*A*env*rq**-1.5
        hf_h = (w < 0.1*np.sqrt(mu)/c4) & (s_h < 0.1)
        small_q = s_q < 0.1
        r_hf = np.sqrt(10*w*c4*rh)                          # deepest radius, at the end, where w < K^(-1/4)/10
        out[name] = dict(lam=lam, rel_offset=(5*np.pi**2/8/D)*(2/9)*A**2*lam**2/dmu,
                         strain_h_end=(2/3)*lam*A*rh**-1.5, strain_q_end=(2/3)*lam*A*rq_end**-1.5, rq_end=rq_end,
                         r_hf=r_hf, x_hf=(rq_end/r_hf)**4, hf_at_q=w < 0.1*curv_q,
                         share_h=share(hf_h), share_q_small=share(small_q))
    return out


def compute():
    R = a1(); c = a2_a3()
    return dict(words=words(), a1=R, c=c, a4=a4(R, c["c2f"]))


def checks(o):
    ch = {}
    ch["A0 words of 514"] = o["words"]
    R = o["a1"]
    ch["A1 our universe's values, as the record holds them"] = (
        abs(R["rh_l5"] - 72762) < 1 and R["N"] > 1e15 and abs(R["D"] - 269.15) < 0.01 and abs(R["l5"] - 1.539e-25) < 1e-28)
    c = o["c"]
    a = c["meas"]
    ch["A2 the first order: P/lam -> sqrt(2) A, within 3 % at lam <= 0.025"] = all(
        abs(p/c["c1"] - 1) < 0.03 for L in a for lam_, p, _, _ in a[L] if lam_ <= 0.025)
    ch["A3 the second order: mass offset/lam^2 -> 5 pi^2/(36 T) = 0.45693, within 1 % at lam <= 0.05; rest < 0.1 lam^3"] = (
        c["exact_avg"] and abs(c["c2f"] - 0.45693) < 1e-4
        and all(abs(off/c["c2f"] - 1) < 0.01 and res < 0.1 for L in a for lam_, _, off, res in a[L] if lam_ <= 0.05))
    b = o["a4"]
    ch["A4 anchored: x = 1's curvature radius is l5; 10 l5 waves are high-frequency to x ~ 1e-4 and small at x = 1; "
       "r_h/10 waves are neither"] = (
        abs(b["curv_q"] - 1) < 1e-9 and not b["10 l5"]["hf_at_q"] and b["10 l5"]["strain_q_end"] < 0.01
        and b["10 l5"]["share_h"] > 0.9999 and b["10 l5"]["share_q_small"] > 0.95 and b["10 l5"]["rel_offset"] < 1e-12
        and b["10 l5"]["r_hf"] > b["10 l5"]["rq_end"] and b["r_h/10"]["strain_q_end"] > 1
        and rh_over_10_not_hf(b))
    return ch


def rh_over_10_not_hf(b):
    return b["r_h/10"]["share_h"] == 0.0 and b["r_h/10"]["share_q_small"] < 0.01


def report(o=None):
    o = o or compute()
    for k, v in checks(o).items():
        print("%-112s %s" % (k, "PASS" if v else "FAIL"))
    R = o["a1"]
    print("  A1 l5 = %.4e m; N = %.4g bits; E5 = %.4g J; r_h = %.4e m = %.0f l5; D = %.2f r_h; seed sqrt72 l5^2" % (
        R["l5"], R["N"], R["E"], R["rh"], R["rh_l5"], R["D"]))
    c = o["c"]
    print("  A3 phase average: %s; c2 = %s = %.5f" % (c["avg"], c["c2"], c["c2f"]))
    for L, rows in c["meas"].items():
        print("  A2/A3 mu0/l5^2 = %d: " % L + "; ".join("lam %g: P/lam %.3f, offset/lam^2 %.4f, rest/lam^3 %.3f" % r for r in rows))
    b = o["a4"]
    print("  A4 A = %.2f l5^1/2, D = %.4g l5, Delta mu = %.4g l5^2; curvature radius at x = 1: %.3g l5; high-frequency at "
          "the horizon needs w < %.0f l5" % (b["A"], b["D"], b["dmu"], b["curv_q"], b["w_max_h"]))
    for name in ("10 l5", "r_h/10"):
        z = b[name]
        print("     w = %-7s lam %.4g: relative 2nd-order offset %.2e; strain at the horizon %.2e, at x = 1 (r_q %.0f l5) "
              "%.2e; high-frequency down to r = %.0f l5 (x = %.1e); energy share high-frequency at the horizon %.7f, "
              "small at x = 1 %.4f" % (name, z["lam"], z["rel_offset"], z["strain_h_end"], z["rq_end"], z["strain_q_end"],
                                       z["r_hf"], z["x_hf"], z["share_h"], z["share_q_small"]))
    return o


MUTANTS = {"no_lam2": "the data's lam env' term dropped: no second-order offset (A3)",
           "unit_h": "h's maximum taken as 1, not sqrt(2) (A2)"}


def selftest():
    o = compute(); c = checks(o); report(o)
    print("%s: %d/%d" % (os.path.basename(__file__), sum(c.values()), len(c)))
    return all(c.values())


def mutants():
    caught = 0
    for m_, desc in MUTANTS.items():
        MUT.clear(); MUT.add(m_)
        try:
            c = checks(compute()); failed = [k for k, v in c.items() if not v]
        except Exception as ex:
            failed = ["raised %s" % type(ex).__name__]
        caught += bool(failed)
        print("mutant %-10s %s  (%s)  failing: %s" % (m_, "caught" if failed else "MISSED", desc, "; ".join(failed)))
    MUT.clear()
    print("mutants: %d/%d" % (caught, len(MUTANTS)))
    return caught == len(MUTANTS)


if __name__ == "__main__":
    if "--mutants" in sys.argv:
        sys.exit(0 if mutants() else 1)
    sys.exit(0 if selftest() else 1)
