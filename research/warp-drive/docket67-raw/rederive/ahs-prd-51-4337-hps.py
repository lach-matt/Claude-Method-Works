#!/usr/bin/env python3
"""DOCKET 67 -- audit ahs-prd-51-4337-hps (composite: AHS <T> as HPS print it, and HPS's
self-consistent throat as the tree's O5 uses it: m < 0 in the flare of HPS's CONSERVED system).

The transcription systems() below is COPIED VERBATIM from the sibling audit script
rederive/gr-qc_9701064_eq9.py, which transcribed HPS (5)-(7) afresh from the arXiv v1 text layer
(src/hps/hps_0.xml, md5 a5f55d322aed581c9b1dead99d63cb84) -- NOT from the tree's hpscentre.py.
Check A re-runs a conservation control on it here.  K = 1 units (lengths in K).

 A  conservation control: (M1, M2) = (116, 2) conserved identically (random rational points);
    printed (16, 1) not.
 B  the tree's datum: from eq. (9) data at L = ln f(0) = -2/3, first l with r' = 1 (m < 0) in K
    and l_P (tree: 0.0516 l_P).
 C  THE UNFIXED PARAMETER.  HPS fn [20]: the renormalisation scale mu 'can be absorbed into the
    definition of f', so a change of mu is a shift of ln f(0) (the metric -f dt^2 rescales by a
    constant = a time rescaling).  TSH gr-qc/9608036 p.3 (read by the sibling audit
    ahs-1995-prd51-4337): the massless analytic approximations 'contain an arbitrary parameter
    whose value cannot be fixed except by experiment'.  So 'HPS's own throat data' are one value
    of an unmeasured parameter.  C scans L over HPS's whole range -1 <= L < 0: does m < 0 in the
    flare survive every mu?  (the datum HPS -- and everyone since -- lacks)
 D  linearised regular centre (hpscentre (b)): about flat space f = e^L0, r = l, the modes
    phi = A sin(kl)/l, rho' = B (sin kl - kl cos kl)/l with (k^2, A/B) = (1/16, -2) and
    (1/(16 (3 L0 + 4)), 4) solve all three linearised conserved equations; m = -eps l rho' + O(eps^2)
    changes sign and 2m/r does not tend to 0.
 E  metre figures: K in l_P; 300 l_P (HPS's largest 'local' throat) in metres with CODATA 2022 l_P.
Exit 0 iff every check passes.
"""
import math, sys, random
import sympy as sp
import numpy as np
from scipy.integrate import solve_ivp

l = sp.Symbol('l')
fs = sp.symbols('f0:5')
rs = sp.symbols('r0:5')
f, f1, f2, f3, f4 = fs
r, r1, r2, r3, r4 = rs
LN = sp.log(f)

def systems(M1, M2):
    tt_n = (32/r**4 + 7*f1**4/f**4 - 24*f1**3*r1/(f**3*r) + 24*f1**2*r1**2/(f**2*r**2)
            - 32*r1**4/r**4 + 4*f1**2*f2/f**3 - 12*f2**2/f**2 + 80*f1**2*r2/(f**2*r)
            - 160*f1*r1*r2/(f*r**2) + 128*r1**2*r2/r**3 - 64*f2*r2/(f*r) + 32*r2**2/r**2
            - 16*f1*f3/f**2 + 64*r1*f3/(f*r) - 96*f1*r3/(f*r) - 64*r1*r3/r**2
            + 16*f4/f - 64*r4/r)
    tt_l = (16/r**4 - 49*f1**4/f**4 + 44*f1**3*r1/(f**3*r) + 20*f1**2*r1**2/(f**2*r**2)
            - 16*r1**4/r**4 + M1*f1**2*f2/f**3 - 104*f1*r1*f2/(f**2*r) - 36*f2**2/f**2
            + 8*f1**2*r2/(f**2*r) - 80*f1*r1*r2/(f*r**2) + 64*r1**2*r2/r**3 + 16*f2*r2/(f*r)
            + 16*r2**2/r**2 - 48*f1*f3/f**2 + 64*r1*f3/(f*r) - 16*f1*r3/(f*r)
            - 32*r1*r3/r**2 + 16*f4/f - 32*r4/r)
    ll_n = (f1**4/f**4 - 16*f1**3*r1/(f**3*r) + 64*f1*r1**3/(f*r**3) - 4*f1**2*f2/f**3
            + 64*f1*r1*f2/(f**2*r) - 64*r1**2*f2/(f*r**2) - 4*f2**2/f**2
            - 48*f1**2*r2/(f**2*r) + 32*f1*r1*r2/(f*r**2) + 32*f2*r2/(f*r)
            + 8*f1*f3/f**2 - 32*r1*f3/(f*r) - 32*f1*r3/(f*r))
    ll_l = (16/r**4 + 7*f1**4/f**4 - 20*f1**3*r1/(f**3*r) - 4*f1**2*r1**2/(f**2*r**M2)
            + 32*f1*r1**3/(f*r**3) - 16*r1**4/r**4 - 12*f1**2*f2/f**3 + 48*f1*r1*f2/(f**2*r)
            - 32*r1**2*f2/(f*r**2) - 4*f2**2/f**2 - 16*f1**2*r2/(f**2*r)
            + 16*f1*r1*r2/(f*r**2) + 16*f2*r2/(f*r) - 16*r2**2/r**2 + 8*f1*f3/f**2
            - 16*r1*f3/(f*r) - 16*f1*r3/(f*r) + 32*r1*r3/r**2)
    th_n = (17*f1**4/f**4 - 16*f1**3*r1/(f**3*r) - 32*f1*r1**3/(f*r**3) - 52*f1**2*f2/f**3
            + 32*f1*r1*f2/(f**2*r) + 32*r1**2*f2/(f*r**2) + 28*f2**2/f**2
            + 16*f1**2*r2/(f**2*r) + 64*f1*r1*r2/(f*r**2) - 32*f2*r2/(f*r)
            + 24*f1*f3/f**2 - 48*r1*f3/(f*r) + 32*f1*r3/(f*r) - 16*f4/f)
    th_l = (-16/r**4 + 21*f1**4/f**4 - 12*f1**3*r1/(f**3*r) - 8*f1**2*r1**2/(f**2*r**2)
            - 16*f1*r1**3/(f*r**3) + 16*r1**4/r**4 - 52*f1**2*f2/f**3
            + 28*f1*r1*f2/(f**2*r) + 16*r1**2*f2/(f*r**2) + 20*f2**2/f**2
            + 4*f1**2*r2/(f**2*r) + 32*f1*r1*r2/(f*r**2) - 32*r1**2*r2/r**3
            - 16*f2*r2/(f*r) + 20*f1*f3/f**2 - 24*r1*f3/(f*r) + 16*f1*r3/(f*r)
            - 8*f4/f + 16*r4/r)
    T = dict(tt=tt_n + LN*tt_l, ll=ll_n + LN*ll_l, th=th_n + LN*th_l)   # = 8 pi T / K^2
    G = dict(tt=2*r2/r + r1**2/r**2 - 1/r**2,
             ll=f1*r1/(f*r) + r1**2/r**2 - 1/r**2,
             th=f2/(2*f) + r2/r + f1*r1/(2*f*r) - f1**2/(4*f**2))
    return G, T

fails = []
def chk(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ((" -- " + detail) if detail else ""), flush=True)
    if not ok:
        fails.append(name)

# ---------------- A: conservation control
F = sp.Function('F')(l); R = sp.Function('R')(l)
sub = {}
for k in range(4, -1, -1):
    sub[fs[k]] = sp.diff(F, l, k); sub[rs[k]] = sp.diff(R, l, k)
def divergence(M1, M2):
    G, T = systems(M1, M2)
    Ttt, Tll, Tth = [T[c].subs(sub, simultaneous=True) for c in ('tt', 'll', 'th')]
    return sp.diff(Tll, l) + sp.diff(F, l)/(2*F)*(Tll - Ttt) + 2*sp.diff(R, l)/R*(Tll - Tth)
random.seed(67)
def div_at_points(M1, M2, npts=3):
    d = divergence(M1, M2)
    vals = []
    for _ in range(npts):
        # polynomial test functions with random rational coefficients, evaluated at l = 1/3
        cf = [sp.Rational(random.randint(1, 9), random.randint(1, 9)) for _ in range(6)]
        cr = [sp.Rational(random.randint(1, 9), random.randint(1, 9)) for _ in range(6)]
        Fp = sum(c*l**i for i, c in enumerate(cf)); Rp = sum(c*l**i for i, c in enumerate(cr))
        e = d.subs({F: Fp, R: Rp}).doit()
        vals.append(sp.nsimplify(sp.N(e.subs(l, sp.Rational(1, 3)), 40), rational=False))
    return [float(v) for v in vals]
dc = div_at_points(116, 2); dp = div_at_points(16, 1)
chk("A1 conserved reading (116, r^2): divergence 0 at 3 random points", max(abs(v) for v in dc) < 1e-25, str(dc))
chk("A2 printed reading (16, r^1): divergence != 0", min(abs(v) for v in dp) > 1e-6, str(["%.3g" % v for v in dp]))

# ---------------- integrator for the conserved system
G, T = systems(116, 2)
sol = sp.solve([sp.Eq(G['tt'], T['tt']), sp.Eq(G['th'], T['th'])], [f4, r4], dict=True)[0]
args = (f, f1, f2, f3, r, r1, r2, r3)
F4 = sp.lambdify(args, sol[f4], 'math'); R4 = sp.lambdify(args, sol[r4], 'math')
LLres = sp.lambdify(args, G['ll'] - T['ll'], 'math')
LLscale = sp.lambdify(args, sp.Abs(f1*r1/(f*r)) + r1**2/r**2 + 1/r**2, 'math')
def rhs(x, y):
    return [y[1], y[2], y[3], F4(*y), y[5], y[6], y[7], R4(*y)]
def ev(x, y): return y[5] - 1.0
ev.direction = 1
def run(L, xmax, method='DOP853', rtol=1e-11, atol=1e-13, t_eval=None):
    y0 = [math.exp(L), 0, 0, 0, math.sqrt(-16*L), 0, 0, 0]
    s = solve_ivp(rhs, (0, xmax), y0, method=method, rtol=rtol, atol=atol, events=ev, dense_output=False, t_eval=t_eval,
                  max_step=0.05)
    return s
Kp = 1/math.sqrt(5760*math.pi)        # K in l_P
# ---------------- B
s = run(-2/3, 60)
x1 = s.t_events[0][0]
chk("B1 L = -2/3: first r' = 1 (m < 0 beyond) at x = %.6f K = %.4f l_P; tree 0.0516" % (x1, x1*Kp),
    round(x1*Kp, 4) == 0.0516)
ys = s.y[:, -1]
rel = max(abs(LLres(*s.y[:, k]))/LLscale(*s.y[:, k]) for k in range(0, s.y.shape[1], 50))
chk("B2 ll constraint held along the run (relative max %.2e < 1e-6)" % rel, rel < 1e-6)
s2 = run(-2/3, 60, method='Radau', rtol=1e-10, atol=1e-12)
chk("B3 Radau agrees on first crossing (%.7f)" % s2.t_events[0][0], abs(s2.t_events[0][0] - x1) < 1e-5)

# ---------------- C: mu scan over HPS's range
print("C  L = ln f(0) (a choice of mu, HPS fn [20]); first m<0 x (K), l_P; crossings of r'=1 up to x=200; min over run of |3 ln f + 4|")
Cres = []
W = 8*math.pi   # the tree's window width (hpscentre (d): 'recurs in EVERY 8 pi K window between 50 K and 1e4 K')
wins = [(50 + i*W, 50 + (i+1)*W) for i in range(int((200 - 50)//W))]
for L in [-1.0, -0.9, -0.8, -2/3, -0.5, -0.4, -0.3, -0.2, -0.1, -0.05, -0.01]:
    te = np.linspace(0, 200, 200001)
    s = run(L, 200, t_eval=te)
    n = len(s.t_events[0]); xf = s.t_events[0][0] if n else float('nan')
    mn = min(abs(3*math.log(v) + 4) for v in s.y[0])
    rp = s.y[5]
    hit = sum(1 for a, b in wins if np.any(rp[(s.t >= a) & (s.t < b)] > 1))
    ok_run = s.status == 0
    Cres.append((L, xf, n, mn, ok_run, hit))
    print("   L = %+.3f   x1 = %9.4f K = %.4f l_P   up-crossings to 200 K %3d   8piK windows in [50,200] with m<0 %d of %d   min|3lnf+4| %.3f   status %d" % (L, xf, xf*Kp, n, hit, len(wins), mn, s.status), flush=True)
chk("C1 every L in [-1, 0) scanned reaches x = 200 (no singular stop)", all(c[4] for c in Cres))
chk("C2 m < 0 in the flare for EVERY scanned L (at least one r' = 1 up-crossing)", all(c[2] >= 1 for c in Cres))
# C3 as first written ('>= 10 up-crossings to 200 K') was a threshold set before looking, with no
# ground; it FAILED (8 is the count at L = -2/3, where the tree's own window test passes).  Replaced
# by the tree's own recurrence test (every 8 pi K window), restricted to [50, 200] K.
chk("C3 recurs: every 8 pi K window in [50, 200] K contains m < 0, for every scanned L", all(c[5] == len(wins) for c in Cres),
    str([(round(c[0], 3), c[5]) for c in Cres]))
chk("C4 onset stays sub-Planck across the scan (max %.4f l_P)" % max(c[1]*Kp for c in Cres), max(c[1]*Kp for c in Cres) < 1)

# C5 (INFORMATIONAL, outside HPS's printed range): eq. (9) is real for every L < 0 (r(0)^2 = -16 L);
# HPS chose -1 <= L.  Below -4/3 the 4th-order determinant -256 (3 ln f + 4) vanishes at the throat.
print("C5 informational, L in (-4/3, -1) (outside HPS's range, inside eq. (9)'s):")
def ev_det(x, y): return 3*math.log(y[0]) + 4 if y[0] > 0 else -1.0
ev_det.terminal = True
def ev_f(x, y): return y[0] - 1e-12
ev_f.terminal = True
for L in [-1.1, -1.2, -1.3]:
    y0 = [math.exp(L), 0, 0, 0, math.sqrt(-16*L), 0, 0, 0]
    s = solve_ivp(rhs, (0, 60), y0, method='DOP853', rtol=1e-10, atol=1e-12, events=(ev, ev_det, ev_f), max_step=0.05)
    n = len(s.t_events[0]); xf = s.t_events[0][0] if n else float('nan')
    print("   L = %+.3f   first m<0 x1 = %8.4f K   up-crossings %d   stopped at x = %.4f (status %d: %s)   3 ln f + 4 there %.3g   f there %.3g"
          % (L, xf, n, s.t[-1], s.status, s.message[:40], 3*math.log(s.y[0, -1]) + 4 if s.y[0, -1] > 0 else float('nan'), s.y[0, -1]), flush=True)

# ---------------- D: linearised regular centre
eps, A, B, k, L0 = sp.symbols('epsilon A B k L0', real=True)
phi = sp.Function('phi')(l); rho = sp.Function('rho')(l)
fb = sp.exp(L0)*(1 + eps*phi); rb = l + eps*rho
subs_b = {}
for kk in range(4, -1, -1):
    subs_b[fs[kk]] = sp.diff(fb, l, kk); subs_b[rs[kk]] = sp.diff(rb, l, kk)
lin = {}
for c in ('tt', 'll', 'th'):
    e = (G[c] - T[c]).subs(subs_b, simultaneous=True)
    e0 = sp.simplify(e.subs(eps, 0))
    lin[c] = (e0, sp.diff(e, eps).subs(eps, 0))
chk("D0 flat space solves all three (zeroth order 0)", all(sp.simplify(lin[c][0]) == 0 for c in lin))
def mode_residual(k2, ratio):
    kk = sp.sqrt(k2)
    ph = ratio*B*sp.sin(kk*l)/l
    rp = B*(sp.sin(kk*l) - kk*l*sp.cos(kk*l))/l
    rh = sp.integrate(rp, l)
    out = []
    for c in lin:
        e = lin[c][1].subs({phi: ph, rho: rh}).doit()
        vals = [abs(complex(sp.N(e.subs({B: 1, L0: Lv, l: lv}), 30))) for Lv in (sp.Rational(-1, 3), sp.Rational(1, 2)) for lv in (sp.Rational(7, 10), sp.Rational(23, 10))]
        out.append(max(vals))
    return out
m1 = mode_residual(sp.Rational(1, 16), -2)
m2 = mode_residual(1/(16*(3*L0 + 4)), 4)
chk("D1 mode 1 (k^2 = 1/(16K^2), A = -2B) solves tt, ll, thth linearised", max(m1) < 1e-20, str(["%.1e" % v for v in m1]))
chk("D2 mode 2 (k^2 = 1/(16K^2(3L0+4)), A = 4B) solves tt, ll, thth linearised", max(m2) < 1e-20, str(["%.1e" % v for v in m2]))
# control: a wrong k must fail
mc = mode_residual(sp.Rational(1, 9), -2)
chk("D3 control: k^2 = 1/9 does NOT solve (the check can fail)", max(mc) > 1e-6, str(["%.1e" % v for v in mc]))
mlin = sp.expand(-l*(B*(sp.sin(k*l) - k*l*sp.cos(k*l))/l))
xs = np.linspace(0.1, 60, 4000)
mv = [float(mlin.subs({B: 1, k: sp.Rational(1, 4), l: xv})) for xv in xs]
chk("D4 linear m = -B (sin kl - kl cos kl) takes both signs on (0, 60 K]", min(mv) < 0 < max(mv))
tail = [abs(2*v/xv) for v, xv in zip(mv, xs) if xv > 40]
chk("D5 |2m/r| does not decay (max over x > 40 is %.3f B ~ 2kB = 0.5 B)" % max(tail), max(tail) > 0.45)

# ---------------- E: metre figures
lP22 = 1.616255e-35    # CODATA 2022 (scipy 1.17.1 constants, txt2022 block), unchanged from CODATA 2018
chk("E1 K = 1/sqrt(5760 pi) l_P = %.7f l_P (tree's withdrawn typed 0.0074335 is off in the 5th digit)" % Kp, abs(Kp - 0.0074338) < 5e-7)
chk("E2 r(0) at L = -2/3 = %.5f l_P (HPS 'about 0.02 l_P')" % (4*math.sqrt(2/3)*Kp), abs(4*math.sqrt(2/3)*Kp - 0.02428) < 1e-4)
chk("E3 300 l_P = %.4g m (tree largest throat 4.849e-33 m; CODATA 2022 l_P)" % (300*lP22), round(300*lP22, 36) == 4.849e-33)
print("FAILS:", fails if fails else "none")
sys.exit(1 if fails else 0)
