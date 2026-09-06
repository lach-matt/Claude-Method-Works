# gate95.py -- scores PREDICTION-OVERSHOOT.md (sha 561239ae02c5de53, filed 15:18:24Z).
# Sealed nlchain.jsonl only. Sign convention taken from the prediction, stated literally.
import json,sys
L="spdfghi"; nl=lambda c:int(c[0])+L.index(c[1])
CF=int(sys.argv[sys.argv.index("--canfail")+1]) if "--canfail" in sys.argv else 0
rows={x["Z"]:x for x in (json.loads(l) for l in open("nlchain.jsonl"))}
def look(Z,fch):
    r=rows[Z]; S=nl(fch); od=list(r["order"])
    if CF==1 and Z==58: od=[[k,(v*0.2 if k=="4f" else v)] for k,v in od]   # un-collapse 4f
    shell=sorted([(k,v) for k,v in od if nl(k)==S],key=lambda t:t[1])
    d={k:v for k,v in od}
    rank=[k for k,_ in shell].index(fch)+1
    best_other=[v for k,v in shell if k!=fch][0]
    return dict(Z=Z,ent=r["ent"],S=S,rank=rank,n=len(shell),Df=d[fch],
                best_other=best_other,shell=shell,
                gap=d[fch]-best_other)   # <0 means f is AHEAD by |gap|
A={Z:look(Z,"4f") for Z in (57,58)}
B={Z:look(Z,"5f") for Z in (89,90,91)}
short=lambda x: max(0.0, x["gap"]);  surp=lambda x: max(0.0,-x["gap"])
if CF==3: B[90]["gap"]=-9.0
print("  Z    f    rank/shell   D(f)      best rival in shell     gap (+ = f behind)")
for x in list(A.values())+list(B.values()):
    f="4f" if x in A.values() else "5f"
    rv=[k for k,v in x["shell"] if k!=f][0]
    print(f"  {x['Z']:<4} {f}   {x['rank']} of {x['n']}     {x['Df']:>9.5f}   {rv} {x['best_other']:>9.5f}   {x['gap']:>+9.5f}   ent={x['ent']}")
sw4=short(A[57])+surp(A[58]); sw5=short(B[90])+surp(B[91])
V=[]
V.append(("OV-1 4f rank 3->1 across 57->58", A[57]["rank"]==3 and A[58]["rank"]==1, f"{A[57]['rank']}->{A[58]['rank']}"))
V.append(("OV-2 5f rank 4 at 89, <=2 at 90, 1 at 91", B[89]["rank"]==4 and B[90]["rank"]<=2 and B[91]["rank"]==1, f"{B[89]['rank']},{B[90]['rank']},{B[91]['rank']}"))
V.append(("OV-3 swing(4f) > 2 x shortfall(57)", sw4>2*short(A[57]), f"swing {sw4:.5f} vs 2x{short(A[57]):.5f}={2*short(A[57]):.5f}"))
V.append(("OV-4 swing(5f) > 2 x shortfall(90)", sw5>2*short(B[90]), f"swing {sw5:.5f} vs 2x{short(B[90]):.5f}={2*short(B[90]):.5f}"))
V.append(("OV-5 shortfall(90) < shortfall(89)", short(B[90])<short(B[89]), f"{short(B[90]):.5f} < {short(B[89]):.5f}"))
V.append(("OV-6 f wins against SAME n+l at 58 and 91", nl(A[58]['ent'])==7 and nl(B[91]['ent'])==8 and A[58]['ent']=="4f" and B[91]['ent']=="5f", f"ent58={A[58]['ent']}(n+l={nl(A[58]['ent'])}) ent91={B[91]['ent']}(n+l={nl(B[91]['ent'])})"))
np=sum(1 for _,o,_ in V if o)
print(f"\nGATE 95 -- PREDICTION-OVERSHOOT  {np}/{len(V)}"+(f"   [CANFAIL {CF}]" if CF else ""))
for n_,o,note in V: print(f"   {'PASS' if o else 'FAIL'}  {n_:<42} {note}")
print(f"\n  shortfall(57)={short(A[57]):.5f}  surplus(58)={surp(A[58]):.5f}  SWING={sw4:.5f}  ratio={sw4/short(A[57]):.2f}x")
print(f"  shortfall(90)={short(B[90]):.5f}  surplus(91)={surp(B[91]):.5f}  SWING={sw5:.5f}  ratio={sw5/short(B[90]):.2f}x")
print(f"  shortfall(89)={short(B[89]):.5f}  (plateau atom)")