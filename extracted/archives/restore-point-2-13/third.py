import sys, math; sys.path.insert(0,"/home/claude/work")
import ground as G
L="spdfg"
R=13.605693122994   # Rydberg in eV
def cap(l): return 2*(2*l+1)
# ionisation energies of the neutrals, eV, from the same GSIE fetch
IE={1:13.598434599702,2:24.587389011,3:5.391714996,4:9.322699,5:8.298019,
6:11.2602880,7:14.53413,8:13.618055,9:17.42282,10:21.564541,11:5.13907696,
12:7.646236,13:5.985769,14:8.15168,15:10.486686,16:10.3600167,17:12.967633,
18:15.7596119,19:4.34066373,20:6.1131549210,21:6.56149,22:6.828120,23:6.746187,
24:6.76651,25:7.4340380,26:7.9024681,27:7.88101,28:7.639878,29:7.726380,
30:9.394197,31:5.9993020,32:7.899435,33:9.78855,34:9.752368,35:11.81381,
36:13.9996055,37:4.1771281,38:5.69486745,39:6.21726,40:6.634126,41:6.75885,
42:7.09243,43:7.11938,44:7.36050,45:7.45890,46:8.336839,47:7.576234,
48:8.993820,49:5.7863558,50:7.343918,51:8.608389,52:9.009808,53:10.451236,
54:12.1298437,55:3.89390572743,56:5.2116646,57:5.5769,58:5.5386,
70:6.254160,71:5.425871,72:6.825070,80:10.437504,81:6.1082873,
86:10.74850,87:4.0727411,88:5.2784239,89:5.380235,90:6.30670,102:6.62621}
def bracket(Z):
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
    gp=gn-gl-1; lo,hi=-1e9,1e9
    for n,l in cand:
        if (n,l)==(gn,gl): continue
        d=math.sqrt(n-l-1)-math.sqrt(gp); r=n-gn
        if abs(d)<1e-12: continue
        if d>0: hi=min(hi,r/d)
        else:   lo=max(lo,r/d)
    return lo,hi,gn,gl,gp
print("  THE THIRD COORDINATE  —  a from the ionisation energy\n")
print("      ν = c√(R/IE) with c = 1;  a = (n − ν)/√p\n")
print(f"      {'Z':>4}{'el':>4}{'fills':>7}{'IE':>10}{'ν':>9}{'a_meas':>9}"
      f"{'L':>9}{'U':>9}{'  in?'}")
inn=out=0; OUT=[]
for Z in sorted(IE):
    if Z<3: continue
    b=bracket(Z)
    if b is None: continue
    lo,hi,gn,gl,gp=b
    if gp<1: continue
    nu=math.sqrt(R/IE[Z]); am=(gn-nu)/math.sqrt(gp)
    ok = lo<am<hi
    inn+=ok; out+=(not ok)
    if not ok: OUT.append((Z,am,lo,hi))
    if Z in (3,11,19,20,21,30,37,38,39,48,55,56,57,70,71,80,87,88,89,102) or not ok:
        print(f"      {Z:>4}{G.GROUND[Z][0]:>4}{f'{gn}{L[gl]}':>7}{IE[Z]:>10.4f}"
              f"{nu:>9.4f}{am:>9.4f}"
              f"{(lo if lo>-1e8 else float('-inf')):>9.3f}"
              f"{(hi if hi<1e8 else float('inf')):>9.3f}   {'YES' if ok else 'NO'}")
print()
print(f"      inside the corridor : {inn}")
print(f"      outside             : {out}")
print(f"      total tested        : {inn+out}\n")
if OUT:
    print("      outside at:")
    for Z,am,lo,hi in OUT[:20]:
        print(f"          Z={Z:>3} {G.GROUND[Z][0]:>3}  a={am:.4f}  "
              f"({lo if lo>-1e8 else float('-inf'):.3f}, {hi if hi<1e8 else float('inf'):.3f})")
