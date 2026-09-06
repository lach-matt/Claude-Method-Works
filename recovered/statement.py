import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
print("  THE STATEMENT\n")
print("      ν(n,ℓ) = n − a·√(n−ℓ−1)")
print("      the electron enters the Pauli-admissible subshell of least ν.")
print()
print("      a = a(Nₑ, c), and the ordering flips when a descends through")
print("          a_cross = (nᵣ−n_g)/(√pᵣ−√p_g)")
print()
print("      the charge at which it flips is set by n_f, the f-electron count")
print("      of the core:  n_f = 0 → c = 2,  14 → 3,  28 → 5.\n")
print("  PLUGGING IN — a(Nₑ) for NEUTRALS, from the six group-2 brackets\n")
# at c=1 every ladder gives a LOWER bound = its own a_cross
LB={20:0.5774,38:1.0000,56:1.2168,70:1.2168,88:1.3938,102:1.3938}
print("      at c = 1 each ladder requires a > a_cross, so a(Nₑ,1) exceeds:")
for ne in sorted(LB): print(f"          Nₑ = {ne:>3} : a > {LB[ne]:.4f}")
print()
print("      the TIGHTEST is Nₑ = 88 and 102 : a > 1.3938")
print("      so for every neutral, a > 1.3938 would satisfy all six.\n")
print("  TEST — run the generator with a = 1.40 constant for all neutrals\n")
def run(av):
    ok=bad=0; BAD=[]
    for Z in range(3,109):
        pr={(n,l):o for n,l,o in G.expand(Z-1)}
        cu={(n,l):o for n,l,o in G.expand(Z)}
        got=[k for k in cu if cu[k]>pr.get(k,0)]
        if len(got)!=1: continue
        got=got[0]; cand=[]
        for l in range(5):
            for n in range(l+1,9):
                if pr.get((n,l),0)>=cap(l): continue
                cand.append((n,l,n-av*math.sqrt(n-l-1)))
                if pr.get((n,l),0)==0: break
        if len(cand)<2 or got not in [(a,b) for a,b,_ in cand]: continue
        pick=min(cand,key=lambda x:x[2])
        if (pick[0],pick[1])==got: ok+=1
        else: bad+=1; BAD.append((Z,got,(pick[0],pick[1])))
    return ok,bad,BAD
for av in (0.58,0.60,1.00,1.20,1.39,1.40,1.50):
    ok,bad,_=run(av)
    print(f"      a = {av:.2f} : {ok}/{ok+bad} = {100*ok/(ok+bad):.1f}%")
print()
print("  THE CONTRADICTION\n")
print("      the six ladders require a > 1.3938 at c = 1.")
print("      the generator's best is at a ≈ 0.60, and a = 1.40 does far worse.")
print()
ok6,bad6,B6=run(0.60); ok14,bad14,B14=run(1.40)
print(f"      a = 0.60 : {ok6}/{ok6+bad6}      a = 1.40 : {ok14}/{ok14+bad14}")
print()
print("      → the LADDER brackets and the FILLING generator disagree about a.")
print("        both are derived from the same observed configurations.")
print()
print("  WHERE THEY DISAGREE\n")
s6={Z for Z,_,_ in B6}; s14={Z for Z,_,_ in B14}
print(f"      fails at a=0.60 only : {sorted(s6-s14)[:16]}")
print(f"      fails at a=1.40 only : {sorted(s14-s6)[:16]}")
print(f"      fails at both        : {sorted(s6&s14)[:16]}")