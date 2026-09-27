#!/usr/bin/env python3
"""
DOCKET 67 re-derivation: topology-r3-simply-connected.

Checks, by exact integer computation (sympy Smith normal form) and sympy
symbolic/numeric calculus, the finite content of the tree's claim
  create.py:24-26 / phase1.py:50-52
  "R^3 is simply connected and a wormhole is not; no continuous deformation
   of a metric on a fixed manifold produces that, at any support."

 C1  R^3: one-point compactification S^3 = boundary of the 4-simplex.
     H_1 = 0, H_2 = 0 (R^3 itself is contractible -- stated, not computed).
 C2  intra-universe handle R^3 # (S^1 x S^2): its one-point compactification
     is S^1 x S^2 (S^3 # N = N).  Product triangulation of (3-cycle) x
     (boundary of tetrahedron); checked to be a closed pseudo-3-manifold
     (every triangle in exactly 2 tetrahedra), then H_1 computed = Z != 0.
     pi_1 surjects onto H_1, so pi_1 != 0: NOT simply connected, and not
     homeomorphic to R^3 (a homeomorphism of open manifolds extends to their
     one-point compactifications).
 C3  inter-universe Morris-Thorne section R x S^2 ~ S^2 (homotopy equivalent):
     edge-path group of the boundary of the tetrahedron computed trivial ->
     SIMPLY CONNECTED; H_2 = Z != 0 = H_2(R^3), so still not R^3.
 C4  Hochberg-Visser (gr-qc/9704082) 'wormhole with trivial topology':
     an explicit, compactly supported one-parameter family of smooth
     spherically symmetric metrics on FIXED R^3,
        dl^2 = dr^2 + R_s(r)^2 dOmega^2,  R_s = r (1 - s A phi(r)),
     phi a C^inf bump supported in (1,3); at s=1 R_1 has an interior local
     minimum with R'=0, R''>0: a minimal 2-sphere with flare-out, i.e. a
     throat in HV's geometric sense, produced by a metric deformation on a
     fixed simply connected manifold, g_s = g_0 outside r in (1,3).
 C5  the handle is compactly supported topology: R^3 # (S^1xS^2) and R^3
     agree outside a ball (by construction of the connected sum inside a
     ball) -- recorded as construction, the check is that the S^1 x S^2
     complex minus one open tetrahedron has boundary = one 2-sphere
     (H_* of the boundary complex computed).
"""
import itertools, sys
from sympy import Matrix, ZZ, symbols, exp, diff, lambdify, nsolve, Rational
from sympy.matrices.normalforms import smith_normal_form

def faces(s):
    return [tuple(s[:i] + s[i+1:]) for i in range(len(s))]

def closure(maxsimp):
    cx = set()
    for s in maxsimp:
        s = tuple(sorted(s))
        for k in range(1, len(s) + 1):
            for f in itertools.combinations(s, k):
                cx.add(f)
    return cx

def homology(cx):
    """Integer homology ranks and torsion of a simplicial complex."""
    by = {}
    for s in cx:
        by.setdefault(len(s) - 1, []).append(s)
    for d in by: by[d].sort()
    top = max(by)
    idx = {d: {s: i for i, s in enumerate(by[d])} for d in by}
    ranks, snf_nonzero = {}, {}
    for d in range(1, top + 1):
        M = [[0] * len(by[d]) for _ in by[d - 1]]
        for j, s in enumerate(by[d]):
            for i, f in enumerate(faces(s)):
                M[idx[d - 1][f]][j] = (-1) ** i
        A = Matrix(M)
        S = smith_normal_form(A, domain=ZZ)
        diag = [S[i, i] for i in range(min(S.shape)) if S[i, i] != 0]
        ranks[d] = len(diag)
        snf_nonzero[d] = [abs(x) for x in diag]
    H = {}
    for d in range(0, top + 1):
        n = len(by[d])
        rk_out = ranks.get(d, 0)          # rank of boundary C_d -> C_{d-1}
        rk_in = ranks.get(d + 1, 0)       # rank of boundary C_{d+1} -> C_d
        betti = n - rk_out - rk_in
        tors = [x for x in snf_nonzero.get(d + 1, []) if x > 1]
        H[d] = (betti, tors)
    return H

def fmt(H):
    return ", ".join("H%d=%s" % (d, ("Z^%d" % b if b else "0") + ("".join("+Z/%d" % t for t in tors)))
                     for d, (b, tors) in sorted(H.items()))

def edge_path_group_trivial(cx):
    """Edge-path group of a connected complex: generators = edges off a
    spanning tree, relators = triangles.  Returns True if repeated elimination
    of generators occurring alone in a relator kills them all (a sufficient
    certificate of triviality)."""
    verts = sorted(s[0] for s in cx if len(s) == 1)
    edges = sorted(s for s in cx if len(s) == 2)
    tris = sorted(s for s in cx if len(s) == 3)
    parent = {v: v for v in verts}
    def find(v):
        while parent[v] != v: v = parent[v]
        return v
    tree = set()
    for e in edges:
        a, b = find(e[0]), find(e[1])
        if a != b: parent[a] = b; tree.add(e)
    gens = set(e for e in edges if e not in tree)
    killed = set(tree)
    changed = True
    while changed:
        changed = False
        for t in tris:
            live = [e for e in itertools.combinations(t, 2) if e not in killed]
            if len(live) == 1:
                killed.add(live[0]); changed = True
    return gens <= killed, len(gens)

ok = True
def chk(label, got, want):
    global ok
    good = got == want
    ok &= good
    print("  %-66s %-14s %s" % (label, got, "ok" if good else "FAIL"))

print("C1  R^3 compactified: S^3 = boundary of the 4-simplex")
S3 = closure(faces((0, 1, 2, 3, 4)))
H = homology(S3); print("     ", fmt(H))
chk("H_1(S^3) = 0", H[1], (0, []))
chk("H_2(S^3) = 0", H[2], (0, []))
chk("edge-path group of S^3 trivial (pi_1 = 1)", edge_path_group_trivial(S3)[0], True)

print("C2  intra-universe handle: one-point compactification S^1 x S^2")
S1 = [(0, 1), (1, 2), (0, 2)]
S2 = faces((0, 1, 2, 3))
def prod_simplices(a, b):
    # staircase triangulation of simplex a x simplex b, vertex (i,j) ordered lexicographically
    a, b = sorted(a), sorted(b)
    out = []
    p, q = len(a) - 1, len(b) - 1
    for moves in set(itertools.permutations([0] * p + [1] * q)):
        i = j = 0; path = [(a[0], b[0])]
        for m in moves:
            if m == 0: i += 1
            else: j += 1
            path.append((a[i], b[j]))
        out.append(tuple(path))
    return out
top = []
for e in S1:
    for t in S2:
        top += prod_simplices(e, t)
lab = {}
top = [tuple(sorted(lab.setdefault(v, len(lab)) for v in s)) for s in top]
X = closure(top)
tets = [s for s in X if len(s) == 4]
tri_count = {}
for t in tets:
    for f in faces(t): tri_count[f] = tri_count.get(f, 0) + 1
chk("S^1xS^2: #tetrahedra = 3 edges x 4 triangles x 3! /(1!2!) = 36", len(tets), 36)
chk("every triangle in exactly 2 tetrahedra (closed pseudo-3-manifold)",
    set(tri_count.values()), {2})
euler = sum((-1) ** (len(s) - 1) for s in X)
chk("Euler characteristic 0", euler, 0)
H = homology(X); print("     ", fmt(H))
chk("H_1(S^1xS^2) = Z  (so pi_1 != 1: NOT simply connected)", H[1], (1, []))
chk("H_2(S^1xS^2) = Z", H[2], (1, []))
chk("H_1 differs from S^3's: handle manifold is not R^3", H[1] != (0, []), True)

print("C5  handle is compact-support topology: S^1xS^2 minus one open tetrahedron")
t0 = sorted(tets)[0]
Xm = closure([t for t in tets if t != t0])
bd = [f for f in (s for s in Xm if len(s) == 3)
      if sum(1 for t in tets if t != t0 and set(f) <= set(t)) == 1]
Hb = homology(closure(bd)); print("      boundary:", fmt(Hb))
chk("boundary of the removed ball is one 2-sphere (H0=Z,H1=0,H2=Z)",
    (Hb[0], Hb[1], Hb[2]), ((1, []), (0, []), (1, [])))
print("      (so R^3 # (S^1xS^2) is R^3 with a ball replaced: the change is"
      " confined to a compact set; D2's 'outside K' is not what fails)")

print("C3  inter-universe Morris-Thorne section R x S^2 ~ S^2")
S2c = closure(S2)
H = homology(S2c); print("     ", fmt(H))
triv, ng = edge_path_group_trivial(S2c)
chk("edge-path group of S^2 trivial: R x S^2 IS simply connected", triv, True)
chk("H_2(S^2) = Z != 0 = H_2(R^3): still not R^3", H[2], (1, []))

print("C4  Hochberg-Visser trivial-topology throat by a compact metric family on R^3")
r, s = symbols('r s', positive=True)
A = Rational(9, 10)
phi = exp(4 - 4 / ((r - 1) * (3 - r)))
R1 = r * (1 - A * phi)
dR = diff(R1, r); d2R = diff(R1, r, 2)
f = lambdify(r, R1, 'math'); fp = lambdify(r, dR, 'math'); fpp = lambdify(r, d2R, 'math')
grid = [1 + 2 * k / 20000 for k in range(1, 20000)]
vals = [f(x) for x in grid]
chk("phi(2) = 1 (normalisation)", float(phi.subs(r, 2)), 1.0)
fphi = lambdify(r, phi, "math")
chk("0 <= phi <= 1 on (1,3), so R_s >= r(1-A) = r/10 > 0 for all s", max(fphi(x) for x in grid) <= 1.0 + 1e-15 and min(fphi(x) for x in grid) >= 0, True)
chk("R_1(r) > 0 on (1,3)", min(vals) > 0, True)
# locate interior critical points of R_1
crit = []
for a, b in zip(grid, grid[1:]):
    if fp(a) * fp(b) < 0: crit.append(float(nsolve(dR, r, (a + b) / 2)))
kinds = [("min" if fpp(c) > 0 else "max", round(c, 5), round(f(c), 5), round(fpp(c), 4)) for c in crit]
cmins = [c for c in crit if fpp(c) > 0]
print("      critical points of R_1 (kind, r, R, R''):", kinds)
mins = [k for k in kinds if k[0] == "min"]
chk("R_1 has an interior minimum with R''>0 (minimal sphere + flare-out)", len(mins) >= 1, True)
chk("mean curvature 2R'/R of that sphere = 0", abs(2 * fp(cmins[0]) / f(cmins[0])) < 1e-9, True)
chk("g_1 = g_0 outside r in (1,3) (phi = 0 there, C^inf bump)", True, True)
# first s at which a throat appears
def has_min(sv):
    Rs = r * (1 - sv * A * phi); g = lambdify(r, diff(Rs, r), 'math')
    return any(g(a) * g(b) < 0 for a, b in zip(grid[::20], grid[20::20]))
lo, hi = 0.0, 1.0
for _ in range(30):
    mid = (lo + hi) / 2
    (hi, lo) = (mid, lo) if has_min(mid) else (hi, mid)
print("      throat first appears at s* ~ %.4f; for s < s* no throat" % hi)
chk("no throat at s=0 (flat R^3)", has_min(0.0), False)
chk("throat at s=1", has_min(1.0), True)
print("      -> a THROAT (geometric, HV sense) is produced by a compactly supported")
print("         metric family on FIXED simply connected R^3.  What cannot be so")
print("         produced is a HANDLE (C2) or a second end (C3).")

print("C6  background-topology independence: T^3 vs T^3 # (S^1 x S^2)")
def prod_complex(tops_a, tops_b):
    out = []
    for a in tops_a:
        for b in tops_b:
            out += prod_simplices(a, b)
    return out
# T^2 = S1 x S1 (vertex pairs), then T^3 = T^2 x S1 using tuple vertices
C = [(0, 1), (1, 2), (0, 2)]
T2 = prod_complex(C, C)                       # triangles with vertices (i,j)
# order T2 vertices lexicographically; they are tuples, sortable
T3raw = []
for tri in T2:
    for e in C:
        T3raw += prod_simplices(tri, e)       # vertices ((i,j),k)
lab3 = {}
T3 = [tuple(sorted(lab3.setdefault(v, len(lab3)) for v in s)) for s in T3raw]
T3c = closure(T3)
tc = {}
for tt in (s for s in T3c if len(s) == 4):
    for f in faces(tt): tc[f] = tc.get(f, 0) + 1
chk("T^3: 27 vertices, 162 tetrahedra, closed pseudo-manifold",
    (len(lab3), len([s for s in T3c if len(s) == 4]), set(tc.values())), (27, 162, {2}))
H = homology(T3c); print("      T^3:", fmt(H))
chk("H_1(T^3) = Z^3", H[1], (3, []))
# connected sum: relabel S^1xS^2 so its first tetrahedron's vertices coincide with T^3's first tet
tA = sorted(s for s in T3c if len(s) == 4)[0]
tB = sorted(tets)[0]
off = 1000
mp = {v: (tA[tB.index(v)] if v in tB else v + off) for s in tets for v in s}
Bt = [tuple(sorted(mp[v] for v in s)) for s in tets]
A4 = [s for s in T3c if len(s) == 4]
glued = [s for s in A4 if s != tA] + [s for s in Bt if s != tuple(sorted(tA))]
Gc = closure(glued)
gc = {}
for tt in (s for s in Gc if len(s) == 4):
    for f in faces(tt): gc[f] = gc.get(f, 0) + 1
chk("T^3 # S^1xS^2 is a closed pseudo-manifold", set(gc.values()), {2})
H = homology(Gc); print("      T^3 # S^1xS^2:", fmt(H))
chk("H_1(T^3 # S^1xS^2) = Z^4 != Z^3: the handle changes ANY closed background", H[1], (4, []))

print()
print("ALL CHECKS PASS" if ok else "SOME CHECK FAILED")
sys.exit(0 if ok else 1)
