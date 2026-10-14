#!/usr/bin/env python3
"""DOCKET 67 re-derivation: GMMPS (arXiv 2604.01047v1) dispersion functions as linstab.py uses them.
   Q(w^2) (4.30), F_S (5.3) with b_0, b_1, a (5.2), F_TT (5.4) with a = 4m^2, b_0 = 0, b_1 = 60/kappa.

Independent of linstab.py (nothing imported from the tree; its source is only READ as text in D1).
Source text: GMMPS v1 text layer (alphaXiv full-text dump held at scratchpad d64/L4/galanda.txt).

 R1  (5.1) and the TT equation from printed (3.11) S, T and printed (3.16):
       (1/4) S = [6 (1/6 - xi)^2 / 4] (Box - a)^2,  a = 2m^2/(6 xi - 1);   -(1/2) T = -(1/120)(Box - 4m^2)^2
 R2  term-by-term comparison with the prototype (4.9)  iota G~(Box (Box-a1)(Box-a2) phi (x) rho) + sum b_j Box^j phi = S:
       S: b_0 = -4 alpha_1 m^4 / (6(1/6-xi)^2), b_1 = -(2/kappa - 2 alpha_2 m^2)/(6(1/6-xi)^2) -> printed (5.2) at alpha_2 = 0,
          b_2 = -4 alpha_3/(6(1/6-xi)^2)  (GMMPS: 'free ... depends on alpha~^S_3'; the SIGN is computed here)
       TT: b_0 = 120 alpha^TT_1 m^4 -> 0 at Thm 3.6's alpha^TT_1 = 0, b_1 = 60/kappa (at alpha^TT_2 = 0), b_2 = 120 alpha^TT_4
 R3  the Fourier-Laplace symbol of (4.9) is Q(w^2) (4.30): Box -> -w^2, and the retarded Green function of (Box - M)
       is -theta(t) sin(omega t)/omega (GMMPS Cor. 4.4 proof), whose Laplace transform at omega^2 = p^2 + M is 1/(-w^2 - M)
 R4  F_S(-w^2) = -Q(w^2) identically (a1 = a2 = a); F_TT(-w^2) = -Q(w^2)|_{b_0 = 0}.  GMMPS's own sentence under (5.3),
       'this function equals Q(-w) given in (4.30) for xi = -w^2', is literally false (sign; Q(-w) != Q(w^2)): a misprint,
       immaterial to the zeros.
 D1  linstab.py's code lines carry exactly these expressions (text match on the owner file, line numbers asserted)
 N1  numeric: TT negative zero -> -b_1/b_2 and shrinks as b_2 grows (GMMPS 5.2's sentence), J from the (4.5) integral
 N2  numeric scope note on GMMPS 5.1's 'For sufficiently large -b_2, this [gamma_0] is the only negative zero':
       count negative real zeros of F_S (J included) on a finite grid at a test point, both signs of b_2
 H   hypotheses of use: the tree's xi in {0, 1/3} satisfy 5.1's 2/(6xi-1) < 4 and Prop 4.12's a < 4m^2;
       TT's a = 4m^2 is NOT in Prop 4.12's open interval (-inf, 4m^2)
Exit 0 iff every assertion passes.
"""
import os
import re
import sys
import sympy as sp
import mpmath as mp

ok = True


def chk(name, cond):
    global ok
    print(("PASS " if cond else "FAIL ") + name)
    ok = ok and bool(cond)


# ------------------------------------------------------------------ R1
m, kap, xi, B, w2 = sp.symbols('m kappa xi Box w2', real=True)
al1, al2, al3, t1, t2, t4 = sp.symbols('alpha1 alpha2 alpha3 alphaTT1 alphaTT2 alphaTT4', real=True)
S_op = sp.Rational(2, 3) * (m**2 + sp.Rational(1, 2) * (1 - 6 * xi) * B)**2      # (3.11) printed
T_op = sp.Rational(1, 60) * (B - 4 * m**2)**2                                     # (3.11) printed
aS = 2 * m**2 / (6 * xi - 1)
cS = 6 * (sp.Rational(1, 6) - xi)**2 / 4                                          # (5.1) printed prefactor
chk("R1 (1/4) S == [6(1/6-xi)^2/4] (Box - 2m^2/(6xi-1))^2   [(3.16) S line -> (5.1)]",
    sp.simplify(sp.Rational(1, 4) * S_op - cS * (B - aS)**2) == 0)
chk("R1 -(1/2) T == -(1/120)(Box - 4m^2)^2                    [(3.16) TT line -> 5.2 display]",
    sp.simplify(-sp.Rational(1, 2) * T_op + sp.Rational(1, 120) * (B - 4 * m**2)**2) == 0)

# ------------------------------------------------------------------ R2
# (3.16) S:  -(1/2k) Box h = -(1/4) S K0[h] + a1 m^4 h - (1/2) a2 m^2 Box h + a3 Box^2 h + S_S
# moved to the left:  (1/4) S K0[h] - a1 m^4 h - (1/2)(1/k - a2 m^2) Box h - a3 Box^2 h = S_S    (5.1 form)
localS = -al1 * m**4 - sp.Rational(1, 2) * (1 / kap - al2 * m**2) * B - al3 * B**2
bS = sp.Poly(sp.expand(localS / cS), B).all_coeffs()[::-1]        # divide by the nonlocal prefactor -> (4.9)
b0S, b1S, b2S = [sp.simplify(x) for x in bS]
c6 = 6 * (sp.Rational(1, 6) - xi)**2
chk("R2 S: b_0 = -alpha~^S_1 4m^4/(6(1/6-xi)^2)  == printed (5.2)", sp.simplify(b0S - (-al1 * 4 * m**4 / c6)) == 0)
chk("R2 S: b_1 = -(2/kappa)/(6(1/6-xi)^2) at alpha~^S_2 = 0  == printed (5.2)",
    sp.simplify(b1S.subs(al2, 0) - (-(2 / kap) / c6)) == 0)
chk("R2 S: b_1 carries +alpha~^S_2 m^2 term when alpha~^S_2 != 0 (so 5.1's alpha_2 = 0 is load-bearing)",
    sp.simplify(sp.diff(b1S, al2)) != 0)
chk("R2 S: b_2 = -4 alpha~^S_3/(6(1/6-xi)^2)  (computed; GMMPS print only 'depends on alpha~^S_3')",
    sp.simplify(b2S - (-4 * al3 / c6)) == 0)
chk("R2 S: sign(b_2) = -sign(alpha~^S_3) for xi != 1/6", sp.simplify(sp.diff(b2S, al3) * c6 + 4) == 0)
# (3.16) TT: -(1/2k) Box h = (1/2) T K0[h] + t1 m^4 h - (1/2) t2 m^2 Box h + t4 Box^2 h + S_TT
localT = -t1 * m**4 - sp.Rational(1, 2) * (1 / kap - t2 * m**2) * B - t4 * B**2
cT = -sp.Rational(1, 120)
bT = [sp.simplify(x) for x in sp.Poly(sp.expand(localT / cT), B).all_coeffs()[::-1]]
chk("R2 TT: b_0 = 120 alpha~^TT_1 m^4 -> 0 at Thm 3.6's alpha~^TT_1 = 0  == printed", sp.simplify(bT[0] - 120 * t1 * m**4) == 0
    and bT[0].subs(t1, 0) == 0)
chk("R2 TT: b_1 = 60/kappa at alpha~^TT_2 = 0  == printed", sp.simplify(bT[1].subs(t2, 0) - 60 / kap) == 0)
chk("R2 TT: b_2 = 120 alpha~^TT_4 ('proportional to alpha~^TT_4', printed)", sp.simplify(bT[2] - 120 * t4) == 0)
chk("R2 TT: a = 4m^2 read off T (double root of T in Box) == printed", sp.roots(sp.Poly(T_op, B)) == {4 * m**2: 2})

# ------------------------------------------------------------------ R3
t, s, om = sp.symbols('t s omega', positive=True)
G = -sp.sin(om * t) / om                                         # retarded Green fn of (Box - M), Box = -d_t^2 + Lap
# check it solves -G'' - omega^2 G = delta: for t > 0 homogeneous, G(0) = 0, G'(0+) = -1 (jump of -G' is +1)
chk("R3 -theta sin(omega t)/omega: homogeneous for t>0 and jump -G'(0+) = +1",
    sp.simplify(-sp.diff(G, t, 2) - om**2 * G) == 0 and G.subs(t, 0) == 0 and sp.diff(G, t).subs(t, 0) == -1)
LG = sp.simplify(sp.laplace_transform(G, t, s, noconds=True))
p2, M = sp.symbols('p2 M', positive=True)
chk("R3 Laplace[-sin(omega t)/omega] = -1/(s^2+omega^2) = 1/(-w^2 - M) at omega^2 = p^2 + M, w^2 = s^2 + p^2",
    sp.simplify(LG + 1 / (s**2 + om**2)) == 0)
a1, a2, b0, b1, b2 = sp.symbols('a1 a2 b0 b1 b2', real=True)
J = sp.Function('J')
# symbol: Box -> -w2 ; nonlocal: [-w2 (-w2-a1)(-w2-a2)] * INT rho(M)/(-w2-M) dM = [...] * (-J(-w2))
sym_49 = (-w2) * (-w2 - a1) * (-w2 - a2) * (-J(-w2)) + b0 + b1 * (-w2) + b2 * (-w2)**2
Q430 = w2 * (w2 + a1) * (w2 + a2) * J(-w2) + b0 - b1 * w2 + b2 * w2**2          # printed (4.30)
chk("R3 symbol of (4.9) == printed Q(w^2) (4.30)", sp.simplify(sym_49 - Q430) == 0)

# ------------------------------------------------------------------ R4
a, g = sp.symbols('a gamma', real=True)
FS = g * (a - g)**2 * J(g) - (b0 + b1 * g + b2 * g**2)                            # printed (5.3)
FTT = g * (a - g)**2 * J(g) - g * (b1 + b2 * g)                                   # printed (5.4)
Qaa = Q430.subs({a1: a, a2: a})
chk("R4 F_S(-w^2) = -Q(w^2) identically (a1 = a2 = a)", sp.simplify(FS.subs(g, -w2) + Qaa) == 0)
chk("R4 F_TT(-w^2) = -Q(w^2)|_{b0=0} identically", sp.simplify(FTT.subs(g, -w2) + Qaa.subs(b0, 0)) == 0)
chk("R4 F_TT is F_S at b_0 = 0 (so (5.4) is (5.3) specialised, not a new form)", sp.simplify(FTT - FS.subs(b0, 0)) == 0)
w = sp.Symbol('w', real=True)
lit = sp.simplify(FS.subs(g, -w**2) - Qaa.subs(w2, -w))
chk("R4 DISCREPANCY (recorded): GMMPS's sentence 'F_S equals Q(-w) for xi=-w^2' is literally false "
    "(F_S(-w^2) - Q(-w) != 0); only the overall sign/variable, zeros unaffected", lit != 0)
chk("R4 zeros unaffected: F_S(-w^2) and Q(w^2) differ by the factor -1 exactly",
    sp.simplify(FS.subs(g, -w2) / Qaa) == -1)

# ------------------------------------------------------------------ D1  the owner's lines, as text
LS = "/home/user/Claude-Method-Works/research/warp-drive/linstab.py"
src = open(LS, encoding="utf-8").read().splitlines()
want = {573: "c = 6 * (sp.Rational(1, 6) - xi) ** 2",
        574: "b0 = -al * 4 * m ** 4 / c",
        575: "b1 = -(2 / kap) / c",
        576: "a = 2 * m ** 2 / (6 * xi - 1)",
        605: "Q = w2 * (w2 + a) * (w2 + a) * J(-w2) + b0 - b1 * w2 + b2 * w2 ** 2",
        607: "FS = gam * (a - gam) ** 2 * J(gam) - (b0 + b1 * gam + b2 * gam ** 2)",
        646: "b0, b1, a = -al * 4 / c, -(2 / eps) / c, 2 / (6 * xi - 1)",
        761: "F = lambda g, J: g * (a - g) ** 2 * J - b0 - b1 * g - b2 * g ** 2",
        763: "a, b1 = mp.mpf(4), 60 / eps",
        764: "F = lambda g, J: g * (a - g) ** 2 * J - g * (b1 + b2 * g)"}
for ln, txt in want.items():
    chk("D1 linstab.py:%d carries '%s'" % (ln, txt), txt in src[ln - 1])
# the tree's expressions, retyped from those lines, against the source-derived ones
alt, kapt, xit, mt = sp.symbols('alpha kappa xi m', real=True)
ct = 6 * (sp.Rational(1, 6) - xit)**2
chk("D1 tree b0,b1,a (573-576) == R2's S coefficients",
    sp.simplify(-alt * 4 * mt**4 / ct - b0S.subs({al1: alt, m: mt, xi: xit})) == 0
    and sp.simplify(-(2 / kapt) / ct - b1S.subs({al2: 0, kap: kapt, xi: xit})) == 0
    and sp.simplify(2 * mt**2 / (6 * xit - 1) - aS.subs({m: mt, xi: xit})) == 0)
chk("D1 tree m = 1 units at 646: b0 = -4 al/c, b1 = -(2/eps)/c is (5.2) at m = 1, kappa = eps = kappa m^2",
    sp.simplify((-al1 * 4 * m**4 / c6).subs(m, 1) + 4 * al1 / c6) == 0)
chk("D1 tree F_S(0) = -b0 = 4 alpha m^4/(6(1/6-xi)^2) (linstab.py:158)",
    sp.simplify(FS.subs(g, 0).subs(b0, b0S) - 4 * al1 * m**4 / c6) == 0)

# ------------------------------------------------------------------ H  hypotheses of use
for xv in (0, sp.Rational(1, 3)):
    chk("H xi = %s: 2/(6xi-1) = %s < 4 (5.1 / Prop 4.5) and a = %s m^2 < 4m^2 (Prop 4.12)"
        % (xv, 2 / (6 * xv - 1), 2 / (6 * xv - 1)), 2 / (6 * xv - 1) < 4)
chk("H TT: a = 4m^2 is NOT in Prop 4.12's (-inf, 4m^2) (boundary; recorded, GMMPS still cite Thm 4.14 for TT)",
    not (4 < 4))

# ------------------------------------------------------------------ N1  TT negative zero
mp.mp.dps = 40


def Jint(gv, mm=1):
    f = lambda MM: mp.sqrt(1 - 4 * mm**2 / MM) / (16 * mp.pi**2 * MM) / (MM - gv)
    return mp.quad(f, [4 * mm**2, 8 * mm**2, 64 * mm**2, mp.inf])


def FTTn(gv, b1v, b2v, av=4):
    return gv * (av - gv)**2 * Jint(gv) - gv * (b1v + b2v * gv)


prev = None
for kv in (mp.mpf(1),):
    b1v = 60 / kv
    for b2v in (mp.mpf(10)**3, mp.mpf(10)**4, mp.mpf(10)**6):
        # zero of F_TT/gamma on gamma < 0
        h = lambda gv: (4 - gv)**2 * Jint(gv) - (b1v + b2v * gv)
        r = mp.findroot(h, -b1v / b2v)
        pred = -b1v / b2v
        print("   TT kappa=1 b2=%s: root %s, -b1/b2 = %s, rel %s" % (mp.nstr(b2v, 3), mp.nstr(r, 12), mp.nstr(pred, 12),
                                                                    mp.nstr((r - pred) / pred, 3)))
        chk("N1 TT b2=%s: a negative zero exists, within 1e-3 of -b1/b2" % mp.nstr(b2v, 3),
            r < 0 and abs((r - pred) / pred) < 1e-3 and abs(FTTn(r, b1v, b2v)) < mp.mpf(10)**-25)
        if prev is not None:
            chk("N1   |gamma_0| shrinks as b2 grows (GMMPS 5.2)", abs(r) < abs(prev))
        prev = r
chk("N1 gamma = 0 is always a zero of F_TT (5.2: 'the classical gravitational waves')", FTTn(mp.mpf(0), 60, 10**3) == 0)

# ------------------------------------------------------------------ N2  scope note on 5.1's sentence
alv = 1 / (64 * mp.pi**2)


def FSn(gv, b2v, kv=1, xv=0):
    c = 6 * (mp.mpf(1) / 6 - xv)**2
    b0v, b1v, av = -alv * 4 / c, -(2 / kv) / c, 2 / (6 * mp.mpf(xv) - 1)
    return gv * (av - gv)**2 * Jint(gv) - (b0v + b1v * gv + b2v * gv**2)


grid = [-mp.mpf(10)**(e / mp.mpf(8)) for e in range(-48, 49)]       # gamma in [-1e6, -1e-6]
for b2v in (mp.mpf(100), mp.mpf(-100), mp.mpf(-1000)):
    vals = [FSn(gv, b2v) for gv in grid]
    changes = sum(1 for i in range(len(vals) - 1) if vals[i] * vals[i + 1] < 0)
    print("   S (m=1, kappa=1, xi=0, alpha=1/64pi^2) b2=%s: sign changes of F_S on [-1e6,-1e-6] = %d"
          % (mp.nstr(b2v, 3), changes))
    if b2v == 100:
        chk("N2 b2 = +100: exactly ONE negative zero (gamma_0) on the grid", changes == 1)
    elif b2v == -100:
        chk("N2 b2 = -100: TWO negative zeros on the grid (gamma_0 and ~ -b1/b2) -- 'only negative zero' fails here",
            changes == 2)
    else:
        disc = (2 / (mp.mpf(1) / 6))**2 - 4 * (alv * 4 / (mp.mpf(1) / 6)) * 1000
        chk("N2 b2 = -1000: discriminant of b0 + b1 g + b2 g^2 is < 0 (%s) and NO negative real zero on the grid"
            % mp.nstr(disc, 4), disc < 0 and changes == 0)

print("\nALL PASS" if ok else "\nSOME FAIL")
sys.exit(0 if ok else 1)
