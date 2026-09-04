"""circ.py -- SESSION 65, FIRST ACT. Read-only probe of the s65 work-list item 1.

QUESTION IT ASKS, AND NOTHING ELSE:
  Is the ratio measure `a` at base (n,l) an INDEPENDENT predictor of which member of
  the equal-n+l pair {A=(n,l+1), B=(n+1,l)} the field puts first, or is it an
  ALGEBRAIC RESTATEMENT of that comparison at the same Z?
  If the latter, FINDING-ALPHA §6's test T-B cannot fail and must not be run as filed.

  a = [D(n,l+1) - D(n,l)] / [D(n+1,l) - D(n,l)] = num/den
  If den > 0:  a < 1  <=>  D(A) < D(B)  <=>  A is deeper AT THAT Z.
  If den < 0:  the inequality reverses. Count both cases; nothing is assumed.

No solves. Sealed chain only. No file is edited.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
CHAIN = os.path.join(HERE, '..', 'rt', 'nlchain.jsonl')
T = lambda n, l: f"{n}{'spdfg'[l]}"
rows = {json.loads(l)['Z']: json.loads(l) for l in open(CHAIN)}

tot = same = flip = negden = 0
for Z in sorted(rows):
    if Z < 3: continue
    D = dict(rows[Z]['order'])
    for n in range(2, 8):
        for l in range(0, 3):
            a, A, B = T(n, l), T(n, l + 1), T(n + 1, l)
            if not (a in D and A in D and B in D): continue
            den = D[B] - D[a]
            if abs(den) <= 1e-4: continue
            val = (D[A] - D[a]) / den
            tot += 1
            if den < 0: negden += 1
            deeper_A = D[A] < D[B]
            if (val < 1) == deeper_A: same += 1
            else: flip += 1

print(f"  measurements                     {tot}")
print(f"  denominator negative             {negden}")
print(f"  (a<1) equals (A deeper at same Z) {same}")
print(f"  disagreements                    {flip}")
print()
print("  VERDICT:", "IDENTICAL -- a is a restatement, T-B as filed cannot fail."
      if flip == 0 else "NOT identical -- a carries content beyond the pair comparison.")