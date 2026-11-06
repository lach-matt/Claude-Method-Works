#!/usr/bin/env python3
"""dustloss5.py -- FAMILIES5 4e (D490, written by verifier 209 on D488): what a null dust's first derivative
needs in the doubly-null split of [CTWG23] (Chrusciel-Tagne Wafo-Gray, arXiv:2305.07306), D488's suggested route.

Metric (4D for speed; the angular count does not matter):
    g = -2 W^2 du dv + a dx^2 + b dy^2,   W, a, b functions of (u, v, x, y).
Dust: T = K dv (x) dv, k = -grad v (null, tangent to v = const, along d/du).
Checks:
  1. nabla^mu T_{mu nu} = 0 reduces to one transport  d_u K = c K, and c contains
     d_u a, d_u b: c = -(1/2) d_u log(ab), minus the null expansion of the v = const surfaces (W drops out).
  2. d_x of that transport: d_u (d_x K) = c d_x K + (d_x c) K, and d_x c contains
     d_x d_u a, d_x d_u b: angular derivatives of a connection coefficient.
  3. The Bianchi source J ~ nabla_[k T_l]j (T trace-free) contains d_x K.
  4. Control: a dust with K = K(v, x, y) on a metric with u-independent a, b, W
     has d_x c = 0 (no connection derivative), so the d_x d_u terms are the expansion's.

The dust's transport brings the null expansion into c, and the transport of d_x K brings d_x c, an angular
derivative of a connection coefficient that is not among [CTWG23]'s unknowns (4.9)-(4.10); adding it needs the
derivative of the curvature and so of J, the dust's second derivatives, and so on. Shown at the level of the
equations, not as a no-go theorem. Labels: exact (sympy), on a 4D metric in double-null form (the angular count
does not matter).
"""
import sympy as sp

u, v, x, y = sp.symbols('u v x y')
X = [u, v, x, y]
W = sp.Function('W')(*X)
a = sp.Function('a')(*X)
b = sp.Function('b')(*X)
K = sp.Function('K')(*X)

g = sp.zeros(4)
g[0, 1] = g[1, 0] = -W**2
g[2, 2] = a
g[3, 3] = b
gi = sp.simplify(g.inv())

def christoffel(g, gi):
    G = [[[0]*4 for _ in range(4)] for _ in range(4)]
    for l in range(4):
        for m in range(4):
            for n in range(4):
                G[l][m][n] = sp.simplify(sum(gi[l, s]*(sp.diff(g[s, m], X[n]) + sp.diff(g[s, n], X[m])
                                                       - sp.diff(g[m, n], X[s])) for s in range(4))/2)
    return G

G = christoffel(g, gi)

# T_{mu nu} = K dv dv
T = sp.zeros(4)
T[1, 1] = K

# nabla_l T_{m n}
def covT(l, m, n):
    return sp.diff(T[m, n], X[l]) - sum(G[s][l][m]*T[s, n] + G[s][l][n]*T[m, s] for s in range(4))

divT = [sp.simplify(sum(gi[l, m]*covT(l, m, n) for l in range(4) for m in range(4))) for n in range(4)]
print("1. div T components (u, v, x, y):")
for n, e in enumerate(divT):
    print("   ", X[n], ":", sp.factor(e))
nonzero = [n for n, e in enumerate(divT) if sp.simplify(e) != 0]
assert nonzero == [1], nonzero          # only the v-component survives
sol = sp.solve(divT[1], sp.diff(K, u))[0]
c = sp.simplify(sol/K)
print("   d_u K = c K with c =", c)
assert c.has(sp.Derivative(a, u)) and c.has(sp.Derivative(b, u))

dxc = sp.expand(sp.diff(c, x))
print("2. d_x c =", sp.simplify(dxc))
need = [sp.Derivative(a, u, x), sp.Derivative(b, u, x)]
assert all(dxc.has(t) for t in need), "d_x c lacks the mixed derivatives"
print("   d_x c contains d_x d_u a and d_x d_u b: yes")

# trace of T: g^{mu nu} T_{mu nu} = g^{vv} K = 0
trT = sp.simplify(sum(gi[m, n]*T[m, n] for m in range(4) for n in range(4)))
assert trT == 0
# J_{j k l} ~ nabla_k T_{l j} - nabla_l T_{k j} (trace-free T, R_{mu nu} = T_{mu nu} up to a constant)
J = lambda j, k, l: sp.simplify(covT(k, l, j) - covT(l, k, j))
Jvxv = J(1, 2, 1)
print("3. J_{v x v} ~ nabla_x T_vv - nabla_v T_xv =", Jvxv)
assert Jvxv.has(sp.Derivative(K, x))

# 4. control: u-independent metric
W0 = sp.Function('W0')(v, x, y); a0 = sp.Function('a0')(v, x, y); b0 = sp.Function('b0')(v, x, y)
c0 = c.subs({W: W0, a: a0, b: b0}).doit()
print("4. control, u-independent metric: c =", sp.simplify(c0), "; d_x c =", sp.simplify(sp.diff(c0, x)))
assert sp.simplify(c0) == 0
print("ALL PASS")
