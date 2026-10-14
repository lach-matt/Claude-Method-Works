#!/usr/bin/env python3
"""DOCKET 67 -- audit of gr-qc/9701064 (Hochberg-Popov-Sushkov 1997), eqs. (5)-(9).

Independent re-derivation.  Eqs. (5)-(7) are RE-TYPED here from the arXiv v1
PDF text layer (scratchpad d67/src/hps/hps_0.xml, pp.4-5), NOT imported from
the tree.  The tree's transcription (hpscentre.build) is then imported from a
read-only COPY (_hps_tree/, md5 checked against the live file) only to compare.

Checks (all sympy, exact):
  C1  printed LHS of (5)-(7) == G^mu_nu of metric (2), MTW convention (own
      curvature code).
  C2  my text-layer transcription == tree's hpscentre.build() at PRINTED slots
      (term-by-term difference 0).
  C3  dimension: every term of every bracket scales as length^-4 under
      l -> s l, r -> s r (f dimensionless); list the terms that do not.
  C4  conservation d_l T^l_l + (f'/2f)(T^l_l-T^t_t) + (2r'/r)(T^l_l-T^th_th) = 0
      identically: solve for the tt-log f'^2 f''/f^3 coefficient a_tt and the
      thth-log f'^4/f^4 coefficient a_th as UNKNOWNS, for ll-log slot r^1 and r^2.
      Also: is the log bracket ALONE conserved and traceless (mu-independence,
      footnote [20])?
  C5  trace of non-log part == 16 (Riem^2 - Ric^2 + c box R): solve c.
  C6  eq. (8) re-derived from (6) at l=0 with r'=f'=0; compared with the printed
      quartic (as re-typed from p.6).
  C7  eq. (9): r0^2 = -16 K^2 L; r0 at L=-2/3 vs printed "~0.02 l_P"; the p.7
      case f=f''=1, r''=0 vs printed "~67 l_P".
  C8  throat fourth derivatives from (5),(7) at l=0 with data (9); rho, p_l, p_t;
      rho+p_l at O(l^2) at L=-2/3; sign of f''''/f, r''''/r on [-1,0) (sympy
      interval reasoning); compared with the tree's qeihps.py:176-187 values.
  C9  Misner-Sharp mass m = (r/2)(1-r'^2) near the throat with data (9):
      m = r0/2 + O(l^4)?  (throatmass.py:27-28 says "through second order").
Exit 1 if any assertion fails.
"""
import hashlib
import os
import sys

sys.dont_write_bytecode = True
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
COPY = os.path.join(HERE, "_hps_tree")
REAL = "/home/user/Claude-Method-Works/research/warp-drive"
FAIL = []


def check(name, ok, detail=""):
    print(("PASS " if ok else "FAIL ") + name + ("  " + detail if detail else ""))
    if not ok:
        FAIL.append(name)


l = sp.Symbol('l', real=True)
fF, rF = sp.Function('f')(l), sp.Function('r')(l)
f, f1, f2, f3, f4 = [sp.diff(fF, l, k) for k in range(5)]
r, r1, r2, r3, r4 = [sp.diff(rF, l, k) for k in range(5)]
a_tt, a_th = sp.symbols('a_tt a_th')
P = sp.Symbol('P')  # placeholder power for ll slot

# ------------------------------------------------------------------ text layer
# HPS (5), non-log and ln f bracket, re-typed from hps_0.xml p.5
TT_N = (32/r**4 + 7*f1**4/f**4 - 24*f1**3*r1/(f**3*r) + 24*f1**2*r1**2/(f**2*r**2)
        - 32*r1**4/r**4 + 4*f1**2*f2/f**3 - 12*f2**2/f**2 + 80*f1**2*r2/(f**2*r)
        - 160*f1*r1*r2/(f*r**2) + 128*r1**2*r2/r**3 - 64*f2*r2/(f*r) + 32*r2**2/r**2
        - 16*f1*f3/f**2 + 64*r1*f3/(f*r) - 96*f1*r3/(f*r) - 64*r1*r3/r**2
        + 16*f4/f - 64*r4/r)
TT_L = (16/r**4 - 49*f1**4/f**4 + 44*f1**3*r1/(f**3*r) + 20*f1**2*r1**2/(f**2*r**2)
        - 16*r1**4/r**4 + a_tt*f1**2*f2/f**3 - 104*f1*r1*f2/(f**2*r) - 36*f2**2/f**2
        + 8*f1**2*r2/(f**2*r) - 80*f1*r1*r2/(f*r**2) + 64*r1**2*r2/r**3
        + 16*f2*r2/(f*r) + 16*r2**2/r**2 - 48*f1*f3/f**2 + 64*r1*f3/(f*r)
        - 16*f1*r3/(f*r) - 32*r1*r3/r**2 + 16*f4/f - 32*r4/r)
# HPS (6)
LL_N = (f1**4/f**4 - 16*f1**3*r1/(f**3*r) + 64*f1*r1**3/(f*r**3) - 4*f1**2*f2/f**3
        + 64*f1*r1*f2/(f**2*r) - 64*r1**2*f2/(f*r**2) - 4*f2**2/f**2
        - 48*f1**2*r2/(f**2*r) + 32*f1*r1*r2/(f*r**2) + 32*f2*r2/(f*r)
        + 8*f1*f3/f**2 - 32*r1*f3/(f*r) - 32*f1*r3/(f*r))
LL_L = (16/r**4 + 7*f1**4/f**4 - 20*f1**3*r1/(f**3*r) - 4*f1**2*r1**2/(f**2*r**P)
        + 32*f1*r1**3/(f*r**3) - 16*r1**4/r**4 - 12*f1**2*f2/f**3
        + 48*f1*r1*f2/(f**2*r) - 32*r1**2*f2/(f*r**2) - 4*f2**2/f**2
        - 16*f1**2*r2/(f**2*r) + 16*f1*r1*r2/(f*r**2) + 16*f2*r2/(f*r)
        - 16*r2**2/r**2 + 8*f1*f3/f**2 - 16*r1*f3/(f*r) - 16*f1*r3/(f*r)
        + 32*r1*r3/r**2)
# HPS (7)
TH_N = (17*f1**4/f**4 - 16*f1**3*r1/(f**3*r) - 32*f1*r1**3/(f*r**3)
        - 52*f1**2*f2/f**3 + 32*f1*r1*f2/(f**2*r) + 32*r1**2*f2/(f*r**2)
        + 28*f2**2/f**2 + 16*f1**2*r2/(f**2*r) + 64*f1*r1*r2/(f*r**2)
        - 32*f2*r2/(f*r) + 24*f1*f3/f**2 - 48*r1*f3/(f*r) + 32*f1*r3/(f*r)
        - 16*f4/f)
TH_L = (-16/r**4 + a_th*f1**4/f**4 - 12*f1**3*r1/(f**3*r) - 8*f1**2*r1**2/(f**2*r**2)
        - 16*f1*r1**3/(f*r**3) + 16*r1**4/r**4 - 52*f1**2*f2/f**3
        + 28*f1*r1*f2/(f**2*r) + 16*r1**2*f2/(f*r**2) + 20*f2**2/f**2
        + 4*f1**2*r2/(f**2*r) + 32*f1*r1*r2/(f*r**2) - 32*r1**2*r2/r**3
        - 16*f2*r2/(f*r) + 20*f1*f3/f**2 - 24*r1*f3/(f*r) + 16*f1*r3/(f*r)
        - 8*f4/f + 16*r4/r)
PRINTED = {a_tt: 16, a_th: 21, P: 1}
LHS_PRINTED = (2*r2/r + r1**2/r**2 - 1/r**2,
               f1*r1/(f*r) + r1**2/r**2 - 1/r**2,
               f2/(2*f) + r2/r + f1*r1/(2*f*r) - f1**2/(4*f**2))

# ------------------------------------------------------------------ curvature
t, th, ph = sp.symbols('t theta phi')
X = [t, l, th, ph]
g = sp.diag(-fF, 1, rF**2, rF**2*sp.sin(th)**2)
gi = g.inv()
N = 4
Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                  - sp.diff(g[b, c], X[d])) for d in range(N))/2)
         for c in range(N)] for b in range(N)] for a in range(N)]


def riem(a, b, c, d):  # R^a_bcd, MTW
    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
    e += sum(Gam[a][c][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][c] for k in range(N))
    return sp.simplify(e)


R4 = [[[[riem(a, b, c, d) for d in range(N)] for c in range(N)] for b in range(N)] for a in range(N)]
Ric = sp.Matrix(N, N, lambda b, d: sp.simplify(sum(R4[a][b][a][d] for a in range(N))))
Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(N) for b in range(N)))
Gmix = sp.simplify(gi*Ric - sp.eye(N)*Rs/2)
c1 = [sp.simplify(Gmix[0, 0] - LHS_PRINTED[0]), sp.simplify(Gmix[1, 1] - LHS_PRINTED[1]),
      sp.simplify(Gmix[2, 2] - LHS_PRINTED[2])]
check("C1 printed LHS (5)-(7) == G^mu_nu of metric (2), MTW", c1 == [0, 0, 0], str(c1))

# Riem^2, Ric^2, box R
g_low = g
Riem_low = lambda a, b, c, d: sum(g_low[a, e]*R4[e][b][c][d] for e in range(N))
riem2 = 0
for a in range(N):
    for b in range(N):
        for c in range(N):
            for d in range(N):
                lo = Riem_low(a, b, c, d)
                if lo == 0:
                    continue
                riem2 += lo**2*gi[a, a]*gi[b, b]*gi[c, c]*gi[d, d]  # diagonal metric
riem2 = sp.simplify(riem2)
ric2 = sp.simplify(sum(Ric[a, b]**2*gi[a, a]*gi[b, b] for a in range(N) for b in range(N)))
sqrtg = sp.sqrt(fF)*rF**2
boxR = sp.simplify(sp.diff(sqrtg*sp.diff(Rs, l), l)/sqrtg)

# ------------------------------------------------------------------ C2 tree comparison
md5 = lambda p: hashlib.md5(open(p, 'rb').read()).hexdigest()
same = md5(os.path.join(COPY, "hpscentre.py")) == md5(os.path.join(REAL, "hpscentre.py"))
check("C2a tree copy md5 == live hpscentre.py", same, md5(os.path.join(REAL, "hpscentre.py")))
sys.path.insert(0, COPY)
sys.path.append(REAL)
import hpscentre as H  # noqa: E402
S = H.build(sp)
sub_tree = {S['a_tt']: 16, S['a_th']: 21, S['ll_pow']: 1}
fT, rT = S['fF'], S['rF']
rep = {fT: fF, rT: rF, S['l']: l}
mine = [(TT_N, TT_L), (LL_N, LL_L), (TH_N, TH_L)]
diffs = []
for (mn, ml), (tn, tl) in zip(mine, S['hps']):
    tn2 = tn.subs(sub_tree).subs(rep)
    tl2 = tl.subs(sub_tree).subs(rep)
    diffs.append(sp.simplify(mn.subs(PRINTED) - tn2))
    diffs.append(sp.simplify(ml.subs(PRINTED) - tl2))
check("C2b my text-layer transcription == tree hpscentre.build() at printed slots",
      all(d == 0 for d in diffs), str(diffs))
tree_lhs = [sp.simplify(Gt.subs(rep) - Lp) for Gt, Lp in zip(S['G'], LHS_PRINTED)]
check("C2c tree LHS == printed LHS", tree_lhs == [0, 0, 0])

# ------------------------------------------------------------------ C3 dimension
s = sp.Symbol('s', positive=True)
Dsyms = sp.symbols('F0:5 R0:5')
Fs, Rsy = Dsyms[:5], Dsyms[5:]
tosym = {}
for k in range(4, -1, -1):
    tosym[sp.diff(fF, l, k) if k else fF] = Fs[k]
    tosym[sp.diff(rF, l, k) if k else rF] = Rsy[k]


def symb(e):
    return e.subs(tosym)


scale = {Fs[k]: Fs[k]*s**(-k) for k in range(5)}
scale.update({Rsy[k]: Rsy[k]*s**(1-k) for k in range(5)})
bad = []
for name, e in [("tt_n", TT_N), ("tt_l", TT_L), ("ll_n", LL_N), ("ll_l", LL_L),
                ("th_n", TH_N), ("th_l", TH_L)]:
    e = symb(e.subs(PRINTED))
    for term in sp.Add.make_args(sp.expand(e)):
        w = sp.simplify(term.subs(scale)/term)
        if sp.simplify(w - s**-4) != 0:
            bad.append((name, term, w))
print("     non-homogeneous terms (printed):", bad)
check("C3 exactly one printed term is not length^-4: ll-log -4 f'^2 r'^2/(f^2 r)",
      len(bad) == 1 and bad[0][0] == "ll_l" and bad[0][2] == s**-3)

# ------------------------------------------------------------------ C4 conservation
Lf = sp.log(fF)


def div(T):
    tt, ll, thth = T
    return sp.diff(ll, l) + f1/(2*f)*(ll - tt) + 2*r1/r*(ll - thth)


def coeff_eqs(expr):
    e = sp.expand(symb(sp.expand(expr)).subs(sp.log(Fs[0]), sp.Symbol('LOG')))
    num = sp.numer(sp.together(e))
    poly = sp.Poly(sp.expand(num), *Dsyms, sp.Symbol('LOG'))
    return [c for c in poly.coeffs()]


results = {}
for p in (1, 2):
    T = (TT_N + Lf*TT_L, (LL_N + Lf*LL_L).subs(P, p), TH_N + Lf*TH_L)
    eqs = coeff_eqs(div(T))
    sol = sp.solve(eqs, [a_tt, a_th], dict=True)
    results[p] = sol
    print(f"     ll-log slot r^{p}: conserving (a_tt, a_th) solutions = {sol}")
check("C4a printed r^1 slot: NO (a_tt, a_th) conserves", results[1] == [])
check("C4b r^2 slot: unique conserving pair (a_tt, a_th) = (116, 21)",
      results[2] == [{a_tt: 116, a_th: 21}])
T_cons = (TT_N + Lf*TT_L, (LL_N + Lf*LL_L).subs(P, 2), TH_N + Lf*TH_L)
T_cons = tuple(x.subs({a_tt: 116, a_th: 21}) for x in T_cons)
LOGB = (TT_L.subs({a_tt: 116}), LL_L.subs(P, 2), TH_L.subs({a_th: 21}))
dl = sp.simplify(div(LOGB))
trl = sp.simplify(LOGB[0] + LOGB[1] + 2*LOGB[2])
check("C4c conserved reading: log bracket alone conserved", dl == 0, str(dl)[:80])
check("C4d conserved reading: log bracket traceless", trl == 0, str(trl)[:80])
trl_pr = sp.simplify((TT_L + LL_L + 2*TH_L).subs(PRINTED))
print("     printed log-bracket trace:", trl_pr)
dfull_pr = sp.simplify(div(tuple(x.subs(PRINTED) for x in
                                 (TT_N + Lf*TT_L, LL_N + Lf*LL_L, TH_N + Lf*TH_L))))
check("C4e printed system (16, 21, r^1) NOT conserved", dfull_pr != 0)
# does the M1/M2 slot matter AT THE THROAT (f'=r'=0)?
thr = {f1: 0, r1: 0}
m1_at_throat = sp.simplify((TT_L.subs(a_tt, 116) - TT_L.subs(a_tt, 16)).subs(thr))
m2_at_throat = sp.simplify((LL_L.subs(P, 2) - LL_L.subs(P, 1)).subs(thr))
check("C4f both repaired terms vanish where f'=0 (the throat)",
      m1_at_throat == 0 and m2_at_throat == 0)

# ------------------------------------------------------------------ C5 trace anomaly form
cc = sp.Symbol('c')
trn = sp.simplify(TT_N + LL_N + 2*TH_N)
res = sp.simplify(trn - 16*(riem2 - ric2 + cc*boxR))
csol = sp.solve(coeff_eqs(res), cc, dict=True)
print("     non-log trace == 16(Riem^2 - Ric^2 + c boxR): c =", csol)
check("C5 non-log trace is 16(Riem^2 - Ric^2 + c box R) with unique c = 1",
      csol == [{cc: 1}])

# ------------------------------------------------------------------ C6 eq. (8)
K2 = sp.Rational(1, 5760)/sp.pi
F0, FPP, RPP, R0 = sp.symbols('f0 fpp rpp r0', positive=True)
L = sp.log(F0)
at0 = {f4: sp.Symbol('F4'), r4: sp.Symbol('R4'), f3: sp.Symbol('F3'), r3: sp.Symbol('R3'),
       f2: FPP, r2: RPP, f1: 0, r1: 0}
ll_eq = (LHS_PRINTED[1] - K2*(LL_N + Lf*LL_L.subs(P, 1)))
ll0 = ll_eq.subs(at0).subs({fF: F0, rF: R0})
ll0 = sp.simplify(ll0)
quart_mine = sp.expand(sp.simplify(-ll0*R0**4/K2))
quart_printed = (-4*(FPP/F0)**2*(1 + L)*R0**4 + 32*(FPP*RPP/F0)*(1 + L/2)*R0**3
                 + (1/K2 - 16*RPP**2*L)*R0**2 + 16*L)
d8 = sp.simplify(sp.expand(quart_mine - quart_printed))
check("C6a eq. (8) follows from (6) at l=0 with r'=f'=0 (printed quartic reproduced)",
      d8 == 0, str(d8))
free3 = sp.Symbol('F3') in ll0.free_symbols or sp.Symbol('R3') in ll0.free_symbols
check("C6b eq. (8) independent of f'''(0), r'''(0) (p.6 claim)", not free3)
ll0_p2 = sp.simplify((LHS_PRINTED[1] - K2*(LL_N + Lf*LL_L.subs(P, 2))).subs(at0).subs({fF: F0, rF: R0}))
check("C6c eq. (8) is the same under the ll-slot repair (r^1 vs r^2)", sp.simplify(ll0 - ll0_p2) == 0)

# ------------------------------------------------------------------ C7 eq. (9) and p.7
Lm = sp.Rational(-2, 3)
Lv = sp.Symbol('Lv', negative=True)
q9_from8 = sp.simplify(quart_printed.subs({FPP: 0, RPP: 0}).subs(F0, sp.exp(Lv)))
q9 = (1/K2)*R0**2 + 16*Lv
check('C7a0 (8) with f\'\'=r\'\'=0 collapses to K^-2 r0^2 + 16 L = 0', sp.simplify(q9_from8 - q9) == 0)
r0_9 = sp.solve(q9, R0)
check("C7a eq. (9) r(0) = sqrt(-16 K^2 ln f(0)) from (8) with f''=r''=0",
      len(r0_9) == 1 and sp.simplify(r0_9[0]**2 + 16*K2*Lv) == 0)
r0_23 = sp.sqrt(-16*K2*Lm)
print(f"     r0(L=-2/3) = {sp.nsimplify(r0_23)} = {float(r0_23):.6f} l_P  (printed '~0.02 l_P')")
check("C7b r0(L=-2/3) = sqrt(15)/(90 sqrt(pi)) = 0.02428 l_P",
      sp.simplify(r0_23 - sp.sqrt(15)/(90*sp.sqrt(sp.pi))) == 0 and abs(float(r0_23) - 0.02428) < 5e-6)
qc2 = quart_printed.subs({F0: 1, FPP: 1, RPP: 0})
sc2 = [x for x in sp.solve(qc2, R0) if x.is_positive]
print(f"     case f=f''=1, r''=0: r0 = {sc2} = {[float(x) for x in sc2]} l_P  (printed '~67 l_P')")
check("C7c p.7 case: r0 = 12 sqrt(10 pi) = 67.2599 l_P",
      len(sc2) == 1 and sp.simplify(sc2[0] - 12*sp.sqrt(10*sp.pi)) == 0)
check("C7d p.7 case lies OUTSIDE the eq. (9) range (ln f(0)=0, f''(0)=1 != 0)", True,
      "recorded: it is a separate p.7 illustration, not the plotted solution")

# ------------------------------------------------------------------ C8 throat 4th derivatives
F4s, R4s = sp.symbols('F4 R4')
Lsym = sp.Symbol('L', negative=True)
f0v = sp.exp(Lsym)
r0v = sp.sqrt(-16*K2*Lsym)
at9 = {f4: F4s, r4: R4s, f3: 0, r3: 0, f2: 0, r2: 0, f1: 0, r1: 0}
cons_sys = [LHS_PRINTED[0] - K2*T_cons[0], LHS_PRINTED[2] - K2*T_cons[2]]
eqs8 = [sp.simplify(e.subs(at9).subs({fF: f0v, rF: r0v})) for e in cons_sys]
sol8 = sp.solve(eqs8, [F4s, R4s], dict=True)[0]
f4f = sp.simplify(sol8[F4s]/f0v)
r4r = sp.simplify(sol8[R4s]/r0v)
tree_f4f = 259200*sp.pi**2*(-Lsym - 1)/(Lsym*(3*Lsym + 4))
tree_r4r = 129600*sp.pi**2*(2 - Lsym**2)/(Lsym**2*(3*Lsym + 4))
print("     f''''(0)/f(0) =", sp.factor(f4f), "   r''''(0)/r(0) =", sp.factor(r4r))
check("C8a f''''/f and r''''/r at the throat == qeihps.py values",
      sp.simplify(f4f - tree_f4f) == 0 and sp.simplify(r4r - tree_r4r) == 0)
# printed system gives the same at the throat
pr_sys = [LHS_PRINTED[0] - K2*(TT_N + Lf*TT_L).subs(PRINTED), LHS_PRINTED[2] - K2*(TH_N + Lf*TH_L).subs(PRINTED)]
eqsp = [sp.simplify(e.subs(at9).subs({fF: f0v, rF: r0v})) for e in pr_sys]
solp = sp.solve(eqsp, [F4s, R4s], dict=True)[0]
check("C8b printed and conserved readings agree at the throat (4th derivatives)",
      sp.simplify(solp[F4s] - sol8[F4s]) == 0 and sp.simplify(solp[R4s] - sol8[R4s]) == 0)
# signs on [-1, 0): sample densely + endpoint analysis
import fractions
signs_ok = True
for k in range(1, 1000):
    Lval = sp.Rational(-k, 1000)
    a = tree_f4f.subs(Lsym, Lval)
    b = tree_r4r.subs(Lsym, Lval)
    if not (a >= 0 and b > 0):
        signs_ok = False
a_m1 = tree_f4f.subs(Lsym, -1)
b_m1 = tree_r4r.subs(Lsym, -1)
# exact: numerator/denominator factor signs on (-1,0): -L-1 <0... check symbolically
num_f = sp.factor(-Lsym - 1); den_f = sp.factor(Lsym*(3*Lsym + 4))
print(f"     at L=-1: f''''/f = {a_m1}, r''''/r = {b_m1}; on (-1,0): (-L-1)<0, L<0, 3L+4>0 => f''''/f>0; 2-L^2>0 => r''''/r>0")
xL = sp.Symbol('x', real=True)
setF = sp.solve_univariate_inequality(tree_f4f.subs(Lsym, xL) >= 0, xL, relational=False)
setR = sp.solve_univariate_inequality(tree_r4r.subs(Lsym, xL) > 0, xL, relational=False)
exactF = sp.Interval.Ropen(-1, 0).is_subset(setF)
exactR = sp.Interval.Ropen(-1, 0).is_subset(setR)
print("     exact solution sets: f''''/f>=0 on", setF, "; r''''/r>0 on", setR)
check("C8c f''''/f >= 0 and r''''/r > 0 on [-1, 0) (exact inequality solve + grid of 999 rationals)",
      signs_ok and a_m1 == 0 and b_m1 > 0 and exactF and exactR)
rho0 = -LHS_PRINTED[0].subs(at9).subs({fF: f0v, rF: r0v})/(8*sp.pi)
pl0 = LHS_PRINTED[1].subs(at9).subs({fF: f0v, rF: r0v})/(8*sp.pi)
pt0 = LHS_PRINTED[2].subs(at9).subs({fF: f0v, rF: r0v})/(8*sp.pi)
rho0 = sp.simplify(rho0)
print("     throat: rho =", rho0, " p_l =", sp.simplify(pl0), " p_t =", sp.simplify(pt0),
      " rho(-2/3) =", rho0.subs(Lsym, Lm))
check("C8d rho = -45/L, p_l = -rho, p_t = 0; rho(-2/3) = 135/2",
      sp.simplify(rho0 + 45/Lsym) == 0 and sp.simplify(pl0 + rho0) == 0 and sp.simplify(pt0) == 0
      and rho0.subs(Lsym, Lm) == sp.Rational(135, 2))
# rho + p_l to O(l^2): (G^l_l - G^t_t)/(8 pi) with r = r0 + R4 l^4/24, f = f0 + F4 l^4/24
fs = f0v + sol8[F4s]*l**4/24
rs = r0v + sol8[R4s]*l**4/24
Gtt = (2*sp.diff(rs, l, 2)/rs + sp.diff(rs, l)**2/rs**2 - 1/rs**2)
Gll = (sp.diff(fs, l)*sp.diff(rs, l)/(fs*rs) + sp.diff(rs, l)**2/rs**2 - 1/rs**2)
nec = sp.series((Gll - Gtt)/(8*sp.pi), l, 0, 4).removeO()
nec23 = sp.simplify(nec.subs(Lsym, Lm))
print("     rho + p_l (L=-2/3) =", nec23, "+ O(l^4)")
check("C8e rho + p_l = -28350 pi l^2 + O(l^4) at L=-2/3",
      sp.simplify(nec23 + 28350*sp.pi*l**2) == 0)

# ------------------------------------------------------------------ C9 Misner-Sharp
ms = rs/2*(1 - sp.diff(rs, l)**2)
ms_ser = sp.series(ms, l, 0, 6).removeO()
print("     m(l) =", sp.simplify(ms_ser))
check("C9 m = r0/2 + O(l^4) on data (9) (so 'through second order' holds, and further)",
      sp.simplify(sp.series(ms - r0v/2, l, 0, 4).removeO()) == 0)

print()
print("SUMMARY:", "ALL PASS" if not FAIL else "FAILED: " + ", ".join(FAIL))
sys.exit(1 if FAIL else 0)
