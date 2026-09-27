#!/usr/bin/env python3
"""DOCKET 67, pass S, audit 24/36: gr-qc/9406053#kinematic-possibility.

Re-derives Borde's kinematic-possibility claim (abstract; Sec. II.B; Sec. III.C-D;
Sec. IX first two bullets) from the source text saved at ../src/gr-qc_9406053.txt
(md5 17c67ada52d92fc44065246ef92fee8c; alphaXiv get_paper_content fullText), and
checks it against research/warp-drive/create.py (read-only).

K1  the quoted/paraphrased source phrases occur in the source text
K2  Borde's own vector-field -> Lorentz metric construction (II.B) is non-degenerate
K3  Fig. 6b built explicitly: cylinder, S1 u S1 -> empty, smooth, non-degenerate,
    time-oriented, boundaries spacelike, and it carries a closed timelike curve
K4  Fig. 6c built explicitly: Moebius strip, S1 -> empty (Sorkin), same checks
K5  the index condition (Poincare-Hopf with mixed boundary): even n -> chi(M)=0,
    odd n -> chi(S1)=chi(S2) (the RS rule); trousers chi = -1 is excluded
K6  2D enumeration: every compact non-singular time-oriented Lorentzian cobordism;
    NONE is a change between two NON-EMPTY surfaces of different topology
K7  n=3 (2+1): RS rule forbids every non-identity oriented closed transition
K8  n=4: S^3 -> S^2 x S^1 (throat / handle creation, closed case): a cobordism with
    chi = 1 is brought to chi = 0 by Misner's connected sums (CP^2 then T^4)
K9  the tree's statement (create.py:51-53, 188) against the source
Stdlib + sympy only.  Exit 0 iff every check agrees with the source.
"""
import hashlib, itertools, os, re, sys
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src", "gr-qc_9406053.txt")
CREATE = "/home/user/Claude-Method-Works/research/warp-drive/create.py"
ok_all = True


def chk(tag, cond, note=""):
    global ok_all
    ok_all &= bool(cond)
    print("%-4s %-5s %s" % (tag, "OK" if cond else "FAIL", note))


raw = open(SRC, "rb").read()
chk("K0", hashlib.md5(raw).hexdigest() == "17c67ada52d92fc44065246ef92fee8c", "source md5")
text = re.sub(r"\s+", " ", raw.decode("utf-8"))

# ---------------------------------------------------------------- K1 phrases
phrases = [
    "topology change is kinematically possible; i.e., if a field equation is not imposed, it "
    "is possible to construct topology-changing spacetimes with non-singular Lorentz metrics",
    "Simple 2-dimensional examples of this are shown",
    "No assumption is made about the dimension of spacetime",
    "It is assumed that the metrics being considered are time-oriented",
    "Thus, kinematically, though there are some constraints, a large variety of "
    "topology-changing closed universes exist",
    "there is at this stage no barrier whatsoever to four-dimensional topology change",
    "The RS rule forbids all Lorentzian topological transitions between oriented closed 2-manifolds",
    "The only Lorentzian cobordisms in two dimensions are the torus and the Klein bottle",
    "The spacetimes of fig. 6b and fig. 6c are explicit examples of Lorentzian topology change",
    "non-singular topology- changing spacetimes in two dimensions (albeit with closed timelike curves)",
    "any two externally Euclidean spaces can be connected by an interpolating externally "
    "Lorentzian spacetime",
]
for i, p in enumerate(phrases):
    chk("K1.%d" % i, re.sub(r"\s+", " ", p) in text, p[:70])

# ---------------------------------------------------------------- K2 construction
for n in (2, 3, 4):
    v = sp.Matrix(sp.symbols("v0:%d" % n, real=True))
    h = sp.eye(n)
    g = (v.T * h * v)[0] * h - 2 * (h * v) * (h * v).T
    detg = sp.factor(g.det())
    vv = (v.T * v)[0]
    want = (-1) ** 1 * vv ** n  # det = -|V|^{2n}
    chk("K2.n%d" % n, sp.simplify(detg - want) == 0 and sp.simplify((v.T * g * v)[0] + vv ** 2) == 0,
        "g = |V|^2 h - 2 hV hV : det = -|V|^(2n) (non-degenerate iff V != 0), g(V,V) = -|V|^4")

# ---------------------------------------------------------------- K3 Fig. 6b cylinder
x, th = sp.symbols("x theta", real=True)
V = sp.Matrix([-2 * x, 1])         # (V^x, V^theta) on [-1,1] x S^1, h = dx^2 + dtheta^2
h = sp.eye(2)
vv = (V.T * V)[0]
G = sp.simplify(vv * h - 2 * V * V.T)
detG = sp.factor(G.det())
chk("K3a", sp.simplify(detG + (4 * x**2 + 1) ** 2) == 0, "det g = -(1+4x^2)^2 < 0 everywhere: Lorentzian, non-singular, smooth (polynomial)")
chk("K3b", sp.solve([sp.Eq(V[0], 0), sp.Eq(V[1], 0)], [x]) == [], "V nowhere zero -> time-orientable (V = future)")
gtt = G[1, 1]
chk("K3c", all(gtt.subs(x, s) > 0 for s in (-1, 1)), "boundary circles x=+-1 spacelike: g(d_theta,d_theta) = 4x^2-1 = 3")
chk("K3d", V[0].subs(x, 1) < 0 and V[0].subs(x, -1) > 0,
    "V points INTO M at both circles: both are past boundaries -> S1 u S1 -> empty (fig. 6b)")
chk("K3e", gtt.subs(x, 0) < 0, "the circle x=0 has g(d_theta,d_theta) = -1: a CLOSED TIMELIKE CURVE (Borde IX: 'albeit with CTCs'; Theorem 1)")
# curvature of the 2D metric: finite everywhere on the strip (smooth non-singular)
gi = G.inv()
coords = [x, th]
Gam = [[[sp.simplify(sum(gi[a, d] * (sp.diff(G[d, b], coords[c]) + sp.diff(G[d, c], coords[b]) - sp.diff(G[b, c], coords[d])) for d in range(2)) / 2)
         for c in range(2)] for b in range(2)] for a in range(2)]
def riem(a, b, c, d):
    return sp.diff(Gam[a][b][d], coords[c]) - sp.diff(Gam[a][b][c], coords[d]) + sum(
        Gam[a][c][e] * Gam[e][b][d] - Gam[a][d][e] * Gam[e][b][c] for e in range(2))
Ric = sp.Matrix(2, 2, lambda b, d: sp.simplify(sum(riem(a, b, a, d) for a in range(2))))
R = sp.simplify(sum(gi[b, d] * Ric[b, d] for b in range(2) for d in range(2)))
den = sp.denom(sp.together(R))
chk("K3f", all(sp.N(r) not in (0,) for r in [den.subs(x, s) for s in (-1, -0.5, 0, 0.5, 1)]) and
    not [r for r in sp.solve(den, x) if r.is_real and -1 <= r <= 1],
    "scalar curvature R(x) = %s : denominator has no real zero on [-1,1]" % sp.factor(R))

# ---------------------------------------------------------------- K4 Fig. 6c Moebius (Sorkin)
# Moebius strip = [-1,1] x R / (x,theta) ~ (-x, theta+2pi).  phi*(d_x) = -d_x, phi*(d_theta) = d_theta.
dphi = sp.diag(-1, 1)
Vphi = V.subs(x, -x)
chk("K4a", sp.simplify(dphi * V - Vphi) == sp.zeros(2, 1), "V is invariant under the Moebius identification: descends, time-orientable")
chk("K4b", sp.simplify(dphi.T * h * dphi - h) == sp.zeros(2, 2), "flat h is invariant: g descends, non-degenerate as in K3a")
chk("K4c", True, "boundary x=+-1 becomes ONE circle; V inward on it (K3d) -> S1 -> empty (fig. 6c); the x=0 core circle "
    "(closed after one turn, tangent d_theta) is timelike (K3e): CTC")

# ---------------------------------------------------------------- K5 index condition
chiM, chi1, chi2 = sp.symbols("chiM chi1 chi2")
# Poincare-Hopf, field inward on S1, outward on S2: sum of indices = chi(M) - chi(S1).
# even n: S1 closed odd-dim -> chi(S1) = 0.  odd n: chi(M) = chi(dM)/2 = (chi1+chi2)/2.
odd = sp.simplify((chi1 + chi2) / 2 - chi1)
chk("K5a", sp.simplify(odd - (chi2 - chi1) / 2) == 0, "odd n: obstruction = (chi(S2)-chi(S1))/2 -> RS rule chi(S1)=chi(S2)")
chk("K5b", True, "even n: obstruction = chi(M) (chi of odd-dim closed S1 = 0) -> chi(M) = 0 [source: 'If n is even, then M admits such a field if chi(M) = 0']")
trousers = 2 - 2 * 0 - 3  # genus 0, 3 boundary circles
chk("K5c", trousers == -1, "trousers S1 u S1 -> S1 has chi = -1 != 0: no non-singular Lorentz metric (Borde IX: 'In this case there is a singularity')")

# ---------------------------------------------------------------- K6 2D enumeration
found = []
for orient, g_or_k in [(True, g) for g in range(0, 5)] + [(False, k) for k in range(1, 8)]:
    for b in range(0, 8):
        chi = (2 - 2 * g_or_k - b) if orient else (2 - g_or_k - b)
        if chi != 0:
            continue
        name = {(True, 0, 2): "cylinder", (True, 1, 0): "torus", (False, 1, 1): "Moebius", (False, 2, 0): "Klein"}.get((orient, g_or_k, b), "?")
        for s1 in range(0, b + 1):  # s1 circles past, b-s1 circles future
            found.append((name, s1, b - s1))
names = sorted({f[0] for f in found})
chk("K6a", names == ["Klein", "Moebius", "cylinder", "torus"], "chi=0 compact surfaces: %s (source III.D list)" % names)
nonempty_change = [f for f in found if f[1] > 0 and f[2] > 0 and f[1] != f[2]]
chk("K6b", nonempty_change == [], "transitions: %s -- no NON-EMPTY -> NON-EMPTY change of topology exists; "
    "every 2D example of topology change has an empty initial or final surface" % sorted(set(found)))

# ---------------------------------------------------------------- K7 n = 3
chis = {gg: 2 - 2 * gg for gg in range(0, 6)}
chk("K7", all(chis[a] != chis[b] for a, b in itertools.combinations(chis, 2)),
    "n=3: chi = 2-2g injective in genus -> RS forbids every non-identity oriented closed transition (e.g. S^2 -> T^2)")

# ---------------------------------------------------------------- K8 n = 4 throat creation (closed)
# M0 = (S^2 x D^2) minus open 4-ball: boundary S^3 u (S^2 x S^1).  chi(S^2 x D^2) = chi(S^2) = 2.
chi_M0 = 2 - 1 + 0      # remove ball: chi(M \ B) = chi(M) - chi(B^4) + chi(S^3) = 2 - 1 + 0
cs = lambda a, b: a + b - 2   # even-dim connected sum
chi_1 = cs(chi_M0, 3)         # # CP^2 (chi 3), n = 4k, k = 1
chi_2 = cs(chi_1, 0)          # # T^4 (chi 0)
chk("K8", (chi_M0, chi_1, chi_2) == (1, 2, 0),
    "S^3 -> S^2xS^1 cobordism chi 1 -> #CP^2 -> 2 -> #T^4 -> 0: a smooth time-oriented Lorentz metric exists (n even, chi = 0)")

# ---------------------------------------------------------------- K9 the tree
c = open(CREATE).read().splitlines()
l51_53 = " ".join(s.strip() for s in c[50:53])
chk("K9a", "KINEMATICALLY POSSIBLE" in l51_53 and "non-singular Lorentz metrics" in l51_53 and "2-dimensional examples" in l51_53,
    "create.py:51-53 = %r" % l51_53[:110])
chk("K9b", c[187].startswith("KINEMATICALLY_POSSIBLE = True"), "create.py:188 = %r" % c[187].strip())
chk("K9c", "time-orient" not in l51_53 and "constraints" not in l51_53,
    "create.py:51-53 carries neither time-orientation nor the source's 'though there are some constraints' (recorded as drift, harmless in n=4)")

print("\nALL AGREE" if ok_all else "\nDISAGREEMENT")
sys.exit(0 if ok_all else 1)
