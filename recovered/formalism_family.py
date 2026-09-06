#!/usr/bin/env python3
"""The table is not one table. It is a family indexed by formalism choices.

Three independent formalism axes surfaced this session:
  ctc   : D-CTC | P-CTC | process-matrix (linear indefinite causal structure)
  alg   : standard Weyl algebra | generalised (Wald-Ishibashi / Yurtsever)
  meas  : projection postulate (Soulas) | Lueders (Sorkin impossible measurements)

Coordinates extended by SD (microcausality / spacetime distinctness).
Rd remains OUTSIDE the box: it is the second disjunct of C's consequence.
"""
from itertools import product, combinations

LAWS = ["T", "H", "L", "U", "N", "C", "E", "D", "SD"]

def clauses(ctc, alg, meas):
    cl = [("T", "H"), ("T", "E"),           # geometric, model-independent
          ("D", "N"), ("N", "C"),           # Gisin - VERIFIED grade 4
          ("E", "C")]                       # NEC violation: stable => superluminal
    if ctc in ("D", "P"):
        cl += [("T", "L"), ("T", "D")]      # absent under process-matrix (linear)
    if ctc == "D":
        cl += [("T", "U"), ("T", "N")]      # P-CTCs: pure->pure, no cloning
    if alg == "standard":
        cl += [("H", "U")]                  # fails under generalised algebras
    if meas == "projection":
        cl += [("C", "SD")]                 # Soulas: no-signalling => microcausality
    cl += [("L", "C")]                      # CONTESTED (Bona, Svetlichny)
    return cl

def close(S, cl):
    S = set(S); grew = True
    while grew:
        grew = False
        for a, b in cl:
            if a in S and b not in S:
                S.add(b); grew = True
    return frozenset(S)

results = {}
for ctc, alg, meas in product(["D", "P", "M"], ["standard", "general"],
                              ["projection", "lueders"]):
    cl = clauses(ctc, alg, meas)
    closed = {close(c, cl) for r in range(len(LAWS) + 1)
              for c in combinations(LAWS, r)}
    mins = frozenset(c for c in closed
                     if c and not any(d < c and d for d in closed))
    ante = frozenset(a for a, b in cl)
    results[(ctc, alg, meas)] = (len(closed), mins, ante,
                                 close({"T"}, cl), close({"E"}, cl))

print("="*74)
print("  FORMALISM FAMILY: 3 x 2 x 2 = 12 combinations")
print("="*74)
print(f"  {'ctc':<4} {'algebra':<9} {'measure':<11} {'closed':>7}  "
      f"{'clos(T)':<12} {'clos(E)':<8} minimal")
for k in sorted(results):
    n, mins, ante, ct, ce = results[k]
    ms = ",".join(sorted("".join(sorted(m)) for m in mins))
    print(f"  {k[0]:<4} {k[1]:<9} {k[2]:<11} {n:>7}  "
          f"{''.join(sorted(ct)):<12} {''.join(sorted(ce)):<8} {ms}")

distinct_struct = len({tuple(sorted("".join(sorted(c)) for c in
                                    (lambda cl: {close(x, cl) for r in range(len(LAWS)+1)
                                                 for x in combinations(LAWS, r)})(clauses(*k))))
                       for k in results})
distinct_mins = len({results[k][1] for k in results})
distinct_ante = len({results[k][2] for k in results})
distinct_counts = len({results[k][0] for k in results})

print("\n" + "="*74)
print("  HOW MANY TABLES DOES THE CONSTRUCTION ACTUALLY HAVE?")
print("="*74)
print(f"  combinations                 12")
print(f"  distinct closure structures  {distinct_struct}")
print(f"  distinct closed-profile counts {distinct_counts}")
print(f"  distinct antecedent sets     {distinct_ante}")
print(f"  distinct MINIMAL-PROFILE sets {distinct_mins}   <-- prediction was 4")
print("\n  the distinct minimal sets:")
for m in sorted({results[k][1] for k in results},
                key=lambda s: sorted("".join(sorted(x)) for x in s)):
    who = [k for k in sorted(results) if results[k][1] == m]
    print(f"    {{{', '.join(sorted(''.join(sorted(x)) for x in m))}}}")
    print(f"        under: {', '.join('/'.join(k) for k in who)}")

print(f"\n  is E ever minimal?  "
      f"{any(frozenset({'E'}) in results[k][1] for k in results)}")
print(f"  is C ever minimal?  "
      f"{any(frozenset({'C'}) in results[k][1] for k in results)}")
print(f"  is T ever minimal?  "
      f"{any(frozenset({'T'}) in results[k][1] for k in results)}")
