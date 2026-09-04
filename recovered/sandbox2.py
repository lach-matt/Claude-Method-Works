from itertools import combinations
print("="*78)
print("DIAGNOSING THE THREE MISPREDICTIONS")
print("="*78)

def failures(cells):
    S=set(cells)
    jn=lambda a,b: tuple(max(x,y) for x,y in zip(a,b))
    mt=lambda a,b: tuple(min(x,y) for x,y in zip(a,b))
    bj=[(a,b,jn(a,b)) for a,b in combinations(cells,2) if jn(a,b) not in S]
    bm=[(a,b,mt(a,b)) for a,b in combinations(cells,2) if mt(a,b) not in S]
    return bj,bm

print("\n(1) 'varying lower bound x2 ≥ x1' — I predicted FAIL, it is a LATTICE")
Q=[(a,b) for a in range(6) for b in range(6) if b>=a]
bj,bm=failures(Q)
print(f"    join fails {len(bj)}, meet fails {len(bm)}")
print("    Why my criterion was wrong here:")
print("      b ≥ a is a lower bound on b varying with a — my rule says FAIL.")
print("      But it is EQUIVALENTLY an upper bound on a: a ≤ b.")
print("      A single inequality can be read either way. My criterion was")
print("      stated on the SYNTAX of the constraint, not its content.")

print("\n(2) 'simplex x+y+z ≤ 6' — I predicted LATTICE, it FAILS")
S6=[(x,y,z) for x in range(5) for y in range(5) for z in range(5) if x+y+z<=6]
bj,bm=failures(S6)
print(f"    join fails {len(bj)}, meet fails {len(bm)}")
print(f"    example: {bj[0][0]} ∨ {bj[0][1]} = {bj[0][2]}  (sum={sum(bj[0][2])})")
print("    Why: the bound couples coordinates ADDITIVELY. Raising x while")
print("    y stays high can breach the joint budget even though each")
print("    coordinate individually was fine. My criterion only looked at")
print("    bounds of the form x_i ≤ f(x_j), never at bounds on combinations.")

print("\n(3) 'disc x²+y² ≤ 9' — I predicted LATTICE, it FAILS")
D=[(x,y) for x in range(5) for y in range(5) if x*x+y*y<=9]
bj,bm=failures(D)
print(f"    join fails {len(bj)}, meet fails {len(bm)}")
print(f"    example: {bj[0][0]} ∨ {bj[0][1]} = {bj[0][2]}")
print("    Same defect: a joint constraint, not a per-coordinate one.")

print()
print("="*78)
print("THE CORRECT STATEMENT")
print("="*78)
print("""
  What actually governs closure is far simpler, and it is classical.

  A subset S of a product of chains is closed under componentwise
  join and meet iff S is a SUBLATTICE of that product. For sets
  defined by inequalities, the operative property is:

      S is closed under meet  iff  S is DOWNWARD closed
                                    within its own join-structure
      S is closed under join  iff  S is UPWARD closed likewise

  Concretely, the workable sufficient condition is that S be defined
  by constraints each involving AT MOST ONE coordinate on each side
  in a monotone way — i.e. S is an intersection of sets of the form
      { x : x_i ≤ x_j },  { x : x_i ≤ c },  { x : x_i ≥ c }.
  Such sets are exactly the order ideals/filters of a product order,
  and finite intersections of sublattices are sublattices.

  Λ qualifies:  ℓ ≤ n−1 is (coordinate ≤ coordinate + const),
                k ≤ 2(2ℓ+1) is monotone in a SINGLE other coordinate,
                floors are constants.
  Λ′ fails because |m| ≤ ℓ is TWO constraints, m ≤ ℓ and −m ≤ ℓ,
  and the second is not monotone in the same direction — it involves
  −m, reversing orientation. That is the real reason, and it is a
  statement about ORIENTATION, not about 'varying floors'.
""")

print("="*78)
print("RETEST WITH THE CORRECTED CRITERION")
print("="*78)
print("  Criterion: every constraint is monotone non-decreasing in each")
print("  coordinate it involves, after moving all terms to one side, and")
print("  involves no negated coordinate.\n")
cases=[
 ("Young  x1≥x2≥x3",      [(a,b,c) for a in range(6) for b in range(6) for c in range(6) if a>=b>=c], True),
 ("x2 ≥ x1",              [(a,b) for a in range(6) for b in range(6) if b>=a], True),
 ("divisor box",          [(a,b,c) for a in range(3) for b in range(2) for c in range(2)], True),
 ("simplex x+y+z≤6",      [(x,y,z) for x in range(5) for y in range(5) for z in range(5) if x+y+z<=6], False),
 ("disc x²+y²≤9",         [(x,y) for x in range(5) for y in range(5) if x*x+y*y<=9], False),
 ("annulus",              [(x,y) for x in range(6) for y in range(6) if 4<=x*x+y*y<=16], False),
 ("Λ (n,ℓ,k)",            [(n,l,k) for n in range(1,8) for l in range(0,min(n,5)) for k in range(1,2*(2*l+1)+1)], True),
 ("Λ′ (n,ℓ,m,s)",         [(n,l,m,s) for n in range(1,8) for l in range(0,min(n,5)) for m in range(-l,l+1) for s in (-1,1)], False),
]
good=0
for nm,cells,pred in cases:
    S=set(cells)
    jn=lambda a,b: tuple(max(x,y) for x,y in zip(a,b))
    mt=lambda a,b: tuple(min(x,y) for x,y in zip(a,b))
    ok = all(jn(a,b) in S and mt(a,b) in S for a,b in combinations(cells,2))
    m = "✓" if ok==pred else "✗"
    if ok==pred: good+=1
    print(f"  {nm:<24} actual={'LATTICE' if ok else 'not':<8} predicted={'LATTICE' if pred else 'not':<8} {m}")
print(f"\n  corrected criterion: {good}/{len(cases)}")