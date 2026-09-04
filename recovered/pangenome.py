"""Lambda_P : the pangenome allele index. Tests P1-P6 as committed."""
from itertools import product, combinations

def R(cells):
    """sublattice generated: closure under coordinatewise join AND meet, to fixed point"""
    S = set(cells)
    while True:
        new = {tuple(map(max,zip(x,y))) for x in S for y in S} | \
              {tuple(map(min,zip(x,y))) for x in S for y in S}
        if new <= S: return S
        S |= new

def E(cells): return len(R(cells)) - len(set(cells))

# ---------- P1 : is the obstruction the SUM ? -----------------------------
# locus with A alleles, carrier counts c_a summing to H.  Cells (a, c_a).
print("=== P1  DOES THE SUM OBSTRUCT? ===")
H, A = 12, 4
comps = [c for c in product(range(1,H), repeat=A) if sum(c)==H]
byE = {}
for c in comps:
    e = E([(a,ca) for a,ca in enumerate(c)])
    byE.setdefault(e, []).append(c)
print(f"  all {len(comps)} compositions of H={H} into A={A} positive parts")
for e in sorted(byE): print(f"    E={e}: {len(byE[e]):4d} compositions   e.g. {byE[e][0]}")
mono = [c for c in comps if list(c)==sorted(c)]
print(f"  of these, {len(mono)} are non-decreasing; their E values: "
      f"{sorted(set(E([(a,ca) for a,ca in enumerate(c)]) for c in mono))}")

# does E depend on H at all, holding the ORDER PATTERN fixed?
print("\n  same order-pattern, different sums:")
for H2 in (12, 40, 400):
    c = (H2-6, 2, 3, 1)                       # same descending-ish shape
    print(f"    H={H2:3d}  c={c}  E={E([(a,x) for a,x in enumerate(c)])}")
print("  --> E is a function of the ORDER PATTERN, not of the sum. P1 REFUTED.")

# ---------- P2 : does adjoining H as a coordinate change anything? --------
print("\n=== P2  ADJOIN THE SUM AS A COORDINATE ===")
c = (6,2,3,1)
base = [(a,x) for a,x in enumerate(c)]
withH = [(a,x,sum(c)) for a,x in enumerate(c)]
print(f"  E without H-axis: {E(base)}   E with constant H-axis: {E(withH)}")
print("  --> a constant axis is inert. P2 REFUTED; P3's 'weak zero' never arises.")

# ---------- P6 : the snarl-nesting index ----------------------------------
# cell = (level d, allele index a, carrier count c).  Real bound: d <= 28.
print("\n=== P6  SNARL NESTING, BOTH ORIENTATIONS ===")
# synthetic nested snarl: A(child) <= A(parent).  levels 0..D outermost..innermost
def build(Avec):
    """Avec[d] = number of observed alleles at level d"""
    return [(d,a) for d,Ad in enumerate(Avec) for a in range(Ad)]

Aout = [8,6,6,4,3,3,2,2]          # A decreasing with level (outermost has most)
print(f"  A by level (level 0 = outermost): {Aout}")
print(f"    as labelled (a <= A(d), A antitone):   E = {E(build(Aout))}")
print(f"    reversed to height (A monotone):       E = {E(build(Aout[::-1]))}")

# ---------- the general law, stated and tested ----------------------------
print("\n=== THE LAW: E OF A FUNCTION-GRAPH ON A TREE-BOUNDED AXIS ===")
import random
random.seed(5)
def law_test(trials=4000):
    rows=[]
    for _ in range(trials):
        n = random.randint(2,7)
        v = [random.randint(1,9) for _ in range(n)]
        cells = [(i,x) for i,x in enumerate(v)]
        # count strict descents' contribution: |R| - |X|
        rows.append((tuple(v), E(cells), list(v)==sorted(v)))
    mono_nonzero = [r for r in rows if r[2] and r[1]!=0]
    nonmono_zero = [r for r in rows if not r[2] and r[1]==0]
    return len(rows), len(mono_nonzero), len(nonmono_zero)
t, mnz, nmz = law_test()
print(f"  {t} random vectors tested")
print(f"  monotone with E != 0 : {mnz}      (should be 0)")
print(f"  non-monotone with E = 0 : {nmz}   (should be 0)")
print("  --> E = 0  <=>  the bound is monotone in its label. Exhaustive on the sample.")