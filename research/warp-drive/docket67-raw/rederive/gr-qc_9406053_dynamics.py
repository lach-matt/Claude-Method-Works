#!/usr/bin/env python3
"""DOCKET 67 -- audit of gr-qc/9406053#dynamics (Borde 1994, Theorem 3 and its
abstract sentence "in dimensions >= 3 causally compact topology-changing
spacetimes cannot satisfy Einstein's equation (with a reasonable source)").

Reads only: the cached full text of gr-qc/9406053v1 (scratchpad d67/src,
md5 17c67ada52d92fc44065246ef92fee8c) and research/warp-drive/create.py
(read-only).  Writes nothing.  Exit 0 iff every check comes out as recorded.

  D1  the tree's quotation against the abstract (verbatim test)
  D2  Einstein's equation with Lambda: R_ab U^a U^b = k T_ab U^a U^b for null U,
      n = 3..6 (Borde Sec. V.A: "holds even if there is a cosmological constant")
  D3  Sec. VI lemma: T(V,V) >= K for every unit timelike V  =>  T(U,U) >= 0
  D4  Sec. V.A, n = 3: at most 4 null directions with R_ab U^a U^b = 0 (quartic)
  D5  focusing coefficient 1/(n-2): the blow-up time (n-2)/|theta0|; n = 2 has none
  D6  what 'reasonable' excludes: a static throat's source violates assumption (ii)
      (general zero-redshift throat, identity; Ellis throat, exact numbers)
  D7  z3: the theorem as a propositional skeleton -- the tree's unconditional
      reading does not follow; the contrapositive (creation => (i) or (ii) fails)
      does
"""
import hashlib
import re
import sys

import sympy as sp

D67 = "/tmp/claude-0/-home-user-Claude-Method-Works/6d820e7d-6d3c-5ac7-8067-527dc14c2847/scratchpad/d67/"
SRC = D67 + "src/gr-qc_9406053.txt"
CREATE = "/home/user/Claude-Method-Works/research/warp-drive/create.py"
FAIL = []


def chk(label, got, want):
    ok = (got == want)
    print("  [%s] %s: %s" % ("ok" if ok else "FAIL", label, got))
    if not ok:
        FAIL.append(label)


def norm(s):
    s = s.replace("’", "'").replace("≥", ">=")
    return re.sub(r"\s+", " ", s).strip()


# ---------------------------------------------------------------- D1
print("D1  quotation vs source")
raw = open(SRC, "rb").read()
chk("cached source md5", hashlib.md5(raw).hexdigest(), "17c67ada52d92fc44065246ef92fee8c")
txt = raw.decode("utf-8")
ntxt = norm(txt)
sys.path.insert(0, "/home/user/Claude-Method-Works/research/warp-drive")
src_create = open(CREATE).read()
m = re.search(r'BORDE_DYNAMICS = \((.*?)\)\n', src_create, re.S)
tree_q = norm("".join(re.findall(r'"([^"]*)"', m.group(1))))
print("      tree:", tree_q)
chk("BORDE_DYNAMICS occurs verbatim in the abstract (after >= and whitespace normalisation)",
    tree_q in ntxt, True)
chk("the abstract continues with 'i.e., there are severe dynamical obstructions'",
    (tree_q + "; i.e., there are severe dynamical obstructions to topology change") in ntxt, True)
thm3 = norm(txt[txt.index("Theorem 3: Let M"):txt.index("It is important to note that this result")])
print("      Theorem 3 (as extracted):", thm3[:400], "...")
chk("Theorem 3 names 'causally compact interpolating space- time of dimension >= 3'",
    "causally compact interpolating space- time of dimension >= 3" in thm3, True)
chk("Theorem 3's conclusion includes 'S 1 and S 2 are connected'",
    "and S 1 and S 2 are connected" in thm3, True)
chk("Theorem 3 is stated on curvature (hypotheses i, ii), not on T_ab",
    ("T ab" not in thm3) and ("R b]ef" in thm3 or "R\nb]ef" in thm3 or "R b]ef [c" in thm3), True)
chk("Sec. IX.B names energy-condition violation large enough to break (ii) as a route",
    "violations of the energy conditions large enough to allow assumption (ii) to be violated" in ntxt, True)
chk("Sec. VI calls integral conditions for quantum sources 'wishful thinking'",
    "This is so far only a piece of wishful think- ing" in ntxt or "only a piece of wishful thinking" in ntxt, True)
chk("Sec. IX.B: weakening the curvature constraints 'would not affect the presence of causality violations'",
    "This would not affect the presence of causality violations" in ntxt, True)

# ---------------------------------------------------------------- D2
print("D2  Einstein's equation + Lambda, contracted on a null vector")
k, Lam = sp.symbols("k Lambda")
for n in range(3, 7):
    eta = sp.diag(*([-1] + [1] * (n - 1)))
    Rm = sp.Matrix(n, n, lambda i, j: sp.Symbol("R_%d%d" % (min(i, j), max(i, j))))
    Rs = sum((eta.inv()[i, j] * Rm[i, j] for i in range(n) for j in range(n)))
    T = (Rm - Rs / 2 * eta + Lam * eta) / k          # T defined by the field equation
    U = sp.Matrix([1, 1] + [0] * (n - 2))
    lhs = (U.T * Rm * U)[0]
    rhs = k * (U.T * T * U)[0]
    chk("n=%d: R_UU - k T_UU == 0 (Lambda drops)" % n, sp.simplify(lhs - rhs), 0)

# ---------------------------------------------------------------- D3
print("D3  Sec. VI: energy density bounded below by K (any sign) => null convergence")
T00, T01, T11, K, eta_ = sp.symbols("T00 T01 T11 K eta", real=True)
# unit timelike V = (cosh, sinh); T(V,V) >= K  <=>  T00 + 2T01 tanh + T11 tanh^2 >= K sech^2
lhs = T00 + 2 * T01 * sp.tanh(eta_) + T11 * sp.tanh(eta_) ** 2
rhs = K / sp.cosh(eta_) ** 2
chk("limit eta->oo of the scaled inequality gives T00+2T01+T11 >= 0 = T(U,U), U=(1,1)",
    (sp.limit(lhs, eta_, sp.oo), sp.limit(rhs, eta_, sp.oo)), (T00 + 2 * T01 + T11, 0))
# counter-direction: K>0 is not needed; T = C g is Borde's formal example
C = sp.Symbol("C", real=True)
g2 = sp.diag(-1, 1)
Vb = sp.Matrix([sp.cosh(eta_), sp.sinh(eta_)])
chk("T = C g: T(V,V) = -C for every unit timelike V (bounded below), T(U,U) = 0",
    (sp.simplify((Vb.T * (C * g2) * Vb)[0]), (sp.Matrix([1, 1]).T * (C * g2) * sp.Matrix([1, 1]))[0]),
    (-C, 0))

# ---------------------------------------------------------------- D4
print("D4  Sec. V.A, n = 3: R_UU = 0 is a quartic in beta")
b = sp.Symbol("beta")
# basis P, M null, P.M = -1, S unit spacelike orthogonal; components in (P, M, S)
G = sp.Matrix([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])
Uv = sp.Matrix([1, b ** 2 / 2, b])
chk("U = P + (beta^2/2) M + beta S is null", sp.expand((Uv.T * G * Uv)[0]), 0)
Rsym = sp.Matrix(3, 3, lambda i, j: sp.Symbol("r%d%d" % (min(i, j), max(i, j))))
poly = sp.Poly(sp.expand((Uv.T * Rsym * Uv)[0]), b)
chk("degree 4, leading coefficient R_MM/4", (poly.degree(), poly.LC()), (4, Rsym[1, 1] / 4))
poly3 = sp.Poly(sp.expand((Uv.T * Rsym.subs(Rsym[1, 1], 0) * Uv)[0]), b)
chk("R_MM = 0: degree 3 (plus the direction M itself) -> at most 4 null directions", poly3.degree(), 3)

# ---------------------------------------------------------------- D5
print("D5  focusing: d theta/du = -theta^2/(n-2) - R_UU - 2 sigma^2")
u, th0, nn = sp.symbols("u theta0 n", real=True)
th = sp.Function("theta")
sol = sp.dsolve(sp.Eq(th(u).diff(u), -th(u) ** 2 / (nn - 2)), th(u), ics={th(0): th0})
chk("shear-free, R_UU = 0 solution", sp.simplify(sol.rhs - (nn - 2) * th0 / (th0 * u + nn - 2)), 0)
chk("blow-up at u* = -(n-2)/theta0 (finite for theta0 < 0 when n >= 3)",
    sp.solve(sp.denom(sp.together(sol.rhs)), u), [(2 - nn) / th0])
chk("n = 2: coefficient 1/(n-2) undefined (no transverse space; Borde states the lemma for n > 2)",
    (1 / (nn - 2)).subs(nn, 2) == sp.zoo, True)

# ---------------------------------------------------------------- D6
print("D6  what 'reasonable' (assumption ii) excludes: a static throat")
t, l, th_, ph = sp.symbols("t l th ph", real=True)
r = sp.Function("r")(l)
x = [t, l, th_, ph]
g = sp.diag(-1, 1, r ** 2, r ** 2 * sp.sin(th_) ** 2)   # zero-redshift throat
gi = g.inv()
N = 4
Gam = [[[sum(gi[a, d] * (g[d, bb].diff(x[c]) + g[d, c].diff(x[bb]) - g[bb, c].diff(x[d]))
             for d in range(N)) / 2 for c in range(N)] for bb in range(N)] for a in range(N)]


def ricci(bb, c):
    return sp.simplify(sum(Gam[a][bb][c].diff(x[a]) - Gam[a][bb][a].diff(x[c])
                           + sum(Gam[a][a][e] * Gam[e][bb][c] - Gam[a][c][e] * Gam[e][bb][a]
                                 for e in range(N)) for a in range(N)))


kv = [1, 1, 0, 0]
acc = [sp.simplify(sum(Gam[a][bb][c] * kv[bb] * kv[c] for bb in range(N) for c in range(N)))
       for a in range(N)]
chk("radial k = (1,1,0,0) is an affinely parametrised null geodesic (u = t = l)",
    (sp.simplify(sum(g[i, j] * kv[i] * kv[j] for i in range(N) for j in range(N))), acc), (0, [0, 0, 0, 0]))
Rkk = sp.simplify(sum(ricci(i, j) * kv[i] * kv[j] for i in range(2) for j in range(2)))
chk("R_ab k^a k^b = -2 r''/r", sp.simplify(Rkk + 2 * r.diff(l, 2) / r), 0)
q = r.diff(l) / r
chk("identity r''/r = (r'/r)' + (r'/r)^2  => INT R_kk = -2[r'/r] - 2 INT (r'/r)^2",
    sp.simplify(r.diff(l, 2) / r - (q.diff(l) + q ** 2)), 0)
print("      so, from the far past (r'/r -> 0) to the throat (r' = 0): INT_{-oo}^{0} R_kk du"
      " = -2 INT (r'/r)^2 < 0 for EVERY zero-redshift throat")
b0 = sp.Symbol("b0", positive=True)
rE = sp.sqrt(b0 ** 2 + l ** 2)                       # Ellis throat
RkkE = sp.simplify((-2 * r.diff(l, 2) / r).subs(r, rE).doit())
chk("Ellis: R_kk = -2 b0^2/(b0^2+l^2)^2", sp.simplify(RkkE + 2 * b0 ** 2 / (b0 ** 2 + l ** 2) ** 2), 0)
full = sp.integrate(RkkE, (l, -sp.oo, sp.oo))
half = sp.integrate(RkkE, (l, -sp.oo, 0))
chk("Ellis: INT over the whole geodesic = -pi/b0 (ANEC violated)", sp.simplify(full), -sp.pi / b0)
chk("Ellis: INT from -oo to the throat = -pi/(2 b0)", sp.simplify(half), -sp.pi / (2 * b0))
# assumption (ii) at u0 = 0 (the throat): for delta < INT_{-b0}^{0}|R_kk|, every u <= -b0
# has INT_u^0 R_kk du <= INT_{-b0}^0 R_kk du < -delta, so no interval I with sup I < u1 = -b0 exists.
w = sp.simplify(sp.integrate(RkkE, (l, -b0, 0)))
chk("Ellis: INT_{-b0}^{0} R_kk = -(pi+2)/(4 b0) < 0", sp.simplify(w + (sp.pi + 2) / (4 * b0)), 0)
chk("R_kk < 0 everywhere, so INT_u^0 is monotone: (ii) FAILS at u0 = 0 with delta = (pi+2)/(8 b0)",
    (sp.solve(sp.Eq(RkkE, 0), l), bool(RkkE.subs({l: 0, b0: 1}) < 0)), ([], True))

# ---------------------------------------------------------------- D7
print("D7  z3: Theorem 3 as a propositional skeleton")
try:
    import z3
except ImportError:
    print("  z3 missing: pip install z3-solver"); FAIL.append("z3"); z3 = None
if z3:
    cc, d3, gi_, hi, to, sm, tc, ein, reas = z3.Bools("cc dim3 gen_i halfint_ii timeoriented smooth topchange einstein reasonable")
    thm3 = z3.Implies(z3.And(to, sm, cc, d3, gi_, hi), z3.Not(tc))
    # Borde: 'reasonable' = the source restriction that yields (i) and (ii) via Einstein's equation
    reas_def = z3.Implies(z3.And(ein, reas), z3.And(gi_, hi))

    def proves(prem, concl):
        s = z3.Solver(); s.add(prem); s.add(z3.Not(concl))
        return str(s.check())
    chk("theorem + definition |- (cc & dim3 & Einstein & reasonable & smooth & to) -> no topology change",
        proves(z3.And(thm3, reas_def), z3.Implies(z3.And(to, sm, cc, d3, ein, reas), z3.Not(tc))), "unsat")
    chk("but NOT (cc & dim3 & Einstein) -> no topology change: the source restriction is load-bearing",
        proves(z3.And(thm3, reas_def), z3.Implies(z3.And(to, sm, cc, d3, ein), z3.Not(tc))), "sat")
    chk("contrapositive: topology change & cc & dim3 & smooth & to -> (i) fails or (ii) fails",
        proves(thm3, z3.Implies(z3.And(tc, cc, d3, sm, to), z3.Or(z3.Not(gi_), z3.Not(hi)))), "unsat")
    chk("without time-orientation or smoothness, the theorem is silent",
        (proves(thm3, z3.Implies(z3.And(cc, d3, gi_, hi, sm), z3.Not(tc))),
         proves(thm3, z3.Implies(z3.And(cc, d3, gi_, hi, to), z3.Not(tc)))), ("sat", "sat"))

print()
print("FAILED: %s" % FAIL if FAIL else "ALL CHECKS AS RECORDED")
sys.exit(1 if FAIL else 0)
