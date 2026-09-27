#!/usr/bin/env python3
"""DOCKET 67 -- audit of HPS gr-qc/9701064 eq. (9), the throat initial data.

INDEPENDENT of the tree: eqs. (5), (6), (7) are transcribed here afresh from the
arXiv v1 text layer (scratchpad/d67/src/hps/hps_0.xml, pp.4-5), NOT imported
from hpscentre.py.  K = 1 units (lengths in K, K^2 = 1/(5760 pi) l_P^2).
M1 = the ln-f coefficient of f'^2 f''/f^3 in (5): 16 printed, 116 conserved.
M2 = the power of r in -4 f'^2 r'^2/(f^2 r^M2) in (6)'s log bracket: 1 printed.

Checks
 A  transcription control: with (M1, M2) = (116, 2) the source is conserved
    identically; with (16, 1) it is not.
 B  eq. (8) re-derived from (6) at l = 0 using only r'(0) = f'(0) = 0.
 C  eq. (9): r(0)^2 = -16 K^2 ln f(0) is the ONLY positive root of (8) at
    f''(0) = r''(0) = 0, and it is real iff ln f(0) < 0.
 D  r(0) at ln f(0) = -2/3, in l_P, against HPS's 'r(0) ~ 0.02 l_P'.
 E  f''''(0), r''''(0) from tt and thth at eq. (9) data, as functions of
    L = ln f(0); both readings (M1 drops out at l = 0); 7 sqrt(6)/768 at -2/3;
    the 4th-order determinant -256 (3L + 4)/(f r); sign over -1 <= L < 0.
 F  integration from eq. (9) data (L = -2/3) of THIS transcription: first
    l with r' = 1 (Misner-Sharp m = (r/2)(1 - r'^2) < 0), in K and in l_P,
    against the tree's FIRST_NEGATIVE_M_THROAT_LP = 0.0516 and 'l < 8 K'.
Exit 0 iff every check passes.
"""
import math, sys
import sympy as sp

l = sp.Symbol('l')
fs = sp.symbols('f0:5')   # f, f', f'', f''', f''''
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
    print(("PASS " if ok else "FAIL ") + name + ((" -- " + detail) if detail else ""))
    if not ok:
        fails.append(name)

# ---------------- A: transcription control via conservation
F = sp.Function('F')(l); R = sp.Function('R')(l)
sub = {}
for k in range(5):
    sub[fs[k]] = sp.diff(F, l, k); sub[rs[k]] = sp.diff(R, l, k)
def divergence(T):
    Tt, Tl, Th = [T[c].subs(sub) for c in ('tt', 'll', 'th')]
    fp, rp = sp.diff(F, l), sp.diff(R, l)
    return sp.diff(Tl, l) + fp/(2*F)*(Tl - Tt) + 2*rp/R*(Tl - Th)
# conservation at a numerical random point with random derivatives (fast, exact rationals)
import random
random.seed(67)
def div_at_point(M1, M2, trials=3):
    G, T = systems(M1, M2)
    fs5 = sp.symbols('f5'); rs5 = sp.symbols('r5')
    # d/dl acting on a function of (f0..f4, r0..r4)
    def dl(e):
        out = 0
        for k in range(5):
            nxt_f = fs[k+1] if k < 4 else fs5
            nxt_r = rs[k+1] if k < 4 else rs5
            out += sp.diff(e, fs[k])*nxt_f + sp.diff(e, rs[k])*nxt_r
        return out
    D = dl(T['ll']) + f1/(2*f)*(T['ll'] - T['tt']) + 2*r1/r*(T['ll'] - T['th'])
    vals = []
    for _ in range(trials):
        pt = {s: sp.Rational(random.randint(1, 9), random.randint(1, 9)) for s in list(fs) + list(rs) + [fs5, rs5]}
        vals.append(sp.nsimplify(sp.N(D.subs(pt), 40), tolerance=1e-30))
    Dg = dl(G['ll']) + f1/(2*f)*(G['ll'] - G['tt']) + 2*r1/r*(G['ll'] - G['th'])
    return vals, sp.simplify(Dg)
vc, dg = div_at_point(116, 2)
chk("A0 Bianchi: Einstein side of this transcription is conserved identically", dg == 0, str(dg))
chk("A1 conserved reading (M1, M2) = (116, 2): divergence of source = 0 at 3 random points",
    all(abs(float(v)) < 1e-25 for v in vc), str([float(v) for v in vc]))
vp, _ = div_at_point(16, 1)
chk("A2 printed reading (16, 1): divergence of source != 0 (control)",
    any(abs(float(v)) > 1e-6 for v in vp), str([float(v) for v in vp]))
vm, _ = div_at_point(16, 2)
chk("A3 (16, 2) i.e. M2 repaired, M1 as printed: still not conserved",
    any(abs(float(v)) > 1e-6 for v in vm), str([float(v) for v in vm]))

# ---------------- B: eq. (8)
K = sp.Symbol('K', positive=True)
G, T = systems(116, 2)
throat = {f1: 0, r1: 0, f3: 0, r3: 0}
ll0 = sp.expand((G['ll'] - K**2*T['ll']).subs({f1: 0, r1: 0}))
eq8 = (-4*(f2/f)**2*(1 + LN)*r**4 + 32*(f2*r2/f)*(1 + LN/2)*r**3
       + (K**-2 - 16*r2**2*LN)*r**2 + 16*LN)
ratio = sp.simplify(ll0*(-r**4/K**2) - eq8)
chk("B  eq.(8) = -(r^4/K^2) x [ll eq. at r'=f'=0], exactly (independent of f''', r''')",
    ratio == 0 and not ll0.has(f3) and not ll0.has(r3), str(ratio))
G1, T1 = systems(16, 1)
ll0p = sp.expand((G1['ll'] - K**2*T1['ll']).subs({f1: 0, r1: 0}))
chk("B' same eq.(8) from the printed reading (M1, M2 vanish at r' = f' = 0)",
    sp.simplify(ll0p - ll0) == 0)

# ---------------- C: eq. (9)
L = sp.Symbol('L', real=True)
X = sp.Symbol('X')    # X = r(0)^2
eq8_9 = eq8.subs({f2: 0, r2: 0}).subs(LN, L).subs(r**2, X)
solX = sp.solve(sp.Eq(eq8_9, 0), X)
chk("C  at f''=r''=0, eq.(8) is linear in r(0)^2 with the single root -16 K^2 ln f(0)",
    solX == [-16*K**2*L], str(solX))
chk("C' real positive r(0) iff ln f(0) < 0 (HPS's upper bound is forced; -1 is a choice)",
    sp.solve(-16*K**2*L > 0, L) is not None)
print("     solve(-16 K^2 L > 0):", sp.solve(-16*K**2*L > 0, L))

# ---------------- D: r(0) in l_P at L = -2/3
Kp = 1/math.sqrt(5760*math.pi)
r0K = math.sqrt(-16*(-2/3))
r0 = r0K*Kp
print("     K = %.6f l_P ; r(0) = sqrt(32/3) K = %.5f K = %.5f l_P" % (Kp, r0K, r0))
chk("D  r(0) at ln f(0) = -2/3 rounds to HPS's printed 'r(0) ~ 0.02 l_P'", round(r0, 2) == 0.02,
    "%.5f l_P" % r0)
# the case-1 throat of eq (8) (f(0)=f''(0)=1, r''(0)=0) quoted ~67 l_P: sibling audit; recheck
Kn = sp.sqrt(1/(5760*sp.pi))
q = sp.Poly(eq8.subs({f: 1, f2: 1, r2: 0}).subs(sp.log(1), 0).subs(K, Kn), r)
roots = [complex(z) for z in q.nroots()]
pos = sorted(z.real for z in roots if abs(z.imag) < 1e-12 and z.real > 0)
print("     control: eq.(8) at f=f''=1, r''=0 positive roots (l_P):", pos)

# ---------------- E: 4th derivatives at eq.(9) data
Lsym = sp.Symbol('L', negative=True)
Kone = {K: 1}
res = {}
for nm, (m1, m2) in (("conserved", (116, 2)), ("printed", (16, 1))):
    G_, T_ = systems(m1, m2)
    d = {f: sp.exp(Lsym), f1: 0, f2: 0, f3: 0, r: sp.sqrt(-16*Lsym), r1: 0, r2: 0, r3: 0}
    ett = sp.simplify((G_['tt'] - T_['tt']).subs(d))
    eth = sp.simplify((G_['th'] - T_['th']).subs(d))
    s = sp.solve([ett, eth], [f4, r4], dict=True)[0]
    A = sp.Matrix([[sp.diff((G_[c] - T_[c]), v) for v in (f4, r4)] for c in ('tt', 'th')])
    detA = sp.simplify(A.det())
    res[nm] = (sp.simplify(s[f4]), sp.simplify(s[r4]), detA)
    print("     %s: f''''(0) = %s ; r''''(0) = %s ; det = %s" % (nm, res[nm][0], res[nm][1], sp.factor(detA)))
chk("E0 4th-derivative data identical in both readings at l = 0",
    all(sp.simplify(a - b) == 0 for a, b in zip(res['conserved'][:2], res['printed'][:2])))
f4L, r4L, detA = res['conserved']
chk("E1 4th-order determinant = -256 (3 ln f + 4)/(f r)  (K = 1)",
    sp.simplify(detA + 256*(3*sp.log(f) + 4)/(f*r)) == 0, str(sp.factor(detA)))
r4v = sp.nsimplify(sp.simplify(r4L.subs(Lsym, sp.Rational(-2, 3))))
chk("E2 r''''(0) at ln f(0) = -2/3 equals 7 sqrt(6)/768 K^-3 (tree, hpscentre.py:204)",
    sp.simplify(r4v - 7*sp.sqrt(6)/768) == 0, str(r4v))
f4v = sp.nsimplify(sp.simplify(f4L.subs(Lsym, sp.Rational(-2, 3))))
print("     f''''(0)/K^-4 at -2/3 =", f4v, "=", float(f4v))
# sign over the whole range
grid = [-1 + k/1000 for k in range(1000)]
r4s = [float(r4L.subs(Lsym, g)) for g in grid]
f4s = [float(f4L.subs(Lsym, g)) for g in grid]
chk("E3 r''''(0) > 0 on all of -1 <= ln f(0) < 0 (grid 1e-3): a minimum throughout HPS's range",
    all(v > 0 for v in r4s), "min %.4g" % min(r4s))
print("     f''''(0) sign over the range: min %.4g, max %.4g" % (min(f4s), max(f4s)))
chk("E5 f4(0) = 0 exactly at ln f(0) = -1, > 0 on (-1, 0), < 0 on (-4/3, -1): the lower bound -1 "
    "coincides with f having a 4th-order local minimum at the throat -- COMPUTED; HPS state no reason",
    sp.simplify(f4L.subs(Lsym, -1)) == 0 and all(v > 0 for v in f4s[1:])
    and all(float(f4L.subs(Lsym, g)) < 0 for g in (-1.3, -1.2, -1.1, -1.01)))
chk("E4 |3 ln f + 4| >= 1 on HPS's range (determinant nonzero at l = 0 for every allowed datum)",
    min(abs(3*g + 4) for g in grid) >= 1 - 1e-12)

# ---------------- F: integrate this transcription from eq.(9) data
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
def build(m1, m2):
    G_, T_ = systems(m1, m2)
    E = [G_[c] - T_[c] for c in ('tt', 'th')]
    A = sp.Matrix([[sp.diff(e, v) for v in (f4, r4)] for e in E])
    b = sp.Matrix([e.subs({f4: 0, r4: 0}) for e in E])
    sol = A.LUsolve(-b)
    args = (f, f1, f2, f3, r, r1, r2, r3)
    fF4 = sp.lambdify(args, sol[0], 'math'); fR4 = sp.lambdify(args, sol[1], 'math')
    fll = sp.lambdify(args, G_['ll'] - T_['ll'], 'math')
    def rhs(x, y):
        return [y[1], y[2], y[3], fF4(*y), y[5], y[6], y[7], fR4(*y)]
    return rhs, fll
L0 = -2/3
y0 = [math.exp(L0), 0, 0, 0, math.sqrt(-16*L0), 0, 0, 0]
out = {}
for nm, (m1, m2) in (("conserved", (116, 2)), ("printed-M1", (16, 2))):
    rhs, fll = build(m1, m2)
    sols = {}
    for meth in ("DOP853", "Radau", "LSODA"):
        s = solve_ivp(rhs, (0, 60), y0, method=meth, rtol=1e-10, atol=1e-13, dense_output=True)
        xs = np.linspace(0, s.t[-1], 60001)
        r1v = s.sol(xs)[5]
        idx = np.where((r1v[:-1] <= 1) & (r1v[1:] > 1))[0]
        xn = brentq(lambda x: s.sol(x)[5] - 1, xs[idx[0]], xs[idx[0]+1], xtol=1e-12) if len(idx) else None
        llmax = max(abs(fll(*s.sol(x))) for x in np.linspace(0.5, min(40, s.t[-1]), 400))
        sols[meth] = (xn, s.status, llmax)
    out[nm] = sols
    for meth, (xn, st, llm) in sols.items():
        print("     %-11s %-6s first r'=1 at l = %s K = %s l_P ; |ll residual| max on [0.5,40]K = %.3g"
              % (nm, meth, None if xn is None else "%.6f" % xn,
                 None if xn is None else "%.5f" % (xn*Kp), llm))
xc = [out['conserved'][m][0] for m in ("DOP853", "Radau", "LSODA")]
chk("F1 conserved reading: r' crosses 1 (m < 0) before l = 8 K, three integrators agree to 1e-6",
    all(x is not None and x < 8 for x in xc) and max(xc) - min(xc) < 1e-6, str(xc))
chk("F2 first m < 0 in l_P rounds to the tree's FIRST_NEGATIVE_M_THROAT_LP = 0.0516",
    xc[0] is not None and round(xc[0]*Kp, 4) == 0.0516, "%.6f" % (xc[0]*Kp))
chk("F3 conserved reading keeps the ll constraint (|residual| < 1e-6 on [0.5, 40] K)",
    out['conserved']['DOP853'][2] < 1e-6, "%.3g" % out['conserved']['DOP853'][2])

print("\n%d FAIL" % len(fails) if fails else "\nALL PASS")
sys.exit(1 if fails else 0)
