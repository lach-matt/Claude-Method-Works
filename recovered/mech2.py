from itertools import combinations
def jn(a,b): return tuple(max(x,y) for x,y in zip(a,b))
def mt(a,b): return tuple(min(x,y) for x,y in zip(a,b))
def test(name,S):
    Ss=set(S); jf=mf=0
    for a,b in combinations(S,2):
        if jn(a,b) not in Ss: jf+=1
        if mt(a,b) not in Ss: mf+=1
    print(f"  {name:<46} |S|={len(S):>4}  join {jf:>5}  meet {mf:>5}")

print("ISOLATING THE FLOOR'S TWO DEPENDENCIES\n")
# (a) floor depends on k ONLY, non-decreasing in k
S=[(k,m) for k in range(1,13) for m in range(max(0,k-5), k//2+1)]
test("m >= max(0,k-5), ceiling k//2   [k only]", S)
# (b) floor depends on l too, decreasing in l  (the real bound)
S=[(l,k,m) for l in range(0,4) for k in range(1,2*(2*l+1)+1)
           for m in range(max(0,k-(2*l+1)), k//2+1)]
test("m >= max(0,k-(2l+1))            [k and l]", S)
# (c) same but with the l-dependence frozen at its max
S=[(l,k,m) for l in range(0,4) for k in range(1,2*(2*l+1)+1)
           for m in range(max(0,k-7), k//2+1)]
test("m >= max(0,k-7)  (l-term frozen)          ", S)

print("\nTHE OTHER NAMED CULPRIT: 2Jc <= k-q  (decreasing in q)\n")
S=[(k,q,J) for k in range(0,9) for q in range(0,k+1) for J in range(0,k-q+1)]
test("2Jc <= k-q                                ", S)