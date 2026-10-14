#!/usr/bin/env python3
r"""
DOCKET 67 -- audit of gr-qc/9701064#not-af: HPS p.8, "The redshift function
however, does not approach a constant value as l -> infinity, so the metric as
a whole is not asymptotically flat", as hpscentre.py:99-101 uses it.

Source text: HPS arXiv v1 text layer, d67/src/hps/hps_0.xml, p.8
("F(l) ~ (a ln l - b)^2 for a = 5.3 and b = 25.5", "R(l) -> l").

PART A (sympy, exact):
  A1  F = (a ln l - b)^2 diverges for every a != 0; a = 0 is the only member of
      the family with f -> const.  No rescaling t -> lam t (f -> lam^2 f) makes
      f -> 1.
  A2  Smooth part (r = l, f = F): G^t_t = 0 = G^th_th, G^l_l = 2a/(l^2 u),
      u = a ln l - b; the Bianchi (conservation) identity closes.
  A3  Komar integral of the static Killing field, proper-length gauge,
      M_K(l) = r^2 f'/(2 sqrt f): = a l on the smooth part (diverges, for every
      normalisation of t); control: Schwarzschild gives M_K = M.
  A4  The AHS source (conserved reading, tree's transcription, imported from a
      scratch COPY whose md5 is asserted) on the smooth part alone is smaller
      than G^l_l by a factor that -> 0: the smooth law is not a self-consistent
      solution by itself; the growth of F is carried by the ripple averages.
      (Recorded: HPS's form is numerics-guided, as HPS say.)
PART B (numeric, the tree's system from a COPY; no byte-code written):
  eq. (9) data, ln f(0) = -2/3, both readings (conserved; printed-M1), to X K:
  window-averaged sqrt f, Komar M_K / l, max |2m/r| and r/l per decade.
Exit 0 iff every asserted check passes.
"""
import hashlib
import math
import os
import sys
import time

sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__))
COPY = os.path.join(HERE, "_hps_tree")
LIVE = "/home/user/Claude-Method-Works/research/warp-drive"
FAILS = []


def check(ok, label, detail=""):
    print(("PASS " if ok else "FAIL ") + label + (("  " + str(detail)) if detail else ""))
    if not ok:
        FAILS.append(label)


def md5(p):
    return hashlib.md5(open(p, "rb").read()).hexdigest()


def part_a():
    import sympy as sp
    print("PART A -- closed form (sympy)")
    l = sp.Symbol('l', positive=True)
    a, b, lam, M = sp.symbols('a b lam M', positive=True)
    A, B = sp.Rational(53, 10), sp.Rational(51, 2)
    u = A*sp.log(l) - B
    F = u**2
    lim = sp.limit(F, l, sp.oo)
    check(lim == sp.oo, "A1a HPS law F=(5.3 ln l - 25.5)^2 -> oo", lim)
    check(sp.limit(lam**2*F, l, sp.oo) == sp.oo, "A1b lam^2 F -> oo for every lam > 0")
    ag = sp.Symbol('ag', nonzero=True, real=True)
    Fg = (ag*sp.log(l) - b)**2
    check(sp.limit(Fg, l, sp.oo) == sp.oo, "A1c (a ln l - b)^2 -> oo for every a != 0")
    check(sp.simplify(Fg.subs(ag, 0)) == b**2, "A1d a = 0 is the only f -> const member (b^2)")
    l0 = math.exp(float(B/A))
    print("     zero of the law l0 = exp(b/a) = %.3f; 3 ln F + 4 > 0 needs |u| > e^{-2/3} = %.4f"
          % (l0, math.exp(-2/3)))
    lo, hi = math.exp((float(B) - math.exp(-2/3))/float(A)), math.exp((float(B) + math.exp(-2/3))/float(A))
    print("     omega_2^2 = 1/(16K^2(4 + 3 ln F)) is singular / imaginary on l in (%.2f, %.2f): the law is a"
          " large-l form only" % (lo, hi))

    # A2 -- Einstein tensor of the smooth part, HPS's own G components (p.4)
    uu = a*sp.log(l) - b
    f = uu**2
    r = l
    f1, f2 = sp.diff(f, l), sp.diff(f, l, 2)
    r1, r2 = sp.diff(r, l), sp.diff(r, l, 2)
    Gtt = sp.simplify(2*r2/r + r1**2/r**2 - 1/r**2)
    Gll = sp.simplify(f1*r1/(f*r) + r1**2/r**2 - 1/r**2)
    Gth = sp.simplify(f2/(2*f) + r2/r + f1*r1/(2*f*r) - f1**2/(4*f**2))
    check(Gtt == 0, "A2a G^t_t = 0 on (r = l, f = F)")
    check(Gth == 0, "A2b G^th_th = 0 on (r = l, f = F)")
    check(sp.simplify(Gll - 2*a/(l**2*uu)) == 0, "A2c G^l_l = 2a/(l^2 (a ln l - b))", Gll)
    div = sp.simplify(sp.diff(Gll, l) + f1/(2*f)*(Gll - Gtt) + 2*r1/r*(Gll - Gth))
    check(div == 0, "A2d conservation identity closes on the smooth part", div)

    # A3 -- Komar integral
    MK = sp.simplify(r**2*f1/(2*sp.sqrt(f)))
    MKu = sp.simplify(MK.subs(sp.sqrt(uu**2), uu))
    MK_pos = sp.simplify((r**2*f1/(2*uu)))  # sqrt f = u on u > 0
    check(sp.simplify(MK_pos - a*l) == 0, "A3a Komar M_K = r^2 f'/(2 sqrt f) = a l on the smooth part (u > 0)")
    check(sp.limit(lam*a*l, l, sp.oo) == sp.oo, "A3b t -> lam t scales M_K by lam: diverges for every normalisation")
    rr = sp.Symbol('rr', positive=True)
    fs = 1 - 2*M/rr
    # proper length: dl = dr/sqrt(fs) -> d/dl = sqrt(fs) d/dr
    MKs = sp.simplify(rr**2*sp.sqrt(fs)*sp.diff(fs, rr)/(2*sp.sqrt(fs)))
    check(sp.simplify(MKs - M) == 0, "A3c control: Schwarzschild M_K = M (finite)", MKs)
    del MKu
    return sp


def part_a4(sp):
    print("A4 -- AHS source (conserved reading) on the smooth part alone, tree transcription from COPY")
    sys.path.insert(0, COPY)
    sys.path.append(LIVE)      # throatmass's seated imports (achievable, ...), read only; no byte-code
    import hpscentre as H
    S = H.build(sp)
    T = H.source(sp, S, H.CONSERVED)
    l = S['l']
    A, B = sp.Rational(53, 10), sp.Rational(51, 2)
    fsm = (A*sp.log(l) - B)**2
    rep = {}
    for k in range(4, -1, -1):
        rep[sp.diff(S['fF'], l, k)] = sp.diff(fsm, l, k)
        rep[sp.diff(S['rF'], l, k)] = sp.diff(l, l, k)
    Tll = T[1].subs(rep)
    Gll = S['G'][1].subs(rep)
    rows = []
    for x in (1e3, 1e4, 1e5):
        g = float(Gll.subs(l, x))
        t = float(Tll.subs(l, x))
        rows.append((x, g, t, abs(t/g)))
        print("     l = %.0e K:  G^l_l = %.4e   8pi T^l_l (K=1) = %.4e   |T/G| = %.3e" % (x, g, t, abs(t/g)))
    check(all(r_[3] < 1e-3 for r_ in rows) and rows[0][3] > rows[1][3] > rows[2][3],
          "A4 smooth-part AHS source << G^l_l and falling: the law is not self-consistent without the ripples")
    return H


def part_b(sp, H, X):
    import numpy as np
    print("PART B -- the tree's integrations from the COPY, eq. (9) data, to x = %g K" % X)
    L0 = sp.Rational(-2, 3)
    y0 = [math.exp(float(L0)), 0, 0, 0, float(sp.sqrt(-16*L0)), 0, 0, 0]
    out = {}
    for name, reading in (("conserved", H.CONSERVED), ("printed-M1", H.PRINTED_M1)):
        t0 = time.time()
        num = H.numeric_system(sp, reading)
        res = H.integrate(num, y0, 0, X, rtol=1e-10)
        print("     %-10s status %d end %.1f K (%.0f s)" % (name, res.status, res.t[-1], time.time() - t0))
        check(res.status == 0 and res.t[-1] >= X*(1 - 1e-9), "B0 %s reached x = %g K" % (name, X))
        W = 100.0     # averaging window, K: > 25 ripple periods of omega_1
        # every window lies INSIDE the integrated range (dense output never extrapolated)
        pts = [x for x in (300, 1000, 3000, 10000, 30000, 99000) if x + W/2 <= X]
        rows = []
        for x in pts:
            xs = np.linspace(x - W/2, x + W/2, 20001)
            Y = res.sol(xs)
            f, f1, r, r1 = Y[0], Y[1], Y[4], Y[5]
            sq = float(np.mean(np.sqrt(f)))
            mk = float(np.mean(r**2*f1/(2*np.sqrt(f))))
            twomr = float(np.max(np.abs(1 - r1**2)))
            rl = float(np.mean(r/xs))
            rows.append((x, sq, mk/x, twomr, rl, float(f.min()), float(f.max())))
            print("       x = %6.0f K  <sqrt f> = %8.4f  <M_K>/x = %7.4f  max|2m/r| = %.3e  <r/x> = %.5f"
                  % (x, sq, mk/x, twomr, rl))
        sqs = [r_[1] for r_ in rows]
        check(all(s2 > s1 for s1, s2 in zip(sqs, sqs[1:])), "B1 %s: <sqrt f> strictly increasing over %s K"
              % (name, pts))
        check(sqs[-1] / sqs[0] > 2, "B2 %s: <sqrt f> grows by > 2x across the range" % name,
              "%.3f -> %.3f" % (sqs[0], sqs[-1]))
        mks = [r_[2] for r_ in rows]
        # A FINITE Komar mass M would give <M_K>/x = M/x, falling by pts[-1]/pts[0]
        # (330x over 300..99000 K).  Criterion (revised after a 3100 K test run, where the
        # first criterion "M_K/x monotone non-decreasing" failed on ripple scatter):
        # <M_K>/x positive at every point and within a factor 3 across the range.
        check(min(mks) > 0 and max(mks)/min(mks) < 3,
              "B3 %s: <M_K>/x positive and flat within 3x (finite Komar mass would fall %.0fx)"
              % (name, pts[-1]/pts[0]), ["%.3f" % v for v in mks])
        tm = [r_[3] for r_ in rows]
        print("       max|2m/r| per point: %s (the SPATIAL ripples: recorded, not graded here)"
              % ["%.2e" % v for v in tm])
        out[name] = rows
    return out


def main():
    X = float(sys.argv[1]) if len(sys.argv) > 1 else 1e5
    t0 = time.time()
    for fn in ("hpscentre.py", "throatmass.py", "qeihps.py"):
        a_, b_ = md5(os.path.join(COPY, fn)), md5(os.path.join(LIVE, fn))
        check(a_ == b_, "C0 copy md5 == live %s" % fn, a_)
    sp = part_a()
    H = part_a4(sp)
    part_b(sp, H, X)
    print("elapsed %.0f s" % (time.time() - t0))
    print("SUMMARY: %s" % ("ALL PASS" if not FAILS else "FAILS: %s" % FAILS))
    return 1 if FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
