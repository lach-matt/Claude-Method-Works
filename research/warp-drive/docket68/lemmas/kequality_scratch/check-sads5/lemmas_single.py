#!/usr/bin/env python3
"""Independent single-plane lemmas (own derivation; sympy exact).
Units L (slab AdS radius) = 1 unless stated. u = 1/a^2. tau = kappa^2 sigma / 6.
F(u) = f(a)/a^2 = k u + 1/L^2 - mu u^2 (+ Q u^3, Q = q^2).
A side's signed root s = eta sqrt(F).  Plane static & pure tension  <=>  sum s = -2 tau  and  sum F'/(2 s) = 0.
"""
import sympy as sp

u, mu, Q, tau, k, L = sp.symbols('u mu Q tau k L', real=True)
up = sp.Symbol('u', positive=True)

def F(kk, mu_, L2inv=1, Q_=0, uu=u):
    return kk*uu + L2inv - mu_*uu**2 + Q_*uu**3

out = {}
# ---- L1: mirrored plane at RS value of its adjacent bulk: s = -tau, both sides same => F = tau^2, F' = 0, tau = 1/L = 1
for kk in (1, 0, -1):
    eqs = [F(kk, mu) - 1, sp.diff(F(kk, mu), u)]
    sol = sp.solve(eqs, [u, mu], dict=True)
    adm = [s for s in sol if sp.sympify(s.get(u, u)).is_positive]
    print("L1 k=%2d: solutions %s ; with u>0: %s" % (kk, sol, adm))
    # also: as polynomial ideal
    G = sp.groebner([sp.expand(e) for e in eqs], u, mu, order='lex')
    print("       groebner:", list(G))
# closed form: stationary u* = k/(2 mu), F(u*) - 1 = k^2/(4 mu)
us = k/(2*mu)
print("L1 closed form F(u*)-1 =", sp.simplify(F(k, mu, uu=us) - 1))

# ---- C1: mirrored, tau free, k=1: F = tau^2, F'=0
sol = sp.solve([F(1, mu) - tau**2, sp.diff(F(1, mu), u)], [u, mu], dict=True)
print("C1 general:", sol)
s = sol[0]
print("C1 at tau = 11/10:", {kk: sp.nsimplify(v.subs(tau, sp.Rational(11, 10))) for kk, v in s.items()},
      " a^2 = 1/u =", sp.simplify(1/s[u]).subs(tau, sp.Rational(11, 10)),
      " 2 mu =", (2*s[mu]).subs(tau, sp.Rational(11, 10)))
muC = s[mu].subs(tau, sp.Rational(11, 10)); aC2 = 1/s[u].subs(tau, sp.Rational(11, 10))
Rh2 = (-1 + sp.sqrt(1 + 4*muC))/2
print("    horizon R_h^2 =", sp.nsimplify(Rh2), "=", float(Rh2), " a^2 =", aC2, float(aC2), " outside horizon:", aC2 > Rh2)
print("    sqrt F at the plane =", sp.sqrt(F(1, muC, uu=1/aC2)), "(= tau, so eta=-1 consistent)")
# stability: V(a) for adot^2 + V = 0 with adot^2 = a^2 (tau^2 - F(1/a^2))
a = sp.Symbol('a', positive=True)
V = -a**2*(sp.Rational(121, 100) - F(1, muC, uu=1/a**2))
print("    V(a*) =", sp.simplify(V.subs(a, sp.sqrt(aC2))), " V'(a*) =", sp.simplify(sp.diff(V, a).subs(a, sp.sqrt(aC2))),
      " V''(a*) =", sp.simplify(sp.diff(V, a, 2).subs(a, sp.sqrt(aC2))), "(negative = unstable)")
# subcritical tau < 1 at k=1: mu<0 ; k=-1:
for kk in (1, -1):
    sol = sp.solve([F(kk, mu) - tau**2, sp.diff(F(kk, mu), u)], [u, mu], dict=True)
    print("C1 k=%d general:" % kk, sol)

# ---- L2: two-sided plane at RS value (tau=1, L=1 both sides, both decaying), masses mp, mm free
mp, mm, sp_, sm_ = sp.symbols('m_p m_m s_p s_m', real=True)
for kk in (1, 0, -1):
    eqs = [sp_**2 - F(kk, mp), sm_**2 - F(kk, mm), sp_ + sm_ + 2,
           sp.diff(F(kk, mp), u)*sm_ + sp.diff(F(kk, mm), u)*sp_]
    G = sp.groebner([sp.expand(e) for e in eqs], sp_, sm_, mp, mm, u, order='lex')
    print("L2 k=%2d groebner (lex s_p>s_m>m_p>m_m>u), last elements:" % kk, [g for g in G][-3:])
# L2 k=-1 parametrisation by Delta = mp - mm
D = sp.Symbol('Delta', real=True)
eqs = [sp_**2 - F(-1, mp), sm_**2 - F(-1, mm), sp_ + sm_ + 2,
       sp.diff(F(-1, mp), u)*sm_ + sp.diff(F(-1, mm), u)*sp_, mp - mm - D]
G = sp.groebner([sp.expand(e) for e in eqs], sp_, sm_, mp, mm, u, D, order='lex')
for g in G:
    if g.free_symbols <= {u, D}:
        print("  relation u, Delta:", sp.factor(g))
# with mm = 0 (far side corridor-free), RS value: what slab mass is required?
eqs0 = [sp_**2 - F(-1, mp), sm_**2 - F(-1, 0), sp_ + sm_ + 2,
        sp.diff(F(-1, mp), u)*sm_ + sp.diff(F(-1, 0), u)*sp_]
sol = sp.solve(eqs0, [sp_, sm_, mp, u], dict=True)
print("L2 k=-1 with far side mu=0:", [s_ for s_ in sol if all(v.is_real for v in s_.values())])
