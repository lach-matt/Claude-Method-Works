#!/usr/bin/env python3
"""Three fixes applied:
  (1) D and N merged  - cloning-discrimination equivalence (deterministic regime)
  (2) Rd brought inside as TWO vertices - Visser: Rd is not binary
  (3) NEGATIVE edges added - "breaking X forbids breaking Y"
      Visser: imposing a preferred foliation automatically enforces
      Hawking's chronology protection conjecture.  Rd inversion forbids T.

Formalism fixed at D-CTC / standard algebra / projection postulate for readability.
Leaked vertices (instability, locality, energy-momentum) declared but NOT wired:
they have no retrieved edges, so under the Admission Law they cannot be entered.
"""
from itertools import combinations

LAWS = ["T", "H", "L", "U", "DN", "C", "E", "SD", "Rdf", "Rdi"]
GLOSS = {"T": "chronology", "H": "global hyperbolicity", "L": "linearity",
         "U": "unitarity", "DN": "no-cloning = no perfect discrimination",
         "C": "no superluminal signalling", "E": "null energy condition",
         "SD": "spacetime distinctness (microcausality)",
         "Rdf": "dynamical relativity, finite signal speed",
         "Rdi": "dynamical relativity, infinite signal speed"}

POS = [("T", "H"), ("T", "E"), ("T", "L"), ("T", "DN"), ("T", "U"),
       ("DN", "C"), ("E", "C"), ("SD", "C"), ("H", "U"), ("L", "C"),
       ("Rdi", "H")]

# negative: breaking a FORBIDS breaking b
NEG = [("Rdf", "T"), ("Rdi", "T")]

def close(S):
    S = set(S); grew = True
    while grew:
        grew = False
        for a, b in POS:
            if a in S and b not in S:
                S.add(b); grew = True
    return frozenset(S)

def admissible(S):
    return not any(a in S and b in S for a, b in NEG)

# ---- without negative edges (fixes 1-2 only) ----
closed_pos = {close(c) for r in range(len(LAWS)+1) for c in combinations(LAWS, r)}
# ---- with negative edges (all three fixes) ----
closed_all = {c for c in closed_pos if admissible(c)}

def lattice_failures(fam):
    F = set(fam)
    jf = sum(1 for a, b in combinations(F, 2) if (a | b) not in F)
    mf = sum(1 for a, b in combinations(F, 2) if (a & b) not in F)
    return jf, mf

jf0, mf0 = lattice_failures(closed_pos)
jf1, mf1 = lattice_failures(closed_all)

print("="*70)
print("  THREE FIXES APPLIED")
print("="*70)
print(f"  vertices                    {len(LAWS)}  (D,N merged; Rd split in two)")
print(f"  positive edges              {len(POS)}")
print(f"  negative edges              {len(NEG)}")
print(f"\n  closed profiles, POSITIVE edges only     {len(closed_pos)}")
print(f"    join failures  {jf0}    meet failures  {mf0}")
print(f"\n  admissible profiles, WITH negative edges  {len(closed_all)}")
print(f"    join failures  {jf1}    meet failures  {mf1}")
print(f"\n  profiles killed by the negative edges     "
      f"{len(closed_pos) - len(closed_all)}")

print("\n" + "="*70)
print("  IS THE INDEX STILL A MOORE FAMILY (closed under intersection)?")
print("="*70)
print(f"  positive only:  {'YES' if mf0 == 0 else 'NO'}")
print(f"  with negative:  {'YES' if mf1 == 0 else 'NO'}")
print(f"  closed under union?  positive: {'YES' if jf0==0 else 'NO'}   "
       f"with negative: {'YES' if jf1==0 else 'NO'}")

# the forced choice
print("\n" + "="*70)
print("  THE FORCED CHOICE:  C -> T or Rd, and Rd forbids T")
print("="*70)
cbreak = [c for c in closed_all if "C" in c]
with_t   = [c for c in cbreak if "T" in c]
with_rd  = [c for c in cbreak if ("Rdf" in c or "Rdi" in c)]
with_both= [c for c in cbreak if "T" in c and ("Rdf" in c or "Rdi" in c)]
neither  = [c for c in cbreak if "T" not in c and "Rdf" not in c and "Rdi" not in c]
print(f"  admissible profiles breaking C        {len(cbreak)}")
print(f"    ... that also break T               {len(with_t)}")
print(f"    ... that also break Rd (either)     {len(with_rd)}")
print(f"    ... that break BOTH                 {len(with_both)}  (must be 0)")
print(f"    ... that break NEITHER              {len(neither)}")

mins = [c for c in closed_all if c and not any(d < c and d for d in closed_all)]
print(f"\n  minimal admissible profiles:")
for c in sorted(mins, key=lambda s: (len(s), sorted(s))):
    print(f"    {{{','.join(sorted(c))}}}")
