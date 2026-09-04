import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
print("  THE LAW WITH NO STATE AT ALL\n")
print("      if a is always the crossing value of the ACTIVE pair, then a is")
print("      not carried between steps. it is computed at each step from the")
print("      configuration alone — and the walk needs no memory.\n")
print("      but 'the active pair' must be defined WITHOUT knowing the answer.")
print("      the only candidates at step Z are the admissible subshells.")
print("      the active pair is the two with the LEAST ν — which requires a.\n")
print("      → circular unless resolved. testing the fixed point:\n")
print("      for each ordered pair (g,r) of admissible subshells, set")
print("      a = a_cross(g,r) and ask whether g is then the least-ν subshell.")
print("      a pair is CONSISTENT if it is; the law picks a consistent one.\n")
def run():
    ok=bad=amb=0; BAD=[]; AMB=[]
    for Z in range(3,109):
        pr={(n,l):o for n,l,o in G.expand(Z-1)}
        cu={(n,l):o for n,l,o in G.expand(Z)}
        got=[k for k in cu if cu[k]>pr.get(k,0)]
        if len(got)!=1: continue
        got=got[0]; cand=[]
        for l in range(5):
            for n in range(l+1,9):
                if pr.get((n,l),0)>=cap(l): continue
                cand.append((n,l))
                if pr.get((n,l),0)==0: break
        if len(cand)<2 or got not in cand: continue
        cons=set()
        for gi,(gn,gl) in enumerate(cand):
            gp=gn-gl-1
            for ri,(rn,rl) in enumerate(cand):
                if ri==gi: continue
                rp=rn-rl-1
                d=math.sqrt(rp)-math.sqrt(gp)
                if abs(d)<1e-12: continue
                av=(rn-gn)/d
                if av<0: continue
                # at a just inside, is g the least?
                eps=1e-7
                for sgn in (-eps,+eps):
                    aa=av+sgn
                    if aa<0: continue
                    vals=[(n-aa*math.sqrt(n-l-1),n,l) for n,l in cand]
                    m=min(vals)
                    if (m[1],m[2])==(gn,gl): cons.add((gn,gl))
        if len(cons)==1:
            if got in cons: ok+=1
            else: bad+=1; BAD.append((Z,got,list(cons)[0]))
        else:
            amb+=1; AMB.append((Z,got,sorted(cons)))
    return ok,bad,amb,BAD,AMB
ok,bad,amb,BAD,AMB=run()
print(f"      unique consistent subshell, and correct : {ok}")
print(f"      unique consistent subshell, and wrong   : {bad}")
print(f"      more than one consistent                : {amb}")
print(f"      total steps                             : {ok+bad+amb}\n")
if BAD:
    print("      wrong at:")
    for Z,g,c in BAD[:10]:
        print(f"          Z={Z:>3} {G.GROUND[Z][0]:>3} observed {g[0]}{L[g[1]]}"
              f"  predicted {c[0]}{L[c[1]]}")
print()
if AMB:
    from collections import Counter
    print(f"      ambiguous at {len(AMB)} steps · sizes: "
          f"{dict(Counter(len(c) for _,_,c in AMB))}")
    print("      first few:")
    for Z,g,c in AMB[:8]:
        print(f"          Z={Z:>3} {G.GROUND[Z][0]:>3} observed {g[0]}{L[g[1]]}"
              f"  consistent: {[f'{n}{L[l]}' for n,l in c]}")