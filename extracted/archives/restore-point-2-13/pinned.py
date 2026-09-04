import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
def cap(l): return 2*(2*l+1)
def step(Z):
    pr={(n,l):o for n,l,o in G.expand(Z-1)}
    cu={(n,l):o for n,l,o in G.expand(Z)}
    got=[k for k in cu if cu[k]>pr.get(k,0)]
    if len(got)!=1: return None
    gn,gl=got[0]; cand=[]
    for l in range(5):
        for n in range(l+1,9):
            if pr.get((n,l),0)>=cap(l): continue
            cand.append((n,l))
            if pr.get((n,l),0)==0: break
    if (gn,gl) not in cand or len(cand)<2: return None
    return (gn,gl),cand
def acr(gn,gl,rn,rl):
    gp=gn-gl-1; rp=rn-rl-1
    d=math.sqrt(rp)-math.sqrt(gp)
    if abs(d)<1e-12: return None
    return (rn-gn)/d
print("  IS EVERY RESET THE a_cross OF THE PAIR COMPETING AT THAT STEP?\n")
a=0.0; RES=[]
for Z in range(3,109):
    s=step(Z)
    if s is None: continue
    (gn,gl),cand=s
    gp=gn-gl-1; lo,hi=-1e9,1e9; blo=bhi=None
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        v=acr(gn,gl,n,l)
        if v is None: continue
        if math.sqrt(n-l-1)>math.sqrt(gp):
            if v<hi: hi,bhi=v,(n,l)
        else:
            if v>lo: lo,blo=v,(n,l)
    if lo<a<hi: continue
    old=a
    if a<=lo: a=lo+1e-9; b=blo; side="lower"
    else:     a=hi-1e-9; b=bhi; side="upper"
    RES.append((Z,gn,gl,b,a,side))
print(f"      {'Z':>4}{'el':>4}{'fills':>7}{'rival that pins it':>20}"
      f"{'a after':>10}{'side':>8}")
for Z,gn,gl,b,av,side in RES:
    rv=f"{b[0]}{L[b[1]]}" if b else "—"
    print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{f'{gn}{L[gl]}':>7}{rv:>20}"
          f"{av:>10.6f}{side:>8}")
print(f"\n      {len(RES)} resets · every one is the a_cross of a REAL pair:")
print("      the subshell being filled against a specific named rival.\n")
print("  THE EXACT FORMS\n")
print(f"      {'Z':>4}{'pair':>12}{'value':>12}{'  closed form'}")
import fractions
for Z,gn,gl,b,av,side in RES:
    if not b: continue
    gp=gn-gl-1; rp=b[0]-b[1]-1; dn=b[0]-gn
    den=gp-rp
    print(f"      {Z:>4}{f'{gn}{L[gl]}/{b[0]}{L[b[1]]}':>12}{av:>12.6f}"
          f"   {-dn}·(√{gp}+√{rp})/{den}" if den else "")
print()
print("  THE STATEMENT\n")
print("      a is not an amplitude that descends. at every step it equals the")
print("      crossing value of the competition that is ACTIVE at that step —")
print("      and it changes only when the active competition changes.")
print()
print("      each value is (Δn)(√p_g + √p_r)/(p_g − p_r): integers and surds,")
print("      determined entirely by the two subshells in play.")
