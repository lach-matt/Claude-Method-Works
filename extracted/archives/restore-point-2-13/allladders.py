import sys; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
print("  EVERY LADDER THAT CAN EXIST  —  one per electron count where a\n")
print("  subshell crossing is possible.\n")
print("      a ladder is: fixed Nₑ, charges c = 1,2,3,4, i.e. the four species")
print("      Z = Nₑ, Nₑ+1, Nₑ+2, Nₑ+3.  it constrains a(period,block,c) only if")
print("      TWO subshells are in genuine competition at that Nₑ.\n")
EL={n:G.GROUND[n][0] for n in G.GROUND}
# a crossing is possible where the neutral's outermost subshell is s or p and a
# lower-n higher-l subshell is empty or partly filled
ROWS=[]
for ne in range(4,105):
    cfg=G.expand(ne)
    n_,l_,o_=cfg[-1]
    # is there an empty/partial subshell with lower n and higher l?
    have={(n,l):o for n,l,o in cfg}
    riv=[]
    for l in range(l_+1,5):
        for n in range(l+1,n_+1):
            if have.get((n,l),0)<2*(2*l+1): riv.append((n,l)); break
    if not riv: continue
    per=1+sum(1 for b in (2,10,18,36,54,86) if ne>b)
    sp=[f"{EL.get(ne+i,'?')} {'I II III IV'.split()[i]}" for i in range(4) if ne+i<=104]
    ROWS.append((ne,per,f"{n_}{L[l_]}{o_}",
                 " / ".join(f"{n}{L[l]}" for n,l in riv[:2]), sp))
print(f"      {'Nₑ':>4}{'per':>4}{'outermost':>11}{'rivals':>12}   the four species")
for ne,per,out,riv,sp in ROWS:
    print(f"      {ne:>4}{per:>4}{out:>11}{riv:>12}   {', '.join(sp)}")
print(f"\n      {len(ROWS)} possible ladders\n")
print("  THE ONES THAT MATTER MOST — closed-shell neutrals, s² outermost\n")
KEY=[r for r in ROWS if r[2].endswith("2") and r[2][1]=="s"]
print(f"      {'Nₑ':>4}{'per':>4}{'rivals':>12}   species")
for ne,per,out,riv,sp in KEY:
    print(f"      {ne:>4}{per:>4}{riv:>12}   {', '.join(sp)}")
print(f"\n      {len(KEY)} closed-s ladders — these give the cleanest brackets")
print("      because the neutral is ¹S₀ and the competition is unambiguous.")
print()
print("  ALREADY HELD : Nₑ = 20, 38, 56, 88")
print("  STILL NEEDED : " + ", ".join(str(r[0]) for r in KEY if r[0] not in (20,38,56,88)))
