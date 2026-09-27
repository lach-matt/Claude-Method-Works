#!/usr/bin/env python3
"""DOCKET 67 audit: hps-1997-largest-throat-300lp.

Source READ: Hochberg, Popov, Sushkov, gr-qc/9701064v1 (PRL 78, 2050 (1997)),
alphaXiv page text cached at ../src/hps/hps_0.xml (md5 a5f55d322aed581c9b1dead99d63cb84).

What is checkable here, and is checked:
  A. HPS eq (8) (the throat quartic) re-derived from HPS eq (6) as transcribed from
     the page text, at l = 0 with f'(0) = r'(0) = 0 (sympy, exact).
  B. Dimensional homogeneity of every transcribed term of eq (6) (each must scale
     as length^-4 under l, r -> lambda l, lambda r); flags transcription/print
     discrepancies.  A flag is a DISCREPANCY, not a refutation.
  C. HPS's two printed figures from (8): ~0.02 l_P and ~67 l_P.
  D. The quartic alone admits r(0) arbitrarily large (HPS abstract's claim):
     the largest root diverges as f''(0)/f(0) -> 0+ with -1 < ln f(0) <= 0,
     r''(0) = 0.  Boundary data needed for 300 l_P and for 1 m.
  E. The scale ledger: 300 l_P in metres (CODATA 2018 = 2022 l_P), orders short
     of 1 m and of the Proxima span; sensitivity to HPS's printed range 200-300
     and to radius-vs-diameter.
NOT checkable here: whether HPS's 200-300 l_P 'local solutions' exist as global
solutions (boundary data and xi not printed; 'full account ... separate
publication'); the horizons 'located far from the throat' (no data printed).
"""
import math
import sympy as sp

ok = True


def chk(label, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + label)
    ok = ok and bool(cond)


# ---------------------------------------------------------------- A, B
f, f1, f2, f3, r, r1, r2, r3 = sp.symbols("f f1 f2 f3 r r1 r2 r3")
L = sp.log(f)
# eq (6) RHS bracket, non-log part, transcribed term by term from the page text
nonlog = [f1**4/f**4, -16*f1**3*r1/(f**3*r), 64*f1*r1**3/(f*r**3),
          -4*f1**2*f2/f**3, 64*f1*r1*f2/(f**2*r), -64*r1**2*f2/(f*r**2),
          -4*f2**2/f**2, -48*f1**2*r2/(f**2*r), 32*f1*r1*r2/(f*r**2),
          32*f2*r2/(f*r), 8*f1*f3/f**2, -32*r1*f3/(f*r), -32*f1*r3/(f*r)]
# log part; the 4th term is printed (page text) as f'^2 r'^2/(f^2 r)
logp = [16/r**4, 7*f1**4/f**4, -20*f1**3*r1/(f**3*r),
        -4*f1**2*r1**2/(f**2*r),            # as printed -- see B
        32*f1*r1**3/(f*r**3), -16*r1**4/r**4, -12*f1**2*f2/f**3,
        48*f1*r1*f2/(f**2*r), -32*r1**2*f2/(f*r**2), -4*f2**2/f**2,
        -16*f1**2*r2/(f**2*r), 16*f1*r1*r2/(f*r**2), 16*f2*r2/(f*r),
        -16*r2**2/r**2, 8*f1*f3/f**2, -16*r1*f3/(f*r), -16*f1*r3/(f*r),
        32*r1*r3/r**2]

lam = sp.Symbol("lam", positive=True)
scale = {f1: f1/lam, f2: f2/lam**2, f3: f3/lam**3, r: lam*r, r1: r1, r2: r2/lam,
         r3: r3/lam**2}
bad = []
for tag, terms in (("nonlog", nonlog), ("log", logp)):
    for i, t in enumerate(terms):
        ratio = sp.simplify(t.subs(scale, simultaneous=True) / t)
        if sp.simplify(ratio - lam**-4) != 0:
            bad.append((tag, i + 1, t, ratio))
print("B. dimensional scan of eq (6) as transcribed: %d term(s) off length^-4" % len(bad))
for b in bad:
    print("   ", b)
chk("B: exactly one inhomogeneous term, the log-part f'^2 r'^2/(f^2 r)",
    len(bad) == 1 and bad[0][1] == 4 and bad[0][0] == "log")

K2 = sp.Symbol("K2", positive=True)
rhs = K2 * (sum(nonlog) + L * sum(logp))
lhs = f1*r1/(f*r) + r1**2/r**2 - 1/r**2
eq6_throat = sp.expand((lhs - rhs).subs({f1: 0, r1: 0}))
# the misprinted term carries r'^2: it vanishes at the throat either way
q, a, Ls, x = sp.symbols("q a L x")
hps8 = (-4*q**2*(1 + Ls)*x**4 + 32*q*a*(1 + Ls/2)*x**3
        + (1/K2 - 16*a**2*Ls)*x**2 + 16*Ls)
mine = sp.expand(-eq6_throat * r**4 / K2)
mine = mine.subs({f2: q*f, r2: a, r: x}).subs(sp.log(f), Ls)
chk("A: eq (6) at l=0, f'=r'=0, times -r^4/K^2 == HPS eq (8) exactly",
    sp.simplify(sp.expand(mine) - sp.expand(hps8)) == 0)

# ---------------------------------------------------------------- C
Kv2 = sp.Rational(1, 5760) / sp.pi
c1 = sp.solve(hps8.subs({K2: Kv2, q: 0, a: 0, Ls: sp.Rational(-2, 3)}), x)
c1 = [s for s in c1 if s.is_positive][0]
chk("C1: ln f(0)=-2/3, f''=r''=0 -> r0 = sqrt(15)/(90 sqrt(pi)) = %.5f (printed ~0.02)"
    % float(c1), sp.simplify(c1 - sp.sqrt(15)/(90*sp.sqrt(sp.pi))) == 0)
c2 = sp.solve(hps8.subs({K2: Kv2, q: 1, a: 0, Ls: 0}), x)
c2 = [s for s in c2 if s.is_positive][0]
chk("C2: f(0)=f''(0)=1, r''=0 -> r0 = 12 sqrt(10 pi) = %.4f (printed ~67)" % float(c2),
    sp.simplify(c2 - 12*sp.sqrt(10*sp.pi)) == 0)
# eq (9)'s r(0) = sqrt(-16 K^2 ln f(0)) is the q=0 case of (8)
chk("C3: eq (9)'s r(0)=sqrt(-16K^2 ln f(0)) solves (8) at q=0",
    sp.simplify(hps8.subs({q: 0, a: 0, x: sp.sqrt(-16*K2*Ls)})) == 0)

# ---------------------------------------------------------------- D
Kinv = math.sqrt(5760 * math.pi)            # K^-1 in l_P
def largest_root(qv, Lv, av=0.0):
    import numpy as np
    co = [-4*qv**2*(1+Lv), 32*qv*av*(1+Lv/2), Kinv**2 - 16*av**2*Lv, 0.0, 16*Lv]
    rts = [z.real for z in np.roots(co) if abs(z.imag) < 1e-9*max(1, abs(z)) and z.real > 0]
    return max(rts) if rts else float("nan")
seq = [(qv, largest_root(qv, -0.5)) for qv in (1.0, 1e-1, 1e-2, 1e-3, 1e-6)]
print("D. ln f(0) = -1/2, r''(0) = 0: largest root r0 (l_P) vs f''(0)/f(0):")
for qv, rv in seq:
    print("    q = %-8g r0 = %.6g   (asymptote K^-1/(2 q sqrt(1+L)) = %.6g)"
          % (qv, rv, Kinv/(2*qv*math.sqrt(0.5))))
chk("D1: r0 grows without bound as q -> 0+ (monotone, > 1e6 l_P at q=1e-6)",
    all(seq[i][1] < seq[i+1][1] for i in range(len(seq)-1)) and seq[-1][1] > 1e6)
q300 = Kinv / (2 * 300.0)                   # f(0)=1 (L=0), r''=0: r0 = 1/(2Kq)
chk("D2: f(0)=1, r''(0)=0, f''(0)=%.4f l_P^-2 gives r0 = 300 l_P (order-unity data)"
    % q300, abs(largest_root(q300, 0.0) - 300.0) < 1e-6)
LP18 = 1.616255e-35                          # CODATA 2018 == CODATA 2022 value
r1m = 1.0 / LP18
q1m = Kinv / (2 * r1m)
print("   r0 = 1 m = %.4e l_P needs f''(0)/f(0) = %.4e l_P^-2 = %.4e m^-2"
      % (r1m, q1m, q1m / LP18**2))
xr = sp.Rational(1) / sp.Rational("1.616255e-35")      # 1 m in l_P, exact rational
qr = 1 / (2 * sp.sqrt(Kv2) * xr)                       # exact q for that root
chk("D3: the throat constraint (8) alone does not cap r0: r0 = 1 m is an exact root "
    "(sympy, f(0)=1, r''(0)=0)",
    sp.simplify(hps8.subs({K2: Kv2, q: qr, a: 0, Ls: 0, x: xr})) == 0)

# ---------------------------------------------------------------- E
PROXIMA_M = 4.2465 * 9.4607304725808e15
for lp, tag in ((1.616255e-35, "CODATA 2018 = 2022"), (1.61605e-35, "CODATA 1986")):
    m300 = 300 * lp
    print("E. %s: 300 l_P = %.4e m; orders short of 1 m %.3f; of Proxima %.3f"
          % (tag, m300, math.log10(1/m300), math.log10(PROXIMA_M/m300)))
m300 = 300 * LP18
chk("E1: 300 l_P = 4.849e-33 m (tree)", abs(m300/4.849e-33 - 1) < 1e-3)
chk("E2: orders short of 1 m = 32.31 (tree)", abs(math.log10(1/m300) - 32.31) < 5e-3)
chk("E3: orders short of Proxima = 48.92 (tree)",
    abs(math.log10(PROXIMA_M/m300) - 48.92) < 5e-3)
print("   HPS print 'r(0) ~ 200 - 300 l_P': orders to 1 m span %.3f .. %.3f"
      % (math.log10(1/(300*LP18)), math.log10(1/(200*LP18))))
print("   radius vs diameter (abstract speaks of diameter): shift %.3f orders"
      % math.log10(2))
print("   Gaia DR3 parallax of Proxima 768.0665 mas -> %.4f ly (tree 4.2465)"
      % (1/0.7680665 * 3.26156377716743))

print("\nALL PASS" if ok else "\nSOME FAIL")
raise SystemExit(0 if ok else 1)
