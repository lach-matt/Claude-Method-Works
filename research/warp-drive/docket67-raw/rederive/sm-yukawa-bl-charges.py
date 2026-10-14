#!/usr/bin/env python3
"""DOCKET 67 audit, key sm-yukawa-bl-charges.
Re-derives massform.py C3 ("every Yukawa term is a fermion bilinear with zero
net B and L; no Higgs coupling carries B or L", THEOREM (perturbative SM)) from
the SM field content, WITHOUT importing massform (no write under research/).

 (1) reads massform's _Q table and YUKAWA_TERMS by AST and recomputes them;
 (2) enumerates EVERY gauge-invariant, Lorentz-scalar, derivative-free operator
     built from the SM Weyl fields + H, H^dagger, by mass dimension 4..7, using
     necessary-and-(for these multiplicities)-sufficient conditions:
       hypercharge sum 0; SU(3) triality 0; even number of SU(2) doublets;
       even number of LH Weyl and even number of RH Weyl fermions;
     checks the dim-4 psi-psi-H list is exactly the three Yukawa structures and
     all carry B = L = 0; finds the first Higgs-bearing operators with B or L != 0;
 (3) explicit SU(2) check that the Weinberg contraction (eps L H)(eps L H) is a
     non-vanishing invariant (random SU(2) matrices);
 (4) anomaly coefficients: SU(2)^2 x B, x L; Y^2 x B, x L; SU(3)^2 x B; grav x B-L.
Exits 1 on any mismatch with the tree's stated C3 content."""
import ast, itertools, sys, random, cmath, math
from fractions import Fraction as F

MF = "/home/user/Claude-Method-Works/research/warp-drive/massform.py"
src = open(MF).read()
tree = ast.parse(src)
vals = {}
for node in tree.body:
    if isinstance(node, ast.Assign) and len(node.targets) == 1 and isinstance(node.targets[0], ast.Name):
        n = node.targets[0].id
        if n in ("_Q", "YUKAWA_TERMS"):
            vals[n] = ast.get_source_segment(src, node.value)
env = {"Fraction": F}
Q = eval(vals["_Q"], env); YT = eval(vals["YUKAWA_TERMS"], env)
ok = True
print("(1) massform tables, recomputed:")
for name, term in YT.items():
    B = sum(s * Q[f][0] for f, s in term); L = sum(s * Q[f][1] for f, s in term)
    print("   %-18s B=%s L=%s" % (name, B, L)); ok &= (B, L) == (0, 0)

# SM left-handed Weyl fields: name: (colour rep 3/-3/1, doublet?, Y, B, L)
FIELDS = {
    "Q":  (3, 1, F(1, 6), F(1, 3), 0),
    "uc": (-3, 0, F(-2, 3), F(-1, 3), 0),
    "dc": (-3, 0, F(1, 3), F(-1, 3), 0),
    "L":  (1, 1, F(-1, 2), 0, 1),
    "ec": (1, 0, F(1), 0, -1),
}
NUR = {"nc": (1, 0, F(0), 0, -1)}  # optional right-handed neutrino (conjugate)
SCAL = {"H": (1, 1, F(1, 2), 0, 0)}

def objs(fields):
    o = []
    for n, (c, d, y, b, l) in fields.items():
        o.append((n, "LH", c, d, y, b, l))
        o.append((n + "~", "RH", -c, d, -y, -b, -l))   # conjugate: RH Weyl
    for n, (c, d, y, b, l) in SCAL.items():
        o.append((n, "S", c, d, y, b, l)); o.append((n + "+", "S", -c, d, -y, -b, -l))
    return o

def allowed(combo):
    Y = sum(x[4] for x in combo)
    tri = sum((1 if x[2] == 3 else -1 if x[2] == -3 else 0) for x in combo) % 3
    nd = sum(x[3] for x in combo)
    nl = sum(1 for x in combo if x[1] == "LH"); nr = sum(1 for x in combo if x[1] == "RH")
    return Y == 0 and tri == 0 and nd % 2 == 0 and nl % 2 == 0 and nr % 2 == 0

def enum(fields, nf, ns):
    O = objs(fields)
    ferm = [x for x in O if x[1] != "S"]; sc = [x for x in O if x[1] == "S"]
    out = set()
    for fc in itertools.combinations_with_replacement(ferm, nf):
        for scc in itertools.combinations_with_replacement(sc, ns):
            c = fc + scc
            if allowed(c):
                B = sum(x[5] for x in c); L = sum(x[6] for x in c)
                out.add((" ".join(sorted(x[0] for x in c)), B, L))
    return sorted(out)

print("(2) dim-4 psi psi phi operators (minimal SM):")
d4 = enum(FIELDS, 2, 1)
for o in d4: print("   ", o)
# expect exactly Q uc H, Q dc H+, L ec H+ and their conjugates (6 lines), all B=L=0
lh_only = [o for o in d4 if "~" not in o[0]]
exp = {"H Q uc", "H+ Q dc", "H+ L ec"}
got = {o[0] for o in lh_only}
print("   LH-type structures:", sorted(got), "== expected:", got == exp)
ok &= got == exp and all(o[1] == 0 and o[2] == 0 for o in d4)
# bare fermion mass terms (dim 3, no Higgs) in minimal SM: none
d3 = enum(FIELDS, 2, 0); print("   dim-3 psi psi (bare mass) in minimal SM:", d3); ok &= d3 == []
# other Higgs couplings at dim<=4 (no fermions): H+H, (H+H)^2 -- B=L=0 trivially
print("   dim-4 phi^4:", enum(FIELDS, 0, 4))

print("(2b) with a right-handed neutrino added:")
d4n = [o for o in enum({**FIELDS, **NUR}, 2, 1) if "n" in o[0]]
print("   new dim-4 Yukawa:", d4n); ok &= all(o[1] == 0 and o[2] == 0 for o in d4n)
d3n = enum({**FIELDS, **NUR}, 2, 0); print("   new dim-3 bare mass:", d3n, "(Majorana nu_R mass, L=-2, NO Higgs)")

print("(2c) dim-5 psi psi phi phi (minimal SM):")
d5 = enum(FIELDS, 2, 2)
bl5 = [o for o in d5 if (o[1], o[2]) != (0, 0)]
for o in bl5: print("    B/L-carrying:", o)
ok &= [o[0] for o in bl5] == ["H H L L", "H+ H+ L~ L~"] or sorted(o[0] for o in bl5) == sorted(["H H L L", "H+ H+ L~ L~"])

print("(2d) dim-6: 4-fermion B-violating (no Higgs) and psi psi phi^3:")
d6f = [o for o in enum(FIELDS, 4, 0) if o[1] != 0]
print("    B-violating 4-fermion structures:", len(d6f), "e.g.", d6f[:4])
d6h = [o for o in enum(FIELDS, 2, 3) if (o[1], o[2]) != (0, 0)]
print("    psi psi phi^3 carrying B or L:", d6h)
ok &= d6h == []
print("(2e) dim-7: psi^4 phi carrying B:")
d7 = [o for o in enum(FIELDS, 4, 1) if o[1] != 0]
for o in d7: print("   ", o)
print("    every one has Delta B = -Delta L:", all(o[1] == -o[2] for o in d7))
d7L = [o for o in enum(FIELDS, 2, 3) + enum(FIELDS, 4, 1) if o[1] == 0 and o[2] != 0]
print("    Higgs-bearing structures with Delta B = 0, Delta L != 0 (dim-6 psi^2 phi^3: none; dim-7 psi^4 phi):", len(d7L), d7L[:2])
print("    NOTE: (2) is hypercharge/triality/doublet/chirality counting; flavour antisymmetry not imposed (irrelevant at dim 4, where the list is exact).")

print("(2f) dim-5..7 Higgs-bearing B/L carriers all violate B-L (so H-BL excludes them)?")
carriers = bl5 + d7 + d7L
print("    all violate B-L:", all(o[1] - o[2] != 0 for o in carriers), " count", len(carriers))
ok &= all(o[1] - o[2] != 0 for o in carriers)
d8 = [o for o in enum(FIELDS, 4, 2) if o[1] != 0 and o[1] == o[2]]
print("(2g) dim-8 psi^4 phi^2 with Delta B = Delta L != 0 (B-L CONSERVING, Higgs-bearing):", len(d8), d8[:3])
ok &= any(o[0] == "H H+ L Q Q Q" for o in d8)
print("(3) Weinberg contraction (eps L H)(eps L H), SU(2) invariance + non-vanishing:")
def rsu2():
    a = complex(random.gauss(0, 1), random.gauss(0, 1)); b = complex(random.gauss(0, 1), random.gauss(0, 1))
    n = math.sqrt(abs(a) ** 2 + abs(b) ** 2); a /= n; b /= n
    return [[a, -b.conjugate()], [b, a.conjugate()]]
def mv(U, v): return [U[0][0] * v[0] + U[0][1] * v[1], U[1][0] * v[0] + U[1][1] * v[1]]
def epsc(x, y): return x[0] * y[1] - x[1] * y[0]
random.seed(1); mx = 0; val = None
for _ in range(200):
    l = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(2)]
    h = [complex(random.gauss(0, 1), random.gauss(0, 1)) for _ in range(2)]
    U = rsu2()
    w0 = epsc(l, h) ** 2; w1 = epsc(mv(U, l), mv(U, h)) ** 2
    mx = max(mx, abs(w0 - w1)); val = w0
print("    max |O - O(U)| over 200 random SU(2):", "%.1e" % mx, " sample |O| =", "%.3f" % abs(val))
ok &= mx < 1e-12 and abs(val) > 1e-6

print("(4) anomaly coefficients per generation (LH Weyl basis):")
def A(weight):
    s2 = sum(F(1, 2) * (3 if abs(c) == 3 else 1) * weight(n) for n, (c, d, y, b, l) in FIELDS.items() if d)
    y2 = sum((3 if abs(c) == 3 else 1) * (2 if d else 1) * y * y * weight(n) for n, (c, d, y, b, l) in FIELDS.items())
    s3 = sum(F(1, 2) * (2 if d else 1) * weight(n) for n, (c, d, y, b, l) in FIELDS.items() if abs(c) == 3)
    gr = sum((3 if abs(c) == 3 else 1) * (2 if d else 1) * weight(n) for n, (c, d, y, b, l) in FIELDS.items())
    return s2, y2, s3, gr
for lab, w in (("B", lambda n: FIELDS[n][3]), ("L", lambda n: FIELDS[n][4]),
               ("B-L", lambda n: FIELDS[n][3] - FIELDS[n][4]), ("B+L", lambda n: FIELDS[n][3] + FIELDS[n][4])):
    s2, y2, s3, gr = A(w)
    print("    %-4s SU(2)^2=%-5s Y^2=%-5s SU(3)^2=%-4s grav=%s" % (lab, s2, y2, s3, gr))
s2B, y2B, s3B, _ = A(lambda n: FIELDS[n][3]); s2L, y2L, _, _ = A(lambda n: FIELDS[n][4])
ok &= s2B == s2L == F(1, 2) and y2B == y2L and s3B == 0
print("    B, L each anomalous under SU(2)^2 and Y^2, equally: B-L free of SM-gauge anomalies;"
      " B+L is not -> 'perturbative' is a NEEDED qualifier.  grav(B-L) = -1/gen without nu_R.")
print("RESULT:", "PASS" if ok else "FAIL")
sys.exit(0 if ok else 1)
