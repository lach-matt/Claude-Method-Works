"""circ2.py -- SESSION 65. The second half of the circularity probe.

T-B asks: at Zo = min(first[A], first[B]), does (a < 1) match "A enters first"?
circ.py showed (a<1) == "A deeper at that Z". This asks whether "A deeper at Zo"
is ITSELF forced to equal "A enters first" by the definition of Zo.
The entrant at any Z is the argmin over available channels. At Zo one of A,B enters
by construction, so that one is the argmin, so it is deeper than the other.
If that holds at every block, T-B has no falsifier available to it.
No solves. Sealed chain only.
"""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
rows = {json.loads(l)['Z']: json.loads(l) for l in open(os.path.join(HERE,'..','rt','nlchain.jsonl'))}
T = lambda n, l: f"{n}{'spdfg'[l]}"

first = {}
for Z in sorted(rows):
    t = T(*rows[Z]['ent_nl'])
    if t not in first: first[t] = Z

print("  blk  A(low n) B      Zopen  ent   A_first  A_deeper@Zo  forced?")
nblk = forced = 0
for N in range(3, 9):
    for l in range(0, 4):
        n = N - l
        if n < l + 2: continue
        A, B = T(n, l + 1), T(n + 1, l)
        if A not in first or B not in first: continue
        Afirst = first[A] < first[B]
        Zo = min(first[A], first[B])
        D = dict(rows[Zo]['order'])
        if A not in D or B not in D:
            print(f"   {N}   {A:>3}   {B:>3}   {Zo:>4}  {rows[Zo]['ent']:>4}  pair not both available")
            continue
        deeper = D[A] < D[B]
        nblk += 1
        ok = (deeper == Afirst)
        forced += ok
        print(f"   {N}   {A:>3}   {B:>3}   {Zo:>4}  {rows[Zo]['ent']:>4}   {str(Afirst):>5}    {str(deeper):>5}"
              f"       {'YES' if ok else 'no'}")
print(f"\n  blocks {nblk}   'A first' == 'A deeper at Zopen' at {forced}/{nblk}")