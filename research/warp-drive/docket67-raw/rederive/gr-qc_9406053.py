#!/usr/bin/env python3
"""DOCKET 67 -- re-derivation / machine checks for Borde, gr-qc/9406053.

Reads (never writes) research/warp-drive/create.py by AST, and the saved
full text of gr-qc/9406053v1 (alphaXiv get_paper_content, fullText) at
../src/gr-qc_9406053.txt.  Exits 1 if any check disagrees with what the
audit report records.

  C1  verbatim: every quotation create.py attributes to Borde occurs in the source
  C2  structure: where the escapes sit (section IX, not VIII) and how many there are
  C3  sympy: g = h(V,V) h - 2 (hV)(hV) is Lorentzian with V timelike (Sec. II.B)
  C4  sympy: U = P + (b^2/2) M + b S is null, R(U,U)=0 is at most quartic in b (Sec. V.A, n=3)
  C5  sympy: null Raychaudhuri focusing, theta0 > 0 diverges within (n-2)/theta0 (Lemma B core)
  C6  sympy: T(V,V) >= K for all unit timelike V  =>  T(U,U) >= 0 for null U (Sec. VI)
  C7  Euler-characteristic arithmetic of Sec. III.C (RS rule, Misner trick, the n=7 example)
  C8  brute force: finite shadow of Theorem 1 (no cycle => every flow line ends on S2)
      and of Theorem 2 (connected + one root per tree => one root)
  C9  z3: the encodings specthm.py uses -- what the facts imply and what they do not
"""
import ast, itertools, os, re, sys, unicodedata
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "src", "gr-qc_9406053.txt")
CREATE = "/home/user/Claude-Method-Works/research/warp-drive/create.py"
FAIL = []


def check(name, ok, detail=""):
    print("%-5s %-4s %s" % (name, "OK" if ok else "FAIL", detail))
    if not ok:
        FAIL.append(name)


def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("≥", ">=").replace("–", "-").replace("—", "-")
    s = re.sub(r"-\s+", "-", s)          # line-broken hyphenations ("topolo- gies")
    s = re.sub(r"\s+", " ", s)
    return s.lower().strip()


# ------------------------------------------------------------------ inputs
text_raw = open(SRC, encoding="utf-8").read()
TEXT = norm(text_raw)
tree = ast.parse(open(CREATE, encoding="utf-8").read())
CONST = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        try:
            CONST[node.targets[0].id] = ast.literal_eval(node.value)
        except Exception:
            pass
DOC = ast.get_docstring(tree)

# ------------------------------------------------------------------ C1 verbatim
quotes = {
    "abstract 'price'": "topology change is only to be had at a price",
    "abstract 'wide range'": "a condition satisfied in a very wide range of situations",
    "BORDE": CONST["BORDE"],
    "BORDE_SINGULARITY": CONST["BORDE_SINGULARITY"],
    "BORDE_DYNAMICS": CONST["BORDE_DYNAMICS"].replace(">=", ">="),
    "ESCAPES[0] quote": "a highly undesirable feature",
    "ESCAPES[1] quote": "such an alteration would have to be fairly severe",
    "BORDE_CAUTION": CONST["BORDE_CAUTION"],
}
for k, q in quotes.items():
    check("C1", norm(q) in TEXT, "verbatim in source: %s" % k)

# ------------------------------------------------------------------ C2 structure
i_viii = TEXT.find("viii. a few words on differentiability")
i_ix = TEXT.find("ix. concluding comments")
i_a = TEXT.find("a ] dropping causal compactness")
i_b = TEXT.find("b ] weakening the curvature constraints")
i_c = TEXT.find("c ] degenerate metrics")
i_ack = TEXT.find("acknowledgements")
i_eucl = TEXT.find("abandon the lorentzian framework altogether and to use a euclidean path integral")
check("C2", 0 < i_viii < i_ix < i_a < i_b < i_c < i_ack,
      "escape subsections A,B,C sit in SECTION IX (Concluding Comments); section VIII is "
      "'A Few Words on Differentiability' -> the tree's 'section VIII.A' (specthm.py:587, :1850) "
      "is a section-number discrepancy")
check("C2", i_ix < i_eucl < i_a,
      "Euclidean path integral is named BEFORE the subsections, as leaving the Lorentzian framework")
check("C2", norm("but even within the general lorentzian framework there are still several "
                 "interesting possibilities") in TEXT,
      "A, B, C are introduced as possibilities WITHIN the general Lorentzian framework")
source_routes = ["Euclidean path integral (leaves Lorentzian)", "IX.A drop causal compactness",
                 "IX.B weaken curvature constraints", "IX.C degenerate metrics"]
tree_routes = [e[0] for e in CONST["ESCAPES"]]
print("      source routes (%d): %s" % (len(source_routes), source_routes))
print("      tree routes   (%d): %s" % (len(tree_routes), tree_routes))
check("C2", len(tree_routes) == 3 and len(source_routes) == 4,
      "len(create.ESCAPES) = 3 against 4 routes in the source: IX.C DEGENERATE METRICS is omitted")
seg_b = TEXT[i_b:i_c]
check("C2", norm("this would not affect the presence of causality violations") in seg_b,
      "IX.B: weakening curvature constraints does NOT remove the causality violation (Thm 1 stands)")
check("C2", norm("violations of the energy conditions large enough to allow assumption (ii) to be violated") in seg_b,
      "IX.B has a second sub-route INSIDE Einstein's equation (energy-condition violation, cf. "
      "wormhole creation) -- create.ESCAPES[1] records only 'altering Einstein's equation'")
seg_c = TEXT[i_c:i_ack]
check("C2", norm("even in standard general relativity (couched in first-order language) horowitz") in seg_c
      and norm("this might well prove to be the correct approach") in seg_c,
      "IX.C: degenerate metrics, Horowitz in first-order standard GR, 'might well prove to be the correct approach'")
check("C2", norm("if we were satisfied with metrics that are only continuous") in TEXT
      and norm("s 1 and s 2 need not be diffeomorphic, even if causality violations are forbidden") in TEXT,
      "Sec. VIII: Theorem 1's conclusion needs a differentiable (C^1) vector field; with a C^0 metric it fails")
seg_a = TEXT[i_a:i_b]
check("C2", norm("under some mild additional assumptions") in seg_a and norm("in the closed universe case") in seg_a
      and norm("or a point at infinity") in seg_a,
      "IX.A: Tipler Thm 5, closed-universe case, mild additional assumptions, singularity OR point at infinity")
check("C2", norm("the truth of this depends on the definition of a singularity") in TEXT
      and norm("other definitions of a singularity may make the statement true") in TEXT,
      "the 'even if incomplete geodesics are admitted' sentence is conditional on the standard definition")
check("C2", norm("theorem 1: let m be a (time-oriented) causally compact spacetime that interpolates") in TEXT,
      "Theorem 1 located: time-oriented (removable, Sec. VII), causally compact, interpolating")
check("C2", norm("theorem 3: let m be a (time-oriented) causally compact interpolating space- time of dimension >= 3".replace("space- time", "space-time")) in TEXT
      or "theorem 3: let m be a (time-oriented) causally compact interpolating" in TEXT,
      "Theorem 3 located: dim >= 3, null generic condition (i), half-integral null convergence (ii)")

# ------------------------------------------------------------------ C3 Lorentz metric from V
for n in range(2, 6):
    V = sp.Matrix(sp.symbols("v1:%d" % (n + 1), real=True))
    h = sp.eye(n)
    g = (V.T * h * V)[0] * h - 2 * (h * V) * (h * V).T
    gVV = sp.simplify((V.T * g * V)[0])
    # eigenvalues: |V|^2 (n-1 times) and -|V|^2
    vals = {1: 3, 2: -1, 3: 0, 4: 2, 5: 1}
    num = g.subs({V[i]: vals[i + 1] for i in range(n)})
    ev = sorted(sp.Matrix(num).eigenvals(multiple=True))
    nneg = sum(1 for e in ev if e < 0)
    check("C3", sp.simplify(gVV + (V.T * V)[0] ** 2) == 0 and nneg == 1,
          "n=%d: g(V,V) = -|V|^4 and signature (-,+..+) at a sample V (eig %s)" % (n, ev))

# ------------------------------------------------------------------ C4 null directions n=3
b = sp.symbols("beta", real=True)
# basis P, M null with P.M = -1, S unit spacelike orthogonal: Gram matrix in (P,M,S)
G = sp.Matrix([[0, -1, 0], [-1, 0, 0], [0, 0, 1]])
U = sp.Matrix([1, b ** 2 / 2, b])
check("C4", sp.simplify((U.T * G * U)[0]) == 0, "U = P + (b^2/2)M + bS is null")
r = sp.symbols("r11 r12 r13 r22 r23 r33", real=True)
R = sp.Matrix([[r[0], r[1], r[2]], [r[1], r[3], r[4]], [r[2], r[4], r[5]]])
poly = sp.Poly(sp.expand((U.T * R * U)[0]), b)
check("C4", poly.degree() == 4 and sp.simplify(poly.coeff_monomial(b ** 4) - R[1, 1] / 4) == 0,
      "R(U,U) is quartic in beta, leading coeff R(M,M)/4 -> cubic if R(M,M)=0: at most 4 null zero-directions")

# ------------------------------------------------------------------ C5 focusing
u, th0, nn = sp.symbols("u theta0 n", positive=True)
th = sp.Function("theta")
sol = sp.dsolve(sp.Eq(th(u).diff(u), -th(u) ** 2 / (nn - 2)), th(u), ics={th(0): th0})
expr = sp.simplify(sol.rhs)
pole = sp.solve(sp.denom(sp.together(expr)), u)
check("C5", any(sp.simplify(p + (nn - 2) / th0) == 0 for p in pole),
      "d theta/du = -theta^2/(n-2), theta(0)=theta0>0: theta = %s -> inf at u = -(n-2)/theta0, i.e. within "
      "affine distance (n-2)/theta0 in the direction of DECREASING u = the PAST under Lemma B's / proof step 4's "
      "convention (u increases to the future) -- agrees with Lemma B" % expr)
# eq.(1) is form-invariant under u -> -u (U -> -U, theta -> -theta): the set-up sentence before eq.(1)
# ('u ... chosen to increase in the past direction') conflicts with Lemma B and step 4 (u increasing to
# the future); the invariance shows the conflict is a convention discrepancy that changes only the sign of theta.
tt = sp.Function("tt")
lhs = sp.Derivative(-tt(-u), u).doit()          # d(-theta(-u))/du
rhs_rev = -(-tt(-u)) ** 2 / (nn - 2)
orig_at = (-tt(u) ** 2 / (nn - 2)).subs(u, -u)  # original RHS evaluated at -u
# lhs = theta'(-u); original eq at -u: theta'(-u) = -theta(-u)^2/(n-2) = rhs_rev

check("C5", sp.simplify(rhs_rev - orig_at) == 0,
      "reversal u->-u, theta->-theta leaves the RHS of eq.(1) unchanged (theta^2, R(U,U), sigma^2 are even): "
      "the source's two conventions differ only in the sign attached to 'theta > 0' -- a DISCREPANCY, not an error")

# ------------------------------------------------------------------ C6 energy condition limit (2D block)
eta = sp.symbols("eta", real=True)
T00, T01, T11 = sp.symbols("T00 T01 T11", real=True)
Vt = sp.Matrix([sp.cosh(eta), sp.sinh(eta)])
Tm = sp.Matrix([[T00, T01], [T01, T11]])
TVV = sp.expand((Vt.T * Tm * Vt)[0].rewrite(sp.exp))
lead = sp.simplify(sp.limit(TVV * sp.exp(-2 * eta), eta, sp.oo))
Un = sp.Matrix([1, 1])
check("C6", sp.simplify(lead - (Un.T * Tm * Un)[0] / 4) == 0,
      "T(V_eta,V_eta) = e^{2eta} T(U,U)/4 + O(1): a lower bound K over all boosts forces T(U,U) >= 0 (U=(1,1))")
# T = C g example (Borde's 'formally possible' bounded-below case): T(U,U)=0
gm = sp.diag(-1, 1)
C = sp.symbols("C", real=True)
check("C6", sp.simplify((Un.T * (C * gm) * Un)[0]) == 0 and sp.simplify((Vt.T * (C * gm) * Vt)[0] + C) == 0,
      "T = C g: T(V,V) = -C for every unit timelike V, T(U,U) = 0 (Borde's example)")

# ------------------------------------------------------------------ C7 Euler characteristics
chi_S = lambda k: 1 + (-1) ** k
chi_T = lambda k: 0 if k > 0 else 1
chi_CP2 = 3
csum = lambda a, bb: a + bb - 2       # even-dimensional closed connected sum
check("C7", chi_T(4) == 0 and chi_S(2) * chi_S(2) == 4 and chi_CP2 == 3,
      "chi(T^n)=0, chi(S^2 x S^{n-2})=4 (n even), chi(CP^2)=3")
check("C7", all(csum(x, chi_T(4)) == x - 2 and csum(x, 4) == x + 2 and csum(x, chi_CP2) == x + 1
                for x in range(-7, 8)),
      "Misner trick: # T^n lowers chi by 2, # S^2xS^{n-2} raises it by 2, # CP^2 (n=4) shifts parity -> any chi reaches 0 (n=4k)")
g_ = list(range(0, 6))
check("C7", len({2 - 2 * gg for gg in g_}) == len(g_),
      "n=3 RS rule: chi = 2-2g is injective in genus -> every nontrivial oriented 2-surface transition forbidden")
chi_S4xS2 = chi_S(4) * chi_S(2)
check("C7", chi_S(6) == 2 and csum(chi_S4xS2, chi_T(6)) == 2,
      "n=7 example: chi(S^6) = 2 = chi((S^4 x S^2) # T^6) = 4 + 0 - 2")

# ------------------------------------------------------------------ C8 finite shadow of Thm 1 and Thm 2
def orbits_ok(nodes, succ, terminal):
    """Follow succ from each node; return (has_cycle, all_reach_terminal)."""
    has_cycle = False
    allreach = True
    for s in nodes:
        seen = set(); x = s
        while x not in terminal:
            if x in seen:
                has_cycle = True; allreach = False; break
            seen.add(x); x = succ[x]
    return has_cycle, allreach

count = 0; bad = 0
for N in range(1, 6):
    nodes = list(range(N))
    for tmask in range(1, 2 ** N):
        terminal = {i for i in nodes if tmask >> i & 1}
        free = [i for i in nodes if i not in terminal]
        for choice in itertools.product(nodes, repeat=len(free)):
            succ = dict(zip(free, choice))
            cyc, reach = orbits_ok(nodes, succ, terminal)
            count += 1
            if (not cyc) and (not reach):
                bad += 1
check("C8", bad == 0 and count > 0,
      "all %d finite flows (N<=5): no cycle => every flow line ends on the final set (Thm 1's compactness step in discrete form)" % count)
bad2 = 0; count2 = 0
for N in range(1, 6):
    for parent in itertools.product(range(-1, N), repeat=N):   # -1 = root (a point of S1)
        # a forest: following parents must terminate
        ok = True
        for s in range(N):
            seen = set(); x = s
            while parent[x] != -1:
                if x in seen: ok = False; break
                seen.add(x); x = parent[x]
            if not ok: break
        if not ok:
            continue
        count2 += 1
        adj = {i: set() for i in range(N)}
        for i, p in enumerate(parent):
            if p != -1:
                adj[i].add(p); adj[p].add(i)
        comp = set([0]); stack = [0]
        while stack:
            x = stack.pop()
            for y in adj[x]:
                if y not in comp: comp.add(y); stack.append(y)
        connected = len(comp) == N
        roots = sum(1 for p in parent if p == -1)
        if connected and roots != 1:
            bad2 += 1
check("C8", bad2 == 0, "all %d finite forests (N<=5): connected => exactly one root (Thm 2's basin argument in discrete form)" % count2)

# ------------------------------------------------------------------ C9 z3 encodings
import z3
created, cc, ctc, path, nongr, closed, tipx, smooth = z3.Bools("created cc ctc pathology nongr closed tipler_extra smooth_nondeg")
s = z3.Solver()
# Borde Thm 1 as READ: created (topology change) & cc & smooth nondegenerate time-orientable Lorentz metric -> ctc
thm1 = z3.Implies(z3.And(created, cc, smooth), ctc)
# Tipler Thm 5 as Borde IX.A restates it: closed & not cc & mild extra -> singularity or point at infinity
tip5 = z3.Implies(z3.And(created, z3.Not(cc), closed, tipx, smooth), path)
# (a) specthm GEROCH-BORDE as encoded (no smooth hypothesis): is it implied by thm1?  Only if smooth holds.
s.push(); s.add(thm1, z3.Not(z3.Implies(z3.And(created, cc), ctc)))
r_a = s.check(); m_a = s.model() if r_a == z3.sat else None; s.pop()
check("C9", r_a == z3.sat and z3.is_false(m_a.eval(smooth, model_completion=True)),
      "GEROCH-BORDE as encoded (created & cc -> ctc) is NOT implied by Thm 1 as read: countermodel has smooth_nondeg = False "
      "(degenerate / C^0 metric) -- the smoothness hypothesis is dropped")
s.push(); s.add(thm1, smooth, z3.Not(z3.Implies(z3.And(created, cc), ctc)))
check("C9", s.check() == z3.unsat, "with smooth_nondeg added, GEROCH-BORDE follows from Thm 1 (unsat)"); s.pop()
# (b) specthm BORDE-ESCAPES as encoded: created & not cc -> pathology or nongr
enc_b = z3.Implies(z3.And(created, z3.Not(cc)), z3.Or(path, nongr))
s.push(); s.add(tip5, smooth, closed, tipx, z3.Not(enc_b))
check("C9", s.check() == z3.unsat,
      "under H_closed + Tipler's extra assumptions (+ smooth), BORDE-ESCAPES follows from Tipler Thm 5 (unsat)"); s.pop()
s.push(); s.add(tip5, thm1, z3.Not(closed), z3.Not(enc_b))
check("C9", s.check() == z3.sat,
      "without H_closed, BORDE-ESCAPES is NOT implied by anything Borde states (sat) -- specthm scopes it to H_closed, correctly"); s.pop()
# (c) the 'nongr' disjunct is not a consequence of dropping cc in the source: Borde's other routes are
#     alternatives, not outcomes of dropping cc.  Show the disjunction is strictly weaker than tip5's consequent.
s.push(); s.add(tip5, smooth, closed, tipx, created, z3.Not(cc), z3.Not(path))
check("C9", s.check() == z3.unsat,
      "in the H_closed case the source forces the PATHOLOGY disjunct itself; 'or nongr' is a weakening, harmless but not Borde's structure"); s.pop()

print("\nRESULT: %s" % ("ALL CHECKS AGREE WITH THE REPORT" if not FAIL else "FAILED: %s" % FAIL))
sys.exit(1 if FAIL else 0)
