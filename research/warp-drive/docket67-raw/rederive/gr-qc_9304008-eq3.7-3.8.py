#!/usr/bin/env python3
"""DOCKET 67 -- audit of Kuo & Ford gr-qc/9304008 v1, eqs (3.7) and (3.8)
(vacuum + two-particle state).  Independent re-derivation: the stress tensor is
built from the mode function itself (not from the tree's :T00: formula), normal
ordering is done by the commutative-symbol map, expectations by explicit Fock
matrices at two truncations.  z3 for the sign / inequality claims.
Source text used: d67/src/casmag/all/gr-qc_9304008v1.txt (md5 f1a6628604751cf61b2a4bd411b00153)."""
import sympy as sp, z3, itertools, json, sys

out = {}
def rec(k, v):
    out[k] = v
    print("%-66s %s" % (k, v))

t, x, L, w = sp.symbols('t x L omega', positive=True)
eps = sp.symbols('epsilon', real=True)
th = sp.symbols('theta', real=True)
# ---- 1. mode function and KF bilinears (2.11)-(2.14), massless, k along x, omega = k
f = sp.exp(sp.I*(w*x - w*t))/sp.sqrt(2*w*L**3)
fc = sp.conjugate(f)
eta = sp.diag(-1, 1, 1, 1)
X = (t, x, sp.Symbol('y'), sp.Symbol('zz'))
def T00(g, h):
    dg = [sp.diff(g, v) for v in X]; dh = [sp.diff(h, v) for v in X]
    contr = sum(eta[i, i]*dg[i]*dh[i] for i in range(4))
    return sp.simplify(dg[0]*dh[0] - sp.Rational(1, 2)*eta[0, 0]*contr)
K00 = w/(2*L**3)
theta_expr = w*x - w*t          # theta = k_rho x^rho with signature (-+++)
Tff, Tffc, Tfcf, Tfcfc = T00(f, f), T00(f, fc), T00(fc, f), T00(fc, fc)
rec("(2.12) T00[f,f] = -K00 e^{2i theta}", sp.simplify(Tff + K00*sp.exp(2*sp.I*theta_expr)) == 0)
rec("(2.13) T00[f*,f] = T00[f,f*] = K00", sp.simplify(Tffc - K00) == 0 and sp.simplify(Tfcf - K00) == 0)
rec("(2.14) T00[f*,f*] = -K00 e^{-2i theta}", sp.simplify(Tfcfc + K00*sp.exp(-2*sp.I*theta_expr)) == 0)

# ---- 2. normal ordering by commutative map: b = a^dagger, a = a ; T00 = sum over phi phi
K = sp.symbols('K', positive=True)
zt = sp.exp(2*sp.I*th)
a_, b_ = sp.symbols('a b')    # commuting stand-ins: normal-ordered monomial b^m a^n
T_lin = a_**2*(-K*zt) + a_*b_*(K) + b_*a_*(K) + b_**2*(-K/zt)   # T[phi,phi], phi = a f + a+ f*
NT1 = sp.expand(T_lin)
NT2 = sp.expand(T_lin**2)        # :T00 T00: -- normal ordering of the product
def to_op(P, N):
    A = sp.zeros(N, N)
    for i in range(N-1):
        A[i, i+1] = sp.sqrt(i+1)
    Ad = A.T
    M = sp.zeros(N, N)
    for (m, n), c in sp.Poly(P, b_, a_).terms():
        M += c*(Ad**m)*(A**n)
    return M
def expect(P, N):
    psi = sp.zeros(N, 1); psi[0] = 1; psi[2] = eps
    psi = psi/sp.sqrt(1 + eps**2)
    M = to_op(P, N)
    return sp.simplify((psi.H*M*psi)[0].rewrite(sp.cos))
rho9, rho12 = expect(NT1, 9), expect(NT1, 12)
T2_9, T2_12 = expect(NT2, 9), expect(NT2, 12)
rec("truncation independent (N=9 vs 12), <:T:> and <:T^2:>",
    sp.simplify(rho9 - rho12) == 0 and sp.simplify(T2_9 - T2_12) == 0)
rho, T2 = sp.simplify(rho9), sp.simplify(T2_9)
N_ = 1 + eps**2
c2 = sp.cos(2*th)
Xq = 2*eps - sp.sqrt(2)*c2
mid = eps/N_*(sp.sqrt(2)*(-K*zt - K/zt) + 2*eps*(2*K))
final = K*eps/N_*Xq
rec("(2.16) middle line exact", sp.simplify((mid - rho).rewrite(sp.cos)) == 0)
rec("(2.16) final line exact", sp.simplify(final - rho) == 0)
rec("(2.16) final / exact", str(sp.simplify(final/rho)))
kf37 = K**2*12*eps**2/N_**2
kf37_first = 2*eps**2/N_**2*6*K**2     # six products each = K00^2 (e^{+-2i th} cancel)
exact37 = sp.simplify(T2)
rec("exact <:T00^2:> (vac+2)", str(exact37))
rec("exact <:T00^2:> == 12 K^2 eps^2/(1+eps^2)", sp.simplify(exact37 - 12*K**2*eps**2/N_) == 0)
rec("KF (3.7) first line == second line (internal)", sp.simplify(kf37_first - kf37) == 0)
rec("KF (3.7) exact", sp.simplify(kf37 - exact37) == 0)
rec("KF (3.7) printed / exact", str(sp.simplify(kf37/exact37)))
six = [Tfcfc*Tff, Tfcf*Tfcf, Tfcf*Tffc, Tffc*Tfcf, Tffc*Tffc, Tff*Tfcfc]
rec("six bilinear products of (3.7) first line sum to 6 K00^2", sp.simplify(sum(six) - 6*K00**2) == 0)

# ---- 3. Delta, KF (3.2) with its absolute value
def Delta(r, q):
    return sp.Abs((q - r**2)/q)
Dx = sp.simplify(1 - rho**2/T2)
closed = 1 - Xq**2/(3*N_)
rec("exact 1 - rho^2/<T^2> == 1 - (2eps - sqrt2 cos2th)^2/(3(1+eps^2))", sp.simplify(Dx - closed) == 0)
kf38 = (10*eps + sp.sqrt(2)*c2)/(12*eps)
rec("KF (3.8) == 1 - (2eps - sqrt2 cos2th)/(12 eps)  [linear in X]", sp.simplify(kf38 - (1 - Xq/(12*eps))) == 0)
combos = {}
for n16, r in (("2.16printed", final), ("2.16exact", rho)):
    for n37, q in (("3.7printed", kf37), ("3.7exact", exact37)):
        d = sp.simplify(1 - r**2/q)
        combos[n16 + "+" + n37] = {"1-rho^2/T2": str(d),
                                  "equals_KF38": sp.simplify(d - kf38) == 0}
rec("any (2.16)x(3.7) combination, printed or exact, reproduces (3.8)",
    any(v["equals_KF38"] for v in combos.values()))
out["combos"] = combos
cs = sp.symbols('c', real=True)
for k_, v in combos.items():
    pass
deg_kf = sp.Poly(sp.expand(kf38.subs(c2, cs)*12*eps), cs).degree()
deg_ex = sp.Poly(sp.expand(closed.subs(c2, cs)*3*N_), cs).degree()
rec("degree in cos2th: KF (3.8) / exact Delta", (deg_kf, deg_ex))

# witness
at = {eps: sp.Rational(1, 10), th: 0}
rec("witness eps=1/10, th=0: exact Delta", round(float(sp.Abs(Dx).subs(at)), 4))
rec("witness eps=1/10, th=0: KF (3.8)", round(float(kf38.subs(at)), 4))
rec("witness eps=1/10, th=0: rho/K < 0", float((rho/K).subs(at)) < 0)
at2 = {eps: sp.Rational(1, 10), th: sp.pi/2}
rec("KF (3.8) at eps=1/10, th=pi/2 (cos2th=-1)", round(float(kf38.subs(at2)), 4))
at3 = {eps: 1, th: sp.pi/2}
rec("unsigned 1 - rho^2/T2 at eps=1, th=pi/2 (rho>0)", round(float(Dx.subs(at3)), 4))
rec("  KF (3.2) |.| there", round(float(sp.Abs(Dx).subs(at3)), 4))
# eps < 0 is theta -> theta + pi/2
rec("eps -> -eps equals th -> th + pi/2 in Delta", sp.simplify(closed.subs(eps, -eps) - closed.subs(th, th + sp.pi/2)) == 0)

# ---- 4. z3 on the reals: e = eps > 0, c = cos 2th in [-1,1], q = sqrt2
e, c, q = z3.Reals('e c q')
base = [q > 0, q*q == 2, c >= -1, c <= 1, e > 0]
Xz = 2*e - q*c
def sat(extra):
    s = z3.Solver(); s.add(*base, *extra); r = s.check()
    return str(r), (s.model() if r == z3.sat else None)
r, mdl = sat([10*e + q*c < 0])                      # KF (3.8) < 0
rec("z3: exists eps>0, |c|<=1 with KF (3.8) < 0 (contradicts |.| of (3.2))", r)
out["z3_kf38_negative_model"] = str(mdl)
r, _ = sat([Xz > 0, Xz*Xz > 3*(1 + e*e)])           # unsigned tree form < 0, rho>0
rec("z3: unsigned exact form < 0 somewhere with rho > 0", r)
r, _ = sat([Xz < 0, Xz*Xz >= 3*(1 + e*e)])          # ... with rho < 0 ?
rec("z3: unsigned exact form <= 0 anywhere with rho < 0 (expect unsat)", r)
r, _ = sat([Xz < 0, z3.Not(z3.And(Xz*Xz < 2*(1 + e*e), Xz*Xz > 0))])
rec("z3: rho<0 => 1/3 < Delta < 1 counterexample (expect unsat)", r)
r, _ = sat([Xz < 0, z3.Not(12*e - Xz > 12*e)])      # KF(3.8)>1 <=> -X>0
rec("z3: rho<0 and KF(3.8) <= 1 (expect unsat: (3.8)>1 iff rho<0)", r)
r, _ = sat([Xz > 0, 12*e - Xz > 12*e])
rec("z3: rho>0 and KF(3.8) > 1 (expect unsat)", r)

json.dump(out, open(sys.argv[1] if len(sys.argv) > 1 else "/dev/null", "w"), indent=1, default=str)
