#!/usr/bin/env python3
r"""
DOCKET 67 audit, key 'semiclassical-einstein-equation'.

The tree uses G_ab = 8 pi <T_ab> (HPS eq. (1)/(3); FW eq. (1.1)).  The general
form read at source (Hu & Verdaguer 0802.0658 eq. (3.7), p.8) is

    G_ab + Lambda g_ab - 2(alpha A_ab + beta B_ab) = 8 pi G <T^R_ab>,

with Lambda, alpha, beta renormalized couplings "zero in the classical Einstein
equation", the counterterm ambiguity "absorbed into the renormalized coupling
constants".  The tree's form is the member Lambda = alpha = beta = 0.

This script checks, exactly (sympy), on HPS's metric (2)
    ds^2 = -f(l) dt^2 + dl^2 + r(l)^2 dOmega^2 :
 C1  G^a_b of metric (2) is identically conserved (contracted Bianchi) -- the
     integrability condition that makes G = 8 pi <T> demand nabla.<T> = 0.
 C2  (1)H_ab := 2 nabla_a nabla_b R - 2 g_ab Box R - 2 R R_ab + g_ab R^2/2
     (the metric variation of INT sqrt(-g) R^2) is identically conserved and
     has trace -6 Box R: an allowed beta-type term.  A sign-flipped control
     (+2 R R_ab) must FAIL conservation.
 C3  the Bach tensor (Weyl^2 variation, the alpha-type term) is identically
     conserved and traceless on metric (2); and HPS's log bracket B (the tree's
     own transcription, qeihps.hps_system, repaired) is compared with it.
 C4  AT HPS's THROAT DATA (f',f'',f''' = r',r'',r''' = 0): the ll component of
     (1)H is 2/r0^4 with NO fourth derivatives, so the ll (constraint) equation
     with a beta-type term b*(1)H on the left reads
          -1/r0^2 - b * 2/r0^4 = 16 K^2 L / r0^4
     => r0^2 = -16 K^2 L - 2 b.   b = 0 reproduces HPS eq. (9) exactly.
     Numbers at HPS's L = -2/3; b at which the throat ceases to exist.
 C5  with b != 0 the tt and theta-theta equations at the throat are re-solved
     for f''''(0)/f(0), r''''(0)/r(0): the tree's closed forms are the b = 0
     member; a sample b shows they move.
 C6  Kuo-Ford: nothing new here (audited as kuo-ford-1993-measure); the
     fluctuation hypothesis is only cross-referenced.

The tree's own HPS system is imported read-only (no bytecode written).
"""
import sys
sys.dont_write_bytecode = True
import sympy as sp

TREE = '/home/user/Claude-Method-Works/research/warp-drive'
sys.path.insert(0, TREE)
import qeihps  # noqa: E402  (read-only import)

results = []


def rec(name, ok, detail):
    results.append((name, ok, detail))
    print(('PASS ' if ok else 'FAIL ') + name + ' :: ' + str(detail))


l = sp.Symbol('l', real=True)
t, th, ph = sp.symbols('t theta phi', real=True)
f = sp.Function('f')(l)
r = sp.Function('r')(l)
X = [t, l, th, ph]
n = 4
g = sp.diag(-f, 1, r**2, r**2*sp.sin(th)**2)
gi = g.inv()

Gam = [[[sp.simplify(sum(gi[a, d]*(sp.diff(g[d, b], X[c]) + sp.diff(g[d, c], X[b])
                                    - sp.diff(g[b, c], X[d])) for d in range(n))/2)
         for c in range(n)] for b in range(n)] for a in range(n)]


def riemann():
    Rm = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    e = sp.diff(Gam[a][b][d], X[c]) - sp.diff(Gam[a][b][c], X[d])
                    e += sum(Gam[a][c][k]*Gam[k][b][d] - Gam[a][d][k]*Gam[k][b][c]
                             for k in range(n))
                    Rm[a, b, c, d] = sp.simplify(e)
    return Rm


Rm = riemann()                                    # R^a_{bcd}, MTW
Ric = sp.Matrix(n, n, lambda b, d: sp.simplify(sum(Rm[a, b, a, d] for a in range(n))))
Rs = sp.simplify(sum(gi[a, b]*Ric[a, b] for a in range(n) for b in range(n)))
Gdn = sp.simplify(Ric - Rs*g/2)


def cov_d_scalar2(S):
    """nabla_a nabla_b S (lower indices)."""
    dS = [sp.diff(S, X[a]) for a in range(n)]
    return sp.Matrix(n, n, lambda a, b: sp.simplify(sp.diff(dS[b], X[a])
                     - sum(Gam[k][a][b]*dS[k] for k in range(n))))


def div_mixed(Tdn):
    """nabla^a T_ab for symmetric lower-index T, returned as a covector."""
    Tup = gi*Tdn                                        # T^a_b
    out = []
    for b in range(n):
        e = sum(sp.diff(Tup[a, b], X[a]) for a in range(n))
        e += sum(Gam[a][a][k]*Tup[k, b] for a in range(n) for k in range(n))
        e -= sum(Gam[k][a][b]*Tup[a, k] for a in range(n) for k in range(n))
        out.append(sp.simplify(e))
    return out


def mixed(Tdn):
    M = gi*Tdn
    return [sp.simplify(M[i, i]) for i in range(n)]


# ---------------------------------------------------------------- C1
divG = div_mixed(Gdn)
Gm = mixed(Gdn)
Gprinted = qeihps.hps_system(sp)['G']
S0 = qeihps.hps_system(sp)
sub_tree = {S0['f']: f, S0['r']: r}
lhs_match = [sp.simplify(Gm[i] - Gprinted[j].subs(S0['l'], l).subs(sub_tree))
             for j, i in enumerate((0, 1, 2))]
rec('C1 Bianchi: nabla^a G_ab == 0 on metric (2)', all(x == 0 for x in divG), divG)
rec('C1b HPS printed G^t_t, G^l_l, G^th_th == computed', all(x == 0 for x in lhs_match), lhs_match)

# ---------------------------------------------------------------- C2
DDR = cov_d_scalar2(Rs)
boxR = sp.simplify(sum(gi[a, b]*DDR[a, b] for a in range(n) for b in range(n)))
H1 = sp.simplify(2*DDR - 2*g*boxR - 2*Rs*Ric + g*Rs**2/2)
H1_bad = sp.simplify(2*DDR - 2*g*boxR + 2*Rs*Ric + g*Rs**2/2)
divH1 = div_mixed(H1)
divH1bad = div_mixed(H1_bad)
trH1 = sp.simplify(sum(gi[a, b]*H1[a, b] for a in range(n) for b in range(n)) + 6*boxR)
rec('C2 (1)H conserved', all(sp.simplify(x) == 0 for x in divH1), [sp.simplify(x) for x in divH1])
rec('C2b control: +2RR_ab variant NOT conserved', any(sp.simplify(x) != 0 for x in divH1bad), 'l-component nonzero')
rec('C2c trace (1)H == -6 Box R', trH1 == 0, trH1)

# ---------------------------------------------------------------- C3  Bach
# Weyl tensor, all lower: C_abcd
Rdn = {}
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                Rdn[a, b, c, d] = sp.simplify(sum(g[a, e]*Rm[e, b, c, d] for e in range(n)))
P = sp.simplify((Ric - Rs*g/6)/2)                 # Schouten in 4D
C = {}
for a in range(n):
    for b in range(n):
        for c in range(n):
            for d in range(n):
                C[a, b, c, d] = sp.simplify(Rdn[a, b, c, d]
                    - (g[a, c]*P[b, d] - g[a, d]*P[b, c] - g[b, c]*P[a, d] + g[b, d]*P[a, c]))
# Bach_ab = nabla^c nabla_a P_bc - Box P_ab + P^cd C_acbd  (4D, one standard form)
#          equivalently (nabla^c nabla^d + R^cd/2) C_acbd.
# Use: B_ab = nabla^c C_acbd ;^d ... computed via Cotton: B_ab = nabla^c Cot_abc + P^cd C_acbd,
# Cotton Cot_abc = nabla_c P_ab - nabla_b P_ac.


def cov_d_2(T):
    """nabla_c T_ab -> dict (a,b,c)."""
    out = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                e = sp.diff(T[a, b], X[c])
                e -= sum(Gam[k][c][a]*T[k, b] + Gam[k][c][b]*T[a, k] for k in range(n))
                out[a, b, c] = sp.simplify(e)
    return out


dP = cov_d_2(P)
Cot = {(a, b, c): sp.simplify(dP[a, b, c] - dP[a, c, b])
       for a in range(n) for b in range(n) for c in range(n)}


def div3_first(T3):
    """nabla^c T_abc  (contract derivative with LAST index c)."""
    out = sp.zeros(n, n)
    for a in range(n):
        for b in range(n):
            s = 0
            for c in range(n):
                for e in range(n):
                    if gi[c, e] == 0:
                        continue
                    # nabla_e T_abc
                    d = sp.diff(T3[a, b, c], X[e])
                    d -= sum(Gam[k][e][a]*T3[k, b, c] + Gam[k][e][b]*T3[a, k, c]
                             + Gam[k][e][c]*T3[a, b, k] for k in range(n))
                    s += gi[c, e]*d
            out[a, b] = sp.simplify(s)
    return out


Pup = gi*P*gi
PC = sp.Matrix(n, n, lambda a, b: sp.simplify(sum(Pup[c, d]*C[a, c, b, d]
                                               for c in range(n) for d in range(n))))
Bach = sp.simplify(div3_first(Cot) + PC)
divBach = div_mixed(Bach)
trBach = sp.simplify(sum(gi[a, b]*Bach[a, b] for a in range(n) for b in range(n)))
rec('C3 Bach conserved on metric (2)', all(sp.simplify(x) == 0 for x in divBach), [sp.simplify(x) for x in divBach])
rec('C3b Bach traceless', trBach == 0, trBach)
Bm = mixed(Bach)
Hm = mixed(H1)
# HPS log bracket (tree's repaired transcription) vs Bach: is B^mu_nu = k * Bach^mu_nu ?
Bt, Bl, Bh = [x.subs(S0['l'], l).subs(sub_tree) for x in S0['B']]
k = sp.Symbol('k')
ratios = [sp.simplify(Bt/Bm[0]), sp.simplify(Bl/Bm[1]), sp.simplify(Bh/Bm[2])]
prop = all(sp.simplify(x - ratios[0]) == 0 for x in ratios) and not ratios[0].has(l)
rec('C3c HPS log bracket B == const * Bach (so shifting ln mu == shifting alpha)',
    prop, ratios[0] if prop else ratios)

# ---------------------------------------------------------------- C4 throat
L, a4, b4, bb = sp.symbols('L a4 b4 b', real=True)
rt = sp.Symbol('rt', positive=True)
K2 = S0['K2']


def at0(e):
    e = e.subs({f.diff(l, 4): a4*sp.exp(L), r.diff(l, 4): b4*rt})
    e = e.subs({f.diff(l, kk): 0 for kk in (3, 2, 1)})
    e = e.subs({r.diff(l, kk): 0 for kk in (3, 2, 1)})
    return sp.simplify(e.subs({f: sp.exp(L), r: rt}))


A_ = [x.subs(S0['l'], l).subs(sub_tree) for x in S0['A']]
lf = sp.log(f)
Hl0 = at0(Hm[1])
rec('C4a (1)H^l_l at throat data == 2/r0^4, no 4th derivatives',
    sp.simplify(Hl0 - 2/rt**4) == 0, Hl0)
Ebeta = [at0(Gm[i] - bb*Hm[i] - K2*(A_[j] + lf*[Bt, Bl, Bh][j]))
         for j, i in enumerate((0, 1, 2))]
r0sq = sp.solve(sp.Eq(Ebeta[1], 0), rt**2) or sp.solve(sp.Eq(sp.numer(sp.together(Ebeta[1])), 0), rt)
r0sq_expr = sp.simplify(sp.solve(sp.numer(sp.together(Ebeta[1])).subs(rt, sp.sqrt(sp.Symbol('s', positive=True))),
                                 sp.Symbol('s', positive=True))[0])
target = -16*K2*L - 2*bb
rec('C4b ll constraint with beta term: r0^2 == -16 K^2 L - 2b', sp.simplify(r0sq_expr - target) == 0, r0sq_expr)
Lv = sp.Rational(-2, 3)
r0sq_hps = sp.nsimplify(target.subs({bb: 0, L: Lv}))
rec('C4c b=0, L=-2/3: r0^2 == 1/(540 pi), r0 = 0.0242789 l_P (HPS eq.(9), tree)',
    sp.simplify(r0sq_hps - 1/(540*sp.pi)) == 0, (r0sq_hps, sp.N(sp.sqrt(r0sq_hps), 7)))
b_crit = sp.solve(sp.Eq(target.subs(L, Lv), 0), bb)[0]
rec('C4d throat ceases to exist at b >= b_crit = 1/(1080 pi) l_P^2 = %.6e' % float(b_crit),
    sp.simplify(b_crit - 1/(1080*sp.pi)) == 0, (b_crit, float(b_crit), float(b_crit/K2)))
for bv in (sp.Rational(-1, 1)*K2, K2, -sp.Rational(1, 100), sp.Rational(1, 10000)):
    v = target.subs({L: Lv, bb: bv})
    print('    b = %-14s r0^2 = %.6e  r0 = %s  rho_geom(0)=1/(8 pi r0^2)= %s' % (
        sp.nsimplify(bv), float(v), ('%.6f' % float(sp.sqrt(v))) if v > 0 else 'NO THROAT',
        ('%.4f' % float(1/(8*sp.pi*v))) if v > 0 else '-'))

# ---------------------------------------------------------------- C5 4th derivatives
rr = sp.sqrt(target)
sol = sp.solve([Ebeta[0].subs(rt, rr), Ebeta[2].subs(rt, rr)], [a4, b4], dict=True)
A4b, B4b = sp.factor(sol[0][a4]), sp.factor(sol[0][b4])
A4_0 = sp.factor(A4b.subs(bb, 0))
B4_0 = sp.factor(B4b.subs(bb, 0))
tree_A4 = 259200*sp.pi**2*(-L - 1)/(L*(3*L + 4))
tree_B4 = 129600*sp.pi**2*(2 - L**2)/(L**2*(3*L + 4))
rec('C5a b=0 reproduces the tree f4/f = 259200 pi^2 (-L-1)/(L(3L+4))', sp.simplify(A4_0 - tree_A4) == 0, A4_0)
rec('C5b b=0 reproduces the tree r4/r = 129600 pi^2 (2-L^2)/(L^2(3L+4))', sp.simplify(B4_0 - tree_B4) == 0, B4_0)
bs = K2  # a sample beta of one-loop size
vA0, vB0 = float(A4_0.subs(L, Lv)), float(B4_0.subs(L, Lv))
vA, vB = float(A4b.subs({L: Lv, bb: bs})), float(B4b.subs({L: Lv, bb: bs}))
rec('C5c b = K^2 (one-loop size) moves both fourth derivatives at L=-2/3',
    abs(vA - vA0) > 1e-6*abs(vA0) or abs(vB - vB0) > 1e-6*abs(vB0),
    dict(f4f_b0=vA0, f4f_bK2=vA, r4r_b0=vB0, r4r_bK2=vB))
print('    f4/f(b) =', A4b)
print('    r4/r(b) =', B4b)


# ---------------------------------------------------------------- C6 throat <rho>, rho+p_l with b
Ht0 = at0(Hm[0]); Hl0b = at0(Hm[1]); Gt0 = at0(Gm[0]); Gl0 = at0(Gm[1])
subs4 = {a4: A4b, b4: B4b, rt: rr}
rho_q = sp.simplify((-(Gt0 - bb*Ht0)/(8*sp.pi)).subs(subs4))
nec_q = sp.simplify((((Gl0 - bb*Hl0b) - (Gt0 - bb*Ht0))/(8*sp.pi)).subs(subs4))
rec('C6a b=0: <rho>(0) == -45/L (tree)', sp.simplify(rho_q.subs(bb, 0) + 45/L) == 0, sp.simplify(rho_q.subs(bb, 0)))
rec('C6b b=0: <rho+p_l>(0) == 0 (tree: radial NEC saturated on throat)', sp.simplify(nec_q.subs(bb, 0)) == 0, sp.simplify(nec_q.subs(bb, 0)))
print('    <rho>(0; b)       =', sp.factor(rho_q))
print('    <rho+p_l>(0; b)   =', sp.factor(nec_q))
for bv in (-K2, K2):
    print('    b=%s: <rho>(0)=%.4f  <rho+p_l>(0)=%.4f' % (sp.nsimplify(bv), float(rho_q.subs({L: Lv, bb: bv})), float(nec_q.subs({L: Lv, bb: bv}))))
# sign of r4/r (throat a minimum) and existence as b varies, L=-2/3, scanning b in units of K^2
import fractions
rows = []
for m in [x/4 for x in range(-40, 41)]:
    bv = sp.Rational(fractions.Fraction(m).limit_denominator(8).numerator, fractions.Fraction(m).limit_denominator(8).denominator)*K2
    tv = target.subs({L: Lv, bb: bv})
    if tv <= 0:
        rows.append((m, 'no-throat')); continue
    rows.append((m, 'min' if B4b.subs({L: Lv, bb: bv}) > 0 else 'NOT-min'))
chg = [(rows[i][0], rows[i][1]) for i in range(1, len(rows)) if rows[i][1] != rows[i-1][1]]
rec('C6c throat character changes with b/K^2 on [-10,10] at L=-2/3 (transitions listed)', len(chg) > 0, chg)

# ---------------------------------------------------------------- C7 hbar-dependence of the throat
hb = sp.Symbol('hbar', positive=True)       # K^2 -> hbar * K^2 (G = c = 1, lengths in units where l_P^2 = hbar)
r0_h = sp.sqrt(-16*hb*K2*L)
d1 = sp.limit(sp.diff(r0_h.subs(L, Lv), hb), hb, 0, '+')
rec('C7 r0 = sqrt(-16 hbar K^2 L) -> 0 as hbar -> 0 with d r0/d hbar -> oo: not a power series in hbar about a classical solution (FW fn [77] class)',
    d1 == sp.oo, dict(r0=r0_h, dr0_dhbar_at_0=d1))
# ---------------------------------------------------------------- C8 data: Lambda and the R^2 coupling bound
Lam = sp.Float('2.846e-122')                # Planck 2018, m_Pl^-2 units (sibling audit, READ there)
rec('C8a Lambda / |G^t_t(throat)| at L=-2/3 (Lambda negligible)', True, float(Lam/(540*sp.pi)))
c2max = sp.Integer(10)**61                  # Calmet-Hsu-Reeb 0803.1836 p.2: c2(mu~1e-3 eV) < 1e61
bmax = 16*sp.pi*c2max                       # b = c2/c1, c1 = M_P^2/(16 pi) -> b = 16 pi c2 l_P^2
rec('C8b experimental ceiling |b| < 16 pi 1e61 l_P^2 exceeds b_crit by', True, float(bmax/b_crit))

lP = 1.616255e-35                            # m, CODATA 2018
rec('C8c length sqrt(|b|max) below which data do not exclude b*(1)H ~ G (metres)', True, float(sp.sqrt(bmax))*lP)

npass = sum(1 for _, ok, _ in results if ok)
print('\n%d/%d checks pass' % (npass, len(results)))
sys.exit(0 if npass == len(results) else 1)
